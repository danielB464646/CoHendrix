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
| [`docs/architecture/`](docs/architecture/) | Diagrams and design notes |
| [`docs/decisions/`](docs/decisions/) | ADRs: numbered files, one decision per file |
| [`meetings/`](meetings/) | Summaries named `YYYY-MM-DD-topic.md` |
| [`meetings/transcripts/`](meetings/transcripts/) | Raw transcripts when a summary is not enough |
| [`comms/digests/`](comms/digests/) | Weekly digests named `YYYY-Www.md` |
| [`comms/emails/`](comms/emails/) | Important emails, kept verbatim |
| [`deliverables/`](deliverables/) | Non-code binaries in `YYYY-MM-DD-name/` folders |
| [`tasks/backlog.md`](tasks/backlog.md) | Task backlog |
| [`src/`](src/) | Application code (empty until implementation) |
| [`tests/`](tests/) | Tests (empty until implementation) |

Read [`CONTEXT.md`](CONTEXT.md) and the latest [`CHANGELOG.md`](CHANGELOG.md) entry before changing anything. Follow [`AGENTS.md`](AGENTS.md) for where new material goes.
