import pytest

from cohendrix.config import Settings


def test_settings_come_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("POSTGRES_HOST", "db")
    monkeypatch.setenv("POSTGRES_PORT", "5432")
    monkeypatch.setenv("POSTGRES_DB", "cohendrix")
    monkeypatch.setenv("POSTGRES_USER", "cohendrix")
    monkeypatch.setenv("POSTGRES_PASSWORD", "s3cret")
    monkeypatch.setenv("GEMINI_API_KEY", "key-123")

    settings = Settings(_env_file=None)

    assert settings.postgres_host == "db"
    assert settings.gemini_api_key.get_secret_value() == "key-123"
    assert settings.database_url == "postgresql://cohendrix:s3cret@db:5432/cohendrix"


def test_secrets_are_hidden_when_printed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("POSTGRES_PASSWORD", "s3cret")
    monkeypatch.setenv("GEMINI_API_KEY", "key-123")

    shown = repr(Settings(_env_file=None))

    assert "s3cret" not in shown
    assert "key-123" not in shown
