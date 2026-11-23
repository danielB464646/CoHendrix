import pytest


@pytest.fixture(autouse=True)
def _never_call_a_real_llm(monkeypatch: pytest.MonkeyPatch) -> None:
    """Tests always get the mock LLM and no key, whatever a developer's .env says."""
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    monkeypatch.setenv("GEMINI_API_KEY", "")
