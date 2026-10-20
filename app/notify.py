"""Notifications Discord : embeds riches, anti-spam et reprise sur erreur."""

from __future__ import annotations

import asyncio
import re
import time
from collections import deque
from typing import Any

import httpx

from .config import ConfigStore
from .database import Database
from .utils import format_money, mask_webhook, utcnow_iso

VINTED_TEAL = 0x09B1BA
COLOR_PRICE_DROP = 0x2ECC71


def stars(rating: float | None) -> str:
    """Note sur 5 rendue en étoiles (pleines / demies / vides)."""
    if rating is None:
        return "—"
    full = int(rating)
    half = 1 if rating - full >= 0.5 else 0
    return (
        "★" * full
        + ("½" if half else "")
        + "☆" * (5 - full - half)
        + f"  {rating:.1f}/5"
    )


class RateLimiter:
    """Fenêtre glissante : ``limit`` envois par minute maximum."""

    def __init__(self, limit: int = 20):
        self.limit = max(1, int(limit))
        self._sent: deque[float] = deque()
        self._lock = asyncio.Lock()

    async def acquire(self) -> float:
        waited = 0.0
        async with self._lock:
            now = time.monotonic()
            while self._sent and now - self._sent[0] > 60:
                self._sent.popleft()
            if len(self._sent) >= self.limit:
                wait = 60 - (now - self._sent[0]) + 0.25
                waited = max(0.0, wait)
                await asyncio.sleep(waited)
                now = time.monotonic()
                while self._sent and now - self._sent[0] > 60:
                    self._sent.popleft()
            self._sent.append(time.monotonic())
        return waited


class DiscordNotifier:
    def __init__(self, config: ConfigStore, db: Database):
        self.config = config
        self.db = db
        self.limiter = RateLimiter(int(config.get("notifications.max_per_minute", 20)))
        #: Anti-spam du journal : même erreur pour le même profil = 1 ligne / min.
        self._log_throttle: dict[tuple[str, str], float] = {}
        self._client: httpx.AsyncClient | None = None
        #: Mode test (tests automatisés uniquement) : journalise au lieu de poster.
        self.dry_run = False
        self.stats = {"sent": 0, "failed": 0, "last_error": None, "last_sent_at": None}

    async def close(self) -> None:
        if self._client:
            await self._client.aclose()
            self._client = None

    async def _http(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(timeout=15, follow_redirects=True)
        return self._client

    # ── Résolution du webhook ───────────────────────────────────────────
    def webhook_for(self, profile: dict | None) -> str:
        if profile and profile.get("webhook"):
            return str(profile["webhook"])
        return str(self.config.get("discord.default_webhook", "") or "")

    # ── Envoi bas niveau ────────────────────────────────────────────────
    async def _post(self, webhook: str, payload: dict) -> tuple[bool, str | None]:
        if self.dry_run:
            embed = (payload.get("embeds") or [{}])[0]
            self.stats["sent"] += 1
            self.stats["last_sent_at"] = utcnow_iso()
            self.db.log(
                "INFO",
                f"[DÉMO] Alerte simulée : « {embed.get('title', '')[:80]} » "
                f"→ {embed.get('url', '')} (aucun envoi Discord).",
                source="notify",
            )
            return True, None
        if not webhook:
            return False, "Aucun webhook Discord configuré (profil ou global)."
        if not self.config.get("notifications.enabled", True):
            return False, "Notifications désactivées dans la configuration."
        attempts = max(1, int(self.config.get("notifications.max_attempts", 5)))
        client = await self._http()
        last_error = "erreur inconnue"
        for attempt in range(attempts):
            try:
                await self.limiter.acquire()
                response = await client.post(webhook, json=payload)
                if response.status_code in {200, 204}:
                    self.stats["sent"] += 1
                    self.stats["last_sent_at"] = utcnow_iso()
                    return True, None
                if response.status_code == 429:
                    retry_after = 1.0
                    try:
                        retry_after = float(response.json().get("retry_after", 1.0))
                    except Exception:
                        pass
                    await asyncio.sleep(min(max(retry_after, 0.5), 15))
                    last_error = "Discord rate limit (429)"
                    continue
                if response.status_code in {400, 401, 403, 404}:
                    detail = response.text[:180]
                    last_error = f"HTTP {response.status_code} : {detail}"
                    break  # erreur définitive (webhook invalide / supprimé)
                last_error = f"HTTP {response.status_code} : {response.text[:120]}"
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"[:200]
            await asyncio.sleep(min(2**attempt, 20))
        self.stats["failed"] += 1
        self.stats["last_error"] = last_error
        return False, last_error

    # ── Carte de l'annonce ──────────────────────────────────────────────
    def build_embed(self, profile: dict | None, item: dict) -> dict:
        profile_name = (profile or {}).get("name") or "Recherche"
        currency = str(item.get("currency") or "EUR").upper()
        price = format_money(item.get("price"), currency)
        price_value = f"**{price}**\nDevise : `{currency}`"
        if (
            item.get("total_price")
            and item.get("price") is not None
            and abs(float(item["total_price"]) - float(item["price"])) > 0.001
        ):
            price_value += (
                f"\n*(soit {format_money(item['total_price'], currency)} port inclus)*"
            )

        fields: list[dict[str, Any]] = [
            {"name": "💰 Prix", "value": price_value, "inline": True},
            {
                "name": "🏷️ Marque",
                "value": item.get("brand") or "Non précisée",
                "inline": True,
            },
            {"name": "📏 Taille", "value": item.get("size") or "—", "inline": True},
            {"name": "✨ État", "value": item.get("condition") or "—", "inline": True},
        ]

        seller_name = item.get("seller_name") or "Vendeur inconnu"
        seller_url = item.get("seller_url") or ""
        seller_value = (
            f"[{seller_name}]({seller_url})" if seller_url else f"**{seller_name}**"
        )
        fields.append({"name": "👤 Vendeur", "value": seller_value, "inline": True})

        rating = item.get("seller_rating")
        feedback = item.get("seller_feedback")
        rating_value = stars(rating) if rating is not None else "Note indisponible"
        if feedback is not None:
            rating_value += f"\n{feedback} avis"
        fields.append({"name": "⭐ Réputation", "value": rating_value, "inline": True})

        if item.get("favourites") is not None:
            fields.append(
                {"name": "❤️ Favoris", "value": str(item["favourites"]), "inline": True}
            )

        title = (item.get("title") or "Annonce Vinted").strip()[:250]
        embed: dict[str, Any] = {
            "title": title,
            "color": VINTED_TEAL,
            "fields": fields,
            "footer": {"text": f"Profil : {profile_name}  •  Vinted Sniper"},
            "timestamp": utcnow_iso(),
        }
        url = str(item.get("url") or "")
        if url.startswith(("http://", "https://")):
            embed["url"] = url
        if item.get("image_url"):
            embed["image"] = {"url": item["image_url"]}
        if item.get("description"):
            excerpt = item["description"].strip().replace("\n", " ")
            embed["description"] = (
                (excerpt[:280] + "…") if len(excerpt) > 280 else excerpt
            )
        return embed

    async def notify(self, profile: dict | None, item: dict) -> tuple[bool, str | None]:
        webhook = self.webhook_for(profile)
        embed = self.build_embed(profile, item)
        mention = str(self.config.get("discord.mention", "") or "").strip()
        role_ids = re.findall(r"<@&(\d+)>", mention)
        if role_ids:
            allowed_mentions: dict[str, Any] = {"parse": [], "roles": role_ids}
        elif "@everyone" in mention or "@here" in mention:
            allowed_mentions = {"parse": ["everyone"]}
        else:
            allowed_mentions = {"parse": []}
        payload: dict[str, Any] = {
            "embeds": [embed],
            "username": self.config.get("discord.username", "Vinted Sniper")
            or "Vinted Sniper",
            "allowed_mentions": allowed_mentions,
        }
        avatar = self.config.get("discord.avatar_url", "")
        if avatar:
            payload["avatar_url"] = avatar
        if mention:
            payload["content"] = mention

        ok, error = await self._post(webhook, payload)
        label = (profile or {}).get("name", "profil")
        if ok and not self.dry_run:
            self.db.log(
                "INFO",
                f"🔔 Alerte Discord envoyée — « {item.get('title', '')[:70]} » "
                f"({format_money(item.get('price'), item.get('currency', 'EUR'))}) "
                f"[{label}]",
                profile_id=(profile or {}).get("id"),
            )
        elif not ok and self._should_log(label, str(error or "")):
            self.db.log(
                "ERROR",
                f"Échec notification Discord [{label}] : {error} "
                f"(webhook {mask_webhook(webhook) or 'absent'})",
                profile_id=(profile or {}).get("id"),
            )
        return ok, error

    def _should_log(self, label: str, error: str, window: float = 60.0) -> bool:
        """Une seule ligne de journal par minute et par cause.

        Sans webhook configuré, un scan peut produire des dizaines d'échecs
        identiques : le journal devient illisible et masque les vrais problèmes.
        """
        now = time.monotonic()
        key = (label, error[:80])
        # Pas de valeur par défaut à 0.0 : sur une machine fraîchement démarrée,
        # ``time.monotonic()`` peut être inférieur à la fenêtre (60 s) et la
        # première erreur serait alors silencieusement avalée — bug observé en
        # CI (« 0 ligne de journal » au lieu de 1).
        last = self._log_throttle.get(key)
        if last is not None and now - last < window:
            return False
        self._log_throttle[key] = now
        if len(self._log_throttle) > 200:  # ménage
            for stale in [k for k, v in self._log_throttle.items() if now - v > window]:
                self._log_throttle.pop(stale, None)
        return True

    async def send_test(
        self, webhook: str = "", profile_name: str = "Test"
    ) -> tuple[bool, str | None]:
        webhook = webhook or str(self.config.get("discord.default_webhook", "") or "")
        embed = {
            "title": "✅ Vinted Sniper est connecté",
            "description": (
                "Ce salon recevra désormais les alertes de vos profils de veille.\n"
                "Chaque annonce arrive sous forme d'embed : prix, marque, taille, état, "
                "vendeur, note, photo HD et lien direct."
            ),
            "color": COLOR_PRICE_DROP,
            "fields": [
                {"name": "Profil", "value": profile_name, "inline": True},
                {"name": "Statut", "value": "Webhook opérationnel", "inline": True},
            ],
            "footer": {"text": "Vinted Sniper  •  test de connexion"},
            "timestamp": utcnow_iso(),
        }
        payload = {
            "embeds": [embed],
            "username": self.config.get("discord.username", "Vinted Sniper")
            or "Vinted Sniper",
        }
        return await self._post(webhook, payload)
