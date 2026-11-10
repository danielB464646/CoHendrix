# ARD kickoff

The ARD is not written yet. A session that writes it should start from the sources below and should not add requirements, names, or numbers that those sources do not contain.

## Draw on these

1. [`requirements-review.md`](requirements-review.md) — markdown extract of the 10 Nov 2026 requirements review: problem, competitors, vision, architecture labels, stakeholders, the use-case map, UC1–UC4, FR1–FR14 with UC traces, non-functional requirements, risks, and the week-7 Alpha.
2. [`deliverables/2026-11-10-requirements-review/Co-Hendrix_Requirements_Review.pptx`](../../deliverables/2026-11-10-requirements-review/Co-Hendrix_Requirements_Review.pptx) — the team-approved deck. If this extract and the deck disagree, the deck wins.
3. [`docs/decisions/0001-v1-scope-after-requirements-review.md`](../decisions/0001-v1-scope-after-requirements-review.md) — scope and naming locked since proposal v2.
4. [`deliverables/2026-11-07-proposal/`](../../deliverables/2026-11-07-proposal/) — proposal v2. Use it as background where the review does not restate a topic. Where they differ, the review is later.
5. [`CONTEXT.md`](../../CONTEXT.md) — open questions. Leave them open.

Slide 5 of the deck is the architecture diagram. The extract lists its labels. Do not redraw it with new boxes or flows.

## Leave open

- The named customer. The review prints "Customer [name, organization]". Do not invent a person or organization.
- Student IDs and phone numbers (blank on proposal v2 slide 2).
- The Sprint 1 LLM provider and who pays.
- Whether UC2 and UC4 should drop "does not learn taste" to match FR10. FR10 on the deck already dropped that clause. Do not silently edit either side while writing the ARD.

## Do not fill in

The review already points at later ARD chapters and does not supply their missing rows:

- Non-functional requirements: cost and usability targets are set after the Sprint 5 baseline. The slide says the full list is in ARD chapter 4. Only the seven quality rows on the slide are agreed.
- Risks: the slide prints three risks and says the full register of 10 risks with owners is in ARD chapter 5. Do not invent the other seven, and do not copy extra risks from proposal v2 into that register as if the review had approved them.

Also do not add back what ADR 0001 removed: a reference library of about 100 or 300 files, game-audio editors as users, a claim that the system learns the producer's taste, raw audio input, automatic chord extraction, a similarity flag, or taste clusters. Do not renumber the Alpha constraints. The week-7 slice checks protected bars (C1). C2–C4 (key, range, grid) are not in that slice. Keep the Integrity, Verifier, and Alpha 100% targets as printed.
