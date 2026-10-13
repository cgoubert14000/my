"""SQLite persistence (WAL mode). One small repository class; JSON columns for nested breakdowns."""
from __future__ import annotations

import json
import pathlib
import sqlite3
import threading
import time
from typing import Any, Iterable

SCHEMA = """
CREATE TABLE IF NOT EXISTS opportunities (
  id TEXT PRIMARY KEY, ts REAL, chain_id INTEGER, block_number INTEGER, route TEXT, route_key TEXT, token TEXT,
  flash_source TEXT, amount_in TEXT, gross_profit TEXT, expected_net TEXT, simulated_net TEXT, realized_net TEXT,
  expected_net_eur REAL, margin_bps REAL, spread_bps REAL, decision TEXT, p_success REAL, p_lower REAL, p_n INTEGER,
  uncertainty TEXT, sim_ok INTEGER, sim_error TEXT, sim_gas_used INTEGER, data_age_ms REAL, ghost_next_block_net TEXT,
  tx_hash TEXT, payload TEXT
);
CREATE INDEX IF NOT EXISTS idx_opp_ts ON opportunities(ts);
CREATE INDEX IF NOT EXISTS idx_opp_route_block ON opportunities(route_key, block_number);
CREATE TABLE IF NOT EXISTS observations (
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, source TEXT, route_key TEXT, label INTEGER, net_after REAL,
  net_expected REAL, features TEXT
);
CREATE TABLE IF NOT EXISTS executions (
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, opportunity_id TEXT, tx_hash TEXT, status TEXT, gas_used INTEGER,
  effective_gas_price TEXT, gas_cost_wei TEXT, realized_net TEXT, expected_net TEXT, error TEXT, block_number INTEGER
);
CREATE TABLE IF NOT EXISTS metrics (
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, name TEXT, value REAL, labels TEXT
);
CREATE INDEX IF NOT EXISTS idx_metrics_name_ts ON metrics(name, ts);
CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, level TEXT, kind TEXT, message TEXT, data TEXT
);
CREATE TABLE IF NOT EXISTS lab_runs (
  id INTEGER PRIMARY KEY AUTOINCREMENT, started REAL, finished REAL, status TEXT, report TEXT
);
CREATE TABLE IF NOT EXISTS changes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, kind TEXT, description TEXT, before TEXT, after TEXT,
  metric_before REAL, metric_after REAL, accepted INTEGER, git_ref TEXT
);
CREATE TABLE IF NOT EXISTS kv (key TEXT PRIMARY KEY, value TEXT);
"""


class Database:
    def __init__(self, path: pathlib.Path | str):
        self.path = pathlib.Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._conn = sqlite3.connect(str(self.path), check_same_thread=False, isolation_level=None)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA synchronous=NORMAL")
        self._conn.executescript(SCHEMA)

    def close(self) -> None:
        with self._lock:
            self._conn.close()

    # ------------------------------------------------------------------ generic

    def _exec(self, sql: str, params: Iterable[Any] = ()) -> sqlite3.Cursor:
        with self._lock:
            return self._conn.execute(sql, tuple(params))

    def _rows(self, sql: str, params: Iterable[Any] = ()) -> list[dict]:
        with self._lock:
            return [dict(r) for r in self._conn.execute(sql, tuple(params)).fetchall()]

    # ------------------------------------------------------------------ opportunities

    def upsert_opportunity(self, rec: dict) -> None:
        cols = [
            "id", "ts", "chain_id", "block_number", "route", "route_key", "token", "flash_source", "amount_in", "gross_profit",
            "expected_net", "simulated_net", "realized_net", "expected_net_eur", "margin_bps", "spread_bps", "decision",
            "p_success", "p_lower", "p_n", "uncertainty", "sim_ok", "sim_error", "sim_gas_used", "data_age_ms",
            "ghost_next_block_net", "tx_hash",
        ]
        vals = []
        for c in cols:
            v = rec.get(c)
            if c in ("amount_in", "gross_profit", "expected_net", "simulated_net", "realized_net", "ghost_next_block_net") and v is not None:
                v = str(v)
            if c == "sim_ok" and v is not None:
                v = int(v)
            vals.append(v)
        vals.append(json.dumps(rec, default=str))
        placeholders = ",".join("?" * (len(cols) + 1))
        self._exec(f"INSERT OR REPLACE INTO opportunities ({','.join(cols)},payload) VALUES ({placeholders})", vals)

    def count_opportunities(self, since: float | None = None, decision: str | None = None) -> int:
        sql, params = "SELECT COUNT(*) FROM opportunities", []
        where = []
        if since:
            where.append("ts >= ?")
            params.append(since)
        if decision:
            where.append("decision = ?")
            params.append(decision)
        if where:
            sql += " WHERE " + " AND ".join(where)
        return int(self._exec(sql, params).fetchone()[0])

    def iter_export(self, since: float | None, max_rows: int = 30_000):
        """Streams opportunity payloads for the session export, most informative first: every record with a positive
        expected net, a simulation or a ghost label, then the remaining negatives by decreasing expected net, capped
        at `max_rows` (the full set stays in the SQLite file)."""
        sql = ("SELECT payload FROM opportunities" + (" WHERE ts >= ?" if since else "") +
               " ORDER BY (expected_net_eur > 0) DESC, (sim_ok IS NOT NULL) DESC, (ghost_next_block_net IS NOT NULL) DESC,"
               " expected_net_eur DESC, ts ASC LIMIT ?")
        cur = self._conn.execute(sql, ([since] if since else []) + [max_rows])
        for (payload,) in cur:
            yield json.loads(payload)

    def opportunities(self, limit: int = 200, decision: str | None = None, since: float | None = None) -> list[dict]:
        sql = "SELECT payload FROM opportunities"
        where, params = [], []
        if decision:
            where.append("decision = ?")
            params.append(decision)
        if since:
            where.append("ts >= ?")
            params.append(since)
        if where:
            sql += " WHERE " + " AND ".join(where)
        sql += " ORDER BY ts DESC LIMIT ?"
        params.append(limit)
        return [json.loads(r["payload"]) for r in self._rows(sql, params)]

    def opportunity_stats(self, since: float | None = None) -> dict:
        """Exact session aggregates computed in SQL (never capped by a page size)."""
        w = " WHERE ts >= ?" if since else ""
        p = (since,) if since else ()
        row = self._rows(
            "SELECT COUNT(*) AS total,"
            " SUM(CASE WHEN CAST(expected_net AS REAL) > 0 THEN 1 ELSE 0 END) AS positive,"
            " SUM(CASE WHEN sim_ok IS NOT NULL THEN 1 ELSE 0 END) AS simulated,"
            " SUM(CASE WHEN sim_ok = 1 THEN 1 ELSE 0 END) AS sim_ok,"
            " SUM(CASE WHEN sim_ok = 0 THEN 1 ELSE 0 END) AS sim_failed,"
            " SUM(CASE WHEN ghost_next_block_net IS NOT NULL THEN 1 ELSE 0 END) AS ghost_labeled,"
            " SUM(CASE WHEN CAST(ghost_next_block_net AS REAL) > 0 THEN 1 ELSE 0 END) AS ghost_positive"
            f" FROM opportunities{w}", p)[0]
        out = {k: int(v or 0) for k, v in row.items()}
        out["decisions"] = self.opportunity_counts(since)
        try:
            rows = self._rows("SELECT je.value AS reason, COUNT(*) AS n FROM opportunities, json_each(json_extract(payload,'$.reasons')) AS je"
                              + w + " GROUP BY je.value", p)
            reasons: dict[str, int] = {}
            for r in rows:
                key = str(r["reason"]).split(":")[0].split("(")[0]
                reasons[key] = reasons.get(key, 0) + int(r["n"])
            out["reject_reasons"] = reasons
        except sqlite3.OperationalError:  # SQLite built without JSON1 → caller falls back to row scan
            out["reject_reasons"] = None
        return out

    def top_opportunities(self, since: float | None = None, limit: int = 25, positive_only: bool = False) -> list[dict]:
        """Highest expected net (EUR) first — exact over the whole session."""
        where, params = ["expected_net_eur IS NOT NULL"], []
        if since:
            where.append("ts >= ?")
            params.append(since)
        if positive_only:
            where.append("CAST(expected_net AS REAL) > 0")
        sql = "SELECT payload FROM opportunities WHERE " + " AND ".join(where) + " ORDER BY expected_net_eur DESC LIMIT ?"
        params.append(limit)
        return [json.loads(r["payload"]) for r in self._rows(sql, params)]

    def opportunity_counts(self, since: float | None = None) -> dict:
        sql = "SELECT decision, COUNT(*) AS n FROM opportunities" + (" WHERE ts >= ?" if since else "") + " GROUP BY decision"
        return {r["decision"]: r["n"] for r in self._rows(sql, (since,) if since else ())}

    # ------------------------------------------------------------------ observations

    def add_observation(self, ts: float, source: str, route_key: str, label: int, net_after: float | None,
                        net_expected: float | None, features: dict) -> None:
        self._exec(
            "INSERT INTO observations (ts,source,route_key,label,net_after,net_expected,features) VALUES (?,?,?,?,?,?,?)",
            (ts, source, route_key, int(label), net_after, net_expected, json.dumps(features)),
        )

    def observations(self, limit: int = 100_000) -> list[dict]:
        rows = self._rows("SELECT * FROM observations ORDER BY ts ASC LIMIT ?", (limit,))
        for r in rows:
            r["features"] = json.loads(r["features"])
        return rows

    # ------------------------------------------------------------------ executions / metrics / events

    def add_execution(self, rec: dict) -> None:
        cols = ["ts", "opportunity_id", "tx_hash", "status", "gas_used", "effective_gas_price", "gas_cost_wei", "realized_net",
                "expected_net", "error", "block_number"]
        self._exec(f"INSERT INTO executions ({','.join(cols)}) VALUES ({','.join('?' * len(cols))})",
                   [str(rec.get(c)) if c in ("effective_gas_price", "gas_cost_wei", "realized_net", "expected_net") and rec.get(c) is not None else rec.get(c) for c in cols])

    def executions(self, limit: int = 200) -> list[dict]:
        return self._rows("SELECT * FROM executions ORDER BY ts DESC LIMIT ?", (limit,))

    def execution_summary(self) -> dict:
        rows = self._rows("SELECT status, COUNT(*) n, SUM(CAST(gas_cost_wei AS REAL)) gas, SUM(CAST(realized_net AS REAL)) net FROM executions GROUP BY status")
        return {r["status"]: {"n": r["n"], "gas_wei": r["gas"] or 0, "net": r["net"] or 0} for r in rows}

    def add_metric(self, name: str, value: float, labels: dict | None = None, ts: float | None = None) -> None:
        self._exec("INSERT INTO metrics (ts,name,value,labels) VALUES (?,?,?,?)",
                   (ts or time.time(), name, float(value), json.dumps(labels or {})))

    def metrics(self, name: str, since: float, limit: int = 2000) -> list[dict]:
        return self._rows("SELECT ts,value,labels FROM metrics WHERE name=? AND ts>=? ORDER BY ts ASC LIMIT ?", (name, since, limit))

    def add_event(self, level: str, kind: str, message: str, data: dict | None = None) -> None:
        self._exec("INSERT INTO events (ts,level,kind,message,data) VALUES (?,?,?,?,?)",
                   (time.time(), level, kind, message, json.dumps(data or {}, default=str)))

    def events(self, limit: int = 200, kind: str | None = None) -> list[dict]:
        if kind:
            return self._rows("SELECT * FROM events WHERE kind=? ORDER BY ts DESC LIMIT ?", (kind, limit))
        return self._rows("SELECT * FROM events ORDER BY ts DESC LIMIT ?", (limit,))

    # ------------------------------------------------------------------ lab / changes / kv

    def add_lab_run(self, started: float, finished: float | None, status: str, report: dict) -> int:
        cur = self._exec("INSERT INTO lab_runs (started,finished,status,report) VALUES (?,?,?,?)",
                         (started, finished, status, json.dumps(report, default=str)))
        return int(cur.lastrowid)

    def update_lab_run(self, run_id: int, finished: float | None, status: str, report: dict) -> None:
        self._exec("UPDATE lab_runs SET finished=?, status=?, report=? WHERE id=?",
                   (finished, status, json.dumps(report, default=str), run_id))

    def lab_runs(self, limit: int = 20) -> list[dict]:
        rows = self._rows("SELECT * FROM lab_runs ORDER BY started DESC LIMIT ?", (limit,))
        for r in rows:
            r["report"] = json.loads(r["report"])
        return rows

    def add_change(self, kind: str, description: str, before: dict, after: dict, metric_before: float | None,
                   metric_after: float | None, accepted: bool, git_ref: str = "") -> None:
        self._exec(
            "INSERT INTO changes (ts,kind,description,before,after,metric_before,metric_after,accepted,git_ref) VALUES (?,?,?,?,?,?,?,?,?)",
            (time.time(), kind, description, json.dumps(before, default=str), json.dumps(after, default=str), metric_before,
             metric_after, int(accepted), git_ref),
        )

    def changes(self, limit: int = 100) -> list[dict]:
        return self._rows("SELECT * FROM changes ORDER BY ts DESC LIMIT ?", (limit,))

    def kv_get(self, key: str, default: Any = None) -> Any:
        rows = self._rows("SELECT value FROM kv WHERE key=?", (key,))
        return json.loads(rows[0]["value"]) if rows else default

    def kv_set(self, key: str, value: Any) -> None:
        self._exec("INSERT OR REPLACE INTO kv (key,value) VALUES (?,?)", (key, json.dumps(value, default=str)))
