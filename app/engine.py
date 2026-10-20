"""Moteur de veille temps réel : ordonnancement, détection, alertes.

Boucle principale (« scheduler ») :

* chaque profil actif est suivi **en continu** (intervalle adaptatif de 1,5 s à
  10 s) : un autre scan démarre dès que le précédent est terminé ;
* détection incrémentale : tant que la première annonce de la page ne change
  pas, le HTML n'est même pas analysé (une requête + une regex ≈ quelques ms) ;
* alerte **immédiate** : l'annonce est enregistrée et publiée sur le flux du
  dashboard puis envoyée à Discord sans attendre l'enrichissement (description,
  vendeur), qui se poursuit en tâche de fond et met à jour la fiche ;
* concurrence bornée pour ne pas déclencher les protections Vinted ;
* sur 403/429/blocage : rotation proxy + UA, renouvellement de session,
  backoff exponentiel, puis reprise automatique (jamais de crash) ;
* anti-doublon garanti par SQLite + cache mémoire, même après redémarrage ;
* premier scan = « baseline » (les annonces existantes sont enregistrées
  silencieusement, seules les nouvelles déclenchent une alerte).
"""

from __future__ import annotations

import asyncio
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .config import ConfigStore
from .database import Database
from .filters import MatchResult, matches_profile, needs_description
from .http_client import HttpClient
from .notify import DiscordNotifier
from .realtime import HARD_MIN_INTERVAL, LiveSettings, is_live, next_interval
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
    #: Page identique au dernier passage (aucune analyse nécessaire).
    unchanged: bool = False
    #: Délai entre le début du scan et la première nouveauté détectée (ms).
    detection_ms: int | None = None


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
    unchanged: int = 0
    last_scan_at: str | None = None
    last_detection_ms: int | None = None
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
        self._interval: dict[int, float] = {}
        self._failures: dict[int, int] = {}
        self._warm: dict[str, float] = {}
        self._force_renew: set[str] = set()
        self._global_cooldown_until = 0.0
        self._alert_sem = asyncio.Semaphore(3)
        self._sem: asyncio.Semaphore | None = None

        # ── Temps réel ───────────────────────────────────────────────────
        self._settings = LiveSettings.from_config(config)
        self._head: dict[int, str] = {}
        #: Profils dont le prochain passage doit analyser toute la page (rafale).
        self._deep_next: set[int] = set()
        self._last_found: dict[int, float] = {}
        self._quiet: dict[int, int] = {}
        #: Multiplicateur d'intervalle après blocages répétés (anti-ban adaptatif).
        self._throttle: dict[int, float] = {}
        self._seen_cache: dict[int, set[str]] = {}
        self._ignored_cache: dict[int, set[str]] = {}
        self._listeners: set[asyncio.Queue] = set()
        self._enrich_sem = asyncio.Semaphore(2)
        self._bg: set[asyncio.Task] = set()

    # ── Cycle de vie ─────────────────────────────────────────────────────
    async def start(self) -> None:
        if self._running:
            return
        self._running = True
        self._settings = LiveSettings.from_config(self.config)
        self._sem = asyncio.Semaphore(
            max(1, int(self.config.get("engine.max_concurrent_profiles", 2)))
        )
        live = bool(self.config.get("engine.live_mode", True))
        self.db.log(
            "INFO",
            f"Moteur démarré (transport {self.client.transport}, "
            + (
                f"temps réel {self._settings.describe()})"
                if live
                else f"intervalle par défaut "
                f"{self.config.get('engine.default_interval_seconds')}s)"
            ),
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
        pending = [*self._tasks, *list(self._inflight.values()), *list(self._bg)]
        for task in pending:
            task.cancel()
        await asyncio.gather(*pending, return_exceptions=True)
        self._tasks.clear()
        self._inflight.clear()
        self._bg.clear()
        self._listeners.clear()
        self.db.log("INFO", "Moteur arrêté proprement.", source="engine")

    def set_paused(self, paused: bool) -> None:
        self.paused = bool(paused)
        self.db.log(
            "INFO", "Moteur en pause." if paused else "Moteur relancé.", source="engine"
        )

    async def apply_config(self) -> None:
        """Répercute les réglages (concurrence, intervalles) sans redémarrer."""
        concurrency = max(1, int(self.config.get("engine.max_concurrent_profiles", 2)))
        self._sem = asyncio.Semaphore(concurrency)
        self._settings = LiveSettings.from_config(self.config)

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

    # ── Bus temps réel (Server-Sent Events) ──────────────────────────────
    def subscribe(self) -> asyncio.Queue:
        """Abonne le dashboard : chaque nouveauté arrive sans attendre le poll."""
        queue: asyncio.Queue = asyncio.Queue(maxsize=200)
        self._listeners.add(queue)
        return queue

    def unsubscribe(self, queue: asyncio.Queue) -> None:
        self._listeners.discard(queue)

    def publish(self, event: dict[str, Any]) -> None:
        for queue in list(self._listeners):
            try:
                queue.put_nowait(event)
            except asyncio.QueueFull:  # pragma: no cover - client trop lent
                pass

    # ── Caches mémoire (anti-doublon instantané) ─────────────────────────
    def invalidate_profile(self, profile_id: int) -> None:
        """Oublie les caches d'un profil (après « oublier les annonces vues »)."""
        self._seen_cache.pop(profile_id, None)
        self._ignored_cache.pop(profile_id, None)
        self._head.pop(profile_id, None)
        self._interval.pop(profile_id, None)
        self._last_found.pop(profile_id, None)
        self._throttle.pop(profile_id, None)
        self._deep_next.discard(profile_id)

    def challenge_info(self) -> dict[str, Any]:
        """Ce qui est disponible pour débloquer une vérification (gratuit)."""
        from .browser_session import find_browser

        explicit = str(self.config.get("challenge.browser_path", "") or "")
        browser = find_browser(explicit)
        return {
            "browser": Path(browser).name if browser else "",
            "browser_path": browser or "",
            "solver": bool(str(self.config.get("challenge.solver_url", "") or "").strip()),
            "headless": bool(self.config.get("challenge.headless", False)),
            "available": bool(browser) or bool(
                str(self.config.get("challenge.solver_url", "") or "").strip()
            ),
        }

    def resume_after_unblock(self) -> int:
        """Reprend les scans tout de suite après une session débloquée.

        Sans cela, le profil restait en pause 5 min (backoff de vérification)
        alors que la nouvelle session était déjà valable : l'utilisateur
        venait de débloquer, et il attendait encore.
        """
        resumed = 0
        now = time.time()
        for profile in self.db.list_profiles():
            if not profile.get("active"):
                continue
            profile_id = int(profile["id"])
            self._failures.pop(profile_id, None)
            self._throttle.pop(profile_id, None)
            self._next_run[profile_id] = now
            resumed += 1
        self._global_cooldown_until = 0.0
        self.stats.last_error = None
        if resumed:
            self.db.log(
                "INFO",
                f"Session navigateur importée : {resumed} profil(s) relancé(s) immédiatement.",
            )
        return resumed

    def _seen(self, profile_id: int) -> set[str]:
        cache = self._seen_cache.get(profile_id)
        if cache is None:
            cache = self.db.seen_ids(profile_id)
            self._seen_cache[profile_id] = cache
        return cache

    def _ignored(self, profile_id: int) -> set[str]:
        cache = self._ignored_cache.get(profile_id)
        if cache is None:
            cache = self.db.ignored_ids(profile_id)
            self._ignored_cache[profile_id] = cache
        return cache

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
        await asyncio.sleep(0.2)  # laisse le dashboard démarrer
        while self._running:
            try:
                await self._schedule_tick()
            except asyncio.CancelledError:
                raise
            except Exception as exc:  # pragma: no cover
                self.db.log("ERROR", f"Ordonnanceur : {exc}", source="engine")
            # Tick court : indispensable pour tenir un intervalle de 1,5 s.
            await asyncio.sleep(0.25)

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
                self.invalidate_profile(profile_id)

        now = time.time()
        for profile in profiles:
            profile_id = profile["id"]
            if profile_id in self._inflight:
                continue
            if not profile.get("url"):
                continue  # rien à surveiller : on ne consomme pas de requête
            due = self._next_run.get(profile_id)
            if due is None:
                # Démarrage immédiat (léger décalage pour lisser les profils).
                self._next_run[profile_id] = now + 0.2 + (profile_id % 5) * 0.25
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
        self._next_run[profile_id] = time.time() + self._current_interval(profile)

        def _cleanup(_task: asyncio.Task, pid: int = profile_id) -> None:
            if self._inflight.get(pid) is _task:
                self._inflight.pop(pid, None)

        task.add_done_callback(_cleanup)

    def _current_interval(self, profile: dict) -> float:
        """Intervalle courant d'un profil (avant même son premier scan)."""
        if is_live(profile, self.config):
            return self._interval.get(profile["id"], self._settings.min_interval)
        try:
            return max(
                HARD_MIN_INTERVAL,
                float(
                    profile.get("interval_seconds")
                    or self.config.get("engine.default_interval_seconds", 60)
                ),
            )
        except (TypeError, ValueError):
            return 60.0

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
            interval = self._after_scan(profile, outcome)
            self._next_run[profile_id] = time.time() + interval

    def _after_scan(self, profile: dict, outcome: ScanOutcome) -> float:
        """Calcule le prochain passage et applique le self-healing."""
        profile_id = int(profile["id"])
        live = is_live(profile, self.config)
        if outcome.status == "blocked":
            self._record_failure(profile, outcome.error or "blocage")
            domain = domain_of(profile.get("url") or "", "www.vinted.fr")
            failures = self._failures.get(profile_id, 1)
            error = str(outcome.error or "")
            hard = bool(re.search(r"HTTP (401|403|407|429|451|503)", error))
            # « challenge-platform », « captcha-delivery »… : Vinted exige une
            # vérification navigateur. Réessayer toutes les 20 s ne fait que
            # prolonger le blocage : on laisse respirer l'IP.
            interactive = bool(
                re.search(r"challenge-platform|captcha-delivery|cf-chl|just a moment", error, re.I)
            )
            # Défi Datadome (HTTP 200) : renouveler la session à chaque passage
            # jetait le cookie posé par la page de vérification — donc nouveau
            # défi au scan suivant, indéfiniment. On garde la session et on
            # laisse simplement retomber la pression.
            self._slow_down(profile, cap=8.0 if hard else 3.0)
            if interactive and not hard:
                delay = self._challenge_backoff(profile_id)
                self.db.log(
                    "WARNING",
                    f"Vérification navigateur exigée par Vinted ({error}). "
                    f"Pause de {human_duration(delay)} : insister prolongerait "
                    f"le blocage. Changez d'IP (partage de connexion, proxy) "
                    f"si cela dure.",
                    profile_id=profile_id,
                )
            elif hard or failures >= 3:
                self._force_renew.add(domain)
                delay = self._backoff(profile_id)
                self.db.log(
                    "WARNING",
                    f"Self-healing : renouvellement de session {domain} programmé "
                    f"(blocage #{failures}), reprise dans {human_duration(delay)}.",
                    profile_id=profile_id,
                )
            else:
                delay = self._soft_backoff(profile_id)
                self.db.log(
                    "WARNING",
                    f"Blocage Vinted ({error or 'anti-bot'}) : cookies conservés, "
                    f"nouvelle tentative dans {human_duration(delay)}.",
                    profile_id=profile_id,
                )
            self._global_cooldown_until = max(
                self._global_cooldown_until, time.time() + min(8, delay / 4)
            )
            self._interval[profile_id] = self._settings.min_interval
            return delay
        if outcome.status == "error":
            self._record_failure(profile, outcome.error or "erreur")
            delay = self._backoff(profile_id)
            self._interval[profile_id] = self._settings.min_interval
            return delay

        self._failures[profile_id] = 0
        self._speed_up(profile)
        if not live:
            try:
                return max(
                    HARD_MIN_INTERVAL,
                    float(
                        profile.get("interval_seconds")
                        or self.config.get("engine.default_interval_seconds", 60)
                    ),
                )
            except (TypeError, ValueError):
                return 60.0

        since_found: float | None = None
        last = self._last_found.get(profile_id)
        if last:
            since_found = time.time() - last
        interval = next_interval(
            self._interval.get(profile_id),
            new_items=outcome.new_items,
            since_last_found=since_found,
            settings=self._settings,
        )
        # Après un blocage, on sonde volontairement moins vite pendant un moment.
        throttle = self._throttle.get(profile_id, 1.0)
        if throttle > 1.0:
            interval = min(60.0, interval * throttle)
        self._interval[profile_id] = interval
        return interval

    def throttle_for(self, profile_id: int) -> float:
        return round(self._throttle.get(profile_id, 1.0), 2)

    def _slow_down(self, profile: dict, cap: float = 8.0) -> None:
        """Blocage détecté : on espace les passages (jusqu'à ``cap`` ×)."""
        profile_id = int(profile["id"])
        previous = self._throttle.get(profile_id, 1.0)
        value = min(float(cap), previous * 1.6)
        if value - previous < 0.05:
            return
        self._throttle[profile_id] = value
        self.db.log(
            "WARNING",
            f"Anti-blocage : « {profile['name']} » ralenti ×{value:.1f} "
            f"(intervalle ≈ {self._settings.min_interval * value:.1f} s) "
            f"le temps que Vinted se calme.",
            profile_id=profile_id,
        )

    def _speed_up(self, profile: dict) -> None:
        """Retour progressif à la vitesse normale après des passages réussis."""
        profile_id = int(profile["id"])
        value = self._throttle.get(profile_id)
        if not value or value <= 1.0:
            return
        value = max(1.0, value * 0.9)
        if value <= 1.05:
            self._throttle.pop(profile_id, None)
            self.db.log(
                "INFO",
                f"« {profile['name']} » : vitesse de détection revenue à la normale.",
                profile_id=profile_id,
            )
        else:
            self._throttle[profile_id] = value

    def _backoff(self, profile_id: int) -> float:
        failures = self._failures.get(profile_id, 1)
        base = max(15, int(self._settings.max_interval or 15))
        delay = min(base * (2 ** min(failures, 4)), 900)
        return max(10.0, float(delay))

    def _challenge_backoff(self, profile_id: int) -> float:
        """Pause après une vérification navigateur : 60 s, 2 min, 5 min.

        Contrairement à un simple ralentissement, insister ici **aggrave** le
        blocage (Cloudflare/Datadome comptent les tentatives). Mieux vaut
        laisser l'IP respirer que brûler le quota pour rien.
        """
        failures = max(1, self._failures.get(profile_id, 1))
        return float(min(60 * (2 ** min(failures - 1, 3)), 300))

    def _soft_backoff(self, profile_id: int) -> float:
        """Reprise après un défi anti-bot : courte, pour ne rien manquer.

        Un défi Datadome rendu en HTTP 200 n'est pas une sanction durable :
        attendre quatre minutes (ancien comportement) revenait à perdre toutes
        les annonces publiées entre-temps. On plafonne à 90 s.
        """
        failures = max(1, self._failures.get(profile_id, 1))
        delay = min(20.0 * (2 ** min(failures - 1, 3)), 90.0)
        return max(15.0, delay)

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
    def _block_age(self, now: float) -> float | None:
        """Secondes écoulées depuis le dernier blocage (calculé côté serveur).

        Le dashboard lisait ``last_block_at`` (UTC sans fuseau) avec
        ``Date.parse`` : décalage d'une à deux heures selon le fuseau du
        navigateur. On expose donc l'âge en secondes, sans ambiguïté.
        """
        stamp = self.stats.last_block_at
        if not stamp:
            return None
        try:
            from datetime import datetime, timezone

            moment = datetime.fromisoformat(stamp)
        except ValueError:  # pragma: no cover - horodatage inattendu
            return None
        if moment.tzinfo is None:
            moment = moment.replace(tzinfo=timezone.utc)
        return max(0.0, now - moment.timestamp())

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
        live = is_live(profile, self.config)

        detail_budget = max(
            0, int(self.config.get("engine.detail_budget_per_scan", 15))
        )
        head_limit = (
            max(1, int(self.config.get("engine.realtime_head_items", 24)))
            if live
            else None
        )
        delay = float(self.config.get("engine.min_request_delay", 2.0))
        pages = max(1, min(int(profile.get("pages") or 1), 5))
        per_page = int(self.config.get("engine.max_items_per_page", 96))
        candidates: list[dict] = []

        try:
            await self._ensure_session(domain, profile_id, live)
            for page in range(1, pages + 1):
                # Page 1 en mode incrémental : on ne demande le HTML complet que
                # si la tête de liste a bougé depuis le dernier passage.
                # Après une rafale (nouvelles annonces), on analyse une fois
                # toute la page : les annonces au-delà des 24 premières cartes
                # ne doivent jamais être perdues.
                deep = page == 1 and profile_id in self._deep_next
                known = (
                    None
                    if deep
                    else (self._head.get(profile_id) if page == 1 else None)
                )
                # Temps réel : on ne s'endort pas 30-60 s dans les tentatives.
                # Un blocage échoue vite (8 s), la boucle repart avec une autre
                # identité : c'est elle qui dosait déjà le rythme.
                result = await self.api.search(
                    profile,
                    page=page,
                    domain=domain,
                    known_head=known,
                    head_limit=None if deep else head_limit,
                    attempts=1 if live else None,
                    timeout=10 if live else None,
                )
                if deep:
                    self._deep_next.discard(profile_id)
                if result.blocked:
                    outcome.status = "blocked"
                    outcome.error = result.error or "blocage anti-bot"
                    self.stats.blocked += 1
                    self.stats.last_block_at = utcnow_iso()
                    self.publish(
                        {
                            "type": "blocked",
                            "profile_id": profile_id,
                            "error": outcome.error,
                        }
                    )
                    break
                if result.error:
                    outcome.status = "error"
                    outcome.error = result.error
                    break

                if page == 1:
                    if result.unchanged:
                        outcome.unchanged = True
                        self.stats.unchanged += 1
                        break
                    if result.head_key:
                        self._head[profile_id] = result.head_key

                outcome.pages += 1
                outcome.items_seen += len(result.items)
                if result.empty:
                    self.db.log(
                        "DEBUG",
                        f"« {profile['name']} » : la recherche ne renvoie "
                        f"aucune annonce (page vide, filtres trop stricts ?).",
                        profile_id=profile_id,
                    )
                seen = self._seen(profile_id)
                ignored = self._ignored(profile_id)
                for item in result.items:
                    if not item.get("id"):
                        continue
                    if str(item["id"]) in seen or str(item["id"]) in ignored:
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
                expected = head_limit or per_page
                if len(result.items) < expected:
                    break
                if page < pages and not live:
                    await asyncio.sleep(delay * (1 + page * 0.2))

            # ── Vérification fine : description (si nécessaire) + vendeur ──
            base_profile = {
                **profile,
                "min_seller_rating": None,
                "min_seller_feedback": None,
            }
            needs_seller = (
                profile.get("min_seller_rating") is not None
                or profile.get("min_seller_feedback") is not None
            )

            # Les requêtes « fiche article / vendeur » partent en parallèle : la
            # première annonce n'attend jamais les autres (latence minimale).
            if candidates and (needs_description(profile) or needs_seller):
                if live:
                    await self._enrich_candidates(
                        profile, candidates, domain, detail_budget, needs_seller
                    )
                else:
                    await self._enrich_candidates_serial(
                        profile, candidates, domain, detail_budget, needs_seller, delay
                    )

            matches: list[dict] = []
            seen_rows: list[dict] = []
            for item in candidates:
                if str(item["id"]) in self._ignored(profile_id):
                    continue

                # 1) Filtres prix / blacklist / whitelist (vendeur inconnu toléré)
                verdict: MatchResult = matches_profile(base_profile, item)
                if not verdict.matched:
                    self._reject(profile_id, item, verdict.reason)
                    continue

                # 2) Réputation vendeur (déjà récupérée si un seuil est défini)
                verdict = matches_profile(profile, item)
                if not verdict.matched:
                    if verdict.reason.startswith("nombre d'avis"):
                        self.db.log(
                            "DEBUG",
                            f"Vendeur non vérifié ({verdict.reason}) : "
                            f"« {item.get('title', '')[:60]} »",
                            profile_id=profile_id,
                        )
                    else:
                        self._reject(profile_id, item, verdict.reason)
                    continue

                if not self.db.add_seen(profile_id, item, raw=None):
                    continue  # doublon détecté entre-temps
                self._seen(profile_id).add(str(item["id"]))
                self._last_found[profile_id] = time.time()
                outcome.new_items += 1
                self.stats.new_items += 1
                if outcome.detection_ms is None:
                    outcome.detection_ms = max(
                        1, int((time.perf_counter() - started) * 1000)
                    )
                    self.stats.last_detection_ms = outcome.detection_ms
                row = self.db.get_item(profile_id, item["id"]) or item
                seen_rows.append({**row, "profile_name": profile["name"]})
                matches.append(item)

            # ── Publication immédiate sur le flux + Discord ────────────────
            for row in seen_rows:
                self.publish(
                    {
                        "type": "item",
                        "profile_id": profile_id,
                        "detection_ms": outcome.detection_ms,
                        "baseline": baseline,
                        "item": row,
                    }
                )

            if baseline:
                for item in matches:
                    self.db.mark_notified(profile_id, item["id"], skipped=True)
            elif matches:
                results = await asyncio.gather(
                    *(self._notify(profile, item) for item in matches)
                )
                for item, (ok, error) in zip(matches, results):
                    if ok:
                        outcome.alerts += 1
                        self.stats.alerts_sent += 1
                    else:
                        self.stats.alerts_failed += 1
                    self.db.mark_notified(profile_id, item["id"], None if ok else error)

            if outcome.new_items:
                # Le prochain passage relira toute la page (voir « deep »).
                self._deep_next.add(profile_id)

            # ── Enrichissement en tâche de fond (ne retarde jamais l'alerte) ─
            if not baseline:
                for item in matches:
                    self._schedule_enrichment(profile, item, domain)

            if outcome.unchanged:
                outcome.status = "ok"  # page identique : rien à signaler
            elif outcome.status == "ok" and outcome.items_seen == 0:
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
                detection_ms=outcome.detection_ms,
            )
            self.db.record_scan(
                profile_id,
                status=status,
                last_error=outcome.error,
                new_items=outcome.new_items,
                found=outcome.new_items > 0,
            )
            if status == "ok" and (outcome.items_seen > 0 or outcome.pages > 0):
                # La baseline est consommée dès qu'une page a réellement été lue :
                # une recherche momentanément vide ne doit pas retarder les alertes
                # des annonces publiées ensuite. Un blocage, lui, ne la consomme pas.
                self.db.mark_baseline_done(profile_id)
            self._log_scan(profile, outcome, live)
            self.publish(
                {
                    "type": "scan",
                    "profile_id": profile_id,
                    "status": status,
                    "new_items": outcome.new_items,
                    "duration_ms": duration,
                    "detection_ms": outcome.detection_ms,
                    "unchanged": outcome.unchanged,
                }
            )
        return outcome

    def _log_scan(self, profile: dict, outcome: ScanOutcome, live: bool) -> None:
        """Journalise sans noyer les logs quand on sonde toutes les secondes."""
        profile_id = int(profile["id"])
        quiet_count = self._quiet.get(profile_id, 0) + 1
        self._quiet[profile_id] = quiet_count
        if outcome.baseline:
            self.db.log(
                "INFO",
                f"Scan initial (baseline) « {profile['name']} » : "
                f"{outcome.new_items} annonce(s) enregistrée(s) sans "
                f"notification.",
                profile_id=profile_id,
            )
            return
        if outcome.new_items:
            self._quiet[profile_id] = 0
            self.db.log(
                "INFO",
                f"⚡ {outcome.new_items} nouvelle(s) annonce(s) « "
                f"{profile['name']} » en {outcome.detection_ms or 0} ms "
                f"({outcome.alerts} alerte(s) Discord).",
                profile_id=profile_id,
            )
            return
        if outcome.status == "empty" and not outcome.error:
            if live and quiet_count % 60 != 0:
                return
            self.db.log(
                "WARNING",
                f"Scan « {profile['name']} » : aucune annonce reçue. "
                f"Vérifiez l'URL de recherche, les filtres de prix, ou "
                f"relancez plus tard (Vinted a peut-être modifié sa structure).",
                profile_id=profile_id,
            )
            return
        if outcome.status in {"error", "blocked"}:
            self.db.log(
                "WARNING",
                f"Scan « {profile['name']} » interrompu "
                f"({outcome.status}) : {outcome.error}",
                profile_id=profile_id,
            )
            return
        if live and not (quiet_count % 60 == 0 and outcome.items_seen):
            return  # silence en temps réel : un point de statut par minute max
        self.db.log(
            "INFO",
            f"Scan « {profile['name']} » : {outcome.items_seen} annonce(s) "
            f"analysée(s), 0 nouvelle, {outcome.duration_ms} ms.",
            profile_id=profile_id,
        )

    def _reject(self, profile_id: int, item: dict, reason: str) -> None:
        self.db.add_ignored(profile_id, item["id"], reason)
        self._ignored(profile_id).add(str(item["id"]))
        self.db.log(
            "DEBUG",
            f"Écarté ({reason}) : « {item.get('title', '')[:60]} »",
            profile_id=profile_id,
        )

    # ── Enrichissement avant décision ────────────────────────────────────
    async def _enrich_candidates(
        self,
        profile: dict,
        candidates: list[dict],
        domain: str,
        budget: int,
        needs_seller: bool,
    ) -> None:
        """Complète les fiches en parallèle (mode temps réel).

        Le résultat est réinjecté **dans les dictionnaires d'origine** : la
        suite du scan reste séquentielle, donc déterministe côté SQLite.

        Deux garde-fous de latence, tous deux indispensables au « seconde par
        seconde » : une seule tentative réseau par fiche (``fast``) et un
        budget global (``engine.realtime_enrich_budget``, 3,5 s par défaut).
        Si une fiche traîne, on continue avec les données déjà lues : l'alerte
        part sans attendre, quitte à afficher un vendeur inconnu.
        """
        profile_id = int(profile["id"])
        wanted = candidates[:budget] if budget else []
        if not wanted:
            return
        semaphore = asyncio.Semaphore(4)
        done = 0

        async def complete(item: dict) -> None:
            nonlocal done
            async with semaphore:
                try:
                    if needs_description(profile):
                        item.update(
                            await self.api.enrich_item(
                                item, domain, profile_id, fast=True
                            )
                            or {}
                        )
                    if needs_seller:
                        item.update(
                            await self.api.fetch_seller(
                                item, domain, profile_id, fast=True
                            )
                            or {}
                        )
                except asyncio.CancelledError:
                    raise
                except Exception:  # pragma: no cover - best effort
                    pass
                finally:
                    done += 1

        seconds = float(self.config.get("engine.realtime_enrich_budget", 3.5))
        tasks = [asyncio.ensure_future(complete(item)) for item in wanted]
        try:
            await asyncio.wait_for(
                asyncio.gather(*tasks, return_exceptions=True), timeout=max(0.5, seconds)
            )
        except asyncio.TimeoutError:
            for task in tasks:
                task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            self.db.log(
                "DEBUG",
                f"Fiches non complétées en {seconds:g}s "
                f"({done}/{len(wanted)}) : le scan continue, l'alerte n'attend pas.",
                profile_id=profile_id,
            )

    async def _enrich_candidates_serial(
        self,
        profile: dict,
        candidates: list[dict],
        domain: str,
        budget: int,
        needs_seller: bool,
        delay: float,
    ) -> None:
        """Version douce (mode intervalle) : une requête à la fois, avec pause."""
        profile_id = int(profile["id"])
        used = 0
        for item in candidates:
            if used >= budget:
                break
            used += 1
            try:
                if needs_description(profile):
                    item.update(
                        await self.api.enrich_item(item, domain, profile_id) or {}
                    )
                    await asyncio.sleep(min(delay * 0.5, 1.0))
                if needs_seller:
                    item.update(
                        await self.api.fetch_seller(item, domain, profile_id) or {}
                    )
                    await asyncio.sleep(min(delay * 0.3, 1.0))
            except asyncio.CancelledError:
                raise
            except Exception:  # pragma: no cover - best effort
                pass

    # ── Enrichissement différé ───────────────────────────────────────────
    def _schedule_enrichment(self, profile: dict, item: dict, domain: str) -> None:
        if not (
            self.config.get("engine.detail_fetch", True)
            or self.config.get("engine.enrich_sellers", True)
        ):
            return
        # Vague de blocages en cours : la fiche article et le profil vendeur
        # seraient des requêtes perdues, et de nouveaux signaux pour Datadome.
        if getattr(self.client, "recently_blocked", None) and self.client.recently_blocked(120):
            self._enrich_deferred = getattr(self, "_enrich_deferred", 0) + 1
            return
        task = asyncio.create_task(
            self._enrich_later(profile, item, domain),
            name=f"enrich-{profile['id']}-{item['id']}",
        )
        self._bg.add(task)
        task.add_done_callback(self._bg.discard)

    async def _enrich_later(self, profile: dict, item: dict, domain: str) -> None:
        """Description + vendeur + photo HD, puis mise à jour de la fiche."""
        async with self._enrich_sem:
            profile_id = int(profile["id"])
            current = dict(item)
            try:
                if self.config.get("engine.detail_fetch", True):
                    current = await asyncio.wait_for(
                        self.api.enrich_item(current, domain, profile_id), timeout=20
                    )
                if self.config.get("engine.enrich_sellers", True):
                    current = await asyncio.wait_for(
                        self.api.fetch_seller(current, domain, profile_id), timeout=20
                    )
            except asyncio.CancelledError:
                raise
            except Exception as exc:  # pragma: no cover - best effort
                self.db.log(
                    "DEBUG",
                    f"Enrichissement différé incomplet ({type(exc).__name__}).",
                    profile_id=profile_id,
                )
                return
            fields = {
                key: current.get(key)
                for key in (
                    "title",
                    "description",
                    "price",
                    "total_price",
                    "currency",
                    "brand",
                    "size",
                    "condition",
                    "image_url",
                    "seller_id",
                    "seller_name",
                    "seller_rating",
                    "seller_feedback",
                    "seller_url",
                    "favourites",
                )
                if current.get(key) not in (None, "")
            }
            if not fields:
                return
            # On ne réécrit (ni ne publie) que si quelque chose a réellement changé.
            before = self.db.get_item(profile_id, item["id"]) or {}
            changed = {
                key: value
                for key, value in fields.items()
                if str(before.get(key, "")) != str(value)
            }
            if not changed:
                return
            if self.db.update_item(profile_id, item["id"], changed):
                row = self.db.get_item(profile_id, item["id"])
                if row:
                    self.publish(
                        {
                            "type": "item_update",
                            "profile_id": profile_id,
                            "item": {**row, "profile_name": profile["name"]},
                        }
                    )

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

    async def _ensure_session(
        self, domain: str, profile_id: int, live: bool = False
    ) -> None:
        refresh = int(self.config.get("http.cookie_refresh_minutes", 25)) * 60
        last = self._warm.get(domain, 0)
        force = domain in self._force_renew or bool(
            last and time.time() - last > refresh
        )
        if force:
            self._force_renew.discard(domain)
        await self.api.ensure_session(
            f"https://{domain}/",
            profile_id=profile_id,
            force=force,
            attempts=1 if live else 2,
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
                    self.db.prune_scans(keep_per_profile=600)
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
        # Vinted vient de renvoyer une page de vérification : relancer un scan
        # immédiatement ne peut pas réussir et prolonge le blocage. On refuse
        # en expliquant le délai restant, plutôt que d'insister en silence.
        cooldown = getattr(self.client, "block_cooldown_left", None)
        wait = float(cooldown(25)) if callable(cooldown) else 0.0
        if wait > 0:
            return {
                "ok": False,
                "blocked": True,
                "error": (
                    f"Vinted exige une vérification navigateur. "
                    f"Réessayez dans {int(wait)} s (insister prolonge le blocage). "
                    "Si cela dure : partage de connexion du téléphone ou proxy."
                ),
            }
        self._launch(profile)  # fonctionne aussi quand le moteur est en pause
        self.db.log(
            "INFO",
            f"Scan manuel demandé pour « {profile['name']} ».",
            profile_id=profile_id,
        )
        return {"ok": True, "message": "Scan lancé."}

    def seconds_to_next(self, profile_id: int) -> float | None:
        due = self._next_run.get(profile_id)
        if due is None:
            return None
        return max(0.0, round(due - time.time(), 1))

    def status(self) -> dict[str, Any]:
        now = time.time()
        profiles = self.db.list_profiles()
        with_url = len([p for p in profiles if p.get("url")])
        live_profiles = [
            p["id"] for p in profiles if p.get("active") and is_live(p, self.config)
        ]
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
            "realtime": {
                "enabled": bool(self.config.get("engine.live_mode", True)),
                "live_profiles": live_profiles,
                "min_interval": self._settings.min_interval,
                "max_interval": self._settings.max_interval,
                "turbo": self._settings.turbo,
            },
            "stats": {
                "scans": self.stats.scans,
                "scans_failed": self.stats.scans_failed,
                "items_seen": self.stats.items_seen,
                "new_items": self.stats.new_items,
                "alerts_sent": self.stats.alerts_sent,
                "alerts_failed": self.stats.alerts_failed,
                "blocked": self.stats.blocked,
                "unchanged": self.stats.unchanged,
                "last_scan_at": self.stats.last_scan_at,
                "last_detection_ms": self.stats.last_detection_ms,
                "last_error": self.stats.last_error,
                "last_block_at": self.stats.last_block_at,
                "block_age_seconds": self._block_age(now),
            },
            "next_runs": {
                str(pid): max(0, int(due - now)) for pid, due in self._next_run.items()
            },
            "intervals": {str(pid): value for pid, value in self._interval.items()},
            "throttle": {str(pid): value for pid, value in self._throttle.items()},
            "challenge": self.challenge_info(),
            "http": self.client.stats(),
            "notifier": dict(self.notifier.stats),
            #: Sans webhook, une annonce est détectée… puis perdue : le
            #: dashboard doit le dire clairement plutôt que de laisser croire
            #: que tout fonctionne.
            "webhook_configured": bool(
                str(self.config.get("discord.default_webhook", "") or "").strip()
                or any(str(p.get("webhook") or "").strip() for p in profiles)
            ),
        }

    def next_run_for(self, profile_id: int) -> str | None:
        due = self._next_run.get(profile_id)
        if not due:
            return None
        from datetime import datetime, timezone

        return datetime.fromtimestamp(due, tz=timezone.utc).isoformat(
            timespec="seconds"
        )
