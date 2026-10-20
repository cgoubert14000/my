"""Couche réseau : sessions cookies, rotation de User-Agents & de proxys.

Trois responsabilités :

* ``ProxyPool``    — stocke, teste, met en quarantaine et renouvelle les proxys ;
* ``HttpClient``   — requêtes HTTP avec cookies de session, UA aléatoires,
                     détection Cloudflare / Datadome et « smart sleep » ;
* ``warm_up``      — obtention d'une session anonyme propre (``_vinted_fr_session``).
"""

from __future__ import annotations

import asyncio
import random
import re
import time
from dataclasses import dataclass, field
from collections.abc import Callable
from typing import Any
from urllib.parse import urlparse

from .config import ConfigStore
from .database import Database
from .utils import origin_of

# ── Transport : curl_cffi (empreinte TLS Chrome) si dispo, sinon httpx ─────────
try:  # pragma: no cover - dépend de l'environnement
    from curl_cffi.requests import AsyncSession as _CurlSession  # type: ignore

    TRANSPORT = "curl_cffi"
except Exception:  # pragma: no cover
    _CurlSession = None  # type: ignore
    TRANSPORT = "httpx"

import httpx  # noqa: E402  (toujours disponible : sert aussi à la découverte de proxys)

#: Marqueurs de page de blocage. ⚠️ Ne JAMAIS y mettre le simple mot
#: « datadome » : la page catalogue normale charge le script Datadome, donc
#: elle le contient — la requête était alors déclarée « bloquée » alors que
#: Vinted avait répondu normalement (et aucune annonce n'était jamais lue).
BLOCK_MARKERS = (
    "just a moment",
    "attention required",
    "cf-browser-verification",
    "challenge-platform",
    "captcha-delivery",
    "geo.captcha-delivery",
    "access to this page has been denied",
    "pardon our interruption",
    "enable javascript and cookies",
    "unusual traffic",
    "request blocked",
    "you have been blocked",
)

BLOCK_STATUSES = {401, 403, 407, 429, 451, 503}

#: Marqueurs propres à la page de vérification Datadome (défi JS).
CHALLENGE_MARKERS = ("captcha-delivery", "geo.captcha-delivery", "dd-captcha")

#: Signes qu'une VRAIE page de résultats a été servie (donc pas un blocage).
GRID_PRESENT_MARKERS = ('data-testid="grid-item"', "product-item-id-")


def _same_origin(referer: str, url: str) -> bool:
    """Le Referer appartient-il au même site que l'URL demandée ?"""
    try:
        return urlparse(referer).netloc == urlparse(url).netloc
    except Exception:  # pragma: no cover - URL exotique
        return False


def _is_challenge(text: str) -> bool:
    """La page renvoyée est-elle le défi navigateur Datadome ?"""
    sample = (text or "")[:20000].lower()
    return any(marker in sample for marker in CHALLENGE_MARKERS)


#: Marqueurs d'une vérification **interactive** (Cloudflare / Datadome) :
#: impossible à passer sans navigateur, et insister ne fait qu'allonger le ban.
INTERACTIVE_MARKERS = (
    "challenge-platform",
    "captcha-delivery",
    "dd-captcha",
    "just a moment",
    "cf-chl",
)


def is_interactive_challenge(text: str) -> bool:
    """La page demande-t-elle une vérification navigateur (pas un simple 429) ?"""
    sample = (text or "")[:20000].lower()
    return any(marker in sample for marker in INTERACTIVE_MARKERS)


def block_reason(text: str) -> str:
    """Quel marqueur a fait conclure à un blocage (utile dans le journal)."""
    sample = (text or "")[:20000].lower()
    for marker in CHALLENGE_MARKERS:
        if marker in sample:
            return f"défi Datadome « {marker} »"
    for marker in BLOCK_MARKERS:
        if marker in sample:
            return f"page « {marker} »"
    return "réponse inattendue"

ACCEPT_LANGUAGE = "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"


# ── Proxys ────────────────────────────────────────────────────────────────────


@dataclass
class ProxyEntry:
    url: str
    source: str = "configured"  # configured | discovered
    successes: int = 0
    failures: int = 0
    consecutive_failures: int = 0
    banned_until: float = 0.0
    banned_count: int = 0
    last_used: float = 0.0

    @property
    def available(self) -> bool:
        return self.banned_until <= time.time()


def mask_proxy(url: str) -> str:
    """Cache le mot de passe d'un proxy avant affichage/log."""
    return re.sub(r"://([^/@:\s]+):([^/@\s]+)@", r"://\1:•••@", url)


def normalize_proxy(value: str) -> str | None:
    raw = (value or "").strip()
    if not raw or raw.startswith("#"):
        return None
    raw = raw.split("#", 1)[0].strip()
    if "://" not in raw:
        raw = "http://" + raw
    parsed = urlparse(raw)
    if parsed.scheme not in {"http", "https", "socks4", "socks5", "socks5h"}:
        return None
    if not parsed.hostname:
        return None
    try:
        port = parsed.port
    except ValueError:
        return None
    if not port or not (1 <= port <= 65535):
        return None
    if parsed.username:
        credentials = f"{parsed.username}:{parsed.password or ''}@"
    else:
        credentials = ""
    return f"{parsed.scheme}://{credentials}{parsed.hostname}:{port}"


class ProxyPool:
    """File de proxys auto-nettoyante (quarantaine, purge, santé)."""

    def __init__(self, config: ConfigStore, db: Database):
        self.config = config
        self.db = db
        self._lock = asyncio.Lock()
        self._entries: dict[str, ProxyEntry] = {}
        self._last_discovery = 0.0
        self.discovery_error: str | None = None
        self._load_configured()

    # ── Gestion ──────────────────────────────────────────────────────────
    def _load_configured(self) -> None:
        for raw in self.config.get("proxies.list", []) or []:
            url = normalize_proxy(str(raw))
            if url:
                self._entries[url] = ProxyEntry(url=url, source="configured")

    @property
    def enabled(self) -> bool:
        return bool(self.config.get("proxies.enabled", False))

    @property
    def prefer_proxies(self) -> bool:
        return bool(self.config.get("proxies.prefer_proxies", False))

    async def reload(self) -> None:
        """Reconstruit les proxys configurables (les découverts restent en place)."""
        async with self._lock:
            self._entries = {
                url: entry
                for url, entry in self._entries.items()
                if entry.source == "discovered"
            }
            added = 0
            for raw in self.config.get("proxies.list", []) or []:
                url = normalize_proxy(str(raw))
                if url and url not in self._entries:
                    self._entries[url] = ProxyEntry(url=url)
                    added += 1
            total = len(self._entries)
        self.db.log(
            "INFO",
            f"Pool de proxys rechargé : {added} configuré(s), {total} au total.",
            source="proxy",
        )

    async def add(self, values: list[str], source: str = "discovered") -> int:
        added = 0
        async with self._lock:
            limit = int(self.config.get("proxies.max_pool_size", 40))
            for raw in values:
                url = normalize_proxy(raw)
                if not url or url in self._entries:
                    continue
                if (
                    source == "discovered"
                    and len(
                        [e for e in self._entries.values() if e.source == "discovered"]
                    )
                    >= limit
                ):
                    break
                self._entries[url] = ProxyEntry(url=url, source=source)
                added += 1
        if added:
            self.db.log(
                "INFO",
                f"{added} nouveau(x) proxy(s) ajouté(s) au pool.",
                source="proxy",
            )
        return added

    async def remove(self, url: str, reason: str = "") -> None:
        async with self._lock:
            entry = self._entries.pop(url, None)
        if entry:
            self.db.log(
                "WARNING",
                f"Proxy purgé ({entry.source}) : {mask_proxy(url)} {reason}".strip(),
                source="proxy",
            )

    async def pick(self, exclude: set[str] | None = None) -> ProxyEntry | None:
        exclude = exclude or set()
        async with self._lock:
            available = [
                e
                for e in self._entries.values()
                if e.available and e.url not in exclude
            ]
        if not available:
            return None
        configured = [e for e in available if e.source == "configured"]
        discovered = [e for e in available if e.source == "discovered"]
        # Un proxy configuré (souvent payant, fiable) est favorisé, sauf si
        # l'utilisateur demande explicitement de privilégier la rotation large.
        pool = (
            discovered
            if (discovered and (self.prefer_proxies or not configured))
            else configured
        )
        pool = pool or available
        # Priorité aux proxys qui n'ont jamais échoué, puis tirage aléatoire.
        healthy = [e for e in pool if e.consecutive_failures == 0]
        entry = random.choice(healthy or pool)
        entry.last_used = time.time()
        return entry

    async def report_success(self, url: str | None) -> None:
        if not url:
            return
        async with self._lock:
            entry = self._entries.get(url)
            if entry:
                entry.successes += 1
                entry.consecutive_failures = 0

    async def report_failure(self, url: str | None, reason: str = "") -> None:
        if not url:
            return
        cooldown = int(self.config.get("proxies.cooldown_seconds", 300))
        ban_after = int(self.config.get("proxies.ban_after_failures", 3))
        async with self._lock:
            entry = self._entries.get(url)
            if not entry:
                return
            entry.failures += 1
            entry.consecutive_failures += 1
            if entry.consecutive_failures >= ban_after:
                entry.banned_count += 1
                factor = min(2 ** (entry.banned_count - 1), 8)
                entry.banned_until = time.time() + cooldown * factor
                entry.consecutive_failures = 0
                should_purge = entry.source == "discovered" and entry.banned_count >= 2
            else:
                entry.banned_until = time.time() + min(cooldown / ban_after, 60)
                should_purge = False
        if should_purge:
            await self.remove(url, f"(défaillant ×{ban_after}, {reason})")

    async def reset_bans(self) -> None:
        async with self._lock:
            for entry in self._entries.values():
                entry.banned_until = 0.0
                entry.consecutive_failures = 0

    def stats(self) -> dict[str, Any]:
        now = time.time()
        entries = list(self._entries.values())
        healthy = [e for e in entries if e.available]
        return {
            "enabled": self.enabled,
            "prefer_proxies": self.prefer_proxies,
            "total": len(entries),
            "available": len(healthy),
            "quarantined": len(entries) - len(healthy),
            "configured": len([e for e in entries if e.source == "configured"]),
            "discovered": len([e for e in entries if e.source == "discovered"]),
            "last_discovery": self._last_discovery or None,
            "discovery_error": self.discovery_error,
            "proxies": [
                {
                    "url": mask_proxy(e.url),
                    "source": e.source,
                    "successes": e.successes,
                    "failures": e.failures,
                    "available": e.available,
                    "quarantine_left": max(0, int(e.banned_until - now)),
                }
                for e in sorted(entries, key=lambda e: (e.source, e.url))[:80]
            ],
        }

    async def discover(self, client: "HttpClient", force: bool = False) -> int:
        """Récupère des proxys publics ; silencieux en cas d'échec."""
        if not self.config.get("proxies.auto_discover", True):
            return 0
        interval = int(self.config.get("proxies.discover_interval_seconds", 600))
        if not force and time.time() - self._last_discovery < interval:
            return 0
        self._last_discovery = time.time()
        found: list[str] = []
        for source in self.config.get("proxies.sources", []) or []:
            try:
                response = await client.get(
                    str(source), use_proxy=False, attempts=1, timeout=10, quiet=True
                )
                if not response.ok:
                    continue
                for match in re.finditer(
                    r"(?:socks[45]h?|https?)://[^\s\"'<>]+|"
                    r"\b(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}\b",
                    response.text,
                ):
                    url = normalize_proxy(match.group(0))
                    if url:
                        found.append(url)
            except Exception as exc:  # réseau instable : on continue
                self.discovery_error = str(exc)[:200]
                continue
        self.discovery_error = None
        random.shuffle(found)
        total = await self.add(found[:200])
        if total:
            self.db.log(
                "INFO",
                f"Découverte auto : {total} proxy(s) ajouté(s) au pool.",
                source="proxy",
            )
            if not self.config.get("proxies.enabled", False):
                # Piège classique : un pool rempli mais inutilisé, donc tout
                # part en direct et l'IP personnelle prend les blocages.
                self.db.log(
                    "WARNING",
                    "Proxys découverts mais désactivés : les requêtes partent en direct "
                    "(votre IP). Cochez « Utiliser les proxys » dans les réglages pour les employer.",
                    source="proxy",
                )
        return total


# ── Réponses ──────────────────────────────────────────────────────────────────


@dataclass
class HttpResponse:
    url: str
    status: int = 0
    text: str = ""
    headers: dict[str, str] = field(default_factory=dict)
    proxy: str | None = None
    error: str | None = None
    blocked: bool = False
    elapsed_ms: int = 0
    attempts: int = 1

    @property
    def ok(self) -> bool:
        return self.error is None and 200 <= self.status < 300 and not self.blocked

    def json(self) -> Any:
        import json

        try:
            return json.loads(self.text)
        except Exception:
            return None

    @property
    def short_error(self) -> str:
        if self.error:
            return self.error
        if self.blocked:
            # On nomme la cause : « just a moment », « captcha-delivery »…
            # C'est ce qui permet de distinguer un quota épuisé d'un vrai défi
            # navigateur, et donc de savoir s'il faut attendre ou changer d'IP.
            reason = block_reason(self.text or "")
            return f"blocage anti-bot (HTTP {self.status} — {reason})"
        return f"HTTP {self.status}"


# ── Client HTTP ───────────────────────────────────────────────────────────────


class HttpClient:
    def __init__(
        self,
        config: ConfigStore,
        db: Database,
        on_block: Callable[[str], None] | None = None,
    ):
        self.config = config
        self.db = db
        self.on_block = on_block
        self.proxies = ProxyPool(config, db)
        self._ua_index = 0
        #: Une seule identité (User-Agent) par domaine, tant que la session vit.
        #: Datadome lie son cookie à l'empreinte du navigateur : changer d'UA
        #: entre deux requêtes tout en gardant les cookies = incohérence
        #: immédiate, donc nouveau défi à chaque passage.
        self._identities: dict[str, str] = {}
        self._supports_discard_cookies = True
        self._cookies: dict[str, dict[str, str]] = {}
        self._sessions: dict[tuple[str, str | None], Any] = {}
        self._httpx_clients: dict[str | None, httpx.AsyncClient] = {}
        self._warm_lock = asyncio.Lock()
        self._warm_at: dict[str, float] = {}
        #: Diagnostic : peu de tentatives, pauses courtes (réponse rapide à l'utilisateur).
        self.fast_fail = False
        self._stats = {
            "requests": 0,
            "ok": 0,
            "blocked": 0,
            "errors": 0,
            "last_block_at": None,
            "last_ok_at": None,
            "cooldown_until": 0.0,
            "current_proxy": None,
            "session_renewals": 0,
        }

    # ── Infra ────────────────────────────────────────────────────────────
    @property
    def transport(self) -> str:
        return TRANSPORT

    def stats(self) -> dict[str, Any]:
        stats = dict(self._stats)
        stats["cooldown_left"] = max(0, int(stats["cooldown_until"] - time.time()))
        stats["transport"] = TRANSPORT
        stats["proxy_pool"] = self.proxies.stats()
        stats["cookies"] = {
            domain: sorted(jar) for domain, jar in self._cookies.items()
        }
        return stats

    def _identity_for(self, netloc: str) -> str:
        """User-Agent stable par domaine (vraie session de navigateur)."""
        ua = self._identities.get(netloc)
        if not ua:
            ua = self._user_agent()
            self._identities[netloc] = ua
        return ua

    def rotate_identity(self, netloc: str) -> None:
        """Nouvelle identité : à faire seulement quand la session est jetée."""
        self._identities.pop(netloc, None)

    def _user_agent(self) -> str:
        agents = self.config.get("http.user_agents", []) or [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        ]
        # Rotation déterministe : évite de changer d'UA à chaque requête d'un
        # même scan (une session = un navigateur cohérent).
        self._ua_index = (self._ua_index + 1) % len(agents)
        return agents[self._ua_index]

    def _headers(
        self,
        url: str,
        extra: dict[str, str] | None = None,
        ua: str | None = None,
        referer: str | None = None,
    ) -> dict[str, str]:
        headers = {
            "User-Agent": ua or self._user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": ACCEPT_LANGUAGE,
            "Accept-Encoding": (
                "gzip, deflate, br" if _CurlSession is not None else "gzip, deflate"
            ),
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": (
                "same-origin" if referer and _same_origin(referer, url) else "none"
            ),
            "Sec-Fetch-User": "?1",
            "Referer": referer or origin_of(url) + "/",
        }
        if extra:
            headers.update({k: v for k, v in extra.items() if v})
        return headers

    def _cookie_header(self, url: str) -> str | None:
        jar = self._cookies.get(urlparse(url).netloc)
        if not jar:
            return None
        return "; ".join(f"{key}={value}" for key, value in jar.items())

    def _store_cookies(self, url: str, response: Any) -> None:
        netloc = urlparse(url).netloc
        jar = self._cookies.setdefault(netloc, {})
        cookies = getattr(response, "cookies", None)
        if cookies is None:
            return
        extracted: dict[str, str] = {}
        try:
            for item in cookies.jar:  # http.cookiejar.Cookie
                extracted[item.name] = item.value
        except Exception:
            pass
        if not extracted:
            try:
                if hasattr(cookies, "get_dict"):
                    extracted = dict(cookies.get_dict())
                elif isinstance(cookies, dict):
                    extracted = dict(cookies)
            except Exception:
                pass
        jar.update(extracted)

    async def _session(self, proxy: str | None) -> Any:
        """Session curl_cffi réutilisée (pool de connexions + cookies libcurl)."""
        key = (self.config.get("http.impersonate", "chrome124"), proxy)
        session = self._sessions.get(key)
        if session is None:
            session = _CurlSession(  # type: ignore[misc]
                impersonate=key[0],
                proxy=proxy,
                timeout=int(self.config.get("http.timeout_seconds", 25)),
                verify=True,
            )
            self._sessions[key] = session
        return session

    async def _httpx_client(self, proxy: str | None) -> httpx.AsyncClient:
        client = self._httpx_clients.get(proxy)
        if client is None:
            client = httpx.AsyncClient(
                proxy=proxy,
                timeout=int(self.config.get("http.timeout_seconds", 25)),
                follow_redirects=True,
                # Pas de HTTP/2 : évite la dépendance optionnelle `h2`.
                http2=False,
            )
            self._httpx_clients[proxy] = client
        return client

    async def _send(
        self,
        method: str,
        url: str,
        headers: dict[str, str],
        proxy: str | None,
        timeout: int,
    ) -> tuple[int, str, dict[str, str], Any]:
        if _CurlSession is not None:
            session = await self._session(proxy)
            options = {
                "headers": headers,
                "timeout": timeout,
                "allow_redirects": True,
            }
            if self._supports_discard_cookies:
                # On gère nous-mêmes le pot de cookies : libcurl ne doit jamais
                # renvoyer un ancien cookie de session par-dessus le nôtre.
                try:
                    response = await session.request(
                        method, url, discard_cookies=True, **options
                    )
                except TypeError:
                    # Ancienne version de curl_cffi sans cette option.
                    self._supports_discard_cookies = False
                    response = await session.request(method, url, **options)
            else:
                response = await session.request(method, url, **options)
            body = response.text or ""
            headers_out = {str(k).lower(): str(v) for k, v in response.headers.items()}
            return int(response.status_code), body, headers_out, response

        client = await self._httpx_client(proxy)
        response = await client.request(method, url, headers=headers, timeout=timeout)
        return (
            int(response.status_code),
            response.text or "",
            {str(k).lower(): str(v) for k, v in response.headers.items()},
            response,
        )

    def block_cooldown_left(self, seconds: float = 25.0) -> float:
        """Secondes restantes avant de pouvoir réessayer après un blocage."""
        last = float(self._stats.get("last_block_at") or 0)
        if not last:
            return 0.0
        return max(0.0, float(seconds) - (time.time() - last))

    def recently_blocked(self, seconds: float = 90.0) -> bool:
        """Un blocage a-t-il eu lieu il y a moins de ``seconds`` ?

        Pendant une vague de blocages (Datadome), mieux vaut **ne pas** lancer
        les requêtes de confort (fiche article, profil vendeur) : elles
        n'aboutissent pas et aggravent la détection.
        """
        last = float(self._stats.get("last_block_at") or 0)
        return bool(last) and (time.time() - last) < float(seconds)

    @staticmethod
    def _looks_blocked(text: str) -> bool:
        """Page de blocage ? La présence de la grille d'annonces tranche.

        Un vrai catalogue contient ``data-testid="grid-item"`` : dans ce cas,
        aucun marqueur ne doit faire conclure à un blocage. Sans cette garde,
        le mot « datadome » présent dans le HTML normal suffisait à déclarer
        chaque page bloquée — symptôme observé : « blocage anti-bot (HTTP 200) »
        à chaque scan, zéro annonce, session pourtant valide.
        """
        sample = (text or "").lower()
        if GRID_PRESENT_MARKERS and any(m in sample for m in GRID_PRESENT_MARKERS):
            return False
        return any(marker in sample[:20000] for marker in BLOCK_MARKERS)

    async def _smart_sleep(
        self, attempt: int, reason: str, profile_id: int | None = None
    ) -> None:
        backoff = self.config.get("http.block_backoff_seconds", [30, 60, 120, 300]) or [
            30
        ]
        seconds = backoff[min(attempt, len(backoff) - 1)]
        # Jitter : évite les reprises synchronisées (signature de bot).
        seconds = round(seconds * random.uniform(0.8, 1.3), 1)
        if "200" in reason:
            # Page de vérification (HTTP 200) : ce n'est pas un quota épuisé.
            # Attendre 30-60 s ne sert à rien et bloque le reste du programme.
            seconds = min(seconds, 5.0)
        self._stats["cooldown_until"] = time.time() + seconds
        self.db.log(
            "WARNING", f"Smart sleep {seconds:.0f}s — {reason}", profile_id=profile_id
        )
        await asyncio.sleep(seconds)

    async def _reset_transports(self) -> None:
        """Ferme les sessions : libcurl repart avec un pot de cookies vierge."""
        for session in list(self._sessions.values()):
            try:
                await session.close()
            except Exception:
                pass
        for client in list(self._httpx_clients.values()):
            try:
                await client.aclose()
            except Exception:
                pass
        self._sessions.clear()
        self._httpx_clients.clear()

    async def close(self) -> None:
        for session in self._sessions.values():
            try:
                await session.close()
            except Exception:
                pass
        for client in self._httpx_clients.values():
            try:
                await client.aclose()
            except Exception:
                pass
        self._sessions.clear()
        self._httpx_clients.clear()

    def import_session(
        self,
        cookies: dict[str, str] | None = None,
        user_agent: str = "",
        netloc: str = "www.vinted.fr",
    ) -> dict[str, Any]:
        """Injecte une session obtenue dans un **vrai navigateur**.

        ``cf_clearance`` (et le cookie ``datadome``) sont liés à l'adresse IP
        *et* au User-Agent qui les ont obtenus : les deux arrivent donc
        ensemble, et l'identité du domaine devient celle du navigateur. Le
        refroidissement en cours est levé : on a justement de quoi repasser.
        """
        netloc = (netloc or "www.vinted.fr").lower()
        jar = self._cookies.setdefault(netloc, {})
        fresh = {
            str(name): str(value)
            for name, value in (cookies or {}).items()
            if str(name).strip() and str(value)
        }
        jar.update(fresh)
        if user_agent:
            # Même UA que celui qui a obtenu le cookie : sinon Cloudflare
            # considère la clearance comme volée et redemande une vérification.
            self._identities[netloc] = user_agent
        self._stats["cooldown_until"] = 0.0
        self._stats["browser_session_at"] = time.time()
        self._warm_at.pop(netloc, None)
        return {
            "netloc": netloc,
            "imported": len(fresh),
            "cookies": len(jar),
            "user_agent": user_agent,
            "clearance": bool(
                fresh.get("cf_clearance") or fresh.get("cf_clearance_legacy")
            ),
        }

    # ── Requête principale ───────────────────────────────────────────────
    async def get(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        use_proxy: bool | None = None,
        attempts: int | None = None,
        timeout: int | None = None,
        quiet: bool = False,
        profile_id: int | None = None,
        referer: str | None = None,
    ) -> HttpResponse:
        attempts = max(1, int(attempts or self.config.get("http.max_retries", 3) + 1))
        timeout = int(timeout or self.config.get("http.timeout_seconds", 25))
        if self.fast_fail:
            attempts = min(attempts, 2)
            timeout = min(timeout, 12)
        if use_proxy is None:
            use_proxy = self.proxies.enabled
        want_proxy = bool(use_proxy) and self.proxies.enabled

        tried: set[str] = set()
        last = HttpResponse(url=url)
        netloc = urlparse(url).netloc
        ua = self._identity_for(netloc)

        for attempt in range(attempts):
            proxy_entry = await self.proxies.pick(tried) if want_proxy else None
            proxy = proxy_entry.url if proxy_entry else None
            if proxy:
                tried.add(proxy)
            elif want_proxy and attempt >= 1 and len(tried) >= 1:
                # Pool épuisé : on retombe proprement en direct.
                want_proxy = False

            request_headers = self._headers(url, headers, ua=ua, referer=referer)
            cookie = self._cookie_header(url)
            if cookie:
                request_headers["Cookie"] = cookie

            self._stats["requests"] += 1
            started = time.perf_counter()
            try:
                status, text, response_headers, raw = await self._send(
                    "GET", url, request_headers, proxy, timeout
                )
                self._store_cookies(url, raw)
                elapsed = int((time.perf_counter() - started) * 1000)
                blocked = status in BLOCK_STATUSES or (
                    status == 200 and self._looks_blocked(text)
                )
                last = HttpResponse(
                    url=url,
                    status=status,
                    text=text,
                    headers=response_headers,
                    proxy=proxy,
                    blocked=blocked,
                    elapsed_ms=elapsed,
                    attempts=attempt + 1,
                )
                if not blocked:
                    self._stats["ok"] += 1
                    self._stats["last_ok_at"] = time.time()
                    self._stats["current_proxy"] = proxy
                    await self.proxies.report_success(proxy)
                    return last

                # ── Blocage : on purge, on change d'identité, on patiente ──
                self._stats["blocked"] += 1
                self._stats["last_block_at"] = time.time()
                await self.proxies.report_failure(proxy, f"HTTP {status}")
                # Nouvel UA seulement si la session est réellement jetée.
                if status in {403, 429, 451}:
                    self._identities.pop(netloc, None)
                    ua = self._identity_for(netloc)
                # Blocage « dur » (403/429/451) : la session est brûlée, on repart
                # à zéro. Défi Datadome rendu en HTTP 200 : au contraire, on
                # GARDE les cookies — le cookie datadome posé par la page de
                # vérification est justement ce qui permet de repasser ensuite.
                # Les jeter à chaque passage (comportement d'avant) garantissait
                # un nouveau défi à chaque scan.
                if status in {403, 429, 451}:
                    self._cookies.pop(urlparse(url).netloc, {})
                if self.on_block:
                    try:
                        self.on_block(f"HTTP {status} sur {urlparse(url).netloc}")
                    except Exception:
                        pass
                if attempt < attempts - 1:
                    if not quiet:
                        hard = status in {403, 429, 451}
                        if status == 200:
                            detail = block_reason(text)
                        elif hard:
                            detail = "session refusée"
                        else:
                            detail = "page anti-bot"
                        self.db.log(
                            "WARNING",
                            f"Blocage détecté (HTTP {status}, {detail}, "
                            f"proxy={proxy or 'direct'}) → "
                            f"{'purge cookies' if hard else 'cookies conservés'}, "
                            f"tentative {attempt + 2}/{attempts}.",
                            profile_id=profile_id,
                        )
                    await self._smart_sleep(
                        attempt, f"blocage HTTP {status}", profile_id
                    )
                continue

            except Exception as exc:  # timeout, DNS, proxy mort, TLS…
                elapsed = int((time.perf_counter() - started) * 1000)
                self._stats["errors"] += 1
                await self.proxies.report_failure(proxy, str(exc)[:80])
                last = HttpResponse(
                    url=url,
                    proxy=proxy,
                    error=f"{type(exc).__name__}: {exc}"[:200],
                    elapsed_ms=elapsed,
                    attempts=attempt + 1,
                    blocked=False,
                )
                if attempt < attempts - 1:
                    delay = min(2**attempt, 10) + random.uniform(0, 1.5)
                    if not quiet:
                        self.db.log(
                            "WARNING",
                            f"Erreur réseau ({type(exc).__name__}) → nouvelle tentative "
                            f"dans {delay:.1f}s.",
                            profile_id=profile_id,
                        )
                    await asyncio.sleep(delay)

        return last

    # ── Sessions Vinted ──────────────────────────────────────────────────
    async def warm_up(
        self,
        url: str,
        *,
        force: bool = False,
        profile_id: int | None = None,
        attempts: int = 2,
    ) -> bool:
        """Ouvre une session anonyme propre sur le domaine Vinted ciblé."""
        origin = origin_of(url)
        async with self._warm_lock:
            netloc = urlparse(origin).netloc
            jar = self._cookies.get(netloc, {})
            now = time.time()
            recently_warmed = (
                netloc in self._warm_at and now - self._warm_at[netloc] < 600
            )
            if jar and not force and recently_warmed:
                return True
            if force:
                self._cookies.pop(netloc, None)
                self.rotate_identity(netloc)
                self._stats["session_renewals"] += 1
                await (
                    self._reset_transports()
                )  # oublie aussi le pot de cookies de libcurl
                self.db.log(
                    "INFO",
                    f"Renouvellement de session sur {netloc}…",
                    profile_id=profile_id,
                )
            response = await self.get(
                origin + "/",
                attempts=max(1, int(attempts)),
                quiet=True,
                profile_id=profile_id,
                referer=origin + "/",
            )
            if response.ok and self._cookies.get(netloc):
                self._warm_at[netloc] = now
                self.db.log(
                    "DEBUG",
                    f"Session {netloc} prête ({', '.join(self._cookies[netloc])[:120]}).",
                    profile_id=profile_id,
                )
                return True
            if force:
                self.db.log(
                    "WARNING",
                    f"Impossible d'obtenir une session sur {netloc} "
                    f"({response.short_error}).",
                    profile_id=profile_id,
                )
            return False
