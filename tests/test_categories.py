"""Catégories Vinted : listes, navigation, URL de profil et endpoint."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from app.categories import (
    TOP_LEVEL,
    build_profile_url,
    is_valid_path,
    normalize_path,
    page_title,
    parse_children,
    path_label,
    sanitize_path,
    top_level,
)
from app.http_client import HttpResponse
from app.state import AppState
from app.web import create_app
from tests.fake_vinted import FakeVintedAPI

ORIGIN = "https://www.vinted.fr"

# Extrait réaliste de la page /catalog/5-mens (menu latéral).
MENU_HTML = """
<html><body>
<h1>Hommes</h1>
<nav class="sidebar">
  <a href="/catalog/2050-men_clothing"><span>Vêtements</span></a>
  <a href="/catalog/1231-men_shoes_new">Chaussures</a>
  <a href="/catalog/82-men_accessories">Accessoires</a>
  <a href="/catalog/139-cosmetics_and_beauty_items">Soins</a>
  <a href="/catalog/5-mens">Hommes</a>
  <a href="/catalog/1231-men_shoes_new">Chaussures (doublon)</a>
  <a href="/catalog?search_text=nike">Recherche</a>
  <a href="/items/12345-nike">Annonce</a>
  <a href="/catalog/82-men_accessories"></a>
</nav>
</body></html>
"""


class PathTests(unittest.TestCase):
    def test_top_level_is_complete_and_unique(self):
        rows = top_level()
        self.assertGreaterEqual(len(rows), 8)
        ids = [row.id for row in rows]
        self.assertEqual(len(ids), len(set(ids)))
        for row in rows:
            self.assertTrue(row.path.startswith("/catalog/"))
            self.assertRegex(row.path, r"^/catalog/\d+-[a-z0-9_]+$")
            self.assertTrue(row.name)

    def test_top_level_contains_real_vinted_ids(self):
        ids = {cid for cid, _, _ in TOP_LEVEL}
        # Identifiants relevés sur vinted.fr (les URL /catalog/<id> fonctionnent).
        for expected in {"5", "1904", "1193", "4332", "1918", "2994", "2309"}:
            self.assertIn(expected, ids)

    def test_normalize_path(self):
        self.assertEqual(normalize_path("/catalog/5-mens"), "/catalog/5-mens")
        self.assertEqual(normalize_path("/catalog/5-mens/"), "/catalog/5-mens")
        self.assertEqual(normalize_path("https://www.vinted.fr/catalog/5-mens?x=1"), "/catalog/5-mens")
        self.assertEqual(normalize_path("catalog/1231-men_shoes_new"), "/catalog/1231-men_shoes_new")
        self.assertEqual(normalize_path(""), "/catalog")
        self.assertEqual(normalize_path("/catalog"), "/catalog")
        self.assertEqual(normalize_path("/catalog?search_text=nike"), "/catalog")

    def test_invalid_paths_are_neutralised(self):
        for bad in ("../../etc/passwd", "/admin", "/catalog/abc"):
            self.assertEqual(sanitize_path(bad), None, bad)
        self.assertEqual(normalize_path("../../etc/passwd"), "/catalog")
        self.assertEqual(sanitize_path(""), "/catalog")
        self.assertEqual(sanitize_path("https://evil.example/catalog/5"), "/catalog/5")
        self.assertEqual(sanitize_path("/catalog/5-mens?x=1"), "/catalog/5-mens")

    def test_valid_path(self):
        for good in ("/catalog", "/catalog/", "/catalog/5", "/catalog/5-mens"):
            self.assertTrue(is_valid_path(good), good)

    def test_path_label(self):
        self.assertEqual(path_label("/catalog"), "Toutes les catégories")
        self.assertEqual(path_label("/catalog/1231-men_shoes_new"), "Men Shoes New")
        self.assertEqual(path_label("/catalog/5", "Hommes"), "Hommes")


class ParseTests(unittest.TestCase):
    def test_children_are_deduplicated_and_cleaned(self):
        rows = parse_children(MENU_HTML, ORIGIN, exclude="/catalog/5-mens")
        names = [row["name"] for row in rows]
        self.assertEqual(names, ["Vêtements", "Chaussures", "Accessoires", "Soins"])
        self.assertNotIn("Chaussures (doublon)", names)
        self.assertTrue(all(row["url"].startswith(ORIGIN + "/catalog/") for row in rows))

    def test_children_exclude_current_category(self):
        rows = parse_children(MENU_HTML, ORIGIN, exclude="/catalog/5-mens")
        self.assertNotIn("5", [row["id"] for row in rows])

    def test_children_ignore_items_and_queries(self):
        rows = parse_children(MENU_HTML, ORIGIN)
        paths = [row["path"] for row in rows]
        self.assertFalse(any(path.startswith("/items") for path in paths))
        self.assertNotIn("/catalog", paths)

    def test_page_title(self):
        self.assertEqual(page_title(MENU_HTML), "Hommes")
        self.assertEqual(page_title("<html></html>"), "")

    def test_empty_html(self):
        self.assertEqual(parse_children("", ORIGIN), [])


class ProfileUrlTests(unittest.TestCase):
    def test_category_replaces_path_and_keeps_search(self):
        url = build_profile_url(
            "https://www.vinted.fr/catalog?search_text=nike%20air%20max",
            "/catalog/1231-men_shoes_new",
        )
        self.assertEqual(
            url,
            "https://www.vinted.fr/catalog/1231-men_shoes_new?search_text=nike+air+max",
        )

    def test_price_filters_are_preserved(self):
        url = build_profile_url(
            "https://www.vinted.fr/catalog?search_text=nike&price_from=20&price_to=80",
            "/catalog/5-mens",
        )
        self.assertIn("price_from=20", url)
        self.assertIn("price_to=80", url)
        self.assertIn("/catalog/5-mens?", url)

    def test_keyword_only_input_becomes_a_search(self):
        url = build_profile_url("air max 97", "/catalog/4332-sports")
        self.assertEqual(
            url, "https://www.vinted.fr/catalog/4332-sports?search_text=air+max+97"
        )

    def test_domain_is_kept(self):
        url = build_profile_url("https://www.vinted.de/catalog?search_text=nike", "/catalog/5")
        self.assertTrue(url.startswith("https://www.vinted.de/catalog/5"))

    def test_back_to_all_categories(self):
        url = build_profile_url(
            "https://www.vinted.fr/catalog/1231-men_shoes_new?search_text=nike", "/catalog"
        )
        self.assertEqual(url, "https://www.vinted.fr/catalog?search_text=nike")


class CategoryEndpointTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        config_path = root / "config.json"
        config_path.write_text(
            json.dumps({"engine": {"start_paused": True}}), encoding="utf-8"
        )
        self.state = AppState(
            config_path=config_path, db_path=root / "test.db", api_class=FakeVintedAPI
        )
        self.state.notifier.dry_run = True
        from app import api as api_module

        api_module._category_cache.clear()  # cache mémoire partagé entre tests
        self.client = TestClient(create_app(self.state))
        self.client.__enter__()
        self.calls: list[str] = []
        state = self.state
        original = state.client.get

        async def fake_get(url, **kwargs):
            self.calls.append(url)
            if url.endswith("/catalog/5-mens"):
                return HttpResponse(url=url, status=200, text=MENU_HTML)
            if "catalog/9999" in url:
                return HttpResponse(url=url, status=403, text="blocked", blocked=True)
            return HttpResponse(url=url, status=200, text="<html></html>")

        state.client.get = fake_get
        self.addCleanup(setattr, state.client, "get", original)

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()

    def test_root_is_local_and_offline(self):
        response = self.client.get("/api/categories")
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()
        self.assertEqual(data["source"], "local")
        self.assertEqual(data["path"], "/catalog")
        self.assertGreaterEqual(len(data["children"]), 8)
        self.assertEqual(self.calls, [], "aucune requête réseau pour le 1er niveau")

    def test_live_subcategories(self):
        response = self.client.get("/api/categories?path=/catalog/5-mens")
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()
        self.assertEqual(data["source"], "vinted")
        self.assertEqual(data["title"], "Hommes")
        self.assertEqual([row["name"] for row in data["children"]],
                         ["Vêtements", "Chaussures", "Accessoires", "Soins"])
        self.assertTrue(any("/catalog/5-mens" in url for url in self.calls))

    def test_cache_avoids_second_request(self):
        self.client.get("/api/categories?path=/catalog/5-mens")
        before = len(self.calls)
        second = self.client.get("/api/categories?path=/catalog/5-mens")
        self.assertTrue(second.json().get("cached"))
        self.assertEqual(len(self.calls), before)

    def test_invalid_domain_and_path(self):
        self.assertEqual(
            self.client.get("/api/categories?domain=evil.example").status_code, 422
        )
        self.assertEqual(
            self.client.get("/api/categories?path=../../etc/passwd").status_code, 422
        )

    def test_blocked_category(self):
        response = self.client.get("/api/categories?path=/catalog/9999")
        self.assertEqual(response.status_code, 503)

    def test_apply_category_to_existing_profile(self):
        profile = self.state.db.create_profile(
            {"name": "Sneakers", "url": "https://www.vinted.fr/catalog?search_text=nike"}
        )
        response = self.client.post(
            f"/api/profiles/{profile['id']}/category",
            json={"path": "/catalog/1231-men_shoes_new", "label": "Hommes › Chaussures"},
        )
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()["profile"]
        self.assertEqual(data["category"], "Hommes › Chaussures")
        self.assertEqual(
            data["url"],
            "https://www.vinted.fr/catalog/1231-men_shoes_new?search_text=nike",
        )

    def test_apply_invalid_category_to_profile(self):
        profile = self.state.db.create_profile({"name": "X", "url": "nike"})
        response = self.client.post(
            f"/api/profiles/{profile['id']}/category", json={"path": "/admin"}
        )
        self.assertEqual(response.status_code, 422)

    def test_profile_category_is_persisted(self):
        created = self.client.post(
            "/api/profiles",
            json={
                "name": "Chaussures homme",
                "url": "https://www.vinted.fr/catalog/1231-men_shoes_new?search_text=nike",
                "category": "Hommes › Chaussures",
            },
        )
        self.assertEqual(created.status_code, 200, created.text)
        self.assertEqual(created.json()["profile"]["category"], "Hommes › Chaussures")
        listed = self.client.get("/api/profiles").json()["profiles"]
        self.assertEqual(listed[-1]["category"], "Hommes › Chaussures")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
