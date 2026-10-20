"""Marques Vinted : parsing, URLs de profil, endpoints et filtre strict."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from app.brands import (
    MAX_BRANDS,
    brand_ids_from_url,
    brand_labels,
    filter_brands,
    letter_of,
    parse_brand_ids,
    parse_brands,
    popular,
    sanitize_letter,
)
from app.categories import build_profile_url
from app.http_client import HttpResponse
from app.state import AppState
from app.web import create_app
from tests.fake_vinted import FakeVintedAPI

ORIGIN = "https://www.vinted.fr"

#: Extrait réaliste de /brands/by_letter/N (marques + compteurs + doublons).
BRANDS_HTML = """
<html><body>
<h1>Marques connues - N</h1>
<div class="brands">
  <a href="/brand/53-nike"><span>Nike</span> <span>63 286 545 articles</span> <button>Suivre</button></a>
  <a href="/brand/1775-new-balance">New Balance</a>
  <a href="/brand/232-new-era" class="cell"><strong>New Era</strong></a>
  <a href="/brand/53-nike">Nike</a>
  <a href="/brand/5977-nike-air">Nike Air</a>
  <a href="/brands/by_letter/M">Voir tout</a>
  <a href="/catalog/1231-men_shoes_new">Chaussures</a>
</div>
</body></html>
"""


class ParseTests(unittest.TestCase):
    def test_real_page_is_parsed(self):
        rows = parse_brands(BRANDS_HTML, ORIGIN)
        names = [row["name"] for row in rows]
        self.assertEqual(names, ["Nike", "New Balance", "New Era", "Nike Air"])
        self.assertEqual(rows[0]["id"], "53")
        self.assertEqual(rows[0]["url"], f"{ORIGIN}/brand/53-nike")
        self.assertNotIn("63", rows[0]["name"], "les compteurs d'annonces sont retirés")

    def test_links_outside_brands_are_ignored(self):
        rows = parse_brands(BRANDS_HTML, ORIGIN)
        self.assertFalse(any("catalog" in row["url"] for row in rows))
        self.assertFalse(any(row["name"] == "Voir tout" for row in rows))

    def test_empty_html(self):
        self.assertEqual(parse_brands(""), [])

    def test_popular_are_unique_and_numeric(self):
        rows = popular()
        ids = [row["id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(brand_id.isdigit() for brand_id in ids))
        self.assertIn("53", ids)  # Nike
        self.assertIn("14", ids)  # adidas

    def test_letter_of_handles_accents(self):
        self.assertEqual(letter_of("Écusson"), "E")
        self.assertEqual(letter_of("nike"), "N")
        self.assertEqual(letter_of("  "), "")
        self.assertEqual(letter_of("3 Suisses"), "")

    def test_sanitize_letter(self):
        self.assertEqual(sanitize_letter("n"), "N")
        self.assertIsNone(sanitize_letter("1"))
        self.assertIsNone(sanitize_letter("AB"))

    def test_parse_brand_ids(self):
        self.assertEqual(parse_brand_ids(["53", "53", "x", "1775"]), ["53", "1775"])
        self.assertEqual(parse_brand_ids("53, 1775"), ["53", "1775"])
        self.assertEqual(len(parse_brand_ids([str(i) for i in range(60)])), MAX_BRANDS)
        self.assertEqual(parse_brand_ids(None), [])

    def test_brand_ids_from_url(self):
        url = "https://www.vinted.fr/catalog?catalog[]=1231&brand_ids[]=53&brand_ids[]=1775"
        self.assertEqual(brand_ids_from_url(url), ["53", "1775"])
        self.assertEqual(
            brand_ids_from_url("https://www.vinted.fr/catalog?brand_ids%5B%5D=9"), ["9"]
        )
        self.assertEqual(brand_ids_from_url("https://www.vinted.fr/catalog"), [])

    def test_filter_brands_ignores_accents_and_case(self):
        rows = parse_brands(BRANDS_HTML)
        self.assertEqual([row["id"] for row in filter_brands(rows, "new")], ["1775", "232"])
        self.assertEqual([row["id"] for row in filter_brands(rows, "NIKE")], ["53", "5977"])
        self.assertEqual(len(filter_brands(rows, "")), 4)

    def test_brand_labels(self):
        self.assertEqual(brand_labels(["53", "1775"]), "Nike, New Balance")
        self.assertEqual(brand_labels([], {}), "")
        self.assertEqual(brand_labels(["999"], {"999": "Marque maison"}), "Marque maison")


class ProfileUrlTests(unittest.TestCase):
    def test_brand_only_uses_query_style(self):
        url = build_profile_url(
            "https://www.vinted.fr/catalog?search_text=nike", None, ["53"]
        )
        self.assertEqual(
            url, "https://www.vinted.fr/catalog?brand_ids[]=53&search_text=nike"
        )

    def test_brand_and_category_are_combined(self):
        url = build_profile_url(
            "https://www.vinted.fr/catalog?search_text=nike", "/catalog/1231-men_shoes_new", ["53"]
        )
        self.assertEqual(
            url,
            "https://www.vinted.fr/catalog?catalog[]=1231&brand_ids[]=53&search_text=nike",
        )

    def test_price_is_preserved(self):
        url = build_profile_url(
            "https://www.vinted.fr/catalog?search_text=nike&price_from=20&price_to=80",
            "/catalog/5-mens",
            ["53", "1775"],
        )
        self.assertIn("price_from=20", url)
        self.assertIn("price_to=80", url)
        self.assertIn("brand_ids[]=1775", url)

    def test_clearing_brands_returns_to_path_style(self):
        url = build_profile_url(
            "https://www.vinted.fr/catalog?catalog[]=1231&brand_ids[]=53&search_text=nike",
            None,
            [],
        )
        self.assertEqual(url, "https://www.vinted.fr/catalog/1231?search_text=nike")

    def test_category_change_keeps_existing_brands(self):
        url = build_profile_url(
            "https://www.vinted.fr/catalog?catalog[]=1231&brand_ids[]=53&search_text=nike",
            "/catalog/1242-men_sneakers",
        )
        self.assertIn("catalog[]=1242", url)
        self.assertIn("brand_ids[]=53", url)

    def test_keyword_only_profile(self):
        url = build_profile_url("air max 97", None, ["53"])
        self.assertEqual(
            url, "https://www.vinted.fr/catalog?brand_ids[]=53&search_text=air+max+97"
        )


class BrandEndpointTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        config_path = root / "config.json"
        config_path.write_text(json.dumps({"engine": {"start_paused": True}}), encoding="utf-8")
        self.state = AppState(
            config_path=config_path, db_path=root / "test.db", api_class=FakeVintedAPI
        )
        self.state.notifier.dry_run = True
        from app import api as api_module

        api_module._brand_cache.clear()
        self.client = TestClient(create_app(self.state))
        self.client.__enter__()
        self.calls: list[str] = []
        state = self.state
        original = state.client.get

        async def fake_get(url, **kwargs):
            self.calls.append(url)
            if "by_letter/X" in url:
                return HttpResponse(url=url, status=403, text="blocked", blocked=True)
            if "/brands/by_letter/" in url:
                return HttpResponse(url=url, status=200, text=BRANDS_HTML)
            return HttpResponse(url=url, status=200, text="<html></html>")

        state.client.get = fake_get
        self.addCleanup(setattr, state.client, "get", original)

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()

    def test_default_is_local_and_offline(self):
        response = self.client.get("/api/brands")
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()
        self.assertEqual(data["source"], "local")
        self.assertGreaterEqual(len(data["brands"]), 20)
        self.assertEqual(len(data["letters"]), 26)
        self.assertEqual(self.calls, [], "aucune requête réseau pour le raccourci")

    def test_letter_lists_real_brands(self):
        response = self.client.get("/api/brands?letter=n")
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()
        self.assertEqual(data["source"], "vinted")
        self.assertEqual(data["letter"], "N")
        self.assertEqual([row["name"] for row in data["brands"]],
                         ["Nike", "New Balance", "New Era", "Nike Air"])
        self.assertTrue(any("/brands/by_letter/N" in url for url in self.calls))

    def test_search_filters_within_letter(self):
        data = self.client.get("/api/brands?search=new").json()
        self.assertEqual(data["letter"], "N")
        self.assertEqual([row["name"] for row in data["brands"]], ["New Balance", "New Era"])

    def test_cache_is_used(self):
        self.client.get("/api/brands?letter=N")
        before = len(self.calls)
        second = self.client.get("/api/brands?letter=N").json()
        self.assertTrue(second["cached"])
        self.assertEqual(len(self.calls), before)

    def test_bad_inputs(self):
        self.assertEqual(self.client.get("/api/brands?domain=evil.example").status_code, 422)
        self.assertEqual(self.client.get("/api/brands?letter=1").status_code, 422)
        self.assertEqual(self.client.get("/api/brands?search=123").status_code, 422)

    def test_blocked_is_reported(self):
        response = self.client.get("/api/brands?letter=X")
        self.assertEqual(response.status_code, 503)

    def test_apply_brands_to_profile(self):
        profile = self.state.db.create_profile(
            {
                "name": "Sneakers",
                "url": "https://www.vinted.fr/catalog/1231-men_shoes_new?search_text=nike",
            }
        )
        response = self.client.post(
            f"/api/profiles/{profile['id']}/brands",
            json={"brand_ids": ["53", "1775"]},
        )
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()["profile"]
        self.assertEqual(data["brands"], "Nike, New Balance")
        self.assertEqual(data["brand_ids"], ["53", "1775"])
        self.assertIn("brand_ids[]=53", data["url"])
        self.assertIn("catalog[]=1231", data["url"])
        self.assertIn("search_text=nike", data["url"])

    def test_clear_brands(self):
        profile = self.state.db.create_profile(
            {
                "name": "Sneakers",
                "url": "https://www.vinted.fr/catalog?catalog[]=1231&brand_ids[]=53&search_text=nike",
            }
        )
        data = self.client.post(
            f"/api/profiles/{profile['id']}/brands", json={"brand_ids": []}
        ).json()["profile"]
        self.assertEqual(data["brands"], "")
        self.assertEqual(data["brand_ids"], [])
        self.assertNotIn("brand_ids", data["url"])
        self.assertIn("/catalog/1231", data["url"])

    def test_invalid_brand_ids(self):
        profile = self.state.db.create_profile({"name": "X", "url": "nike"})
        response = self.client.post(
            f"/api/profiles/{profile['id']}/brands", json={"brand_ids": ["abc"]}
        )
        self.assertEqual(response.status_code, 422)

    def test_profile_stores_brand_label(self):
        created = self.client.post(
            "/api/profiles",
            json={
                "name": "Nike only",
                "url": "https://www.vinted.fr/catalog?brand_ids[]=53&search_text=nike",
                "brands": "Nike",
            },
        )
        self.assertEqual(created.status_code, 200, created.text)
        profile = created.json()["profile"]
        self.assertEqual(profile["brands"], "Nike")
        self.assertEqual(profile["brand_ids"], ["53"])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
