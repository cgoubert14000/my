"""Persistance SQLite : profils, articles vus, vendeurs, logs, scans.

Une seule connexion par process, protégée par un verrou : suffisant pour un
dashboard local et un moteur qui écrivent en concurrence.
"""

from __future__ import annotations

import json
import re
import sqlite3
import threading
from pathlib import Path
from collections.abc import Iterable
from typing import Any

from .utils import clean_terms, utcnow_iso, utcnow_iso_ms

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
    live_mode               INTEGER NOT NULL DEFAULT 1,
    min_seller_rating       REAL,
    min_seller_feedback     INTEGER,
    pages                   INTEGER NOT NULL DEFAULT 1,
    notes                   TEXT NOT NULL DEFAULT '',
    category                TEXT NOT NULL DEFAULT '',
    brands                  TEXT NOT NULL DEFAULT '',
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
    description      TEXT NOT NULL DEFAULT '',
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
    detection_ms  INTEGER,
    FOREIGN KEY (profile_id) REFERENCES profiles (id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS brands (
    id          TEXT PRIMARY KEY,
    slug        TEXT NOT NULL DEFAULT '',
    name        TEXT NOT NULL DEFAULT '',
    search_key  TEXT NOT NULL DEFAULT '',
    updated_at  TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_brands_key ON brands (search_key);

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
    "live_mode",
    "min_seller_rating",
    "min_seller_feedback",
    "pages",
    "notes",
    "category",
    "brands",
)


def brand_search_key(value: str) -> str:
    """Clé de recherche insensible aux accents, à la casse et aux séparateurs."""
    import unicodedata

    text = unicodedata.normalize("NFKD", (value or "").lower())
    text = "".join(char for char in text if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


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
            if "category" not in columns:
                self._conn.execute(
                    "ALTER TABLE profiles ADD COLUMN category TEXT NOT NULL DEFAULT ''"
                )
            if "brands" not in columns:
                self._conn.execute(
                    "ALTER TABLE profiles ADD COLUMN brands TEXT NOT NULL DEFAULT ''"
                )
            if "live_mode" not in columns:
                # Les bases existantes passent en temps réel par défaut.
                self._conn.execute(
                    "ALTER TABLE profiles ADD COLUMN live_mode INTEGER NOT NULL DEFAULT 1"
                )
            scan_columns = {
                row["name"]
                for row in self._conn.execute("PRAGMA table_info(scans)").fetchall()
            }
            if "detection_ms" not in scan_columns:
                self._conn.execute("ALTER TABLE scans ADD COLUMN detection_ms INTEGER")
            seen_columns = {
                row["name"]
                for row in self._conn.execute(
                    "PRAGMA table_info(seen_items)"
                ).fetchall()
            }
            if "description" not in seen_columns:
                self._conn.execute(
                    "ALTER TABLE seen_items ADD COLUMN description TEXT NOT NULL DEFAULT ''"
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
        row["live_mode"] = bool(row.get("live_mode", 1))
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
            "live_mode": 1,
            "min_seller_rating": None,
            "min_seller_feedback": None,
            "pages": 1,
            "notes": "",
            "category": "",
            "brands": "",
        }
        data = {**defaults, **dict(payload)}
        for key in ("whitelist", "blacklist"):
            data[key] = json.dumps(clean_terms(data.get(key) or []), ensure_ascii=False)
        for key in ("active", "check_description", "live_mode"):
            data[key] = 1 if data.get(key) else 0
        return {key: data.get(key) for key in PROFILE_FIELDS}

    def upsert_brands(self, rows: list[dict]) -> int:
        """Enregistre un lot de marques (index complet issu des sitemaps)."""
        if not rows:
            return 0
        now = utcnow_iso()
        payload = [
            (
                str(row["id"]),
                str(row.get("slug") or ""),
                str(row.get("name") or ""),
                brand_search_key(f"{row.get('name', '')} {row.get('slug', '')} {row.get('id', '')}"),
                now,
            )
            for row in rows
            if str(row.get("id") or "").isdigit()
        ]
        with self._lock:
            self._conn.executemany(
                "INSERT INTO brands (id, slug, name, search_key, updated_at) "
                "VALUES (?, ?, ?, ?, ?) "
                "ON CONFLICT(id) DO UPDATE SET slug=excluded.slug, name=excluded.name, "
                "search_key=excluded.search_key, updated_at=excluded.updated_at",
                payload,
            )
            self._conn.commit()
        return len(payload)

    @staticmethod
    def _brand_clause(query: str, prefix: bool) -> tuple[str, list[str]]:
        """Clause SQL de recherche de marques (contenu ou préfixe).

        En mode préfixe, chaque mot doit commencer un mot de la clé : taper
        « n » propose donc **toutes** les marques commençant par N, et
        « new bal » propose « New Balance ».
        """
        key = brand_search_key(query)
        if not key:
            return "", []
        words = [word for word in key.split() if word][:5]
        if not words:
            return "", []
        # La clé compacte (sans espaces) attrape les marques ponctuées :
        # « C.P. Company » -> « c p company » -> « cpcompany », donc « cp » marche.
        compact = "REPLACE(search_key, ' ', '')"
        if prefix:
            first, *rest = words
            clauses = [f"({compact} LIKE ? OR search_key LIKE ? OR search_key LIKE ?)"]
            params: list[str] = [f"{first}%", f"{first}%", f"% {first}%"]
            for word in rest:
                clauses.append("search_key LIKE ?")
                params.append(f"%{word}%")
            return " AND ".join(clauses), params
        clause = " AND ".join(
            f"(search_key LIKE ? OR {compact} LIKE ?)" for _ in words
        )
        params = []
        for word in words:
            params.extend([f"%{word}%", f"%{word}%"])
        return clause, params

    def list_brands(self, limit: int | None = None) -> list[dict]:
        """Toutes les marques de l'index (export, sauvegarde, partage)."""
        sql = "SELECT id, slug, name FROM brands ORDER BY name COLLATE NOCASE"
        params: tuple = ()
        if limit:
            sql += " LIMIT ?"
            params = (int(limit),)
        with self._lock:
            rows = self._conn.execute(sql, params).fetchall()
        return [{"id": row["id"], "slug": row["slug"], "name": row["name"]} for row in rows]

    def search_brands(
        self, query: str, limit: int = 60, prefix: bool = False
    ) -> list[dict]:
        """Recherche locale dans l'index complet des marques."""
        clause, params = self._brand_clause(query, prefix)
        if not clause:
            return []
        cap = 500 if prefix else 200
        # Les marques qui commencent vraiment par la saisie passent devant.
        rank = ""
        if prefix:
            key = brand_search_key(query).split()[0]
            rank = "CASE WHEN REPLACE(search_key, ' ', '') LIKE ? THEN 0 ELSE 1 END, "
            params = [*params, f"{key}%"]
        with self._lock:
            rows = self._conn.execute(
                f"SELECT id, slug, name FROM brands WHERE {clause} "
                f"ORDER BY {rank}LENGTH(name), name LIMIT ?",
                (*params, max(1, min(int(limit), cap))),
            ).fetchall()
        return [{"id": row["id"], "slug": row["slug"], "name": row["name"]} for row in rows]

    def count_brands(self, query: str, prefix: bool = True) -> int:
        """Nombre de marques correspondant à la recherche (pour l'autocomplétion)."""
        clause, params = self._brand_clause(query, prefix)
        if not clause:
            return 0
        with self._lock:
            row = self._conn.execute(
                f"SELECT COUNT(*) AS total FROM brands WHERE {clause}", tuple(params)
            ).fetchone()
        return int(row["total"] or 0)

    def brand_stats(self) -> dict:
        with self._lock:
            row = self._conn.execute(
                "SELECT COUNT(*) AS total, MAX(updated_at) AS updated FROM brands"
            ).fetchone()
        return {"total": int(row["total"] or 0), "updated_at": row["updated"]}

    def get_brand(self, brand_id: str) -> dict | None:
        with self._lock:
            row = self._conn.execute(
                "SELECT id, slug, name FROM brands WHERE id = ?", (str(brand_id),)
            ).fetchone()
        return dict(row) if row else None

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
                INSERT INTO seen_items (profile_id, item_id, title, description, price,
                    total_price, currency, brand, size, condition, url, image_url,
                    seller_id, seller_name, seller_rating, seller_feedback,
                    seller_url, favourites, found_at, raw)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    profile_id,
                    str(item["id"]),
                    item.get("title", ""),
                    item.get("description", ""),
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
                    utcnow_iso_ms(),
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

    def seen_ids(self, profile_id: int) -> set[str]:
        """Identifiants déjà enregistrés — amorce du cache mémoire du moteur."""
        rows = self._fetchall(
            "SELECT item_id FROM seen_items WHERE profile_id = ?", (profile_id,)
        )
        return {str(row["item_id"]) for row in rows}

    def ignored_ids(self, profile_id: int) -> set[str]:
        rows = self._fetchall(
            "SELECT item_id FROM ignored_items WHERE profile_id = ?", (profile_id,)
        )
        return {str(row["item_id"]) for row in rows}

    def update_item(self, profile_id: int, item_id: str, fields: dict) -> bool:
        """Complète une annonce déjà enregistrée (description, vendeur, photo…)."""
        allowed = {
            "title",
            "description",
            "price",
            "total_price",
            "currency",
            "brand",
            "size",
            "condition",
            "url",
            "image_url",
            "seller_id",
            "seller_name",
            "seller_rating",
            "seller_feedback",
            "seller_url",
            "favourites",
        }
        data = {key: value for key, value in (fields or {}).items() if key in allowed}
        if not data:
            return False
        assignments = ", ".join(f"{key} = ?" for key in data)
        return (
            self._execute_rowcount(
                f"UPDATE seen_items SET {assignments} WHERE profile_id = ? AND item_id = ?",
                [*data.values(), profile_id, str(item_id)],
            )
            > 0
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

    def logs_since(self, last_id: int = 0, limit: int = 50) -> list[dict]:
        """Nouveaux journaux depuis un identifiant (poussée temps réel)."""
        return self._fetchall(
            "SELECT * FROM logs WHERE id > ? ORDER BY id ASC LIMIT ?",
            (int(last_id), max(1, min(int(limit), 200))),
        )

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
        detection_ms: int | None = None,
    ) -> None:
        self._execute(
            """
            UPDATE scans SET finished_at = ?, status = ?, pages = ?, items_seen = ?,
                             new_items = ?, error = ?, duration_ms = ?,
                             detection_ms = ?
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
                detection_ms,
                scan_id,
            ),
        )

    def mark_interrupted_scans(self) -> int:
        """Un scan encore « running » au démarrage vient d'un arrêt brutal."""
        return self._execute_rowcount(
            "UPDATE scans SET status = 'interrupted', finished_at = ? WHERE status = 'running'",
            (utcnow_iso(),),
        )

    def prune_scans(self, keep_per_profile: int = 600) -> int:
        """Ne garde que les N derniers scans par profil (mode temps réel)."""
        keep = max(20, int(keep_per_profile))
        return self._execute_rowcount(
            """
            DELETE FROM scans
             WHERE id NOT IN (
                   SELECT id FROM scans s2
                    WHERE s2.profile_id = scans.profile_id
                    ORDER BY id DESC LIMIT ?
             )
            """,
            (keep,),
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
