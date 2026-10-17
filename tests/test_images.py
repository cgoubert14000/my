from datetime import datetime
from zoneinfo import ZoneInfo

from facebook_bot.images import ImageQueue, file_sha256


def test_queue_reads_sidecar_and_archives(tmp_path) -> None:
    inbox = tmp_path / "inbox"
    archive = tmp_path / "archive"
    inbox.mkdir()
    image = inbox / "01-photo.jpg"
    image.write_bytes(b"fake jpeg content")
    caption = inbox / "01-photo.txt"
    caption.write_text("Une légende en français.\n", encoding="utf-8")
    queue = ImageQueue(
        image_dir=inbox,
        archive_dir=archive,
        queue_order="oldest",
        default_caption="défaut",
    )

    item = queue.next_item(lambda _fingerprint: False)

    assert item is not None
    assert item.caption == "Une légende en français."
    assert item.fingerprint == file_sha256(image)

    destination = queue.archive(
        item, datetime(2026, 10, 17, 12, tzinfo=ZoneInfo("Europe/Paris"))
    )
    assert destination == archive / "2026-10-17" / "01-photo.jpg"
    assert destination.read_bytes() == b"fake jpeg content"
    assert destination.with_suffix(".txt").read_text(encoding="utf-8") == (
        "Une légende en français.\n"
    )
    assert not image.exists()


def test_queue_ignores_already_posted_hash(tmp_path) -> None:
    inbox = tmp_path / "inbox"
    inbox.mkdir()
    image = inbox / "photo.png"
    image.write_bytes(b"image")
    queue = ImageQueue(
        image_dir=inbox,
        archive_dir=tmp_path / "archive",
        queue_order="alphabetical",
        default_caption="",
    )

    assert queue.next_item(lambda value: value == file_sha256(image)) is None
