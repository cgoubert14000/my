from __future__ import annotations

import random
import sqlite3
from collections.abc import Iterator, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from facebook_bot.config import PostingWindow
from facebook_bot.facebook import PublishReceipt
from facebook_bot.images import ImageItem

UTC = timezone.utc


@dataclass(frozen=True)
class Slot:
    day: date
    index: int
    window_start: datetime
    window_end: datetime
    scheduled_at: datetime
    status: str
    attempts: int
    last_error: str | None = None


class StateStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def initialize(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS daily_slots (
                    day TEXT NOT NULL,
                    slot_index INTEGER NOT NULL,
                    window_start TEXT NOT NULL,
                    window_end TEXT NOT NULL,
                    scheduled_at TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'pending',
                    attempts INTEGER NOT NULL DEFAULT 0,
                    last_error TEXT,
                    image_fingerprint TEXT,
                    facebook_photo_id TEXT,
                    updated_at TEXT NOT NULL,
                    PRIMARY KEY (day, slot_index)
                );

                CREATE TABLE IF NOT EXISTS posted_images (
                    fingerprint TEXT PRIMARY KEY,
                    original_path TEXT NOT NULL,
                    archived_path TEXT,
                    caption TEXT NOT NULL,
                    facebook_photo_id TEXT NOT NULL,
                    facebook_post_id TEXT,
                    posted_at TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_daily_slots_status_time
                    ON daily_slots(status, scheduled_at);
                """
            )

    def ensure_day(
        self,
        day: date,
        windows: Sequence[PostingWindow],
        timezone_info: ZoneInfo,
        *,
        now: datetime,
        rng: random.Random | random.SystemRandom | None = None,
    ) -> list[Slot]:
        generator = rng or random.SystemRandom()
        now = now.astimezone(timezone_info)
        with self._connect() as connection:
            existing = {
                row[0]
                for row in connection.execute(
                    "SELECT slot_index FROM daily_slots WHERE day = ?", (day.isoformat(),)
                )
            }
            for index, window in enumerate(windows, start=1):
                if index in existing:
                    continue
                window_start, window_end = window.bounds(day, timezone_info)
                earliest = window_start
                status = "pending"
                if now.date() == day and now > earliest:
                    earliest = now + timedelta(seconds=2)
                if now > window_end or earliest >= window_end:
                    scheduled_at = window_end
                    status = "missed"
                else:
                    available_seconds = max(0, int((window_end - earliest).total_seconds()))
                    offset = generator.randint(0, available_seconds)
                    scheduled_at = earliest + timedelta(seconds=offset)
                connection.execute(
                    """
                    INSERT OR IGNORE INTO daily_slots (
                        day, slot_index, window_start, window_end, scheduled_at,
                        status, attempts, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, 0, ?)
                    """,
                    (
                        day.isoformat(),
                        index,
                        window_start.isoformat(),
                        window_end.isoformat(),
                        scheduled_at.isoformat(),
                        status,
                        _utc_now_iso(),
                    ),
                )
        return self.slots_for_day(day)

    def slots_for_day(self, day: date) -> list[Slot]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT day, slot_index, window_start, window_end, scheduled_at,
                       status, attempts, last_error
                FROM daily_slots
                WHERE day = ?
                ORDER BY slot_index
                """,
                (day.isoformat(),),
            ).fetchall()
        return [_slot_from_row(row) for row in rows]

    def expire_pending(self, now: datetime) -> int:
        expired: list[tuple[str, int]] = []
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT day, slot_index, window_end FROM daily_slots WHERE status = 'pending'"
            ).fetchall()
            for row in rows:
                if datetime.fromisoformat(row[2]) < now:
                    expired.append((row[0], row[1]))
            connection.executemany(
                """
                UPDATE daily_slots
                SET status = 'missed', last_error = 'Plage horaire dépassée', updated_at = ?
                WHERE day = ? AND slot_index = ? AND status = 'pending'
                """,
                [(_utc_now_iso(), day, index) for day, index in expired],
            )
        return len(expired)

    def claim_due_slot(self, now: datetime) -> Slot | None:
        with self._transaction() as connection:
            rows = connection.execute(
                """
                SELECT day, slot_index, window_start, window_end, scheduled_at,
                       status, attempts, last_error
                FROM daily_slots
                WHERE status = 'pending'
                ORDER BY scheduled_at
                """
            ).fetchall()
            due = next(
                (
                    row
                    for row in rows
                    if datetime.fromisoformat(row[4]) <= now
                    and datetime.fromisoformat(row[3]) >= now
                ),
                None,
            )
            if due is None:
                return None
            changed = connection.execute(
                """
                UPDATE daily_slots
                SET status = 'running', updated_at = ?
                WHERE day = ? AND slot_index = ? AND status = 'pending'
                """,
                (_utc_now_iso(), due[0], due[1]),
            ).rowcount
            if changed != 1:
                return None
            claimed = list(due)
            claimed[5] = "running"
            return _slot_from_row(claimed)

    def mark_post_attempt(self, slot: Slot) -> int:
        with self._connect() as connection:
            connection.execute(
                """
                UPDATE daily_slots SET attempts = attempts + 1, updated_at = ?
                WHERE day = ? AND slot_index = ? AND status = 'running'
                """,
                (_utc_now_iso(), slot.day.isoformat(), slot.index),
            )
            row = connection.execute(
                "SELECT attempts FROM daily_slots WHERE day = ? AND slot_index = ?",
                (slot.day.isoformat(), slot.index),
            ).fetchone()
        return int(row[0]) if row else slot.attempts + 1

    def reschedule(self, slot: Slot, scheduled_at: datetime, error: str | None = None) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                UPDATE daily_slots
                SET status = 'pending', scheduled_at = ?, last_error = ?, updated_at = ?
                WHERE day = ? AND slot_index = ? AND status = 'running'
                """,
                (
                    scheduled_at.isoformat(),
                    error,
                    _utc_now_iso(),
                    slot.day.isoformat(),
                    slot.index,
                ),
            )

    def finish_slot(self, slot: Slot, status: str, error: str | None = None) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                UPDATE daily_slots
                SET status = ?, last_error = ?, updated_at = ?
                WHERE day = ? AND slot_index = ?
                """,
                (status, error, _utc_now_iso(), slot.day.isoformat(), slot.index),
            )

    def record_slot_success(
        self,
        slot: Slot,
        item: ImageItem,
        receipt: PublishReceipt,
        posted_at: datetime,
    ) -> None:
        with self._transaction() as connection:
            self._insert_posted(connection, item, receipt, posted_at)
            connection.execute(
                """
                UPDATE daily_slots
                SET status = 'completed', image_fingerprint = ?, facebook_photo_id = ?,
                    last_error = NULL, updated_at = ?
                WHERE day = ? AND slot_index = ?
                """,
                (
                    item.fingerprint,
                    receipt.photo_id,
                    _utc_now_iso(),
                    slot.day.isoformat(),
                    slot.index,
                ),
            )

    def record_manual_success(
        self, item: ImageItem, receipt: PublishReceipt, posted_at: datetime
    ) -> None:
        with self._transaction() as connection:
            self._insert_posted(connection, item, receipt, posted_at)

    def update_archive_path(self, fingerprint: str, archived_path: Path) -> None:
        with self._connect() as connection:
            connection.execute(
                "UPDATE posted_images SET archived_path = ? WHERE fingerprint = ?",
                (str(archived_path), fingerprint),
            )

    def was_posted(self, fingerprint: str) -> bool:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT 1 FROM posted_images WHERE fingerprint = ?", (fingerprint,)
            ).fetchone()
        return row is not None

    def recover_stale_running(self, *, older_than: timedelta = timedelta(minutes=15)) -> int:
        threshold = datetime.now(UTC) - older_than
        recovered: list[tuple[str, int]] = []
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT day, slot_index, updated_at FROM daily_slots WHERE status = 'running'"
            ).fetchall()
            for day, index, updated_at in rows:
                if datetime.fromisoformat(updated_at) < threshold:
                    recovered.append((day, index))
            error = "Arrêt pendant une publication ; non retentée pour éviter un doublon"
            connection.executemany(
                """
                UPDATE daily_slots
                SET status = 'uncertain', last_error = ?, updated_at = ?
                WHERE day = ? AND slot_index = ? AND status = 'running'
                """,
                [(error, _utc_now_iso(), day, index) for day, index in recovered],
            )
        return len(recovered)

    @staticmethod
    def _insert_posted(
        connection: sqlite3.Connection,
        item: ImageItem,
        receipt: PublishReceipt,
        posted_at: datetime,
    ) -> None:
        connection.execute(
            """
            INSERT INTO posted_images (
                fingerprint, original_path, archived_path, caption,
                facebook_photo_id, facebook_post_id, posted_at
            ) VALUES (?, ?, NULL, ?, ?, ?, ?)
            """,
            (
                item.fingerprint,
                str(item.path),
                item.caption,
                receipt.photo_id,
                receipt.post_id,
                posted_at.isoformat(),
            ),
        )

    @contextmanager
    def _connect(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.path, timeout=10)
        try:
            connection.execute("PRAGMA journal_mode=WAL")
            connection.execute("PRAGMA busy_timeout=10000")
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    @contextmanager
    def _transaction(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.path, timeout=10, isolation_level=None)
        try:
            connection.execute("PRAGMA busy_timeout=10000")
            connection.execute("BEGIN IMMEDIATE")
            yield connection
            connection.execute("COMMIT")
        except Exception:
            connection.execute("ROLLBACK")
            raise
        finally:
            connection.close()


def _slot_from_row(row: Sequence[object]) -> Slot:
    return Slot(
        day=date.fromisoformat(str(row[0])),
        index=int(row[1]),
        window_start=datetime.fromisoformat(str(row[2])),
        window_end=datetime.fromisoformat(str(row[3])),
        scheduled_at=datetime.fromisoformat(str(row[4])),
        status=str(row[5]),
        attempts=int(row[6]),
        last_error=str(row[7]) if row[7] is not None else None,
    )


def _utc_now_iso() -> str:
    return datetime.now(UTC).isoformat()
