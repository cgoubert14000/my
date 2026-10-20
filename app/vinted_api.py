"""Lecture du catalogue Vinted — parseur SSR (Next.js App Router, 2026).

Depuis septembre 2026, Vinted ne sert plus les annonces via
``/api/v2/catalog/items`` (404, API interne signée) et n'expose plus de
``__NEXT_DATA__``. Les annonces sont **rendues côté serveur** dans la page
``/catalog`` sous forme de cartes :

* ``div[data-testid="grid-item"]`` (96 par page) ;
* ``[data-testid="product-item-id-<id>"]`` et ses variantes
  ``--title-container``, ``--price-text``, ``--description--content``,
  ``--image--img``, ``--overlay-link`` ;
* un texte compact dans ``<a title>`` / ``<img alt>`` :
  ``"Nike Air Max 97, Marque: Nike, État: Bon état, Taille: 42, 89.00 €, 94.50 €"``.

Ce module :

1. construit l'URL de recherche triée « Plus récent » ;
2. lit la page SSR et extrait chaque carte (avec replis RSC / JSON-LD) ;
3. enrichit l'annonce et le vendeur depuis la page publique de l'article ;
4. tolère les variantes de structure et les autres langues du groupe.
"""

from __future__ import annotations

import html as html_lib
import json
import re
import time
from dataclasses import dataclass
from typing import Any, Iterator
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from .database import Database
from .http_client import HttpClient
from .utils import absolute_url, domain_of, format_rating, normalize_text, parse_money

try:  # bs4 est dans requirements.txt, mais on reste utilisable sans lui.
    from bs4 import BeautifulSoup  # type: ignore
except Exception:  # pragma: no cover
    BeautifulSoup = None  # type: ignore

DEFAULT_DOMAIN = "www.vinted.fr"

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
    "lt": "EUR",
    "lv": "EUR",
    "ee": "EUR",
    "sk": "EUR",
    "at": "EUR",
    "be": "EUR",
    "es": "EUR",
    "it": "EUR",
    "nl": "EUR",
    "pt": "EUR",
    "fi": "EUR",
    "ie": "EUR",
    "gr": "EUR",
    "lu": "EUR",
}

DOMAIN_LOCALES = {
    "fr": "fr-FR,fr;q=0.9,en;q=0.6",
    "de": "de-DE,de;q=0.9,en;q=0.6",
    "at": "de-AT,de;q=0.9,en;q=0.6",
    "co.uk": "en-GB,en;q=0.9",
    "com": "en-US,en;q=0.9",
    "es": "es-ES,es;q=0.9,en;q=0.6",
    "it": "it-IT,it;q=0.9,en;q=0.6",
    "nl": "nl-NL,nl;q=0.9,en;q=0.6",
    "be": "nl-BE,nl;q=0.9,fr;q=0.7,en;q=0.5",
    "pt": "pt-PT,pt;q=0.9,en;q=0.6",
    "pl": "pl-PL,pl;q=0.9,en;q=0.6",
    "cz": "cs-CZ,cs;q=0.9,en;q=0.6",
    "sk": "sk-SK,sk;q=0.9,en;q=0.6",
    "hu": "hu-HU,hu;q=0.9,en;q=0.6",
    "ro": "ro-RO,ro;q=0.9,en;q=0.6",
    "se": "sv-SE,sv;q=0.9,en;q=0.6",
    "dk": "da-DK,da;q=0.9,en;q=0.6",
    "fi": "fi-FI,fi;q=0.9,en;q=0.6",
    "lt": "lt-LT,lt;q=0.9,en;q=0.6",
    "lv": "lv-LV,lv;q=0.9,en;q=0.6",
    "ee": "et-EE,et;q=0.9,en;q=0.6",
    "ch": "de-CH,de;q=0.9,fr;q=0.6,en;q=0.5",
    "ie": "en-IE,en;q=0.9",
    "gr": "el-GR,el;q=0.9,en;q=0.6",
    "lu": "fr-LU,fr;q=0.9,de;q=0.7,en;q=0.5",
}

STATUS_LABELS = {
    "1": "Neuf sans étiquette",
    "2": "Très bon état",
    "3": "Bon état",
    "4": "Satisfaisant",
    "5": "Neuf",
    "6": "Neuf avec étiquette",
    "7": "Bon état",
}

#: Symboles monétaires → code ISO.
SYMBOL_CURRENCIES = {
    "€": "EUR",
    "$": "USD",
    "£": "GBP",
    "chf": "CHF",
    "zł": "PLN",
    "kč": "CZK",
    "kr": "SEK",
    "ft": "HUF",
    "lei": "RON",
}

CONDITION_WORDS = (
    "neuf",
    "très bon état",
    "tres bon etat",
    "bon état",
    "bon etat",
    "satisfaisant",
    "new with tags",
    "new without tags",
    "new",
    "very good",
    "good",
    "satisfactory",
    "sehr gut",
    "gut",
    "neu",
    "muy bueno",
    "bueno",
    "ottimo",
    "buono",
    "nieuw",
    "zo goed als nieuw",
    "goed",
    "bdb",
    "dobry",
    "nowy",
    "velmi dobrý",
    "dobrý",
)


def currency_for_domain(domain: str) -> str:
    host = (domain or DEFAULT_DOMAIN).lower()
    for suffix, currency in DOMAIN_CURRENCIES.items():
        if host.endswith("." + suffix):
            return currency
    return "EUR"


def locale_for_domain(domain: str) -> str:
    host = (domain or DEFAULT_DOMAIN).lower()
    for suffix, locale in DOMAIN_LOCALES.items():
        if host.endswith("." + suffix):
            return locale
    return "fr-FR,fr;q=0.9,en;q=0.6"


class VintedError(RuntimeError):
    """Erreur de lecture du catalogue."""


@dataclass
class SearchPage:
    items: list[dict]
    url: str
    status: int = 200
    blocked: bool = False
    error: str | None = None
    total: int | None = None
    empty: bool = False
    html_bytes: int = 0
    #: Page identique au dernier passage : aucune analyse n'a été nécessaire.
    unchanged: bool = False
    #: Identifiant de l'annonce la plus récente (télémétrie).
    newest_id: str | None = None
    #: Empreinte des premières cartes : sert à détecter une page inchangée.
    head_key: str | None = None
    #: Temps passé à analyser le HTML (ms), pour le diagnostic de latence.
    parse_ms: int = 0

    @property
    def ok(self) -> bool:
        return self.error is None and not self.blocked


# ─── URLs ─────────────────────────────────────────────────────────────────────


def _set_param(params: list[tuple[str, str]], key: str, value: str) -> list[tuple[str, str]]:
    """Remplace un paramètre unique en conservant l'ordre et les doublons."""
    kept = [(k, v) for k, v in params if k != key]
    return [*kept, (key, str(value))]


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
    # Liste de paires : ``brand_ids[]`` et ``catalog[]`` peuvent être répétés.
    params = [
        (key, value)
        for key, value in parse_qsl(parsed.query, keep_blank_values=True)
        if key != "time"  # jeton éphémère ajouté par le navigateur
    ]
    params = _set_param(params, "order", order)
    params = _set_param(params, "page", str(max(1, int(page))))
    if min_price is not None:
        params = _set_param(params, "price_from", str(int(round(float(min_price)))))
    if max_price is not None:
        params = _set_param(params, "price_to", str(int(round(float(max_price)))))
    if (min_price is not None or max_price is not None) and not any(
        key == "currency" for key, _ in params
    ):
        params = _set_param(params, "currency", currency_for_domain(parsed.netloc or domain))

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
    """URL de l'ancienne API JSON (conservée pour les marchés qui la servent)."""
    parsed = urlparse(url)
    params = dict(parse_qsl(parsed.query, keep_blank_values=True))
    params.pop("time", None)
    params["per_page"] = str(max(24, min(int(per_page), 96)))
    params["page"] = str(max(1, int(page)))
    params.setdefault("order", "newest_first")
    return f"https://{parsed.netloc}/api/v2/catalog/items?" + urlencode(
        params, doseq=True
    )


def canonical_item_url(raw: str | None, origin: str, item_id: str | None = None) -> str:
    """URL propre (sans ``?referrer=catalog`` ni jetons de suivi)."""
    if not raw:
        return f"{origin}/items/{item_id}" if item_id else origin
    url = absolute_url(str(raw), origin)
    parsed = urlparse(url)
    path = parsed.path or (f"/items/{item_id}" if item_id else "/")
    return urlunparse((parsed.scheme or "https", parsed.netloc, path, "", "", ""))


def origin_of(url: str) -> str:
    parsed = urlparse(url if "://" in url else f"https://{url}")
    return f"{parsed.scheme or 'https'}://{parsed.netloc}"


# ─── Texte & prix ─────────────────────────────────────────────────────────────

_PRICE_RE = re.compile(
    r"(?<![\d.,])"
    r"(\d{1,3}(?:[ \u00a0\u202f.]\d{3})*(?:[.,]\d{1,2})?|\d+(?:[.,]\d{1,2})?)"
    r"\s*(€|\$|£|CHF|zł|Zł|Kč|kr|Ft|lei|PLN|CZK|SEK|DKK|HUF|RON|EUR|GBP|USD)",
    re.IGNORECASE,
)

_LABEL_ALIASES = {
    "brand": ("brand", "marque", "marke", "marca", "merk", "marka", "značka", "znacka"),
    "condition": (
        "condition",
        "état",
        "etat",
        "zustand",
        "estado",
        "condizioni",
        "conditie",
        "stan",
        "stav",
        "condición",
        "condicao",
        "condição",
        "kondycja",
    ),
    "size": (
        "size",
        "taille",
        "größe",
        "grösse",
        "grosse",
        "talla",
        "taglia",
        "maat",
        "rozmiar",
        "velikost",
        "wielkość",
    ),
    "color": (
        "colour",
        "color",
        "couleur",
        "farbe",
        "colore",
        "kleur",
        "kolor",
        "barva",
    ),
}
_LABEL_LOOKUP = {
    alias: key for key, aliases in _LABEL_ALIASES.items() for alias in aliases
}
_LABEL_RE = re.compile(
    r"\b("
    + "|".join(
        re.escape(alias) for alias in sorted(_LABEL_LOOKUP, key=len, reverse=True)
    )
    + r")\s*:\s*",
    re.IGNORECASE,
)


def _clean(value: str | None) -> str:
    if not value:
        return ""
    text = html_lib.unescape(str(value))
    text = text.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2009", " ")
    return re.sub(r"\s+", " ", text).strip()


def _logo_currency(symbol: str | None, default: str) -> str:
    key = (symbol or "").strip().lower()
    if key in SYMBOL_CURRENCIES:
        return SYMBOL_CURRENCIES[key]
    upper = (symbol or "").strip().upper()
    if upper in {"EUR", "USD", "GBP", "PLN", "CZK", "SEK", "DKK", "HUF", "RON", "CHF"}:
        return upper
    return default or "EUR"


def _amount(value: str) -> float | None:
    raw = str(value).replace(" ", "").replace("\u00a0", "").replace("\u202f", "")
    if raw.count(",") == 1 and raw.count(".") == 0:
        raw = raw.replace(",", ".")
    else:
        raw = raw.replace(",", "")
    try:
        return round(float(raw), 2)
    except ValueError:
        return None


def parse_price_segments(
    text: str, default_currency: str = "EUR"
) -> list[tuple[float, str]]:
    """Tous les montants d'un texte, avec leur devise."""
    found: list[tuple[float, str]] = []
    for match in _PRICE_RE.finditer(_clean(text)):
        amount = _amount(match.group(1))
        if amount is None:
            continue
        found.append((amount, _logo_currency(match.group(2), default_currency)))
    return found


def parse_compact_text(text: str, default_currency: str = "EUR") -> dict:
    """Décode ``"Titre, Marque: X, État: Y, Taille: Z, 12.00 €, 13.20 €"``.

    Utilisé pour les attributs ``title`` / ``alt`` des cartes Vinted, qui
    contiennent toutes les métadonnées affichées, dans la langue du domaine.
    """
    cleaned = _clean(text)
    if not cleaned:
        return {}

    labels = list(_LABEL_RE.finditer(cleaned))
    prices = list(_PRICE_RE.finditer(cleaned))
    cuts = [
        match.start()
        for match in (labels[0] if labels else None, prices[0] if prices else None)
        if match is not None
    ]
    cut = min(cuts) if cuts else len(cleaned)
    title = cleaned[:cut].strip().rstrip(",;·|-").strip()

    data: dict[str, Any] = {}
    if title:
        data["title"] = title

    for index, match in enumerate(labels):
        key = _LABEL_LOOKUP.get(match.group(1).strip().lower())
        if not key or key in data:
            continue
        end = labels[index + 1].start() if index + 1 < len(labels) else len(cleaned)
        for price in prices:
            if match.end() <= price.start() < end:
                end = price.start()
                break
        value = cleaned[match.end() : end].strip().strip(",;·|-").strip()
        value = re.sub(
            r"\s+(incl\.?|inkl\.?|include[d]?)$", "", value, flags=re.I
        ).strip()
        if value:
            data[key] = value

    amounts = [
        (m, _amount(m.group(1)), _logo_currency(m.group(2), default_currency))
        for m in prices
    ]
    amounts = [entry for entry in amounts if entry[1] is not None]
    if amounts:
        data["price"] = amounts[0][1]
        data["currency"] = amounts[0][2]
        if len(amounts) > 1:
            data["total_price"] = amounts[1][1]
    return data


def _looks_like_condition(value: str) -> bool:
    text = normalize_text(value)
    return any(word in text for word in CONDITION_WORDS)


def _split_description_text(text: str) -> dict:
    """Repli : ``"Nike · S · Bon état"`` (marque / taille / état)."""
    data: dict[str, str] = {}
    tokens = [
        token.strip() for token in re.split(r"[·|•]", _clean(text)) if token.strip()
    ]
    if not tokens:
        return data
    condition = next((token for token in tokens if _looks_like_condition(token)), "")
    if condition:
        data["condition"] = condition
    remaining = [token for token in tokens if token != condition]
    if remaining and not _looks_like_condition(remaining[0]):
        data["brand"] = remaining.pop(0)
    if remaining:
        candidate = remaining[0]
        if len(candidate) <= 24 and not _PRICE_RE.search(candidate):
            data["size"] = candidate
    return data


# ─── Extraction RSC (flight Next.js) ──────────────────────────────────────────

_RSC_PUSH_RE = re.compile(r"self\.__next_f\.push\(\[\s*1\s*,\s*")


def extract_rsc_text(html: str, max_chars: int = 24_000_000) -> str:
    """Réassemble les chunks RSC (``self.__next_f.push([1,"…"])``)."""
    if not html or "self.__next_f" not in html:
        return ""
    decoder = json.JSONDecoder()
    chunks: list[str] = []
    total = 0
    for match in _RSC_PUSH_RE.finditer(html):
        try:
            value, _ = decoder.raw_decode(html, match.end())
        except (ValueError, json.JSONDecodeError):
            continue
        if isinstance(value, str):
            chunks.append(value)
            total += len(value)
            if total > max_chars:
                break
    return "".join(chunks)


def _balanced_slice(
    text: str, start: int, opening: str = "[", closing: str = "]"
) -> str | None:
    """Extrait ``[ ... ]`` à partir de ``start`` en respectant les chaînes JSON."""
    if start >= len(text) or text[start] != opening:
        return None
    depth = 0
    in_string = False
    escaped = False
    for index in range(start, min(len(text), start + 4_000_000)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == opening:
            depth += 1
        elif char == closing:
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    return None


def json_arrays_after(text: str, key: str, limit: int = 4) -> Iterator[list]:
    """Toutes les listes JSON associées à une clé (``"items":[...]``)."""
    if not text:
        return
    pattern = re.compile(r'"%s"\s*:\s*\[' % re.escape(key))
    for count, match in enumerate(pattern.finditer(text)):
        if count >= limit:
            return
        raw = _balanced_slice(text, text.find("[", match.start()))
        if not raw:
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(value, list):
            yield value


def items_from_rsc(html: str, origin: str, default_currency: str = "EUR") -> list[dict]:
    """Repli : objets d'annonces présents dans le payload RSC."""
    text = extract_rsc_text(html)
    if not text:
        return []
    items: list[dict] = []
    for key in ("items", "catalogItems", "itemList", "gridItems"):
        for values in json_arrays_after(text, key):
            for value in values:
                if isinstance(value, dict):
                    normalized = normalize_item(value, origin, default_currency)
                    if normalized:
                        items.append(normalized)
            if items:
                return _dedupe(items)
    # JSON-LD ItemList
    for blob in extract_json_blobs(html):
        for fragment in _walk(
            blob,
            lambda node: (
                isinstance(node, dict) and isinstance(node.get("itemListElement"), list)
            ),
        ):
            for entry in fragment["itemListElement"]:
                candidate = entry.get("item") if isinstance(entry, dict) else None
                if isinstance(candidate, dict):
                    normalized = normalize_item(candidate, origin, default_currency)
                    if normalized:
                        items.append(normalized)
    return _dedupe(items)


# ─── Cartes SSR ───────────────────────────────────────────────────────────────

_ITEM_ID_IN_TESTID_RE = re.compile(r"^product-item-id-(\d+)$")
_CARD_TESTID_RE = re.compile(r"^product-item-id-(\d+)(?:--|$)")
_HREF_ITEM_RE = re.compile(r"/items/(\d+)(?:-[^/?#]*)?")


def _dedupe(items: list[dict]) -> list[dict]:
    seen: set[str] = set()
    result: list[dict] = []
    for item in items:
        if not item or not item.get("id") or item["id"] in seen:
            continue
        seen.add(item["id"])
        result.append(item)
    return result


def _node_text(node) -> str:
    if node is None:
        return ""
    return _clean(node.get_text(" ", strip=True))


def _find_testid(node, pattern: str):
    return node.find(attrs={"data-testid": re.compile(pattern)})


def _card_to_item(card, origin: str, default_currency: str) -> dict | None:
    """Transforme une carte SSR en annonce normalisée."""
    testid = str(card.get("data-testid") or "")
    match = _ITEM_ID_IN_TESTID_RE.match(testid) or _CARD_TESTID_RE.match(testid)
    container = card
    if not match:
        inner = _find_testid(card, r"^product-item-id-\d+$")
        if inner is not None:
            container = inner
            match = _ITEM_ID_IN_TESTID_RE.match(str(inner.get("data-testid") or ""))
    if not match:
        return None
    item_id = match.group(1)

    link = container.find("a", href=re.compile(r"/items/\d+")) or card.find(
        "a", href=re.compile(r"/items/\d+")
    )
    image = container.find("img") or card.find("img")

    compact = ""
    if link is not None and link.get("title"):
        compact = str(link.get("title"))
    if not compact and image is not None and image.get("alt"):
        compact = str(image.get("alt"))

    data = parse_compact_text(compact, default_currency) if compact else {}

    price_text = _node_text(_find_testid(container, r"--price-text$"))
    if not price_text:
        price_text = _node_text(_find_testid(card, r"--price-text$"))
    total_text = _node_text(_find_testid(container, r"--total-price$"))
    if not total_text:
        total_text = _node_text(_find_testid(card, r"--total-price$"))

    description_text = " · ".join(
        _node_text(node)
        for node in (
            container.find_all(
                attrs={"data-testid": re.compile(r"--description--content$")}
            )
            or card.find_all(
                attrs={"data-testid": re.compile(r"--description--content$")}
            )
        )
    )
    fallback = _split_description_text(description_text)

    if data.get("price") is None and price_text:
        amounts = parse_price_segments(price_text, default_currency)
        if amounts:
            data["price"], data["currency"] = amounts[0]
    if data.get("total_price") is None and total_text:
        amounts = parse_price_segments(total_text, default_currency)
        if amounts:
            data["total_price"] = amounts[0][0]
    if data.get("currency") is None:
        data["currency"] = default_currency

    for key in ("brand", "size", "condition"):
        if not data.get(key) and fallback.get(key):
            data[key] = fallback[key]

    href = str(link.get("href")) if link is not None and link.get("href") else ""
    image_url = ""
    if image is not None:
        image_url = str(image.get("src") or "")
        if not image_url and image.get("srcset"):
            image_url = str(image["srcset"]).split(",")[0].strip().split(" ")[0]

    favourites_text = _node_text(_find_testid(card, r"favourite-count-text$"))
    favourites = None
    if favourites_text.isdigit():
        favourites = int(favourites_text)

    title = _clean(data.get("title") or "")
    if not title:
        title_node = _find_testid(card, r"--title-container$")
        title = _node_text(title_node)
    if not title:
        title = _clean(compact).split(",")[0]

    return {
        "id": str(item_id),
        "title": title or "Annonce Vinted",
        "description": "",
        "price": data.get("price"),
        "total_price": data.get("total_price"),
        "currency": data.get("currency") or default_currency,
        "brand": _clean(data.get("brand")),
        "size": _clean(data.get("size")),
        "condition": _clean(data.get("condition")),
        "url": canonical_item_url(href, origin, item_id),
        "image_url": image_url,
        "favourites": favourites,
        "seller_id": "",
        "seller_name": "",
        "seller_rating": None,
        "seller_feedback": None,
        "seller_url": "",
        "is_reserved": False,
        "is_hidden": False,
        "is_closed": False,
    }


def _soup(html: str):
    if BeautifulSoup is None:
        return None
    try:
        parser = "lxml" if _has_lxml() else "html.parser"
    except Exception:  # pragma: no cover
        parser = "html.parser"
    try:
        return BeautifulSoup(html, parser)
    except Exception:  # pragma: no cover
        return BeautifulSoup(html, "html.parser")


_LXML_AVAILABLE: bool | None = None


def _has_lxml() -> bool:
    global _LXML_AVAILABLE
    if _LXML_AVAILABLE is None:
        try:
            import lxml  # noqa: F401

            _LXML_AVAILABLE = True
        except Exception:
            _LXML_AVAILABLE = False
    return _LXML_AVAILABLE


def parse_catalog_html(
    html: str,
    origin: str,
    default_currency: str = "EUR",
    *,
    limit: int | None = None,
    fast: bool = False,
) -> list[dict]:
    """Extrait les annonces d'une page catalogue Vinted (SSR).

    ``fast=True`` + ``limit`` court-circuitent l'analyse DOM : indispensable en
    temps réel, où seule la tête de page (annonces les plus récentes) compte.
    """
    if not html:
        return []

    if fast and limit:
        quick = _parse_cards_regex(html, origin, default_currency, limit=limit)
        if quick:
            return _dedupe(quick)

    items: list[dict] = []
    soup = _soup(html)
    if soup is not None:
        cards = soup.find_all(attrs={"data-testid": "grid-item"})
        if not cards:
            cards = soup.find_all(attrs={"data-testid": _ITEM_ID_IN_TESTID_RE})
        for card in cards[:limit] if limit else cards:
            item = _card_to_item(card, origin, default_currency)
            if item:
                items.append(item)
    if not items:
        items = _parse_cards_regex(html, origin, default_currency)
    if not items:
        items = items_from_rsc(html, origin, default_currency)
    if not items:
        items = _parse_anchor_fallback(html, origin, default_currency)
    return _dedupe(items)


def _parse_anchor_fallback(html: str, origin: str, default_currency: str) -> list[dict]:
    """Dernier recours : tout lien ``/items/<id>`` porteur d'un prix.

    Utilisé uniquement si ni les cartes SSR ni le payload RSC n'ont donné
    d'annonce : protège contre un changement de classes/attributs.
    """
    items: list[dict] = []
    pattern = re.compile(r'<a\b[^>]*href="([^"]*?/items/(\d+)[^"]*)"([^>]*)>', re.I)
    for match in pattern.finditer(html or ""):
        href, item_id, attrs = match.group(1), match.group(2), match.group(3)
        chunk = html[match.end() : match.end() + 5000]
        title_attr = re.search(r'title="([^"]{3,400})"', attrs)
        alt_attr = re.search(r'<img\b[^>]*alt="([^"]{3,400})"', chunk, re.I)
        img_attr = re.search(r'<img\b[^>]*src="([^"]+)"', chunk, re.I)
        compact = _clean(
            html_lib.unescape(
                (title_attr.group(1) if title_attr else "")
                or (alt_attr.group(1) if alt_attr else "")
            )
        )
        data = parse_compact_text(compact, default_currency) if compact else {}
        if data.get("price") is None:
            continue  # lien de navigation, pas une annonce
        items.append(
            {
                "id": item_id,
                "title": _clean(data.get("title")) or "Annonce Vinted",
                "description": "",
                "price": data.get("price"),
                "total_price": data.get("total_price"),
                "currency": data.get("currency") or default_currency,
                "brand": _clean(data.get("brand")),
                "size": _clean(data.get("size")),
                "condition": _clean(data.get("condition")),
                "url": canonical_item_url(html_lib.unescape(href), origin, item_id),
                "image_url": html_lib.unescape(img_attr.group(1)) if img_attr else "",
                "favourites": None,
                "seller_id": "",
                "seller_name": "",
                "seller_rating": None,
                "seller_feedback": None,
                "seller_url": "",
                "is_reserved": False,
                "is_hidden": False,
                "is_closed": False,
            }
        )
    return items


def _parse_cards_regex(
    html: str, origin: str, default_currency: str, limit: int | None = None
) -> list[dict]:
    """Repli sans bs4 : découpe le HTML sur les cartes ``grid-item``.

    Bien plus rapide que l'analyse DOM complète (~10× sur une page de 3,5 Mo) :
    utilisée en priorité en mode temps réel pour ne lire que les premières
    cartes, celles qui contiennent les annonces les plus récentes.
    """
    if 'data-testid="grid-item"' not in html and "product-item-id-" not in html:
        return []
    chunks = re.split(r'data-testid="grid-item"', html)
    items: list[dict] = []
    for chunk in chunks[1:]:
        if limit is not None and len(items) >= limit:
            break
        chunk = chunk[:60_000]
        id_match = re.search(r"product-item-id-(\d+)", chunk)
        if not id_match:
            continue
        item_id = id_match.group(1)
        href_match = re.search(r'href="(/items/\d+[^"]*)"', chunk)
        alt_match = re.search(r'<img[^>]+alt="([^"]*)"', chunk)
        img_match = re.search(r'<img[^>]+src="([^"]+)"', chunk)
        title_match = re.search(r'title="([^"]{5,300})"', chunk)
        compact = _clean(html_lib.unescape(alt_match.group(1))) if alt_match else ""
        if not compact and title_match:
            compact = _clean(html_lib.unescape(title_match.group(1)))
        data = parse_compact_text(compact, default_currency)
        if data.get("price") is None:
            text = _clean(re.sub(r"<[^>]+>", " ", chunk))
            amounts = parse_price_segments(text, default_currency)
            if amounts:
                data["price"], data["currency"] = amounts[0]
                if len(amounts) > 1:
                    data["total_price"] = amounts[1][0]
        items.append(
            {
                "id": item_id,
                "title": data.get("title") or "Annonce Vinted",
                "description": "",
                "price": data.get("price"),
                "total_price": data.get("total_price"),
                "currency": data.get("currency") or default_currency,
                "brand": data.get("brand", ""),
                "size": data.get("size", ""),
                "condition": data.get("condition", ""),
                "url": canonical_item_url(
                    html_lib.unescape(href_match.group(1)) if href_match else "",
                    origin,
                    item_id,
                ),
                "image_url": html_lib.unescape(img_match.group(1)) if img_match else "",
                "favourites": None,
                "seller_id": "",
                "seller_name": "",
                "seller_rating": None,
                "seller_feedback": None,
                "seller_url": "",
                "is_reserved": False,
                "is_hidden": False,
                "is_closed": False,
            }
        )
    return items


# ─── JSON embarqué & page article ─────────────────────────────────────────────


def extract_json_blobs(html: str) -> list[Any]:
    """Blocs JSON embarqués (JSON-LD, scripts applicatifs)."""
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
    """Parcours large (volume borné) d'une structure JSON."""
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
    return


def _first(*values):
    for value in values:
        if value not in (None, "", [], {}):
            return value
    return None


def _brand_label(raw: dict) -> str:
    value = _first(raw.get("brand_title"), raw.get("brand"))
    if isinstance(value, dict):
        value = _first(value.get("title"), value.get("name"), value.get("brand_title"))
    return str(value) if value else ""


def _size_label(raw: dict) -> str:
    value = _first(raw.get("size_title"), raw.get("size"))
    if isinstance(value, dict):
        value = _first(value.get("title"), value.get("name"))
    return str(value) if value else ""


def _status_label(raw: dict) -> str:
    value = _first(raw.get("status"), raw.get("status_title"), raw.get("condition"))
    if isinstance(value, dict):
        value = _first(value.get("title"), value.get("name"))
    if value:
        return str(value)
    return STATUS_LABELS.get(str(raw.get("status_id")), "")


def _photo_url(raw: dict) -> str:
    photo = _first(raw.get("photo"), raw.get("photos") and raw["photos"][0], {})
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


def _seller_node(raw: dict) -> dict:
    seller = raw.get("user") or raw.get("seller") or raw.get("owner") or {}
    return seller if isinstance(seller, dict) else {}


def normalize_item(
    raw: dict, origin: str, default_currency: str = "EUR"
) -> dict | None:
    """Normalise une annonce brute (API historique, RSC ou JSON-LD)."""
    if not isinstance(raw, dict):
        return None
    if "id" not in raw and isinstance(raw.get("item"), dict):
        raw = raw["item"]
    item_id = _first(raw.get("id"), raw.get("item_id"))
    if not item_id:
        return None
    price, currency = parse_money(_first(raw.get("price"), raw.get("price_numeric")))
    currency = str(
        _first(
            raw.get("currency"), raw.get("currency_code"), currency, default_currency
        )
        or default_currency
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
    if seller_url:
        seller_url = canonical_item_url(str(seller_url), origin)
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

    favourites = _first(
        raw.get("favourite_count"),
        raw.get("favorites_count"),
        raw.get("favourite_count_total"),
    )

    return {
        "id": str(item_id),
        "title": str(_first(raw.get("title"), raw.get("name"), "") or "").strip(),
        "description": str(_first(raw.get("description"), "") or ""),
        "price": price,
        "total_price": total,
        "currency": currency or "EUR",
        "brand": _brand_label(raw),
        "size": _size_label(raw),
        "condition": _status_label(raw),
        "url": canonical_item_url(
            _first(raw.get("url"), raw.get("item_url")), origin, str(item_id)
        ),
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


def _longest_json_string(text: str, key: str, limit: int = 6) -> str:
    """Plus longue valeur de ``"clé":"…"`` (description d'annonce)."""
    pattern = re.compile(r'"%s"\s*:\s*"((?:[^"\\]|\\.)*)"' % re.escape(key))
    best = ""
    for count, match in enumerate(pattern.finditer(text)):
        if count >= 200:
            break
        try:
            value = json.loads('"' + match.group(1) + '"')
        except json.JSONDecodeError:
            continue
        if len(value) > len(best):
            best = value
        if len(best) > limit * 1000:
            break
    return _clean(best)


def parse_item_page(html: str, item: dict, origin: str) -> dict:
    """Complète une annonce depuis sa page publique (description, vendeur, photo HD)."""
    if not html:
        return item

    enriched = dict(item)
    soup = _soup(html)
    rsc = extract_rsc_text(html)
    meta: dict[str, str] = {}
    if soup is not None:
        for tag in soup.find_all("meta"):
            key = tag.get("property") or tag.get("name")
            content = tag.get("content")
            if key and content:
                meta[str(key).lower()] = str(content)

    # ── Description ──────────────────────────────────────────────────────
    if not enriched.get("description"):
        candidates = []
        if soup is not None:
            for pattern in (
                r"^item-description$",
                r"item-description",
                r"^description$",
            ):
                node = soup.find(attrs={"data-testid": re.compile(pattern)})
                if node is not None:
                    candidates.append(_node_text(node))
            itemprop = soup.find(attrs={"itemprop": "description"})
            if itemprop is not None:
                candidates.append(_node_text(itemprop))
        if rsc:
            candidates.append(_longest_json_string(rsc, "description"))
        candidates.append(meta.get("og:description", ""))
        best = max((text for text in candidates if text), key=len, default="")
        if len(best) >= 15:
            enriched["description"] = best[:4000]

    # ── Photo HD ─────────────────────────────────────────────────────────
    og_image = meta.get("og:image", "")
    if og_image and "vinted.net" in og_image:
        enriched["image_url"] = og_image

    # ── Prix (si absent) ─────────────────────────────────────────────────
    if enriched.get("price") is None:
        for key in ("product:price:amount", "og:price:amount", "price"):
            if meta.get(key):
                amount = _amount(meta[key])
                if amount is not None:
                    enriched["price"] = amount
                    enriched["currency"] = _logo_currency(
                        meta.get("product:price:currency")
                        or meta.get("og:price:currency"),
                        enriched.get("currency") or "EUR",
                    )
                    break

    # ── Vendeur ──────────────────────────────────────────────────────────
    seller = _seller_from_page(html, rsc, enriched)
    enriched.update(
        {key: value for key, value in seller.items() if value not in (None, "")}
    )

    # ── Champs manquants via JSON-LD ─────────────────────────────────────
    if not enriched.get("title") or not enriched.get("brand"):
        for blob in extract_json_blobs(html):
            product = next(
                _walk(
                    blob,
                    lambda node: (
                        isinstance(node, dict)
                        and "Product" in str(node.get("@type", ""))
                    ),
                ),
                None,
            )
            if product:
                enriched["title"] = enriched.get("title") or _clean(
                    product.get("name", "")
                )
                brand = product.get("brand")
                if not enriched.get("brand") and brand:
                    enriched["brand"] = _clean(
                        brand.get("name") if isinstance(brand, dict) else str(brand)
                    )
                break

    return enriched


def _seller_from_page(html: str, rsc: str, item: dict) -> dict:
    """Extrait pseudo / note / avis du vendeur depuis la page article."""
    seller: dict[str, Any] = {}
    seller_id = item.get("seller_id") or ""
    offender = re.search(r"offender_id=(\d+)", html)
    if not seller_id and offender:
        seller_id = offender.group(1)
    if seller_id:
        seller["seller_id"] = seller_id

    text = rsc or html
    login = ""
    if seller_id:
        patterns = (
            rf'"id"\s*:\s*{re.escape(seller_id)}\s*,\s*"login"\s*:\s*"([^"]+)"',
            rf'"login"\s*:\s*"([^"]+)"\s*,\s*"id"\s*:\s*{re.escape(seller_id)}',
        )
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                login = match.group(1)
                break
    if not login:
        matches = re.findall(r'"login"\s*:\s*"([^"]+)"', text)
        if matches:
            login = matches[0]
    if login:
        seller["seller_name"] = _clean(login)

    rating_match = re.search(r'"feedback_reputation"\s*:\s*([0-9.]+)', text)
    if rating_match:
        seller["seller_rating"] = format_rating(float(rating_match.group(1)))
    count_match = re.search(r'"feedback_count"\s*:\s*(\d+)', text)
    if count_match:
        seller["seller_feedback"] = int(count_match.group(1))

    if seller.get("seller_id") or seller.get("seller_name"):
        base = item.get("seller_url") or ""
        if base:
            seller["seller_url"] = base
        elif seller.get("seller_id"):
            parsed = urlparse(item.get("url", ""))
            seller["seller_url"] = (
                f"{parsed.scheme or 'https'}://{parsed.netloc}/member/{seller['seller_id']}"
            )
    return seller


def _seller_from_seller_page(html: str) -> dict:
    """Infos vendeur depuis ``/member/<id>``."""
    seller: dict[str, Any] = {}
    rsc = extract_rsc_text(html)
    text = rsc or html
    login = re.search(r'"login"\s*:\s*"([^"]+)"', text)
    if login:
        seller["name"] = _clean(login.group(1))
    rating = re.search(r'"feedback_reputation"\s*:\s*([0-9.]+)', text)
    if rating:
        seller["rating"] = format_rating(float(rating.group(1)))
    count = re.search(r'"feedback_count"\s*:\s*(\d+)', text)
    if count:
        seller["feedback"] = int(count.group(1))
    return seller


# ─── API haut niveau ──────────────────────────────────────────────────────────


class VintedAPI:
    def __init__(self, client: HttpClient, db: Database, config):
        self.client = client
        self.db = db
        self.config = config

    async def ensure_session(
        self,
        url: str,
        profile_id: int | None = None,
        force: bool = False,
        attempts: int = 2,
    ) -> bool:
        return await self.client.warm_up(
            url, force=force, profile_id=profile_id, attempts=attempts
        )

    async def _search_api(
        self, profile: dict, page: int, domain: str, web_url: str, origin: str
    ) -> SearchPage | None:
        """Ancienne API JSON : 404 depuis sept. 2026, activable pour les marchés qui la servent."""
        per_page = int(self.config.get("engine.max_items_per_page", 96))
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
            api_url,
            headers=headers,
            profile_id=profile.get("id"),
            referer=web_url,
            attempts=2,
        )
        if not response.ok or "json" not in (
            response.headers.get("content-type") or ""
        ):
            return None
        payload = response.json()
        if not isinstance(payload, dict):
            return None
        raw_items = payload.get("items") or payload.get("catalogItems") or []
        if not isinstance(raw_items, list) or not raw_items:
            return None
        currency = currency_for_domain(domain)
        items = [normalize_item(raw, origin, currency) for raw in raw_items]
        pagination = payload.get("pagination") or {}
        return SearchPage(
            items=[item for item in items if item],
            url=web_url,
            status=response.status,
            total=pagination.get("total_entries")
            if isinstance(pagination, dict)
            else None,
            html_bytes=len(response.text or ""),
        )

    async def search(
        self,
        profile: dict,
        page: int = 1,
        domain: str = DEFAULT_DOMAIN,
        *,
        known_head: str | None = None,
        head_limit: int | None = None,
        attempts: int | None = None,
        timeout: int | None = None,
    ) -> SearchPage:
        """Interroge le catalogue : HTML SSR en priorité, API JSON en option.

        ``known_head`` active la détection incrémentale : on compare l'empreinte
        des :data:`HEAD_FINGERPRINT` premières cartes (et non la seule première,
        car Vinted insère des annonces sponsorisées en tête de liste). Empreinte
        identique ⇒ page inchangée, HTML non analysé.
        ``head_limit`` borne l'analyse aux N premières cartes (mode temps réel).
        """
        web_url = search_url(
            profile.get("url"),
            domain,
            min_price=profile.get("min_price"),
            max_price=profile.get("max_price"),
            page=page,
            order="newest_first",
        )
        origin = origin_of(web_url)
        currency = currency_for_domain(domain)

        if self.config.get("http.use_json_api", False):
            api_page = await self._search_api(profile, page, domain, web_url, origin)
            if api_page and api_page.items:
                return api_page

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": locale_for_domain(domain),
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
        }
        response = await self.client.get(
            web_url,
            headers=headers,
            profile_id=profile.get("id"),
            referer=origin + "/",
            attempts=attempts,
            timeout=timeout,
        )
        if response.blocked:
            return SearchPage(
                items=[],
                url=web_url,
                status=response.status,
                blocked=True,
                error=response.short_error,
                html_bytes=len(response.text or ""),
            )
        if not response.ok:
            return SearchPage(
                items=[],
                url=web_url,
                status=response.status,
                error=response.short_error,
                html_bytes=len(response.text or ""),
            )

        html = response.text or ""
        newest = newest_item_id(html)
        head = head_item_ids(html, HEAD_FINGERPRINT)
        head_key = ",".join(head) if head else None
        if known_head and head_key and head_key == known_head:
            return SearchPage(
                items=[],
                url=web_url,
                status=response.status,
                html_bytes=len(html),
                unchanged=True,
                newest_id=newest,
                head_key=head_key,
            )

        started = time.perf_counter()
        items = parse_catalog_html(
            html,
            origin,
            currency,
            limit=head_limit,
            fast=bool(head_limit),
        )
        parse_ms = int((time.perf_counter() - started) * 1000)
        empty = not items and _looks_empty_page(html)
        total = _total_from_html(html)
        return SearchPage(
            items=items,
            url=web_url,
            status=response.status,
            total=total,
            empty=empty,
            html_bytes=len(html),
            newest_id=newest,
            head_key=head_key,
            parse_ms=parse_ms,
        )

    async def enrich_item(
        self,
        item: dict,
        domain: str = DEFAULT_DOMAIN,
        profile_id: int | None = None,
        fast: bool = False,
    ) -> dict:
        """Description + vendeur + photo HD depuis la page publique de l'annonce.

        ``fast`` (mode temps réel) : une seule tentative courte. Une fiche
        article lente ne doit jamais retarder l'alerte Discord.
        """
        if not self.config.get("engine.detail_fetch", True):
            return item
        if not item.get("url"):
            return item
        response = await self.client.get(
            item["url"],
            profile_id=profile_id,
            referer=f"https://{domain}/",
            quiet=True,
            attempts=1 if fast else 2,
            timeout=6 if fast else None,
        )
        if not response.ok:
            return item
        enriched = parse_item_page(response.text, item, origin_of(item["url"]))
        return enriched

    async def fetch_seller(
        self,
        item: dict,
        domain: str = DEFAULT_DOMAIN,
        profile_id: int | None = None,
        fast: bool = False,
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
            url,
            profile_id=profile_id,
            referer=f"https://{domain}/",
            quiet=True,
            attempts=1 if fast else 2,
            timeout=6 if fast else None,
        )
        if not response.ok:
            return item
        seller = _seller_from_seller_page(response.text)
        if seller:
            item = dict(item)
            item["seller_name"] = item.get("seller_name") or seller.get("name") or ""
            item["seller_rating"] = item.get("seller_rating") or seller.get("rating")
            if item.get("seller_feedback") is None:
                item["seller_feedback"] = seller.get("feedback")
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


_GRID_MARKER = 'data-testid="grid-item"'
_ITEM_ID_IN_HTML_RE = re.compile(r"product-item-id-(\d+)")

#: Nombre de cartes dont on compare les identifiants pour dire « page inchangée ».
#: 20 et non 1 : Vinted peut épingler des annonces sponsorisées en tête.
HEAD_FINGERPRINT = 20


def newest_item_id(html: str) -> str | None:
    """Identifiant de la première annonce de la page (tri « Plus récent »).

    Coût : un ``str.find`` + une regex sur 4 Ko, soit ~0,1 ms même sur une page
    de 3,5 Mo. C'est la brique de la détection incrémentale : si cet identifiant
    n'a pas bougé, aucune annonce n'est apparue en tête de liste.
    """
    if not html:
        return None
    start = html.find(_GRID_MARKER)
    if start < 0:
        start = html.find("product-item-id-")
        if start < 0:
            return None
    match = _ITEM_ID_IN_HTML_RE.search(html, start, start + 50_000)
    return match.group(1) if match else None


def head_item_ids(html: str, limit: int = 12) -> list[str]:
    """Identifiants des premières annonces, dans l'ordre de la page."""
    if not html:
        return []
    start = html.find(_GRID_MARKER)
    if start < 0:
        return []
    window = html[start : start + 250_000]
    ids: list[str] = []
    for match in _ITEM_ID_IN_HTML_RE.finditer(window):
        if match.group(1) not in ids:
            ids.append(match.group(1))
        if len(ids) >= limit:
            break
    return ids


def _looks_empty_page(html: str) -> bool:
    sample = (html or "")[-200_000:].lower()
    markers = (
        "aucun résultat",
        "aucun resultat",
        "no results",
        "nothing found",
        "0 résultat",
        "keine ergebnisse",
        "nessun risultato",
        "sin resultados",
        "geen resultaten",
        "brak wyników",
        "0 annonces",
    )
    return any(marker in sample for marker in markers)


def _total_from_html(html: str) -> int | None:
    match = re.search(
        r"([\d\s.,+]{1,12})\s*(?:résultats?|results?|resultados|risultati|"
        r"ergebnisse|resultaten|wyników)",
        html or "",
        re.I,
    )
    if not match:
        return None
    digits = re.sub(r"\D", "", match.group(1))
    return int(digits) if digits else None
