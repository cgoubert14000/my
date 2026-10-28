"""Catalogue de filtres vérifié + construction d'URL (aucun réseau)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.vinted_filters import (  # noqa: E402
    COLORS,
    SIZE_GROUPS,
    STATUSES,
    apply_filters,
    catalogue,
    describe,
    normalize_size_selection,
    read_filters,
)


class CatalogueTests(unittest.TestCase):
    def test_catalogue_is_complete(self):
        data = catalogue()
        self.assertEqual(len(data["statuses"]), 6)
        self.assertEqual(len(data["colors"]), 12)
        self.assertGreaterEqual(len(data["size_groups"]), 3)
        self.assertEqual(data["counts"]["sizes"], sum(len(g["sizes"]) for g in data["size_groups"]))
        self.assertTrue(data["orders"])

    def test_verified_identifiers(self):
        statuses = dict(STATUSES)
        self.assertEqual(statuses["6"], "Neuf avec étiquette")
        self.assertEqual(statuses["4"], "Satisfaisant")
        colors = dict(COLORS)
        self.assertEqual(colors["1"], "Noir")
        self.assertEqual(colors["12"], "Blanc")
        groups = {group["key"]: dict(group["sizes"]) for group in SIZE_GROUPS}
        letters = groups["letters"]
        # Correspondance lue sur vinted.fr (la page réaffiche les filtres appliqués).
        self.assertEqual(letters["205"], "XS")
        self.assertEqual(letters["207"], "M")
        self.assertEqual(letters["209"], "L")
        self.assertEqual(letters["212"], "XXXL")
        self.assertEqual(letters["213"], "Taille unique")
        self.assertNotIn("208", letters)  # identifiant ignoré par Vinted
        shoes = groups["shoes"]
        self.assertEqual(shoes["55"], "35")
        self.assertEqual(shoes["63"], "43")
        self.assertEqual(len(shoes), 9)
        # Bloc « XS / 34 / 6 » relevé sur vinted.fr (size_ids[]=1 … 6).
        eu = groups["eu"]
        self.assertEqual(eu["1"], "XS / 34 / 6")
        self.assertEqual(eu["6"], "XXL / 44 / 16")

    def test_no_duplicate_size_ids(self):
        ids = [size_id for group in SIZE_GROUPS for size_id, _ in group["sizes"]]
        self.assertEqual(len(ids), len(set(ids)))


class ApplyFiltersTests(unittest.TestCase):
    def test_keyword_only_keeps_path_form(self):
        url = "https://www.vinted.fr/catalog?search_text=nike"
        self.assertEqual(apply_filters(url), url)

    def test_sizes_and_status_build_param_form(self):
        url = apply_filters(
            "https://www.vinted.fr/catalog?search_text=nike",
            size_ids=["206", "207"],
            status_ids=["6", "2"],
        )
        self.assertTrue(url.startswith("https://www.vinted.fr/catalog?"))
        self.assertIn("size_ids[]=206", url)
        self.assertIn("size_ids[]=207", url)
        self.assertIn("status_ids[]=6", url)
        self.assertIn("status_ids[]=2", url)
        self.assertIn("search_text=nike", url)

    def test_price_and_order(self):
        url = apply_filters(
            "https://www.vinted.fr/catalog?search_text=nike",
            price_from="20",
            price_to="90,5",
            order="price_low_to_high",
        )
        self.assertIn("price_from=20", url)
        self.assertIn("price_to=90.5", url)
        self.assertIn("order=price_low_to_high", url)

    def test_brand_and_category_use_catalog_param(self):
        url = apply_filters(
            "https://www.vinted.fr/catalog/1231-men_shoes_new?brand_ids[]=53",
            size_ids=["63"],
            color_ids=["1"],
        )
        self.assertIn("catalog[]=1231", url)
        self.assertIn("brand_ids[]=53", url)
        self.assertIn("size_ids[]=63", url)
        self.assertIn("color_ids[]=1", url)
        self.assertNotIn("/catalog/1231", url)

    def test_filters_are_replaced_not_duplicated(self):
        first = apply_filters(
            "https://www.vinted.fr/catalog?search_text=nike", size_ids=["206"]
        )
        second = apply_filters(first, size_ids=["210"])
        self.assertNotIn("size_ids[]=206", second)
        self.assertEqual(second.count("size_ids[]=210"), 1)

    def test_invalid_values_are_dropped(self):
        url = apply_filters(
            "https://www.vinted.fr/catalog?search_text=nike",
            size_ids=["206", "abc", "../1"],
            order="n_importe_quoi",
        )
        self.assertIn("size_ids[]=206", url)
        self.assertNotIn("abc", url)
        self.assertNotIn("order=", url)

    def test_unknown_host_falls_back(self):
        url = apply_filters("https://evil.example/catalog?search_text=nike", size_ids=["206"])
        self.assertTrue(url.startswith("https://www.vinted.fr/"), url)


class ReadFiltersTests(unittest.TestCase):
    def test_roundtrip(self):
        url = apply_filters(
            "https://www.vinted.fr/catalog?search_text=nike",
            size_ids=["206", "210"],
            status_ids=["6"],
            color_ids=["1", "9"],
            price_from="10",
            price_to="80",
            order="newest_first",
        )
        selected = read_filters(url)
        self.assertEqual(selected["size_ids"], ["206", "210"])
        self.assertEqual(selected["status_ids"], ["6"])
        self.assertEqual(selected["color_ids"], ["1", "9"])
        self.assertEqual(selected["price_from"], "10")
        self.assertEqual(selected["price_to"], "80")
        self.assertEqual(selected["order"], "newest_first")
        self.assertTrue(selected["active"])

    def test_empty_url(self):
        selected = read_filters("")
        self.assertFalse(selected["active"])
        self.assertEqual(selected["size_ids"], [])

    def test_aliases_without_brackets(self):
        selected = read_filters("https://www.vinted.fr/catalog?size_ids=206&status_ids=6")
        self.assertEqual(selected["size_ids"], ["206"])
        self.assertEqual(selected["status_ids"], ["6"])


class HelperTests(unittest.TestCase):
    def test_normalize_size_selection(self):
        self.assertEqual(normalize_size_selection(["206", "999", "206"]), ["206"])

    def test_describe(self):
        self.assertEqual(describe(["206", "63"]), "S, 43")


if __name__ == "__main__":
    unittest.main()
