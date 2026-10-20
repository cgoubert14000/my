"""Application FastAPI : API REST + dashboard statique + authentification."""

from __future__ import annotations

import base64
import binascii
import secrets
import sys
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles

from . import __version__
from .api import router
from .config import ConfigError
from .state import AppState

def _static_dir() -> Path:
    """Dossier des fichiers statiques, y compris dans un exécutable PyInstaller."""
    candidates = [Path(__file__).parent / "static"]
    bundle = getattr(sys, "_MEIPASS", None)
    if bundle:
        candidates.insert(0, Path(bundle) / "app" / "static")
    for candidate in candidates:
        if candidate.is_dir():
            return candidate
    return candidates[0]


STATIC_DIR = _static_dir()


def create_app(state: AppState) -> FastAPI:
    @asynccontextmanager
    async def lifespan(_app: FastAPI):
        await state.startup()
        try:
            yield
        finally:
            await state.shutdown()

    app = FastAPI(
        title="Vinted Sniper",
        version=__version__,
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
        lifespan=lifespan,
    )
    app.state.app_state = state
    app.include_router(router, prefix="/api")
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

    @app.get("/", include_in_schema=False)
    async def index() -> FileResponse:
        return FileResponse(
            STATIC_DIR / "index.html", headers={"Cache-Control": "no-store"}
        )

    @app.get("/favicon.ico", include_in_schema=False)
    async def favicon() -> FileResponse:
        return FileResponse(STATIC_DIR / "favicon.svg", media_type="image/svg+xml")

    @app.exception_handler(ConfigError)
    async def config_error(_request: Request, exc: ConfigError) -> JSONResponse:
        return JSONResponse(status_code=400, content={"ok": False, "detail": str(exc)})

    @app.middleware("http")
    async def guard(request: Request, call_next):
        # Mot de passe optionnel (config.json → app.password).
        password = str(state.config.get("app.password", "") or "")
        if password:
            header = request.headers.get("authorization", "")
            authorized = False
            if header.lower().startswith("basic "):
                try:
                    decoded = base64.b64decode(header.split(" ", 1)[1]).decode("utf-8")
                    _user, _, given = decoded.partition(":")
                    authorized = secrets.compare_digest(given, password)
                except (binascii.Error, UnicodeDecodeError):
                    authorized = False
            if not authorized:
                return Response(
                    status_code=401,
                    content="Authentification requise.",
                    headers={
                        "WWW-Authenticate": 'Basic realm="Vinted Sniper", charset="UTF-8"'
                    },
                )
        # Anti-CSRF : refus des écritures initiées par un autre site.
        # (Sec-Fetch-Site est fiable derrière un reverse proxy, contrairement à Host.)
        if request.method not in {"GET", "HEAD", "OPTIONS"}:
            fetch_site = request.headers.get("sec-fetch-site", "")
            if fetch_site == "cross-site":
                return JSONResponse(
                    status_code=403,
                    content={"ok": False, "detail": "Requête cross-site refusée."},
                )
        response = await call_next(request)
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("Referrer-Policy", "same-origin")
        if request.url.path.startswith("/api/"):
            response.headers.setdefault("Cache-Control", "no-store")
        return response

    return app
