"""Tests du pack de marques : export, import, amorçage et endpoint.

Enjeu : le bot doit pouvoir démarrer avec les ~57 000 marques **sans réseau**
(fichier livré), et savoir les **exporter** pour les donner à un autre outil.
"""

from __future__ import annotations

import csv
import io
import json
import tempfile
import unittest
from pathlib import Path

from app.brand_pack import (
    find_brand_file,
    read_brand_file,
    seed_database,
    write_brand_files,
)
from app.database import Database

SAMPLE = [
    {"id": "53", "slug": "nike", "name": "Nike"},
    {"id": "7", "slug": "h-m", "name": "H&M"},
    {"id": "1195", "slug": "levis", "name": "Levi's"},
    {"id": "364", "slug": "zara", "name": "Zara"},
]


class BrandFileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)

    def test_csv_and_json_round_trip(self):
        report = write_brand_files(SAMPLE, self.root / "marques-vinted")
        self.assertEqual(report["rows"], 4)
        csv_rows = read_brand_file(report["csv"])
        json_rows = read_brand_file(report["json"])
        self.assertEqual(csv_rows, json_rows)
        self.assertEqual({row["id"] for row in csv_rows}, {"53", "7", "1195", "364"})
        # Trié par nom : la liste reste lisible à l'œil nu.
        self.assertEqual(csv_rows[0]["name"], "H&M")

    def test_csv_without_header_is_accepted(self):
        path = self.root / "sans-entete.csv"
        path.write_text("53,nike,Nike\n7,h-m,H&M\n", encoding="utf-8")
        rows = read_brand_file(path)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["id"], "53")
        self.assertEqual(rows[0]["name"], "Nike")

    def test_foreign_csv_with_quotes_bom_and_bad_ids(self):
        path = self.root / "externe.csv"
        path.write_text(
            '\ufeffname,id,slug\n"Nike, Inc.",53,nike\nZara,364,zara\nSans id,,x\n',
            encoding="utf-8",
        )
        rows = read_brand_file(path)
        names = {row["id"]: row["name"] for row in rows}
        self.assertEqual(names["53"], "Nike, Inc.")  # virgule protégée par les guillemets
        self.assertNotIn("", names)

    def test_json_list_of_pairs_is_accepted(self):
        path = self.root / "pairs.json"
        path.write_text(json.dumps([["53", "nike", "Nike"]]), encoding="utf-8")
        self.assertEqual(read_brand_file(path)[0]["name"], "Nike")

    def test_missing_name_falls_back_to_slug(self):
        path = self.root / "partiel.csv"
        path.write_text("id,slug,name\n900,air-jordan,\n", encoding="utf-8")
        self.assertEqual(read_brand_file(path)[0]["name"], "air-jordan")


class SeedTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.db = Database(self.root / "test.db")
        self.addCleanup(self.tmp.cleanup)
        self.addCleanup(self.db.close)

    def test_seed_fills_an_empty_database(self):
        write_brand_files(SAMPLE, self.root / "brands")
        report = seed_database(self.db, self.root / "brands.csv")
        self.assertEqual(report["imported"], 4)
        self.assertEqual(report["total"], 4)
        found = self.db.search_brands("nik", prefix=True)
        self.assertEqual(found[0]["name"], "Nike")

    def test_seed_never_overwrites_an_existing_index(self):
        """Un index récupéré en ligne est plus frais qu'un fichier livré."""
        self.db.upsert_brands(SAMPLE[:1])
        write_brand_files(SAMPLE, self.root / "brands")
        report = seed_database(self.db, self.root / "brands.csv")
        self.assertTrue(report["skipped"])
        self.assertEqual(report["total"], 1)

    def test_seed_is_noop_without_file(self):
        report = seed_database(self.db, self.root / "absent.csv")
        self.assertEqual(report["imported"], 0)

    def test_known_filenames_are_discovered(self):
        write_brand_files(SAMPLE[:2], self.root / "marques")
        found = find_brand_file([self.root])
        self.assertIsNotNone(found)
        self.assertIn(found.name, {"marques.csv", "marques.json"})


class ExportEndpointTests(unittest.TestCase):
    """GET /api/brands/export : le fichier téléchargeable depuis le dashboard."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        config_path = root / "config.json"
        config_path.write_text(json.dumps({"engine": {"start_paused": True}}), encoding="utf-8")
        from fastapi.testclient import TestClient

        from app.state import AppState
        from app.web import create_app

        self.state = AppState(config_path=config_path, db_path=root / "test.db")
        self.client = TestClient(create_app(self.state))
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()

    def test_export_returns_a_downloadable_csv(self):
        self.state.db.upsert_brands(SAMPLE)
        response = self.client.get("/api/brands/export")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/csv", response.headers["content-type"])
        self.assertIn("marques-vinted.csv", response.headers["content-disposition"])
        rows = list(csv.reader(io.StringIO(response.text)))
        self.assertEqual(rows[0], ["id", "slug", "name"])
        self.assertEqual(len(rows), 1 + len(SAMPLE))
        self.assertIn("Nike", [cell for row in rows for cell in row])

    def test_export_without_index_is_a_clear_404(self):
        response = self.client.get("/api/brands/export")
        self.assertEqual(response.status_code, 404)
        self.assertIn("import", response.json()["detail"].lower())


if __name__ == "__main__":
    unittest.main()
