"""Tests du parseur SSR Vinted (structure réelle de septembre 2026).

Les fixtures reproduisent le balisage rendu par Vinted : cartes
``data-testid="grid-item"``, attributs ``title``/``alt`` compacts, payload RSC
``self.__next_f.push``, page article avec OpenGraph.
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import vinted_api  # noqa: E402
from app.vinted_api import (  # noqa: E402
    extract_rsc_text,
    items_from_rsc,
    parse_catalog_html,
    parse_item_page,
)

ORIGIN = "https://www.vinted.fr"

FR_CARD = """
<div data-testid="grid-item" class="Grid-module__feed-grid__item">
  <div class="ItemBox-module__new-item-box__container"
       data-testid="product-item-id-10458643821">
    <div data-testid="product-item-id-10458643821--image">
      <img src="https://images1.vinted.net/t/05_00229_wrFzqFEJATFait1RnAYE69Wm/310x430/3655c9a7.webp?s=47a9"
           alt="Nike grey hoodie, Marque: Nike, État: Bon état, Taille: S, 8.00 €, 9.10 €"
           data-testid="product-item-id-10458643821--image--img"/>
    </div>
    <a href="/items/10458643821-nike-grey-hoodie?referrer=catalog"
       title="Nike grey hoodie, Marque: Nike, État: Bon état, Taille: S, 8.00 €, 9.10 €"
       data-testid="product-item-id-10458643821--overlay-link"><div></div></a>
    <button aria-label="Add to favorites, favorited by 5 users"
            data-testid="product-item-id-10458643821--favourite">
      <span data-testid="favourite-count-text">5</span>
    </button>
    <div data-testid="product-item-id-10458643821--summary">
      <div data-testid="product-item-id-10458643821--description">
        <div data-testid="product-item-id-10458643821--description--content">
          <div>Nike</div><div>S · Bon état</div>
        </div>
      </div>
      <div data-testid="product-item-id-10458643821--price-text">8,00 €</div>
      <div data-testid="product-item-id-10458643821--total-price">9,10 € incl.</div>
    </div>
  </div>
</div>
"""

EN_CARD = """
<div data-testid="grid-item" class="Grid-module__feed-grid__item">
  <div data-testid="product-item-id-10286865039">
    <img src="https://images1.vinted.net/t/02_00b5c_WNqVmcxbUVAd1LiejYepiAU3/310x430/3b96bb55.webp?s=d06f"
         alt="Vintage ceramic woven tray, Condition: Very good, 4.00 $, 4.90 $"/>
    <a href="/items/10286865039-vintage-ceramic-woven-tray?referrer=catalog"
       title="Vintage ceramic woven tray, Condition: Very good, 4.00 $, 4.90 $"></a>
    <span data-testid="product-item-id-10286865039--price-text">4.00 $</span>
  </div>
</div>
"""

CATALOG_HTML = f"""<!doctype html><html><head><title>Articles | Vinted</title></head>
<body><main><h1>Articles</h1><p>500+ resultats.</p>
<div class="feed-grid">{FR_CARD}{EN_CARD}</div>
</main></body></html>"""


class CatalogParsingTests(unittest.TestCase):
    def test_parses_real_card_structure(self):
        items = parse_catalog_html(CATALOG_HTML, ORIGIN, "EUR")
        self.assertEqual(len(items), 2)
        first = items[0]
        self.assertEqual(first["id"], "10458643821")
        self.assertEqual(first["title"], "Nike grey hoodie")
        self.assertEqual(first["price"], 8.0)
        self.assertEqual(first["total_price"], 9.1)
        self.assertEqual(first["currency"], "EUR")
        self.assertEqual(first["brand"], "Nike")
        self.assertEqual(first["size"], "S")
        self.assertEqual(first["condition"], "Bon état")
        self.assertEqual(first["url"], f"{ORIGIN}/items/10458643821-nike-grey-hoodie")
        self.assertTrue(first["image_url"].startswith("https://images1.vinted.net/"))
        self.assertEqual(first["favourites"], 5)

        second = items[1]
        self.assertEqual(second["id"], "10286865039")
        self.assertEqual(second["title"], "Vintage ceramic woven tray")
        self.assertEqual(second["condition"], "Very good")
        self.assertEqual(second["currency"], "USD")
        self.assertEqual(
            second["url"], f"{ORIGIN}/items/10286865039-vintage-ceramic-woven-tray"
        )

    def test_regex_fallback_without_bs4(self):
        original = vinted_api.BeautifulSoup
        vinted_api.BeautifulSoup = None
        try:
            items = parse_catalog_html(CATALOG_HTML, ORIGIN, "EUR")
        finally:
            vinted_api.BeautifulSoup = original
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]["id"], "10458643821")
        self.assertEqual(items[0]["price"], 8.0)

    def test_dedupe_and_ignore_broken_cards(self):
        html = (
            CATALOG_HTML
            + '<div data-testid="grid-item"><div>sans identifiant</div></div>'
        )
        items = parse_catalog_html(html, ORIGIN, "EUR")
        self.assertEqual(len(items), 2)
        self.assertEqual(len({item["id"] for item in items}), 2)

    def test_anchor_fallback_when_structure_changes(self):
        html = (
            '<html><body><a href="/catalog/5-men">Hommes</a>'
            '<a href="/items/777-sac-cuir?referrer=catalog" '
            'title="Sac cuir, Marque: Longchamp, État: Très bon état, Taille: M, 145.00 €, 150.00 €">'
            '<img src="https://images1.vinted.net/t/77/f800/a.webp?s=1" alt=""></a>'
            "</body></html>"
        )
        items = parse_catalog_html(html, ORIGIN, "EUR")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["id"], "777")
        self.assertEqual(items[0]["price"], 145.0)
        self.assertEqual(items[0]["brand"], "Longchamp")

    def test_empty_page(self):
        items = parse_catalog_html("<html>Aucun résultat</html>", ORIGIN, "EUR")
        self.assertEqual(items, [])


RSC_HTML = (
    '<html><body><script>self.__next_f.push([1,"{\\"items\\":['
    '{\\"id\\":42,\\"title\\":\\"Sac Longchamp\\",\\"price\\":{\\"amount\\":\\"145.0\\",'
    '\\"currency_code\\":\\"EUR\\"},\\"brand_title\\":\\"Longchamp\\",'
    '\\"url\\":\\"/items/42-sac\\",\\"user\\":{\\"id\\":7,\\"login\\":\\"claire\\",'
    '\\"feedback_reputation\\":0.9,\\"feedback_count\\":42}}]}"])</script></body></html>'
)


class RscParsingTests(unittest.TestCase):
    def test_extract_rsc_text(self):
        text = extract_rsc_text(RSC_HTML)
        self.assertIn('"items"', text)
        self.assertIn("Sac Longchamp", text)

    def test_items_from_rsc(self):
        items = items_from_rsc(RSC_HTML, ORIGIN, "EUR")
        self.assertEqual(len(items), 1)
        item = items[0]
        self.assertEqual(item["id"], "42")
        self.assertEqual(item["price"], 145.0)
        self.assertEqual(item["seller_name"], "claire")
        self.assertEqual(item["seller_rating"], 4.5)
        self.assertEqual(item["seller_feedback"], 42)

    def test_catalog_falls_back_to_rsc(self):
        items = parse_catalog_html(RSC_HTML, ORIGIN, "EUR")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Sac Longchamp")


ITEM_PAYLOAD = {
    "itemDto": {
        "id": 10458643821,
        "description": "Sweat Nike gris taille S, porté deux fois, aucune tache ni défaut.",
        "user": {
            "id": 170944517,
            "login": "vendeur_test",
            "feedback_reputation": 0.96,
            "feedback_count": 132,
        },
    }
}

ITEM_PAGE = (
    "<!doctype html><html><head>"
    '<meta property="og:title" content="Nike grey hoodie | Vinted">'
    '<meta property="og:image" content="https://images1.vinted.net/t/05_00229_wrFzq/f800/3655c9a7.webp?s=6a53">'
    '<meta property="og:description" content="Hoodie Nike gris, porté deux fois.">'
    "</head><body>"
    '<a href="/admin_alert/new?ref_id=10458643821&ref_type=item&offender_id=170944517">Signaler</a>'
    "<script>self.__next_f.push([1,"
    + json.dumps(json.dumps(ITEM_PAYLOAD))
    + "])</script></body></html>"
)


class ItemPageTests(unittest.TestCase):
    def setUp(self):
        self.item = parse_catalog_html(CATALOG_HTML, ORIGIN, "EUR")[0]

    def test_enrich_description_seller_and_hd_photo(self):
        enriched = parse_item_page(ITEM_PAGE, self.item, ORIGIN)
        self.assertIn("porté deux fois", enriched["description"])
        self.assertEqual(enriched["seller_id"], "170944517")
        self.assertEqual(enriched["seller_name"], "vendeur_test")
        self.assertEqual(enriched["seller_rating"], 4.8)
        self.assertEqual(enriched["seller_feedback"], 132)
        self.assertEqual(enriched["seller_url"], f"{ORIGIN}/member/170944517")
        self.assertTrue(enriched["image_url"].startswith("https://images1.vinted.net/"))

    def test_blacklist_can_use_enriched_description(self):
        from app.filters import matches_profile

        profile = {
            "name": "P",
            "min_price": None,
            "max_price": None,
            "whitelist": [],
            "blacklist": ["defaut"],
            "keyword_mode": "any",
            "check_description": True,
            "min_seller_rating": None,
            "min_seller_feedback": None,
        }
        enriched = parse_item_page(ITEM_PAGE, self.item, ORIGIN)
        self.assertFalse(matches_profile(profile, enriched).matched)


if __name__ == "__main__":
    unittest.main()
