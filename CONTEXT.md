# Context

Living one-page snapshot. Update this when status, goals, or open questions change.

## Project

**Name:** Co-Hendrix

University software-engineering team repository: knowledge base and code.

Team on the requirements review: Oren Kashani · Stav Ronen · Daniel Blanga · Eden Sabika. Advisor: Dr. Avi Segal.

## Status

Requirements review is done (10 Nov 2026). The ARD is being written in [`docs/requirements/ard.md`](docs/requirements/ard.md): the Abstract and Chapters 1–5 are approved by the team; the appendices and a final pass are not written yet. Implementation has not started.

- Review deck: [`deliverables/2026-11-10-requirements-review/`](deliverables/2026-11-10-requirements-review/) (`Co-Hendrix_Requirements_Review.pptx`, posted to Slack on 8 Nov 2026; cover date 10 Nov 2026).
- Markdown extract (stakeholders, UC1–UC4, FR1–FR14, NFRs, risks, Alpha): [`docs/requirements/requirements-review.md`](docs/requirements/requirements-review.md).
- Scope decisions since proposal v2: [`docs/decisions/0001-v1-scope-after-requirements-review.md`](docs/decisions/0001-v1-scope-after-requirements-review.md).
- Where to start the ARD: [`docs/requirements/ard-kickoff.md`](docs/requirements/ard-kickoff.md).

Proposal v2 remains at [`deliverables/2026-11-07-proposal/`](deliverables/2026-11-07-proposal/). Where it and the review differ, the review is later.

## Goals

University software-engineering project: a constraint-verified MIDI agent. The current agreed orientation is the 10 Nov 2026 requirements review.

## Open questions

- Student IDs and phone numbers are blank (proposal v2 slide 2).
- Sprint 1 LLM provider and who pays are still TBD.

## Requirements

The ARD and specifications belong in [`docs/requirements/`](docs/requirements/) as the markdown source of truth. The agreed review extract is [`docs/requirements/requirements-review.md`](docs/requirements/requirements-review.md). The ARD draft is [`docs/requirements/ard.md`](docs/requirements/ard.md).

The customer is DJ LIRANO (Liron Goldvaser), producer and DJ (final review deck, 10 Nov 2026).

The ARD changes some review decisions, each noted in the ARD where it applies: producers can state constraints in words (FR15–FR16); reference songs may be sent to the LLM and are stored per chat window (NFR11); several saved chat windows, each with its own MIDI, rules and model (FR22–FR24); the producer chooses the LLM model (FR24); export is never blocked (FR20); rule checks target 100% (NFR7); "does not learn taste" is dropped from the use cases; "licensed" is dropped; the risk register has 7 risks, not 10. These are not yet recorded as ADRs.
