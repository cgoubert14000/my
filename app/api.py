"""API REST consommée par le dashboard (et utilisable en CLI / curl)."""

from __future__ import annotations

import asyncio
import json
import time
from typing import Any

from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import JSONResponse, StreamingResponse

from . import __version__
from .brands import (
    brands_url,
    brand_ids_from_url,
    brand_labels,
    filter_brands,
    letter_of,
    parse_brand_ids,
    parse_brands,
    popular as popular_brands,
    sanitize_letter,
)
from .categories import (
    build_profile_url,
    page_title,
    parse_children,
    path_label,
    sanitize_path,
    top_level,
)
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
from .utils import domain_of, is_vinted_host, utcnow_iso

router = APIRouter()

_preview_lock = asyncio.Lock()
_diagnose_lock = asyncio.Lock()
_brand_lock = asyncio.Lock()
#: Cache des marques lues sur Vinted : {(domain, letter): (ts, payload)}.
_brand_cache: dict[tuple[str, str], tuple[float, dict]] = {}
BRAND_CACHE_SECONDS = 6 * 3600

_category_lock = asyncio.Lock()
#: Cache des sous-catégories lues sur Vinted : {(domain, path): (ts, payload)}.
_category_cache: dict[tuple[str, str], tuple[float, dict]] = {}
CATEGORY_CACHE_SECONDS = 3600


def _state(request: Request):
    return request.app.state.app_state


def _profile_payload(row: dict, state) -> dict[str, Any]:
    profile_id = row["id"]
    data = dict(row)
    data.update(
        {
            "domain": domain_of(row.get("url") or "", "www.vinted.fr"),
            "category": row.get("category") or "",
            "brands": row.get("brands") or "",
            "brand_ids": brand_ids_from_url(row.get("url") or ""),
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


# ── Catégories ────────────────────────────────────────────────────────────────


@router.get("/categories")
async def categories(
    request: Request,
    path: str = Query("", max_length=200),
    domain: str = Query("www.vinted.fr", max_length=80),
    refresh: bool = Query(False),
) -> dict:
    """Arbre des catégories : liste locale, puis sous-catégories lues en direct.

    ``path`` vide → grandes catégories (aucune requête réseau).
    ``path=/catalog/5-mens`` → sous-catégories réelles de cette page Vinted.
    """
    state = _state(request)
    domain = (domain or "www.vinted.fr").strip().lower()
    if not is_vinted_host(domain):
        raise HTTPException(status_code=422, detail="Domaine Vinted invalide.")
    clean = sanitize_path(path)
    if clean is None:
        raise HTTPException(status_code=422, detail="Chemin de catégorie invalide.")
    origin = f"https://{domain}"

    if clean == "/catalog":
        return {
            "ok": True,
            "path": "/catalog",
            "title": "Toutes les catégories",
            "children": [item.as_dict(origin) for item in top_level()],
            "source": "local",
            "domain": domain,
        }

    key = (domain, clean)
    now = time.time()
    cached = _category_cache.get(key)
    if cached and not refresh and now - cached[0] < CATEGORY_CACHE_SECONDS:
        return {**cached[1], "cached": True}

    url = f"{origin}{clean}"
    if _category_lock.locked():
        if cached:
            return {**cached[1], "cached": True}
        raise HTTPException(status_code=429, detail="Exploration déjà en cours.")
    async with _category_lock:
        await state.api.ensure_session(origin + "/")
        response = await state.client.get(
            url,
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
            },
            referer=origin + "/",
            attempts=2,
        )
        if response.blocked:
            raise HTTPException(
                status_code=503,
                detail="Vinted a bloqué la requête. Réessayez dans un instant.",
            )
        if not response.ok:
            raise HTTPException(
                status_code=502,
                detail=f"Catégorie inaccessible ({response.short_error}).",
            )
        payload = {
            "ok": True,
            "path": clean,
            "title": page_title(response.text) or path_label(clean),
            "children": parse_children(response.text, origin, exclude=clean),
            "source": "vinted",
            "domain": domain,
            "html_bytes": len(response.text or ""),
        }
        _category_cache[key] = (now, payload)
        return payload


@router.post("/profiles/{profile_id}/category")
async def set_profile_category(profile_id: int, payload: dict, request: Request) -> dict:
    """Applique une catégorie à un profil en conservant sa recherche et ses filtres."""
    state = _state(request)
    profile = state.db.get_profile(profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profil introuvable.")
    path = sanitize_path(str(payload.get("path") or ""))
    if path is None:
        raise HTTPException(status_code=422, detail="Chemin de catégorie invalide.")
    domain = domain_of(profile.get("url") or "", "www.vinted.fr")
    url = build_profile_url(profile.get("url") or "", path, domain)
    label = str(payload.get("label") or "").strip()[:120] or path_label(path)
    row = state.db.update_profile(profile_id, {**profile, "url": url, "category": label})
    state.db.clear_ignored(profile_id)
    state.engine.invalidate_profile(profile_id)
    state.db.log(
        "INFO",
        f"Catégorie de « {profile['name']} » : {label}.",
        profile_id=profile_id,
    )
    return {"ok": True, "profile": _profile_payload(row, state)}


# ── Marques ───────────────────────────────────────────────────────────────────


@router.get("/brands")
async def brands(
    request: Request,
    letter: str = Query("", max_length=2),
    search: str = Query("", max_length=60),
    domain: str = Query("www.vinted.fr", max_length=80),
    refresh: bool = Query(False),
) -> dict:
    """Marques proposées par Vinted.

    * sans ``letter`` ni ``search`` → raccourci local (aucun réseau) ;
    * ``letter=N`` → marques réelles de la page ``/brands/by_letter/N`` ;
    * ``search=nike`` → mêmes marques, filtrées sur le nom.
    """
    state = _state(request)
    domain = (domain or "www.vinted.fr").strip().lower()
    if not is_vinted_host(domain):
        raise HTTPException(status_code=422, detail="Domaine Vinted invalide.")
    origin = f"https://{domain}"
    query = (search or "").strip()

    if letter and not sanitize_letter(letter):
        raise HTTPException(status_code=422, detail="Lettre invalide (A-Z attendu).")
    letter_value = sanitize_letter(letter) or sanitize_letter(letter_of(query))
    if not letter_value:
        if query:
            raise HTTPException(
                status_code=422,
                detail="Indiquez une marque commençant par une lettre A-Z.",
            )
        return {
            "ok": True,
            "letters": list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            "brands": popular_brands(),
            "source": "local",
            "domain": domain,
        }

    key = (domain, letter_value)
    now = time.time()
    cached = _brand_cache.get(key)
    if cached and not refresh and now - cached[0] < BRAND_CACHE_SECONDS:
        rows = filter_brands(cached[1]["brands"], query)
        return {**cached[1], "brands": rows, "cached": True, "search": query}

    url = brands_url(origin, letter_value)
    if _brand_lock.locked():
        if cached:
            rows = filter_brands(cached[1]["brands"], query)
            return {**cached[1], "brands": rows, "cached": True, "search": query}
        raise HTTPException(status_code=429, detail="Lecture des marques déjà en cours.")
    async with _brand_lock:
        await state.api.ensure_session(origin + "/")
        response = await state.client.get(
            url,
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
            },
            referer=origin + "/brands",
            attempts=2,
        )
        if response.blocked:
            raise HTTPException(
                status_code=503,
                detail="Vinted a bloqué la requête. Réessayez dans un instant.",
            )
        if not response.ok:
            raise HTTPException(
                status_code=502,
                detail=f"Liste des marques inaccessible ({response.short_error}).",
            )
        payload = {
            "ok": True,
            "letter": letter_value,
            "domain": domain,
            "letters": list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            "brands": parse_brands(response.text, origin),
            "source": "vinted",
            "url": url,
        }
        _brand_cache[key] = (now, payload)
        rows = filter_brands(payload["brands"], query)
        return {**payload, "brands": rows, "search": query}


@router.post("/profiles/{profile_id}/brands")
async def set_profile_brands(profile_id: int, payload: dict, request: Request) -> dict:
    """Applique un filtre de marques à un profil (catégorie et mots-clés conservés)."""
    state = _state(request)
    profile = state.db.get_profile(profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profil introuvable.")
    raw = payload.get("brand_ids")
    brand_ids = parse_brand_ids(raw if not isinstance(raw, str) else raw)
    if raw and not brand_ids:
        raise HTTPException(status_code=422, detail="Identifiants de marque invalides.")
    domain = domain_of(profile.get("url") or "", "www.vinted.fr")
    url = build_profile_url(profile.get("url") or "", None, brand_ids, domain)
    label = str(payload.get("label") or "").strip()[:200] or brand_labels(
        brand_ids, {str(k): str(v) for k, v in (payload.get("names") or {}).items()}
    )
    if not label:
        label = f"{len(brand_ids)} marque(s)" if brand_ids else ""
    row = state.db.update_profile(profile_id, {**profile, "url": url, "brands": label})
    state.db.clear_ignored(profile_id)
    state.engine.invalidate_profile(profile_id)
    state.db.log(
        "INFO",
        f"Marques de « {profile['name']} » : {label or 'toutes'}.",
        profile_id=profile_id,
    )
    return {"ok": True, "profile": _profile_payload(row, state)}


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
    return _ok("Message de test envoyé sur Discord.")
