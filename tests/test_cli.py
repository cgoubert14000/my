from datetime import datetime, timedelta
from types import SimpleNamespace
from zoneinfo import ZoneInfo

import pytest

from facebook_bot import cli
from facebook_bot.config import Config, ConfigError
from facebook_bot.facebook import PublishReceipt
from facebook_bot.state import StateStore


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


def test_setup_reads_token_file_then_removes_secret_from_it(
    tmp_path, monkeypatch, capsys
) -> None:
    token = "EAA" + "z" * 80
    token_file = tmp_path / "token madame portugais.txt"
    token_file.write_text(token, encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(cli, "FacebookPublisher", FakePublisher)

    result = cli._setup(tmp_path / ".env", token_file=token_file)

    assert result == 0
    assert token in (tmp_path / ".env").read_text()
    assert token not in token_file.read_text()
    assert "COLLEZ_VOTRE_NOUVEAU_JETON_ICI" in token_file.read_text()
    assert token not in capsys.readouterr().out


def test_token_template_is_not_accepted_as_a_token(tmp_path) -> None:
    path = tmp_path / "token madame portugais.txt"
    path.write_text(cli.TOKEN_FILE_TEMPLATE, encoding="utf-8")

    with pytest.raises(ConfigError, match="Aucun jeton valide"):
        cli._read_token_file(path)


def test_setup_never_writes_secret_to_example_file(tmp_path) -> None:
    with pytest.raises(ConfigError, match=".env.example"):
        cli._setup(tmp_path / ".env.example")


def test_send_schedule_confirms_that_pc_can_be_turned_off(monkeypatch, capsys) -> None:
    result = SimpleNamespace(scheduled=12, pending=0, uncertain=0, succeeded=True)
    runner = SimpleNamespace(schedule_pending_on_facebook=lambda day=None: result)
    monkeypatch.setattr(cli, "BotRunner", lambda _config: runner)

    exit_code = cli._send_pending_schedule(SimpleNamespace(), expected_count=12)

    assert exit_code == 0
    output = capsys.readouterr().out
    assert "Facebook a accepté 12" in output
    assert "éteindre le PC" in output


def test_send_schedule_reports_pending_and_uncertain_items(monkeypatch, capsys) -> None:
    result = SimpleNamespace(scheduled=2, pending=3, uncertain=1, succeeded=False)
    runner = SimpleNamespace(schedule_pending_on_facebook=lambda day=None: result)
    monkeypatch.setattr(cli, "BotRunner", lambda _config: runner)

    exit_code = cli._send_pending_schedule(SimpleNamespace())

    assert exit_code == 1
    output = capsys.readouterr().out
    assert "ARRÊT DE SÉCURITÉ" in output
    assert "3 publication(s) restent" in output


def test_plan_immediately_hands_saved_plan_to_facebook_sender(tmp_path, monkeypatch) -> None:
    timezone = ZoneInfo("Europe/Paris")
    image_dir = tmp_path / "images" / "to_post"
    image_dir.mkdir(parents=True)
    (image_dir / "photo.jpg").write_bytes(b"photo")
    (tmp_path / "horraire1.txt").write_text("07h30\n", encoding="utf-8")
    (tmp_path / "horraire2.txt").write_text("07h15\n", encoding="utf-8")
    (tmp_path / "horraire3.txt").write_text("07h45\n", encoding="utf-8")
    (tmp_path / "hashtags.txt").write_text("#portugal", encoding="utf-8")
    config = Config(
        page_id="1098568206676051",
        page_access_token="token",
        expected_page_name="Madame Portugais",
        api_version="v26.0",
        timezone=timezone,
        timezone_name="Europe/Paris",
        image_dir=image_dir,
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
    calls = []

    def fake_send(config_arg, *, day=None, expected_count=None):
        calls.append((config_arg, day, expected_count))
        return 0

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(cli, "_send_pending_schedule", fake_send)
    future_day = datetime.now(timezone).date() + timedelta(days=2)

    exit_code = cli._plan_publications(
        config,
        future_day.strftime("%d/%m/%Y"),
        schedule_choice="1",
        assume_yes=True,
    )

    assert exit_code == 0
    assert calls == [(config, future_day, 1)]

    answers = iter(["o", "o"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))
    replacement_exit_code = cli._plan_publications(
        config,
        future_day.strftime("%d/%m/%Y"),
        schedule_choice="1",
        assume_yes=False,
    )

    assert replacement_exit_code == 0
    assert calls == [(config, future_day, 1), (config, future_day, 1)]
    store = StateStore(config.state_db)
    assert len(store.scheduled_for_day(future_day)) == 1

    first_publication = store.pending_publications(future_day)[0]
    assert store.claim_for_facebook_scheduling(first_publication)
    store.record_facebook_scheduled(
        first_publication,
        PublishReceipt(photo_id="media-1", post_id="post-1"),
    )
    (image_dir / "photo-2.jpg").write_bytes(b"second photo")

    append_exit_code = cli._plan_publications(
        config,
        future_day.strftime("%d/%m/%Y"),
        schedule_choice="2",
        assume_yes=True,
    )

    assert append_exit_code == 0
    assert calls == [
        (config, future_day, 1),
        (config, future_day, 1),
        (config, future_day, 1),
    ]
    saved = store.scheduled_for_day(future_day)
    assert len(saved) == 2
    assert {publication.window_index for publication in saved} == {1, 2}
