# CoHendrix

CoHendrix is the university software-engineering team repository. It is the knowledge base for the project (requirements, decisions, meetings, and communications) and the home for the code once implementation starts.

## Repository map

| Path | What belongs here |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | Shared rules for every agent and human |
| [`CLAUDE.md`](CLAUDE.md) | Claude entry point: read `AGENTS.md` first |
| [`.cursor/rules/project.mdc`](.cursor/rules/project.mdc) | Cursor rule, always applied; points at `AGENTS.md` |
| [`CONTEXT.md`](CONTEXT.md) | Living one-page current state |
| [`CHANGELOG.md`](CHANGELOG.md) | Append-only log of changes |
| [`docs/requirements/`](docs/requirements/) | ARD and specifications (markdown source of truth) |
| [`docs/planning/`](docs/planning/) | Development plan, sprint plans, handoff notes |
| [`docs/architecture/`](docs/architecture/) | Diagrams and design notes |
| [`docs/decisions/`](docs/decisions/) | ADRs: numbered files, one decision per file |
| [`meetings/`](meetings/) | Summaries named `YYYY-MM-DD-topic.md` |
| [`meetings/transcripts/`](meetings/transcripts/) | Raw transcripts when a summary is not enough |
| [`comms/digests/`](comms/digests/) | Weekly digests named `YYYY-Www.md` |
| [`comms/emails/`](comms/emails/) | Important emails, kept verbatim |
| [`deliverables/`](deliverables/) | Non-code binaries in `YYYY-MM-DD-name/` folders |
| [`tasks/backlog.md`](tasks/backlog.md) | Task backlog |
| [`src/`](src/) | Application code: the server in `src/server/` |
| [`tests/`](tests/) | Tests: `tests/server/` for the server |

Read [`CONTEXT.md`](CONTEXT.md) and the latest [`CHANGELOG.md`](CHANGELOG.md) entry before changing anything. Follow [`AGENTS.md`](AGENTS.md) for where new material goes.

## Run the server

The server is Python 3.13, FastAPI and Pydantic, managed with [uv](https://docs.astral.sh/uv/). Code lives in `src/server/cohendrix/`, tests in `tests/server/`. Schema models go in `cohendrix/schemas/` (S1-07 to S1-09) and the verifier in `cohendrix/verifier/` (S1-25).

First, once:

```sh
git clone https://github.com/danielB464646/CoHendrix.git && cd CoHendrix
cp .env.example .env        # then set POSTGRES_PASSWORD; GEMINI_API_KEY can stay empty for now
```

### With Docker

Needs Docker with Compose v2.

```sh
docker compose up --build
curl http://localhost:8000/health   # {"status":"ok","version":"0.1.0"}
```

This starts the server on port 8000 and PostgreSQL 17 on port 5432. The database has no tables yet; they start with run records in Sprint 2. Stop with `Ctrl+C`; `docker compose down -v` also deletes the database volume.

### Without Docker

Install uv (`curl -LsSf https://astral.sh/uv/install.sh | sh`, or `pip install uv`). uv downloads Python 3.13 itself if you do not have it.

```sh
uv sync                                                  # creates .venv with pinned versions from uv.lock
uv run uvicorn cohendrix.main:app --reload
curl http://localhost:8000/health
```

The server does not use the database yet, so you do not need PostgreSQL to run it. API docs are at http://localhost:8000/docs.

### Score and MIDI import

The [Score contract](src/contracts/score.schema.json) is **provisional**, pending
the team agreement in #27 and the four approvals required by #10.
The [Python model](src/server/cohendrix/schemas/score.py) is the source of truth.
To regenerate the schema and its [TypeScript types](src/contracts/score.ts):

```sh
uv run python scripts/export_score_schema.py
npx --yes --package=json-schema-to-typescript@15.0.4 json2ts --cwd src/contracts -i src/contracts/score.schema.json -o src/contracts/score.ts
```

The [contract fixtures](tests/fixtures/contracts/) show drums and notes crossing
bar lines. Positions are exact fractions of a MIDI quarter note from zero. Bars
are counted from 1, with length `4 * meter numerator / meter denominator` in
quarter notes. `bar_count` includes trailing silence from end-of-track events.
Time signature defaults to 4/4; when no tempo event applies, MIDI's default
tempo is 500,000 microseconds per quarter (120 BPM).

Call `cohendrix.midi_import.import_midi(data: bytes)` to get a `Score`, or catch
`MidiImportError` to report why an input was rejected. The importer reads SMF
types 0 and 1 and separates channels within a source track (channel numbers are
1-based). Channel 10 defaults to drums without remapping pitches. Note IDs
are assigned deterministically from their original source track and onset
index; editing code should keep those IDs when a note moves. Repeated,
overlapping notes on the same channel and pitch are paired oldest first.
Unterminated notes are rejected rather than given an invented duration.

Tempo events store the original MIDI tempo value. Other non-note events store
the MIDI message bytes as decoded by `mido` (without delta ticks), with source
track, position and event order for eventual export. This is not a promise of
byte-identical re-export. The upload endpoint and MIDI export are separate
issues (#9 and #15).

### The LLM

Every LLM call goes through `cohendrix.llm`: build a gateway with `get_llm_gateway(get_settings())` and call `complete(messages, json_schema=..., timeout_s=...)`. It returns the raw reply text with tokens, latency and cost; it raises `LLMTimeoutError` or `LLMError`, and the caller abstains (FR17).

`LLM_PROVIDER` in `.env` picks the implementation:

- `mock` (the default, and always in tests and CI): plays recorded replies and costs nothing. Point `LLM_MOCK_REPLIES_DIR` at a folder of `*.json` files, played in file-name order, the last one repeating. A file is `{"text": "..."}`, `{"text": "...", "delay_s": 3}` for a slow reply, or `{"fault": "error"}` / `{"fault": "timeout"}`. In tests, build `MockLLMGateway([MockReply(...)])` directly; examples are in `tests/server/fixtures/llm/`.
- `litellm`: calls `LLM_MODEL` (for example `gemini/gemini-2.5-flash`) with `GEMINI_API_KEY`. This spends the shared $100 budget (ADR 0015), so use it on purpose. Each call is logged with model, tokens, latency and cost.

### Checks

Each runs with one command from the repository root:

| Check | Command |
| --- | --- |
| Tests | `uv run pytest` |
| Lint | `uv run ruff check .` |
| Format | `uv run ruff format .` (CI: `uv run ruff format --check .`) |
| Types | `uv run mypy` |

Add a dependency with `uv add <package>` (or `uv add --dev <package>` for tools) and commit both `pyproject.toml` and `uv.lock`.

## CI and merging

[`.github/workflows/ci.yml`](.github/workflows/ci.yml) runs on every pull request and on every push to `main`:

| Check | What it runs |
| --- | --- |
| `Server` | `uv sync --locked`, ruff lint and format, mypy, pytest |
| `Client` | `npm ci`, then `npm run lint`, `npm run typecheck`, `npm test` in `src/client/` (skipped until the client exists, S1-24) |
| `Docker images (server)` | builds `src/server/Dockerfile` |
| `Docker images (client)` | builds `src/client/Dockerfile` (skipped until it exists) |

Each job stops after 10 minutes. uv, npm and Docker layers are cached. CI never calls a real LLM: no LLM key is stored in GitHub secrets, and tests use the mock LLM (S1-05).

`main` is protected: changes go in through a pull request, all four checks must pass, and one person other than the author must approve.
