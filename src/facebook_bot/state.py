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
from facebook_bot.planner import PlannedPost

UTC = timezone.utc
_SCHEDULED_COLUMNS = """
    id, day, window_index, scheduled_at, window_end,
    image_path, caption_path, caption, fingerprint,
    status, attempts, last_error
"""


class StateError(RuntimeError):
    """Opération impossible sur le planning local."""


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


@dataclass(frozen=True)
class ScheduledPost:
    id: int
    day: date
    window_index: int
    scheduled_at: datetime
    window_end: datetime
    status: str
    attempts: int
    item: ImageItem
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

                CREATE TABLE IF NOT EXISTS scheduled_publications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    day TEXT NOT NULL,
                    window_index INTEGER NOT NULL,
                    scheduled_at TEXT NOT NULL,
                    window_end TEXT NOT NULL,
                    image_path TEXT NOT NULL,
                    caption_path TEXT,
                    caption TEXT NOT NULL,
                    fingerprint TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'pending',
                    attempts INTEGER NOT NULL DEFAULT 0,
                    last_error TEXT,
                    facebook_photo_id TEXT,
                    updated_at TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_scheduled_publications_status_time
                    ON scheduled_publications(status, scheduled_at);
                CREATE INDEX IF NOT EXISTS idx_scheduled_publications_fingerprint
                    ON scheduled_publications(fingerprint, status);
                """
            )

    def create_plan(
        self,
        day: date,
        entries: Sequence[PlannedPost],
        *,
        replace: bool = False,
        append: bool = False,
    ) -> None:
        if replace and append:
            raise StateError("Un planning ne peut pas être remplacé et complété simultanément.")

        with self._transaction() as connection:
            existing = connection.execute(
                "SELECT status, scheduled_at FROM scheduled_publications WHERE day = ?",
                (day.isoformat(),),
            ).fetchall()
            if existing and not replace and not append:
                raise StateError(
                    f"Un planning existe déjà pour le {day.strftime('%d/%m/%Y')}."
                )
            if existing and replace:
                protected = {
                    "running",
                    "scheduling",
                    "completed",
                    "facebook_scheduled",
                    "uncertain",
                }
                if any(str(row[0]) in protected for row in existing):
                    raise StateError(
                        "Ce planning contient une publication en cours, publiée ou à vérifier ; "
                        "il ne peut plus être remplacé."
                    )
                connection.execute(
                    "DELETE FROM scheduled_publications WHERE day = ?",
                    (day.isoformat(),),
                )
                existing = []

            occupied_times = {str(row[1]) for row in existing}
            for entry in entries:
                scheduled_at = entry.scheduled_at.isoformat()
                if scheduled_at in occupied_times:
                    raise StateError(
                        f"Une publication existe déjà le {day:%d/%m/%Y} à "
                        f"{entry.scheduled_at:%H:%M}."
                    )
                if self._fingerprint_unavailable(connection, entry.item.fingerprint):
                    raise StateError(
                        f"L'image {entry.item.path.name} est déjà publiée ou planifiée."
                    )
                connection.execute(
                    """
                    INSERT INTO scheduled_publications (
                        day, window_index, scheduled_at, window_end,
                        image_path, caption_path, caption, fingerprint,
                        status, attempts, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'pending', 0, ?)
                    """,
                    (
                        day.isoformat(),
                        entry.window_index,
                        entry.scheduled_at.isoformat(),
                        entry.window_end.isoformat(),
                        str(entry.item.path),
                        str(entry.item.caption_path) if entry.item.caption_path else None,
                        entry.item.caption,
                        entry.item.fingerprint,
                        _utc_now_iso(),
                    ),
                )
                occupied_times.add(scheduled_at)

    def scheduled_for_day(self, day: date) -> list[ScheduledPost]:
        with self._connect() as connection:
            rows = connection.execute(
                f"""
                SELECT {_SCHEDULED_COLUMNS}
                FROM scheduled_publications
                WHERE day = ?
                ORDER BY scheduled_at
                """,
                (day.isoformat(),),
            ).fetchall()
        return [_scheduled_from_row(row) for row in rows]

    def next_pending_publication(self) -> ScheduledPost | None:
        with self._connect() as connection:
            row = connection.execute(
                f"""
                SELECT {_SCHEDULED_COLUMNS}
                FROM scheduled_publications
                WHERE status = 'pending'
                ORDER BY scheduled_at
                LIMIT 1
                """
            ).fetchone()
        return _scheduled_from_row(row) if row is not None else None

    def pending_publications(self, day: date | None = None) -> list[ScheduledPost]:
        with self._connect() as connection:
            if day is None:
                rows = connection.execute(
                    f"""
                    SELECT {_SCHEDULED_COLUMNS}
                    FROM scheduled_publications
                    WHERE status = 'pending'
                    ORDER BY scheduled_at
                    """
                ).fetchall()
            else:
                rows = connection.execute(
                    f"""
                    SELECT {_SCHEDULED_COLUMNS}
                    FROM scheduled_publications
                    WHERE status = 'pending' AND day = ?
                    ORDER BY scheduled_at
                    """,
                    (day.isoformat(),),
                ).fetchall()
        return [_scheduled_from_row(row) for row in rows]

    def publication_status_counts(self, day: date | None = None) -> dict[str, int]:
        with self._connect() as connection:
            if day is None:
                rows = connection.execute(
                    "SELECT status, COUNT(*) FROM scheduled_publications GROUP BY status"
                ).fetchall()
            else:
                rows = connection.execute(
                    """
                    SELECT status, COUNT(*) FROM scheduled_publications
                    WHERE day = ? GROUP BY status
                    """,
                    (day.isoformat(),),
                ).fetchall()
        return {str(status): int(count) for status, count in rows}

    def claim_for_facebook_scheduling(self, publication: ScheduledPost) -> bool:
        with self._connect() as connection:
            changed = connection.execute(
                """
                UPDATE scheduled_publications
                SET status = 'scheduling', updated_at = ?
                WHERE id = ? AND status = 'pending'
                """,
                (_utc_now_iso(), publication.id),
            ).rowcount
        return changed == 1

    def release_facebook_scheduling(
        self,
        publication: ScheduledPost,
        *,
        status: str,
        error: str,
        photo_id: str | None = None,
    ) -> None:
        if status not in {"pending", "failed", "uncertain"}:
            raise StateError(f"Statut de programmation Facebook invalide : {status}")
        with self._connect() as connection:
            connection.execute(
                """
                UPDATE scheduled_publications
                SET status = ?, last_error = ?, facebook_photo_id = ?, updated_at = ?
                WHERE id = ? AND status = 'scheduling'
                """,
                (status, error, photo_id, _utc_now_iso(), publication.id),
            )

    def record_facebook_scheduled(
        self,
        publication: ScheduledPost,
        receipt: PublishReceipt,
    ) -> None:
        with self._transaction() as connection:
            changed = connection.execute(
                """
                UPDATE scheduled_publications
                SET status = 'facebook_scheduled', facebook_photo_id = ?,
                    last_error = NULL, updated_at = ?
                WHERE id = ? AND status = 'scheduling'
                """,
                (receipt.photo_id, _utc_now_iso(), publication.id),
            ).rowcount
            if changed != 1:
                raise StateError(
                    "L'état local a changé pendant la programmation Facebook ; "
                    "vérification manuelle requise."
                )
            self._insert_posted(
                connection,
                publication.item,
                receipt,
                publication.scheduled_at,
            )

    def is_unavailable(self, fingerprint: str) -> bool:
        with self._connect() as connection:
            return self._fingerprint_unavailable(connection, fingerprint)

    def is_unavailable_except_day(self, fingerprint: str, day: date) -> bool:
        """Ignore les réservations du jour remplacé, mais aucune autre réservation."""
        with self._connect() as connection:
            posted = connection.execute(
                "SELECT 1 FROM posted_images WHERE fingerprint = ?",
                (fingerprint,),
            ).fetchone()
            if posted is not None:
                return True
            scheduled = connection.execute(
                """
                SELECT 1 FROM scheduled_publications
                WHERE fingerprint = ? AND day <> ?
                  AND status IN (
                      'pending', 'running', 'scheduling', 'completed',
                      'facebook_scheduled', 'uncertain'
                  )
                """,
                (fingerprint, day.isoformat()),
            ).fetchone()
            return scheduled is not None

    def expire_scheduled(self, now: datetime, *, max_late: timedelta) -> int:
        expired_ids: list[int] = []
        threshold = now - max_late
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT id, scheduled_at, window_end
                FROM scheduled_publications
                WHERE status = 'pending'
                """
            ).fetchall()
            for row in rows:
                scheduled_at = datetime.fromisoformat(str(row[1]))
                window_end = datetime.fromisoformat(str(row[2]))
                if scheduled_at < threshold or window_end < now:
                    expired_ids.append(int(row[0]))
            connection.executemany(
                """
                UPDATE scheduled_publications
                SET status = 'missed', last_error = 'Heure dépassée', updated_at = ?
                WHERE id = ? AND status = 'pending'
                """,
                [(_utc_now_iso(), publication_id) for publication_id in expired_ids],
            )
        return len(expired_ids)

    def claim_due_publication(self, now: datetime) -> ScheduledPost | None:
        with self._transaction() as connection:
            rows = connection.execute(
                f"""
                SELECT {_SCHEDULED_COLUMNS}
                FROM scheduled_publications
                WHERE status = 'pending'
                ORDER BY scheduled_at
                """
            ).fetchall()
            due = next(
                (
                    row
                    for row in rows
                    if datetime.fromisoformat(str(row[3])) <= now
                    and datetime.fromisoformat(str(row[4])) >= now
                ),
                None,
            )
            if due is None:
                return None
            publication_id = int(due[0])
            changed = connection.execute(
                """
                UPDATE scheduled_publications
                SET status = 'running', updated_at = ?
                WHERE id = ? AND status = 'pending'
                """,
                (_utc_now_iso(), publication_id),
            ).rowcount
            if changed != 1:
                return None
            claimed = list(due)
            claimed[9] = "running"
            return _scheduled_from_row(claimed)

    def mark_scheduled_attempt(self, publication: ScheduledPost) -> int:
        with self._connect() as connection:
            connection.execute(
                """
                UPDATE scheduled_publications
                SET attempts = attempts + 1, updated_at = ?
                WHERE id = ? AND status = 'running'
                """,
                (_utc_now_iso(), publication.id),
            )
            row = connection.execute(
                "SELECT attempts FROM scheduled_publications WHERE id = ?",
                (publication.id,),
            ).fetchone()
        return int(row[0]) if row else publication.attempts + 1

    def reschedule_publication(
        self,
        publication: ScheduledPost,
        scheduled_at: datetime,
        error: str | None = None,
    ) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                UPDATE scheduled_publications
                SET status = 'pending', scheduled_at = ?, last_error = ?, updated_at = ?
                WHERE id = ? AND status = 'running'
                """,
                (scheduled_at.isoformat(), error, _utc_now_iso(), publication.id),
            )

    def finish_publication(
        self,
        publication: ScheduledPost,
        status: str,
        error: str | None = None,
    ) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                UPDATE scheduled_publications
                SET status = ?, last_error = ?, updated_at = ?
                WHERE id = ?
                """,
                (status, error, _utc_now_iso(), publication.id),
            )

    def record_scheduled_success(
        self,
        publication: ScheduledPost,
        receipt: PublishReceipt,
        posted_at: datetime,
    ) -> None:
        with self._transaction() as connection:
            self._insert_posted(connection, publication.item, receipt, posted_at)
            connection.execute(
                """
                UPDATE scheduled_publications
                SET status = 'completed', facebook_photo_id = ?,
                    last_error = NULL, updated_at = ?
                WHERE id = ?
                """,
                (receipt.photo_id, _utc_now_iso(), publication.id),
            )

    @staticmethod
    def _fingerprint_unavailable(
        connection: sqlite3.Connection,
        fingerprint: str,
    ) -> bool:
        posted = connection.execute(
            "SELECT 1 FROM posted_images WHERE fingerprint = ?",
            (fingerprint,),
        ).fetchone()
        if posted is not None:
            return True
        scheduled = connection.execute(
            """
            SELECT 1 FROM scheduled_publications
            WHERE fingerprint = ?
              AND status IN (
                  'pending', 'running', 'scheduling', 'completed',
                  'facebook_scheduled', 'uncertain'
              )
            """,
            (fingerprint,),
        ).fetchone()
        return scheduled is not None

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
        recovered_legacy: list[tuple[str, int]] = []
        recovered_scheduled: list[int] = []
        with self._connect() as connection:
            legacy_rows = connection.execute(
                "SELECT day, slot_index, updated_at FROM daily_slots WHERE status = 'running'"
            ).fetchall()
            for day, index, updated_at in legacy_rows:
                if datetime.fromisoformat(updated_at) < threshold:
                    recovered_legacy.append((day, index))

            scheduled_rows = connection.execute(
                """
                SELECT id, updated_at FROM scheduled_publications
                WHERE status IN ('running', 'scheduling')
                """
            ).fetchall()
            for publication_id, updated_at in scheduled_rows:
                if datetime.fromisoformat(updated_at) < threshold:
                    recovered_scheduled.append(int(publication_id))

            error = "Arrêt pendant un envoi Facebook ; non retenté pour éviter un doublon"
            connection.executemany(
                """
                UPDATE daily_slots
                SET status = 'uncertain', last_error = ?, updated_at = ?
                WHERE day = ? AND slot_index = ? AND status = 'running'
                """,
                [
                    (error, _utc_now_iso(), day, index)
                    for day, index in recovered_legacy
                ],
            )
            connection.executemany(
                """
                UPDATE scheduled_publications
                SET status = 'uncertain', last_error = ?, updated_at = ?
                WHERE id = ? AND status IN ('running', 'scheduling')
                """,
                [
                    (error, _utc_now_iso(), publication_id)
                    for publication_id in recovered_scheduled
                ],
            )
        return len(recovered_legacy) + len(recovered_scheduled)

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


def _scheduled_from_row(row: Sequence[object]) -> ScheduledPost:
    caption_path = Path(str(row[6])) if row[6] is not None else None
    return ScheduledPost(
        id=int(row[0]),
        day=date.fromisoformat(str(row[1])),
        window_index=int(row[2]),
        scheduled_at=datetime.fromisoformat(str(row[3])),
        window_end=datetime.fromisoformat(str(row[4])),
        status=str(row[9]),
        attempts=int(row[10]),
        item=ImageItem(
            path=Path(str(row[5])),
            caption_path=caption_path,
            caption=str(row[7]),
            fingerprint=str(row[8]),
        ),
        last_error=str(row[11]) if row[11] is not None else None,
    )


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
