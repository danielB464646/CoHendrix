"""FastAPI application entry point: `uvicorn cohendrix.main:app`."""

from fastapi import FastAPI

from cohendrix import __version__
from cohendrix.api.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(title="Co-Hendrix", version=__version__)
    app.include_router(health_router)
    return app


app = create_app()
