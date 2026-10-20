"""Tests du mode temps réel : intervalles adaptatifs, détection, flux SSE."""

from __future__ import annotations

import asyncio
import json
import random
import tempfile
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from app.config import ConfigStore
from app.database import Database
from app.engine import BotEngine
from app.models import ProfileIn
from app.realtime import LiveSettings, is_live, next_interval
from app.state import AppState
from app.utils import utcnow_iso_ms
from app.vinted_api import (
    SearchPage,
    head_item_ids,
    newest_item_id,
    parse_catalog_html,
)

ORIGIN = "https://www.vinted.fr"


def card(item_id: str, title: str = "Nike Air Max 97", price: str = "89,00 €") -> str:
    return (
        f'<div data-testid="grid-item">'
        f'<div data-testid="product-item-id-{item_id}">'
        f'<a href="/items/{item_id}-slug" title="{title}, Marque: Nike, 42, {price}">'
        f'<img src="https://images1.vinted.net/t/{item_id}.webp" alt="{title}">'
        f"</a></div></div>"
    )


class IntervalTests(unittest.TestCase):
    def test_defaults_match_config(self):
        class FakeConfig:
            def get(self, key, default=None):
                return {
                    "engine.realtime_min_interval": 2,
                    "engine.realtime_max_interval": 8,
                    "engine.realtime_turbo": False,
                }.get(key, default)

        settings = LiveSettings.from_config(FakeConfig())
        self.assertEqual(settings.min_interval, 2)
        self.assertEqual(settings.max_interval, 8)
        self.assertIn("2", settings.describe())

    def test_bad_values_are_clamped(self):
        class FakeConfig:
            def get(self, key, default=None):
                return {
                    "engine.realtime_min_interval": 0.01,
                    "engine.realtime_max_interval": -5,
                    "engine.realtime_growth": 99,
                }.get(key, default)

        settings = LiveSettings.from_config(FakeConfig())
        self.assertGreaterEqual(settings.min_interval, 0.5)
        self.assertGreaterEqual(settings.max_interval, settings.min_interval)
        self.assertLessEqual(settings.growth, 4.0)

    def test_hit_goes_back_to_minimum(self):
        settings = LiveSettings(min_interval=1.5, max_interval=10, jitter=0)
        interval = next_interval(9.0, new_items=2, settings=settings)
        self.assertAlmostEqual(interval, 1.5)

    def test_idle_grows_then_caps(self):
        settings = LiveSettings(min_interval=1.5, max_interval=10, growth=1.6, jitter=0)
        first = next_interval(1.5, new_items=0, since_last_found=600, settings=settings)
        self.assertAlmostEqual(first, 2.4)
        capped = 1.5
        for _ in range(20):
            capped = next_interval(
                capped, new_items=0, since_last_found=600, settings=settings
            )
        self.assertAlmostEqual(capped, 10.0)

    def test_burst_after_a_find(self):
        settings = LiveSettings(
            min_interval=1.5, max_interval=10, burst_seconds=90, jitter=0
        )
        interval = next_interval(
            8.0, new_items=0, since_last_found=10, settings=settings
        )
        self.assertAlmostEqual(interval, 1.5)

    def test_turbo_is_constant(self):
        settings = LiveSettings(min_interval=1.0, max_interval=30, turbo=True, jitter=0)
        for _ in range(5):
            self.assertAlmostEqual(
                next_interval(20, new_items=0, since_last_found=999, settings=settings),
                1.0,
            )

    def test_jitter_stays_in_bounds(self):
        settings = LiveSettings(min_interval=2, max_interval=2, jitter=0.5)
        for _ in range(50):
            value = next_interval(
                2,
                new_items=0,
                since_last_found=999,
                settings=settings,
                rng=random.Random(7),
            )
            self.assertGreaterEqual(value, 0.5)
            self.assertLessEqual(value, 2.0)

    def test_is_live_respects_global_switch(self):
        class Config:
            def __init__(self, value):
                self.value = value

            def get(self, key, default=None):
                return self.value

        self.assertTrue(is_live({"live_mode": True}, Config(True)))
        self.assertFalse(is_live({"live_mode": True}, Config(False)))
        self.assertFalse(is_live({"live_mode": False}, Config(True)))


class ProfileModelTests(unittest.TestCase):
    def test_realtime_defaults(self):
        profile = ProfileIn(name="Test")
        self.assertTrue(profile.live_mode)
        self.assertEqual(profile.interval_seconds, 60)

    def test_one_second_interval_allowed(self):
        self.assertEqual(ProfileIn(name="Test", interval_seconds=1).interval_seconds, 1)
        with self.assertRaises(Exception):
            ProfileIn(name="Test", interval_seconds=0)


class DeltaParsingTests(unittest.TestCase):
    def test_newest_item_id(self):
        html = "<html>" + card("111") + card("222") + "</html>"
        self.assertEqual(newest_item_id(html), "111")
        self.assertEqual(head_item_ids(html, limit=2), ["111", "222"])

    def test_newest_item_id_without_grid(self):
        self.assertIsNone(newest_item_id("<html>rien</html>"))
        self.assertIsNone(newest_item_id(""))

    def test_fast_path_limits_parsing(self):
        html = (
            "<html>"
            + "".join(card(str(1000 + i), price=f"{10 + i},00 €") for i in range(20))
            + "</html>"
        )
        full = parse_catalog_html(html, ORIGIN, "EUR")
        fast = parse_catalog_html(html, ORIGIN, "EUR", limit=3, fast=True)
        self.assertEqual(len(full), 20)
        self.assertEqual([item["id"] for item in fast], ["1000", "1001", "1002"])
        self.assertEqual(fast[0]["title"], full[0]["title"])


# ── Moteur ────────────────────────────────────────────────────────────────


class FakeAPI:
    """API scriptée : chaque appel consomme le lot d'annonces suivant."""

    def __init__(self, batches: list[list[dict]], description: str = ""):
        self.batches = list(batches)
        self.calls: list[dict] = []
        self.description = description

    async def ensure_session(self, url, profile_id=None, force=False):
        return True

    async def search(
        self,
        profile,
        page=1,
        domain="www.vinted.fr",
        *,
        known_head=None,
        head_limit=None,
    ):
        self.calls.append({"known_head": known_head, "head_limit": head_limit})
        batch = self.batches.pop(0) if self.batches else []
        newest = batch[0]["id"] if batch else None
        head_key = ",".join(row["id"] for row in batch[:20])
        if known_head and head_key == known_head:
            return SearchPage(
                items=[],
                url="fake://catalog",
                unchanged=True,
                newest_id=newest,
                head_key=head_key,
            )
        return SearchPage(
            items=list(batch), url="fake://catalog", newest_id=newest, head_key=head_key
        )

    async def enrich_item(self, item, domain="www.vinted.fr", profile_id=None):
        if self.description:
            return {**item, "description": self.description}
        return item

    async def fetch_seller(self, item, domain="www.vinted.fr", profile_id=None):
        return item


class FakeNotifier:
    def __init__(self):
        self.sent: list[dict] = []
        self.stats: dict = {}

    async def notify(self, profile, item):
        self.sent.append(item)
        return True, None


class FakeClient:
    transport = "test"

    def stats(self):
        return {"proxy_pool": {"enabled": False, "total": 0, "available": 0}}


def item(item_id: str, price: float = 89.0, title: str = "Nike Air Max 97") -> dict:
    return {
        "id": item_id,
        "title": title,
        "price": price,
        "currency": "EUR",
        "brand": "Nike",
        "size": "42",
        "condition": "Très bon état",
        "description": "",
        "url": f"{ORIGIN}/items/{item_id}",
        "image_url": "",
        "seller_name": "",
        "seller_id": "",
        "seller_rating": None,
        "seller_feedback": None,
        "seller_url": "",
        "favourites": 0,
        "is_reserved": False,
        "is_hidden": False,
        "is_closed": False,
    }


class EngineRealtimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        config_path = root / "config.json"
        config_path.write_text(
            json.dumps(
                {
                    "engine": {
                        "start_paused": True,
                        "min_request_delay": 0.0,
                        "baseline_first_scan": True,
                        "realtime_min_interval": 1.5,
                        "realtime_max_interval": 10,
                        "realtime_jitter": 0,
                    }
                }
            ),
            encoding="utf-8",
        )
        self.config = ConfigStore(config_path)
        self.db = Database(root / "test.db")
        self.profile = self.db.create_profile(
            {
                "name": "Snipe",
                "url": "https://www.vinted.fr/catalog?search_text=nike",
                "min_price": 10,
                "max_price": 300,
                "live_mode": True,
            }
        )

    def tearDown(self):
        self.db.close()
        self.tmp.cleanup()

    def _engine(self, api, notifier):
        return BotEngine(self.config, self.db, FakeClient(), api, notifier)

    def _scan(self, engine):
        """Comme l'ordonnanceur : le profil est relu en base à chaque passage."""
        return asyncio.run(engine.scan_profile(self.db.get_profile(self.profile["id"])))

    def test_detects_new_item_and_dedupes(self):
        api = FakeAPI(
            [
                [item("1")],  # baseline
                [item("2"), item("1")],
                [item("2"), item("1")],  # relecture complète, rien de neuf
                [item("2"), item("1")],  # inchangé → page sautée
            ]
        )
        notifier = FakeNotifier()
        engine = self._engine(api, notifier)

        first = self._scan(engine)
        self.assertTrue(first.baseline)
        self.assertEqual(first.new_items, 1)
        self.assertEqual(notifier.sent, [])

        second = self._scan(engine)
        self.assertFalse(second.baseline)
        self.assertEqual(second.new_items, 1)
        self.assertEqual([row["id"] for row in notifier.sent], ["2"])
        self.assertIsNotNone(second.detection_ms)

        third = self._scan(engine)
        self.assertFalse(third.unchanged)
        self.assertEqual(third.new_items, 0)
        self.assertIsNone(api.calls[-1]["known_head"])

        fourth = self._scan(engine)
        self.assertTrue(fourth.unchanged)
        self.assertEqual(api.calls[-1]["known_head"], "2,1")
        self.assertEqual(len(notifier.sent), 1, "aucune alerte en double")

        scans = self.db.latest_scans(5)
        self.assertTrue(scans[0]["detection_ms"] is None)
        self.assertTrue(any(scan["detection_ms"] for scan in scans))

    def test_interval_shrinks_after_a_find(self):
        api = FakeAPI([[item("1")], [item("2"), item("1")]])
        engine = self._engine(api, FakeNotifier())
        self._scan(engine)
        engine._interval[self.profile["id"]] = 8.0
        outcome = self._scan(engine)
        self.assertEqual(outcome.new_items, 1)
        interval = engine._after_scan(self.profile, outcome)
        self.assertAlmostEqual(interval, 1.5)

    def test_live_events_are_published(self):
        api = FakeAPI([[item("1")], [item("2"), item("1")]])
        engine = self._engine(api, FakeNotifier())
        queue = engine.subscribe()
        self._scan(engine)
        self._scan(engine)
        events = []
        while not queue.empty():
            events.append(queue.get_nowait())
        kinds = [event["type"] for event in events]
        self.assertIn("item", kinds)
        self.assertIn("scan", kinds)
        new_items = [event for event in events if event["type"] == "item"]
        self.assertEqual(new_items[0]["item"]["item_id"], "1")
        self.assertTrue(new_items[0]["baseline"])
        self.assertEqual(new_items[-1]["item"]["item_id"], "2")
        self.assertFalse(new_items[-1]["baseline"])
        self.assertIn("detection_ms", new_items[-1])

    def test_burst_beyond_head_limit_is_not_lost(self):
        """Après une rafale, le passage suivant analyse toute la page."""
        api = FakeAPI(
            [[item("1")], [item("2"), item("1")], [item("3"), item("2"), item("1")]]
        )
        notifier = FakeNotifier()
        engine = self._engine(api, notifier)
        self._scan(engine)
        self.assertEqual(api.calls[0]["known_head"], None)
        second = self._scan(engine)
        self.assertEqual(second.new_items, 1)
        # Trouvaille → le passage suivant relit la page entière.
        self.assertIn(self.profile["id"], engine._deep_next)
        third = self._scan(engine)
        self.assertIsNone(api.calls[2]["known_head"])
        self.assertIsNone(api.calls[2]["head_limit"])
        self.assertEqual(third.new_items, 1)
        self.assertEqual([row["id"] for row in notifier.sent], ["2", "3"])

    def test_sponsored_card_on_top_does_not_hide_new_items(self):
        """Une annonce sponsorisée figée en tête ne doit pas masquer les nouveautés.

        Cas réel relevé sur vinted.fr : les premières cartes ne sont pas toujours
        triées par identifiant décroissant (emplacements sponsorisés). Comparer
        uniquement la première carte raterait les annonces insérées juste après.
        """
        sponsored = item("S1", price=90.0, title="Sponsorisée — Nike Air Max")
        api = FakeAPI([[sponsored, item("1")], [sponsored, item("2"), item("1")]])
        notifier = FakeNotifier()
        engine = self._engine(api, notifier)
        self._scan(engine)  # baseline
        outcome = self._scan(engine)
        self.assertFalse(outcome.unchanged)
        self.assertEqual(outcome.new_items, 1)
        self.assertEqual([row["id"] for row in notifier.sent], ["2"])

    def test_unchanged_scan_is_silent(self):
        """Une page identique ne produit ni alerte, ni avertissement."""
        api = FakeAPI([[item("1")], [item("1")], [item("1")]])
        engine = self._engine(api, FakeNotifier())
        self._scan(engine)  # baseline
        self._scan(engine)  # pleine lecture : rien de neuf
        outcome = self._scan(engine)  # page inchangée
        self.assertTrue(outcome.unchanged)
        self.assertEqual(outcome.status, "ok")
        messages = " ".join(log["message"] for log in self.db.recent_logs(200))
        self.assertNotIn("aucune annonce reçue", messages)

    def test_empty_first_scan_does_not_block_future_alerts(self):
        """Une recherche vide au démarrage ne doit pas rendre les alertes muettes."""
        api = FakeAPI([[], [item("1")]])
        notifier = FakeNotifier()
        engine = self._engine(api, notifier)
        first = self._scan(engine)
        self.assertEqual(first.status, "empty")
        self.assertTrue(self.db.get_profile(self.profile["id"])["baseline_done"])
        second = self._scan(engine)
        self.assertEqual(second.new_items, 1)
        self.assertFalse(second.baseline)
        self.assertEqual([row["id"] for row in notifier.sent], ["1"])

    def test_ignored_items_cache_is_updated(self):
        """Un rejet qui a coûté une requête (description) est mémorisé."""
        self.db.update_profile(
            self.profile["id"],
            {
                **self.profile,
                "whitelist": ["nike"],
                "blacklist": ["tache"],
                "check_description": True,
            },
        )
        api = FakeAPI(
            [[item("9", price=50, title="Nike Air Max 97")]],
            description="Très bon état, petite tache sur la manche.",
        )
        engine = self._engine(api, FakeNotifier())
        outcome = self._scan(engine)
        self.assertEqual(outcome.new_items, 0)
        self.assertIn("9", engine._ignored(self.profile["id"]))
        self.assertEqual(engine._seen(self.profile["id"]), set())

    def test_cheap_rejections_do_not_bloat_the_database(self):
        """Un prix hors bornes est écarté en mémoire, sans ligne en base."""
        api = FakeAPI([[item("1", price=5.0)], [item("2", price=900.0)]])
        engine = self._engine(api, FakeNotifier())
        self._scan(engine)
        self._scan(engine)
        self.assertEqual(engine._seen(self.profile["id"]), set())
        self.assertEqual(engine._ignored(self.profile["id"]), set())
        self.assertEqual(self.db.item_stats()["total"], 0)

    def test_throttle_after_blocks_and_recovery(self):
        """Après un blocage, le profil ralentit, puis revient à la normale."""
        engine = self._engine(FakeAPI([[]]), FakeNotifier())
        pid = self.profile["id"]
        profile = self.db.get_profile(pid)
        engine._slow_down(profile)
        engine._slow_down(profile)
        self.assertAlmostEqual(engine.throttle_for(pid), 2.56, places=2)

        blocked = type(
            "Outcome", (), {"status": "blocked", "error": "HTTP 429", "new_items": 0}
        )()
        interval = engine._after_scan(profile, blocked)
        self.assertGreaterEqual(interval, 10)
        self.assertGreater(engine.throttle_for(pid), 3)

        for _ in range(40):
            engine._speed_up(profile)
        self.assertEqual(engine.throttle_for(pid), 1.0)

    def test_throttle_caps_the_interval(self):
        engine = self._engine(FakeAPI([[]]), FakeNotifier())
        ok = type("Outcome", (), {"status": "ok", "error": None, "new_items": 0})()
        for _ in range(6):
            engine._slow_down(self.profile)
        engine._interval[self.profile["id"]] = 1.5
        interval = engine._after_scan(self.profile, ok)
        self.assertLessEqual(interval, 60.0)
        self.assertGreater(interval, 1.5)

    def test_invalidate_profile_clears_caches(self):
        engine = self._engine(FakeAPI([[]]), FakeNotifier())
        self.db.add_seen(self.profile["id"], item("7"))
        self.assertIn("7", engine._seen(self.profile["id"]))
        engine._head[self.profile["id"]] = "7"
        engine.invalidate_profile(self.profile["id"])
        self.assertNotIn(self.profile["id"], engine._seen_cache)
        self.assertNotIn(self.profile["id"], engine._head)


class DatabaseRealtimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Database(Path(self.tmp.name) / "test.db")

    def tearDown(self):
        self.db.close()
        self.tmp.cleanup()

    def test_live_mode_defaults_to_true(self):
        profile = self.db.create_profile({"name": "T", "url": "https://www.vinted.fr"})
        self.assertTrue(profile["live_mode"])
        updated = self.db.update_profile(profile["id"], {**profile, "live_mode": False})
        self.assertFalse(updated["live_mode"])

    def test_description_is_stored_and_updated(self):
        profile = self.db.create_profile({"name": "T", "url": "https://www.vinted.fr"})
        self.db.add_seen(profile["id"], item("1"))
        self.assertTrue(
            self.db.update_item(profile["id"], "1", {"description": "Porté deux fois."})
        )
        row = self.db.get_item(profile["id"], "1")
        self.assertEqual(row["description"], "Porté deux fois.")
        self.assertEqual(row["seller_rating"], None)
        self.assertFalse(self.db.update_item(profile["id"], "1", {"inconnu": 1}))

    def test_seen_ids_cache_source(self):
        profile = self.db.create_profile({"name": "T", "url": "https://www.vinted.fr"})
        self.db.add_seen(profile["id"], item("1"))
        self.db.add_seen(profile["id"], item("2"))
        self.db.add_ignored(profile["id"], "3", "blacklist")
        self.assertEqual(self.db.seen_ids(profile["id"]), {"1", "2"})
        self.assertEqual(self.db.ignored_ids(profile["id"]), {"3"})

    def test_prune_scans(self):
        profile = self.db.create_profile({"name": "T", "url": "https://www.vinted.fr"})
        for _ in range(30):
            scan_id = self.db.start_scan(profile["id"])
            self.db.finish_scan(
                scan_id,
                status="ok",
                pages=1,
                items_seen=1,
                new_items=0,
                error=None,
                duration_ms=10,
            )
        removed = self.db.prune_scans(keep_per_profile=20)
        self.assertEqual(removed, 10)
        self.assertEqual(len(self.db.latest_scans(100)), 20)

    def test_millisecond_timestamps(self):
        self.assertRegex(utcnow_iso_ms(), r"T\d\d:\d\d:\d\d\.\d{3}")


class StreamEndpointTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        config_path = root / "config.json"
        config_path.write_text(
            json.dumps({"engine": {"start_paused": True}}), encoding="utf-8"
        )
        from tests.fake_vinted import FakeVintedAPI

        self.state = AppState(
            config_path=config_path, db_path=root / "test.db", api_class=FakeVintedAPI
        )
        self.state.notifier.dry_run = True
        self.client = TestClient(self.state_app())
        self.client.__enter__()

    def state_app(self):
        from app.web import create_app

        return create_app(self.state)

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()

    def test_stream_sends_hello_and_events(self):
        with self.client.stream("GET", "/api/stream") as response:
            self.assertEqual(response.status_code, 200)
            self.assertTrue(
                response.headers["content-type"].startswith("text/event-stream")
            )
            lines = response.iter_lines()
            self.assertEqual(next(lines), ": connected")
            self.assertEqual(next(lines), "")
            self.assertEqual(next(lines), "event: hello")
            self.assertIn('"ok": true', next(lines))

    def test_publish_reaches_subscribers(self):
        queue = self.state.engine.subscribe()
        self.state.engine.publish({"type": "item", "item": {"item_id": "42"}})
        event = queue.get_nowait()
        self.assertEqual(event["type"], "item")
        self.state.engine.unsubscribe(queue)
        self.assertNotIn(queue, self.state.engine._listeners)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
