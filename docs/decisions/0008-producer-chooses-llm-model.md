# ADR 0008: The producer chooses the LLM model per chat window

## Context

The review required a swappable LLM provider but did not say who chooses the model. Models differ in cost, latency and output quality.

## Options

1. The team fixes one model in configuration.
2. The producer chooses a model per chat window from a list of supported models.

## Decision

The producer chooses, for each chat window, the LLM model to use from a list of supported models, or keeps the default (FR24, UC6). Adding a supported model is a configuration change only, with no change to the verification code (NFR14).

## Why

It gives the producer control over cost and speed, and gives a fallback for risk R5 (switch to a faster or cheaper model). Verification does not depend on the model, so the guarantee holds for any choice.
