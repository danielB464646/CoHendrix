# Requirements review — 10 Nov 2026

Markdown extract of the team-approved deck [`Co-Hendrix_Requirements_Review.pptx`](../../deliverables/2026-11-10-requirements-review/Co-Hendrix_Requirements_Review.pptx) (16 slides; cover date 10 Nov 2026). Wording below follows the slides. This is the requirements source of truth until the ARD is written. Do not add requirements, names, or numbers that are not on the slides.

Scope locks that are not themselves slide sentences are recorded in [`docs/decisions/0001-v1-scope-after-requirements-review.md`](../decisions/0001-v1-scope-after-requirements-review.md).

**Kicker:** SE Senior Project · Requirements Review · 10 Nov 2026

**Team:** Oren Kashani · Stav Ronen · Daniel Blanga · Eden Sabika | Advisor: Dr. Avi Segal

**One-line description:** A verified AI agent that generates and edits multi-track MIDI within the rules you set.

## The problem: AI help producers cannot trust

Producers sketch 8–16 bar multi-track MIDI ideas in a DAW (Ableton, FL Studio, Logic), often with AI help.

| | |
| --- | --- |
| Taste is lost | Style lives in songs you like, not in a prompt |
| Edits leak | An AI edit may change bars you already finished |
| No guarantees | Nothing proves key, range or rhythm still hold |

## Competitors

AI MIDI tools exist. None guarantee the edit.

| Tool | What it does | What we did not find |
| --- | --- | --- |
| Suno Studio 2.0 | AI chat edits MIDI in its own web DAW | Declared rules, verification |
| MIDI Agent | LLM text-to-MIDI plugin, example files for style | Bar-scoped edits, verification |
| Staccato | Continues your MIDI, claims to learn your style | Protected bars, verification |
| Logic Session Players | Bass and keys follow the chord track | Prompts; works only in Logic |

Our edge: protected bars stay untouched, rules are checked in code, export is blocked on any violation.

Based on public documentation, Nov 2026. Hands-on testing in Sprint 1.

## Vision

Our vision: AI MIDI edits you can trust.

1. You set the rules the MIDI is generated or edited by.
2. You pick the part: the tracks and bars to work on.
3. The system suggests style rules from your reference MIDI; nothing is a rule until you confirm.
4. The system verifies: no rule broken, every other part unchanged.
5. Back to your DAW: the verified changes, as a .mid file.

Guaranteed: your confirmed rules hold, protected bars stay untouched.

Measured, not promised: musical quality, originality, fit to your taste.

## The big picture: inputs, outputs, interfaces

The diagram is on slide 5 of the deck. Labels printed on it:

| Box | Label |
| --- | --- |
| Producer (user) | independent / small-studio MIDI producer |
| Reference library | 1–10 licensed songs you like (.mid) |
| Co-Hendrix | our system |
| LLM provider | external API, swappable |
| DAW | your existing workstation |

Arrow captions on the slide: prompts, confirmations; edited result, or why it failed; uploaded .mid; prompt; patch; verified .mid, downloaded; existing .mid, uploaded.

Solid: direct interface · Dashed: files the producer moves by hand.

## Users and stakeholders

| Who | Role |
| --- | --- |
| Customer [name, organization] | Decides features, priorities, acceptance |
| Independent / small-studio MIDI producers | Primary end users |
| Cloud LLM | External service; limits cost and latency |
| Reference MIDI files | Protected: only features stored |

## Use cases

Two situations, each with or without extracted constraints.

| | No extracted constraints | Extracted constraints confirmed |
| --- | --- | --- |
| Edit an existing section | UC1 | UC2 |
| Generate a part in an empty section | UC3 | UC4 |

Primary actor — an independent / small-studio MIDI producer.

System — Co-Hendrix.

Supporting — a cloud LLM, and the producer's own DAW.

## UC1 · Edit an existing section, no constraints

A story: change notes that are already there, without extracted style rules.

**Actors.** Producer (primary); Co-Hendrix; cloud LLM (supporting); producer's DAW (supporting).

**Preconditions.**

- The producer has loaded a MIDI sketch they wrote.
- The locked region already contains notes.
- No style rules (key, range, grid) have been confirmed.

**Trigger.** The producer selects an existing section and asks Co-Hendrix to change it, without applying extracted constraints.

**Main success scenario.**

1. The producer provides their MIDI sketch.
2. They lock one existing region (tracks and bars that already have notes).
3. They request a change in that region only, with no extracted style rules active.
4. Co-Hendrix asks the cloud LLM for exactly one patch for that region.
5. Co-Hendrix checks that notes outside the locked region are unchanged.
6. The producer accepts the patch as a whole.
7. They export the .mid and continue hand-edits in their DAW.

**Alternate / exception.** If the producer rejects a valid patch, the region stays as it was; they may send a new request for the same region. If the patch would change notes outside the locked region, or the LLM fails, Co-Hendrix does not apply it and the file is unchanged.

**Postcondition.** Only the locked existing region changed. No extracted style rules were enforced.

## UC2 · Edit an existing section, with extracted constraints

A story: change notes that are already there, under confirmed rules.

**Actors.** Producer (primary); Co-Hendrix; cloud LLM (supporting); producer's DAW (supporting).

**Preconditions.**

- The producer has loaded a MIDI sketch they wrote.
- The locked region already contains notes.
- They can attach 1–10 licensed reference MIDI files.

**Trigger.** The producer selects an existing section and asks for a change under confirmed extracted rules.

**Main success scenario.**

1. The producer provides an 8-bar MIDI sketch (drums and bass, in A minor) and attaches 2 licensed reference MIDI files of songs they like.
2. Co-Hendrix extracts key, pitch range, and rhythm grid and suggests them as style rules; it does not learn taste.
3. The producer confirms or edits the rules. Nothing is a rule until confirmed.
4. They lock the bass in bars 5–8 and request: "Change only the bass in bars 5–8. Play more notes. Leave the drums."
5. Co-Hendrix generates exactly one patch for that region.
6. It verifies the locked region, key, range, and rhythm grid.
7. All checks pass. The producer accepts the patch as a whole and continues in their DAW.

Confirmed rules in this example: stay in A minor; stay in the bass's note range; stay on the rhythm grid; only bars 5–8 may change.

**Alternate / exception.** If a check fails (example: the new bass used a note that is not in A minor), the patch is not applied and the producer sees "failed: key". If they reject a valid patch, the region stays as it was; they may retry the same region.

**Postcondition.** Only the bass in bars 5–8 changed. Drums and bars 1–4 stayed the same. Confirmed rules hold.

## UC3 · Generate a part in an empty section, no constraints

A story: write new notes into an empty region, without extracted style rules.

**Actors.** Producer (primary); Co-Hendrix; cloud LLM (supporting); producer's DAW (supporting).

**Preconditions.**

- The producer has loaded a MIDI sketch they wrote.
- The locked region has no notes.
- No style rules have been confirmed.

**Trigger.** The producer selects an empty section and asks Co-Hendrix to generate a part there, without extracted constraints.

**Main success scenario.**

1. The producer provides their MIDI sketch.
2. They lock an empty region (tracks and bars with no notes).
3. They ask Co-Hendrix to generate a new part in that region only, with no extracted style rules active.
4. Co-Hendrix asks the cloud LLM for exactly one patch that fills only that empty region.
5. Co-Hendrix checks that existing notes outside the region are unchanged.
6. The producer accepts the new part as a whole and continues in their DAW.

**Alternate / exception.** If they reject the patch, the section stays empty. If the patch writes outside the empty region, or the LLM fails, Co-Hendrix does not apply it and the file is unchanged.

**Postcondition.** New notes exist only in the previously empty region. The rest of the file is unchanged. No extracted style rules were enforced.

## UC4 · Generate a part in an empty section, with extracted constraints

A story: write new notes into an empty region, under confirmed rules.

**Actors.** Producer (primary); Co-Hendrix; cloud LLM (supporting); producer's DAW (supporting).

**Preconditions.**

- The producer has loaded a MIDI sketch they wrote.
- The locked region has no notes.
- They can attach 1–10 licensed reference MIDI files.

**Trigger.** The producer selects an empty section and asks Co-Hendrix to generate a part there under confirmed extracted rules.

**Main success scenario.**

1. The producer provides their MIDI sketch and attaches 1–10 licensed reference MIDI files.
2. Co-Hendrix extracts key, pitch range, and rhythm grid and suggests them as style rules; it does not learn taste.
3. The producer confirms or edits the rules. Nothing is a rule until confirmed.
4. They lock an empty region and ask Co-Hendrix to generate a new part there only.
5. Co-Hendrix generates exactly one patch for that region.
6. It verifies the locked region and each confirmed rule (key, range, rhythm grid).
7. All checks pass. The producer accepts the new part as a whole and continues in their DAW.

**Alternate / exception.** If a check fails, the patch is not applied, the section stays empty, and the producer sees which rule failed. If they reject a valid patch, the section stays empty; they may retry the same region.

**Postcondition.** The previously empty region contains a generated part that satisfies the confirmed rules. Everything else is unchanged.

## Functional requirements (1/2)

Each requirement shall be testable and traces to a use case.

| FR | Requirement | UC |
| --- | --- | --- |
| FR1 | The system shall accept a MIDI sketch written by the producer. | UC1–UC4 |
| FR2 | The system shall allow the producer to lock exactly one region (specified tracks and bars) per request. | UC1–UC4 |
| FR3 | The system shall generate exactly one patch per request, and that patch shall affect only the locked region. | UC1–UC4 |
| FR4 | The system shall leave all notes outside the locked region unchanged. | UC1–UC4 |
| FR5 | The system shall allow the producer to accept or reject a valid patch only as a whole. | UC1–UC4 |
| FR6 | The system shall not provide a built-in editor; the producer shall continue hand-edits in their own DAW. | UC1–UC4 |
| FR7 | The system shall not accept raw audio as input. | UC1–UC4 |

## Functional requirements (2/2)

Extracted constraints apply only after the producer confirms them.

| FR | Requirement | UC |
| --- | --- | --- |
| FR8 | When no style rules have been confirmed, the system shall not enforce extracted key, range, or rhythm-grid rules. | UC1, UC3 |
| FR9 | The system shall accept between 1 and 10 licensed reference MIDI files. | UC2, UC4 |
| FR10 | The system shall extract key, pitch range, and rhythm grid from the provided MIDI and suggest them as style rules. | UC2, UC4 |
| FR11 | The system shall activate a style rule only after the producer explicitly confirms it. | UC2, UC4 |
| FR12 | The system shall verify every constrained patch against the locked region and each confirmed rule (key, range, rhythm grid). | UC2, UC4 |
| FR13 | The system shall block any patch that fails a verification check, shall not apply it, and shall show the producer which rule failed. | UC1–UC4 |
| FR14 | The system shall allow an optional manually entered chord progression; it shall not extract chords automatically. | UC2, UC4 |

FR10 is printed as in the table. UC2 and UC4 step 2 still say "it does not learn taste." FR10 does not repeat that sentence. Whether those two use cases should drop it is an open question in [`CONTEXT.md`](../../CONTEXT.md).

## Non-functional requirements

Each one has a target and a test.

| Quality | Requirement | Target | How we test it |
| --- | --- | --- | --- |
| Integrity | Protected notes untouched; violations block export | 100% | 10k random patches + E2E |
| Verifier | Checkers catch injected errors | 100% of mutants, ≥ 99% of fixtures | Mutation suite in CI |
| Latency | LLM output to verified diff, 8 bars | Our code p95 < 2 s; end to end < 60 s | Timings in each run record |
| Capacity | Import of licensed reference MIDI | 1–10 files in ≤ 5 min | Import test with 10 reference files |
| Reliability | LLM error or bad patch ends in abstain, not a crash | ≤ 4 LLM calls per request | Fault-injection mocks |
| Auditability | Replaying stored LLM outputs | Identical Score | Replay test in CI |
| Privacy | Reference songs never stored or sent as notes | No notes in prompts | Prompt-payload test |

Cost and usability targets are set after the Sprint 5 baseline. Full list in ARD chapter 4.

## Main risks

Each risk has a date we check it and a fallback.

| Risk | P / I | We check | Mitigation | Fallback |
| --- | --- | --- | --- | --- |
| LLM patches fail constraints | H / H | Sprint 5 baseline | Up to 3 structured repairs | Template composer |
| Suno may copy our idea | M / H | Hands-on tests, Sprint 1–2 | Focus on verification and audit | Re-scope with the customer |
| Modules fail to integrate | M / H | Thin slice, Sprint 3 | Frozen schemas, contract tests | Integration-only sprint |

P = probability, I = impact. Full register of 10 risks with owners in ARD chapter 5.

The slide prints these three risks only. It does not list the other seven.

## Alpha, week 7

One real file, one constraint, one real LLM, through every module.

1. Import a .mid, 4 tracks
2. Profile: key and tempo
3. Protect bars, ask for an edit
4. LLM returns a patch
5. Check protected bars (C1)
6. Diff and .mid export

If C1 fails, the system abstains and shows the violation.

**Also built.**

- Score and Patch schemas frozen
- A run record for every request
- CI with a mock LLM, end to end

**Not yet.**

- Repair loop, constraints C2–C4 (key, range, grid)
- Template fallback

**Done when.**

- Protected bars identical in 100% of mock runs
- Exported file opens in a DAW
- One live run on a real LLM
