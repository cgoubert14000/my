import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest
import requests

from facebook_bot.facebook import (
    FacebookError,
    FacebookPublisher,
    FacebookSchedulingUncertain,
)


class FakeResponse:
    def __init__(self, payload, *, ok=True, status_code=200):
        self._payload = payload
        self.ok = ok
        self.status_code = status_code

    def json(self):
        return self._payload


class FakeSession:
    def __init__(self, response):
        self.headers = {}
        self.responses = response if isinstance(response, list) else [response]
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append((method, url, kwargs))
        response = self.responses.pop(0)
        if isinstance(response, BaseException):
            raise response
        return response


def test_publish_uses_bearer_header_not_query_string(tmp_path: Path) -> None:
    image = tmp_path / "photo.jpg"
    image.write_bytes(b"photo")
    session = FakeSession(FakeResponse({"id": "42", "post_id": "1_42"}))
    publisher = FacebookPublisher(
        page_id="1",
        access_token="secret-token",
        api_version="v24.0",
        session=session,
    )

    receipt = publisher.publish_photo(image, "Bonjour")

    assert receipt.photo_id == "42"
    assert session.headers["Authorization"] == "Bearer secret-token"
    assert "secret-token" not in session.calls[0][1]
    assert session.calls[0][2]["data"]["caption"] == "Bonjour"


def test_schedule_photo_uploads_temporary_media_then_creates_scheduled_post(tmp_path) -> None:
    image = tmp_path / "photo.jpg"
    image.write_bytes(b"photo")
    session = FakeSession(
        [
            FakeResponse({"id": "photo-42"}),
            FakeResponse({"id": "page_scheduled-post-99"}),
        ]
    )
    publisher = FacebookPublisher(
        page_id="page",
        access_token="token",
        api_version="v26.0",
        session=session,
    )
    scheduled_at = datetime(2026, 10, 19, 7, 15, tzinfo=ZoneInfo("Europe/Paris"))

    receipt = publisher.schedule_photo(image, "Bonjour", scheduled_at)

    assert receipt.photo_id == "photo-42"
    assert receipt.post_id == "page_scheduled-post-99"
    assert session.calls[0][1].endswith("/page/photos")
    assert session.calls[0][2]["data"] == {"published": "false", "temporary": "true"}
    assert session.calls[1][1].endswith("/page/feed")
    feed_data = session.calls[1][2]["data"]
    assert feed_data["message"] == "Bonjour"
    assert feed_data["published"] == "false"
    assert feed_data["unpublished_content_type"] == "SCHEDULED"
    assert json.loads(feed_data["attached_media"]) == [{"media_fbid": "photo-42"}]
    assert feed_data["scheduled_publish_time"] == str(int(scheduled_at.timestamp()))


def test_schedule_photo_marks_lost_feed_response_as_uncertain(tmp_path) -> None:
    image = tmp_path / "photo.jpg"
    image.write_bytes(b"photo")
    session = FakeSession(
        [
            FakeResponse({"id": "photo-42"}),
            requests.Timeout("response lost"),
        ]
    )
    publisher = FacebookPublisher(
        page_id="page",
        access_token="token",
        api_version="v26.0",
        session=session,
    )

    with pytest.raises(FacebookSchedulingUncertain) as error:
        publisher.schedule_photo(
            image,
            "Bonjour",
            datetime(2026, 10, 19, 7, 15, tzinfo=ZoneInfo("Europe/Paris")),
        )

    assert error.value.photo_id == "photo-42"
    assert len(session.calls) == 2


def test_schedule_photo_can_retry_after_definite_feed_rejection(tmp_path) -> None:
    image = tmp_path / "photo.jpg"
    image.write_bytes(b"photo")
    session = FakeSession(
        [
            FakeResponse({"id": "photo-42"}),
            FakeResponse(
                {"error": {"code": 100, "message": "invalid time"}},
                ok=False,
                status_code=400,
            ),
        ]
    )
    publisher = FacebookPublisher(
        page_id="page",
        access_token="token",
        api_version="v26.0",
        session=session,
    )

    with pytest.raises(FacebookError) as error:
        publisher.schedule_photo(
            image,
            "Bonjour",
            datetime(2026, 10, 19, 7, 15, tzinfo=ZoneInfo("Europe/Paris")),
        )

    assert not isinstance(error.value, FacebookSchedulingUncertain)


def test_destination_is_locked_to_expected_page_name() -> None:
    session = FakeSession(FakeResponse({"id": "1", "name": "Une autre page"}))
    publisher = FacebookPublisher(
        page_id="1",
        access_token="token",
        api_version="v24.0",
        session=session,
    )

    with pytest.raises(FacebookError, match="Madame Portugais"):
        publisher.verify_destination("Madame Portugais")


def test_destination_name_comparison_ignores_case_and_extra_spaces() -> None:
    session = FakeSession(FakeResponse({"id": "1", "name": "Madame   Portugais"}))
    publisher = FacebookPublisher(
        page_id="1",
        access_token="token",
        api_version="v24.0",
        session=session,
    )

    page = publisher.verify_destination("madame portugais")

    assert page.name == "Madame   Portugais"


def test_permission_error_keeps_the_exact_meta_explanation() -> None:
    session = FakeSession(
        FakeResponse(
            {
                "error": {
                    "message": "Requires pages_manage_posts or CREATE_CONTENT",
                    "code": 200,
                }
            },
            ok=False,
            status_code=403,
        )
    )
    publisher = FacebookPublisher(
        page_id="1",
        access_token="token",
        api_version="v26.0",
        session=session,
    )

    with pytest.raises(FacebookError) as caught:
        publisher.get_page_info()

    assert "Détail Meta" in str(caught.value)
    assert "Requires pages_manage_posts or CREATE_CONTENT" in str(caught.value)


def test_token_error_has_actionable_message() -> None:
    session = FakeSession(
        FakeResponse(
            {"error": {"message": "Invalid OAuth", "code": 190}},
            ok=False,
            status_code=400,
        )
    )
    publisher = FacebookPublisher(
        page_id="1",
        access_token="expired",
        api_version="v24.0",
        session=session,
    )

    with pytest.raises(FacebookError, match="expiré") as caught:
        publisher.get_page_info()

    assert not caught.value.retryable
