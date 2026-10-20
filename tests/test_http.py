"""Tests réseau : client HTTP, cookies, rotation de proxys, self-healing.

Un faux serveur Vinted local (http.server) sert de cible : aucun accès Internet.
"""

from __future__ import annotations

import json
import sys
import tempfile
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import ConfigStore  # noqa: E402
from app.database import Database  # noqa: E402
from app.http_client import HttpClient  # noqa: E402
from app.vinted_api import normalize_item  # noqa: E402

ITEM = {
    "id": 424242,
    "title": "Nike Air Max 97",
    "price": {"amount": "89.0", "currency_code": "EUR"},
    "brand_title": "Nike",
    "size_title": "42",
    "status": "Très bon état",
    "url": "https://www.vinted.fr/items/424242",
    "photo": {"url": "https://img/1.jpg", "full_size_url": "https://img/1-hd.jpg"},
    "user": {
        "id": 12,
        "login": "vendeur",
        "feedback_reputation": 0.9,
        "feedback_count": 42,
    },
}

DETAIL_PAYLOAD = {
    "props": {
        "pageProps": {
            "item": {
                "id": 424242,
                "title": "Nike Air Max 97",
                "description": "Portées deux fois, aucune tache.",
                "user": {
                    "id": 12,
                    "login": "vendeur",
                    "feedback_reputation": 0.96,
                    "feedback_count": 132,
                },
            }
        }
    }
}


class FakeVinted(BaseHTTPRequestHandler):
    hits: list[dict] = []
    fail_api_once = True
    lock = threading.Lock()

    def log_message(self, *_args):  # silence
        pass

    def _send(self, status: int, body: str, content_type="text/html", headers=None):
        payload = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        path = self.path.split("?")[0]
        with FakeVinted.lock:
            FakeVinted.hits.append(
                {
                    "path": self.path,
                    "ua": self.headers.get("User-Agent"),
                    "cookie": self.headers.get("Cookie"),
                }
            )

        if path == "/":
            self._send(
                200,
                "<html><body>ok</body></html>",
                headers={
                    "Set-Cookie": "_vinted_fr_session=session-abc; Path=/; HttpOnly"
                },
            )
            return

        if path == "/api/v2/catalog/items":
            if FakeVinted.fail_api_once:
                FakeVinted.fail_api_once = False
                self._send(
                    429,
                    '{"error": "rate limited"}',
                    "application/json",
                    {"Retry-After": "0"},
                )
                return
            self._send(200, json.dumps({"items": [ITEM]}), "application/json")
            return

        if path == "/items/424242":
            self._send(
                200,
                '<html><script id="__NEXT_DATA__" type="application/json">'
                + json.dumps(DETAIL_PAYLOAD)
                + "</script></html>",
            )
            return

        self._send(404, "not found")


class HttpClientTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        FakeVinted.hits = []
        FakeVinted.fail_api_once = True
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), FakeVinted)
        cls.base = f"http://127.0.0.1:{cls.server.server_address[1]}"
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / "config.json").write_text(
            json.dumps(
                {
                    "http": {
                        "max_retries": 2,
                        "timeout_seconds": 5,
                        "block_backoff_seconds": [0.05, 0.05],
                        "user_agents": ["TestAgent/1.0", "TestAgent/2.0"],
                        "cookie_refresh_minutes": 30,
                    },
                    "engine": {"min_request_delay": 0.01},
                    "proxies": {
                        "enabled": False,
                        "list": [],
                        "sources": [],
                        "auto_discover": False,
                        "ban_after_failures": 2,
                        "cooldown_seconds": 60,
                    },
                }
            ),
            encoding="utf-8",
        )
        self.config = ConfigStore(root / "config.json")
        self.db = Database(root / "http.db")
        self.client = HttpClient(self.config, self.db)

    async def asyncTearDown(self):
        await self.client.close()
        self.db.close()
        self.tmp.cleanup()

    async def test_recently_blocked_uses_last_block_timestamp(self):
        """Pendant une vague de blocages, on met les requêtes de confort en pause."""
        self.assertFalse(self.client.recently_blocked())
        self.client._stats["last_block_at"] = time.time()
        self.assertTrue(self.client.recently_blocked())
        self.assertTrue(self.client.recently_blocked(120))
        self.client._stats["last_block_at"] = time.time() - 300
        self.assertFalse(self.client.recently_blocked(120))

    async def test_block_sets_last_block_timestamp(self):
        FakeVinted.fail_api_once = True
        response = await self.client.get(self.base + "/api/v2/catalog/items", attempts=1)
        self.assertTrue(response.blocked)
        self.assertTrue(self.client.recently_blocked())

    async def test_warm_up_sets_session_cookie(self):
        ok = await self.client.warm_up(self.base + "/")
        self.assertTrue(ok)
        cookies = self.client.stats()["cookies"]
        host = self.base.split("//")[1]
        self.assertIn(host, cookies)
        self.assertIn("_vinted_fr_session", cookies[host])
        ua = [hit["ua"] for hit in FakeVinted.hits if hit["path"] == "/"][-1]
        self.assertTrue(ua.startswith("TestAgent/"))

    async def test_cookie_sent_once_after_warm_up(self):
        await self.client.warm_up(self.base + "/")
        response = await self.client.get(self.base + "/items/424242")
        self.assertTrue(response.ok)
        cookie = FakeVinted.hits[-1]["cookie"] or ""
        self.assertEqual(cookie.count("_vinted_fr_session=session-abc"), 1)

    async def test_blocked_request_retries_and_heals(self):
        FakeVinted.fail_api_once = True
        before = self.client.stats()["blocked"]
        response = await self.client.get(
            self.base + "/api/v2/catalog/items", attempts=3, timeout=5
        )
        self.assertTrue(response.ok, response.short_error)
        self.assertEqual(response.status, 200)
        self.assertGreaterEqual(self.client.stats()["blocked"], before + 1)
        self.assertEqual(len(response.json()["items"]), 1)
        self.assertIsNotNone(response.attempts)

    async def test_item_detail_parsing(self):
        response = await self.client.get(self.base + "/items/424242")
        self.assertTrue(response.ok)
        self.assertIn("description", response.text)

    async def test_proxy_failure_falls_back_to_direct(self):
        await self.client.proxies.add(["127.0.0.1:9"], source="configured")
        self.config.apply_patch({"proxies": {"enabled": True}})
        response = await self.client.get(
            self.base + "/api/v2/catalog/items", attempts=2, timeout=2
        )
        self.assertTrue(response.ok, response.short_error)
        pool = self.client.proxies.stats()
        self.assertTrue(pool["enabled"])
        self.assertEqual(pool["quarantined"], 1)
        self.assertEqual(pool["available"], 0)

    async def test_proxy_reload_masks_credentials(self):
        await self.client.proxies.add(["user:secret@127.0.0.1:9"], source="configured")
        exposed = self.client.proxies.stats()["proxies"][0]["url"]
        self.assertIn("•••", exposed)
        self.assertNotIn("secret", exposed)

        self.config.apply_patch({"proxies": {"list": ["127.0.0.1:10"]}})
        await self.client.proxies.reload()
        pool = self.client.proxies.stats()
        self.assertEqual(pool["total"], 1)
        self.assertTrue(pool["proxies"][0]["url"].endswith("127.0.0.1:10"))

    async def test_transport_exposes_stats(self):
        stats = self.client.stats()
        self.assertIn(stats["transport"], {"curl_cffi", "httpx"})
        self.assertIn("proxy_pool", stats)


class DetailParsingTests(unittest.IsolatedAsyncioTestCase):
    def test_normalize_uses_hd_photo(self):
        item = normalize_item(ITEM, "https://www.vinted.fr")
        self.assertEqual(item["image_url"], "https://img/1-hd.jpg")


if __name__ == "__main__":
    unittest.main()
