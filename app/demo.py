"""Mode démonstration : données fictives pour tester l'UI hors-ligne.

Activé par ``python main.py --demo``. Aucune requête n'est envoyée à Vinted et
aucune alerte réelle n'est postée sur Discord : les embeds sont seulement
journalisés. Pratique pour découvrir le dashboard, régler ses filtres et faire
une démo.
"""

from __future__ import annotations

import asyncio
import itertools

from .utils import origin_of
from .vinted_api import DEFAULT_DOMAIN, SearchPage, VintedAPI

DEMO_ITEMS: list[dict] = [
    {
        "id": "9000001",
        "title": "Nike Air Max 97 Silver Bullet — Taille 42",
        "price": 89.0,
        "brand": "Nike",
        "size": "42",
        "condition": "Très bon état",
        "description": "Portées deux fois, semelles impeccables. Boîte d'origine incluse.",
        "seller_name": "maxime_snk",
        "seller_id": "551001",
        "seller_rating": 4.9,
        "seller_feedback": 187,
        "favourites": 34,
    },
    {
        "id": "9000002",
        "title": "Sac à main Longchamp Le Pliage cuir — Noir",
        "price": 145.0,
        "brand": "Longchamp",
        "size": "M",
        "condition": "Neuf avec étiquette",
        "description": "Jamais porté, étiquette encore attachée. Acheté en boutique.",
        "seller_name": "claire.vnt",
        "seller_id": "551002",
        "seller_rating": 5.0,
        "seller_feedback": 42,
        "favourites": 12,
    },
    {
        "id": "9000003",
        "title": "Manteau en laine Max Mara — Camel — 38",
        "price": 240.0,
        "brand": "Max Mara",
        "size": "38",
        "condition": "Très bon état",
        "description": "Manteau 100 % laine vierge, porté une saison. Pièce impeccable, entretien soigné.",
        "seller_name": "luxe_pieces",
        "seller_id": "551003",
        "seller_rating": 4.8,
        "seller_feedback": 96,
        "favourites": 58,
    },
    {
        "id": "9000004",
        "title": "Adidas Samba OG — Blanc/Noir — 41 1/3",
        "price": 65.0,
        "brand": "adidas",
        "size": "41 1/3",
        "condition": "Bon état",
        "description": "Quelques traces d'usure normales sur les semelles, très propres.",
        "seller_name": "sneakers_addict",
        "seller_id": "551004",
        "seller_rating": 4.6,
        "seller_feedback": 312,
        "favourites": 21,
    },
    {
        "id": "9000005",
        "title": "Ralph Lauren Polo Player — Chemise oxford bleue L",
        "price": 28.0,
        "brand": "Ralph Lauren",
        "size": "L",
        "condition": "Très bon état",
        "description": "Chemise en oxford, coupe droite. Aucun accroc.",
        "seller_name": "vintage_marie",
        "seller_id": "551005",
        "seller_rating": 4.4,
        "seller_feedback": 58,
        "favourites": 7,
    },
    {
        "id": "9000006",
        "title": "Sweat Stone Island crewneck — Gris — M",
        "price": 175.0,
        "brand": "Stone Island",
        "size": "M",
        "condition": "Très bon état",
        "description": "Sweat authentique, badge intact. Facture fournie.",
        "seller_name": "archivio_io",
        "seller_id": "551006",
        "seller_rating": 5.0,
        "seller_feedback": 23,
        "favourites": 45,
    },
    # ── Annonces volontairement peu fiables (la blacklist doit les écarter) ──
    {
        "id": "9000007",
        "title": "Nike Air Max 97 — copie qualité AAA",
        "price": 35.0,
        "brand": "Nike",
        "size": "43",
        "condition": "Neuf",
        "description": "Réplique très proche de l'original. Prix imbattable.",
        "seller_name": "deal.toxico",
        "seller_id": "551007",
        "seller_rating": 3.2,
        "seller_feedback": 6,
        "favourites": 2,
    },
    {
        "id": "9000008",
        "title": "Sac Longchamp — défaut fermeture éclair",
        "price": 55.0,
        "brand": "Longchamp",
        "size": "L",
        "condition": "Satisfaisant",
        "description": "Le zip est cassé et il y a une tache sur le fond. Vendu en l'état.",
        "seller_name": "videgrenier_59",
        "seller_id": "551008",
        "seller_rating": 3.9,
        "seller_feedback": 14,
        "favourites": 1,
    },
    {
        "id": "9000009",
        "title": "Manteau Max Mara — taché au niveau du col",
        "price": 60.0,
        "brand": "Max Mara",
        "size": "40",
        "condition": "Satisfaisant",
        "description": "Tache visible sur le col, nettoyage à prévoir. Sinon superbe pièce.",
        "seller_name": "petit.prix",
        "seller_id": "551009",
        "seller_rating": 4.0,
        "seller_feedback": 9,
        "favourites": 3,
    },
    # ── Vendeurs douteux (seuils de réputation) ────────────────────────────
    {
        "id": "9000010",
        "title": "Air Jordan 1 Low — University Blue — 44",
        "price": 130.0,
        "brand": "Jordan",
        "size": "44",
        "condition": "Très bon état",
        "description": "Très bon état général, boîte incluse.",
        "seller_name": "new_account_2026",
        "seller_id": "551010",
        "seller_rating": 2.5,
        "seller_feedback": 2,
        "favourites": 11,
    },
    {
        "id": "9000011",
        "title": "Sac Gucci Marmont mini — Cuir rouge",
        "price": 180.0,
        "brand": "Gucci",
        "size": "Taille unique",
        "condition": "Bon état",
        "description": "Authentique, dustbag fourni. Légères marques sur le cuir, très belle pièce.",
        "seller_name": "ella.lux",
        "seller_id": "551011",
        "seller_rating": 4.7,
        "seller_feedback": 64,
        "favourites": 77,
    },
    {
        "id": "9000012",
        "title": "Doudoune Moncler Maya — Noir — 2",
        "price": 450.0,
        "brand": "Moncler",
        "size": "2",
        "condition": "Très bon état",
        "description": "Doudoune portée une saison, duvet gonflant, aucune réparation.",
        "seller_name": "ski_shop_grenoble",
        "seller_id": "551012",
        "seller_rating": 4.9,
        "seller_feedback": 203,
        "favourites": 91,
    },
    {
        "id": "9000013",
        "title": "New Balance 550 — Blanc/Vert — 39",
        "price": 72.0,
        "brand": "New Balance",
        "size": "39",
        "condition": "Neuf sans étiquette",
        "description": "Jamais portées, taille normalement.",
        "seller_name": "lucie.snkrs",
        "seller_id": "551013",
        "seller_rating": 4.8,
        "seller_feedback": 31,
        "favourites": 16,
    },
    {
        "id": "9000014",
        "title": "Polo Ralph Lauren blanc — S",
        "price": 19.0,
        "brand": "Ralph Lauren",
        "size": "S",
        "condition": "Bon état",
        "description": "Petite usure au col, reste très portable.",
        "seller_name": "brocante_chic",
        "seller_id": "551014",
        "seller_rating": 4.3,
        "seller_feedback": 121,
        "favourites": 4,
    },
    {
        "id": "9000015",
        "title": "Veste Arc'teryx Beta LT — Noire — L",
        "price": 320.0,
        "brand": "Arc'teryx",
        "size": "L",
        "condition": "Très bon état",
        "description": "Gore-Tex, utilisée en randonnée, imperméabilité intacte.",
        "seller_name": "outdoor_matt",
        "seller_id": "551015",
        "seller_rating": 4.9,
        "seller_feedback": 88,
        "favourites": 39,
    },
    {
        "id": "9000016",
        "title": "Baskets Veja Campo — Blanc — 40",
        "price": 48.0,
        "brand": "Veja",
        "size": "40",
        "condition": "Très bon état",
        "description": "Portées quelques fois, propres.",
        "seller_name": "capucine.c",
        "seller_id": "551016",
        "seller_rating": 4.5,
        "seller_feedback": 27,
        "favourites": 9,
    },
    {
        "id": "9000017",
        "title": "Ceinture Hermès Constance — Cuir noir",
        "price": 290.0,
        "brand": "Hermès",
        "size": "85",
        "condition": "Bon état",
        "description": "Ceinture authentique, boucle argentée, quelques micro-rayures.",
        "seller_name": "heritage.lux",
        "seller_id": "551017",
        "seller_rating": 5.0,
        "seller_feedback": 156,
        "favourites": 62,
    },
    {
        "id": "9000018",
        "title": "Jordan 4 Retro Bred Reimagined — 43",
        "price": 210.0,
        "brand": "Jordan",
        "size": "43",
        "condition": "Neuf avec étiquette",
        "description": "Neuves, jamais portées, facture et boîte d'origine.",
        "seller_name": "kicks.paris",
        "seller_id": "551018",
        "seller_rating": 4.9,
        "seller_feedback": 412,
        "favourites": 120,
    },
]


class DemoVintedAPI(VintedAPI):
    """Remplace l'API Vinted : révèle quelques annonces fictives à chaque scan."""

    def __init__(self, client, db, config):
        super().__init__(client, db, config)
        self._revealed: dict[int, int] = {}
        self._cycle = itertools.count()

    async def ensure_session(
        self, url: str, profile_id: int | None = None, force: bool = False
    ) -> bool:
        await asyncio.sleep(0.05)
        return True

    async def search(
        self, profile: dict, page: int = 1, domain: str = DEFAULT_DOMAIN
    ) -> SearchPage:
        await asyncio.sleep(0.35)
        profile_id = int(profile.get("id") or 0)
        visible = self._revealed.get(profile_id, 6)
        if page > 1:
            visible = 0
        else:
            # +2 ou +3 annonces à chaque passage (rythme d'un vrai marché actif).
            visible = min(visible + 2 + (next(self._cycle) % 2), len(DEMO_ITEMS))
            self._revealed[profile_id] = visible
        origin = origin_of(profile.get("url") or f"https://{DEFAULT_DOMAIN}")
        items = []
        for raw in DEMO_ITEMS[:visible]:
            item = dict(raw)
            item["currency"] = "EUR"
            item["url"] = f"{origin}/items/{raw['id']}"
            item["seller_url"] = f"{origin}/member/{raw['seller_id']}"
            item["image_url"] = f"https://picsum.photos/seed/vinted{raw['id']}/700/860"
            item.setdefault("is_reserved", False)
            item["is_hidden"] = False
            item["is_closed"] = False
            items.append(item)
        return SearchPage(items=items, url="demo://catalog", total=len(DEMO_ITEMS))

    async def enrich_item(
        self, item: dict, domain: str = DEFAULT_DOMAIN, profile_id: int | None = None
    ) -> dict:
        await asyncio.sleep(0.05)
        return item

    async def fetch_seller(
        self, item: dict, domain: str = DEFAULT_DOMAIN, profile_id: int | None = None
    ) -> dict:
        return item


DEMO_PROFILES = [
    {
        "name": "Sneakers Hype",
        "active": True,
        "url": "https://www.vinted.fr/catalog?search_text=nike%20air%20max",
        "min_price": 40,
        "max_price": 250,
        "whitelist": ["nike", "jordan", "adidas", "new balance"],
        "blacklist": ["copie", "replique", "faux", "fake", "defaut", "tache", "abime"],
        "keyword_mode": "any",
        "check_description": True,
        "interval_seconds": 45,
        "min_seller_rating": 4.0,
        "min_seller_feedback": 5,
        "pages": 1,
        "notes": "Exemple de profil — activez vos propres recherches après la démo.",
    },
    {
        "name": "Vêtements de luxe",
        "active": True,
        "url": "https://www.vinted.fr/catalog?search_text=sac%20luxe",
        "min_price": 100,
        "max_price": 600,
        "whitelist": ["longchamp", "max mara", "gucci", "hermes", "moncler"],
        "blacklist": ["copie", "replique", "faux", "defaut", "tache", "usage", "casse"],
        "keyword_mode": "any",
        "check_description": True,
        "interval_seconds": 75,
        "min_seller_rating": 4.5,
        "min_seller_feedback": 20,
        "pages": 1,
        "notes": "Exemple de profil — seuils vendeur exigeants.",
    },
]
