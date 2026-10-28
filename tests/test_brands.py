"""Marques Vinted : parsing, URLs de profil, endpoints et filtre strict."""

from __future__ import annotations

import json
import tempfile
import time
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from app.brands import (
    MAX_BRANDS,
    brand_name_from_slug,
    brand_sitemaps,
    brands_from_sitemap,
    brand_ids_from_url,
    brand_labels,
    filter_brands,
    letter_of,
    parse_brand_ids,
    parse_brand_reference,
    parse_brands,
    parse_sitemap_locs,
    popular,
    sitemaps_from_robots,
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


class ReferenceTests(unittest.TestCase):
    def test_full_url(self):
        brand = parse_brand_reference("https://www.vinted.fr/brand/53-nike")
        self.assertEqual(brand, {"id": "53", "slug": "nike", "name": "Nike"})

    def test_path_only(self):
        self.assertEqual(
            parse_brand_reference("/brand/1775-new-balance")["name"], "New Balance"
        )

    def test_bare_id_and_slug(self):
        self.assertEqual(parse_brand_reference("53")["name"], "Nike")
        self.assertEqual(parse_brand_reference("15464124-brak")["name"], "Brak")

    def test_unknown_id(self):
        brand = parse_brand_reference("999999999")
        self.assertEqual(brand["id"], "999999999")
        self.assertTrue(brand["name"].startswith("Marque"))

    def test_refuses_garbage(self):
        for bad in ("", "Nike", "https://www.vinted.fr/catalog/5", "../brand/53"):
            self.assertIsNone(parse_brand_reference(bad), bad)


ROBOTS_TXT = """
User-agent: *
Disallow: /checkout
Sitemap: https://vinted.fr/sitemap-fr.xml
"""

SITEMAP_INDEX = """<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap><loc>https://www.vinted.fr/sitemaps/fr/pages.xml</loc></sitemap>
  <sitemap><loc>https://www.vinted.fr/sitemaps/fr/brands.xml</loc></sitemap>
  <sitemap><loc>https://www.vinted.fr/sitemaps/fr/brands1.xml</loc></sitemap>
  <sitemap><loc>https://www.vinted.fr/sitemaps/fr/items.xml</loc></sitemap>
</sitemapindex>
"""

BRANDS_SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.vinted.fr/brand/53-nike</loc><changefreq>weekly</changefreq></url>
  <url><loc>https://www.vinted.fr/brand/4745892-good-american-jeans</loc></url>
  <url><loc>https://www.vinted.fr/brand/15464124-brak</loc></url>
  <url><loc>https://www.vinted.fr/items/123456</loc></url>
</urlset>
"""

BRANDS_SITEMAP_2 = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.vinted.fr/brand/53-nike</loc></url>
  <url><loc>https://www.vinted.fr/brand/4784726-takt</loc></url>
</urlset>
"""


class SitemapTests(unittest.TestCase):
    def test_robots_sitemaps(self):
        self.assertEqual(sitemaps_from_robots(ROBOTS_TXT), ["https://vinted.fr/sitemap-fr.xml"])
        self.assertEqual(sitemaps_from_robots(""), [])

    def test_index_filtering(self):
        locs = parse_sitemap_locs(SITEMAP_INDEX)
        self.assertEqual(len(locs), 4)
        self.assertEqual(
            brand_sitemaps(locs),
            [
                "https://www.vinted.fr/sitemaps/fr/brands.xml",
                "https://www.vinted.fr/sitemaps/fr/brands1.xml",
            ],
        )

    def test_brands_from_sitemap(self):
        rows = brands_from_sitemap(BRANDS_SITEMAP)
        self.assertEqual([row["name"] for row in rows],
                         ["Nike", "Good American Jeans", "Brak"])
        self.assertEqual(rows[2]["id"], "15464124")
        # une annonce n'est pas une marque
        self.assertFalse(any("items" in row["slug"] for row in rows))

    def test_duplicates_are_removed(self):
        rows = brands_from_sitemap(BRANDS_SITEMAP_2)
        self.assertEqual([row["id"] for row in rows], ["53", "4784726"])

    def test_name_from_slug(self):
        self.assertEqual(brand_name_from_slug("good-american-jeans"), "Good American Jeans")
        self.assertEqual(brand_name_from_slug("nike-air"), "Nike Air")
        self.assertEqual(brand_name_from_slug("ginori-1735"), "Ginori 1735")
        self.assertEqual(brand_name_from_slug(""), "")

    def test_sitemap_with_no_brands(self):
        self.assertEqual(brands_from_sitemap("<urlset></urlset>"), [])
        self.assertEqual(brands_from_sitemap(""), [])


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

    def test_resolve_brand_from_url(self):
        data = self.client.get(
            "/api/brands/resolve", params={"ref": "https://www.vinted.fr/brand/53-nike"}
        )
        self.assertEqual(data.status_code, 200, data.text)
        self.assertEqual(data.json()["brand"], {"id": "53", "slug": "nike", "name": "Nike"})

    def test_resolve_brand_refuses_garbage(self):
        response = self.client.get("/api/brands/resolve", params={"ref": "/catalog/5"})
        self.assertEqual(response.status_code, 422)

    def test_resolved_brand_can_be_applied(self):
        brand = self.client.get(
            "/api/brands/resolve", params={"ref": "15464124-brak"}
        ).json()["brand"]
        profile = self.state.db.create_profile({"name": "Brak", "url": "nike"})
        data = self.client.post(
            f"/api/profiles/{profile['id']}/brands",
            json={"brand_ids": [brand["id"]], "names": {brand["id"]: brand["name"]}},
        ).json()["profile"]
        self.assertIn("brand_ids[]=15464124", data["url"])
        self.assertEqual(data["brands"], "Brak")

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


class BrandSyncTests(unittest.TestCase):
    """Import complet des marques depuis les sitemaps officiels."""

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

        self.api = api_module
        api_module._brand_cache.clear()
        api_module._brand_sync.update(
            running=False, started_at=None, finished_at=None, sitemaps=0,
            sitemaps_total=0, imported=0, error="", domain="",
        )
        self.calls: list[str] = []
        state = self.state
        original = state.client.get

        async def fake_get(url, **kwargs):
            self.calls.append(url)
            if url.endswith("/robots.txt"):
                return HttpResponse(url=url, status=200, text=ROBOTS_TXT)
            if url.endswith("/sitemap-fr.xml"):
                return HttpResponse(url=url, status=200, text=SITEMAP_INDEX)
            if url.endswith("/brands.xml"):
                return HttpResponse(url=url, status=200, text=BRANDS_SITEMAP)
            if url.endswith("/brands1.xml"):
                return HttpResponse(url=url, status=200, text=BRANDS_SITEMAP_2)
            return HttpResponse(url=url, status=404, text="")

        state.client.get = fake_get
        self.addCleanup(setattr, state.client, "get", original)
        self.client = TestClient(create_app(self.state))
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.client.close()
        self.tmp.cleanup()

    def _wait(self, timeout: float = 10.0) -> dict:
        deadline = time.time() + timeout
        while time.time() < deadline:
            data = self.client.get("/api/brands/sync").json()
            if not data["running"]:
                return data
            time.sleep(0.05)
        self.fail("synchronisation non terminée")

    def test_status_starts_empty(self):
        data = self.client.get("/api/brands/sync").json()
        self.assertFalse(data["running"])
        self.assertEqual(data["total"], 0)

    def test_full_import_and_search(self):
        started = self.client.post("/api/brands/sync").json()
        self.assertTrue(started["ok"])
        finished = self._wait()
        self.assertFalse(finished["running"])
        self.assertEqual(finished["total"], 4, finished)
        self.assertEqual(finished["imported"], 4)
        self.assertEqual(finished["error"], "")
        self.assertTrue(any("/sitemaps/fr/brands.xml" in url for url in self.calls))
        self.assertTrue(any("/sitemaps/fr/brands1.xml" in url for url in self.calls))

        # La recherche passe par l'index local, sans nouvelle requête réseau.
        before = len(self.calls)
        data = self.client.get("/api/brands?search=bra").json()
        self.assertEqual(data["source"], "index")
        self.assertEqual([row["name"] for row in data["brands"]], ["Brak"])
        self.assertEqual(data["total_indexed"], 4)
        self.assertEqual(len(self.calls), before)

    def test_search_is_accent_and_case_insensitive(self):
        self.client.post("/api/brands/sync")
        self._wait()
        self.assertEqual(self.client.get("/api/brands?search=NIKE").json()["brands"][0]["name"], "Nike")
        self.assertEqual(
            self.client.get("/api/brands?search=good%20american").json()["brands"][0]["id"],
            "4745892",
        )

    def test_second_sync_is_idempotent(self):
        self.client.post("/api/brands/sync")
        self._wait()
        self.client.post("/api/brands/sync")
        data = self._wait()
        self.assertEqual(data["total"], 4)

    def test_remote_failure_is_reported_without_crash(self):
        async def dead_get(url, **kwargs):
            self.calls.append(url)
            return HttpResponse(url=url, status=0, error="connexion refusée")

        self.state.client.get = dead_get
        self.client.post("/api/brands/sync")
        data = self._wait()
        self.assertFalse(data["running"])
        self.assertTrue(data["error"])
        self.assertEqual(self.client.get("/api/brands").json()["source"], "local")

    def test_indexed_brand_can_be_applied(self):
        self.client.post("/api/brands/sync")
        self._wait()
        profile = self.state.db.create_profile(
            {"name": "Brak only", "url": "https://www.vinted.fr/catalog?search_text=sac"}
        )
        data = self.client.post(
            f"/api/profiles/{profile['id']}/brands", json={"brand_ids": ["15464124"]}
        ).json()["profile"]
        self.assertIn("brand_ids[]=15464124", data["url"])
        self.assertEqual(data["brand_ids"], ["15464124"])


class CheckBrandTests(unittest.TestCase):
    """``--check --brand nike`` : diagnostic filtré sur une marque, sans réseau."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        config_path = root / "config.json"
        config_path.write_text(json.dumps({"engine": {"start_paused": True}}), encoding="utf-8")
        self.state = AppState(
            config_path=config_path, db_path=root / "test.db", api_class=FakeVintedAPI
        )
        from app.cli import _checked_query

        self.checked_query = staticmethod(_checked_query)

    def tearDown(self):
        self.state.db.close()
        self.tmp.cleanup()

    class _Args:
        domain = "www.vinted.fr"

        def __init__(self, check: str, brand: str = ""):
            self.check = check
            self.brand = brand

    def test_brand_name_from_known_list(self):
        url, label = self.checked_query(self.state, self._Args("chaussures", "nike"))
        self.assertIn("brand_ids[]=53", url)
        self.assertIn("search_text=chaussures", url)
        self.assertEqual(label, "Nike (#53)")

    def test_brand_by_id(self):
        url, label = self.checked_query(self.state, self._Args("chaussures", "53"))
        self.assertIn("brand_ids[]=53", url)
        self.assertEqual(label, "Nike (#53)")

    def test_brand_by_url(self):
        url, label = self.checked_query(
            self.state, self._Args("sneakers", "https://www.vinted.fr/brand/1775-new-balance")
        )
        self.assertIn("brand_ids[]=1775", url)
        self.assertEqual(label, "New Balance (#1775)")

    def test_brand_from_local_index(self):
        self.state.db.upsert_brands(
            [{"id": "15464124", "slug": "brak", "name": "Brak"}]
        )
        url, label = self.checked_query(self.state, self._Args("pull", "brak"))
        self.assertIn("brand_ids[]=15464124", url)
        self.assertEqual(label, "Brak (#15464124)")

    def test_unknown_brand_falls_back_without_filter(self):
        url, label = self.checked_query(self.state, self._Args("pull", "zzzz"))
        self.assertEqual(url, "pull")
        self.assertEqual(label, "")

    def test_no_brand_keeps_query(self):
        url, label = self.checked_query(self.state, self._Args("air max 97"))
        self.assertEqual(url, "air max 97")
        self.assertEqual(label, "")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()


class BrandPrefixTests(unittest.TestCase):
    """Autocomplétion : taper « n » doit proposer *toutes* les marques en N."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        config_path = root / "config.json"
        config_path.write_text(json.dumps({"engine": {"start_paused": True}}), encoding="utf-8")
        self.state = AppState(
            config_path=config_path, db_path=root / "test.db", api_class=FakeVintedAPI
        )
        self.state.db.upsert_brands(
            [
                {"id": "53", "slug": "nike", "name": "Nike"},
                {"id": "999", "slug": "nike-sb", "name": "Nike SB"},
                {"id": "1775", "slug": "new-balance", "name": "New Balance"},
                {"id": "121", "slug": "naked-wolfe", "name": "Naked Wolfe"},
                {"id": "77", "slug": "nina-ricci", "name": "Nina Ricci"},
                {"id": "14", "slug": "adidas", "name": "adidas"},
                {"id": "7", "slug": "h-m", "name": "H&M"},
            ]
        )
        self.client = TestClient(create_app(self.state))
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()

    def names(self, query: str) -> list[str]:
        response = self.client.get(f"/api/brands?search={query}&prefix=1")
        self.assertEqual(response.status_code, 200, response.text)
        return [row["name"] for row in response.json()["brands"]]

    def test_single_letter_returns_every_n_brand(self):
        names = self.names("n")
        # « adidas » et « H&M » ne doivent pas apparaître, tout le reste oui.
        self.assertEqual(sorted(names), sorted(["Naked Wolfe", "New Balance", "Nike", "Nike SB", "Nina Ricci"]))

    def test_two_letter_prefix(self):
        self.assertEqual(sorted(self.names("ni")), sorted(["Nike", "Nike SB", "Nina Ricci"]))

    def test_prefix_reports_total(self):
        data = self.client.get("/api/brands?search=n&prefix=1").json()
        self.assertEqual(data["source"], "index")
        self.assertTrue(data["prefix"])
        self.assertEqual(data["total"], 5)
        self.assertEqual(data["returned"], 5)

    def test_accent_insensitive_prefix(self):
        self.assertEqual(self.names("h"), ["H&M"])

    def test_prefix_without_letter_is_allowed(self):
        # Avant ce correctif, l'absence de lettre valait une erreur 422.
        self.assertEqual(self.client.get("/api/brands?search=h&prefix=1").status_code, 200)

    def test_non_prefix_search_still_works(self):
        response = self.client.get("/api/brands?search=balance")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("New Balance", [row["name"] for row in response.json()["brands"]])



class FiltersEndpointTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        config_path = root / "config.json"
        config_path.write_text(json.dumps({"engine": {"start_paused": True}}), encoding="utf-8")
        self.state = AppState(
            config_path=config_path, db_path=root / "test.db", api_class=FakeVintedAPI
        )
        self.client = TestClient(create_app(self.state))
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()

    def test_catalogue_endpoint(self):
        data = self.client.get("/api/filters").json()
        self.assertTrue(data["ok"])
        self.assertEqual(len(data["statuses"]), 6)
        self.assertEqual(len(data["colors"]), 12)
        self.assertGreaterEqual(data["counts"]["sizes"], 17)
        self.assertFalse(data["selected"]["active"])

    def test_catalogue_reads_existing_url(self):
        url = "https://www.vinted.fr/catalog?size_ids[]=206&status_ids[]=6&price_from=15"
        data = self.client.get("/api/filters", params={"url": url}).json()
        self.assertEqual(data["selected"]["size_ids"], ["206"])
        self.assertEqual(data["selected"]["status_ids"], ["6"])
        self.assertEqual(data["selected"]["price_from"], "15")

    def test_apply_endpoint(self):
        response = self.client.post(
            "/api/filters/apply",
            json={
                "url": "https://www.vinted.fr/catalog?search_text=nike",
                "size_ids": ["206"],
                "color_ids": ["1"],
                "price_to": 100,
            },
        )
        self.assertEqual(response.status_code, 200, response.text)
        url = response.json()["url"]
        self.assertIn("size_ids[]=206", url)
        self.assertIn("color_ids[]=1", url)
        self.assertIn("price_to=100", url)
        self.assertIn("search_text=nike", url)

    def test_apply_endpoint_rejects_bad_domain(self):
        response = self.client.post(
            "/api/filters/apply",
            json={"url": "https://example.com/catalog", "domain": "example.com"},
        )
        self.assertEqual(response.status_code, 422)
