# ADR 0006: Rules are suggested from the sketch; reference songs are style context for the LLM

## Context

The review deck said FR10 extracts key, pitch range and rhythm grid "from the provided MIDI", and listed reference MIDI files as "Protected: only features stored", never sent to the LLM as notes. The ARD draft read this as extraction from the reference files. The team clarified that "the provided MIDI" is the producer's sketch, and that reference songs carry the producer's taste.

## Options

1. Suggest rules from the reference files only.
2. Suggest rules from the sketch and from the reference files.
3. Suggest rules from the sketch only; reference files are style context for the LLM.

## Decision

Option 3. FR10 keeps its review wording; "the provided MIDI" is the sketch. For the key, when the tracks of the sketch agree on a common key, the system suggests that key; when they do not, it suggests its 3 most likely keys, ranked, and the producer picks one. In both cases the producer may enter a different key. Reference files (1–10, FR9) are optional, are not a source of rules, and are sent to the LLM as examples of the style the producer is after. They are stored with their chat window and deleted with it (NFR11). On a track with no notes, a range rule can only come from a stated constraint. The ARD still does not claim that the system learns the producer's taste.

## Why

Rules describe the producer's own sketch, which is what the patch must fit. Songs the producer likes are better used as examples for the generator than as hard rules. The tradeoff: reference songs now leave the system to the selected LLM provider, which reverses the review's privacy row (see the note on NFR11 in the ARD).
