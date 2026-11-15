# ADR 0009: Export is never blocked

## Context

The review deck said "violations block export" (Integrity row, competitor slide). In the ARD, rules are checked when a patch is verified, so a patch that breaks a rule never reaches the sketch. Rules can also be added or changed after notes are already in the sketch.

## Options

1. Block export whenever the sketch breaks a rule.
2. Check patches before they are applied, and never block export.

## Decision

Option 2. A patch that fails a check is never applied (FR13, FR17). Export itself is never blocked (FR20). If the producer later adds or changes rules, notes already in the sketch are not re-checked, and the sketch can still be exported. NFR6 is reworded to match; its target and test are unchanged.

## Why

The guarantee is enforced where changes happen, so blocking export adds nothing for AI changes and would trap the producer's own notes behind rules they added later.
