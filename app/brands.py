"""Marques Vinted : sélection rapide + liste réelle lue en direct.

Vinted n'expose pas d'API publique des marques (``/api/v2/brands`` répond
« jeton invalide »). En revanche, deux pages HTML sont accessibles et rendues
côté serveur :

* ``/brands`` : les marques les plus populaires, regroupées par lettre ;
* ``/brands/by_letter/<L>`` : la liste alphabétique des marques (≈100 par
  lettre, triées par volume d'annonces).

On s'en sert pour proposer un sélecteur réel : à chaque lettre, les marques
correspondantes sont lues sur Vinted puis mises en cache. Un filtre de marque
se traduit dans l'URL par ``brand_ids[]=<id>`` (paramètre vérifié sur le site,
à condition d'utiliser ``/catalog?catalog[]=<id>&brand_ids[]=<id>`` : la forme
« chemin » ``/catalog/1231-slug?brand_ids[]=…`` est ignorée par Vinted).

Aucune marque n'est inventée : les identifiants de la liste ``POPULAR``
proviennent tous de pages Vinted réelles.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from urllib.parse import parse_qsl, urlencode, urlparse

#: Lettres proposées par le navigateur de marques.
LETTERS: tuple[str, ...] = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

#: Raccourci hors ligne : marques les plus recherchées (identifiants vérifiés).
POPULAR: tuple[tuple[str, str], ...] = (
    ("53", "Nike"),
    ("14", "adidas"),
    ("7", "H&M"),
    ("1775", "New Balance"),
    ("1195", "Asics"),
    ("11445", "Converse"),
    ("11943", "Crocs"),
    ("362", "Carhartt"),
    ("255", "Calvin Klein"),
    ("120", "Hugo Boss"),
    ("258", "G-Star"),
    ("5291", "FILA"),
    ("7973", "Champion"),
    ("65", "Dickies"),
    ("309", "Dr. Martens"),
    ("20", "GUESS"),
    ("567", "Gucci"),
    ("671", "Dior"),
    ("364", "Burberry"),
    ("214", "Napapijri"),
    ("188676", "Gymshark"),
    ("232", "New Era"),
    ("386", "Decathlon"),
)

#: Nombre maximum de marques combinables dans un profil.
MAX_BRANDS = 20

_BRAND_LINK_RE = re.compile(
    r'<a\b[^>]*href="(?P<href>/brand/(?P<id>\d+)(?:-(?P<slug>[a-z0-9_-]+))?)"'
    r"[^>]*>(?P<label>.*?)</a>",
    re.I | re.S,
)
_TAG_RE = re.compile(r"<[^>]+>")
_COUNT_RE = re.compile(r"\s*\d[\d\s\u00a0]*articles?\b.*$", re.I | re.S)


@dataclass(frozen=True)
class Brand:
    id: str
    slug: str
    name: str

    def as_dict(self, origin: str = "") -> dict:
        path = f"/brand/{self.id}-{self.slug}" if self.slug else f"/brand/{self.id}"
        return {
            "id": self.id,
            "slug": self.slug,
            "name": self.name,
            "url": f"{origin}{path}" if origin else path,
        }


def popular() -> list[dict]:
    """Marques populaires (aucun réseau), dédupliquées et triées par nom."""
    seen: dict[str, str] = {}
    for brand_id, name in POPULAR:
        seen.setdefault(brand_id, name)
    brands = [Brand(brand_id, _slugify(name), name) for brand_id, name in seen.items()]
    return [brand.as_dict() for brand in sorted(brands, key=lambda b: b.name.lower())]


#: Index id → nom, construit une seule fois.
_POPULAR_BY_ID: dict[str, str] = {brand_id: name for brand_id, name in POPULAR}


def _slugify(name: str) -> str:
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def letter_of(name: str) -> str:
    """Lettre de classement d'une marque (« É» → « E », « Nike » → « N »)."""
    text = unicodedata.normalize("NFKD", (name or "").strip())
    text = "".join(ch for ch in text if not unicodedata.combining(ch)).strip()
    if not text or not text[0].isalpha():
        return ""
    letter = text[0].upper()
    return letter if letter in LETTERS else ""


def sanitize_letter(raw: str | None) -> str | None:
    letter = (raw or "").strip().upper()
    return letter if letter in LETTERS else None


def brands_url(origin: str, letter: str) -> str:
    origin = (origin or "").rstrip("/")
    return f"{origin}/brands/by_letter/{letter}"


def _clean_name(raw: str) -> str:
    text = _TAG_RE.sub(" ", raw or "")
    text = _COUNT_RE.sub(" ", text)
    text = text.replace("Suivre", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text[:80]


def parse_brands(html: str, origin: str = "") -> list[dict]:
    """Marques présentes dans une page ``/brands/by_letter/…``."""
    if not html:
        return []
    seen: set[str] = set()
    brands: list[dict] = []
    for match in _BRAND_LINK_RE.finditer(html):
        brand_id = match.group("id")
        if brand_id in seen:
            continue
        name = _clean_name(match.group("label"))
        if not name:
            continue
        seen.add(brand_id)
        brands.append(Brand(brand_id, match.group("slug") or "", name).as_dict(origin))
    return brands


def parse_brand_reference(raw: str) -> dict | None:
    """Résout n'importe quelle marque Vinted depuis une URL ou un identifiant.

    Accepte ``https://www.vinted.fr/brand/53-nike``, ``/brand/53-nike``,
    ``53`` ou ``53-nike``. C'est la porte d'entrée vers **toutes** les marques,
    y compris celles absent de la liste alphabétique (Vinted n'en affiche que
    les ~100 plus volumineuses par lettre).
    """
    value = (raw or "").strip()
    if not value or ".." in value:
        return None
    match = re.search(r"/brand/(\d{1,10})(?:-([a-z0-9_-]+))?", value, re.I)
    if not match:
        match = re.match(r"^(?:brand\s*[:#]?\s*)?(\d{1,10})(?:-([a-z0-9_-]+))?$", value, re.I)
    if not match:
        return None
    brand_id = match.group(1)
    slug = (match.group(2) or "").lower()
    name = _POPULAR_BY_ID.get(brand_id)
    if not name and slug:
        name = slug.replace("-", " ").replace("_", " ").title()
    if not name:
        name = f"Marque {brand_id}"
    return {"id": brand_id, "slug": slug, "name": name[:80]}


def filter_brands(brands: list[dict], query: str) -> list[dict]:
    """Filtre local (insensible aux accents et à la casse) sur le nom."""
    needle = _slugify(query or "").replace("-", " ")
    if not needle:
        return brands
    return [
        brand
        for brand in brands
        if needle in _slugify(brand.get("name", "")).replace("-", " ")
    ]


def parse_brand_ids(values) -> list[str]:
    """Identifiants de marque valides, dédupliqués et bornés."""
    if values is None:
        return []
    if isinstance(values, str):
        values = re.split(r"[,\s]+", values)
    out: list[str] = []
    for value in values:
        text = str(value).strip()
        if text.isdigit() and text not in out:
            out.append(text)
    return out[:MAX_BRANDS]


def brand_ids_from_url(url: str) -> list[str]:
    """Extrait ``brand_ids[]`` d'une URL de recherche Vinted."""
    if not url or "brand_ids" not in url:
        return []
    query = urlparse(url).query or url.split("?", 1)[-1]
    raw = [value for key, value in parse_qsl(query, keep_blank_values=True) if key.startswith("brand_ids")]
    return parse_brand_ids(raw)


def brands_query(brand_ids: list[str]) -> str:
    """Fragment ``brand_ids[]=…`` prêt à coller dans une URL."""
    return urlencode([("brand_ids[]", brand_id) for brand_id in brand_ids], doseq=True)


def brand_labels(brand_ids: list[str], known: dict[str, str] | None = None) -> str:
    """Libellé lisible stocké sur le profil (« Nike, adidas »)."""
    labels = dict(POPULAR)
    labels.update(known or {})
    names = [labels[brand_id] for brand_id in brand_ids if brand_id in labels]
    return ", ".join(names)[:200]


# ─── Index complet via les sitemaps officiels ────────────────────────────────
#
# Vinted publie l'intégralité de son catalogue de marques dans ses sitemaps
# (déclarés dans robots.txt) : ``/sitemaps/<langue>/brands.xml`` et
# ``brands1.xml``, soit ~57 000 marques avec leur identifiant et leur slug.
# Deux à trois requêtes suffisent pour récupérer ce que les pages
# ``/brands/by_letter/…`` n'exposent jamais (elles s'arrêtent aux 100 plus
# vendues par lettre).

_LOC_RE = re.compile(r"<loc>\s*(?P<url>[^<\s]+)\s*</loc>", re.I)
_SITEMAP_LINE_RE = re.compile(r"^\s*sitemap:\s*(?P<url>\S+)\s*$", re.I | re.M)

#: Mots à ne pas capitaliser dans un nom de marque (« Good American Jeans »).
_LOWER_WORDS = {"de", "du", "des", "la", "le", "les", "et", "and", "of", "the", "for", "by", "x"}


def brand_name_from_slug(slug: str) -> str:
    """Nom lisible à partir d'un slug Vinted (« good-american-jeans »)."""
    words = [word for word in re.split(r"[-_]+", (slug or "").strip()) if word]
    out: list[str] = []
    for index, word in enumerate(words):
        if word.isdigit():
            out.append(word)
        elif index > 0 and word.lower() in _LOWER_WORDS:
            out.append(word.lower())
        else:
            out.append(word[:1].upper() + word[1:])
    return " ".join(out)[:80]


def parse_sitemap_locs(xml: str) -> list[str]:
    """Toutes les URL ``<loc>`` d'un sitemap (index ou liste)."""
    return [match.group("url") for match in _LOC_RE.finditer(xml or "")]


def sitemaps_from_robots(text: str) -> list[str]:
    """Sitemaps déclarés dans un ``robots.txt``."""
    return [match.group("url") for match in _SITEMAP_LINE_RE.finditer(text or "")]


def brand_sitemaps(locs: list[str]) -> list[str]:
    """Parmi les sitemaps d'un index, ceux qui contiennent les marques."""
    return [url for url in locs if re.search(r"/brands?\d*\.xml$", url, re.I)]


def brands_from_sitemap(xml: str) -> list[dict]:
    """Marques extraites d'un sitemap : identifiant, slug et nom lisible."""
    seen: set[str] = set()
    rows: list[dict] = []
    for url in parse_sitemap_locs(xml):
        match = re.search(r"/brand/(\d{1,10})(?:-([a-z0-9_-]+))?\s*$", url, re.I)
        if not match:
            continue
        brand_id = match.group(1)
        if brand_id in seen:
            continue
        seen.add(brand_id)
        slug = (match.group(2) or "").lower()
        name = _POPULAR_BY_ID.get(brand_id) or brand_name_from_slug(slug) or f"Marque {brand_id}"
        rows.append({"id": brand_id, "slug": slug, "name": name})
    return rows
