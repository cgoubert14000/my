from __future__ import annotations

import os
import re
from dataclasses import dataclass
from datetime import date, datetime, time
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from dotenv import load_dotenv

_TIME_RE = re.compile(r"^(?P<hour>[01]\d|2[0-3]):(?P<minute>[0-5]\d)$")
_API_VERSION_RE = re.compile(r"^v\d+\.\d+$")
DEFAULT_PAGE_ID = "1098568206676051"
DEFAULT_PAGE_NAME = "Madame Portugais"
DEFAULT_API_VERSION = "v26.0"
DEFAULT_FIXED_HASHTAGS = (
    "#portugal #portugais #france #francais #cours #apprendre #quiz"
)


class ConfigError(ValueError):
    """Configuration invalide ou incomplète."""


@dataclass(frozen=True)
class PostingWindow:
    start: time
    end: time

    def bounds(self, day: date, timezone: ZoneInfo) -> tuple[datetime, datetime]:
        return (
            datetime.combine(day, self.start, tzinfo=timezone),
            datetime.combine(day, self.end, tzinfo=timezone),
        )

    def __str__(self) -> str:
        return f"{self.start:%H:%M}-{self.end:%H:%M}"


@dataclass(frozen=True)
class Config:
    page_id: str
    page_access_token: str
    expected_page_name: str
    api_version: str
    timezone: ZoneInfo
    timezone_name: str
    image_dir: Path
    archive_dir: Path
    state_db: Path
    queue_order: str
    default_caption: str
    fixed_hashtags: str
    max_late_minutes: int
    poll_interval_seconds: int
    retry_interval_minutes: int
    max_post_attempts: int
    http_timeout_seconds: int

    @classmethod
    def from_env(
        cls,
        env_file: str | Path | None = None,
        *,
        require_facebook: bool = True,
    ) -> Config:
        if env_file is None:
            load_dotenv()
        else:
            env_path = Path(env_file).expanduser().resolve()
            if not env_path.is_file():
                raise ConfigError(f"Fichier de configuration introuvable : {env_path}")
            load_dotenv(env_path, override=True)

        page_id = os.getenv("FACEBOOK_PAGE_ID", DEFAULT_PAGE_ID).strip()
        token = os.getenv("FACEBOOK_PAGE_ACCESS_TOKEN", "").strip()
        if require_facebook:
            if not page_id or not page_id.isdigit():
                raise ConfigError(
                    "FACEBOOK_PAGE_ID doit contenir l'identifiant numérique de la Page."
                )
            if not token or token == "collez_votre_jeton_de_page_ici":
                raise ConfigError("FACEBOOK_PAGE_ACCESS_TOKEN est absent du fichier .env.")

        api_version = os.getenv("FACEBOOK_API_VERSION", DEFAULT_API_VERSION).strip()
        if not _API_VERSION_RE.fullmatch(api_version):
            raise ConfigError("FACEBOOK_API_VERSION doit avoir un format tel que v26.0.")

        timezone_name = os.getenv("BOT_TIMEZONE", "Europe/Paris").strip()
        try:
            timezone = ZoneInfo(timezone_name)
        except ZoneInfoNotFoundError as exc:
            raise ConfigError(f"Fuseau horaire inconnu : {timezone_name}") from exc

        base_dir = Path.cwd()
        image_dir = _path_from_env("IMAGE_DIR", "images/to_post", base_dir)
        archive_dir = _path_from_env("ARCHIVE_DIR", "images/posted", base_dir)
        state_db = _path_from_env("STATE_DB", "data/facebook_bot.sqlite3", base_dir)
        if image_dir == archive_dir:
            raise ConfigError("IMAGE_DIR et ARCHIVE_DIR doivent être deux dossiers différents.")

        queue_order = os.getenv("QUEUE_ORDER", "oldest").strip().lower()
        if queue_order not in {"oldest", "alphabetical", "random"}:
            raise ConfigError("QUEUE_ORDER doit valoir oldest, alphabetical ou random.")

        return cls(
            page_id=page_id,
            page_access_token=token,
            expected_page_name=os.getenv(
                "FACEBOOK_EXPECTED_PAGE_NAME", DEFAULT_PAGE_NAME
            ).strip(),
            api_version=api_version,
            timezone=timezone,
            timezone_name=timezone_name,
            image_dir=image_dir,
            archive_dir=archive_dir,
            state_db=state_db,
            queue_order=queue_order,
            default_caption=os.getenv("DEFAULT_CAPTION", ""),
            fixed_hashtags=(
                os.getenv("FIXED_HASHTAGS", DEFAULT_FIXED_HASHTAGS).strip()
                or DEFAULT_FIXED_HASHTAGS
            ),
            max_late_minutes=_int_env("MAX_LATE_MINUTES", 15, minimum=1),
            poll_interval_seconds=_int_env("POLL_INTERVAL_SECONDS", 15, minimum=2),
            retry_interval_minutes=_int_env("RETRY_INTERVAL_MINUTES", 10, minimum=1),
            max_post_attempts=_int_env("MAX_POST_ATTEMPTS", 3, minimum=1, maximum=10),
            http_timeout_seconds=_int_env("HTTP_TIMEOUT_SECONDS", 120, minimum=10),
        )

    def prepare_directories(self) -> None:
        self.image_dir.mkdir(parents=True, exist_ok=True)
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        self.state_db.parent.mkdir(parents=True, exist_ok=True)


def parse_posting_windows(value: str) -> tuple[PostingWindow, PostingWindow, PostingWindow]:
    chunks = [chunk.strip() for chunk in value.split(",") if chunk.strip()]
    if len(chunks) != 3:
        raise ConfigError(
            "POSTING_WINDOWS doit contenir exactement 3 plages séparées par des virgules."
        )

    windows: list[PostingWindow] = []
    for chunk in chunks:
        parts = chunk.split("-")
        if len(parts) != 2:
            raise ConfigError(f"Plage invalide « {chunk} » ; format attendu : HH:MM-HH:MM.")
        start = _parse_time(parts[0].strip(), chunk)
        end = _parse_time(parts[1].strip(), chunk)
        if start >= end:
            raise ConfigError(
                f"Plage invalide « {chunk} » : la fin doit être après le début le même jour."
            )
        windows.append(PostingWindow(start, end))

    windows.sort(key=lambda window: window.start)
    for previous, current in zip(windows, windows[1:], strict=False):
        if previous.end > current.start:
            raise ConfigError(f"Les plages {previous} et {current} se chevauchent.")

    return (windows[0], windows[1], windows[2])


def _parse_time(value: str, window: str) -> time:
    match = _TIME_RE.fullmatch(value)
    if not match:
        raise ConfigError(f"Heure invalide dans « {window} » ; utilisez le format HH:MM.")
    return time(hour=int(match.group("hour")), minute=int(match.group("minute")))


def _path_from_env(name: str, default: str, base_dir: Path) -> Path:
    path = Path(os.getenv(name, default).strip()).expanduser()
    if not path.is_absolute():
        path = base_dir / path
    return path.resolve()


def _int_env(name: str, default: int, *, minimum: int, maximum: int | None = None) -> int:
    raw_value = os.getenv(name, str(default)).strip()
    try:
        value = int(raw_value)
    except ValueError as exc:
        raise ConfigError(f"{name} doit être un nombre entier.") from exc
    if value < minimum or (maximum is not None and value > maximum):
        interval = f"entre {minimum} et {maximum}" if maximum is not None else f"au moins {minimum}"
        raise ConfigError(f"{name} doit être {interval}.")
    return value
