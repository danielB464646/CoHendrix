"""Settings read from environment variables (and `.env` when present).

Secrets such as the database password and the Gemini key never live in code (NFR12).
"""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "cohendrix"
    postgres_user: str = "cohendrix"
    postgres_password: SecretStr = SecretStr("")

    gemini_api_key: SecretStr = SecretStr("")

    # LLM gateway (S1-05). The mock is the default so nothing spends the budget by accident.
    llm_provider: Literal["mock", "litellm"] = "mock"
    llm_model: str = "gemini/gemini-2.5-flash"
    llm_timeout_s: float = 20.0
    llm_mock_replies_dir: Path | None = None

    @field_validator("llm_mock_replies_dir", mode="before")
    @classmethod
    def _empty_is_none(cls, value: object) -> object:
        return None if value == "" else value

    @property
    def database_url(self) -> str:
        password = self.postgres_password.get_secret_value()
        return (
            f"postgresql://{self.postgres_user}:{password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
