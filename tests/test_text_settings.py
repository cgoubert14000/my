from datetime import time

import pytest

from facebook_bot.config import ConfigError
from facebook_bot.text_settings import load_hashtags, load_schedule_definitions


def _write_default_schedules(tmp_path) -> None:
    (tmp_path / "horraire1.txt").write_text("- **7h30**\n8h30\n09:30\n", encoding="utf-8")
    (tmp_path / "horraire2.txt").write_text("07h15\n08h15\n09h15\n", encoding="utf-8")
    (tmp_path / "horraire3.txt").write_text("07h45\n08h45\n09h45\n", encoding="utf-8")
    (tmp_path / "horraire4.txt").write_text("07h00\n08h00\n09h00\n", encoding="utf-8")


def test_loads_markdown_or_plain_text_times(tmp_path) -> None:
    _write_default_schedules(tmp_path)

    definitions = load_schedule_definitions(tmp_path)

    assert definitions[0].times == (time(7, 30), time(8, 30), time(9, 30))
    assert definitions[1].first == time(7, 15)
    assert definitions[2].last == time(9, 45)
    assert definitions[3].times == (time(7, 0), time(8, 0), time(9, 0))


def test_rejects_same_time_in_two_schedule_files(tmp_path) -> None:
    _write_default_schedules(tmp_path)
    (tmp_path / "horraire3.txt").write_text("07h15\n", encoding="utf-8")

    with pytest.raises(ConfigError, match="apparaît"):
        load_schedule_definitions(tmp_path)


def test_hashtags_file_is_normalized_and_deduplicated(tmp_path) -> None:
    (tmp_path / "hashtags.txt").write_text(
        "portugal #portugais, portugal #quiz", encoding="utf-8"
    )

    assert load_hashtags(tmp_path) == "#portugal #portugais #quiz"
