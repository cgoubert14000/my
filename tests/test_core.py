"""Tests unitaires du socle (aucun réseau requis)."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import ConfigError, ConfigStore  # noqa: E402
from app.database import Database  # noqa: E402
from app.filters import matches_profile  # noqa: E402
from app.notify import DiscordNotifier, stars  # noqa: E402
from app.utils import (
    format_money,
    format_rating,
    normalize_text,  # noqa: E402
    parse_money,
)
from app.vinted_api import (  # noqa: E402
    api_url_from_search,
    normalize_item,
    parse_compact_text,
    search_url,
)


class TextAndMoneyTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize_text("  Taché  d’encre "), "tache d'encre")
        self.assertEqual(normalize_text("DÉFAUT"), "defaut")

    def test_money(self):
        self.assertEqual(
            parse_money({"amount": "12.50", "currency_code": "EUR"}), (12.5, "EUR")
        )
        self.assertEqual(parse_money("9,90"), (9.9, "EUR"))
        self.assertEqual(parse_money("12,50 €"), (12.5, "EUR"))
        self.assertEqual(parse_money("€ 1.234,56"), (1234.56, "EUR"))
        self.assertEqual(parse_money(None), (None, "EUR"))
        self.assertEqual(format_money(12, "EUR"), "12 €")
        self.assertEqual(format_money(12.5, "EUR"), "12,50 €")

    def test_rating(self):
        self.assertEqual(format_rating(0.96), 4.8)
        self.assertEqual(format_rating(4.8), 4.8)
        self.assertIsNone(format_rating(None))

    def test_stars(self):
        self.assertIn("4.8/5", stars(4.8))


class UrlTests(unittest.TestCase):
    def test_search_url_keyword(self):
        url = search_url(
            "nike air max", "www.vinted.fr", min_price=20, max_price=100, page=2
        )
        self.assertIn("https://www.vinted.fr/catalog?", url)
        self.assertIn("order=newest_first", url)
        self.assertIn("page=2", url)
        self.assertIn("price_from=20", url)
        self.assertIn("price_to=100", url)
        self.assertIn("search_text=nike+air+max", url)

    def test_search_url_preserves_existing_filters(self):
        url = search_url(
            "https://www.vinted.fr/catalog?search_text=sac&brand_ids[]=12&order=price_low_to_high",
            min_price=50,
        )
        self.assertIn("brand_ids%5B%5D=12", url)
        self.assertIn("order=newest_first", url)
        self.assertNotIn("price_low_to_high", url)

    def test_api_url(self):
        web = "https://www.vinted.fr/catalog?search_text=nike&order=newest_first&page=1"
        api = api_url_from_search(web, per_page=96)
        self.assertTrue(api.startswith("https://www.vinted.fr/api/v2/catalog/items?"))
        self.assertIn("per_page=96", api)
        self.assertIn("search_text=nike", api)


SAMPLE_ITEM = {
    "id": 123456,
    "title": "Nike Air Max 97",
    "price": {"amount": "89.0", "currency_code": "EUR"},
    "total_item_price": {"amount": "94.5", "currency_code": "EUR"},
    "brand_title": "Nike",
    "size_title": "42",
    "status": "Très bon état",
    "url": "https://www.vinted.fr/items/123456-nike-air-max-97",
    "photo": {
        "url": "https://images.vinted.net/1.jpg",
        "full_size_url": "https://images.vinted.net/1-hd.jpg",
    },
    "favourite_count": 12,
    "user": {
        "id": 77,
        "login": "vendeur_test",
        "profile_url": "https://www.vinted.fr/member/77",
        "feedback_reputation": 0.96,
        "feedback_count": 132,
    },
}


class ParsingTests(unittest.TestCase):
    def test_normalize_item(self):
        item = normalize_item(SAMPLE_ITEM, "https://www.vinted.fr")
        self.assertEqual(item["id"], "123456")
        self.assertEqual(item["price"], 89.0)
        self.assertEqual(item["total_price"], 94.5)
        self.assertEqual(item["currency"], "EUR")
        self.assertEqual(item["brand"], "Nike")
        self.assertEqual(item["size"], "42")
        self.assertEqual(item["condition"], "Très bon état")
        self.assertEqual(item["image_url"], "https://images.vinted.net/1-hd.jpg")
        self.assertEqual(item["seller_name"], "vendeur_test")
        self.assertEqual(item["seller_rating"], 4.8)
        self.assertEqual(item["seller_feedback"], 132)
        self.assertEqual(item["favourites"], 12)

    def test_normalize_relative_url(self):
        raw = dict(SAMPLE_ITEM, url="/items/123456", user={"id": 77, "login": "x"})
        item = normalize_item(raw, "https://www.vinted.fr")
        self.assertEqual(item["url"], "https://www.vinted.fr/items/123456")
        self.assertEqual(item["seller_url"], "https://www.vinted.fr/member/77")

    def test_compact_text_french(self):
        data = parse_compact_text(
            "Nike Air Max 97 GS Sneaker Schwarz / Weiß – Gr. 36 (US 4Y), "
            "Marque: Nike, État: Bon état, Taille: 36, 12.99 €, 14.34 €"
        )
        self.assertEqual(
            data["title"], "Nike Air Max 97 GS Sneaker Schwarz / Weiß – Gr. 36 (US 4Y)"
        )
        self.assertEqual(data["brand"], "Nike")
        self.assertEqual(data["condition"], "Bon état")
        self.assertEqual(data["size"], "36")
        self.assertEqual(data["price"], 12.99)
        self.assertEqual(data["total_price"], 14.34)
        self.assertEqual(data["currency"], "EUR")

    def test_compact_text_english_currency(self):
        data = parse_compact_text(
            "Vintage ceramic woven tray, Condition: Very good, 4.00 $, 4.90 $",
            default_currency="EUR",
        )
        self.assertEqual(data["title"], "Vintage ceramic woven tray")
        self.assertEqual(data["condition"], "Very good")
        self.assertEqual(data["price"], 4.0)
        self.assertEqual(data["currency"], "USD")

    def test_compact_text_title_without_labels(self):
        data = parse_compact_text("Lot de 3 t-shirts, 25,00 €")
        self.assertEqual(data["title"], "Lot de 3 t-shirts")
        self.assertEqual(data["price"], 25.0)

    def test_compact_text_thousands(self):
        data = parse_compact_text(
            "Sac cuir, Marque: Hermès, État: Bon état, 1 250,00 €"
        )
        self.assertEqual(data["price"], 1250.0)


def base_profile(**overrides):
    profile = {
        "id": 1,
        "name": "Test",
        "url": "https://www.vinted.fr/catalog?search_text=nike",
        "min_price": None,
        "max_price": None,
        "whitelist": [],
        "blacklist": [],
        "keyword_mode": "any",
        "check_description": True,
        "min_seller_rating": None,
        "min_seller_feedback": None,
    }
    profile.update(overrides)
    return profile


def base_item(**overrides):
    item = normalize_item(SAMPLE_ITEM, "https://www.vinted.fr")
    item.update(overrides)
    return item


class FilterTests(unittest.TestCase):
    def test_price(self):
        self.assertFalse(
            matches_profile(base_profile(min_price=100), base_item()).matched
        )
        self.assertFalse(
            matches_profile(base_profile(max_price=50), base_item()).matched
        )
        self.assertTrue(
            matches_profile(
                base_profile(min_price=50, max_price=100), base_item()
            ).matched
        )

    def test_blacklist_accent_insensitive(self):
        profile = base_profile(blacklist=["défaut", "taché"])
        self.assertFalse(
            matches_profile(profile, base_item(title="Nike Air Max — défaut")).matched
        )
        result = matches_profile(profile, base_item(title="Nike Air Max tachée"))
        self.assertFalse(result.matched)
        self.assertIn("tach", result.reason)

    def test_blacklist_description(self):
        profile = base_profile(blacklist=["copie"])
        item = base_item(description="Véritable copie AAA")
        self.assertFalse(matches_profile(profile, item).matched)

    def test_whitelist(self):
        profile = base_profile(whitelist=["nike", "jordan"])
        self.assertTrue(matches_profile(profile, base_item()).matched)
        self.assertFalse(
            matches_profile(
                profile, base_item(title="Adidas Samba", brand="adidas")
            ).matched
        )
        both = base_profile(whitelist=["nike", "max"], keyword_mode="all")
        self.assertTrue(matches_profile(both, base_item()).matched)
        self.assertFalse(
            matches_profile(both, base_item(title="Nike Air force")).matched
        )

    def test_seller_thresholds(self):
        profile = base_profile(min_seller_rating=4.9)
        self.assertFalse(matches_profile(profile, base_item()).matched)
        self.assertTrue(
            matches_profile(base_profile(min_seller_rating=4.5), base_item()).matched
        )
        profile = base_profile(min_seller_feedback=200)
        self.assertFalse(matches_profile(profile, base_item()).matched)

    def test_closed(self):
        self.assertFalse(
            matches_profile(base_profile(), base_item(is_closed=True)).matched
        )


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Database(Path(self.tmp.name) / "test.db")

    def tearDown(self):
        self.db.close()
        self.tmp.cleanup()

    def profile_payload(self, name="Sneakers"):
        return {
            "name": name,
            "active": True,
            "url": "https://www.vinted.fr/catalog?search_text=nike",
            "min_price": 10,
            "max_price": 200,
            "whitelist": ["nike", "jordan"],
            "blacklist": ["copie"],
            "keyword_mode": "any",
            "check_description": True,
            "webhook": "",
            "interval_seconds": 60,
            "min_seller_rating": 4.0,
            "min_seller_feedback": 5,
            "pages": 1,
            "notes": "",
        }

    def test_profile_crud(self):
        profile = self.db.create_profile(self.profile_payload())
        self.assertEqual(profile["whitelist"], ["nike", "jordan"])
        self.assertTrue(profile["active"])
        updated = self.db.update_profile(
            profile["id"], {**self.profile_payload("Luxe"), "active": False}
        )
        self.assertEqual(updated["name"], "Luxe")
        self.assertFalse(updated["active"])
        self.db.set_active(profile["id"], True)
        self.assertTrue(self.db.get_profile(profile["id"])["active"])
        dup = self.db.duplicate_profile(profile["id"])
        self.assertIn("copie", dup["name"])
        self.assertFalse(dup["active"])
        self.assertTrue(self.db.delete_profile(profile["id"]))
        self.assertIsNone(self.db.get_profile(profile["id"]))

    def test_seen_dedupe_and_feed(self):
        profile = self.db.create_profile(self.profile_payload())
        item = base_item()
        self.assertFalse(self.db.is_seen(profile["id"], item["id"]))
        self.assertTrue(self.db.add_seen(profile["id"], item))
        self.assertFalse(self.db.add_seen(profile["id"], item))  # doublon
        self.assertTrue(self.db.is_seen(profile["id"], item["id"]))
        self.assertEqual(self.db.item_stats()["total"], 1)
        feed = self.db.recent_items()
        self.assertEqual(feed[0]["profile_name"], "Sneakers")
        self.assertEqual(self.db.clear_seen(profile["id"]), 1)
        self.assertFalse(self.db.is_seen(profile["id"], item["id"]))

    def test_logs_and_scans(self):
        profile = self.db.create_profile(self.profile_payload())
        self.db.log("INFO", "hello", profile_id=profile["id"])
        self.assertEqual(self.db.recent_logs()[0]["message"], "hello")
        scan_id = self.db.start_scan(profile["id"])
        self.db.finish_scan(
            scan_id,
            status="ok",
            pages=1,
            items_seen=10,
            new_items=2,
            error=None,
            duration_ms=120,
        )
        self.assertEqual(self.db.latest_scans()[0]["new_items"], 2)

        # Un scan resté « running » après un arrêt brutal est marqué interrompu.
        self.db.start_scan(profile["id"])
        self.assertEqual(self.db.mark_interrupted_scans(), 1)
        self.assertEqual(self.db.latest_scans()[0]["status"], "interrupted")

    def test_baseline_flag(self):
        profile = self.db.create_profile(self.profile_payload())
        self.assertFalse(profile["baseline_done"])
        self.db.mark_baseline_done(profile["id"])
        self.assertTrue(self.db.get_profile(profile["id"])["baseline_done"])


class ConfigTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "config.json"
        self.store = ConfigStore(self.path)

    def tearDown(self):
        self.tmp.cleanup()

    def test_defaults_written(self):
        self.assertTrue(self.path.exists())
        self.assertEqual(self.store.get("engine.default_interval_seconds"), 60)
        self.assertTrue(self.store.get("engine.baseline_first_scan"))

    def test_patch_and_persist(self):
        self.store.apply_patch(
            {
                "engine": {"default_interval_seconds": 90},
                "proxies": {"enabled": True, "list": "1.2.3.4:8080\n5.6.7.8:3128"},
            }
        )
        reloaded = ConfigStore(self.path)
        self.assertEqual(reloaded.get("engine.default_interval_seconds"), 90)
        self.assertEqual(len(reloaded.get("proxies.list")), 2)
        self.assertTrue(reloaded.get("proxies.enabled"))

    def test_validation(self):
        with self.assertRaises(ConfigError):
            self.store.apply_patch({"engine": {"default_interval_seconds": 0}})
        with self.assertRaises(ConfigError):
            self.store.apply_patch(
                {"discord": {"default_webhook": "https://example.com/hook"}}
            )
        with self.assertRaises(ConfigError):
            self.store.apply_patch({"engine": {"unknown": True}})
        with self.assertRaises(ConfigError):
            self.store.apply_patch({"discord": {"default_webhook": "pas une url"}})

    def test_password_hidden(self):
        self.store.apply_patch({"app": {"password": "secret"}})
        public = self.store.public()
        self.assertEqual(public["app"]["password"], "")
        self.assertTrue(public["app"]["password_set"])


class NotifyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Database(Path(self.tmp.name) / "n.db")
        self.store = ConfigStore(Path(self.tmp.name) / "config.json")
        self.notifier = DiscordNotifier(self.store, self.db)

    def tearDown(self):
        self.db.close()
        self.tmp.cleanup()

    def test_embed(self):
        profile = {"id": 1, "name": "Sneakers Hype"}
        embed = self.notifier.build_embed(profile, base_item())
        self.assertEqual(embed["url"], SAMPLE_ITEM["url"])
        self.assertIn("Nike Air Max", embed["title"])
        self.assertEqual(embed["image"]["url"], "https://images.vinted.net/1-hd.jpg")
        names = [field["name"] for field in embed["fields"]]
        self.assertTrue(any("Prix" in name for name in names))
        self.assertTrue(any("Vendeur" in name for name in names))
        self.assertIn("Sneakers Hype", embed["footer"]["text"])
        self.assertIn(
            "89", [f["value"] for f in embed["fields"] if "Prix" in f["name"]][0]
        )

    def test_webhook_resolution(self):
        profile = {"webhook": "https://discord.com/api/webhooks/1/a"}
        self.assertEqual(
            self.notifier.webhook_for(profile), "https://discord.com/api/webhooks/1/a"
        )
        self.store.apply_patch(
            {"discord": {"default_webhook": "https://discord.com/api/webhooks/2/b"}}
        )
        self.assertEqual(
            self.notifier.webhook_for(None), "https://discord.com/api/webhooks/2/b"
        )


if __name__ == "__main__":
    unittest.main()
