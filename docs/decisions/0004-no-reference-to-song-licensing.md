# ADR 0004: The requirements do not refer to song licensing

Supersedes "licensed" in the reference-library line of [ADR 0001](0001-v1-scope-after-requirements-review.md) ("The reference library is 1–10 licensed files").

## Context

The review deck's FR9 read "between 1 and 10 licensed reference MIDI files", and ADR 0001 repeated "licensed". The word was never defined, and the system does not check licences.

## Options

1. Keep "licensed" as on the deck.
2. Keep "licensed" and define it as the producer's responsibility.
3. Drop it and not refer to song licensing.

## Decision

The ARD does not refer to song licensing. FR9 reads "The system shall accept between 1 and 10 reference MIDI files." and is marked "Review (shortened)". The limit of 1–10 files stays.

## Why

The team does not want the requirements to deal with song licensing. Dropping an undefined word keeps FR9 testable. The Chapter 3 intro says FR9 was shortened, so the claim that FR1–FR14 keep their wording stays true.
