"""Lecture du catalogue Vinted : recherche, parsing des annonces, vendeurs.

Vinted expose un JSON public derrière le catalogue web
(``/api/v2/catalog/items``). Ce module :

1. construit une URL de recherche **triée par « Plus récent »** ;
2. appelle l'API JSON, avec repli sur le HTML (``__NEXT_DATA__``) ;
3. normalise les annonces (prix, marque, taille, état, photo HD, vendeur) ;
4. enrichit le vendeur (note / nombre d'avis) puis met le résultat en cache.
"""

from __future__ import annotations

import html as html_lib
import json
import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from .database import Database
from .http_client import HttpClient, HttpResponse
from .utils import absolute_url, domain_of, format_rating, normalize_text, parse_money

STATUS_LABELS = {
    "1": "Neuf sans étiquette",
    "2": "Très bon état",
    "3": "Bon état",
    "4": "Satisfaisant",
    "5": "Neuf",
    "6": "Neuf avec étiquette",
    "7": "Bon état",
}

DEFAULT_DOMAIN = "www.vinted.fr"

#: Devise associée aux places de marché Vinted (utilisée pour price_from/price_to).
DOMAIN_CURRENCIES = {
    "co.uk": "GBP",
    "com": "USD",
    "pl": "PLN",
    "cz": "CZK",
    "hu": "HUF",
    "ro": "RON",
    "se": "SEK",
    "dk": "DKK",
    "ch": "CHF",
}


def currency_for_domain(domain: str) -> str:
    host = (domain or DEFAULT_DOMAIN).lower()
    for suffix, currency in DOMAIN_CURRENCIES.items():
        if host.endswith("." + suffix):
            return currency
    return "EUR"


@dataclass
class SearchPage:
    items: list[dict]
    url: str
    status: int = 200
    blocked: bool = False
    error: str | None = None
    total: int | None = None

    @property
    def ok(self) -> bool:
        return self.error is None and not self.blocked


# ── Construction des URLs ─────────────────────────────────────────────────────


def search_url(
    raw: str | None,
    domain: str = DEFAULT_DOMAIN,
    *,
    min_price: float | None = None,
    max_price: float | None = None,
    page: int = 1,
    order: str = "newest_first",
) -> str:
    """URL de recherche Vinted, triée par nouveauté, prix bornés."""
    domain = domain_of(domain, DEFAULT_DOMAIN)
    base = f"https://{domain}"
    value = (raw or "").strip()

    if not value:
        url = base + "/catalog"
    elif value.startswith(("http://", "https://")):
        url = value
    elif re.match(r"^[\w.-]*vinted\.[a-z.]{2,}(/.*)?$", value, re.I):
        url = "https://" + value
    else:
        # Simple mot-clé saisi par l'utilisateur.
        url = base + "/catalog?" + urlencode({"search_text": value})

    parsed = urlparse(url)
    params = dict(parse_qsl(parsed.query, keep_blank_values=True))
    params.pop("time", None)  # jeton éphémère ajouté par le navigateur
    params["order"] = order
    params["page"] = str(max(1, int(page)))
    if min_price is not None:
        params["price_from"] = str(int(round(float(min_price))))
    if max_price is not None:
        params["price_to"] = str(int(round(float(max_price))))
    if (min_price is not None or max_price is not None) and "currency" not in params:
        params["currency"] = currency_for_domain(parsed.netloc or domain)

    return urlunparse(
        (
            "https" if parsed.scheme in {"http", "https", ""} else parsed.scheme,
            parsed.netloc or domain,
            parsed.path or "/catalog",
            "",
            urlencode(params, doseq=True),
            "",
        )
    )


def api_url_from_search(url: str, *, per_page: int = 96, page: int = 1) -> str:
    """Transforme une URL de catalogue web en URL de l'API JSON v2."""
    parsed = urlparse(url)
    params = dict(parse_qsl(parsed.query, keep_blank_values=True))
    params.pop("time", None)
    params["per_page"] = str(max(24, min(int(per_page), 96)))
    params["page"] = str(max(1, int(page)))
    params.setdefault("order", "newest_first")
    return f"https://{parsed.netloc}/api/v2/catalog/items?" + urlencode(
        params, doseq=True
    )


# ── Parsing ───────────────────────────────────────────────────────────────────


def _first(*values):
    for value in values:
        if value not in (None, "", [], {}):
            return value
    return None


def _status_label(item: dict) -> str:
    raw = _first(item.get("status"), item.get("status_title"), item.get("condition"))
    if isinstance(raw, dict):
        raw = _first(raw.get("title"), raw.get("name"))
    if raw:
        return str(raw)
    status_id = item.get("status_id")
    return STATUS_LABELS.get(str(status_id), "")


def _size_label(item: dict) -> str:
    raw = _first(item.get("size_title"), item.get("size"))
    if isinstance(raw, dict):
        raw = _first(raw.get("title"), raw.get("name"))
    return str(raw) if raw else ""


def _brand_label(item: dict) -> str:
    raw = _first(item.get("brand_title"), item.get("brand"))
    if isinstance(raw, dict):
        raw = _first(raw.get("title"), raw.get("name"), raw.get("brand_title"))
    return str(raw) if raw else ""


def _photo_url(item: dict) -> str:
    photo = _first(item.get("photo"), item.get("photos") and item["photos"][0], {})
    if isinstance(photo, dict):
        return str(
            _first(
                photo.get("full_size_url"),
                photo.get("url"),
                photo.get("high_resolution_url"),
                "",
            )
            or ""
        )
    if isinstance(photo, str):
        return photo
    return ""


def _seller_node(item: dict) -> dict:
    seller = item.get("user") or item.get("seller") or item.get("owner") or {}
    return seller if isinstance(seller, dict) else {}


def normalize_item(raw: dict, origin: str) -> dict | None:
    """Transforme une annonce brute Vinted en dict homogène."""
    if not isinstance(raw, dict):
        return None
    if "id" not in raw and isinstance(raw.get("item"), dict):
        raw = raw["item"]  # certains payloads encapsulent l'annonce
    item_id = _first(raw.get("id"), raw.get("item_id"))
    if not item_id:
        return None
    price, currency = parse_money(_first(raw.get("price"), raw.get("price_numeric")))
    currency = str(
        _first(raw.get("currency"), raw.get("currency_code"), currency) or currency
    )
    total, total_currency = parse_money(raw.get("total_item_price"))
    if total is not None:
        currency = total_currency or currency
    seller = _seller_node(raw)
    seller_id = _first(seller.get("id"), seller.get("user_id"), raw.get("user_id"))
    seller_name = _first(
        seller.get("login"), seller.get("username"), seller.get("name"), ""
    )
    seller_url = _first(seller.get("profile_url"), seller.get("url"))
    if not seller_url and seller_id:
        seller_url = f"{origin}/member/{seller_id}"
    if seller_url and not str(seller_url).startswith(("http://", "https://")):
        seller_url = absolute_url(str(seller_url), origin)
    rating = format_rating(
        _first(
            seller.get("feedback_reputation"),
            seller.get("rating"),
            seller.get("average_rating"),
        )
    )
    feedback = _first(
        seller.get("feedback_count"),
        seller.get("reviews_count"),
        seller.get("rating_count"),
    )
    try:
        feedback = int(feedback) if feedback is not None else None
    except (TypeError, ValueError):
        feedback = None

    item_url = _first(raw.get("url"), raw.get("item_url"))
    if not item_url:
        item_url = f"{origin}/items/{item_id}"
    else:
        item_url = absolute_url(str(item_url), origin)
    if not item_url.startswith(("http://", "https://")):
        item_url = f"{origin}/items/{item_id}"

    title = str(_first(raw.get("title"), raw.get("name"), "") or "").strip()
    description = str(_first(raw.get("description"), "") or "")
    favourites = _first(
        raw.get("favourite_count"),
        raw.get("favorites_count"),
        raw.get("favourite_count_total"),
    )

    return {
        "id": str(item_id),
        "title": title,
        "description": description,
        "price": price,
        "total_price": total,
        "currency": currency or "EUR",
        "brand": _brand_label(raw),
        "size": _size_label(raw),
        "condition": _status_label(raw),
        "url": item_url,
        "image_url": _photo_url(raw),
        "favourites": int(favourites) if isinstance(favourites, (int, float)) else None,
        "seller_id": str(seller_id) if seller_id else "",
        "seller_name": str(seller_name or ""),
        "seller_rating": rating,
        "seller_feedback": feedback,
        "seller_url": str(seller_url or ""),
        "is_reserved": bool(_first(raw.get("is_reserved"), raw.get("reserved"), False)),
        "is_hidden": bool(_first(raw.get("is_hidden"), raw.get("hidden"), False)),
        "is_closed": bool(_first(raw.get("is_closed"), raw.get("closed"), False)),
    }


def extract_json_blobs(html: str) -> list[Any]:
    """Récupère les blocs JSON embarqués (Next.js, JSON-LD, data-props…)."""
    blobs: list[Any] = []
    for match in re.finditer(
        r'<script[^>]*type=["\']application/(?:ld\+)?json["\'][^>]*>(.*?)</script>',
        html or "",
        re.S | re.I,
    ):
        text = match.group(1).strip()
        if not text or len(text) > 8_000_000:
            continue
        try:
            blobs.append(json.loads(text))
        except json.JSONDecodeError:
            continue
    return blobs


def _walk(node: Any, predicate, limit: int = 60_000):
    """Parcours large (profondeur/volume bornés) d'une structure JSON."""
    stack = [node]
    visited = 0
    while stack and visited < limit:
        current = stack.pop()
        visited += 1
        if predicate(current):
            yield current
        if isinstance(current, dict):
            stack.extend(current.values())
        elif isinstance(current, list):
            stack.extend(current)


def _valid_items(values: Any) -> list[dict]:
    if not isinstance(values, list):
        return []
    return [
        value
        for value in values
        if isinstance(value, dict)
        and (
            value.get("id")
            or (isinstance(value.get("item"), dict) and value["item"].get("id"))
        )
    ]


def items_from_payload(payload: Any) -> list[dict]:
    """Trouve la liste d'annonces, y compris dans une structure imbriquée."""
    if isinstance(payload, dict):
        for key in ("items", "catalogItems", "itemList", "results"):
            found = _valid_items(payload.get(key))
            if found:
                return found
        # Structure inattendue : on cherche la plus grande liste d'annonces.
        best: list[dict] = []
        for node in _walk(
            payload,
            lambda value: (
                isinstance(value, dict)
                and (
                    isinstance(value.get("items"), list)
                    or isinstance(value.get("catalogItems"), list)
                    or isinstance(value.get("itemList"), list)
                )
            ),
        ):
            for key in ("items", "catalogItems", "itemList"):
                found = _valid_items(node.get(key))
                if len(found) > len(best):
                    best = found
        return best
    return []


def items_from_html(html: str) -> list[dict]:
    """Repli HTML : cherche la plus grande liste d'annonces dans le JSON Next."""
    best: list[dict] = []
    for blob in extract_json_blobs(html):
        for fragment in _walk(
            blob,
            lambda node: (
                isinstance(node, dict)
                and (
                    isinstance(node.get("items"), list)
                    or isinstance(node.get("catalogItems"), list)
                    or isinstance(node.get("itemListElement"), list)
                )
            ),
        ):
            candidate: list[dict] = []
            for key in ("items", "catalogItems"):
                candidate = [
                    x for x in _valid_items(fragment.get(key)) if x.get("title")
                ]
                if candidate:
                    break
            if not candidate and isinstance(fragment.get("itemListElement"), list):
                candidate = [
                    element
                    for element in (
                        entry.get("item") if isinstance(entry, dict) else None
                        for entry in fragment["itemListElement"]
                    )
                    if isinstance(element, dict) and element.get("name")
                ]
            if len(candidate) > len(best):
                best = candidate
        if best:
            break
    return best


def _find_item_node(payload: Any, item_id: str) -> dict | None:
    wanted = str(item_id)
    candidates = [
        node
        for node in _walk(
            payload,
            lambda node: (
                isinstance(node, dict)
                and str(node.get("id", "")) == wanted
                and ("title" in node or "description" in node or "price" in node)
            ),
        )
    ]
    if not candidates:
        return None
    # On privilégie le nœud le plus riche (celui qui porte la description).
    return max(candidates, key=lambda node: len(json.dumps(node, default=str)[:20000]))


def _find_product_node(payload: Any) -> dict | None:
    """Nœud schema.org/Product (JSON-LD) présent sur les pages d'annonce."""
    for node in _walk(
        payload,
        lambda n: (
            isinstance(n, dict)
            and ("Product" in str(n.get("@type", "")) or (n.get("@type") == "Product"))
        ),
    ):
        return node
    return None


def _find_user_node(
    payload: Any, seller_id: str | None, login: str | None
) -> dict | None:
    predicate_ids = {str(seller_id)} if seller_id else set()
    candidates = []
    for node in _walk(
        payload,
        lambda n: (
            isinstance(n, dict)
            and (
                "feedback_reputation" in n
                or "feedback_count" in n
                or "reviews_count" in n
            )
        ),
    ):
        if (
            str(node.get("id")) in predicate_ids
            or (login and str(node.get("login")) == str(login))
            or not predicate_ids
        ):
            candidates.append(node)
    if not candidates:
        return None
    return max(candidates, key=lambda node: len(node))


def parse_product_node(node: dict, item: dict, origin: str) -> dict:
    """Complète l'annonce depuis un JSON-LD Product (description, marque, photo)."""
    enriched = dict(item)
    if not enriched.get("description") and node.get("description"):
        enriched["description"] = html_lib.unescape(str(node["description"]))
    if not enriched.get("title") and node.get("name"):
        enriched["title"] = str(node["name"])
    brand = node.get("brand")
    if not enriched.get("brand") and brand:
        enriched["brand"] = brand.get("name") if isinstance(brand, dict) else str(brand)
    image = node.get("image")
    if not enriched.get("image_url") and image:
        if isinstance(image, list):
            image = image[0] if image else None
        if isinstance(image, dict):
            image = _first(image.get("url"), image.get("contentUrl"))
        if image:
            enriched["image_url"] = absolute_url(str(image), origin)
    offers = node.get("offers")
    if isinstance(offers, list):
        offers = offers[0] if offers else None
    if isinstance(offers, dict):
        if enriched.get("price") is None:
            price, currency = parse_money(
                {
                    "amount": offers.get("price") or offers.get("lowPrice"),
                    "currency_code": offers.get("priceCurrency"),
                }
            )
            enriched["price"] = price
            enriched["currency"] = currency or enriched.get("currency", "EUR")
        if not enriched.get("condition") and offers.get("itemCondition"):
            enriched["condition"] = str(offers["itemCondition"]).split("/")[-1]
    return enriched


def parse_item_detail(payload: Any, item: dict) -> dict:
    """Complète une annonce avec description / vendeur depuis une page détail."""
    node = _find_item_node(payload, item["id"])
    if not node:
        return item
    enriched = dict(item)
    if not enriched.get("description") and node.get("description"):
        enriched["description"] = html_lib.unescape(str(node["description"]))
    if not enriched.get("title") and node.get("title"):
        enriched["title"] = str(node["title"])
    if enriched.get("price") is None:
        price, currency = parse_money(node.get("price"))
        enriched["price"], enriched["currency"] = (
            price,
            currency or enriched["currency"],
        )
    if not enriched.get("image_url"):
        enriched["image_url"] = _photo_url(node)
    if not enriched.get("brand"):
        enriched["brand"] = _brand_label(node)
    if not enriched.get("size"):
        enriched["size"] = _size_label(node)
    if not enriched.get("condition"):
        enriched["condition"] = _status_label(node)
    seller = _seller_node(node)
    if seller:
        enriched["seller_id"] = str(
            _first(seller.get("id"), enriched.get("seller_id"), "")
        )
        enriched["seller_name"] = str(
            _first(
                seller.get("login"),
                seller.get("username"),
                enriched.get("seller_name"),
                "",
            )
        )
        enriched["seller_rating"] = format_rating(
            seller.get("feedback_reputation")
        ) or enriched.get("seller_rating")
        feedback = _first(seller.get("feedback_count"), seller.get("reviews_count"))
        if feedback is not None:
            try:
                enriched["seller_feedback"] = int(feedback)
            except (TypeError, ValueError):
                pass
        if not enriched.get("seller_url") and enriched.get("seller_id"):
            enriched["seller_url"] = (
                f"{origin_placeholder(enriched['url'])}/member/{enriched['seller_id']}"
            )
    return enriched


def origin_placeholder(url: str) -> str:
    parsed = urlparse(url)
    return (
        f"{parsed.scheme or 'https'}://{parsed.netloc}"
        if parsed.netloc
        else "https://www.vinted.fr"
    )


# ── API haut niveau ───────────────────────────────────────────────────────────


class VintedAPI:
    def __init__(self, client: HttpClient, db: Database, config):
        self.client = client
        self.db = db
        self.config = config

    async def ensure_session(
        self, url: str, profile_id: int | None = None, force: bool = False
    ) -> bool:
        return await self.client.warm_up(url, force=force, profile_id=profile_id)

    async def search(
        self, profile: dict, page: int = 1, domain: str = DEFAULT_DOMAIN
    ) -> SearchPage:
        """Interroge l'API catalogue ; repli automatique sur le HTML."""
        per_page = int(self.config.get("engine.max_items_per_page", 96))
        web_url = search_url(
            profile.get("url"),
            domain,
            min_price=profile.get("min_price"),
            max_price=profile.get("max_price"),
            page=page,
            order="newest_first",
        )
        api_url = api_url_from_search(web_url, per_page=per_page, page=page)
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": web_url,
        }
        response = await self.client.get(
            api_url, headers=headers, profile_id=profile.get("id"), referer=web_url
        )
        origin = origin_placeholder(web_url)

        if response.ok:
            payload = response.json()
            raw_items = items_from_payload(payload)
            if raw_items:
                items = [normalize_item(raw, origin) for raw in raw_items]
                total = None
                if isinstance(payload, dict):
                    pagination = payload.get("pagination") or {}
                    total = pagination.get("total_entries") or payload.get(
                        "total_count"
                    )
                return SearchPage(
                    items=[item for item in items if item],
                    url=web_url,
                    status=response.status,
                    total=total,
                )
            # 200 mais structure inattendue → repli HTML
            if isinstance(payload, dict) and payload.get("items") == []:
                return SearchPage(
                    items=[],
                    url=web_url,
                    status=response.status,
                    total=(payload.get("pagination") or {}).get("total_entries"),
                )

        if response.blocked:
            return SearchPage(
                items=[],
                url=web_url,
                status=response.status,
                blocked=True,
                error=response.short_error,
            )

        # Repli : page catalogue HTML + JSON embarqué.
        html_response = await self.client.get(
            web_url, profile_id=profile.get("id"), referer=origin + "/"
        )
        if html_response.ok:
            raw_items = items_from_html(html_response.text)
            items = [normalize_item(raw, origin) for raw in raw_items]
            return SearchPage(
                items=[item for item in items if item],
                url=web_url,
                status=html_response.status,
            )
        return SearchPage(
            items=[],
            url=web_url,
            status=html_response.status,
            blocked=html_response.blocked,
            error=html_response.short_error or response.short_error,
        )

    async def enrich_item(
        self, item: dict, domain: str = DEFAULT_DOMAIN, profile_id: int | None = None
    ) -> dict:
        """Récupère la description + les infos vendeur depuis la page détail."""
        if not self.config.get("engine.detail_fetch", True):
            return item
        if not item.get("url"):
            return item
        response: HttpResponse = await self.client.get(
            item["url"],
            profile_id=profile_id,
            referer=f"https://{domain}/",
            quiet=True,
        )
        if not response.ok:
            return item
        blobs = extract_json_blobs(response.text)
        origin = origin_placeholder(item["url"])
        for blob in blobs:
            enriched = parse_item_detail(blob, item)
            if enriched.get("description") or enriched.get("seller_rating") is not None:
                item = enriched
                break
        if not item.get("description"):
            for blob in blobs:
                product = _find_product_node(blob)
                if product:
                    item = parse_product_node(product, item, origin)
                    break
        if not item.get("description"):
            # Dernier repli : balise meta description (souvent = description).
            meta = re.search(
                r'<meta[^>]+(?:property|name)=["\'](?:og:description|description)["\']'
                r'[^>]+content=["\'](.*?)["\']',
                response.text,
                re.S | re.I,
            )
            if meta and not item.get("description"):
                item = dict(item)
                item["description"] = html_lib.unescape(meta.group(1))[:4000]
        return item

    async def fetch_seller(
        self, item: dict, domain: str = DEFAULT_DOMAIN, profile_id: int | None = None
    ) -> dict:
        """Complète la note et le nombre d'avis du vendeur (avec cache SQLite)."""
        if not self.config.get("engine.enrich_sellers", True):
            return item
        if (
            item.get("seller_rating") is not None
            and item.get("seller_feedback") is not None
        ):
            return item
        key = item.get("seller_id") or normalize_text(item.get("seller_name", ""))
        if not key:
            return item
        ttl = int(self.config.get("engine.seller_cache_ttl_hours", 24))
        cached = self.db.get_seller_cache(key, ttl)
        if cached:
            item = dict(item)
            item["seller_rating"] = item.get("seller_rating") or cached.get("rating")
            item["seller_feedback"] = (
                item.get("seller_feedback")
                if item.get("seller_feedback") is not None
                else cached.get("feedback")
            )
            item["seller_name"] = item.get("seller_name") or cached.get("name") or ""
            item["seller_url"] = item.get("seller_url") or cached.get("url") or ""
            return item

        url = item.get("seller_url") or (
            f"https://{domain}/member/{item['seller_id']}"
            if item.get("seller_id")
            else ""
        )
        if not url:
            return item
        response = await self.client.get(
            url, profile_id=profile_id, referer=f"https://{domain}/", quiet=True
        )
        seller: dict | None = None
        if response.ok:
            for blob in extract_json_blobs(response.text):
                seller = _find_user_node(
                    blob, item.get("seller_id"), item.get("seller_name")
                )
                if seller:
                    break
            if not seller:
                seller = self._seller_from_html(response.text, item)
        if seller:
            item = dict(item)
            item["seller_name"] = str(
                _first(
                    seller.get("login"),
                    seller.get("username"),
                    item.get("seller_name"),
                    "",
                )
            )
            item["seller_rating"] = format_rating(
                seller.get("feedback_reputation")
            ) or item.get("seller_rating")
            feedback = _first(seller.get("feedback_count"), seller.get("reviews_count"))
            if feedback is not None:
                try:
                    item["seller_feedback"] = int(feedback)
                except (TypeError, ValueError):
                    pass
            item["seller_url"] = url
            self.db.set_seller_cache(
                key,
                {
                    "id": item.get("seller_id"),
                    "name": item.get("seller_name"),
                    "rating": item.get("seller_rating"),
                    "feedback": item.get("seller_feedback"),
                    "url": url,
                },
            )
        return item

    @staticmethod
    def _seller_from_html(page: str, item: dict) -> dict | None:
        """Repli quand le HTML n'expose pas de JSON exploitable."""
        rating = re.search(r'"feedback_reputation"\s*:\s*([0-9.]+)', page)
        count = re.search(r'"feedback_count"\s*:\s*(\d+)', page)
        login = re.search(r'"login"\s*:\s*"([^"]+)"', page)
        if not (rating or count):
            return None
        return {
            "login": login.group(1) if login else item.get("seller_name"),
            "feedback_reputation": float(rating.group(1)) if rating else None,
            "feedback_count": int(count.group(1)) if count else None,
        }
