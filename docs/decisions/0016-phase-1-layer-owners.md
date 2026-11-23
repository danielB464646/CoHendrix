# ADR 0016: Who builds each layer of the walking skeleton

## Context

Phase 1 (ADR 0014) gives each member one layer of the Alpha slice. The Sprint 1 issues were drafted for "Member 1–4" until the layers were assigned.

## Options

1. Choose each layer by preference.
2. Draw the layers at random.
3. Mixed: fix the layers that have a clear preference, draw the rest.

## Decision

Option 3, on 22 Nov 2026. Stav takes the MIDI engine. The other three layers were drawn at random among Oren, Daniel and Eden:

| Member | Who | Layer |
| --- | --- | --- |
| Member 1 | Oren Kashani | Platform: repo, API, database, LLM gateway, CI |
| Member 2 | Stav Ronen | MIDI engine: Score model, import, export |
| Member 3 | Daniel Blanga | Verifier: Patch and Rule schemas, contract tests, Gemini spike |
| Member 4 | Eden Sabika | Web client: upload screen, track × bar grid |

Shared team issues (decisions, presentation, research) belong to all four. This covers phase 1 only; owners of the four functional areas in phase 2 are decided by the end of Sprint 3.

## Why

It unblocks the Sprint 1 issues on the board without a long negotiation, while keeping the one clear preference.
