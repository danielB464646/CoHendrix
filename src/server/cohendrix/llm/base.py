"""The LLM gateway interface: every LLM call in the server goes through it."""

from typing import Any, Literal, Protocol

from pydantic import BaseModel

JsonSchema = dict[str, Any]


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class LLMReply(BaseModel):
    """The raw reply text, plus what the call cost. Parsing the text is the caller's job."""

    text: str
    model: str
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    latency_s: float
    cost_usd: float | None = None


class LLMError(Exception):
    """The LLM call failed. Callers abstain (FR17, NFR8)."""


class LLMTimeoutError(LLMError):
    """The LLM did not answer within the per-call timeout (T5, NFR2)."""


class LLMGateway(Protocol):
    def complete(
        self,
        messages: list[Message],
        *,
        json_schema: JsonSchema | None = None,
        timeout_s: float | None = None,
    ) -> LLMReply:
        """Send the messages and return the raw reply.

        `json_schema` asks for structured output that follows the schema.
        `timeout_s` overrides the configured per-call timeout.
        Raises `LLMTimeoutError` on timeout and `LLMError` on any other failure.
        """
        ...
