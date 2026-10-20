"""Diagnostic « vraie connexion » : Vinted accessible ? parseur opérationnel ?

Utilisé par ``python main.py --check`` et par le bouton « Diagnostic » du
dashboard. Chaque étape indique précisément ce qui fonctionne ou ce qui bloque,
pour éviter de chercher à l'aveugle.
"""

from __future__ import annotations

import time
from typing import Any

from .utils import format_money, mask_webhook, utcnow_iso

DEFAULT_QUERY = "nike"


async def run_diagnostics(
    state,
    query: str = DEFAULT_QUERY,
    webhook: str = "",
    domain: str = "www.vinted.fr",
    on_step=None,
    on_progress=None,
) -> dict[str, Any]:
    """Diagnostic réel, avec un mode réseau « rapide » (2 tentatives, pauses courtes).

    ``on_step(step)`` est appelé dès qu'une étape est terminée et
    ``on_progress(key, label)`` avant chaque étape réseau : l'appelant peut
    ainsi afficher la progression au lieu d'attendre la fin du diagnostic.
    """
    previous = getattr(state.client, "fast_fail", False)
    state.client.fast_fail = True
    try:
        return await _run_diagnostics(
            state,
            query=query,
            webhook=webhook,
            domain=domain,
            on_step=on_step,
            on_progress=on_progress,
        )
    finally:
        state.client.fast_fail = previous


async def _run_diagnostics(
    state,
    query: str = DEFAULT_QUERY,
    webhook: str = "",
    domain: str = "www.vinted.fr",
    on_step=None,
    on_progress=None,
) -> dict[str, Any]:
    steps: list[dict[str, Any]] = []
    started = time.perf_counter()

    def progress(key: str, label: str, hint: str = "") -> None:
        """Signale le début d'une étape (affichage « en cours… »)."""
        if on_progress is None:
            return
        try:
            on_progress(key, label, hint)
        except Exception:  # pragma: no cover - un affichage ne doit jamais casser
            pass

    def add(
        key: str, label: str, ok: bool, detail: str, skipped: bool = False, **data
    ) -> None:
        step = {
            "key": key,
            "label": label,
            "ok": bool(ok),
            "skipped": bool(skipped),
            "detail": detail,
            "data": data,
        }
        steps.append(step)
        if on_step is not None:
            try:
                on_step(step)
            except Exception:  # pragma: no cover
                pass

    domain = (domain or "www.vinted.fr").strip().lower()
    origin = f"https://{domain}"
    query = (query or DEFAULT_QUERY).strip()[:200]

    # ── 1. Configuration locale ──────────────────────────────────────────
    cookie_domains = state.client.stats().get("cookies", {})
    add(
        "setup",
        "Configuration locale",
        True,
        f"Transport {state.client.transport} · base {state.db_path} · "
        f"{len(state.db.list_profiles())} profil(s)",
        transport=state.client.transport,
    )

    # ── 2. Session anonyme ───────────────────────────────────────────────
    progress("session", "Session Vinted", f"connexion à {origin}…")
    session_ok = True
    session_error = ""
    try:
        session_ok = await state.api.ensure_session(origin + "/")
    except Exception as exc:  # réseau, TLS, proxy…
        session_ok = False
        session_error = f"{type(exc).__name__}: {exc}"
    cookies = cookie_domains.get(domain, [])
    has_session_cookie = any(name.endswith("_vinted_session") for name in cookies)
    add(
        "session",
        "Session Vinted",
        session_ok and bool(cookies),
        session_error
        or (
            f"Cookies obtenus : {', '.join(cookies)}"
            if cookies
            else "Aucun cookie reçu (page d'accueil inaccessible ou bloquée)."
        ),
        cookies=cookies,
        has_session_cookie=has_session_cookie,
        http=state.client.stats().get("ok", 0),
    )

    # ── 3. Catalogue réel ────────────────────────────────────────────────
    profile = {
        "id": None,
        "name": "Diagnostic",
        "url": query,
        "min_price": None,
        "max_price": None,
        "whitelist": [],
        "blacklist": [],
        "keyword_mode": "any",
        "check_description": True,
        "min_seller_rating": None,
        "min_seller_feedback": None,
    }
    page = None
    catalog_ok = False
    progress("catalog", "Catalogue Vinted", f"recherche « {query} »…")
    try:
        page = await state.api.search(profile, page=1, domain=domain)
        catalog_ok = bool(page.ok and page.items)
        if page.blocked:
            detail = (
                f"Blocage anti-bot ({page.error}). Vinted/Cloudflare/Datadome refuse "
                f"cette IP : ralentissez, changez de réseau ou utilisez un proxy résidentiel."
            )
        elif page.status == 0 and page.error:
            detail = (
                f"Connexion impossible : {page.error}. Vérifiez le réseau, le pare-feu, "
                f"le DNS ou un éventuel proxy d'entreprise."
            )
        elif page.error:
            detail = f"Requête en échec : {page.error}"
        elif page.empty:
            detail = (
                f"HTTP {page.status}, page valide mais aucune annonce pour « {query} ». "
                f"Essayez un mot-clé plus large."
            )
        elif not page.items:
            detail = (
                f"HTTP {page.status}, {page.html_bytes / 1024:.0f} Ko reçus mais 0 carte "
                f"reconnue : la structure HTML a peut-être changé."
            )
        else:
            detail = (
                f"{len(page.items)} annonce(s) extraite(s) sur une page de "
                f"{page.html_bytes / 1024:.0f} Ko · tri « Plus récent »"
            )
        add(
            "catalog",
            "Catalogue Vinted",
            catalog_ok,
            detail,
            http_status=page.status,
            blocked=page.blocked,
            items=len(page.items),
            html_bytes=page.html_bytes,
            total=page.total,
            url=page.url,
        )
    except Exception as exc:
        add("catalog", "Catalogue Vinted", False, f"{type(exc).__name__}: {exc}")

    sample = []
    if page and page.items:
        sample = [
            {
                "id": item["id"],
                "title": item.get("title", ""),
                "price": format_money(item.get("price"), item.get("currency", "EUR")),
                "brand": item.get("brand", ""),
                "size": item.get("size", ""),
                "condition": item.get("condition", ""),
                "url": item.get("url", ""),
                "image_url": item.get("image_url", ""),
            }
            for item in page.items[:5]
        ]
        add(
            "sample",
            "Échantillon d'annonces",
            True,
            " · ".join(
                f"{entry['title'][:32]} ({entry['price']})" for entry in sample[:3]
            ),
            items=sample,
        )

    # ── 4. Fiche article + vendeur ───────────────────────────────────────
    if page and page.items:
        first = page.items[0]
        progress("item", "Fiche article et vendeur", "lecture de la première annonce…")
        try:
            enriched = await state.api.enrich_item(first, domain)
        except Exception as exc:
            enriched = first
            add("item", "Fiche article", False, f"{type(exc).__name__}: {exc}")
        else:
            seller_ok = bool(enriched.get("seller_name"))
            add(
                "item",
                "Fiche article",
                bool(enriched.get("description") or enriched.get("image_url")),
                f"Description : {'oui' if enriched.get('description') else 'non'} · "
                f"photo HD : {'oui' if enriched.get('image_url') else 'non'}",
                description=(enriched.get("description") or "")[:300],
                image_url=enriched.get("image_url", ""),
            )
            add(
                "seller",
                "Informations vendeur",
                seller_ok,
                (
                    f"@{enriched.get('seller_name')} · "
                    f"{enriched.get('seller_rating') or '?'}/5 · "
                    f"{enriched.get('seller_feedback') if enriched.get('seller_feedback') is not None else '?'} avis"
                    if seller_ok
                    else "Vendeur non identifié sur la page article (best-effort)."
                ),
                seller_id=enriched.get("seller_id", ""),
                seller_name=enriched.get("seller_name", ""),
                seller_rating=enriched.get("seller_rating"),
                seller_feedback=enriched.get("seller_feedback"),
            )
    else:
        add(
            "item",
            "Fiche article",
            False,
            "Ignoré : aucune annonce à tester.",
            skipped=True,
        )
        add(
            "seller",
            "Informations vendeur",
            False,
            "Ignoré : aucune annonce à tester.",
            skipped=True,
        )

    # ── 5. Webhook Discord ───────────────────────────────────────────────
    configured_webhook = webhook or str(
        state.config.get("discord.default_webhook", "") or ""
    )
    if configured_webhook:
        progress("webhook", "Webhook Discord", "envoi d'un message de test…")
        try:
            ok, error = await state.notifier.send_test(
                configured_webhook, "Diagnostic Vinted"
            )
        except Exception as exc:
            ok, error = False, f"{type(exc).__name__}: {exc}"
        add(
            "webhook",
            "Webhook Discord",
            ok,
            "Message de test envoyé." if ok else f"Échec : {error}",
            webhook=mask_webhook(configured_webhook),
        )
    else:
        add(
            "webhook",
            "Webhook Discord",
            False,
            "Aucun webhook configuré (facultatif) : ajoutez-le dans un profil ou les réglages.",
        )

    duration_ms = int((time.perf_counter() - started) * 1000)
    return {
        "ok": catalog_ok,
        "query": query,
        "domain": domain,
        "time": utcnow_iso(),
        "duration_ms": duration_ms,
        "steps": steps,
        "advice": _advice(steps),
        "items": sample,
    }


def _advice(steps: list[dict[str, Any]]) -> list[str]:
    by_key = {step["key"]: step for step in steps}
    advice: list[str] = []

    session = by_key.get("session", {})
    catalog = by_key.get("catalog", {})
    if not session.get("ok"):
        advice.append(
            "La session Vinted n'a pas pu être créée : vérifiez la connexion Internet, "
            "le pare-feu, puis relancez. Si vous êtes en entreprise/VPN, essayez un autre réseau."
        )
    catalog_data = catalog.get("data", {})
    if catalog_data.get("blocked"):
        advice.append(
            "Vinted bloque l'IP (403/429/Datadome). Attendez 10–15 min, augmentez l'intervalle "
            "à 90–120 s, puis activez un proxy résidentiel si le blocage persiste."
        )
    elif catalog_data.get("http_status") in (0, None) and not catalog.get("ok"):
        advice.append(
            "La connexion réseau a échoué avant toute réponse HTTP (DNS, TLS, pare-feu, "
            "proxy d'entreprise). Testez `curl -I https://www.vinted.fr` sur la même machine."
        )
    elif catalog_data.get("http_status") == 200 and not catalog.get("ok"):
        advice.append(
            "La page est accessible mais aucune annonce n'a été reconnue. Testez un autre "
            "mot-clé ; si le problème persiste, la structure HTML de Vinted a changé."
        )
    seller = by_key.get("seller", {})
    if not seller.get("ok") and not seller.get("skipped"):
        advice.append(
            "Les infos vendeur sont best-effort : Vinted protège davantage les pages article. "
            "Les alertes fonctionnent sans, avec « note inconnue »."
        )
    webhook = by_key.get("webhook", {})
    if not webhook.get("ok") and not webhook.get("skipped"):
        advice.append(
            "Ajoutez un webhook Discord (Paramètres du serveur → Intégrations → Webhooks) "
            "puis utilisez « Tester Discord »."
        )
    if by_key.get("catalog", {}).get("ok") and not advice:
        advice.append(
            "Tout fonctionne : créez un profil avec votre URL de recherche, lancez un scan "
            "manuel pour vérifier, puis activez le profil."
        )
    return advice
