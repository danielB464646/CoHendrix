# ADR 0015: Gemini is the development LLM, with a $100 budget

## Context

ARD 4.1.7 and 4.2.1 left the Sprint 1 LLM provider, and who pays, open. Sprint 1 needs a real LLM for the spike on the patch format (risk R1), and the Alpha needs one live run.

## Options

1. A paid provider with an open budget.
2. Gemini with a fixed total budget, and a mock LLM for CI and day-to-day work.

## Decision

Option 2, decided by the team on 22 Nov 2026. The development LLM is Gemini, reached through LiteLLM (ADR 0013), with a total budget of $100 for the year. CI and day-to-day development use the mock LLM; real Gemini calls are made on purpose and logged with model, tokens, latency and cost. The Sprint 1 spike measures the cost per call; from it the team computes how many real requests the budget allows and sets a cap per request.

Still open: who holds the Gemini API key and the billing.

## Why

A fixed budget keeps cost bounded for a student project. The mock LLM makes tests free and repeatable, as ARD 4.2.1 already requires. Because the provider sits behind LiteLLM, choosing Gemini now does not lock the product to it (NFR14, FR24).
