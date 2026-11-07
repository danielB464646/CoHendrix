# Agent rules

These rules apply to every contributor in this repository: Cursor, Claude, Grok, other agents, and humans.

`AGENTS.md` is the source of truth. Tool-specific files (`.cursor/rules/project.mdc`, `CLAUDE.md`) only point here.

## Before you start

1. Read [`CONTEXT.md`](CONTEXT.md) for goals, status, and open questions.
2. Read the latest entries in [`CHANGELOG.md`](CHANGELOG.md) so you do not repeat or undo recent work.

## After you finish

1. Append one entry to [`CHANGELOG.md`](CHANGELOG.md): date, who, what changed, and where.
2. If goals, status, or open questions changed, update [`CONTEXT.md`](CONTEXT.md). Leave it alone when the change does not affect project state.

## Where things go

| Kind | Location | Naming |
| --- | --- | --- |
| Requirements and specs (ARD) | `docs/requirements/` | Markdown. This folder is the source of truth for requirements. |
| Architecture diagrams and design notes | `docs/architecture/` | Markdown or image files next to the note that explains them |
| Decisions | `docs/decisions/` | Numbered ADRs, one decision per file. Start from [`0000-template.md`](docs/decisions/0000-template.md). |
| Meeting summaries | `meetings/` | `YYYY-MM-DD-topic.md` |
| Raw transcripts | `meetings/transcripts/` | Only when the written summary is not enough |
| Weekly digests | `comms/digests/` | `YYYY-Www.md` (ISO week, e.g. `2026-W45.md`) |
| Important emails | `comms/emails/` | Verbatim, one file per email |
| Non-code deliverables | `deliverables/` | Dated subfolder `YYYY-MM-DD-name/` |
| Tasks | `tasks/backlog.md` | Edit the backlog. Do not add extra task lists. |
| Code | `src/` | Application source |
| Tests | `tests/` | Tests for `src/` |

## Communications

Do not commit raw Slack exports, channel dumps, or other chat logs. Turn that material into a weekly digest under `comms/digests/`. Keep only important emails, verbatim, under `comms/emails/`.

## Decisions

Record each decision in `docs/decisions/` as a numbered ADR (`0001-short-title.md`, then `0002-…`). One decision per file. Use the sections in the template: Context, Options, Decision, Why. A meeting note may mention a decision; the ADR is where it is recorded.

## What not to add

Do not invent product requirements, meeting notes, decisions, or digests. Add a file only when the team has a real source for it. Keep starter text short and replace placeholders when real content exists.
