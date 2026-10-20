"""Chargement / validation / sauvegarde de ``config.json``.

Le fichier est fusionné avec les valeurs par défaut : un ``config.json`` ancien
ou partiel reste utilisable après une mise à jour du projet.
"""

from __future__ import annotations

import copy
import json
import os
import re
import tempfile
import threading
from pathlib import Path
from typing import Any

from .utils import mask_webhook

DEFAULTS: dict[str, Any] = {
    "app": {"host": "127.0.0.1", "port": 8000, "open_browser": True, "password": ""},
    "engine": {
        # ── Temps réel ────────────────────────────────────────────────────
        "live_mode": True,
        "realtime_min_interval": 1.5,
        "realtime_max_interval": 10.0,
        "realtime_growth": 1.6,
        "realtime_burst_seconds": 90,
        "realtime_jitter": 0.15,
        "realtime_turbo": False,
        "realtime_head_items": 24,
        "default_interval_seconds": 60,
        "min_request_delay": 2.0,
        "max_concurrent_profiles": 2,
        "max_items_per_page": 96,
        "enrich_sellers": True,
        "detail_fetch": True,
        "seller_cache_ttl_hours": 24,
        "retention_days": 30,
        "baseline_first_scan": True,
        "detail_budget_per_scan": 15,
        "start_paused": False,
    },
    "http": {
        "impersonate": "chrome124",
        "timeout_seconds": 25,
        "max_retries": 3,
        "cookie_refresh_minutes": 25,
        "use_json_api": False,
        "block_backoff_seconds": [30, 60, 120, 300, 600, 900],
        "user_agents": [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:130.0) Gecko/20100101 Firefox/130.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
            "(KHTML, like Gecko) Version/17.6 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        ],
    },
    "proxies": {
        "enabled": False,
        "prefer_proxies": False,
        "auto_discover": True,
        "list": [],
        "sources": [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http"
            "&timeout=10000&country=all&ssl=all&anonymity=all",
        ],
        "max_pool_size": 40,
        "cooldown_seconds": 300,
        "ban_after_failures": 3,
        "discover_interval_seconds": 600,
    },
    # ── Déblocage d'une vérification navigateur (gratuit) ────────────────
    "challenge": {
        #: Endpoint FlareSolverr / Byparr (Docker, gratuit). Vide = désactivé.
        "solver_url": "",
        #: Chemin explicite du navigateur (vide = détection automatique).
        "browser_path": "",
        #: Fenêtre invisible : plus rapide, mais une vérification interactive
        #: ne peut pas être validée à la main.
        "headless": False,
        "timeout_seconds": 60,
    },
    "discord": {
        "default_webhook": "",
        "username": "Vinted Sniper",
        "avatar_url": "",
        "mention": "",
    },
    "notifications": {"enabled": True, "max_per_minute": 20, "max_attempts": 5},
    "dashboard": {"feed_size": 60, "logs_size": 300},
}


class ConfigError(ValueError):
    """Valeur de configuration refusée."""


#: Chemins modifiables depuis le dashboard → (type, min, max).
EDITABLE: dict[str, tuple] = {
    "engine.live_mode": ("bool",),
    "engine.realtime_min_interval": ("float", 0.5, 60.0),
    "engine.realtime_max_interval": ("float", 2.0, 600.0),
    "engine.realtime_growth": ("float", 1.0, 4.0),
    "engine.realtime_burst_seconds": ("int", 0, 3600),
    "engine.realtime_jitter": ("float", 0.0, 0.6),
    "engine.realtime_turbo": ("bool",),
    "engine.realtime_head_items": ("int", 4, 96),
    "engine.default_interval_seconds": ("int", 1, 3600),
    "engine.min_request_delay": ("float", 0.5, 30.0),
    "engine.max_concurrent_profiles": ("int", 1, 5),
    "engine.max_items_per_page": ("int", 24, 96),
    "engine.pages_per_scan": ("int", 1, 5),
    "engine.enrich_sellers": ("bool",),
    "engine.detail_fetch": ("bool",),
    "engine.seller_cache_ttl_hours": ("int", 1, 720),
    "engine.retention_days": ("int", 1, 365),
    "engine.baseline_first_scan": ("bool",),
    "engine.detail_budget_per_scan": ("int", 0, 40),
    "http.max_retries": ("int", 0, 6),
    "http.timeout_seconds": ("int", 5, 90),
    "http.cookie_refresh_minutes": ("int", 5, 240),
    "http.use_json_api": ("bool",),
    "proxies.enabled": ("bool",),
    "proxies.prefer_proxies": ("bool",),
    "proxies.auto_discover": ("bool",),
    "proxies.list": ("strlist", 200),
    "proxies.max_pool_size": ("int", 1, 500),
    "proxies.cooldown_seconds": ("int", 30, 7200),
    "proxies.ban_after_failures": ("int", 1, 20),
    "challenge.solver_url": ("url", 400),
    "challenge.browser_path": ("str", 400),
    "challenge.headless": ("bool",),
    "challenge.timeout_seconds": ("int", 10, 180),
    "discord.default_webhook": ("webhook",),
    "discord.username": ("str", 80),
    "discord.avatar_url": ("url", 400),
    "discord.mention": ("str", 100),
    "notifications.enabled": ("bool",),
    "notifications.max_per_minute": ("int", 1, 60),
    "dashboard.feed_size": ("int", 12, 200),
    "app.password": ("str", 100),
}


def _deep_merge(base: dict, override: dict) -> dict:
    result = copy.deepcopy(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def _flatten(patch: dict, prefix: str = "") -> list[tuple[str, Any]]:
    flat: list[tuple[str, Any]] = []
    for key, value in (patch or {}).items():
        path = f"{prefix}.{key}" if prefix else key
        if (
            isinstance(value, dict)
            and path not in EDITABLE
            and any(editable.startswith(path + ".") for editable in EDITABLE)
        ):
            flat.extend(_flatten(value, path))
        else:
            flat.append((path, value))
    return flat


class ConfigStore:
    """Accès thread-safe (lecture/écriture) à la configuration."""

    def __init__(self, path: str | Path = "config.json"):
        self.path = Path(path)
        self._lock = threading.RLock()
        self._data: dict[str, Any] = {}
        self.load()

    # ── I/O ──────────────────────────────────────────────────────────────
    def load(self) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        if self.path.exists():
            try:
                raw = json.loads(self.path.read_text(encoding="utf-8") or "{}")
            except (json.JSONDecodeError, OSError):
                raw = {}
        with self._lock:
            self._data = _deep_merge(DEFAULTS, raw if isinstance(raw, dict) else {})
            if not self.path.exists():
                self._write()
            return self._data

    def _write(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps(self._data, indent=2, ensure_ascii=False) + "\n"
        fd, tmp = tempfile.mkstemp(dir=str(self.path.parent or "."), suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(payload)
            os.replace(tmp, self.path)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)

    def save(self) -> None:
        with self._lock:
            self._write()

    # ── Accès ────────────────────────────────────────────────────────────
    @property
    def data(self) -> dict[str, Any]:
        with self._lock:
            return copy.deepcopy(self._data)

    def get(self, path: str, default: Any = None) -> Any:
        with self._lock:
            node: Any = self._data
            for part in path.split("."):
                if not isinstance(node, dict) or part not in node:
                    return default
                node = node[part]
            return copy.deepcopy(node)

    def public(self) -> dict[str, Any]:
        """Configuration exposée au dashboard (webhook masqué)."""
        data = self.data
        data["discord"]["default_webhook_masked"] = mask_webhook(
            data["discord"].get("default_webhook", "")
        )
        data["app"]["password_set"] = bool(data["app"].get("password"))
        data["app"]["password"] = ""
        return data

    def apply_patch(self, patch: dict[str, Any]) -> dict[str, Any]:
        """Applique uniquement les clés autorisées, avec conversion de type."""
        if not isinstance(patch, dict):
            raise ConfigError("Configuration invalide.")
        changes: dict[str, Any] = {}
        for path, value in _flatten(patch):
            spec = EDITABLE.get(path)
            if spec is None:
                raise ConfigError(f"Paramètre inconnu ou non modifiable : {path}")
            changes[path] = self._validate(path, spec, value)
        if not changes:
            return self.public()
        with self._lock:
            for path, value in changes.items():
                node = self._data
                parts = path.split(".")
                for part in parts[:-1]:
                    node = node.setdefault(part, {})
                node[parts[-1]] = value
            self._write()
        return self.public()

    @staticmethod
    def _validate(path: str, spec: tuple, value: Any) -> Any:
        kind = spec[0]
        if kind == "bool":
            if isinstance(value, str):
                return value.strip().lower() in {"1", "true", "yes", "on", "oui"}
            return bool(value)
        if kind in {"int", "float"}:
            try:
                number = (
                    float(str(value).replace(",", "."))
                    if kind == "float"
                    else int(float(value))
                )
            except (TypeError, ValueError):
                raise ConfigError(f"{path} : nombre attendu.") from None
            low, high = spec[1], spec[2]
            if not (low <= number <= high):
                raise ConfigError(f"{path} : valeur hors bornes ({low} → {high}).")
            return number
        if kind == "str":
            text = str(value or "").strip()
            if len(text) > spec[1]:
                raise ConfigError(f"{path} : {spec[1]} caractères maximum.")
            return text
        if kind == "url":
            text = str(value or "").strip()
            if text and not re.match(r"^https?://", text):
                raise ConfigError(f"{path} : URL http(s) attendue.")
            return text
        if kind == "webhook":
            text = str(value or "").strip()
            if text and not re.match(
                r"^https://(?:ptb\.|canary\.)?discord(?:app)?\.com/api/webhooks/\d+/[\w-]+(?:[?#].*)?$",
                text,
            ):
                raise ConfigError(
                    "Webhook Discord invalide (URL https://discord.com/api/webhooks/… attendue)."
                )
            return text
        if kind == "strlist":
            if isinstance(value, str):
                value = re.split(r"[\n,;]", value)
            if not isinstance(value, (list, tuple)):
                raise ConfigError(f"{path} : liste attendue.")
            cleaned = [str(item).strip() for item in value if str(item).strip()]
            if len(cleaned) > spec[1]:
                raise ConfigError(f"{path} : {spec[1]} entrées maximum.")
            return cleaned
        raise ConfigError(f"{path} : type non supporté.")
