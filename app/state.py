"""Composition de l'application (config, DB, client, moteur) partagée par l'API."""

from __future__ import annotations

from pathlib import Path

from .config import ConfigStore
from .database import Database
from .demo import DEMO_PROFILES, DemoVintedAPI
from .engine import BotEngine
from .http_client import HttpClient
from .notify import DiscordNotifier
from .vinted_api import VintedAPI


class AppState:
    def __init__(
        self,
        config_path: str | Path = "config.json",
        db_path: str | Path = "data/vinted_sniper.db",
        demo: bool = False,
    ):
        self.demo = bool(demo)
        self.config = ConfigStore(config_path)
        self.db = Database(db_path)
        self.db_path = Path(db_path)
        self.client = HttpClient(self.config, self.db)
        api_cls = DemoVintedAPI if self.demo else VintedAPI
        self.api = api_cls(self.client, self.db, self.config)
        self.notifier = DiscordNotifier(self.config, self.db)
        self.notifier.dry_run = self.demo
        self.engine = BotEngine(
            self.config, self.db, self.client, self.api, self.notifier
        )
        self._started = False

    async def startup(self) -> None:
        if self._started:
            return
        self._started = True
        interrupted = self.db.mark_interrupted_scans()
        if interrupted:
            self.db.log(
                "WARNING",
                f"{interrupted} scan(s) interrompu(s) par un arrêt précédent.",
                source="system",
            )
        if self.demo:
            self.db.log(
                "INFO",
                "MODE DÉMO activé : annonces fictives, aucun envoi réel "
                "vers Vinted ni Discord.",
                source="system",
            )
            if not self.db.list_profiles():
                for payload in DEMO_PROFILES:
                    self.db.create_profile(payload)
                self.db.log(
                    "INFO",
                    "Deux profils d'exemple ont été créés pour la démo.",
                    source="system",
                )
        self.db.log("INFO", f"Interface prête — {self.db_path}", source="system")
        await self.engine.start()

    async def shutdown(self) -> None:
        await self.engine.stop()
        await self.client.close()
        await self.notifier.close()
        self.db.log("INFO", "Application arrêtée.", source="system")
        self.db.close()
        self._started = False

    def db_size(self) -> int:
        try:
            return self.db_path.stat().st_size
        except OSError:
            return 0
