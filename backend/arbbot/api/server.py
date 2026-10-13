"""FastAPI application: REST + WebSocket over the running Runtime. Read-mostly; the only write endpoints are
operator controls (emergency stop / resume / live enable toggle / tunables within the allowlist / lab start)."""
from __future__ import annotations

import asyncio
import json
import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from ..config.settings import REPO_ROOT, Settings, get_settings
from ..config.tunables import TunableParams
from ..reliability.model import required_sample_size

log = logging.getLogger("arbbot.api")


def _json_safe(o):
    if isinstance(o, dict):
        return {k: _json_safe(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_json_safe(v) for v in o]
    if isinstance(o, int) and not isinstance(o, bool) and abs(o) > 2**53:
        return str(o)
    if isinstance(o, float) and (o != o or o in (float("inf"), float("-inf"))):
        return None
    if hasattr(o, "value") and hasattr(o, "name"):
        return o.value
    return o


def create_app(settings: Settings | None = None, runtime=None) -> FastAPI:
    settings = settings or get_settings()
    state: dict = {"runtime": runtime, "lab": None, "lab_task": None}

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        if state["runtime"] is None:
            from ..app.runtime import Runtime

            rt = Runtime(settings)
            try:
                await rt.start()
            except Exception as e:  # noqa: BLE001
                log.error("runtime failed to start: %s", e)
                state["start_error"] = str(e)
                rt = None
            state["runtime"] = rt
        yield
        rt = state["runtime"]
        if rt is not None:
            await rt.stop()

    app = FastAPI(title="arbbot", version="0.1.0", lifespan=lifespan, default_response_class=ORJSONResponse)
    app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins or ["*"], allow_methods=["*"], allow_headers=["*"])

    def rt():
        r = state["runtime"]
        if r is None:
            raise HTTPException(503, f"runtime not started: {state.get('start_error', 'starting')}")
        return r

    # ------------------------------------------------------------------ read

    @app.get("/api/health")
    def health():
        r = state["runtime"]
        return {"ok": r is not None, "ts": time.time(), "error": state.get("start_error"),
                "block": r.last_block if r else None}

    @app.get("/api/status")
    def status():
        return _json_safe(rt().status())

    @app.get("/api/opportunities")
    def opportunities(limit: int = 100, decision: str | None = None, since_minutes: float | None = None):
        r = rt()
        since = time.time() - since_minutes * 60 if since_minutes else None
        rows = r.db.opportunities(limit=limit, decision=decision, since=since)
        return _json_safe(rows)

    @app.get("/api/opportunities/live")
    def opportunities_live(limit: int = 60):
        r = rt()
        return _json_safe([o.to_record() for o in r.recent_opps[:limit]])

    @app.get("/api/metrics/{name}")
    def metrics(name: str, minutes: float = 60):
        return rt().db.metrics(name, time.time() - minutes * 60)

    @app.get("/api/executions")
    def executions(limit: int = 100):
        return _json_safe(rt().db.executions(limit))

    @app.get("/api/events")
    def events(limit: int = 100, kind: str | None = None):
        return _json_safe(rt().db.events(limit, kind))

    @app.get("/api/reliability")
    def reliability():
        r = rt()
        rep = r.reliability.calibration_report()
        rep["required_n_examples"] = {f"{p:.2f}": required_sample_size(p, r.policy.min_success_probability, r.reliability.level)
                                      for p in (0.8, 0.85, 0.9, 0.95)}
        return _json_safe(rep)

    @app.get("/api/pools")
    def pools():
        r = rt()
        out = []
        for p in r.pools:
            x, y = p.depth_tokens()
            out.append({"address": p.address, "dex": p.dex, "kind": p.kind.name, "fee_ppm": p.fee_ppm, "stable": p.stable,
                        "token0": p.token0.symbol, "token1": p.token1.symbol, "reserve0": str(x), "reserve1": str(y),
                        "updated_block": p.updated_block, "quarantined": p.quarantined, "reason": p.quarantine_reason,
                        "usd": (x / 10**p.token0.decimals * (r.fees.token_price_usd(p.token0) or 0) + y / 10**p.token1.decimals * (r.fees.token_price_usd(p.token1) or 0))})
        return out

    @app.get("/api/routes")
    def routes(limit: int = 50):
        from ..engine.routes import route_fee_bps, route_spread_bps

        r = rt()
        rows = [{"route": x.describe(), "key": x.key, "spread_bps": route_spread_bps(x), "fee_bps": route_fee_bps(x), "hops": len(x.hops)} for x in r.routes]
        rows.sort(key=lambda d: -d["spread_bps"])
        return rows[:limit]

    @app.get("/api/lab/runs")
    def lab_runs(limit: int = 10):
        return _json_safe(rt().db.lab_runs(limit))

    @app.get("/api/lab/current")
    def lab_current():
        lab = state["lab"]
        return _json_safe(lab.snapshot()) if lab else {"running": False}

    @app.get("/api/changes")
    def changes(limit: int = 50):
        return _json_safe(rt().db.changes(limit))

    @app.get("/api/signer")
    def signer():
        r = rt()
        return {"configured": r.signer is not None, "health": r.signer_health,
                "message": None if r.signer is not None else "PRÊT POUR TEST RÉEL — AUTORISATION FINANCIÈRE MANQUANTE: aucun signer configuré (voir docs/06_wallet_securise.md)"}

    # ------------------------------------------------------------------ operator controls

    @app.post("/api/control/emergency-stop")
    def emergency_stop(payload: dict | None = None):
        r = rt()
        r.emergency_stop((payload or {}).get("reason", "operator (UI)"))
        return r.risk.as_dict()

    @app.post("/api/control/resume")
    def resume():
        r = rt()
        r.resume()
        return r.risk.as_dict()

    @app.post("/api/control/live-enabled")
    def live_enabled(payload: dict):
        r = rt()
        r.risk.manual_live_enabled = bool(payload.get("enabled", False))
        r.db.add_event("info", "control", f"manual_live_enabled={r.risk.manual_live_enabled}")
        return r.risk.as_dict()

    @app.post("/api/control/activate-live")
    def activate_live():
        r = rt()
        ok = r.risk.activate_live()
        r.db.add_event("info" if ok else "warning", "control", f"activate_live -> {ok}")
        return {"ok": ok, "risk": r.risk.as_dict()}

    @app.post("/api/control/tunables")
    def set_tunables(payload: dict):
        r = rt()
        try:
            t = r.tunables.with_changes(**payload)
        except PermissionError as e:
            raise HTTPException(403, str(e)) from e
        except TypeError as e:
            raise HTTPException(400, str(e)) from e
        before = r.tunables.as_dict()
        r.set_tunables(t)
        r.db.add_change("operator", "tunables via API", before, t.as_dict(), None, None, True)
        return t.as_dict()

    @app.post("/api/lab/start")
    async def lab_start(payload: dict | None = None):
        from ..lab.runner import LabRunner

        r = rt()
        if state["lab"] and state["lab"].running:
            raise HTTPException(409, "lab already running")
        minutes = float((payload or {}).get("minutes", 60))
        lab = LabRunner(r, total_minutes=minutes)
        state["lab"] = lab
        state["lab_task"] = asyncio.create_task(lab.run())
        return {"started": True, "minutes": minutes}

    @app.post("/api/lab/stop")
    async def lab_stop():
        lab = state["lab"]
        if lab:
            lab.stop()
        return {"stopped": True}

    # ------------------------------------------------------------------ websocket

    @app.websocket("/ws")
    async def ws(sock: WebSocket):
        await sock.accept()
        r = state["runtime"]
        if r is None:
            await sock.send_text(json.dumps({"kind": "error", "data": "runtime not started"}))
            await sock.close()
            return
        q = r.bus.subscribe()
        try:
            await sock.send_text(json.dumps({"kind": "status", "ts": time.time(), "data": _json_safe(r.status())}, default=str))
            while True:
                evt = await q.get()
                await sock.send_text(json.dumps(_json_safe(evt), default=str))
        except WebSocketDisconnect:
            pass
        except Exception as e:  # noqa: BLE001
            log.debug("ws closed: %s", e)
        finally:
            r.bus.unsubscribe(q)

    # Production UI: serve frontend/dist at / when it has been built (npm run build) — one port for everything.
    dist = REPO_ROOT / "frontend" / "dist"
    if dist.exists():
        from fastapi.staticfiles import StaticFiles

        app.mount("/", StaticFiles(directory=str(dist), html=True), name="ui")

    return app


def main() -> None:
    import uvicorn

    s = get_settings()
    logging.basicConfig(level=s.log_level, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    uvicorn.run(create_app(s), host=s.api_host, port=s.api_port, log_level="warning")


if __name__ == "__main__":
    main()
