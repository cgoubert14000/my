from datetime import date, time
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from facebook_bot.images import ImageItem
from facebook_bot.planner import build_plan, distribute_count
from facebook_bot.text_settings import ScheduleDefinition

TZ = ZoneInfo("Europe/Paris")
SCHEDULES = (
    ScheduleDefinition(1, "horraire1.txt", tuple(time(hour, 30) for hour in range(7, 24))),
    ScheduleDefinition(2, "horraire2.txt", tuple(time(hour, 15) for hour in range(7, 24))),
    ScheduleDefinition(3, "horraire3.txt", tuple(time(hour, 45) for hour in range(7, 24))),
)


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
        (50, (17, 17, 16)),
        (51, (17, 17, 17)),
    ],
)
def test_distribute_count_balances_three_schedules(total, expected) -> None:
    assert distribute_count(total) == expected


def test_nine_images_start_at_seven_and_advance_hourly() -> None:
    plan = build_plan(
        day=date(2026, 10, 20),
        items=_items(9),
        timezone=TZ,
        schedules=SCHEDULES,
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


def test_45_images_make_15_hourly_posts_in_each_interleaved_schedule() -> None:
    plan = build_plan(
        day=date(2026, 10, 20),
        items=_items(45),
        timezone=TZ,
        schedules=SCHEDULES,
    )

    by_schedule = {
        schedule: [
            entry.scheduled_at.strftime("%H:%M")
            for entry in plan
            if entry.window_index == schedule
        ]
        for schedule in (1, 2, 3)
    }
    assert len(by_schedule[1]) == len(by_schedule[2]) == len(by_schedule[3]) == 15
    assert (by_schedule[1][0], by_schedule[1][-1]) == ("07:30", "21:30")
    assert (by_schedule[2][0], by_schedule[2][-1]) == ("07:15", "21:15")
    assert (by_schedule[3][0], by_schedule[3][-1]) == ("07:45", "21:45")
    assert len({entry.scheduled_at for entry in plan}) == 45


def test_selecting_only_schedule_one_uses_only_its_text_times() -> None:
    plan = build_plan(
        day=date(2026, 10, 20),
        items=_items(4),
        timezone=TZ,
        schedules=(SCHEDULES[0],),
    )

    assert [entry.scheduled_at.strftime("%H:%M") for entry in plan] == [
        "07:30",
        "08:30",
        "09:30",
        "10:30",
    ]
    assert all(entry.window_index == 1 for entry in plan)


def test_plan_refuses_more_images_than_selected_documents_can_hold() -> None:
    with pytest.raises(ValueError, match="17"):
        build_plan(
            day=date(2026, 10, 20),
            items=_items(18),
            timezone=TZ,
            schedules=(SCHEDULES[0],),
        )
