# Context

Living one-page snapshot. Update this when status, goals, or open questions change.

## Project

**Name:** Co-Hendrix

University software-engineering team repository: knowledge base and code.

Team on the requirements review: Oren Kashani · Stav Ronen · Daniel Blanga · Eden Sabika. Advisor: Dr. Avi Segal.

## Status

Requirements review is done (10 Nov 2026). The ARD is being written in [`docs/requirements/ard.md`](docs/requirements/ard.md): the Abstract and Chapters 1–5 are approved by the team and were revised in a review pass on 15 Nov 2026 (contradictions and missing details fixed; decisions in ADRs 0002–0012); Appendices A–D are drafted and await team review; a final pass is not done yet. Implementation has not started.

- Review deck: [`deliverables/2026-11-10-requirements-review/`](deliverables/2026-11-10-requirements-review/) (`Co-Hendrix_Requirements_Review.pptx`, posted to Slack on 8 Nov 2026; cover date 10 Nov 2026).
- Markdown extract (stakeholders, UC1–UC4, FR1–FR14, NFRs, risks, Alpha): [`docs/requirements/requirements-review.md`](docs/requirements/requirements-review.md).
- Scope decisions since proposal v2: [`docs/decisions/0001-v1-scope-after-requirements-review.md`](docs/decisions/0001-v1-scope-after-requirements-review.md). Changes made while writing the ARD: ADRs 0002–0012 in [`docs/decisions/`](docs/decisions/) (0002–0004 supersede parts of ADR 0001).
- Where to start the ARD: [`docs/requirements/ard-kickoff.md`](docs/requirements/ard-kickoff.md).

Proposal v2 remains at [`deliverables/2026-11-07-proposal/`](deliverables/2026-11-07-proposal/). Where it and the review differ, the review is later.

## Goals

University software-engineering project: a constraint-verified MIDI agent. The current agreed orientation is the 10 Nov 2026 requirements review.

## Open questions

- Phone numbers are blank (proposal v2 slide 2). Student IDs are in the ARD title block (15 Nov 2026).
- Sprint 1 LLM provider and who pays are still TBD.
- Owners of risks R1–R7 in the ARD risk register are TBD.

## Requirements

The ARD and specifications belong in [`docs/requirements/`](docs/requirements/) as the markdown source of truth. The agreed review extract is [`docs/requirements/requirements-review.md`](docs/requirements/requirements-review.md). The ARD draft is [`docs/requirements/ard.md`](docs/requirements/ard.md).

The customer is DJ LIRANO (Liron Goldvaser), producer and DJ (confirmed by the team, 15 Nov 2026; the review deck filed in the repo still prints "[name, organization]"; see ADR 0003).

The ARD changes some review decisions, each noted in the ARD where it applies and recorded as an ADR: verifier fixtures target 100% (0002); the customer is named (0003); no reference to song licensing (0004); constraints stated in words are translated into rules by the LLM (0005); rules are suggested from the sketch, and reference songs are style context sent to the LLM and stored per chat window (0006); several saved chat windows (0007); the producer chooses the LLM model (0008); export is never blocked (0009); "does not learn taste" is stated once, not in the use cases (0010); the risk register has 7 risks, not 10 (0011); the Alpha verifies only protected bars and drops tempo (0012).
