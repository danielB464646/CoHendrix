from fractions import Fraction
from typing import Annotated, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

Channel = Annotated[int, Field(ge=1, le=16)]
MidiValue = Annotated[int, Field(ge=0, le=127)]


class ScoreModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)


class MusicalTime(ScoreModel):
    """Exact nonnegative position in MIDI quarter notes, independent of source PPQ."""

    numerator: int = Field(ge=0)
    denominator: int = Field(gt=0)

    @classmethod
    def from_fraction(cls, value: Fraction) -> Self:
        return cls(numerator=value.numerator, denominator=value.denominator)

    def fraction(self) -> Fraction:
        return Fraction(self.numerator, self.denominator)


class TimeSignature(ScoreModel):
    numerator: int = Field(ge=1, le=255)
    denominator: int = Field(gt=0)

    @model_validator(mode="after")
    def validate_denominator(self) -> Self:
        if self.denominator & (self.denominator - 1):
            raise ValueError("Time signature denominator must be a power of two")
        return self

    def bar_length(self) -> Fraction:
        return Fraction(self.numerator * 4, self.denominator)


class Track(ScoreModel):
    id: str = Field(min_length=1)
    name: str
    source_track: int = Field(ge=0)
    channel: Channel
    is_drum: bool


class Note(ScoreModel):
    id: str = Field(min_length=1)
    track_id: str
    pitch: MidiValue
    velocity: int = Field(ge=1, le=127)
    start: MusicalTime
    end: MusicalTime
    on_index: int = Field(ge=0)
    off_index: int = Field(gt=0)
    release_velocity: MidiValue
    release_as_note_on: bool

    @model_validator(mode="after")
    def validate_end(self) -> Self:
        if self.end.fraction() < self.start.fraction() or self.off_index <= self.on_index:
            raise ValueError("Note release precedes its onset")
        if self.release_as_note_on and self.release_velocity:
            raise ValueError("A note-on release must have velocity zero")
        return self


class LocatedEvent(ScoreModel):
    source_track: int = Field(ge=0)
    event_index: int = Field(ge=0)
    time: MusicalTime


class TempoEvent(LocatedEvent):
    microseconds_per_quarter: int = Field(ge=1, le=0xFFFFFF)


class MidiEvent(LocatedEvent):
    type: str = Field(min_length=1)
    message_hex: str = Field(pattern="^(?:[0-9a-f]{2})+$")


class Score(ScoreModel):
    """The shared, provisional Score contract for an imported MIDI sketch."""

    midi_type: Literal[0, 1]
    source_track_count: int = Field(ge=1)
    time_signature: TimeSignature
    duration: MusicalTime
    tracks: list[Track]
    notes: list[Note]
    tempo_events: list[TempoEvent]
    midi_events: list[MidiEvent]
    bar_count: int = Field(ge=1)

    @staticmethod
    def count_bars(time_signature: TimeSignature, duration: MusicalTime, notes: list[Note]) -> int:
        length = time_signature.bar_length()
        # A note ending on a boundary does not occupy the following bar.
        return max(
            1,
            -(-duration.fraction() // length),
            max((note.start.fraction() // length + 1 for note in notes), default=0),
        )

    @model_validator(mode="after")
    def validate_references(self) -> Self:
        if self.midi_type == 0 and self.source_track_count != 1:
            raise ValueError("Type 0 MIDI must have exactly one source track")
        tracks = {track.id: track for track in self.tracks}
        sources = {(track.source_track, track.channel) for track in self.tracks}
        if len(tracks) != len(self.tracks) or len(sources) != len(self.tracks):
            raise ValueError("Track IDs and source track/channel pairs must be unique")
        if any(track.source_track >= self.source_track_count for track in self.tracks):
            raise ValueError("Track references a nonexistent source track")
        if len({note.id for note in self.notes}) != len(self.notes):
            raise ValueError("Note IDs must be unique")
        duration = self.duration.fraction()
        positions: set[tuple[int, int]] = set()

        def add_position(source: int, index: int) -> None:
            if (source, index) in positions:
                raise ValueError("Duplicate event index in a source track")
            positions.add((source, index))

        for note in self.notes:
            if note.track_id not in tracks or note.end.fraction() > duration:
                raise ValueError("Note references a nonexistent track or ends after the score")
            source = tracks[note.track_id].source_track
            add_position(source, note.on_index)
            add_position(source, note.off_index)
        for event in (*self.tempo_events, *self.midi_events):
            if event.source_track >= self.source_track_count or event.time.fraction() > duration:
                raise ValueError("Event references a nonexistent track or occurs after the score")
            add_position(event.source_track, event.event_index)
        if self.bar_count != self.count_bars(self.time_signature, self.duration, self.notes):
            raise ValueError("Bar count does not match the score's meter and duration")
        return self
