from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

from facebook_bot.images import ImageItem

SCHEDULE_MINUTES = (30, 15, 45)
SCHEDULE_START_HOUR = 7
SCHEDULE_END_HOUR = 23


@dataclass(frozen=True)
class PlannedPost:
    window_index: int
    scheduled_at: datetime
    window_end: datetime
    item: ImageItem


# window_index reste nommé ainsi dans la base pour assurer la compatibilité avec
# les premières versions ; il représente désormais le numéro d'horaire 1, 2 ou 3.
def build_plan(
    *,
    day: date,
    items: list[ImageItem],
    timezone: ZoneInfo,
    max_per_schedule: int = 30,
) -> list[PlannedPost]:
    """Répartit jusqu'à 90 images entre trois horaires qui se chevauchent."""
    capacity = max_per_schedule * len(SCHEDULE_MINUTES)
    if len(items) > capacity:
        raise ValueError(f"Le planning accepte au maximum {capacity} images par date.")
    if not items:
        return []

    counts = distribute_count(len(items), max_per_schedule=max_per_schedule)
    times: list[tuple[int, datetime, datetime]] = []
    for schedule_index, (minute, count) in enumerate(
        zip(SCHEDULE_MINUTES, counts, strict=True),
        start=1,
    ):
        schedule_times = _times_for_schedule(
            day=day,
            minute=minute,
            count=count,
            timezone=timezone,
        )
        end = datetime.combine(day, time(23, 59), tzinfo=timezone)
        times.extend((schedule_index, scheduled_at, end) for scheduled_at in schedule_times)

    times.sort(key=lambda entry: entry[1])
    times = _make_times_distinct(times)
    times.sort(key=lambda entry: entry[1])
    return [
        PlannedPost(
            window_index=schedule_index,
            scheduled_at=scheduled_at,
            window_end=window_end,
            item=item,
        )
        for item, (schedule_index, scheduled_at, window_end) in zip(items, times, strict=True)
    ]


def distribute_count(total: int, *, max_per_schedule: int = 30) -> tuple[int, int, int]:
    if total < 0:
        raise ValueError("Le nombre d'images ne peut pas être négatif.")
    if total > max_per_schedule * 3:
        raise ValueError(f"Maximum autorisé : {max_per_schedule * 3} images.")

    base, remainder = divmod(total, 3)
    counts = [base, base, base]
    for index in range(remainder):
        counts[index] += 1
    if any(count > max_per_schedule for count in counts):
        raise ValueError(f"Maximum autorisé par horaire : {max_per_schedule} images.")
    return counts[0], counts[1], counts[2]


def _times_for_schedule(
    *,
    day: date,
    minute: int,
    count: int,
    timezone: ZoneInfo,
) -> list[datetime]:
    if count == 0:
        return []
    first = datetime.combine(day, time(SCHEDULE_START_HOUR, minute), tzinfo=timezone)
    if count == 1:
        return [first]

    # Jusqu'à 17 publications, l'exemple demandé est suivi à la lettre : une par
    # heure (07:15, 08:15... ou :30 / :45). Au-delà, l'intervalle est réduit
    # régulièrement afin de conserver les 30 publications sur la même date.
    hourly_capacity = SCHEDULE_END_HOUR - SCHEDULE_START_HOUR + 1
    if count <= hourly_capacity:
        return [first + timedelta(hours=index) for index in range(count)]

    last = datetime.combine(day, time(SCHEDULE_END_HOUR, minute), tzinfo=timezone)
    total_minutes = int((last - first).total_seconds() // 60)
    return [
        first + timedelta(minutes=round(index * total_minutes / (count - 1)))
        for index in range(count)
    ]


def _make_times_distinct(
    times: list[tuple[int, datetime, datetime]],
) -> list[tuple[int, datetime, datetime]]:
    seen: set[datetime] = set()
    adjusted: list[tuple[int, datetime, datetime]] = []
    for schedule_index, scheduled_at, window_end in times:
        candidate = scheduled_at
        while candidate in seen and candidate <= window_end:
            candidate += timedelta(minutes=1)
        if candidate > window_end:
            candidate = scheduled_at - timedelta(minutes=1)
            while candidate in seen and candidate.date() == scheduled_at.date():
                candidate -= timedelta(minutes=1)
        if candidate.date() != scheduled_at.date():
            raise ValueError("Impossible de créer des horaires distincts sur cette date.")
        seen.add(candidate)
        adjusted.append((schedule_index, candidate, window_end))
    return adjusted
