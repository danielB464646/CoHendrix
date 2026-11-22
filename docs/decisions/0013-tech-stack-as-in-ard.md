# ADR 0013: The tech stack is the one listed in ARD 4.2

## Context

ARD 4.2 lists the technologies planned in proposal v2 and calls them planning choices, not customer constraints, with the final choice left to the design document (ADD). Sprint 1 (from 23 Nov 2026) starts from an empty repository, and every code task depends on the stack, so it had to be fixed before the ADD.

## Options

1. Confirm the stack listed in ARD 4.2.
2. Choose a different stack now.
3. Leave it open until the ADD and build Sprint 1 against placeholders.

## Decision

Option 1, decided by the team on 22 Nov 2026:

- web client in React and TypeScript, with Tone.js for playback;
- server in Python with FastAPI and Pydantic;
- MIDI reading and writing with mido and pretty_midi, and key analysis with music21;
- PostgreSQL for chat windows, rules, patches and run records;
- LiteLLM as the interface to swappable LLM providers (Gemini in development);
- Docker and GitHub Actions for deployment and CI.

Smaller tooling (linters, test runners, build tool, migrations) is chosen in the Sprint 1 repository-skeleton task. The ADD records this stack as the design choice.

## Why

The stack already fits the requirements: Pydantic gives typed Score, Patch and Rule schemas with a JSON Schema export for contract tests and LLM structured output; LiteLLM keeps the provider a configuration change (NFR14); the MIDI libraries cover import, export and key analysis. Leaving it open would block every code task in Sprint 1.
