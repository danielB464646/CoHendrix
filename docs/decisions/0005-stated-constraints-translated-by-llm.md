# ADR 0005: Constraints stated in words are translated into rules by the LLM

## Context

The review only had rules extracted from MIDI. The ARD adds constraints the producer states in their own words, such as "keep the bass below C3" (FR15, FR16). Turning free text into a checkable rule realistically needs an LLM, while the ARD also requires rule suggestion and checking to use no AI (§4.2).

## Options

1. The LLM translates; the producer confirms.
2. A fixed phrase parser in code.
3. A form instead of free text.
4. The LLM translates, with a form as a built-in fallback.

## Decision

The LLM translates each stated constraint into a proposed rule of a checkable type (key, pitch range, rhythm grid). Code checks that the result is a well-formed rule of such a type; anything else is passed as guidance only and marked "not verified" (FR16). A translated rule is active only after the producer confirms it (FR11). Checking rules and suggesting rules from the sketch stay deterministic code with no AI (§4.2). When the LLM is down, stated constraints cannot be translated (UC5 alternative flow 3.b, §4.1.6). There is no built-in form; a form remains only the fallback of risk R3.

## Why

It keeps the promise that the producer can talk to Co-Hendrix like a chat assistant. The guarantee is not weakened, because nothing the LLM translates becomes a rule until the producer confirms it, and every check stays in code. The tradeoff: stated constraints are unavailable when the LLM is down.
