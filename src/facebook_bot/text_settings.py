from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import time
from pathlib import Path

from facebook_bot.config import DEFAULT_FIXED_HASHTAGS, ConfigError

SCHEDULE_FILENAMES = ("horraire1.txt", "horraire2.txt", "horraire3.txt")
HASHTAGS_FILENAME = "hashtags.txt"
_TIME_PATTERN = re.compile(r"(?<!\d)([01]?\d|2[0-3])\s*(?:h|:)\s*([0-5]\d)(?!\d)", re.I)


@dataclass(frozen=True)
class ScheduleDefinition:
    index: int
    filename: str
    times: tuple[time, ...]

    @property
    def first(self) -> time:
        return self.times[0]

    @property
    def last(self) -> time:
        return self.times[-1]


def load_schedule_definitions(base_dir: Path) -> tuple[ScheduleDefinition, ...]:
    definitions = tuple(
        _load_schedule_file(base_dir / filename, index)
        for index, filename in enumerate(SCHEDULE_FILENAMES, start=1)
    )
    seen: dict[time, str] = {}
    for definition in definitions:
        for scheduled_time in definition.times:
            previous = seen.get(scheduled_time)
            if previous is not None:
                raise ConfigError(
                    f"L'heure {scheduled_time:%H:%M} apparaît dans {previous} et "
                    f"{definition.filename}. Chaque heure doit être unique."
                )
            seen[scheduled_time] = definition.filename
    return definitions


def load_hashtags(base_dir: Path, *, fallback: str = DEFAULT_FIXED_HASHTAGS) -> str:
    path = base_dir / HASHTAGS_FILENAME
    if not path.is_file():
        return " ".join(fallback.split())
    try:
        content = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        raise ConfigError(f"Impossible de lire {HASHTAGS_FILENAME}.") from exc

    tags = []
    for word in content.split():
        cleaned = word.strip(",;.")
        if not cleaned:
            continue
        if not cleaned.startswith("#"):
            cleaned = f"#{cleaned}"
        if cleaned not in tags:
            tags.append(cleaned)
    return " ".join(tags)


def _load_schedule_file(path: Path, index: int) -> ScheduleDefinition:
    if not path.is_file():
        raise ConfigError(f"Document d'horaires introuvable : {path.name}")
    try:
        content = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        raise ConfigError(f"Impossible de lire {path.name}.") from exc

    parsed_times = {
        time(hour=int(match.group(1)), minute=int(match.group(2)))
        for match in _TIME_PATTERN.finditer(content)
    }
    if not parsed_times:
        raise ConfigError(
            f"Aucune heure trouvée dans {path.name}. Exemple accepté : 07h30."
        )
    ordered = tuple(sorted(parsed_times))
    return ScheduleDefinition(index=index, filename=path.name, times=ordered)
