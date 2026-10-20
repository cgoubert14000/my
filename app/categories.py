"""Catégories Vinted : liste de départ + découverte en direct.

Vinted n'expose plus d'API de catégories (``/api/v2/categories`` → 404 depuis
septembre 2026). On combine donc :

* une liste **vérifiée** des grandes catégories (affichage immédiat, hors ligne) ;
* une **découverte en direct** : la page d'une catégorie contient les liens de
  ses sous-catégories, qu'on extrait du HTML. L'arbre reste ainsi toujours à
  jour, y compris pour les sous-catégories les plus profondes.

Les URL de catégorie reposent sur l'identifiant numérique
(``/catalog/1231-men_shoes_new``) : le chemin seul suffit, et ``/catalog/5``
résout correctement quel que soit le domaine (vérifié sur vinted.fr).
"""

from __future__ import annotations

import re
from dataclasses import dataclass

#: Grandes catégories communes à tous les domaines Vinted (identifiants stables).
#: Slugs français : ils servent à construire une URL lisible, Vinted résout aussi
#: les URL sans slug.
TOP_LEVEL: tuple[tuple[str, str, str], ...] = (
    ("1904", "women_root", "Femmes"),
    ("5", "mens", "Hommes"),
    ("1193", "children_new", "Enfants"),
    ("4332", "sports", "Sport"),
    ("1918", "home", "Maison"),
    ("2994", "electronics", "Électronique"),
    ("2309", "entertainment", "Livres et médias"),
    ("4824", "hobbies_collectables", "Loisirs et collections"),
    ("139", "cosmetics_and_beauty_items", "Soins et beauté"),
)

#: Chemin de catégorie accepté (protection contre les injections d'URL).
CATEGORY_PATH_RE = re.compile(r"^/catalog(?:/\d+(?:-[a-z0-9_-]+)?)?/?$", re.I)
_LINK_RE = re.compile(
    r'<a\b[^>]*href="(?P<href>/catalog/(?P<id>\d+)(?:-(?P<slug>[a-z0-9_-]+))?)"'
    r"[^>]*>(?P<label>.*?)</a>",
    re.I | re.S,
)
_TAG_RE = re.compile(r"<[^>]+>")


@dataclass(frozen=True)
class Category:
    id: str
    slug: str
    name: str
    path: str

    def as_dict(self, origin: str = "") -> dict:
        url = f"{origin}{self.path}" if origin else self.path
        return {
            "id": self.id,
            "slug": self.slug,
            "name": self.name,
            "path": self.path,
            "url": url,
        }


def top_level() -> list[Category]:
    return [
        Category(cid, slug, name, f"/catalog/{cid}-{slug}")
        for cid, slug, name in TOP_LEVEL
    ]


def category_url(origin: str, path: str) -> str:
    origin = (origin or "").rstrip("/")
    return f"{origin}{normalize_path(path)}"


def normalize_path(path: str | None) -> str:
    """Ramène un chemin utilisateur à ``/catalog/...`` (ou ``/catalog``)."""
    value = (path or "").strip()
    if not value:
        return "/catalog"
    if value.startswith("http://") or value.startswith("https://"):
        from urllib.parse import urlparse

        value = urlparse(value).path or "/catalog"
    if not value.startswith("/"):
        value = "/" + value
    if value.startswith("/catalog?") or value == "/catalog/":
        return "/catalog"
    if not CATEGORY_PATH_RE.match(value):
        return "/catalog"
    return value.rstrip("/") or "/catalog"


def is_valid_path(path: str | None) -> bool:
    return CATEGORY_PATH_RE.match((path or "").strip()) is not None


def sanitize_path(raw: str | None) -> str | None:
    """Chemin sûr ou ``None`` si l'entrée n'est pas une catégorie Vinted.

    Accepte ``/catalog/5-mens``, ``catalog/5`` et une URL Vinted complète ;
    refuse tout le reste (traversée de répertoire, autre section du site…).
    """
    value = (raw or "").strip()
    if not value:
        return "/catalog"
    if value.startswith(("http://", "https://")):
        from urllib.parse import urlparse

        value = urlparse(value).path or "/catalog"
    if ".." in value:
        return None
    candidate = value.split("?", 1)[0].rstrip("/")
    if not candidate.startswith("/"):
        candidate = "/" + candidate
    if not candidate.startswith("/catalog") or not is_valid_path(candidate):
        return None
    return normalize_path(candidate)


def _clean_label(raw: str) -> str:
    text = _TAG_RE.sub(" ", raw or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_children(html: str, origin: str = "", exclude: str | None = None) -> list[dict]:
    """Sous-catégories présentes dans une page de catégorie Vinted.

    Les liens ``/catalog/<id>-<slug>`` du menu latéral sont extraits, dédupliqués
    et débarrassés des entrées vides. La catégorie courante est exclue.
    """
    if not html:
        return []
    current = normalize_path(exclude) if exclude else ""
    seen: set[str] = set()
    children: list[dict] = []
    for match in _LINK_RE.finditer(html):
        cat_id = match.group("id")
        slug = match.group("slug") or ""
        name = _clean_label(match.group("label"))
        if not name or len(name) > 80:
            continue
        path = f"/catalog/{cat_id}-{slug}" if slug else f"/catalog/{cat_id}"
        if path == current or cat_id in seen:
            continue
        seen.add(cat_id)
        children.append(Category(cat_id, slug, name, path).as_dict(origin))
    return children


def page_title(html: str) -> str:
    """Nom de la catégorie affichée en haut de la page (``<h1>``)."""
    match = re.search(r"<h1[^>]*>(.*?)</h1>", html or "", re.I | re.S)
    if not match:
        return ""
    return _clean_label(match.group(1))[:80]


def path_label(path: str, name: str = "") -> str:
    """Libellé lisible stocké sur le profil (ex. « Hommes › Chaussures »)."""
    if name:
        return name[:120]
    clean = normalize_path(path)
    if clean == "/catalog":
        return "Toutes les catégories"
    last = clean.rsplit("/", 1)[-1]
    slug = last.split("-", 1)[1] if "-" in last else last
    return slug.replace("_", " ").replace("-", " ").title()[:120]


def category_id_from_path(path: str | None) -> str:
    """Identifiant numérique d'un chemin de catégorie (``""`` si racine)."""
    clean = normalize_path(path)
    match = re.match(r"^/catalog/(\d+)", clean)
    return match.group(1) if match else ""


def category_id_from_url(url: str) -> str:
    """Identifiant de catégorie présent dans une URL (chemin ou ``catalog[]``)."""
    from urllib.parse import parse_qsl, urlparse

    value = (url or "").strip()
    if not value:
        return ""
    parsed = urlparse(value if "://" in value else f"https://{value}")
    from_path = category_id_from_path(parsed.path or "")
    if from_path:
        return from_path
    for key, item in parse_qsl(parsed.query, keep_blank_values=True):
        if key in {"catalog[]", "catalog"}:
            match = re.match(r"^(\d+)", str(item).strip())
            if match:
                return match.group(1)
    return ""


def compose_query(pairs: list[tuple[str, str]]) -> str:
    """Assemble une query string en gardant les crochets littéraux.

    Vinted construit ses propres liens avec ``brand_ids[]=53`` (non encodé) :
    on reproduit exactement cette forme, vérifiée sur le site.
    """
    from urllib.parse import quote, quote_plus

    return "&".join(
        f"{quote(str(key), safe='[]')}={quote_plus(str(value))}"
        for key, value in pairs
        if str(key)
    )


def _split_source(current_url: str, domain: str) -> tuple[str, str, list[tuple[str, str]]]:
    """Décompose une URL (ou un mot-clé) en (domaine, chemin, paramètres)."""
    from urllib.parse import parse_qsl, urlparse

    value = (current_url or "").strip()
    if value.startswith(("http://", "https://")):
        parsed = urlparse(value)
        netloc = parsed.netloc or domain
        if "vinted." not in netloc.lower():  # mot-clé ou domaine inattendu
            netloc = domain
        path = parsed.path or "/catalog"
        params = [
            (key, item)
            for key, item in parse_qsl(parsed.query, keep_blank_values=True)
            if key
        ]
        return netloc, path, params
    if value and "=" in value:  # « search_text=nike »
        return domain, "/catalog", [(k, v) for k, v in parse_qsl(value, keep_blank_values=True) if k]
    if value:  # simple mot-clé
        return domain, "/catalog", [("search_text", value)]
    return domain, "/catalog", []


#: Paramètres pilotés par le sélecteur : toujours reconstruits, jamais dupliqués.
_MANAGED = {"catalog[]", "catalog", "brand_ids[]", "brand_ids", "page", "time"}


def build_profile_url(
    current_url: str,
    path: str | None = None,
    brand_ids: list[str] | None = None,
    domain: str = "www.vinted.fr",
) -> str:
    """Construit l'URL d'un profil en conservant mots-clés et filtres.

    * ``path`` : catégorie à appliquer (``None`` = ne pas y toucher).
    * ``brand_ids`` : marques à appliquer (``None`` = ne pas y toucher,
      ``[]`` = retirer le filtre de marque).

    Sans marque, la catégorie reste dans le chemin
    (``/catalog/1231-men_shoes_new?search_text=nike``), forme vérifiée sur
    Vinted. Dès qu'une marque est sélectionnée, l'URL passe en paramètres
    (``/catalog?catalog[]=1231&brand_ids[]=53``) : c'est la seule forme où
    Vinted applique réellement ``brand_ids[]``.
    """
    from urllib.parse import urlunparse

    netloc, current_path, params = _split_source(current_url, domain)

    # Catégorie : argument explicite, sinon celle déjà présente dans l'URL.
    if path is None:
        cat_id = category_id_from_url(current_url)
        clean_path = current_path if cat_id else "/catalog"
        if cat_id:
            clean_path = f"/catalog/{cat_id}"
    else:
        cat_id = category_id_from_path(path)
        clean_path = normalize_path(path)

    # Marques : argument explicite, sinon celles déjà présentes dans l'URL.
    if brand_ids is None:
        brands = [
            value
            for key, value in params
            if key.startswith("brand_ids") and str(value).strip().isdigit()
        ]
        brands = list(dict.fromkeys(brands))
    else:
        brands = [str(brand_id).strip() for brand_id in brand_ids if str(brand_id).strip().isdigit()]
        brands = list(dict.fromkeys(brands))

    kept = [(key, value) for key, value in params if key not in _MANAGED]
    kept = [
        (key, value)
        for key, value in kept
        if not (brands and key.startswith("brand_ids")) and not (cat_id and key.startswith("catalog"))
    ]

    if brands:
        query = []
        if cat_id:
            query.append(("catalog[]", cat_id))
        query.extend(("brand_ids[]", brand_id) for brand_id in brands)
        query.extend(kept)
        return urlunparse(("https", netloc, "/catalog", "", compose_query(query), ""))

    if cat_id and kept:
        return urlunparse(("https", netloc, clean_path, "", compose_query(kept), ""))
    if cat_id:
        return urlunparse(("https", netloc, clean_path, "", "", ""))
    return urlunparse(("https", netloc, "/catalog", "", compose_query(kept), ""))
