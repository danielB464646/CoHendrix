from fractions import Fraction
from io import BytesIO

import mido
import pytest

from cohendrix.midi_import import MidiImportError, import_midi


def midi_bytes(midi: mido.MidiFile) -> bytes:
    output = BytesIO()
    midi.save(file=output)
    return output.getvalue()


def drums_example() -> bytes:
    midi = mido.MidiFile(type=0, ticks_per_beat=480)
    track = midi.add_track("Sketch")
    track.extend(
        [
            mido.MetaMessage("set_tempo", tempo=600_000),
            mido.Message("program_change", channel=0, program=12),
            mido.Message("control_change", channel=0, control=64, value=127),
            mido.Message("note_on", channel=0, note=60, velocity=80),
            mido.Message("note_on", channel=9, note=36, velocity=100),
            mido.Message("pitchwheel", channel=0, pitch=-500, time=120),
            mido.Message("note_off", channel=9, note=36, velocity=40, time=120),
            mido.Message("note_on", channel=0, note=60, velocity=0, time=240),
            mido.MetaMessage("set_tempo", tempo=400_000, time=480),
            mido.MetaMessage("end_of_track", time=960),
        ]
    )
    return midi_bytes(midi)


def crossing_example(ppq: int = 480) -> bytes:
    midi = mido.MidiFile(type=1, ticks_per_beat=ppq)
    midi.add_track("Conductor").append(
        mido.MetaMessage("time_signature", numerator=6, denominator=8)
    )
    track = midi.add_track("Piano")
    track.extend(
        [
            mido.Message("note_on", note=60, velocity=80, time=5 * ppq // 2),
            mido.Message("note_on", note=60, velocity=90, time=ppq // 4),
            mido.Message("note_off", note=60, velocity=11, time=ppq // 2),
            mido.Message("note_off", note=60, velocity=22, time=ppq // 4),
        ]
    )
    return midi_bytes(midi)


def test_type_zero_splits_channels_and_preserves_non_note_messages() -> None:
    score = import_midi(drums_example())
    assert [(track.channel, track.is_drum) for track in score.tracks] == [(1, False), (10, True)]
    assert [
        (event.time.fraction(), event.microseconds_per_quarter) for event in score.tempo_events
    ] == [
        (Fraction(0), 600_000),
        (Fraction(2), 400_000),
    ]
    assert {event.type: event.message_hex for event in score.midi_events} == {
        "track_name": "ff0306536b65746368",
        "program_change": "c00c",
        "control_change": "b0407f",
        "pitchwheel": bytes(mido.Message("pitchwheel", pitch=-500).bytes()).hex(),
        "end_of_track": "ff2f00",
    }
    piano, drum = score.notes
    assert (piano.release_as_note_on, piano.release_velocity) == (True, 0)
    assert (drum.release_as_note_on, drum.release_velocity) == (False, 40)
    assert score.duration.fraction() == 4
    assert score.bar_count == 1


def test_type_one_normalizes_ppq_preserves_overlaps_and_crossing_notes() -> None:
    score = import_midi(crossing_example())
    assert score == import_midi(crossing_example(960))
    assert score.source_track_count == 2
    assert [track.name for track in score.tracks] == ["Piano"]
    assert score.time_signature.bar_length() == 3
    assert score.bar_count == 2
    first, second = score.notes
    assert first.id != second.id
    assert (first.start.fraction(), first.end.fraction(), first.release_velocity) == (
        Fraction(5, 2),
        Fraction(13, 4),
        11,
    )
    assert (second.start.fraction(), second.end.fraction(), second.release_velocity) == (
        Fraction(11, 4),
        Fraction(7, 2),
        22,
    )


def test_type_one_keeps_same_channel_separate_by_source_track() -> None:
    midi = mido.MidiFile(type=1)
    for name in ("Piano", "Bass"):
        track = midi.add_track(name)
        track.extend([mido.Message("note_on", note=60), mido.Message("note_off", note=60, time=1)])
    score = import_midi(midi_bytes(midi))
    assert [track.name for track in score.tracks] == ["Piano", "Bass"]
    assert [note.track_id for note in score.notes] == [track.id for track in score.tracks]
    assert len({note.id for note in score.notes}) == 2


def test_smpte_ticks_use_tempo_map_to_locate_bars() -> None:
    midi = mido.MidiFile(type=0, ticks_per_beat=-25 * 256 + 40)
    track = midi.add_track()
    track.extend(
        [
            mido.Message("note_on", note=64),
            mido.MetaMessage("set_tempo", tempo=250_000, time=500),
            mido.Message("note_off", note=64, time=250),
        ]
    )
    score = import_midi(midi_bytes(midi))
    assert score.tempo_events[0].time.fraction() == 1
    assert score.notes[0].end.fraction() == 2


def test_rejects_time_signature_change_but_accepts_restatement() -> None:
    midi = mido.MidiFile(type=0)
    track = midi.add_track()
    track.extend([mido.MetaMessage("time_signature"), mido.MetaMessage("time_signature", time=480)])
    assert import_midi(midi_bytes(midi)).bar_count == 1
    track.append(mido.MetaMessage("time_signature", numerator=3, time=480))
    with pytest.raises(MidiImportError, match="time signature changes"):
        import_midi(midi_bytes(midi))


@pytest.mark.parametrize(
    ("data", "reason"),
    [
        (b"RIFF\x00\x00\x00\x00WAVE", "Not a Standard MIDI File"),
        (b"MThd", "truncated MThd"),
        (drums_example()[:-1], "truncated MIDI track chunk"),
        (drums_example() + b"trailing", "Unexpected data"),
        (drums_example()[:9] + b"\x02" + drums_example()[10:], "type 2 is unsupported"),
    ],
)
def test_rejects_invalid_inputs(data: bytes, reason: str) -> None:
    with pytest.raises(MidiImportError, match=reason):
        import_midi(data)


def test_rejects_unterminated_note() -> None:
    midi = mido.MidiFile(type=0)
    midi.add_track().append(mido.Message("note_on"))
    with pytest.raises(MidiImportError, match="Unterminated note"):
        import_midi(midi_bytes(midi))
