from datetime import time

import pytest

from facebook_bot.config import ConfigError, parse_posting_windows


def test_parse_exactly_three_sorted_windows() -> None:
    windows = parse_posting_windows("18:00-22:00,07:00-10:00,12:00-15:00")

    assert [window.start for window in windows] == [time(7), time(12), time(18)]
    assert str(windows[0]) == "07:00-10:00"


@pytest.mark.parametrize(
    "value",
    [
        "07:00-10:00,12:00-15:00",
        "07:00-10:00,09:00-11:00,18:00-20:00",
        "7:00-10:00,12:00-15:00,18:00-20:00",
        "10:00-07:00,12:00-15:00,18:00-20:00",
    ],
)
def test_reject_invalid_windows(value: str) -> None:
    with pytest.raises(ConfigError):
        parse_posting_windows(value)
