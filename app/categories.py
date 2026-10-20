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


def build_profile_url(
    current_url: str, path: str, domain: str = "www.vinted.fr"
) -> str:
    """Applique une catégorie à une URL de recherche en conservant les filtres.

    Exemple : ``https://www.vinted.fr/catalog?search_text=nike`` + ``/catalog/5``
    → ``https://www.vinted.fr/catalog/5?search_text=nike``.
    """
    from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

    value = (current_url or "").strip()
    if value.startswith(("http://", "https://")):
        parsed = urlparse(value)
        netloc = parsed.netloc or domain
        if "vinted." not in netloc.lower():  # mot-clé ou domaine inattendu
            netloc = domain
        query = parsed.query
    else:
        netloc = domain
        query = ""
        if value and "=" in value:  # « search_text=nike »
            query = value
        elif value:  # simple mot-clé
            query = urlencode({"search_text": value})
    params = [(k, v) for k, v in parse_qsl(query, keep_blank_values=True) if k]
    return urlunparse(
        (
            "https",
            netloc,
            normalize_path(path),
            "",
            urlencode(params, doseq=True),
            "",
        )
    )
