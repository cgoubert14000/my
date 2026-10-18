from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time
from zoneinfo import ZoneInfo

from facebook_bot.images import ImageItem
from facebook_bot.text_settings import ScheduleDefinition


@dataclass(frozen=True)
class PlannedPost:
    # window_index conserve ce nom dans SQLite pour la compatibilité ; il s'agit
    # maintenant du numéro du document horraire1, horraire2 ou horraire3.
    window_index: int
    scheduled_at: datetime
    window_end: datetime
    item: ImageItem


def build_plan(
    *,
    day: date,
    items: list[ImageItem],
    timezone: ZoneInfo,
    schedules: tuple[ScheduleDefinition, ...],
) -> list[PlannedPost]:
    """Répartit les images entre les documents d'horaires sélectionnés."""
    capacities = tuple(len(schedule.times) for schedule in schedules)
    capacity = sum(capacities)
    if len(items) > capacity:
        raise ValueError(f"Le planning sélectionné accepte au maximum {capacity} images.")
    if not items:
        return []

    counts = distribute_count(len(items), capacities=capacities)
    end = datetime.combine(day, time(23, 59), tzinfo=timezone)
    planned_times: list[tuple[int, datetime, datetime]] = []
    for schedule, count in zip(schedules, counts, strict=True):
        for scheduled_time in schedule.times[:count]:
            scheduled_at = datetime.combine(day, scheduled_time, tzinfo=timezone)
            planned_times.append((schedule.index, scheduled_at, end))

    planned_times.sort(key=lambda entry: entry[1])
    if len({entry[1] for entry in planned_times}) != len(planned_times):
        raise ValueError("Deux documents contiennent la même heure de publication.")

    return [
        PlannedPost(
            window_index=schedule_index,
            scheduled_at=scheduled_at,
            window_end=window_end,
            item=item,
        )
        for item, (schedule_index, scheduled_at, window_end) in zip(
            items,
            planned_times,
            strict=True,
        )
    ]


def distribute_count(
    total: int,
    *,
    capacities: tuple[int, ...] = (17, 17, 17, 17),
) -> tuple[int, ...]:
    if total < 0:
        raise ValueError("Le nombre d'images ne peut pas être négatif.")
    if not capacities or any(capacity < 0 for capacity in capacities):
        raise ValueError("Capacités d'horaires invalides.")
    if total > sum(capacities):
        raise ValueError(f"Maximum autorisé : {sum(capacities)} images.")

    counts = [0] * len(capacities)
    remaining = total
    while remaining:
        progressed = False
        for index, capacity in enumerate(capacities):
            if remaining == 0:
                break
            if counts[index] < capacity:
                counts[index] += 1
                remaining -= 1
                progressed = True
        if not progressed:
            raise ValueError("Impossible de répartir toutes les images.")
    return tuple(counts)
