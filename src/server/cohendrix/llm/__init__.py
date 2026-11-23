"""LLM gateway: the one way the server talks to an LLM (S1-05).

Use `get_llm_gateway(settings)`; it returns the mock unless `LLM_PROVIDER=litellm`.
"""

from cohendrix.config import Settings
from cohendrix.llm.base import (
    JsonSchema,
    LLMError,
    LLMGateway,
    LLMReply,
    LLMTimeoutError,
    Message,
)
from cohendrix.llm.mock import MockLLMGateway, MockReply

__all__ = [
    "JsonSchema",
    "LLMError",
    "LLMGateway",
    "LLMReply",
    "LLMTimeoutError",
    "Message",
    "MockLLMGateway",
    "MockReply",
    "get_llm_gateway",
]


def get_llm_gateway(settings: Settings) -> LLMGateway:
    if settings.llm_provider == "litellm":
        # Imported here: LiteLLM is slow to import and the mock does not need it.
        from cohendrix.llm.litellm_gateway import LiteLLMGateway

        return LiteLLMGateway(
            model=settings.llm_model,
            api_key=settings.gemini_api_key.get_secret_value(),
            timeout_s=settings.llm_timeout_s,
        )
    if settings.llm_mock_replies_dir is not None:
        return MockLLMGateway.from_dir(settings.llm_mock_replies_dir, settings.llm_timeout_s)
    return MockLLMGateway([], timeout_s=settings.llm_timeout_s)
