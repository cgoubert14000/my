from pathlib import Path

import pytest

from facebook_bot.facebook import FacebookError, FacebookPublisher


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
        self.response = response
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append((method, url, kwargs))
        return self.response


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
