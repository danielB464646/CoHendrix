# Sprint 1 — issues

Sprint 1 · Mon 23 Nov – Sun 6 Dec 2026 · Approved by Eden and opened on GitHub on 22 Nov 2026 as issues #5–#25 in milestone [Sprint 1](https://github.com/danielB464646/CoHendrix/milestone/1).

**Sprint goal.** Foundations for the Alpha: repo and CI with a mock LLM, frozen Score/Patch/Rule schemas, MIDI import/export with round-trip tests, a first GUI screen (upload + track × bar grid), the Gemini spike on the patch format, and hands-on competitor tests. On 1 Dec we show the plan and whatever runs by then.

Once the issues are opened, the GitHub board is the working list; this file stays as the sprint-planning record.

## Conventions

**Members (phase 1 layers).** Assigned on 22 Nov 2026: Stav takes the MIDI layer; the other three layers were drawn at random among Oren, Daniel and Eden. Phase 2 area owners are still to be decided (before 4 Jan 2027).

| Member | Who (GitHub) | Layer in the walking skeleton | Shared component (phase 2) |
| --- | --- | --- | --- |
| Member 1 | Oren Kashani (`orenkash5`) | Platform: repo, API, database, LLM gateway, CI | API, database, LLM gateway, CI |
| Member 2 | Stav Ronen (GitHub login TBD; not yet a repository collaborator) | MIDI engine: Score model, import, export | MIDI engine |
| Member 3 | Daniel Blanga (`danielB464646`) | Verifier: Patch and Rule schemas, contract tests, Gemini spike | Verifier |
| Member 4 | Eden Sabika (`sabika19971`) | Web client: upload screen, track × bar grid | Web client |
| Team | All four | Shared work: decisions, presentation, research | — |

**Labels.**

- `layer:platform` · `layer:midi` · `layer:verifier` · `layer:web` · `layer:team`
- `type:feature` · `type:infra` · `type:spike` · `type:research` · `type:docs` · `type:decision`
- `size:S` (≤ ½ day) · `size:M` (1–2 days) · `size:L` (3–4 days)
- `blocked` — waiting on an open decision
- `member:1` · `member:2` · `member:3` · `member:4` · `member:team` — stand-ins for assignees until owners are decided

**Board.** [Main project Kanban](https://github.com/users/danielB464646/projects/2). Sprint 1 issues start in *Ready*, with the board's Size field set and dates 23 Nov – 6 Dec 2026.

**Milestone:** `Sprint 1` (due 6 Dec 2026).

**Definition of done** (from the development plan): merged to main, tests written and passing in CI, reviewed by someone other than the author, shown at the sprint review. For `type:docs`, `type:decision` and `type:research` issues: the file is merged and the team has seen it.

## Summary

| ID | Issue | Title | Member | Labels | Size | Depends on |
| --- | --- | --- | --- | --- | --- | --- |
| S1-01 | — | ~~Decide and record the tech stack~~ — done, [ADR 0013](../decisions/0013-tech-stack-as-in-ard.md); not opened as an issue | Team | layer:team, type:decision | S | — |
| S1-02 | [#5](https://github.com/danielB464646/CoHendrix/issues/5) | Issue and PR templates, CODEOWNERS | Member 1 | layer:platform, type:infra | S | — |
| S1-03 | [#6](https://github.com/danielB464646/CoHendrix/issues/6) | Repository skeleton: FastAPI server, React client, Docker Compose | Member 1 | layer:platform, type:infra | M | — |
| S1-04 | [#7](https://github.com/danielB464646/CoHendrix/issues/7) | CI on GitHub Actions and branch protection | Member 1 | layer:platform, type:infra | M | S1-03 |
| S1-05 | [#8](https://github.com/danielB464646/CoHendrix/issues/8) | LLM gateway on LiteLLM, and mock LLM | Member 1 | layer:platform, type:feature | M | S1-03 |
| S1-06 | [#9](https://github.com/danielB464646/CoHendrix/issues/9) | Upload endpoint returning the Score | Member 1 | layer:platform, type:feature | M | S1-03, S1-07, S1-11 |
| S1-07 | [#10](https://github.com/danielB464646/CoHendrix/issues/10) | Freeze the Score schema | Member 2 | layer:midi, type:feature | M | — |
| S1-08 | [#11](https://github.com/danielB464646/CoHendrix/issues/11) | Freeze the Patch schema | Member 3 | layer:verifier, type:feature | M | S1-07 |
| S1-09 | [#12](https://github.com/danielB464646/CoHendrix/issues/12) | Freeze the Rule schema | Member 3 | layer:verifier, type:feature | S | S1-07 |
| S1-10 | [#13](https://github.com/danielB464646/CoHendrix/issues/13) | Schema contract tests in CI | Member 3 | layer:verifier, type:infra | S | S1-04, S1-07, S1-08, S1-09 |
| S1-11 | [#14](https://github.com/danielB464646/CoHendrix/issues/14) | MIDI import into the Score model (mido) | Member 2 | layer:midi, type:feature | L | S1-07 |
| S1-12 | [#15](https://github.com/danielB464646/CoHendrix/issues/15) | MIDI export and round-trip tests | Member 2 | layer:midi, type:feature | M | S1-11 |
| S1-13 | [#16](https://github.com/danielB464646/CoHendrix/issues/16) | MIDI test corpus | Member 2 | layer:midi, type:research | S | S1-18 |
| S1-14 | [#17](https://github.com/danielB464646/CoHendrix/issues/17) | Gemini spike via LiteLLM: patches in our format | Member 3 | layer:verifier, type:spike, blocked | L | S1-08, Gemini key |
| S1-15 | [#18](https://github.com/danielB464646/CoHendrix/issues/18) | React client: app shell and API client | Member 4 | layer:web, type:infra | S | S1-03 |
| S1-16 | [#19](https://github.com/danielB464646/CoHendrix/issues/19) | Upload screen | Member 4 | layer:web, type:feature | M | S1-15 (S1-06 for the real call) |
| S1-17 | [#20](https://github.com/danielB464646/CoHendrix/issues/20) | Track × bar grid view | Member 4 | layer:web, type:feature | L | S1-15, S1-07 |
| S1-18 | [#21](https://github.com/danielB464646/CoHendrix/issues/21) | Customer: book the 21 Dec demo, ask for real DAW exports | Team | layer:team, type:research | S | — |
| S1-19 | [#22](https://github.com/danielB464646/CoHendrix/issues/22) | Hands-on competitor tests | Team | layer:team, type:research | M | — |
| S1-20 | [#23](https://github.com/danielB464646/CoHendrix/issues/23) | Update the ARD: real calendar (Table 7, Ch. 5) and confirmed stack (4.2) | Team | layer:team, type:docs | S | — |
| S1-21 | [#24](https://github.com/danielB464646/CoHendrix/issues/24) | Alpha presentation for the 1 Dec seminar | Team | layer:team, type:docs | M | S1-20 |
| S1-22 | [#25](https://github.com/danielB464646/CoHendrix/issues/25) | Oral ARD exam preparation | Team | layer:team, type:docs | S | — |

**Load per member.** Member 1: S + 3 M · Member 2: 2 M + L + S · Member 3: M + 2 S + L · Member 4: S + M + L. Per the Gantt, MIDI import/export (S1-11, S1-12) and the GUI (S1-16, S1-17) may run until 14 Dec, into Sprint 2.

**Stack.** Decided on 22 Nov 2026 as listed in ARD 4.2 ([ADR 0013](../decisions/0013-tech-stack-as-in-ard.md)): React + TypeScript (Tone.js later, for playback) · Python + FastAPI + Pydantic · mido, pretty_midi, music21 · PostgreSQL · LiteLLM to Gemini · Docker + GitHub Actions. Tools marked *suggested* below are chosen in S1-03.

**Critical path.** S1-03 (skeleton) → every code issue; it should merge by Wed 25 Nov. S1-07 (Score) → S1-08 (Patch) → S1-14 (spike).

---

## S1-01 · Decide and record the tech stack — done

Decided by the team on 22 Nov 2026: the stack listed in ARD 4.2, recorded in [ADR 0013](../decisions/0013-tech-stack-as-in-ard.md). Not opened as an issue; the ARD wording is updated in S1-20.

## S1-02 · Issue and PR templates, CODEOWNERS

Labels: `layer:platform` `type:infra` `size:S` · Member: Member 1 · Depends on: —

The board ([Main project Kanban](https://github.com/users/danielB464646/projects/2): Backlog · Ready · In progress · In review · Done), the labels and the `Sprint 1` milestone already exist (22 Nov 2026).

Acceptance criteria:

- [ ] Issue template (description, acceptance criteria, ARD references) and PR template with the definition-of-done checklist (tests, CI green, non-owner reviewer, can explain every line).
- [ ] `CODEOWNERS` file; schema files need all four stewards once owners are known (S1-10).
- [ ] `tasks/backlog.md` points to the board.

## S1-03 · Repository skeleton: FastAPI server, React client, Docker Compose

Labels: `layer:platform` `type:infra` `size:M` · Member: Member 1 · Depends on: —

Acceptance criteria:

- [ ] `src/server/`: Python FastAPI app with Pydantic, a `GET /health` endpoint and one pytest test. Dependencies pinned (suggested: uv or pip-tools).
- [ ] `src/client/`: React + TypeScript app (suggested: Vite) with one component test (suggested: Vitest + React Testing Library).
- [ ] Server tests live in `tests/server/` (AGENTS.md); if the client tooling needs tests next to components, the README says so.
- [ ] Lint, format and type checks: Python (suggested: ruff + mypy), TypeScript (suggested: ESLint + Prettier + `tsc --noEmit`), each runnable with one command.
- [ ] `docker compose up` starts the server, the client and a PostgreSQL container. No tables yet; the database schema starts with run records in Sprint 2 (suggested migrations: Alembic).
- [ ] Secrets (the Gemini key, the database password) come from environment variables; `.env` is git-ignored and an `.env.example` exists (NFR12).
- [ ] README: a new member gets everything running in ≤ 15 minutes, with and without Docker.

## S1-04 · CI on GitHub Actions and branch protection

Labels: `layer:platform` `type:infra` `size:M` · Member: Member 1 · Depends on: S1-03

Acceptance criteria:

- [ ] A GitHub Actions workflow on every PR and on main, with separate jobs for the server (Python: lint, mypy, pytest) and the client (Node: lint, `tsc`, tests) (ARD 4.2.1).
- [ ] The Docker images for server and client build in CI.
- [ ] CI never calls a real LLM; it uses the mock from S1-05, and no LLM key is stored in GitHub secrets for CI.
- [ ] `main` is protected: PRs only, CI must pass, at least one approving review by a non-author.
- [ ] A CI run takes ≤ 10 minutes (dependency caching on).

## S1-05 · LLM gateway on LiteLLM, and mock LLM

Labels: `layer:platform` `type:feature` `size:M` · Member: Member 1 · Depends on: S1-03

One server module through which every LLM call goes, built on LiteLLM so the provider and model are configuration (NFR14), plus a mock for tests and CI (ARD 4.2.1).

Acceptance criteria:

- [ ] A gateway interface in the server: messages and an optional JSON Schema for structured output in, raw reply out; per-call timeout (T5); model name from configuration (for example `gemini/<model>`).
- [ ] The real implementation calls `litellm.completion`; it is never used in CI.
- [ ] A mock implementation behind the same interface returns recorded replies from files and can inject an error, a timeout or a slow reply (NFR8, NFR2). Tests select it by configuration.
- [ ] Every real call is logged with model, tokens, latency and cost, using LiteLLM's usage and cost data (budget rule in the development plan).
- [ ] The API key never appears in a response or a log (NFR12); a test checks this.

## S1-06 · Upload endpoint returning the Score

Labels: `layer:platform` `type:feature` `size:M` · Member: Member 1 · Depends on: S1-03, S1-07, S1-11

Joins the MIDI engine to the web client, so the first GUI screen shows a real file.

Acceptance criteria:

- [ ] A FastAPI endpoint (`POST /sketches`, multipart upload) accepts a `.mid` file and returns the Score as JSON, with the Pydantic Score model as the response model (tracks, bars, notes, drum-track flags).
- [ ] An invalid file returns an error with the reason from FR25 (not a valid MIDI file; time-signature change).
- [ ] Integration test with FastAPI's `TestClient`: upload a fixture file, get the expected Score.
- [ ] No database write yet; storing sketches comes with chat windows later.
- [ ] The endpoint requires the deployment access key (NFR17); a request without it is refused. *(Can be a stub key in Sprint 1.)*

## S1-07 · Freeze the Score schema

Labels: `layer:midi` `type:feature` `size:M` · Member: Member 2 · Depends on: —

The normalised in-memory model of a sketch, shared by every module (challenge T3).

Acceptance criteria:

- [ ] Schema covers: tracks (name, channel, drum flag), one time signature, tempo events, resolution-independent note timing, bars, and notes (pitch, velocity, start, end, track).
- [ ] Every note has a stable ID assigned by our code, which the Patch schema references (challenge T4).
- [ ] Non-note events (CC, pitch bend, program change, tempo) are kept so export can write them back unchanged (ARD 3.4).
- [ ] Written as Pydantic models in the server; the JSON Schema is exported with `model_json_schema()` and committed, with two example Score files.
- [ ] TypeScript types for the client are generated from the JSON Schema (suggested: json-schema-to-typescript), not written by hand.
- [ ] Approved in the PR by all four members (schema rule in the development plan).

## S1-08 · Freeze the Patch schema

Labels: `layer:verifier` `type:feature` `size:M` · Member: Member 3 · Depends on: S1-07

What the LLM returns and the verifier checks (challenges T1, T4).

Acceptance criteria:

- [ ] Schema describes one patch for one locked region (tracks × bars): notes added, notes removed (by note ID), notes changed (by note ID, new pitch/velocity/start/end) (FR3, FR19).
- [ ] A patch can change only notes, never other events (ARD 3.4).
- [ ] Shape is suitable for the LLM's structured output through LiteLLM (checked in S1-14).
- [ ] Pydantic models, committed JSON Schema export, generated TypeScript types, and example valid and invalid patches.
- [ ] Approved in the PR by all four members.

## S1-09 · Freeze the Rule schema

Labels: `layer:verifier` `type:feature` `size:S` · Member: Member 3 · Depends on: S1-07

Acceptance criteria:

- [ ] Schema for the four checkable rule types of ARD Table 9: locked region (tracks, bars), key (set of pitch classes), pitch range (track, lowest, highest), rhythm grid (step; tolerance fixed at ± 1/8 of the step).
- [ ] Each rule has a status: suggested, confirmed, rejected (FR11), and a source: sketch or stated constraint (FR10, FR15).
- [ ] Pydantic models, committed JSON Schema export, generated TypeScript types, one example of each type.
- [ ] Approved in the PR by all four members.

## S1-10 · Schema contract tests in CI

Labels: `layer:verifier` `type:infra` `size:S` · Member: Member 3 · Depends on: S1-04, S1-07, S1-08, S1-09

Acceptance criteria:

- [ ] A pytest contract test validates the example files against each committed JSON Schema, and fails when `model_json_schema()` of the Pydantic models differs from the committed file.
- [ ] CI fails when the generated TypeScript types are out of date with the schemas.
- [ ] Schema files are covered by CODEOWNERS so a change needs all four stewards.

## S1-11 · MIDI import into the Score model (mido)

Labels: `layer:midi` `type:feature` `size:L` · Member: Member 2 · Depends on: S1-07

Acceptance criteria:

- [ ] Reads standard MIDI type 0 and type 1 with mido (pretty_midi where it simplifies note handling); a type 0 file is split into tracks by channel (ARD 3.1).
- [ ] Timing normalised independently of the file's tick resolution; bars computed from the single time signature.
- [ ] Tracks on channel 10 are marked as drum tracks.
- [ ] Rejects, with the reason, a file that is not valid MIDI and a sketch whose time signature changes (FR25). Raw audio is rejected (FR7).
- [ ] Handles overlapping notes and notes that cross bar lines without losing them (challenge T3).
- [ ] pytest unit tests for each case above.
- [ ] Key analysis with music21 is not part of this issue; it comes with the key profile (Sprint 2) and key suggestion (M3).

## S1-12 · MIDI export and round-trip tests

Labels: `layer:midi` `type:feature` `size:M` · Member: Member 2 · Depends on: S1-11

Acceptance criteria:

- [ ] Writes a Score back to a standard `.mid` file with mido, including the non-note events kept on import (FR20).
- [ ] Round-trip test in CI: import → export → import gives an identical Score for every file in the test corpus (NFR10).
- [ ] One exported file opened by hand in a DAW; result noted in the PR.

## S1-13 · MIDI test corpus

Labels: `layer:midi` `type:research` `size:S` · Member: Member 2 · Depends on: S1-18 (customer files)

Acceptance criteria:

- [ ] `tests/fixtures/midi/` with a README listing each file: source, DAW, type 0/1, resolution, tracks, time signature, special cases.
- [ ] At least 5 team-made files covering type 0, type 1, a drum track on channel 10, overlapping notes, a note crossing a bar line, a time-signature change (for rejection), and a non-MIDI file.
- [ ] Customer exports from DJ LIRANO added when they arrive (target 5–10). Only files the customer agrees to put in the repository.

## S1-14 · Gemini spike via LiteLLM: patches in our format

Labels: `layer:verifier` `type:spike` `size:L` `blocked` · Member: Member 3 · Depends on: S1-08, the Gemini API key (open decision: who holds the key and billing)

Answers risk R1 and challenge T1 early: can Gemini return a valid patch in our format, how fast, and at what cost.

Acceptance criteria:

- [ ] 20–30 real calls to Gemini through the LiteLLM gateway (S1-05) on 2–3 sketches from the corpus, with structured output (`response_format` with the Patch JSON Schema); requests are realistic edits in a locked region.
- [ ] Every reply is parsed with the Pydantic Patch model; a reply that does not parse is counted, not fixed by hand.
- [ ] Notes which Gemini model(s) were tried, and whether LiteLLM's structured output works with our schema as-is or needs changes to the Patch schema.
- [ ] Report in `docs/architecture/` with: parse rate (valid Patch), rate of patches that stay inside the region, latency per call, tokens and cost per call.
- [ ] From the cost per call: how many real requests the $100 budget allows, and a proposed cap per request.
- [ ] The replies are saved as recorded outputs for the mock LLM (S1-05).
- [ ] Total spend logged; it stays under a cap the team sets before the spike (suggested: $5).

## S1-15 · React client: app shell and API client

Labels: `layer:web` `type:infra` `size:S` · Member: Member 4 · Depends on: S1-03

Builds on the React + TypeScript app from S1-03. Tone.js comes with playback (FR21) after the hackathon, not in this sprint.

Acceptance criteria:

- [ ] App shell with an upload page and a grid page; one component test per page passes in CI.
- [ ] A typed API client module using the TypeScript types generated from the schemas (S1-07); server URL and access key from environment configuration, never hard-coded.

## S1-16 · Upload screen

Labels: `layer:web` `type:feature` `size:M` · Member: Member 4 · Depends on: S1-15 (S1-06 for the real call)

Acceptance criteria:

- [ ] A React page where the producer chooses a `.mid` file and uploads it to `POST /sketches`; the UI is in English (NFR16).
- [ ] On success, the grid view (S1-17) opens with the returned Score.
- [ ] On rejection, the reason from the server is shown (FR25).
- [ ] Until S1-06 is merged, works against an example Score file; component tests cover success and rejection.

## S1-17 · Track × bar grid view

Labels: `layer:web` `type:feature` `size:L` · Member: Member 4 · Depends on: S1-15, S1-07

A simple grid, not a piano roll (challenge T6). Region selection comes in Sprint 2.

Acceptance criteria:

- [ ] A React component: rows are tracks (name, drum flag), columns are numbered bars; a cell shows whether the bar has notes on that track. Its input is the generated Score type.
- [ ] Renders the example Score files and a 16-bar × 4-track sketch without lag in desktop Chrome.
- [ ] Component tests for an empty track, a drum track and a note crossing a bar line.
- [ ] A screenshot is ready for the 1 Dec presentation (S1-21).

## S1-18 · Customer: book the 21 Dec demo, ask for real DAW exports

Labels: `layer:team` `type:research` `size:S` · Member: Team · Depends on: —

Acceptance criteria:

- [ ] Demo slot with DJ LIRANO on 21 Dec 2026 confirmed (challenge P4).
- [ ] Asked for 5–10 `.mid` exports from his DAW(s), with permission to keep them in the repository for tests (challenge T3, risk R6).
- [ ] The request and the reply kept in `comms/emails/` if sent by email.

## S1-19 · Hands-on competitor tests

Labels: `layer:team` `type:research` `size:M` · Member: Team · Depends on: —

ARD Appendix B is based on public documentation only and promises hands-on testing in Sprint 1.

Acceptance criteria:

- [ ] Suno Studio 2.0, MIDI Agent, Staccato and Logic Session Players tested hands-on (one member per tool where possible), on the same short sketch and the same request.
- [ ] For each, every "Not found" / "Not established" cell in ARD Table 11 is confirmed or corrected.
- [ ] ARD Appendix B updated, with the test date and what was tried.

## S1-20 · Update the ARD: real calendar (Table 7, Ch. 5) and confirmed stack (4.2)

Labels: `layer:team` `type:docs` `size:S` · Member: Team · Depends on: —

Acceptance criteria:

- [ ] ARD Table 7 matches the milestone table in `docs/planning/development-plan.md` (M1 from 23 Nov; working Alpha at the hackathon; M3 stretched over the exam period).
- [ ] Chapter 5 says "Alpha planned for week 7, working by the hackathon"; the R6 note in 5.1 matches the new sprint numbers.
- [ ] ARD 4.2 says the listed technologies are confirmed for development ([ADR 0013](../decisions/0013-tech-stack-as-in-ard.md)), not only planning choices.
- [ ] Cost and LLM notes (4.1.7, 4.2.1) say the development LLM is Gemini through LiteLLM, with a $100 budget; who holds the key stays TBD if still open.

## S1-21 · Alpha presentation for the 1 Dec seminar

Labels: `layer:team` `type:docs` `size:M` · Member: Team · Depends on: S1-20

Seminar: 1 Dec 2026, 09:10, room 313, building 96; about 10 minutes.

Acceptance criteria:

- [ ] Deck in English covering: planned Alpha scope and functionality (ARD 5.2), the confirmed tech stack (ADR 0013), the initial GUI (screenshot from S1-17 or a mock-up), anything already running, the challenges slide (development plan), and both Gantt charts.
- [ ] Includes Avi's requested changes from the previous meeting. *(List TBD — still to be collected.)*
- [ ] Filed in `deliverables/2026-12-01-alpha-plan/`.
- [ ] One dry run with the whole team by 30 Nov.

## S1-22 · Oral ARD exam preparation

Labels: `layer:team` `type:docs` `size:S` · Member: Team · Depends on: —

About 15 minutes on 1 Dec; every member must be able to explain and justify the ARD.

Acceptance criteria:

- [ ] A question list covering actors, use cases UC1–UC6, FR1–FR26, NFR1–NFR17, risks R1–R7 and the Alpha, with short answers and ARD references.
- [ ] Each member has answered questions outside their own part in a mock session by 30 Nov.
