# ADR 0002: Verifier fixture target raised to 100%

Supersedes the Verifier line of [ADR 0001](0001-v1-scope-after-requirements-review.md) ("100% of mutants, ≥ 99% of fixtures … stay").

## Context

The requirements review printed the Verifier target as "100% of mutants, ≥ 99% of fixtures", and ADR 0001 kept it. While writing the ARD, the team saw that ≥ 99% leaves room for a wrong verdict on a valid hand-written case, which sits badly with the promise that confirmed rules hold.

## Options

1. Keep 100% of mutants and ≥ 99% of fixtures, as on the deck.
2. Raise fixtures to 100%.

## Decision

NFR7 targets 100% of mutants and 100% of fixtures (ARD §4.1.2).

## Why

Each rule is defined precisely: a key is a set of allowed pitch classes, a range is a lowest and highest note, a grid is a step size with a fixed tolerance. Every check is therefore an exact computation, like the locked-region check, so "confirmed rules hold" can be as strong as "protected bars stay untouched". The tradeoff: any single wrong verdict on a fixture is a bug that blocks the target.
