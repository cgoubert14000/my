"""Tests d'intégration : API + moteur, avec un faux Vinted (aucun réseau)."""

from __future__ import annotations

import json
import sys
import tempfile
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient  # noqa: E402

from app.state import AppState  # noqa: E402
from app.web import create_app  # noqa: E402
from tests.fake_vinted import FAKE_PROFILES, FakeVintedAPI  # noqa: E402


class AppTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        config_path = root / "config.json"
        config_path.write_text(
            json.dumps(
                {
                    "app": {"host": "127.0.0.1", "port": 8000, "open_browser": False},
                    "engine": {
                        "start_paused": True,
                        "min_request_delay": 0.05,
                        "default_interval_seconds": 60,
                        "baseline_first_scan": True,
                    },
                    "notifications": {"enabled": True},
                }
            ),
            encoding="utf-8",
        )
        self.state = AppState(
            config_path=config_path,
            db_path=root / "test.db",
            api_class=FakeVintedAPI,
        )
        self.state.notifier.dry_run = True  # aucun envoi Discord réel
        for payload in FAKE_PROFILES:
            self.state.db.create_profile(payload)
        self.client = TestClient(create_app(self.state))
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()

    # ── Santé / profils ──────────────────────────────────────────────────
    def test_health_and_status(self):
        health = self.client.get("/api/health").json()
        self.assertTrue(health["ok"])
        self.assertNotIn("demo", health)  # plus aucun mode démo
        status = self.client.get("/api/status").json()
        self.assertTrue(status["running"])
        self.assertTrue(status["paused"])
        self.assertEqual(status["profiles_total"], 2)
        self.assertIn("proxy_pool", status["http"])

    def test_seeded_profiles_and_toggle(self):
        profiles = self.client.get("/api/profiles").json()["profiles"]
        self.assertEqual(len(profiles), 2)
        profile = profiles[0]
        response = self.client.post(
            f"/api/profiles/{profile['id']}/toggle", json={"active": False}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["profile"]["active"])
        self.assertEqual(
            self.client.get("/api/profiles").json()["profiles"][0]["active"], False
        )

    def test_create_update_delete(self):
        payload = {
            "name": "Test API",
            "active": True,
            "url": "https://www.vinted.fr/catalog?search_text=nike",
            "min_price": 10,
            "max_price": 100,
            "whitelist": "nike, jordan",
            "blacklist": ["copie"],
            "interval_seconds": 30,
            "webhook": "",
        }
        created = self.client.post("/api/profiles", json=payload)
        self.assertEqual(created.status_code, 200, created.text)
        profile = created.json()["profile"]
        self.assertEqual(profile["whitelist"], ["nike", "jordan"])
        self.assertEqual(profile["domain"], "www.vinted.fr")

        updated = self.client.put(
            f"/api/profiles/{profile['id']}",
            json={**payload, "name": "Renommé", "max_price": 200},
        )
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.json()["profile"]["name"], "Renommé")

        duplicated = self.client.post(f"/api/profiles/{profile['id']}/duplicate")
        self.assertEqual(duplicated.status_code, 200)
        self.assertFalse(duplicated.json()["profile"]["active"])

        deleted = self.client.delete(f"/api/profiles/{profile['id']}")
        self.assertEqual(deleted.status_code, 200)
        self.assertEqual(
            self.client.get(f"/api/profiles/{profile['id']}").status_code, 404
        )

    def test_invalid_inputs(self):
        bad_url = self.client.post(
            "/api/profiles", json={"name": "Bad", "url": "https://example.com/catalog"}
        )
        self.assertEqual(bad_url.status_code, 422)
        bad_webhook = self.client.post(
            "/api/profiles",
            json={"name": "Bad", "webhook": "https://discord.com/api/webhooks/abc"},
        )
        self.assertEqual(bad_webhook.status_code, 422)
        bad_price = self.client.post(
            "/api/profiles", json={"name": "Bad", "min_price": 100, "max_price": 10}
        )
        self.assertEqual(bad_price.status_code, 422)

    # ── Moteur & flux ────────────────────────────────────────────────────
    def test_manual_scan_feeds_dashboard(self):
        profile = self.client.get("/api/profiles").json()["profiles"][0]
        response = self.client.post(f"/api/profiles/{profile['id']}/scan")
        self.assertEqual(response.status_code, 200, response.text)
        items = []
        deadline = time.time() + 12
        while time.time() < deadline:
            items = self.client.get("/api/feed").json()["items"]
            if items:
                break
            time.sleep(0.25)
        self.assertTrue(items, "le flux devrait contenir les annonces du faux Vinted")
        top = items[0]
        for key in (
            "item_id",
            "title",
            "price",
            "url",
            "image_url",
            "seller_name",
            "seller_rating",
            "profile_name",
            "found_at",
        ):
            self.assertIn(key, top)
        self.assertIsNotNone(top["seller_rating"])
        # Les annonces blacklistées par le profil ne doivent pas apparaître.
        titles = " ".join(item["title"].lower() for item in items)
        self.assertNotIn("copie", titles)
        # Anti-doublon : un second scan n'ajoute pas deux fois le même item.
        ids = [item["item_id"] for item in items]
        self.assertEqual(len(ids), len(set(ids)))
        logs = self.client.get("/api/logs").json()["logs"]
        self.assertTrue(any("Scan" in log["message"] for log in logs))

    def test_preview_does_not_persist(self):
        profile = self.client.get("/api/profiles").json()["profiles"][0]
        preview = self.client.post(f"/api/profiles/{profile['id']}/preview")
        self.assertEqual(preview.status_code, 200, preview.text)
        data = preview.json()
        self.assertGreater(data["total"], 0)
        self.assertIn("matched", data["items"][0])
        self.assertEqual(self.client.get("/api/feed").json()["items"], [])

    def test_latest_scans_recorded(self):
        profile = self.client.get("/api/profiles").json()["profiles"][0]
        self.client.post(f"/api/profiles/{profile['id']}/scan")
        deadline = time.time() + 12
        scans = []
        while time.time() < deadline:
            scans = self.client.get("/api/scans").json()["scans"]
            if scans and scans[0]["status"] != "running":
                break
            time.sleep(0.25)
        self.assertTrue(scans)
        self.assertIn(scans[0]["status"], {"ok", "blocked", "error", "empty"})

    # ── Config / notifications ───────────────────────────────────────────
    def test_config_patch(self):
        response = self.client.put(
            "/api/config",
            json={
                "patch": {
                    "engine": {"default_interval_seconds": 120},
                    "notifications": {"enabled": True},
                }
            },
        )
        self.assertEqual(response.status_code, 200, response.text)
        config = self.client.get("/api/config").json()
        self.assertEqual(config["engine"]["default_interval_seconds"], 120)
        invalid = self.client.put(
            "/api/config", json={"patch": {"engine": {"default_interval_seconds": 0}}}
        )
        self.assertEqual(invalid.status_code, 400)

    def test_diagnose_endpoint(self):
        response = self.client.post(
            "/api/diagnose",
            json={"query": "nike", "webhook": "", "domain": "www.vinted.fr"},
        )
        self.assertEqual(response.status_code, 200, response.text)
        report = response.json()
        self.assertTrue(report["ok"])
        keys = [step["key"] for step in report["steps"]]
        self.assertEqual(keys[:4], ["setup", "session", "catalog", "sample"])
        catalog = next(step for step in report["steps"] if step["key"] == "catalog")
        self.assertTrue(catalog["ok"])
        self.assertGreater(catalog["data"]["items"], 0)
        self.assertTrue(report["advice"])
        self.assertTrue(all("skipped" in step for step in report["steps"]))

    def test_diagnose_skips_missing_enrichment(self):
        """Sans annonce exploitable, article/vendeur sont marqués « ignoré »."""
        state = self.state
        original = state.api.search

        async def empty_search(*args, **kwargs):
            page = await original(*args, **kwargs)
            page.items = []
            return page

        state.api.search = empty_search
        try:
            report = self.client.post("/api/diagnose", json={"query": "zzz"}).json()
        finally:
            state.api.search = original
        steps = {step["key"]: step for step in report["steps"]}
        self.assertTrue(steps["item"]["skipped"])
        self.assertTrue(steps["seller"]["skipped"])
        self.assertFalse(report["ok"])
        self.assertFalse(any("best-effort" in line for line in report["advice"]))

    def test_diagnose_rejects_bad_domain(self):
        response = self.client.post("/api/diagnose", json={"domain": "example.com"})
        self.assertEqual(response.status_code, 422)

    def test_webhook_test_dry_run(self):
        response = self.client.post(
            "/api/notifications/test",
            json={
                "webhook": "https://discord.com/api/webhooks/123456789/abcdef",
                "profile_name": "Tests",
            },
        )
        self.assertEqual(response.status_code, 200, response.text)
        self.assertTrue(response.json()["ok"])

    def test_pause_resume(self):
        started = self.client.post("/api/engine/toggle", json={"active": True}).json()
        self.assertFalse(started["paused"])
        paused = self.client.post("/api/engine/toggle", json={"active": False}).json()
        self.assertTrue(paused["paused"])

    def test_optional_basic_auth(self):
        self.state.config.apply_patch({"app": {"password": "s3cret"}})
        self.assertEqual(self.client.get("/api/health").status_code, 401)
        self.assertEqual(
            self.client.get("/api/health", auth=("vinted", "s3cret")).status_code, 200
        )
        self.assertEqual(
            self.client.get("/api/health", auth=("vinted", "wrong")).status_code, 401
        )
        self.state.config.apply_patch({"app": {"password": ""}})

    def test_static_dashboard(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertIn("Vinted Sniper", page.text)
        css = self.client.get("/static/styles.css")
        self.assertEqual(css.status_code, 200)
        js = self.client.get("/static/app.js")
        self.assertEqual(js.status_code, 200)


if __name__ == "__main__":
    unittest.main()
