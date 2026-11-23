# Build from the repository root: docker build -f src/server/Dockerfile .
FROM python:3.13-slim

RUN pip install --no-cache-dir uv==0.11.32

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Dependencies first, so code changes do not reinstall them.
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-dev --no-install-project

COPY src/server ./src/server
RUN uv sync --frozen --no-dev

RUN useradd --create-home app
USER app

EXPOSE 8000
CMD ["uvicorn", "cohendrix.main:app", "--host", "0.0.0.0", "--port", "8000"]
