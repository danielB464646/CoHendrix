"""The mock gateway for tests, CI and day-to-day work: no network, no cost.

It plays recorded replies in order and repeats the last one when it runs out.
A reply can also inject a fault (NFR8) or a slow answer (NFR2).

A recorded reply file is JSON:

    {"text": "<raw LLM reply>"}                 a normal reply
    {"text": "...", "delay_s": 3}               a slow reply
    {"fault": "error"}                          the LLM returns an error
    {"fault": "timeout"}                        the LLM never answers

`from_dir` loads every `*.json` file in a folder, sorted by file name.
"""

import json
import logging
import time
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, model_validator

from cohendrix.llm.base import JsonSchema, LLMError, LLMReply, LLMTimeoutError, Message

logger = logging.getLogger(__name__)

MOCK_MODEL = "mock"


class MockReply(BaseModel):
    text: str = ""
    delay_s: float = 0.0
    fault: Literal["error", "timeout"] | None = None

    @model_validator(mode="after")
    def _text_or_fault(self) -> "MockReply":
        if self.fault is None and not self.text:
            raise ValueError("a mock reply needs either text or a fault")
        return self


class MockCall(BaseModel):
    messages: list[Message]
    json_schema: JsonSchema | None
    timeout_s: float


class MockLLMGateway:
    def __init__(self, replies: list[MockReply], timeout_s: float = 20.0) -> None:
        self.replies = replies
        self.timeout_s = timeout_s
        self.calls: list[MockCall] = []

    @classmethod
    def from_dir(cls, folder: Path, timeout_s: float = 20.0) -> "MockLLMGateway":
        files = sorted(folder.glob("*.json"))
        if not files:
            raise ValueError(f"no recorded replies (*.json) in {folder}")
        replies = [MockReply.model_validate(json.loads(f.read_text("utf-8"))) for f in files]
        return cls(replies, timeout_s=timeout_s)

    def complete(
        self,
        messages: list[Message],
        *,
        json_schema: JsonSchema | None = None,
        timeout_s: float | None = None,
    ) -> LLMReply:
        timeout = timeout_s if timeout_s is not None else self.timeout_s
        self.calls.append(MockCall(messages=messages, json_schema=json_schema, timeout_s=timeout))
        if not self.replies:
            raise LLMError("the mock LLM has no recorded replies")
        reply = self.replies[min(len(self.calls), len(self.replies)) - 1]

        start = time.perf_counter()
        if reply.fault == "error":
            raise LLMError("mock LLM error")
        if reply.fault == "timeout" or reply.delay_s > timeout:
            time.sleep(min(reply.delay_s, timeout))
            raise LLMTimeoutError(f"mock LLM did not answer within {timeout} s")
        time.sleep(reply.delay_s)

        logger.debug("mock LLM call %d", len(self.calls))
        return LLMReply(text=reply.text, model=MOCK_MODEL, latency_s=time.perf_counter() - start)
