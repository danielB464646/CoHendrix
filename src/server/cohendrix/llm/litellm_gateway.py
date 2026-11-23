"""The real gateway: calls the configured model through LiteLLM. Never used in CI."""

import logging
import os
import time
from typing import Any

from cohendrix.llm.base import JsonSchema, LLMError, LLMReply, LLMTimeoutError, Message

# Use the model price list bundled with LiteLLM instead of downloading it at import.
os.environ.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")

import litellm
from litellm.exceptions import Timeout as LiteLLMTimeout

logger = logging.getLogger(__name__)


class LiteLLMGateway:
    def __init__(self, model: str, api_key: str, timeout_s: float) -> None:
        self.model = model
        self._api_key = api_key
        self.timeout_s = timeout_s

    def __repr__(self) -> str:
        return f"LiteLLMGateway(model={self.model!r}, timeout_s={self.timeout_s})"

    def complete(
        self,
        messages: list[Message],
        *,
        json_schema: JsonSchema | None = None,
        timeout_s: float | None = None,
    ) -> LLMReply:
        timeout = timeout_s if timeout_s is not None else self.timeout_s
        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": [m.model_dump() for m in messages],
            "timeout": timeout,
        }
        if self._api_key:
            kwargs["api_key"] = self._api_key
        if json_schema is not None:
            kwargs["response_format"] = {
                "type": "json_schema",
                "json_schema": {"name": "reply", "schema": json_schema, "strict": True},
            }

        start = time.perf_counter()
        try:
            response = litellm.completion(**kwargs)
        except LiteLLMTimeout:
            latency = time.perf_counter() - start
            logger.warning("LLM call timed out: model=%s latency_s=%.2f", self.model, latency)
            raise LLMTimeoutError(f"{self.model} did not answer within {timeout} s") from None
        except Exception as exc:
            latency = time.perf_counter() - start
            reason = self._redact(f"{type(exc).__name__}: {exc}")
            logger.warning(
                "LLM call failed: model=%s latency_s=%.2f error=%s", self.model, latency, reason
            )
            # `from None`: the original exception text may contain the key.
            raise LLMError(f"{self.model} failed: {reason}") from None
        latency = time.perf_counter() - start

        text = response.choices[0].message.content or ""
        usage = getattr(response, "usage", None)
        prompt_tokens = getattr(usage, "prompt_tokens", None)
        completion_tokens = getattr(usage, "completion_tokens", None)
        try:
            cost: float | None = float(litellm.completion_cost(completion_response=response))
        except Exception:
            cost = None  # LiteLLM has no price for this model

        logger.info(
            "LLM call: model=%s prompt_tokens=%s completion_tokens=%s latency_s=%.2f cost_usd=%s",
            self.model,
            prompt_tokens,
            completion_tokens,
            latency,
            f"{cost:.6f}" if cost is not None else "unknown",
        )
        return LLMReply(
            text=text,
            model=self.model,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            latency_s=latency,
            cost_usd=cost,
        )

    def _redact(self, text: str) -> str:
        return text.replace(self._api_key, "***") if self._api_key else text
