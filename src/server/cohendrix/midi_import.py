from bisect import bisect_right
from collections import defaultdict, deque
from collections.abc import Callable
from dataclasses import dataclass
from fractions import Fraction
from io import BytesIO
from itertools import pairwise
from struct import Struct, error

import mido

from cohendrix.schemas.score import (
    MidiEvent,
    MusicalTime,
    Note,
    Score,
    TempoEvent,
    TimeSignature,
    Track,
)

_HEADER = Struct(">4sIHHh")
_CHUNK = Struct(">4sI")
_DEFAULT_TEMPO = 500_000


class MidiImportError(ValueError):
    """A MIDI file could not be represented as a Score; message is user-facing."""


@dataclass(frozen=True)
class _Onset:
    time: MusicalTime
    index: int
    velocity: int


def _validate_container(data: bytes) -> None:
    if not data.startswith(b"MThd") or len(data) < _HEADER.size:
        raise MidiImportError("Not a Standard MIDI File (missing or truncated MThd header)")
    _, header_size, kind, count, _ = _HEADER.unpack_from(data)
    if kind not in (0, 1):
        raise MidiImportError(f"MIDI type {kind} is unsupported; expected type 0 or 1")
    if count == 0 or (kind == 0 and count != 1):
        raise MidiImportError("Invalid MIDI track count")
    if header_size < 6 or header_size + 8 > len(data):
        raise MidiImportError("Invalid MIDI header length")
    position = header_size + 8
    for _ in range(count):
        if position + _CHUNK.size > len(data):
            raise MidiImportError("Truncated MIDI track header")
        tag, track_size = _CHUNK.unpack_from(data, position)
        position += _CHUNK.size + track_size
        if tag != b"MTrk" or position > len(data):
            raise MidiImportError("Invalid or truncated MIDI track chunk")
    if position != len(data):
        raise MidiImportError("Unexpected data after the declared MIDI tracks")


def _quarter_positions(midi: mido.MidiFile) -> Callable[[int], Fraction]:
    division: int = midi.ticks_per_beat
    if division > 0:
        return lambda tick: Fraction(tick, division)

    fps_code, ticks_per_frame = -(division >> 8), division & 0xFF
    if fps_code not in (24, 25, 29, 30) or ticks_per_frame == 0:
        raise MidiImportError("Invalid MIDI time division")
    fps = Fraction(30_000, 1001) if fps_code == 29 else Fraction(fps_code)
    microseconds_per_tick = Fraction(1_000_000) / (fps * ticks_per_frame)
    tempo_by_tick = {0: _DEFAULT_TEMPO}
    for track in midi.tracks:
        tick = 0
        for msg in track:
            tick += msg.time
            if msg.type == "set_tempo":
                if msg.tempo == 0:
                    raise MidiImportError("Invalid zero MIDI tempo")
                tempo_by_tick[tick] = msg.tempo

    ticks = sorted(tempo_by_tick)
    elapsed = Fraction(0)
    quarters = [elapsed]
    for left, right in pairwise(ticks):
        elapsed += (right - left) * microseconds_per_tick / tempo_by_tick[left]
        quarters.append(elapsed)

    def at(tick: int) -> Fraction:
        index = bisect_right(ticks, tick) - 1
        start = ticks[index]
        return quarters[index] + (tick - start) * microseconds_per_tick / tempo_by_tick[start]

    return at


def _to_score(midi: mido.MidiFile) -> Score:
    at = _quarter_positions(midi)
    tracks: list[Track] = []
    notes: list[Note] = []
    tempo_events: list[TempoEvent] = []
    midi_events: list[MidiEvent] = []
    signatures: dict[Fraction, TimeSignature] = {}
    last_tick = 0

    for source, track in enumerate(midi.tracks):
        if not track or track[-1].type != "end_of_track":
            raise MidiImportError(f"MIDI track {source + 1} is missing its end-of-track event")
        channels = sorted({msg.channel for msg in track if hasattr(msg, "channel")})
        track_ids = {channel: f"track-{source}-{channel + 1}" for channel in channels}
        title = track.name or f"Track {source + 1}"
        tracks.extend(
            Track(
                id=track_ids[channel],
                name=f"{title} (ch. {channel + 1})" if len(channels) > 1 else title,
                source_track=source,
                channel=channel + 1,
                is_drum=channel == 9,
            )
            for channel in channels
        )
        active: dict[tuple[int, int], deque[_Onset]] = defaultdict(deque)
        tick = 0
        for index, msg in enumerate(track):
            tick += msg.time
            time = MusicalTime.from_fraction(at(tick))
            if msg.type == "end_of_track" and index != len(track) - 1:
                raise MidiImportError(f"Unexpected events after end of MIDI track {source + 1}")
            if msg.type == "set_tempo":
                tempo_events.append(
                    TempoEvent(
                        source_track=source,
                        event_index=index,
                        time=time,
                        microseconds_per_quarter=msg.tempo,
                    )
                )
                continue
            if msg.type == "time_signature":
                signature = TimeSignature(numerator=msg.numerator, denominator=msg.denominator)
                position = time.fraction()
                if position in signatures and signatures[position] != signature:
                    raise MidiImportError(
                        "MIDI time signature changes or conflicts are unsupported"
                    )
                signatures[position] = signature
            if msg.type in ("note_on", "note_off"):
                key = (msg.channel, msg.note)
                if msg.type == "note_on" and msg.velocity > 0:
                    active[key].append(_Onset(time, index, msg.velocity))
                    continue
                if active[key]:
                    # SMF releases do not identify an onset; pair repeated pitches FIFO.
                    onset = active[key].popleft()
                    notes.append(
                        Note(
                            id=f"note-{source}-{onset.index}",
                            track_id=track_ids[msg.channel],
                            pitch=msg.note,
                            velocity=onset.velocity,
                            start=onset.time,
                            end=time,
                            on_index=onset.index,
                            off_index=index,
                            release_velocity=msg.velocity,
                            release_as_note_on=msg.type == "note_on",
                        )
                    )
                    continue
            midi_events.append(
                MidiEvent(
                    source_track=source,
                    event_index=index,
                    time=time,
                    type=msg.type,
                    message_hex=bytes(msg.bytes()).hex(),
                )
            )
        if any(active.values()):
            raise MidiImportError(f"Unterminated note in MIDI track {source + 1}")
        last_tick = max(last_tick, tick)

    meter = signatures.get(Fraction(0)) or TimeSignature(numerator=4, denominator=4)
    if any(signature != meter for signature in signatures.values()):
        raise MidiImportError("MIDI time signature changes are unsupported")

    source_by_id = {track.id: track.source_track for track in tracks}
    notes.sort(key=lambda note: (note.start.fraction(), source_by_id[note.track_id], note.on_index))
    tempo_events.sort(
        key=lambda event: (event.time.fraction(), event.source_track, event.event_index)
    )
    duration = MusicalTime.from_fraction(at(last_tick))
    return Score(
        midi_type=midi.type,
        source_track_count=len(midi.tracks),
        time_signature=meter,
        duration=duration,
        tracks=tracks,
        notes=notes,
        tempo_events=tempo_events,
        midi_events=midi_events,
        bar_count=Score.count_bars(meter, duration, notes),
    )


def import_midi(data: bytes) -> Score:
    """Read a type 0/1 Standard MIDI File; raise MidiImportError on rejected input."""
    _validate_container(data)
    try:
        midi = mido.MidiFile(file=BytesIO(data))
        return _to_score(midi)
    except MidiImportError:
        raise
    except (EOFError, OSError, ValueError, IndexError, error) as exc:
        raise MidiImportError(f"Invalid MIDI: {exc or 'truncated MIDI event'}") from exc
