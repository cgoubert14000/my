from datetime import date
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from facebook_bot.images import ImageItem
from facebook_bot.planner import build_plan, distribute_count

TZ = ZoneInfo("Europe/Paris")


def _items(count: int) -> list[ImageItem]:
    return [
        ImageItem(Path(f"image-{index:02d}.jpg"), None, "légende", f"hash-{index}")
        for index in range(count)
    ]


@pytest.mark.parametrize(
    ("total", "expected"),
    [
        (1, (1, 0, 0)),
        (2, (1, 1, 0)),
        (3, (1, 1, 1)),
        (4, (2, 1, 1)),
        (89, (30, 30, 29)),
        (90, (30, 30, 30)),
    ],
)
def test_distribute_count_balances_three_schedules(total, expected) -> None:
    assert distribute_count(total) == expected


def test_nine_images_follow_requested_hourly_examples() -> None:
    plan = build_plan(
        day=date(2026, 10, 20),
        items=_items(9),
        timezone=TZ,
    )

    by_schedule = {
        schedule: [
            entry.scheduled_at.strftime("%H:%M")
            for entry in plan
            if entry.window_index == schedule
        ]
        for schedule in (1, 2, 3)
    }
    assert by_schedule == {
        1: ["07:30", "08:30", "09:30"],
        2: ["07:15", "08:15", "09:15"],
        3: ["07:45", "08:45", "09:45"],
    }


def test_plan_fits_90_images_on_same_date_with_distinct_times() -> None:
    day = date(2026, 10, 20)
    plan = build_plan(day=day, items=_items(90), timezone=TZ)

    assert len(plan) == 90
    assert [sum(entry.window_index == index for entry in plan) for index in (1, 2, 3)] == [
        30,
        30,
        30,
    ]
    assert len({entry.scheduled_at for entry in plan}) == 90
    assert all(entry.scheduled_at.date() == day for entry in plan)
    assert min(entry.scheduled_at for entry in plan).strftime("%H:%M") == "07:15"
    assert max(entry.scheduled_at for entry in plan).strftime("%H:%M") == "23:45"


def test_plan_refuses_more_than_90_images() -> None:
    with pytest.raises(ValueError, match="90"):
        build_plan(
            day=date(2026, 10, 20),
            items=_items(91),
            timezone=TZ,
        )
