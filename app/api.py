"""API REST consommée par le dashboard (et utilisable en CLI / curl)."""

from __future__ import annotations

import asyncio
import json
from typing import Any

from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import JSONResponse, StreamingResponse

from . import __version__
from .config import ConfigError
from .filters import matches_profile
from .diagnostics import run_diagnostics
from .models import (
    ConfigPatch,
    DiagnoseIn,
    ProfileIn,
    ProfileOut,
    ToggleIn,
    WebhookTestIn,
)
from .utils import domain_of, utcnow_iso

router = APIRouter()

_preview_lock = asyncio.Lock()
_diagnose_lock = asyncio.Lock()


def _state(request: Request):
    return request.app.state.app_state


def _profile_payload(row: dict, state) -> dict[str, Any]:
    profile_id = row["id"]
    data = dict(row)
    data.update(
        {
            "domain": domain_of(row.get("url") or "", "www.vinted.fr"),
            "running": profile_id in state.engine._inflight,
            "next_run_at": state.engine.next_run_for(profile_id),
            "seconds_to_next": state.engine.seconds_to_next(profile_id),
            "poll_interval": round(state.engine._current_interval(row), 2),
            "throttle": state.engine.throttle_for(profile_id),
            "effective_webhook": bool(
                row.get("webhook") or state.config.get("discord.default_webhook")
            ),
        }
    )
    return ProfileOut(**data).model_dump()


def _ok(message: str, **extra) -> dict:
    return {"ok": True, "message": message, **extra}


# ── Santé / statut ────────────────────────────────────────────────────────────


@router.get("/health")
async def health(request: Request) -> dict:
    state = _state(request)
    return {
        "ok": True,
        "version": __version__,
        "demo": state.demo,
        "time": utcnow_iso(),
        "engine": "running" if state.engine._running else "stopped",
        "paused": state.engine.paused,
    }


@router.get("/status")
async def status(request: Request) -> dict:
    state = _state(request)
    status = state.engine.status()
    counts = state.db.item_stats()
    status.update(
        {
            "version": __version__,
            "demo": state.demo,
            "now": utcnow_iso(),
            "db_path": str(state.db_path),
            "db_size": state.db_size(),
            "counts": counts,
            "config": {
                "default_webhook": state.notifier.webhook_for(None) != "",
                "notifications_enabled": state.config.get(
                    "notifications.enabled", True
                ),
                "baseline_first_scan": state.config.get(
                    "engine.baseline_first_scan", True
                ),
            },
        }
    )
    return status


@router.get("/config")
async def get_config(request: Request) -> dict:
    return _state(request).config.public()


@router.put("/config")
async def update_config(payload: ConfigPatch, request: Request) -> dict:
    state = _state(request)
    try:
        updated = state.config.apply_patch(payload.patch)
    except ConfigError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from None
    if "proxies" in (payload.patch or {}):
        await state.client.proxies.reload()
    await state.engine.apply_config()
    state.db.log(
        "INFO", "Configuration mise à jour depuis le dashboard.", source="system"
    )
    return _ok("Configuration enregistrée.", config=updated)


# ── Profils ───────────────────────────────────────────────────────────────────


@router.get("/profiles")
async def list_profiles(request: Request) -> dict:
    state = _state(request)
    return {
        "profiles": [_profile_payload(row, state) for row in state.db.list_profiles()]
    }


@router.post("/profiles")
async def create_profile(payload: ProfileIn, request: Request) -> dict:
    state = _state(request)
    row = state.db.create_profile(payload.model_dump())
    state.db.log("INFO", f"Profil « {row['name']} » créé.", profile_id=row["id"])
    return {"ok": True, "profile": _profile_payload(row, state)}


@router.get("/profiles/{profile_id}")
async def get_profile(profile_id: int, request: Request) -> dict:
    state = _state(request)
    row = state.db.get_profile(profile_id)
    if not row:
        raise HTTPException(status_code=404, detail="Profil introuvable.")
    return {"profile": _profile_payload(row, state)}


@router.put("/profiles/{profile_id}")
async def update_profile(profile_id: int, payload: ProfileIn, request: Request) -> dict:
    state = _state(request)
    row = state.db.update_profile(profile_id, payload.model_dump())
    if not row:
        raise HTTPException(status_code=404, detail="Profil introuvable.")
    # Les filtres ont pu changer : on oublie les annonces précédemment écartées.
    state.db.clear_ignored(profile_id)
    state.engine.invalidate_profile(profile_id)
    state.db.log(
        "INFO",
        f"Profil « {row['name']} » mis à jour (filtres réévalués).",
        profile_id=profile_id,
    )
    return {"ok": True, "profile": _profile_payload(row, state)}


@router.post("/profiles/{profile_id}/toggle")
async def toggle_profile(profile_id: int, payload: ToggleIn, request: Request) -> dict:
    state = _state(request)
    row = state.db.set_active(profile_id, payload.active)
    if not row:
        raise HTTPException(status_code=404, detail="Profil introuvable.")
    state.db.log(
        "INFO",
        f"Profil « {row['name']} » {'activé' if payload.active else 'désactivé'}.",
        profile_id=profile_id,
    )
    return {"ok": True, "profile": _profile_payload(row, state)}


@router.post("/profiles/{profile_id}/duplicate")
async def duplicate_profile(profile_id: int, request: Request) -> dict:
    state = _state(request)
    row = state.db.duplicate_profile(profile_id)
    if not row:
        raise HTTPException(status_code=404, detail="Profil introuvable.")
    state.db.log("INFO", f"Profil dupliqué : « {row['name']} ».", profile_id=row["id"])
    return {"ok": True, "profile": _profile_payload(row, state)}


@router.delete("/profiles/{profile_id}")
async def delete_profile(profile_id: int, request: Request) -> dict:
    state = _state(request)
    row = state.db.get_profile(profile_id)
    if not row:
        raise HTTPException(status_code=404, detail="Profil introuvable.")
    if profile_id in state.engine._inflight:
        raise HTTPException(
            status_code=409, detail="Scan en cours : réessayez dans un instant."
        )
    state.db.delete_profile(profile_id)
    state.engine.invalidate_profile(profile_id)
    state.db.log("INFO", f"Profil « {row['name']} » supprimé.", source="system")
    return _ok("Profil supprimé.")


@router.post("/profiles/{profile_id}/scan")
async def scan_profile(profile_id: int, request: Request) -> dict:
    state = _state(request)
    result = await state.engine.scan_now(profile_id)
    if not result.get("ok"):
        raise HTTPException(status_code=409, detail=result.get("error"))
    return result


@router.post("/profiles/{profile_id}/clear-seen")
async def clear_seen(profile_id: int, request: Request) -> dict:
    state = _state(request)
    if not state.db.get_profile(profile_id):
        raise HTTPException(status_code=404, detail="Profil introuvable.")
    removed = state.db.clear_seen(profile_id)
    state.engine.invalidate_profile(profile_id)
    state.db.log(
        "INFO",
        f"{removed} entrée(s) « déjà vue(s) » supprimée(s) pour ce profil.",
        profile_id=profile_id,
    )
    return _ok(f"{removed} annonce(s) oubliée(s) : elles pourront être re-détectées.")


@router.post("/profiles/{profile_id}/preview")
async def preview_profile(
    profile_id: int, request: Request, limit: int = Query(30, ge=1, le=60)
) -> dict:
    """Teste les filtres sur les annonces actuellement en ligne, sans rien enregistrer."""
    state = _state(request)
    profile = state.db.get_profile(profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profil introuvable.")
    if not profile.get("url"):
        raise HTTPException(status_code=400, detail="Renseignez une URL de recherche.")
    if _preview_lock.locked():
        raise HTTPException(
            status_code=429, detail="Un test est déjà en cours, patientez."
        )
    async with _preview_lock:
        domain = domain_of(profile["url"])
        await state.api.ensure_session(profile["url"], profile_id=profile_id)
        result = await state.api.search(profile, page=1, domain=domain)
        if result.blocked:
            raise HTTPException(
                status_code=503,
                detail=result.error
                or "Vinted a bloqué la requête. Réessayez dans un instant.",
            )
        if result.error:
            raise HTTPException(status_code=502, detail=result.error)
        items = []
        for item in result.items[:limit]:
            verdict = matches_profile(profile, item)
            items.append(
                {
                    **item,
                    "matched": verdict.matched,
                    "reason": "" if verdict.matched else verdict.reason,
                }
            )
        accepted = len([item for item in items if item["matched"]])
        return {
            "ok": True,
            "url": result.url,
            "total": len(result.items),
            "accepted": accepted,
            "rejected": len(items) - accepted,
            "items": items,
            "note": "Aperçu basé sur les informations du catalogue ; la description "
            "complète est vérifiée lors du scan réel.",
        }


@router.post("/diagnose")
async def diagnose(payload: DiagnoseIn, request: Request) -> dict:
    """Test réel de bout en bout : session, catalogue, fiche article, vendeur."""
    state = _state(request)
    if _diagnose_lock.locked():
        raise HTTPException(status_code=429, detail="Un diagnostic est déjà en cours.")
    async with _diagnose_lock:
        try:
            return await asyncio.wait_for(
                run_diagnostics(
                    state,
                    query=payload.query,
                    webhook=payload.webhook,
                    domain=payload.domain,
                ),
                timeout=240,
            )
        except asyncio.TimeoutError:
            raise HTTPException(
                status_code=504, detail="Diagnostic interrompu (délai dépassé)."
            )


# ── Flux temps réel (Server-Sent Events) ─────────────────────────────────────


@router.get("/stream")
async def stream(request: Request):
    """Flux d'événements poussé vers le dashboard.

    Événements : ``hello`` (connexion), ``item`` (nouvelle annonce),
    ``item_update`` (fiche enrichie), ``scan`` (fin de passage),
    ``blocked`` (self-healing). Un commentaire ``: ping`` toutes les 15 s
    maintient la connexion ouverte derrière un proxy.
    """
    state = _state(request)
    queue = state.engine.subscribe()

    async def events():
        yield ": connected\n\n"
        yield 'event: hello\ndata: {"ok": true}\n\n'
        try:
            while True:
                if await request.is_disconnected():
                    break
                try:
                    event = await asyncio.wait_for(queue.get(), timeout=15)
                except asyncio.TimeoutError:
                    yield ": ping\n\n"
                    continue
                payload = json.dumps(event, ensure_ascii=False, default=str)
                yield f"event: {event.get('type', 'message')}\ndata: {payload}\n\n"
        except asyncio.CancelledError:  # pragma: no cover - client parti
            raise
        finally:
            state.engine.unsubscribe(queue)

    return StreamingResponse(
        events(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-store",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


# ── Flux / historique / logs ─────────────────────────────────────────────────


@router.get("/feed")
async def feed(
    request: Request,
    limit: int | None = Query(None, ge=1, le=200),
    profile_id: int | None = None,
) -> dict:
    state = _state(request)
    limit = limit or int(state.config.get("dashboard.feed_size", 60))
    items = state.db.recent_items(limit=limit, profile_id=profile_id)
    return {"items": items, "count": len(items)}


@router.get("/logs")
async def logs(
    request: Request,
    limit: int | None = Query(None, ge=1, le=500),
    profile_id: int | None = None,
) -> dict:
    state = _state(request)
    limit = limit or int(state.config.get("dashboard.logs_size", 300))
    return {"logs": state.db.recent_logs(limit=limit, profile_id=profile_id)}


@router.get("/scans")
async def scans(request: Request, limit: int = Query(15, ge=1, le=100)) -> dict:
    return {"scans": _state(request).db.latest_scans(limit)}


# ── Moteur, proxys, sessions ─────────────────────────────────────────────────


@router.post("/engine/toggle")
async def toggle_engine(payload: ToggleIn, request: Request) -> dict:
    state = _state(request)
    state.engine.set_paused(not payload.active)
    return _ok(
        "Moteur relancé." if payload.active else "Moteur mis en pause.",
        paused=state.engine.paused,
    )


@router.post("/engine/renew-sessions")
async def renew_sessions(request: Request) -> dict:
    state = _state(request)
    result = await state.engine.renew_sessions()
    return _ok(
        f"Session(s) renouvelée(s) : {', '.join(result) or 'aucune'}.", domains=result
    )


@router.get("/proxies")
async def proxies(request: Request) -> dict:
    return _state(request).client.proxies.stats()


@router.post("/proxies/discover")
async def discover_proxies(request: Request) -> dict:
    state = _state(request)
    added = await state.client.proxies.discover(state.client, force=True)
    return _ok(
        f"{added} proxy(s) ajouté(s) au pool.",
        added=added,
        pool=state.client.proxies.stats(),
    )


@router.post("/proxies/reset")
async def reset_proxies(request: Request) -> dict:
    state = _state(request)
    await state.client.proxies.reset_bans()
    return _ok("Quarantaines levées.", pool=state.client.proxies.stats())


# ── Notifications ────────────────────────────────────────────────────────────


@router.post("/notifications/test")
async def test_notification(payload: WebhookTestIn, request: Request) -> dict:
    state = _state(request)
    ok, error = await state.notifier.send_test(payload.webhook, payload.profile_name)
    if not ok:
        return JSONResponse(
            status_code=400,
            content={"ok": False, "error": error or "Envoi impossible."},
        )
    return _ok(
        "Message de test envoyé sur Discord."
        + (" (simulé — mode démo)" if state.demo else "")
    )
