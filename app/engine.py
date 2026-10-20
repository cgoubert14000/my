"""Moteur de veille : ordonnancement, scans, self-healing, alertes.

Boucle principale (« scheduler ») :

* un scan indépendant par profil actif, selon son propre intervalle ;
* concurrence bornée pour ne pas déclencher les protections Vinted ;
* sur 403/429/blocage : rotation proxy + UA, renouvellement de session,
  backoff exponentiel, puis reprise automatique (jamais de crash) ;
* anti-doublon garanti par SQLite, même après redémarrage ;
* premier scan = « baseline » (les annonces existantes sont enregistrées
  silencieusement, seules les nouvelles déclenchent une alerte).
"""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field
from typing import Any

from .config import ConfigStore
from .database import Database
from .filters import MatchResult, matches_profile, needs_description
from .http_client import HttpClient
from .notify import DiscordNotifier
from .utils import domain_of, human_duration, utcnow_iso
from .vinted_api import VintedAPI


@dataclass
class ScanOutcome:
    status: str = "ok"  # ok | blocked | error | empty
    pages: int = 0
    items_seen: int = 0
    new_items: int = 0
    alerts: int = 0
    error: str | None = None
    duration_ms: int = 0
    baseline: bool = False


@dataclass
class EngineStats:
    started_at: float = field(default_factory=time.time)
    scans: int = 0
    scans_failed: int = 0
    items_seen: int = 0
    new_items: int = 0
    alerts_sent: int = 0
    alerts_failed: int = 0
    blocked: int = 0
    last_scan_at: str | None = None
    last_error: str | None = None
    last_block_at: str | None = None


class BotEngine:
    def __init__(
        self,
        config: ConfigStore,
        db: Database,
        client: HttpClient,
        api: VintedAPI,
        notifier: DiscordNotifier,
    ):
        self.config = config
        self.db = db
        self.client = client
        self.api = api
        self.notifier = notifier

        self.stats = EngineStats()
        self.paused = bool(config.get("engine.start_paused", False))
        self._running = False
        self._tasks: list[asyncio.Task] = []
        self._inflight: dict[int, asyncio.Task] = {}
        self._next_run: dict[int, float] = {}
        self._failures: dict[int, int] = {}
        self._warm: dict[str, float] = {}
        self._force_renew: set[str] = set()
        self._global_cooldown_until = 0.0
        self._alert_sem = asyncio.Semaphore(3)
        self._sem: asyncio.Semaphore | None = None

    # ── Cycle de vie ─────────────────────────────────────────────────────
    async def start(self) -> None:
        if self._running:
            return
        self._running = True
        self._sem = asyncio.Semaphore(
            max(1, int(self.config.get("engine.max_concurrent_profiles", 2)))
        )
        self.db.log(
            "INFO",
            f"Moteur démarré (transport {self.client.transport}, "
            f"intervalle par défaut "
            f"{self.config.get('engine.default_interval_seconds')}s).",
            source="engine",
        )
        self._tasks = [
            asyncio.create_task(
                self._watchdog(self._scheduler, "scheduler"), name="scheduler"
            ),
            asyncio.create_task(
                self._watchdog(self._maintenance, "maintenance"), name="maintenance"
            ),
        ]

    async def stop(self) -> None:
        self._running = False
        pending = [*self._tasks, *list(self._inflight.values())]
        for task in pending:
            task.cancel()
        await asyncio.gather(*pending, return_exceptions=True)
        self._tasks.clear()
        self._inflight.clear()
        self.db.log("INFO", "Moteur arrêté proprement.", source="engine")

    def set_paused(self, paused: bool) -> None:
        self.paused = bool(paused)
        self.db.log(
            "INFO", "Moteur en pause." if paused else "Moteur relancé.", source="engine"
        )

    async def apply_config(self) -> None:
        """Répercute les réglages (concurrence, délais) sans redémarrer."""
        concurrency = max(1, int(self.config.get("engine.max_concurrent_profiles", 2)))
        self._sem = asyncio.Semaphore(concurrency)

    async def renew_sessions(self) -> list[str]:
        """Force une nouvelle session Vinted (nouveaux cookies) sur chaque domaine."""
        domains = sorted(
            {
                domain_of(profile.get("url") or "", "www.vinted.fr")
                for profile in self.db.list_profiles(only_active=True)
                if profile.get("url")
            }
        )
        for domain in domains:
            await self.client.warm_up(f"https://{domain}/", force=True)
        self._warm.clear()
        return domains

    async def _watchdog(self, coro_factory, name: str) -> None:
        """Relance la boucle si elle meurt (protection anti-crash ultime)."""
        while self._running:
            try:
                await coro_factory()
            except asyncio.CancelledError:
                raise
            except Exception as exc:  # pragma: no cover - filet de sécurité
                self.stats.last_error = f"{type(exc).__name__}: {exc}"
                self.db.log(
                    "ERROR",
                    f"Boucle « {name} » interrompue ({exc}) → redémarrage dans 5 s.",
                    source="engine",
                )
                await asyncio.sleep(5)

    # ── Ordonnanceur ─────────────────────────────────────────────────────
    async def _scheduler(self) -> None:
        await asyncio.sleep(0.4)  # laisse le dashboard démarrer
        while self._running:
            try:
                await self._schedule_tick()
            except asyncio.CancelledError:
                raise
            except Exception as exc:  # pragma: no cover
                self.db.log("ERROR", f"Ordonnanceur : {exc}", source="engine")
            await asyncio.sleep(1)

    async def _schedule_tick(self) -> None:
        if self.paused or time.time() < self._global_cooldown_until:
            return
        profiles = self.db.list_profiles(only_active=True)
        active_ids = {profile["id"] for profile in profiles}
        # Nettoyage des profils supprimés / désactivés.
        for profile_id in list(self._next_run):
            if profile_id not in active_ids and profile_id not in self._inflight:
                self._next_run.pop(profile_id, None)
                self._failures.pop(profile_id, None)

        now = time.time()
        for profile in profiles:
            profile_id = profile["id"]
            if profile_id in self._inflight:
                continue
            due = self._next_run.get(profile_id)
            if due is None:
                # Premier passage : décalage aléatoire pour lisser les scans.
                self._next_run[profile_id] = now + min(5 + profile_id * 1.5, 20)
                continue
            if now < due:
                continue
            self._launch(profile)

    def _launch(self, profile: dict) -> None:
        profile_id = profile["id"]
        assert self._sem is not None
        task = asyncio.create_task(
            self._run_profile(profile, self._sem), name=f"scan-{profile_id}"
        )
        self._inflight[profile_id] = task
        self._next_run[profile_id] = time.time() + int(
            profile.get("interval_seconds") or 60
        )

        def _cleanup(_task: asyncio.Task, pid: int = profile_id) -> None:
            if self._inflight.get(pid) is _task:
                self._inflight.pop(pid, None)

        task.add_done_callback(_cleanup)

    async def _run_profile(self, profile: dict, sem: asyncio.Semaphore) -> None:
        profile_id = profile["id"]
        async with sem:
            try:
                outcome = await self.scan_profile(profile)
            except asyncio.CancelledError:
                raise
            except Exception as exc:  # un profil ne doit jamais tuer le moteur
                outcome = ScanOutcome(
                    status="error", error=f"{type(exc).__name__}: {exc}"[:300]
                )
                self.db.log(
                    "ERROR",
                    f"Scan du profil « {profile['name']} » en échec : {outcome.error}",
                    profile_id=profile_id,
                )
                self._record_failure(profile, outcome.error or "erreur inconnue")
            interval = int(
                profile.get("interval_seconds")
                or self.config.get("engine.default_interval_seconds", 60)
            )
            if outcome.status == "ok":
                self._failures[profile_id] = 0
                self._next_run[profile_id] = time.time() + interval
            elif outcome.status == "blocked":
                self._record_failure(profile, outcome.error or "blocage")
                domain = domain_of(profile.get("url") or "", "www.vinted.fr")
                self._force_renew.add(domain)
                delay = self._backoff(profile_id, interval)
                self._next_run[profile_id] = time.time() + delay
                self._global_cooldown_until = max(
                    self._global_cooldown_until, time.time() + min(30, delay / 2)
                )
                self.db.log(
                    "WARNING",
                    f"Self-healing : session {domain} programmée pour "
                    f"renouvellement, reprise dans {human_duration(delay)}.",
                    profile_id=profile_id,
                )
            elif outcome.status == "error":
                self._record_failure(profile, outcome.error or "erreur")
                self._next_run[profile_id] = time.time() + self._backoff(
                    profile_id, interval
                )
            else:
                self._failures[profile_id] = 0
                self._next_run[profile_id] = time.time() + interval

    def _backoff(self, profile_id: int, interval: int) -> int:
        failures = self._failures.get(profile_id, 1)
        delay = min(interval * (2 ** min(failures, 4)), 900)
        return max(15, int(delay))

    def _record_failure(self, profile: dict, error: str) -> None:
        if self.paused:
            return
        self._failures[profile["id"]] = self._failures.get(profile["id"], 0) + 1
        self.stats.last_error = error
        self.db.log(
            "WARNING",
            f"Profil « {profile['name']} » en difficulté "
            f"(échec #{self._failures[profile['id']]}) : {error}",
            profile_id=profile["id"],
        )

    # ── Un scan ──────────────────────────────────────────────────────────
    async def scan_profile(self, profile: dict, *, manual: bool = False) -> ScanOutcome:
        started = time.perf_counter()
        profile_id = int(profile["id"])
        domain = domain_of(profile.get("url") or "", "www.vinted.fr")
        outcome = ScanOutcome()
        scan_id = self.db.start_scan(profile_id)
        baseline = (
            not profile.get("baseline_done", False)
            and bool(self.config.get("engine.baseline_first_scan", True))
            and not manual
        )
        outcome.baseline = baseline

        detail_budget = max(
            0, int(self.config.get("engine.detail_budget_per_scan", 15))
        )
        delay = float(self.config.get("engine.min_request_delay", 2.0))
        pages = max(1, min(int(profile.get("pages") or 1), 5))
        per_page = int(self.config.get("engine.max_items_per_page", 96))
        candidates: list[dict] = []

        try:
            await self._ensure_session(domain, profile_id)
            for page in range(1, pages + 1):
                result = await self.api.search(profile, page=page, domain=domain)
                if result.blocked:
                    outcome.status = "blocked"
                    outcome.error = result.error or "blocage anti-bot"
                    self.stats.blocked += 1
                    self.stats.last_block_at = utcnow_iso()
                    break
                if result.error:
                    outcome.status = "error"
                    outcome.error = result.error
                    break

                outcome.pages += 1
                outcome.items_seen += len(result.items)
                if result.empty:
                    self.db.log(
                        "DEBUG",
                        f"« {profile['name']} » : la recherche ne renvoie "
                        f"aucune annonce (page vide, filtres trop stricts ?).",
                        profile_id=profile_id,
                    )
                for item in result.items:
                    if not item.get("id"):
                        continue
                    if self.db.is_seen(profile_id, item["id"]) or self.db.is_ignored(
                        profile_id, item["id"]
                    ):
                        continue
                    preliminary = matches_profile(
                        {
                            **profile,
                            "min_seller_rating": None,
                            "min_seller_feedback": None,
                        },
                        item,
                    )
                    if preliminary.matched:
                        candidates.append(item)
                    elif needs_description(profile) and preliminary.reason.startswith(
                        ("aucun mot-clé", "mots-clés manquants")
                    ):
                        # La description peut contenir le mot-clé attendu.
                        candidates.append(item)
                if len(result.items) < per_page:
                    break
                if page < pages:
                    await asyncio.sleep(delay * (1 + page * 0.2))

            # ── Enrichissement + filtrage fin + alertes ──────────────────
            base_profile = {
                **profile,
                "min_seller_rating": None,
                "min_seller_feedback": None,
            }
            enrich = bool(self.config.get("engine.enrich_sellers", True))
            needs_seller = (
                enrich
                or profile.get("min_seller_rating") is not None
                or profile.get("min_seller_feedback") is not None
            )
            detail_used = 0
            for item in candidates:
                if self.db.is_ignored(profile_id, item["id"]):
                    continue

                fetched_detail = False
                if detail_used < detail_budget:
                    detail_used += 1
                    item = await self.api.enrich_item(item, domain, profile_id)
                    fetched_detail = True
                    await asyncio.sleep(delay * 0.6)
                elif baseline:
                    # Budget épuisé pendant la baseline : on mémorise l'annonce
                    # pour ne pas envoyer une alerte « en retard » plus tard.
                    self.db.add_ignored(profile_id, item["id"], "baseline incomplète")
                    continue

                # 1) Filtres prix / blacklist / whitelist (vendeur inconnu toléré)
                verdict: MatchResult = matches_profile(base_profile, item)
                if not verdict.matched:
                    # Si la description n'a pas pu être lue, on réessaiera au
                    # prochain scan plutôt que d'écarter définitivement.
                    if fetched_detail or not needs_description(profile):
                        self.db.add_ignored(profile_id, item["id"], verdict.reason)
                    self.db.log(
                        "DEBUG",
                        f"Écarté ({verdict.reason}) : « {item.get('title', '')[:60]} »",
                        profile_id=profile_id,
                    )
                    continue

                # 2) Réputation vendeur (cache SQLite, 1 requête max par vendeur)
                if needs_seller:
                    item = await self.api.fetch_seller(item, domain, profile_id)
                    await asyncio.sleep(min(delay * 0.3, 1.0))
                verdict = matches_profile(profile, item)
                if not verdict.matched:
                    if verdict.reason.startswith("nombre d'avis"):
                        # Info vendeur momentanément indisponible : on retentera.
                        self.db.log(
                            "DEBUG",
                            f"Vendeur non vérifié ({verdict.reason}) : "
                            f"« {item.get('title', '')[:60]} »",
                            profile_id=profile_id,
                        )
                    else:
                        self.db.add_ignored(profile_id, item["id"], verdict.reason)
                        self.db.log(
                            "DEBUG",
                            f"Écarté ({verdict.reason}) : "
                            f"« {item.get('title', '')[:60]} »",
                            profile_id=profile_id,
                        )
                    continue

                if not self.db.add_seen(profile_id, item, raw=None):
                    continue  # doublon détecté entre-temps
                outcome.new_items += 1
                self.stats.new_items += 1
                if baseline:
                    self.db.mark_notified(profile_id, item["id"], skipped=True)
                    continue
                ok, error = await self._notify(profile, item)
                if ok:
                    outcome.alerts += 1
                    self.stats.alerts_sent += 1
                else:
                    self.stats.alerts_failed += 1
                self.db.mark_notified(profile_id, item["id"], None if ok else error)

            if outcome.status == "ok" and outcome.items_seen == 0:
                outcome.status = "empty"

        except asyncio.CancelledError:
            raise
        except Exception as exc:
            outcome.status = "error"
            outcome.error = f"{type(exc).__name__}: {exc}"[:300]
            self.db.log(
                "ERROR",
                f"Exception pendant le scan « {profile['name']} » : {outcome.error}",
                profile_id=profile_id,
            )
        finally:
            duration = int((time.perf_counter() - started) * 1000)
            outcome.duration_ms = duration
            self.stats.scans += 1
            self.stats.items_seen += outcome.items_seen
            self.stats.last_scan_at = utcnow_iso()
            if outcome.status in {"error", "blocked"}:
                self.stats.scans_failed += 1
            status = "ok" if outcome.status in {"ok", "empty"} else outcome.status
            self.db.finish_scan(
                scan_id,
                status=status,
                pages=outcome.pages,
                items_seen=outcome.items_seen,
                new_items=outcome.new_items,
                error=outcome.error,
                duration_ms=duration,
            )
            self.db.record_scan(
                profile_id,
                status=status,
                last_error=outcome.error,
                new_items=outcome.new_items,
                found=outcome.new_items > 0,
            )
            if status == "ok" and outcome.items_seen > 0:
                # La baseline n'est consommée que par un scan qui a réellement vu
                # des annonces (pas par une réponse vide / un blocage).
                self.db.mark_baseline_done(profile_id)
            if (
                outcome.status == "empty"
                and outcome.items_seen == 0
                and not outcome.error
            ):
                self.db.log(
                    "WARNING",
                    f"Scan « {profile['name']} » : aucune annonce reçue. "
                    f"Vérifiez l'URL de recherche ou réessayez plus tard "
                    f"(Vinted a peut-être modifié son API).",
                    profile_id=profile_id,
                )
            if baseline:
                self.db.log(
                    "INFO",
                    f"Scan initial (baseline) « {profile['name']} » : "
                    f"{outcome.new_items} annonce(s) enregistrée(s) sans "
                    f"notification.",
                    profile_id=profile_id,
                )
            elif outcome.status in {"ok", "empty"}:
                self.db.log(
                    "INFO",
                    f"Scan « {profile['name']} » : {outcome.items_seen} annonce(s) "
                    f"analysée(s), {outcome.new_items} nouvelle(s), "
                    f"{outcome.alerts} alerte(s), {duration} ms.",
                    profile_id=profile_id,
                )
            else:
                self.db.log(
                    "WARNING",
                    f"Scan « {profile['name']} » interrompu "
                    f"({outcome.status}) : {outcome.error}",
                    profile_id=profile_id,
                )
        return outcome

    async def _notify(self, profile: dict, item: dict) -> tuple[bool, str | None]:
        async with self._alert_sem:
            try:
                return await asyncio.wait_for(
                    self.notifier.notify(profile, item), timeout=90
                )
            except asyncio.TimeoutError:
                return False, "délai d'envoi Discord dépassé"
            except Exception as exc:
                return False, f"{type(exc).__name__}: {exc}"[:200]

    async def _ensure_session(self, domain: str, profile_id: int) -> None:
        refresh = int(self.config.get("http.cookie_refresh_minutes", 25)) * 60
        last = self._warm.get(domain, 0)
        force = domain in self._force_renew or bool(
            last and time.time() - last > refresh
        )
        if force:
            self._force_renew.discard(domain)
        await self.api.ensure_session(
            f"https://{domain}/", profile_id=profile_id, force=force
        )
        self._warm[domain] = time.time()

    # ── Tâches de fond ───────────────────────────────────────────────────
    async def _maintenance(self) -> None:
        last_discovery = 0.0
        last_purge = 0.0
        while self._running:
            try:
                now = time.time()
                if (
                    self.config.get("proxies.enabled", False)
                    and now - last_discovery > 60
                ):
                    last_discovery = now
                    await self.client.proxies.discover(self.client)
                if now - last_purge > 3600:
                    last_purge = now
                    retention = int(self.config.get("engine.retention_days", 30))
                    purged = self.db.purge_seen(retention)
                    self.db.purge_logs(5000)
                    if purged:
                        self.db.log(
                            "INFO",
                            f"Purge automatique : {purged} annonce(s) de plus "
                            f"de {retention} jours supprimée(s).",
                            source="engine",
                        )
            except asyncio.CancelledError:
                raise
            except Exception as exc:  # pragma: no cover
                self.db.log("WARNING", f"Maintenance : {exc}", source="engine")
            await asyncio.sleep(60)

    # ── API dashboard ────────────────────────────────────────────────────
    async def scan_now(self, profile_id: int) -> dict:
        profile = self.db.get_profile(profile_id)
        if not profile:
            return {"ok": False, "error": "Profil introuvable."}
        if profile_id in self._inflight:
            return {"ok": False, "error": "Ce profil est déjà en cours de scan."}
        if not profile.get("url"):
            return {"ok": False, "error": "Renseignez d'abord une URL de recherche."}
        self._launch(profile)
        self.db.log(
            "INFO",
            f"Scan manuel demandé pour « {profile['name']} ».",
            profile_id=profile_id,
        )
        return {"ok": True, "message": "Scan lancé."}

    def status(self) -> dict[str, Any]:
        now = time.time()
        profiles = self.db.list_profiles()
        with_url = len([p for p in profiles if p.get("url")])
        return {
            "running": self._running,
            "paused": self.paused,
            "uptime_seconds": int(now - self.stats.started_at),
            "uptime_human": human_duration(now - self.stats.started_at),
            "transport": self.client.transport,
            "profiles_total": len(profiles),
            "profiles_active": len([p for p in profiles if p.get("active")]),
            "profiles_configured": with_url,
            "inflight": sorted(self._inflight),
            "global_cooldown": max(0, int(self._global_cooldown_until - now)),
            "stats": {
                "scans": self.stats.scans,
                "scans_failed": self.stats.scans_failed,
                "items_seen": self.stats.items_seen,
                "new_items": self.stats.new_items,
                "alerts_sent": self.stats.alerts_sent,
                "alerts_failed": self.stats.alerts_failed,
                "blocked": self.stats.blocked,
                "last_scan_at": self.stats.last_scan_at,
                "last_error": self.stats.last_error,
                "last_block_at": self.stats.last_block_at,
            },
            "next_runs": {
                str(pid): max(0, int(due - now)) for pid, due in self._next_run.items()
            },
            "http": self.client.stats(),
            "notifier": dict(self.notifier.stats),
        }

    def next_run_for(self, profile_id: int) -> str | None:
        due = self._next_run.get(profile_id)
        if not due:
            return None
        from datetime import datetime, timezone

        return datetime.fromtimestamp(due, tz=timezone.utc).isoformat(
            timespec="seconds"
        )
