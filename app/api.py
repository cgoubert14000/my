"""API REST consommée par le dashboard (et utilisable en CLI / curl)."""

from __future__ import annotations

import asyncio
import json
import re
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import JSONResponse, PlainTextResponse, StreamingResponse

from . import __version__
from .brands import (
    brand_sitemaps,
    brands_from_sitemap,
    brands_url,
    brand_ids_from_url,
    brand_labels,
    filter_brands,
    letter_of,
    parse_brand_ids,
    parse_brand_reference,
    parse_brands,
    parse_sitemap_locs,
    popular as popular_brands,
    sanitize_letter,
    sitemaps_from_robots,
)
from .categories import (
    build_profile_url,
    page_title,
    parse_children,
    path_label,
    sanitize_path,
    top_level,
)
from .brand_pack import export_rows as export_brand_rows
from .browser_session import BrowserError, SolverError, harvest, session_from_curl
from .config import ConfigError
from .filters import matches_profile
from .vinted_filters import apply_filters, catalogue as filter_catalogue, read_filters
from .diagnostics import run_diagnostics
from .models import (
    ConfigPatch,
    CurlIn,
    DiagnoseIn,
    ProfileIn,
    ProfileOut,
    ToggleIn,
    UnblockIn,
    WebhookTestIn,
)
from .utils import domain_of, is_vinted_host, utcnow_iso

router = APIRouter()

_preview_lock = asyncio.Lock()
_diagnose_lock = asyncio.Lock()
#: Un seul déblocage à la fois (le navigateur est une ressource unique).
_unblock_lock = asyncio.Lock()
_brand_lock = asyncio.Lock()
#: Cache des marques lues sur Vinted : {(domain, letter): (ts, payload)}.
_brand_cache: dict[tuple[str, str], tuple[float, dict]] = {}
BRAND_CACHE_SECONDS = 6 * 3600

#: État de la synchronisation de l'index complet des marques (sitemaps Vinted).
#: Référence forte vers la tâche d'import (évite un ramassage par le GC).
_brand_sync_task: asyncio.Task | None = None

_brand_sync: dict = {
    "running": False,
    "started_at": None,
    "finished_at": None,
    "sitemaps": 0,
    "sitemaps_total": 0,
    "imported": 0,
    "error": "",
    "domain": "",
}

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


def _profile_domain(state, profile: dict) -> str:
    """Domaine Vinted du profil, ou ``www.vinted.fr`` pour un mot-clé seul."""
    raw = domain_of(profile.get("url") or "", "www.vinted.fr")
    if not is_vinted_host(raw):
        default = str(state.config.get("http.default_domain", "www.vinted.fr"))
        return default if is_vinted_host(default) else "www.vinted.fr"
    return raw


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
    domain = _profile_domain(state, profile)
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
    prefix: bool = Query(False),
    limit: int = Query(0, ge=0, le=500),
    domain: str = Query("www.vinted.fr", max_length=80),
    refresh: bool = Query(False),
) -> dict:
    """Marques proposées par Vinted.

    * sans ``letter`` ni ``search`` → raccourci local (aucun réseau) ;
    * ``letter=N`` → marques réelles de la page ``/brands/by_letter/N`` ;
    * ``search=nike`` → mêmes marques, filtrées sur le nom ;
    * ``search=n&prefix=1`` → **toutes** les marques commençant par « n »
      (index local, aucune lettre à choisir).
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
    if not letter_value and query and not prefix:
        raise HTTPException(
            status_code=422,
            detail="Indiquez une marque commençant par une lettre A-Z.",
        )
    if not letter_value and not query:
        return {
            "ok": True,
            "letters": list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            "brands": popular_brands(),
            "source": "local",
            "domain": domain,
        }

    stats = state.db.brand_stats()
    if query and stats["total"]:
        wanted = limit or (300 if prefix else 80)
        rows = state.db.search_brands(query, limit=wanted, prefix=prefix)
        return {
            "ok": True,
            "brands": rows,
            "source": "index",
            "search": query,
            "prefix": prefix,
            "total": state.db.count_brands(query, prefix=prefix),
            "returned": len(rows),
            "letters": list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            "total_indexed": stats["total"],
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


@router.get("/filters")
async def filters(url: str = Query("", max_length=1500)) -> dict:
    """Catalogue des filtres Vinted + sélection déjà présente dans ``url``.

    Le tableau de bord construit l'URL du profil avec ces identifiants : le
    moteur scrape ensuite cette URL telle quelle, sans logique supplémentaire.
    """
    payload = filter_catalogue()
    payload["ok"] = True
    payload["selected"] = read_filters(url) if url else read_filters("")
    return payload


@router.post("/filters/apply")
async def filters_apply(payload: dict) -> dict:
    """Applique des filtres à une URL (aperçu avant enregistrement)."""
    url = str(payload.get("url") or "")
    domain = str(payload.get("domain") or "www.vinted.fr").strip().lower()
    if not is_vinted_host(domain):
        raise HTTPException(status_code=422, detail="Domaine Vinted invalide.")
    result = apply_filters(
        url,
        size_ids=payload.get("size_ids") or [],
        status_ids=payload.get("status_ids") or [],
        color_ids=payload.get("color_ids") or [],
        material_ids=payload.get("material_ids") or [],
        price_from=payload.get("price_from"),
        price_to=payload.get("price_to"),
        order=payload.get("order"),
        domain=domain,
    )
    return {"ok": True, "url": result, "selected": read_filters(result)}


def _brand_sync_snapshot(state) -> dict:
    stats = state.db.brand_stats()
    return {
        "ok": True,
        "running": _brand_sync["running"],
        "started_at": _brand_sync["started_at"],
        "finished_at": _brand_sync["finished_at"],
        "sitemaps": _brand_sync["sitemaps"],
        "sitemaps_total": _brand_sync["sitemaps_total"],
        "imported": _brand_sync["imported"],
        "error": _brand_sync["error"],
        "domain": _brand_sync["domain"],
        "total": stats["total"],
        "updated_at": stats["updated_at"],
    }


async def _run_brand_sync(state, domain: str) -> None:
    """Télécharge les sitemaps de marques de Vinted et remplit l'index local."""
    origin = f"https://{domain}"
    _brand_sync.update(
        running=True,
        started_at=utcnow_iso(),
        finished_at=None,
        sitemaps=0,
        sitemaps_total=0,
        imported=0,
        error="",
        domain=domain,
    )
    try:
        reachable = False
        robots = await state.client.get(
            f"{origin}/robots.txt", attempts=2, timeout=20, quiet=True
        )
        reachable = reachable or robots.ok
        index_urls = sitemaps_from_robots(robots.text) if robots.ok else []
        if not index_urls:
            index_urls = [f"{origin}/sitemap.xml"]

        targets: list[tuple[str, str]] = []
        for index_url in index_urls:
            if re.search(r"/brands?\d*\.xml$", index_url, re.I):
                targets.append((index_url, ""))  # robots pointe déjà un sitemap de marques
                continue
            response = await state.client.get(
                index_url, attempts=2, timeout=30, quiet=True
            )
            reachable = reachable or response.ok
            if not response.ok:
                continue
            for url in brand_sitemaps(parse_sitemap_locs(response.text)):
                targets.append((url, ""))

        if not targets:
            _brand_sync["error"] = (
                "Sitemaps de marques introuvables sur ce domaine."
                if reachable
                else (
                    "Vinted injoignable depuis cette machine (robots.txt et sitemap.xml). "
                    "Vérifiez la connexion, le pare-feu ou un proxy, puis relancez."
                )
            )
            return

        _brand_sync["sitemaps_total"] = len(targets)
        total_imported = 0
        for url, _ in targets:
            document = await state.client.get(url, attempts=2, timeout=60, quiet=True)
            reachable = reachable or document.ok
            if not document.ok:
                state.db.log(
                    "WARNING",
                    f"Index des marques : {url} inaccessible ({document.short_error}).",
                    source="brands",
                )
                continue
            rows = brands_from_sitemap(document.text)
            if rows:
                total_imported += await asyncio.to_thread(state.db.upsert_brands, rows)
            _brand_sync["sitemaps"] += 1
            _brand_sync["imported"] = total_imported
        total = state.db.brand_stats()["total"]
        _brand_sync["imported"] = total
        if not total and not _brand_sync["error"]:
            _brand_sync["error"] = (
                "Les sitemaps de marques n'ont pas pu être téléchargés."
                if reachable
                else "Vinted injoignable depuis cette machine. Vérifiez la connexion ou un proxy."
            )
        if total:
            state.db.log(
                "SUCCESS",
                f"Index des marques synchronisé : {total} marques disponibles "
                "localement (recherche instantanée, hors ligne).",
                source="brands",
            )
        else:
            _brand_sync["error"] = "Aucune marque extraite des sitemaps."
    except Exception as error:  # noqa: BLE001 — jamais de crash du serveur
        _brand_sync["error"] = f"{type(error).__name__}: {error}"
        state.db.log("ERROR", f"Index des marques : {_brand_sync['error']}", source="brands")
    finally:
        _brand_sync["running"] = False
        _brand_sync["finished_at"] = utcnow_iso()


@router.get("/brands/sync")
async def brand_sync_status(request: Request) -> dict:
    """État de l'index complet des marques."""
    return _brand_sync_snapshot(_state(request))


@router.get("/brands/export")
async def brands_export(request: Request) -> PlainTextResponse:
    """Télécharge l'index complet des marques (CSV ``id,slug,name``).

    Sert à partager la liste avec un autre outil — ou à la réinjecter dans une
    autre instance via ``--import-brands`` ou ``app/data/brands.csv``.
    """
    state = _state(request)
    rows = export_brand_rows(state.db)
    if not rows:
        raise HTTPException(
            status_code=404,
            detail="Aucune marque en base : lancez d'abord l'import de l'index.",
        )
    lines = ["id,slug,name"]
    for row in rows:
        name = str(row.get("name") or "").replace('"', '""')
        slug = str(row.get("slug") or "").replace('"', '""')
        lines.append(f'{row["id"]},{slug},"{name}"' if ("," in name or '"' in name) else f'{row["id"]},{slug},{name}')
    state.db.log("INFO", f"Export de {len(rows)} marque(s) depuis le dashboard.", source="brands")
    return PlainTextResponse(
        "\n".join(lines) + "\n",
        media_type="text/csv; charset=utf-8",
        headers={
            "Content-Disposition": 'attachment; filename="marques-vinted.csv"',
        },
    )


@router.post("/brands/sync")
async def brand_sync(
    request: Request,
    domain: str = Query("www.vinted.fr", max_length=80),
) -> dict:
    """Importe **toutes** les marques Vinted depuis ses sitemaps officiels."""
    state = _state(request)
    domain = (domain or "www.vinted.fr").strip().lower()
    if not is_vinted_host(domain):
        raise HTTPException(status_code=422, detail="Domaine Vinted invalide.")
    global _brand_sync_task
    if _brand_sync["running"]:
        return {**_brand_sync_snapshot(state), "message": "Synchronisation déjà en cours."}
    _brand_sync_task = asyncio.create_task(_run_brand_sync(state, domain))
    return {
        **_brand_sync_snapshot(state),
        "message": "Synchronisation lancée : quelques secondes suffisent.",
    }


@router.get("/brands/resolve")
async def resolve_brand(ref: str = Query(..., max_length=300)) -> dict:
    """Résout une marque depuis son URL ou son identifiant Vinted."""
    brand = parse_brand_reference(ref)
    if not brand:
        raise HTTPException(
            status_code=422,
            detail=(
                "Référence non reconnue. Collez l'adresse de la marque "
                "(https://www.vinted.fr/brand/53-nike) ou son identifiant (53)."
            ),
        )
    return {"ok": True, "brand": brand}


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
    domain = _profile_domain(state, profile)
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
        # 429 quand c'est un blocage Vinted : le dashboard peut afficher un
        # message d'attente plutôt qu'une erreur générique.
        code = 429 if result.get("blocked") else 409
        raise HTTPException(status_code=code, detail=result.get("error"))
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


@router.post("/session/unblock")
async def unblock(payload: UnblockIn, request: Request) -> dict:
    """Ouvre le navigateur local, laisse Cloudflare valider, importe la session.

    C'est la seule réponse **honnête et gratuite** à une page
    ``challenge-platform`` : le défi est exécuté par un vrai navigateur (celui
    de la machine), puis le cookie ``cf_clearance`` — invisible en JavaScript
    car ``HttpOnly`` — est récupéré via le protocole DevTools et réinjecté avec
    le User-Agent qui l'a obtenu.
    """
    state = _state(request)
    if _unblock_lock.locked():
        raise HTTPException(
            status_code=429, detail="Un déblocage est déjà en cours (fenêtre ouverte)."
        )
    url = (payload.url or "").strip()
    if not url:
        profile = next(
            (
                row
                for row in state.db.list_profiles()
                if row.get("active") and str(row.get("url") or "").startswith("http")
            ),
            None,
        )
        url = str((profile or {}).get("url") or "https://www.vinted.fr/catalog")
    if not url.startswith(("http://", "https://")):
        url = "https://" + url.lstrip("/")

    config = state.config
    headless = (
        bool(payload.headless)
        if payload.headless is not None
        else bool(config.get("challenge.headless", False))
    )
    timeout = float(config.get("challenge.timeout_seconds", 60))
    state.db.log("INFO", f"Déblocage demandé : ouverture de {url} dans le navigateur…")

    def log(message: str) -> None:
        state.db.log("INFO", message, source="challenge")

    async with _unblock_lock:
        try:
            result = await asyncio.to_thread(
                harvest,
                url,
                solver_url=str(config.get("challenge.solver_url", "") or ""),
                browser_path=str(config.get("challenge.browser_path", "") or ""),
                profile_dir=str(Path(state.db_path).parent / "browser-profile"),
                timeout=timeout,
                headless=headless,
                on_log=log,
            )
        except (BrowserError, SolverError) as error:
            state.db.log("ERROR", f"Déblocage impossible : {error}", source="challenge")
            raise HTTPException(status_code=502, detail=str(error)) from None
        except Exception as error:  # pragma: no cover - imprévu (pilote, OS…)
            state.db.log("ERROR", f"Déblocage interrompu : {error}", source="challenge")
            raise HTTPException(status_code=500, detail=f"Déblocage interrompu : {error}") from None

        summary = result.summary()
        if not result.ok or not result.cookies:
            state.db.log(
                "WARNING",
                result.message or "La vérification n'est pas terminée.",
                source="challenge",
            )
            return {"ok": False, "harvest": summary, "detail": result.message}

        netloc = urlparse(result.url or url).netloc or "www.vinted.fr"
        imported = state.client.import_session(
            result.cookies, result.user_agent, netloc=netloc
        )
        resumed = state.engine.resume_after_unblock()
        state.db.log(
            "INFO",
            f"Session importée depuis le navigateur ({imported['imported']} cookie(s), "
            f"clearance : {'oui' if imported['clearance'] else 'non'}) — "
            f"{resumed} profil(s) relancé(s).",
            source="challenge",
        )
        return {
            "ok": True,
            "harvest": summary,
            "session": imported,
            "resumed": resumed,
            "detail": f"{imported['imported']} cookie(s) importé(s) pour {netloc}.",
        }


@router.post("/session/import")
async def import_session(payload: CurlIn, request: Request) -> dict:
    """Importe une session copiée du navigateur (« Copier en tant que cURL »).

    Secours quand le pilotage automatique est refusé (stratégie Windows,
    antivirus, navigateur exotique) : la commande cURL contient les cookies
    ``HttpOnly`` et le User-Agent exact, seuls éléments que Cloudflare accepte.
    """
    state = _state(request)
    try:
        session = session_from_curl(payload.command)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from None
    imported = state.client.import_session(
        session["cookies"],
        session["user_agent"],
        netloc=urlparse(session["url"]).netloc or "www.vinted.fr",
    )
    resumed = state.engine.resume_after_unblock()
    state.db.log(
        "INFO",
        f"Session importée depuis le navigateur ({imported['imported']} cookie(s), "
        f"clearance : {'oui' if imported['clearance'] else 'non'}) — "
        f"{resumed} profil(s) relancé(s).",
        source="challenge",
    )
    return {
        "ok": True,
        "session": imported,
        "resumed": resumed,
        "clearance": imported["clearance"],
        "detail": f"{imported['imported']} cookie(s) importé(s) pour {imported['netloc']}.",
    }


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
        # Reprise : le client reçoit d'abord les dernières lignes de journal.
        try:
            latest = await asyncio.to_thread(state.db.recent_logs, 1)
            last_log_id = latest[0]["id"] if latest else 0
        except Exception:  # pragma: no cover - base occupée
            last_log_id = 0
        idle = 0.0
        try:
            while True:
                if await request.is_disconnected():
                    break
                try:
                    event = await asyncio.wait_for(queue.get(), timeout=0.5)
                except asyncio.TimeoutError:
                    # Aucun événement moteur : on pousse les nouvelles lignes de
                    # journal (les logs arrivent donc à la seconde, pas au poll).
                    try:
                        rows = await asyncio.to_thread(state.db.logs_since, last_log_id, 40)
                    except Exception:  # pragma: no cover - base occupée
                        rows = []
                    if rows:
                        idle = 0.0
                        last_log_id = rows[-1]["id"]
                        for row in rows:
                            payload = json.dumps(row, ensure_ascii=False, default=str)
                            yield f"event: log\ndata: {payload}\n\n"
                    else:
                        idle += 0.5
                        if idle >= 10:
                            idle = 0.0
                            # Événement nommé (et non un simple commentaire) :
                            # le navigateur le reçoit, ce qui permet au
                            # dashboard de détecter un flux mort et de se
                            # reconnecter tout seul.
                            yield 'event: ping\ndata: {"ok": true}\n\n' 
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
