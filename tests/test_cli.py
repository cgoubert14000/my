from types import SimpleNamespace

import pytest

from facebook_bot import cli
from facebook_bot.config import ConfigError


class FakePublisher:
    def __init__(self, **_kwargs):
        pass

    def verify_destination(self, expected_page_name):
        assert expected_page_name == "Madame Portugais"
        return SimpleNamespace(name="Madame Portugais", id="1098568206676051")


def test_setup_verifies_and_saves_token_without_printing_it(tmp_path, monkeypatch, capsys) -> None:
    token = "EAA" + "x" * 80
    template = tmp_path / ".env.example"
    template.write_text("POSTING_WINDOWS=07:00-10:00,12:00-15:00,18:00-22:00\n")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(cli.getpass, "getpass", lambda _prompt: token)
    monkeypatch.setattr(cli, "FacebookPublisher", FakePublisher)

    result = cli._setup(tmp_path / ".env")

    assert result == 0
    content = (tmp_path / ".env").read_text()
    assert f"FACEBOOK_PAGE_ACCESS_TOKEN='{token}'" in content
    assert "FACEBOOK_PAGE_ID=1098568206676051" in content
    assert token not in capsys.readouterr().out


def test_setup_can_read_and_clear_clipboard(tmp_path, monkeypatch, capsys) -> None:
    token = "EAA" + "y" * 80
    clipboard_was_cleared = []
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(cli, "_read_clipboard_token", lambda: token)
    monkeypatch.setattr(cli, "_clear_clipboard", lambda: clipboard_was_cleared.append(True))
    monkeypatch.setattr(cli, "FacebookPublisher", FakePublisher)

    result = cli._setup(tmp_path / ".env", from_clipboard=True)

    assert result == 0
    assert clipboard_was_cleared == [True]
    assert token in (tmp_path / ".env").read_text()
    assert token not in capsys.readouterr().out


def test_setup_never_writes_secret_to_example_file(tmp_path) -> None:
    with pytest.raises(ConfigError, match=".env.example"):
        cli._setup(tmp_path / ".env.example")
