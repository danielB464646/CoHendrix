from pathlib import Path

import pytest

from cohendrix.config import Settings
from cohendrix.llm import (
    LLMError,
    LLMTimeoutError,
    Message,
    MockLLMGateway,
    MockReply,
    get_llm_gateway,
)

FIXTURES = Path(__file__).parent / "fixtures" / "llm"
PROMPT = [Message(role="user", content="Add a bass line in bars 5-8.")]


def test_settings_select_the_mock_by_default() -> None:
    gateway = get_llm_gateway(Settings(_env_file=None))

    assert isinstance(gateway, MockLLMGateway)


def test_settings_select_recorded_replies_from_a_folder(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LLM_MOCK_REPLIES_DIR", str(FIXTURES))

    gateway = get_llm_gateway(Settings(_env_file=None))

    assert gateway.complete(PROMPT).text == '{"notes": []}'


def test_empty_replies_dir_setting_means_none(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LLM_MOCK_REPLIES_DIR", "")

    assert Settings(_env_file=None).llm_mock_replies_dir is None


def test_recorded_replies_play_in_file_order() -> None:
    gateway = MockLLMGateway.from_dir(FIXTURES, timeout_s=1)

    first = gateway.complete(PROMPT)
    with pytest.raises(LLMError):
        gateway.complete(PROMPT)
    third = gateway.complete(PROMPT)

    assert first.text == '{"notes": []}'
    assert first.model == "mock"
    assert third.text == "late"
    assert third.latency_s >= 0.05


def test_last_reply_repeats_when_replies_run_out() -> None:
    gateway = MockLLMGateway([MockReply(text="a"), MockReply(text="b")])

    texts = [gateway.complete(PROMPT).text for _ in range(4)]

    assert texts == ["a", "b", "b", "b"]


def test_injected_timeout() -> None:
    gateway = MockLLMGateway([MockReply(fault="timeout")])

    with pytest.raises(LLMTimeoutError):
        gateway.complete(PROMPT)


def test_slow_reply_past_the_timeout_is_a_timeout() -> None:
    gateway = MockLLMGateway([MockReply(text="too late", delay_s=0.5)])

    with pytest.raises(LLMTimeoutError):
        gateway.complete(PROMPT, timeout_s=0.01)


def test_timeout_is_an_llm_error_so_callers_can_abstain_on_one_type() -> None:
    assert issubclass(LLMTimeoutError, LLMError)


def test_no_recorded_replies_is_an_error() -> None:
    with pytest.raises(LLMError, match="no recorded replies"):
        MockLLMGateway([]).complete(PROMPT)


def test_calls_are_recorded_for_assertions() -> None:
    gateway = MockLLMGateway([MockReply(text="ok")], timeout_s=7)
    schema = {"type": "object"}

    gateway.complete(PROMPT, json_schema=schema)

    assert gateway.calls[0].messages == PROMPT
    assert gateway.calls[0].json_schema == schema
    assert gateway.calls[0].timeout_s == 7


def test_a_reply_needs_text_or_a_fault() -> None:
    with pytest.raises(ValueError):
        MockReply()
