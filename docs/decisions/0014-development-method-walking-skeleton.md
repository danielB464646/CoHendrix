# ADR 0014: Walking skeleton until the hackathon, then feature ownership

## Context

Four students build one pipeline (web client, API, MIDI engine, LLM gateway, verifier) that must work end to end at the hackathon on 29 Dec 2026. The highest integration risk is R6. After the hackathon the team needs a way of working that lasts until June 2027 and spreads the load evenly.

## Options

1. Feature ownership from day one: each member owns one functional area end to end.
2. Component ownership: each member owns one module (client, MIDI engine, verifier, platform) for the whole project.
3. Method C: the whole team builds one thin end-to-end slice (the Alpha) until the hackathon, each member building one layer of it; after the hackathon each member owns one functional area end to end and stewards one shared component.

## Decision

Option 3, chosen on 22 Nov 2026. Phase 1 runs until the hackathon; phase 2 runs from 4 Jan 2027 to June 2027. The Score, Patch and Rule schemas are frozen first and change only with the approval of all four stewards. Team rules: definition of done (merged, tests pass in CI, reviewed by a non-author, shown at the sprint review); every PR reviewed by a non-owner; AI-assisted code allowed only if the author can explain every line, with tests. Work is tracked on a GitHub Projects Kanban board in two-week sprints. Details: [`docs/planning/development-plan.md`](../planning/development-plan.md).

## Why

Option 1 integrates late (R6), loads members unevenly and builds knowledge silos. Option 2 also integrates late, and nobody owns user value. Option 3 retires R6 early with the walking skeleton and then gives each member end-to-end ownership. The cost is a hand-over at the start of phase 2, when area owners must be decided (by the end of Sprint 3).
