# ADR 0012: The Alpha verifies only protected bars; tempo is dropped

## Context

The review's Alpha (week 7) slide listed "Profile: key and tempo" and checked only protected bars (C1), with C2–C4 (key, range, grid) not yet built. Key checks are scheduled for M3 (Sprints 5–6).

## Options

1. Keep the slide as printed.
2. Drop key from the profile.
3. Keep key as information, verify only C1, and drop tempo.

## Decision

Option 3. The Alpha is due in week 7, at the end of Sprint 4. Step 2 is "Profile it: key." The Alpha verifies only C1. Other rules, such as the detected key, may be sent to the LLM in the prompt as guidance, but are not checked until M3. Tempo is dropped from the Alpha. Milestone M2 reads "One constraint (protected bars, C1)". C1–C4 keep their numbers (ADR 0001).

## Why

The Alpha's goal is one constraint through every module. Showing the detected key costs little and makes the first demo more useful to the customer, while verification stays limited to the one check the Alpha promises.
