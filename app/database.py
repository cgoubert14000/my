"""Persistance SQLite : profils, articles vus, vendeurs, logs, scans.

Une seule connexion par process, protégée par un verrou : suffisant pour un
dashboard local et un moteur qui écrivent en concurrence.
"""

from __future__ import annotations

import json
import sqlite3
import threading
from pathlib import Path
from collections.abc import Iterable
from typing import Any

from .utils import clean_terms, utcnow_iso

SCHEMA = """
CREATE TABLE IF NOT EXISTS profiles (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    name                    TEXT NOT NULL,
    active                  INTEGER NOT NULL DEFAULT 1,
    url                     TEXT NOT NULL DEFAULT '',
    min_price               REAL,
    max_price               REAL,
    whitelist               TEXT NOT NULL DEFAULT '[]',
    blacklist               TEXT NOT NULL DEFAULT '[]',
    keyword_mode            TEXT NOT NULL DEFAULT 'any',
    check_description       INTEGER NOT NULL DEFAULT 1,
    webhook                 TEXT NOT NULL DEFAULT '',
    interval_seconds        INTEGER NOT NULL DEFAULT 60,
    min_seller_rating       REAL,
    min_seller_feedback     INTEGER,
    pages                   INTEGER NOT NULL DEFAULT 1,
    notes                   TEXT NOT NULL DEFAULT '',
    baseline_done           INTEGER NOT NULL DEFAULT 0,
    created_at              TEXT NOT NULL,
    updated_at              TEXT NOT NULL,
    last_run_at             TEXT,
    last_error              TEXT,
    last_found_at           TEXT,
    scan_count              INTEGER NOT NULL DEFAULT 0,
    found_count             INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS seen_items (
    profile_id       INTEGER NOT NULL,
    item_id          TEXT NOT NULL,
    title            TEXT NOT NULL DEFAULT '',
    price            REAL,
    total_price      REAL,
    currency         TEXT NOT NULL DEFAULT 'EUR',
    brand            TEXT NOT NULL DEFAULT '',
    size             TEXT NOT NULL DEFAULT '',
    condition        TEXT NOT NULL DEFAULT '',
    url              TEXT NOT NULL DEFAULT '',
    image_url        TEXT NOT NULL DEFAULT '',
    seller_id        TEXT NOT NULL DEFAULT '',
    seller_name      TEXT NOT NULL DEFAULT '',
    seller_rating    REAL,
    seller_feedback  INTEGER,
    seller_url       TEXT NOT NULL DEFAULT '',
    favourites       INTEGER,
    found_at         TEXT NOT NULL,
    notified         INTEGER NOT NULL DEFAULT 0,
    notify_error     TEXT,
    raw              TEXT,
    PRIMARY KEY (profile_id, item_id),
    FOREIGN KEY (profile_id) REFERENCES profiles (id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_seen_item    ON seen_items (item_id);
CREATE INDEX IF NOT EXISTS idx_seen_found   ON seen_items (found_at DESC);
CREATE INDEX IF NOT EXISTS idx_seen_profile ON seen_items (profile_id, found_at DESC);

CREATE TABLE IF NOT EXISTS ignored_items (
    profile_id  INTEGER NOT NULL,
    item_id     TEXT NOT NULL,
    reason      TEXT,
    seen_at     TEXT NOT NULL,
    PRIMARY KEY (profile_id, item_id),
    FOREIGN KEY (profile_id) REFERENCES profiles (id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_ignored_profile ON ignored_items (profile_id, seen_at DESC);

CREATE TABLE IF NOT EXISTS seller_cache (
    key         TEXT PRIMARY KEY,
    seller_id   TEXT,
    name        TEXT,
    rating      REAL,
    feedback    INTEGER,
    url         TEXT,
    fetched_at  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS logs (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    ts          TEXT NOT NULL,
    level       TEXT NOT NULL DEFAULT 'INFO',
    source      TEXT NOT NULL DEFAULT 'engine',
    profile_id  INTEGER,
    message     TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_logs_ts ON logs (ts DESC);

CREATE TABLE IF NOT EXISTS scans (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id    INTEGER NOT NULL,
    started_at    TEXT NOT NULL,
    finished_at   TEXT,
    status        TEXT NOT NULL DEFAULT 'running',
    pages         INTEGER NOT NULL DEFAULT 0,
    items_seen    INTEGER NOT NULL DEFAULT 0,
    new_items     INTEGER NOT NULL DEFAULT 0,
    error         TEXT,
    duration_ms   INTEGER,
    FOREIGN KEY (profile_id) REFERENCES profiles (id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_scans_profile ON scans (profile_id, id DESC);

"""

PROFILE_FIELDS = (
    "name",
    "active",
    "url",
    "min_price",
    "max_price",
    "whitelist",
    "blacklist",
    "keyword_mode",
    "check_description",
    "webhook",
    "interval_seconds",
    "min_seller_rating",
    "min_seller_feedback",
    "pages",
    "notes",
)


class Database:
    def __init__(self, path: str | Path = "data/vinted_sniper.db"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._conn = sqlite3.connect(self.path, check_same_thread=False, timeout=30)
        self._conn.row_factory = sqlite3.Row
        with self._lock:
            self._conn.execute("PRAGMA journal_mode=WAL")
            self._conn.execute("PRAGMA synchronous=NORMAL")
            self._conn.execute("PRAGMA foreign_keys=ON")
            self._conn.execute("PRAGMA busy_timeout=15000")
            self._conn.executescript(SCHEMA)
            self._conn.commit()
            self._migrate()

    def _migrate(self) -> None:
        """Migrations légères pour les bases créées avant une mise à jour."""
        with self._lock:
            columns = {
                row["name"]
                for row in self._conn.execute("PRAGMA table_info(profiles)").fetchall()
            }
            if "baseline_done" not in columns:
                self._conn.execute(
                    "ALTER TABLE profiles ADD COLUMN baseline_done INTEGER NOT NULL DEFAULT 0"
                )
                self._conn.execute(
                    "UPDATE profiles SET baseline_done = 1 WHERE scan_count > 0"
                )
                self._conn.commit()

    # ── Helpers ──────────────────────────────────────────────────────────
    def close(self) -> None:
        with self._lock:
            self._conn.close()

    def _fetchall(self, sql: str, params: Iterable = ()) -> list[dict]:
        with self._lock:
            return [
                dict(row) for row in self._conn.execute(sql, tuple(params)).fetchall()
            ]

    def _fetchone(self, sql: str, params: Iterable = ()) -> dict | None:
        with self._lock:
            row = self._conn.execute(sql, tuple(params)).fetchone()
            return dict(row) if row else None

    def _execute(self, sql: str, params: Iterable = ()) -> int:
        with self._lock:
            cur = self._conn.execute(sql, tuple(params))
            self._conn.commit()
            return cur.lastrowid or 0

    def _execute_rowcount(self, sql: str, params: Iterable = ()) -> int:
        with self._lock:
            cur = self._conn.execute(sql, tuple(params))
            self._conn.commit()
            return cur.rowcount or 0

    # ── Profils ──────────────────────────────────────────────────────────
    @staticmethod
    def _profile_to_dict(row: dict) -> dict:
        row = dict(row)
        row["active"] = bool(row.get("active"))
        row["check_description"] = bool(row.get("check_description", 1))
        row["baseline_done"] = bool(row.get("baseline_done", 0))
        for key in ("whitelist", "blacklist"):
            try:
                row[key] = json.loads(row.get(key) or "[]")
            except json.JSONDecodeError:
                row[key] = []
        for key in (
            "min_price",
            "max_price",
            "min_seller_rating",
            "min_seller_feedback",
            "pages",
        ):
            if row.get(key) is not None:
                row[key] = (
                    float(row[key])
                    if key in {"min_price", "max_price", "min_seller_rating"}
                    else int(row[key])
                )
        return row

    def list_profiles(self, only_active: bool = False) -> list[dict]:
        sql = "SELECT * FROM profiles"
        if only_active:
            sql += " WHERE active = 1"
        sql += " ORDER BY id ASC"
        return [self._profile_to_dict(row) for row in self._fetchall(sql)]

    def get_profile(self, profile_id: int) -> dict | None:
        row = self._fetchone("SELECT * FROM profiles WHERE id = ?", (profile_id,))
        return self._profile_to_dict(row) if row else None

    @staticmethod
    def _encode(payload: dict) -> dict:
        defaults = {
            "name": "Profil",
            "active": 1,
            "url": "",
            "min_price": None,
            "max_price": None,
            "whitelist": [],
            "blacklist": [],
            "keyword_mode": "any",
            "check_description": 1,
            "webhook": "",
            "interval_seconds": 60,
            "min_seller_rating": None,
            "min_seller_feedback": None,
            "pages": 1,
            "notes": "",
        }
        data = {**defaults, **dict(payload)}
        for key in ("whitelist", "blacklist"):
            data[key] = json.dumps(clean_terms(data.get(key) or []), ensure_ascii=False)
        for key in ("active", "check_description"):
            data[key] = 1 if data.get(key) else 0
        return {key: data.get(key) for key in PROFILE_FIELDS}

    def create_profile(self, payload: dict) -> dict:
        now = utcnow_iso()
        data = self._encode(payload)
        data["created_at"] = now
        data["updated_at"] = now
        columns = ", ".join(data)
        marks = ", ".join("?" for _ in data)
        new_id = self._execute(
            f"INSERT INTO profiles ({columns}) VALUES ({marks})", list(data.values())
        )
        return self.get_profile(new_id)  # type: ignore[return-value]

    def update_profile(self, profile_id: int, payload: dict) -> dict | None:
        if not self.get_profile(profile_id):
            return None
        data = self._encode(payload)
        data["updated_at"] = utcnow_iso()
        assignments = ", ".join(f"{key} = ?" for key in data)
        self._execute(
            f"UPDATE profiles SET {assignments} WHERE id = ?",
            [*data.values(), profile_id],
        )
        return self.get_profile(profile_id)

    def set_active(self, profile_id: int, active: bool) -> dict | None:
        self._execute(
            "UPDATE profiles SET active = ?, updated_at = ? WHERE id = ?",
            (1 if active else 0, utcnow_iso(), profile_id),
        )
        return self.get_profile(profile_id)

    def duplicate_profile(self, profile_id: int) -> dict | None:
        source = self.get_profile(profile_id)
        if not source:
            return None
        payload = {key: source.get(key) for key in PROFILE_FIELDS}
        payload["name"] = f"{source['name']} (copie)"[:80]
        payload["active"] = False
        return self.create_profile(payload)

    def delete_profile(self, profile_id: int) -> bool:
        return (
            self._execute_rowcount("DELETE FROM profiles WHERE id = ?", (profile_id,))
            > 0
        )

    def mark_baseline_done(self, profile_id: int) -> None:
        self._execute(
            "UPDATE profiles SET baseline_done = 1 WHERE id = ?", (profile_id,)
        )

    def record_scan(
        self,
        profile_id: int,
        *,
        status: str,
        last_error: str | None,
        new_items: int,
        found: bool,
    ) -> None:
        self._execute(
            """
            UPDATE profiles
               SET last_run_at = ?, last_error = ?, scan_count = scan_count + 1,
                   found_count = found_count + ?, last_found_at = CASE WHEN ? = 1
                       THEN ? ELSE last_found_at END
             WHERE id = ?
            """,
            (
                utcnow_iso(),
                last_error,
                new_items,
                1 if found else 0,
                utcnow_iso(),
                profile_id,
            ),
        )

    # ── Articles vus ─────────────────────────────────────────────────────
    def is_seen(self, profile_id: int, item_id: str) -> bool:
        return (
            self._fetchone(
                "SELECT 1 AS x FROM seen_items WHERE profile_id = ? AND item_id = ?",
                (profile_id, str(item_id)),
            )
            is not None
        )

    def add_seen(self, profile_id: int, item: dict, raw: dict | None = None) -> bool:
        """Insère un article ; renvoie False s'il existait déjà (anti-doublon)."""
        try:
            self._execute(
                """
                INSERT INTO seen_items (profile_id, item_id, title, price, total_price,
                    currency, brand, size, condition, url, image_url, seller_id,
                    seller_name, seller_rating, seller_feedback, seller_url,
                    favourites, found_at, raw)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    profile_id,
                    str(item["id"]),
                    item.get("title", ""),
                    item.get("price"),
                    item.get("total_price"),
                    item.get("currency", "EUR"),
                    item.get("brand", ""),
                    item.get("size", ""),
                    item.get("condition", ""),
                    item.get("url", ""),
                    item.get("image_url", ""),
                    item.get("seller_id", ""),
                    item.get("seller_name", ""),
                    item.get("seller_rating"),
                    item.get("seller_feedback"),
                    item.get("seller_url", ""),
                    item.get("favourites"),
                    utcnow_iso(),
                    json.dumps(raw, ensure_ascii=False) if raw else None,
                ),
            )
            return True
        except sqlite3.IntegrityError:
            return False

    def mark_notified(
        self,
        profile_id: int,
        item_id: str,
        error: str | None = None,
        skipped: bool = False,
    ) -> None:
        """1 = alerte envoyée, 0 = échec, 2 = enregistrée sans alerte (baseline)."""
        status = 2 if skipped else (0 if error else 1)
        self._execute(
            "UPDATE seen_items SET notified = ?, notify_error = ? "
            "WHERE profile_id = ? AND item_id = ?",
            (status, error, profile_id, str(item_id)),
        )

    # ── Annonces écartées (mémoire négative) ─────────────────────────────
    def is_ignored(self, profile_id: int, item_id: str) -> bool:
        return (
            self._fetchone(
                "SELECT 1 AS x FROM ignored_items WHERE profile_id = ? AND item_id = ?",
                (profile_id, str(item_id)),
            )
            is not None
        )

    def add_ignored(self, profile_id: int, item_id: str, reason: str = "") -> None:
        try:
            self._execute(
                "INSERT INTO ignored_items (profile_id, item_id, reason, seen_at) "
                "VALUES (?,?,?,?)",
                (profile_id, str(item_id), reason[:200], utcnow_iso()),
            )
        except sqlite3.IntegrityError:
            pass

    def clear_ignored(self, profile_id: int | None = None) -> int:
        if profile_id:
            return self._execute_rowcount(
                "DELETE FROM ignored_items WHERE profile_id = ?", (profile_id,)
            )
        return self._execute_rowcount("DELETE FROM ignored_items")

    def recent_items(
        self, limit: int = 60, profile_id: int | None = None
    ) -> list[dict]:
        sql = """
            SELECT s.*, p.name AS profile_name
              FROM seen_items s
              JOIN profiles p ON p.id = s.profile_id
        """
        params: list[Any] = []
        if profile_id:
            sql += " WHERE s.profile_id = ?"
            params.append(profile_id)
        sql += " ORDER BY s.found_at DESC, s.rowid DESC LIMIT ?"
        params.append(max(1, min(int(limit), 500)))
        return self._fetchall(sql, params)

    def get_item(self, profile_id: int, item_id: str) -> dict | None:
        return self._fetchone(
            "SELECT * FROM seen_items WHERE profile_id = ? AND item_id = ?",
            (profile_id, str(item_id)),
        )

    def item_stats(self, profile_id: int | None = None) -> dict:
        where, params = (
            ("WHERE profile_id = ?", [profile_id]) if profile_id else ("", [])
        )
        row = (
            self._fetchone(
                f"""
            SELECT COUNT(*) AS total,
                   COALESCE(SUM(CASE WHEN notified = 1 THEN 1 ELSE 0 END), 0) AS notified,
                   COALESCE(SUM(CASE WHEN notify_error IS NOT NULL THEN 1 ELSE 0 END), 0) AS failed
              FROM seen_items {where}
            """,
                params,
            )
            or {}
        )
        row["today"] = (
            self._fetchone(
                f"SELECT COUNT(*) AS c FROM seen_items {where} "
                f"{'AND' if where else 'WHERE'} substr(found_at, 1, 10) = ?",
                [*params, utcnow_iso()[:10]],
            )
            or {}
        ).get("c", 0)
        return row

    def purge_seen(self, retention_days: int) -> int:
        from datetime import timedelta

        from .utils import utcnow

        cutoff = (utcnow() - timedelta(days=retention_days)).isoformat(
            timespec="seconds"
        )
        with self._lock:
            cur = self._conn.execute(
                "DELETE FROM seen_items WHERE found_at < ?", (cutoff,)
            )
            self._conn.execute("DELETE FROM ignored_items WHERE seen_at < ?", (cutoff,))
            self._conn.commit()
            return cur.rowcount or 0

    def clear_seen(self, profile_id: int | None = None) -> int:
        """Oublie les annonces vues **et** écartées (pour re-tester des filtres)."""
        with self._lock:
            if profile_id:
                cur = self._conn.execute(
                    "DELETE FROM seen_items WHERE profile_id = ?", (profile_id,)
                )
                self._conn.execute(
                    "DELETE FROM ignored_items WHERE profile_id = ?", (profile_id,)
                )
            else:
                cur = self._conn.execute("DELETE FROM seen_items")
                self._conn.execute("DELETE FROM ignored_items")
            self._conn.commit()
            return cur.rowcount or 0

    # ── Cache vendeurs ───────────────────────────────────────────────────
    def get_seller_cache(self, key: str, max_age_hours: int) -> dict | None:
        from .utils import parse_iso

        row = self._fetchone("SELECT * FROM seller_cache WHERE key = ?", (key,))
        if not row:
            return None
        fetched = parse_iso(row.get("fetched_at"))
        if not fetched:
            return None
        from .utils import utcnow

        age_hours = (utcnow() - fetched).total_seconds() / 3600
        return row if age_hours <= max_age_hours else None

    def set_seller_cache(self, key: str, seller: dict) -> None:
        self._execute(
            """
            INSERT INTO seller_cache (key, seller_id, name, rating, feedback, url, fetched_at)
            VALUES (?,?,?,?,?,?,?)
            ON CONFLICT(key) DO UPDATE SET seller_id = excluded.seller_id,
                name = excluded.name, rating = excluded.rating,
                feedback = excluded.feedback, url = excluded.url,
                fetched_at = excluded.fetched_at
            """,
            (
                key,
                str(seller.get("id") or ""),
                seller.get("name") or "",
                seller.get("rating"),
                seller.get("feedback"),
                seller.get("url") or "",
                utcnow_iso(),
            ),
        )

    # ── Logs ─────────────────────────────────────────────────────────────
    def log(
        self,
        level: str,
        message: str,
        *,
        source: str = "engine",
        profile_id: int | None = None,
    ) -> None:
        self._execute(
            "INSERT INTO logs (ts, level, source, profile_id, message) VALUES (?,?,?,?,?)",
            (
                utcnow_iso(),
                level.upper()[:8],
                source[:20],
                profile_id,
                str(message)[:2000],
            ),
        )

    def recent_logs(
        self, limit: int = 200, profile_id: int | None = None
    ) -> list[dict]:
        params: list[Any] = []
        sql = "SELECT * FROM logs"
        if profile_id:
            sql += " WHERE profile_id = ?"
            params.append(profile_id)
        sql += " ORDER BY id DESC LIMIT ?"
        params.append(max(1, min(int(limit), 1000)))
        return self._fetchall(sql, params)

    def purge_logs(self, keep: int = 5000) -> int:
        with self._lock:
            cur = self._conn.execute(
                "DELETE FROM logs WHERE id NOT IN (SELECT id FROM logs ORDER BY id DESC LIMIT ?)",
                (max(100, int(keep)),),
            )
            self._conn.commit()
            return cur.rowcount or 0

    # ── Scans ────────────────────────────────────────────────────────────
    def start_scan(self, profile_id: int) -> int:
        return self._execute(
            "INSERT INTO scans (profile_id, started_at, status) VALUES (?,?,'running')",
            (profile_id, utcnow_iso()),
        )

    def finish_scan(
        self,
        scan_id: int,
        *,
        status: str,
        pages: int,
        items_seen: int,
        new_items: int,
        error: str | None,
        duration_ms: int,
    ) -> None:
        self._execute(
            """
            UPDATE scans SET finished_at = ?, status = ?, pages = ?, items_seen = ?,
                             new_items = ?, error = ?, duration_ms = ?
             WHERE id = ?
            """,
            (
                utcnow_iso(),
                status,
                pages,
                items_seen,
                new_items,
                error,
                duration_ms,
                scan_id,
            ),
        )

    def mark_interrupted_scans(self) -> int:
        """Un scan encore « running » au démarrage vient d'un arrêt brutal."""
        return self._execute_rowcount(
            "UPDATE scans SET status = 'interrupted', finished_at = ? WHERE status = 'running'",
            (utcnow_iso(),),
        )

    def latest_scans(self, limit: int = 20) -> list[dict]:
        return self._fetchall(
            """
            SELECT s.*, p.name AS profile_name
              FROM scans s JOIN profiles p ON p.id = s.profile_id
             ORDER BY s.id DESC LIMIT ?
            """,
            (max(1, min(int(limit), 200)),),
        )
