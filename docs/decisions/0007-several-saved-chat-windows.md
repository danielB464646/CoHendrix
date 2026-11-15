# ADR 0007: Several saved chat windows

## Context

The review described one sketch at a time. Producers work on several ideas in parallel and return to them later.

## Options

1. One sketch per session, nothing saved.
2. Several chat windows, each saved until the producer deletes it.

## Decision

The producer can open several chat windows (FR22). Each holds one MIDI sketch with its own reference files, confirmed rules, LLM model and request history. Windows are independent: nothing done in one changes another. Each window is saved until the producer deletes it (FR23, UC6).

## Why

It matches how producers work on several sketches, and keeps rules and history tied to the sketch they belong to. The tradeoff: the system must store windows on the server and delete everything in a window when it is deleted (NFR11).
