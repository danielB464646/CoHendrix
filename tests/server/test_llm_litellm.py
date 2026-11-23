"""The real gateway, with LiteLLM's own `mock_response` so no request leaves the machine."""

import logging
from collections.abc import Callable
from typing import Any

import litellm
import pytest
from fastapi.testclient import TestClient
from litellm.exceptions import Timeout as LiteLLMTimeout

from cohendrix.config import Settings
from cohendrix.llm import LLMError, LLMTimeoutError, Message, get_llm_gateway
from cohendrix.llm.litellm_gateway import LiteLLMGateway
from cohendrix.main import app

KEY = "AIzaSy-test-key-that-must-never-leak"
MODEL = "gemini/gemini-2.5-flash"
PROMPT = [Message(role="user", content="Add a bass line in bars 5-8.")]

Completion = Callable[..., Any]


def fake_completion(mock_response: object, seen: dict[str, Any]) -> Completion:
    real = litellm.completion

    def completion(**kwargs: Any) -> Any:
        seen.update(kwargs)
        return real(**kwargs, mock_response=mock_response)

    return completion


@pytest.fixture
def gateway() -> LiteLLMGateway:
    return LiteLLMGateway(model=MODEL, api_key=KEY, timeout_s=20)


def test_settings_select_litellm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LLM_PROVIDER", "litellm")
    monkeypatch.setenv("LLM_MODEL", "gemini/some-other-model")

    gateway = get_llm_gateway(Settings(_env_file=None))

    assert isinstance(gateway, LiteLLMGateway)
    assert gateway.model == "gemini/some-other-model"


def test_reply_with_usage_cost_and_model(
    gateway: LiteLLMGateway, monkeypatch: pytest.MonkeyPatch
) -> None:
    seen: dict[str, Any] = {}
    monkeypatch.setattr(litellm, "completion", fake_completion("hello", seen))

    reply = gateway.complete(PROMPT)

    assert reply.text == "hello"
    assert reply.model == MODEL
    assert reply.prompt_tokens is not None
    assert reply.completion_tokens is not None
    assert reply.cost_usd is not None and reply.cost_usd > 0
    assert seen["model"] == MODEL
    assert seen["timeout"] == 20
    assert seen["messages"] == [{"role": "user", "content": "Add a bass line in bars 5-8."}]


def test_json_schema_and_timeout_are_passed_to_litellm(
    gateway: LiteLLMGateway, monkeypatch: pytest.MonkeyPatch
) -> None:
    seen: dict[str, Any] = {}
    monkeypatch.setattr(litellm, "completion", fake_completion("{}", seen))
    schema = {"type": "object", "properties": {}}

    gateway.complete(PROMPT, json_schema=schema, timeout_s=3)

    assert seen["response_format"]["json_schema"]["schema"] == schema
    assert seen["timeout"] == 3


def test_every_call_is_logged_with_model_tokens_latency_and_cost(
    gateway: LiteLLMGateway, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    monkeypatch.setattr(litellm, "completion", fake_completion("hello", {}))

    with caplog.at_level(logging.INFO, logger="cohendrix.llm"):
        gateway.complete(PROMPT)

    line = caplog.records[-1].getMessage()
    for field in (
        "model=gemini/",
        "prompt_tokens=",
        "completion_tokens=",
        "latency_s=",
        "cost_usd=",
    ):
        assert field in line


def test_litellm_timeout_becomes_llm_timeout_error(
    gateway: LiteLLMGateway, monkeypatch: pytest.MonkeyPatch
) -> None:
    timeout = LiteLLMTimeout(message="slow", model=MODEL, llm_provider="gemini")
    monkeypatch.setattr(litellm, "completion", fake_completion(timeout, {}))

    with pytest.raises(LLMTimeoutError):
        gateway.complete(PROMPT)


def test_api_key_never_appears_in_errors_or_logs(
    gateway: LiteLLMGateway, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    def leaky_completion(**kwargs: Any) -> Any:
        raise RuntimeError(f"401 Unauthorized for key={kwargs['api_key']}")

    monkeypatch.setattr(litellm, "completion", leaky_completion)

    with caplog.at_level(logging.DEBUG), pytest.raises(LLMError) as raised:
        gateway.complete(PROMPT)

    assert KEY not in str(raised.value)
    assert raised.value.__cause__ is None
    assert raised.value.__suppress_context__
    assert KEY not in caplog.text
    assert KEY not in repr(gateway)


def test_api_key_never_appears_in_a_response(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", KEY)
    client = TestClient(app)

    for path in ("/health", "/openapi.json"):
        assert KEY not in client.get(path).text
