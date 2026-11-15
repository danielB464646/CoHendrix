# ADR 0010: "Does not learn taste" is not repeated in the use cases

Closes the open question in `CONTEXT.md` on whether UC2 and UC4 should drop "it does not learn taste".

## Context

On the review deck, UC2 and UC4 step 2 said "it does not learn taste", while FR10 on the same deck dropped that clause. ADR 0001 locked that the system does not claim to learn the producer's taste.

## Options

1. Keep the clause in UC2 and UC4.
2. Drop it from the use cases and state it once for the whole system.

## Decision

The use cases do not repeat the clause. The ARD states it in §1.3 ("without claiming that the system learns their taste") and §4.3 ("does not claim to learn the producer's taste"). ADR 0001's decision stands.

## Why

A use case describes what the producer and system do; a non-claim is a system-wide limitation and belongs with the vision and the limitations. Stating it once keeps the use cases consistent with FR10.
