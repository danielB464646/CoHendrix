# Context

Living one-page snapshot. Update this when status, goals, or open questions change.

## Project

**Name:** Co-Hendrix

University software-engineering team repository: knowledge base and code.

Team on the requirements review: Oren Kashani · Stav Ronen · Daniel Blanga · Eden Sabika. Advisor: Dr. Avi Segal.

## Status

Requirements review is done (10 Nov 2026). The ARD is being written in [`docs/requirements/ard.md`](docs/requirements/ard.md): the Abstract and Chapters 1–5 are approved by the team and were revised in a review pass on 15 Nov 2026 (contradictions and missing details fixed; decisions in ADRs 0002–0012); Appendices A–D are drafted and await team review; a final pass is not done yet.

Development is planned in [`docs/planning/development-plan.md`](docs/planning/development-plan.md) (22 Nov 2026): method C, a shared walking skeleton until the hackathon on 29 Dec 2026, then feature ownership. Sprint 1 (23 Nov – 6 Dec) has 24 issues (#5–#25 and #27–#29) on the [Main project Kanban](https://github.com/users/danielB464646/projects/2) board, assigned by layer: Oren platform, Stav MIDI, Daniel verifier, Eden web client (ADR 0016). The Alpha deck for the 1 Dec seminar is drafted: [`deliverables/2026-12-01-alpha-plan/`](deliverables/2026-12-01-alpha-plan/); slide 9 ("where we are") is filled in on 30 Nov. Context from the planning chat: [`docs/planning/2026-11-22-handoff.md`](docs/planning/2026-11-22-handoff.md).

Code on `main` (24 Nov 2026; how to run and check it is in the README):

- Issue and PR templates and `CODEOWNERS` (S1-02, #5, closed).
- Server skeleton: FastAPI + Pydantic in `src/server/cohendrix/`, PostgreSQL in Docker Compose, uv, ruff, mypy, pytest (S1-03, #6, closed).
- CI on GitHub Actions: `Server`, `Client`, `Docker images (server)`, `Docker images (client)`; the client checks skip until `src/client/` exists (S1-04, #7, open: branch protection on `main` is not set yet).
- LLM gateway `cohendrix.llm` on LiteLLM, with a mock LLM that tests and CI always use (S1-05, #8, closed).

Next for the platform layer: the upload endpoint (S1-06, #9) waits for the frozen Score schema (S1-07, #10) and MIDI import (S1-11, #14).

- Review deck: [`deliverables/2026-11-10-requirements-review/`](deliverables/2026-11-10-requirements-review/) (`Co-Hendrix_Requirements_Review.pptx`, posted to Slack on 8 Nov 2026; cover date 10 Nov 2026).
- Markdown extract (stakeholders, UC1–UC4, FR1–FR14, NFRs, risks, Alpha): [`docs/requirements/requirements-review.md`](docs/requirements/requirements-review.md).
- Scope decisions since proposal v2: [`docs/decisions/0001-v1-scope-after-requirements-review.md`](docs/decisions/0001-v1-scope-after-requirements-review.md). Changes made while writing the ARD: ADRs 0002–0012 in [`docs/decisions/`](docs/decisions/) (0002–0004 supersede parts of ADR 0001).
- Where to start the ARD: [`docs/requirements/ard-kickoff.md`](docs/requirements/ard-kickoff.md).

Proposal v2 remains at [`deliverables/2026-11-07-proposal/`](deliverables/2026-11-07-proposal/). Where it and the review differ, the review is later.

## Goals

University software-engineering project: a constraint-verified MIDI agent. The current agreed orientation is the 10 Nov 2026 requirements review.

## Open questions

- Phone numbers are blank (proposal v2 slide 2). Student IDs are in the ARD title block (15 Nov 2026).
- Development LLM is Gemini with a $100 total budget; who holds the API key and billing is TBD.
- Owners of the four feature areas (needed before 4 Jan 2027).
- The advisor's requested changes from the previous meeting (slide 13 of the 1 Dec deck).
- Semester B start date (the plan assumes 1 Mar 2027).
- ARD Table 7 is out of date; the real calendar is in the development plan.
- Owners of risks R1–R7 in the ARD risk register are TBD.
- Branch protection on `main` (PRs only, CI green, one non-author approval) and "Automatically delete head branches" need a repository admin (Daniel); until then #7 stays open.
- PRs #31–#33 (S1-03 to S1-05) were merged on 24 Nov without a non-author review; a review after the fact is pending.
- The live Alpha deck (Claude artifact) is private to Eden's account; others see only the 22 Nov source in the repo.

## Requirements

The ARD and specifications belong in [`docs/requirements/`](docs/requirements/) as the markdown source of truth. The agreed review extract is [`docs/requirements/requirements-review.md`](docs/requirements/requirements-review.md). The ARD draft is [`docs/requirements/ard.md`](docs/requirements/ard.md).

The customer is DJ LIRANO (Liron Goldvaser), producer and DJ (confirmed by the team, 15 Nov 2026; the review deck filed in the repo still prints "[name, organization]"; see ADR 0003).

The ARD changes some review decisions, each noted in the ARD where it applies and recorded as an ADR: verifier fixtures target 100% (0002); the customer is named (0003); no reference to song licensing (0004); constraints stated in words are translated into rules by the LLM (0005); rules are suggested from the sketch, and reference songs are style context sent to the LLM and stored per chat window (0006); several saved chat windows (0007); the producer chooses the LLM model (0008); export is never blocked (0009); "does not learn taste" is stated once, not in the use cases (0010); the risk register has 7 risks, not 10 (0011); the Alpha verifies only protected bars and drops tempo (0012). The tech stack listed in ARD 4.2 is confirmed for development (0013); the ARD text still calls it a planning choice. Development follows method C, a walking skeleton then feature ownership (0014); the development LLM is Gemini with a $100 budget (0015); phase 1 layers are assigned (0016).
