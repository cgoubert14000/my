from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

from facebook_bot.config import Config
from facebook_bot.facebook import (
    FacebookError,
    FacebookSchedulingUncertain,
    PageInfo,
    PublishReceipt,
)
from facebook_bot.images import ImageItem, file_sha256
from facebook_bot.planner import build_plan
from facebook_bot.runner import BotRunner
from facebook_bot.state import StateStore
from facebook_bot.text_settings import ScheduleDefinition

TZ = ZoneInfo("Europe/Paris")


class FakeSchedulingPublisher:
    def __init__(self, *, uncertain: bool = False) -> None:
        self.uncertain = uncertain
        self.calls = []

    def verify_destination(self, expected_page_name: str) -> PageInfo:
        assert expected_page_name == "Madame Portugais"
        return PageInfo(id="1098568206676051", name=expected_page_name)

    def schedule_photo(self, image_path, caption, scheduled_at):
        self.calls.append((image_path, caption, scheduled_at))
        if self.uncertain:
            raise FacebookSchedulingUncertain("réponse perdue", photo_id="media-unknown")
        index = len(self.calls)
        return PublishReceipt(photo_id=f"media-{index}", post_id=f"page_post-{index}")


class RejectSecondPublisher(FakeSchedulingPublisher):
    def schedule_photo(self, image_path, caption, scheduled_at):
        self.calls.append((image_path, caption, scheduled_at))
        if len(self.calls) == 2:
            raise FacebookError("requête refusée")
        return PublishReceipt(photo_id="media-1", post_id="page_post-1")


def _config(tmp_path) -> Config:
    return Config(
        page_id="1098568206676051",
        page_access_token="token",
        expected_page_name="Madame Portugais",
        api_version="v26.0",
        timezone=TZ,
        timezone_name="Europe/Paris",
        image_dir=tmp_path / "images" / "to_post",
        archive_dir=tmp_path / "images" / "posted",
        state_db=tmp_path / "data" / "state.sqlite3",
        queue_order="alphabetical",
        default_caption="",
        fixed_hashtags="",
        max_late_minutes=15,
        poll_interval_seconds=15,
        retry_interval_minutes=10,
        max_post_attempts=3,
        http_timeout_seconds=120,
    )


def _create_future_plan(config: Config, count: int = 2) -> tuple[StateStore, list[ImageItem]]:
    config.prepare_directories()
    items = []
    for index in range(count):
        path = config.image_dir / f"photo-{index}.jpg"
        path.write_bytes(f"photo-{index}".encode())
        items.append(
            ImageItem(
                path=path,
                caption_path=None,
                caption=f"Légende {index}",
                fingerprint=file_sha256(path),
            )
        )
    future_day = datetime.now(TZ).date() + timedelta(days=2)
    schedule = ScheduleDefinition(
        index=1,
        filename="horraire1.txt",
        times=tuple(time(7 + index, 30) for index in range(count)),
    )
    plan = build_plan(
        day=future_day,
        items=items,
        timezone=TZ,
        schedules=(schedule,),
    )
    store = StateStore(config.state_db)
    store.initialize()
    store.create_plan(future_day, plan)
    return store, items


def test_advance_scheduler_sends_every_post_then_archives_images(tmp_path) -> None:
    config = _config(tmp_path)
    store, items = _create_future_plan(config)
    runner = BotRunner(config)
    publisher = FakeSchedulingPublisher()
    runner.publisher = publisher

    result = runner.schedule_pending_on_facebook()

    assert result.succeeded
    assert result.scheduled == 2
    assert result.pending == result.uncertain == 0
    assert len(publisher.calls) == 2
    assert all(store.was_posted(item.fingerprint) for item in items)
    assert [post.status for post in store.scheduled_for_day(
        datetime.now(TZ).date() + timedelta(days=2)
    )] == ["facebook_scheduled", "facebook_scheduled"]
    assert not any(item.path.exists() for item in items)


def test_retry_only_sends_items_not_yet_accepted_by_facebook(tmp_path) -> None:
    config = _config(tmp_path)
    store, items = _create_future_plan(config)
    runner = BotRunner(config)
    rejecting_publisher = RejectSecondPublisher()
    runner.publisher = rejecting_publisher

    first_result = runner.schedule_pending_on_facebook()

    assert first_result.scheduled == 1
    assert first_result.pending == 1
    assert [call[0] for call in rejecting_publisher.calls] == [items[0].path, items[1].path]

    retry_publisher = FakeSchedulingPublisher()
    runner.publisher = retry_publisher
    second_result = runner.schedule_pending_on_facebook()

    assert second_result.succeeded
    assert second_result.scheduled == 1
    assert [call[0].name for call in retry_publisher.calls] == [items[1].path.name]
    assert store.publication_status_counts() == {"facebook_scheduled": 2}


def test_advance_scheduler_never_retries_an_uncertain_post(tmp_path) -> None:
    config = _config(tmp_path)
    store, _items = _create_future_plan(config)
    runner = BotRunner(config)
    publisher = FakeSchedulingPublisher(uncertain=True)
    runner.publisher = publisher

    first_result = runner.schedule_pending_on_facebook()
    second_result = runner.schedule_pending_on_facebook()

    assert first_result.scheduled == 0
    assert first_result.uncertain == 1
    assert first_result.pending == 1
    assert second_result.uncertain == 2
    assert len(publisher.calls) == 2
    assert publisher.calls[0][0] != publisher.calls[1][0]
    statuses = store.publication_status_counts()
    assert statuses == {"uncertain": 2}
