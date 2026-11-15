# ADR 0001: v1 scope after the requirements review

## Context

Proposal v2 (7 Nov 2026) is filed in [`deliverables/2026-11-07-proposal/`](../../deliverables/2026-11-07-proposal/). The requirements review (10 Nov 2026) is the later team-approved orientation. Its deck is in [`deliverables/2026-11-10-requirements-review/`](../../deliverables/2026-11-10-requirements-review/), and the slide text is extracted in [`docs/requirements/requirements-review.md`](../requirements/requirements-review.md).

The review had to lock scope and naming so the ARD does not revive cuts from earlier material, and so a smaller reference library is not mistaken for a lower quality target. Proposal v2 already uses the name Co-Hendrix and a library of 1–10 reference songs, and it already says the project does not claim to learn the producer's taste. It still prints the teammate as "Eden Svika" (the email on that slide is Sabika@post.bgu.ac.il).

## Options

Each point had a wider or older alternative that the review did not keep:

1. A reference library of about 100 files, or of 300 files, or of 1–10 licensed reference MIDI files.
2. Game-audio editors as target users, or not.
3. A claim that the system learns the producer's taste, or no such claim.
4. Raw audio as input and automatic chord extraction, or neither.
5. A similarity flag and taste clusters, or neither.
6. Constraints still outside the week-7 Alpha numbered through C5, or only C2–C4 (key, range, grid).
7. Lowering the Integrity, Verifier, and Alpha 100% targets when the library size was set, or keeping those targets.
8. The project name Muse-MIDI or Muse MIDI, and the teammate spelled Savika or Svika, or Co-Hendrix and Sabika.
9. Inventing a customer name, or leaving the named customer open.

## Decision

The requirements review locks the last alternative in each point:

- The reference library is 1–10 licensed files, not about 100 or 300.
- Game-audio editors are not target users. The primary end users are independent / small-studio MIDI producers.
- The system does not claim to learn the producer's taste. It suggests style rules from extracted features. Nothing is a rule until the producer confirms it.
- No raw audio input. No automatic chord extraction. An optional chord progression is entered by hand.
- No similarity flag and no taste clusters.
- Constraints still outside the week-7 Alpha are C2–C4 (key, range, grid). The Alpha path checks protected bars (C1). It does not include a C5.
- The Integrity target (100%), the Verifier target (100% of mutants, ≥ 99% of fixtures), and the Alpha target (protected bars identical in 100% of mock runs) stay. They are quality targets, not the library size.
- The project name is Co-Hendrix. The teammate is spelled Sabika.
- No customer name is invented. The named customer is still an open question. The review prints "Customer [name, organization]".

## Why

v1 stays checkable: a small set of licensed references the producer supplies, one region per request, and rules that count only after confirmation. The 100% figures were not relaxed to match that smaller library. The name and the Sabika spelling are fixed so later documents do not reintroduce Muse-MIDI or the Svika spelling from proposal v2. No person or organization was available to name as the customer, so none was added.

One wording mismatch is still open and is not decided here. On the review deck, UC2 and UC4 say "it does not learn taste," and FR10 does not repeat that clause. See [`CONTEXT.md`](../../CONTEXT.md).
