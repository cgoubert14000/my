import random
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from facebook_bot.config import parse_posting_windows
from facebook_bot.facebook import PublishReceipt
from facebook_bot.images import ImageItem
from facebook_bot.state import StateStore

TZ = ZoneInfo("Europe/Paris")
WINDOWS = parse_posting_windows("07:00-10:00,12:00-15:00,18:00-22:00")


def test_schedule_is_persisted_and_inside_each_window(tmp_path) -> None:
    store = StateStore(tmp_path / "state.sqlite3")
    store.initialize()
    now = datetime(2026, 10, 17, 6, 0, tzinfo=TZ)

    first = store.ensure_day(date(2026, 10, 17), WINDOWS, TZ, now=now, rng=random.Random(4))
    second = store.ensure_day(
        date(2026, 10, 17), WINDOWS, TZ, now=now, rng=random.Random(999)
    )

    assert [slot.scheduled_at for slot in first] == [slot.scheduled_at for slot in second]
    assert len(first) == 3
    for slot in first:
        assert slot.window_start <= slot.scheduled_at <= slot.window_end
        assert slot.status == "pending"


def test_late_start_marks_finished_windows_missed(tmp_path) -> None:
    store = StateStore(tmp_path / "state.sqlite3")
    store.initialize()
    now = datetime(2026, 10, 17, 16, 0, tzinfo=TZ)

    slots = store.ensure_day(date(2026, 10, 17), WINDOWS, TZ, now=now, rng=random.Random(1))

    assert [slot.status for slot in slots] == ["missed", "missed", "pending"]
    assert slots[2].scheduled_at > now


def test_claim_record_and_deduplicate_image(tmp_path) -> None:
    store = StateStore(tmp_path / "state.sqlite3")
    store.initialize()
    now = datetime(2026, 10, 17, 7, 0, tzinfo=TZ)
    slots = store.ensure_day(date(2026, 10, 17), WINDOWS, TZ, now=now, rng=random.Random(1))
    due_time = slots[0].scheduled_at

    claimed = store.claim_due_slot(due_time)
    assert claimed is not None
    assert claimed.status == "running"
    assert store.mark_post_attempt(claimed) == 1

    image_path = tmp_path / "photo.jpg"
    image_path.write_bytes(b"photo")
    item = ImageItem(image_path, None, "bonjour", "abc123")
    store.record_slot_success(
        claimed,
        item,
        PublishReceipt(photo_id="photo-id", post_id="post-id"),
        due_time,
    )

    assert store.was_posted("abc123")
    assert store.slots_for_day(date(2026, 10, 17))[0].status == "completed"


def test_empty_slot_can_be_rescheduled(tmp_path) -> None:
    store = StateStore(tmp_path / "state.sqlite3")
    store.initialize()
    now = datetime(2026, 10, 17, 7, 0, tzinfo=TZ)
    slots = store.ensure_day(date(2026, 10, 17), WINDOWS, TZ, now=now, rng=random.Random(2))
    claimed = store.claim_due_slot(slots[0].scheduled_at)
    assert claimed is not None

    later = claimed.scheduled_at + timedelta(minutes=5)
    store.reschedule(claimed, later, "vide")
    refreshed = store.slots_for_day(date(2026, 10, 17))[0]

    assert refreshed.status == "pending"
    assert refreshed.scheduled_at == later
    assert refreshed.last_error == "vide"
