"""Catalogue des filtres Vinted et application à l'URL d'un profil.

Tous les identifiants de ce module ont été **vérifiés en direct sur vinted.fr**
le 20/10/2026 : la page ``/catalog`` réaffiche les filtres appliqués avec leur
libellé humain, ce qui permet de lire la correspondance id → libellé sans
disposer de l'API privée.

Deux constats importants, tous deux vérifiés :

* Vinted **ignore** les identifiants qui n'appartiennent pas à un groupe de
  tailles existant (ex. ``208`` ne renvoie aucun libellé) : mieux vaut ne rien
  envoyer que d'envoyer un identifiant inventé ;
* les identifiants de taille **dépendent de la catégorie** (``205`` = ``XS``
  pour les hauts, alors que ``1`` = ``XS / 34 / 6`` pour les tailles
  françaises). On propose donc des groupes explicites, et l'URL de recherche
  libre reste le moyen d'ajouter une taille exotique (enfant, pointure 44+).

Les filtres sont écrits dans l'URL du profil, exactement comme le fait le site
(``/catalog?catalog[]=…&size_ids[]=…``) : le moteur n'a donc rien à changer,
il continue de scraper l'URL fournie.
"""

from __future__ import annotations

from urllib.parse import parse_qsl, urlparse, urlunparse

from .categories import compose_query, category_id_from_url, build_profile_url, normalize_path

# ── États (vérifiés : status_ids[]=1 → « Neuf sans étiquette ») ───────────────
STATUSES: tuple[tuple[str, str], ...] = (
    ("6", "Neuf avec étiquette"),
    ("1", "Neuf sans étiquette"),
    ("2", "Très bon état"),
    ("3", "Bon état"),
    ("4", "Satisfaisant"),
    ("7", "Ne fonctionne pas"),
)

# ── Couleurs (vérifiées : color_ids[]=1 → « Noir » … 12 → « Blanc ») ─────────
COLORS: tuple[tuple[str, str], ...] = (
    ("1", "Noir"),
    ("2", "Marron"),
    ("3", "Gris"),
    ("4", "Beige"),
    ("5", "Fuchsia"),
    ("6", "Violet"),
    ("7", "Rouge"),
    ("8", "Jaune"),
    ("9", "Bleu"),
    ("10", "Vert"),
    ("11", "Orange"),
    ("12", "Blanc"),
)

# ── Tri ──────────────────────────────────────────────────────────────────────
ORDERS: tuple[tuple[str, str], ...] = (
    ("newest_first", "Plus récentes"),
    ("relevance", "Pertinence"),
    ("price_low_to_high", "Prix croissant"),
    ("price_high_to_low", "Prix décroissant"),
)

# ── Tailles ──────────────────────────────────────────────────────────────────
#: Chaque groupe est un bloc de cases à cocher ; ``hint`` rappelle à quoi il sert.
SIZE_GROUPS: tuple[dict, ...] = (
    {
        "key": "letters",
        "label": "Tailles lettres",
        "hint": "Hauts, robes, vestes, pantalons (la plupart des catégories).",
        "sizes": (
            ("205", "XS"),
            ("206", "S"),
            ("207", "M"),
            ("209", "L"),
            ("210", "XL"),
            ("211", "XXL"),
            ("212", "XXXL"),
            ("213", "Taille unique"),
        ),
    },
    {
        "key": "shoes",
        "label": "Pointures",
        "hint": "Chaussures, du 35 au 43 (pointures supérieures : collez une URL vinted.fr).",
        "sizes": tuple((str(20 + size), str(size)) for size in range(35, 44)),
    },
    {
        "key": "eu",
        "label": "Tailles françaises / UK / US",
        "hint": "Bloc affiché « XS / 34 / 6 » : utile pour les catégories qui n'utilisent pas les lettres.",
        "sizes": (
            ("1", "XS / 34 / 6"),
            ("2", "S / 36 / 8"),
            ("3", "M / 38 / 10"),
            ("4", "L / 40 / 12"),
            ("5", "XL / 42 / 14"),
            ("6", "XXL / 44 / 16"),
        ),
    },
)


def _sizes_from_letters() -> tuple[tuple[str, str], ...]:  # pragma: no cover - lisibilité
    return next(group["sizes"] for group in SIZE_GROUPS if group["key"] == "letters")


#: Paramètres pilotés par ce module : toujours reconstruits, jamais dupliqués.
MANAGED_PARAMS = frozenset(
    {
        "catalog[]",
        "catalog",
        "brand_ids[]",
        "brand_ids",
        "size_ids[]",
        "status_ids[]",
        "color_ids[]",
        "material_ids[]",
        "price_from",
        "price_to",
        "order",
        "page",
        "time",
    }
)

#: Alias acceptés (le site écrit parfois ``size_ids`` sans crochets).
_PARAM_ALIASES = {
    "catalog": "catalog[]",
    "brand_ids": "brand_ids[]",
    "size_ids": "size_ids[]",
    "status_ids": "status_ids[]",
    "color_ids": "color_ids[]",
    "material_ids": "material_ids[]",
}


def catalogue() -> dict:
    """Catalogue complet, prêt à être affiché par le tableau de bord."""
    return {
        "statuses": [{"id": i, "label": l} for i, l in STATUSES],
        "colors": [{"id": i, "label": l} for i, l in COLORS],
        "orders": [{"id": i, "label": l} for i, l in ORDERS],
        "size_groups": [
            {
                "key": group["key"],
                "label": group["label"],
                "hint": group["hint"],
                "sizes": [{"id": i, "label": l} for i, l in group["sizes"]],
            }
            for group in SIZE_GROUPS
        ],
        "materials": [],
        "counts": {
            "statuses": len(STATUSES),
            "colors": len(COLORS),
            "sizes": sum(len(group["sizes"]) for group in SIZE_GROUPS),
        },
    }


def _split(url: str, domain: str) -> tuple[str, str, list[tuple[str, str]]]:
    """Décompose une URL (ou un mot-clé) en (domaine, chemin, paramètres)."""
    value = (url or "").strip()
    if value.startswith(("http://", "https://")):
        parsed = urlparse(value)
        netloc = parsed.netloc or domain
        if "vinted." not in netloc.lower():
            netloc = domain
        return netloc, parsed.path or "/catalog", [
            (key, item)
            for key, item in parse_qsl(parsed.query, keep_blank_values=True)
            if key
        ]
    if value and "=" in value:
        return domain, "/catalog", [
            (key, item)
            for key, item in parse_qsl(value, keep_blank_values=True)
            if key
        ]
    if value:
        return domain, "/catalog", [("search_text", value)]
    return domain, "/catalog", []


def _clean_ids(values) -> list[str]:
    """Identifiants numériques, dédupliqués et dans l'ordre d'arrivée."""
    if isinstance(values, str):
        values = [values]
    cleaned: list[str] = []
    for value in values or []:
        text = str(value).strip()
        if text.isdigit() and text not in cleaned:
            cleaned.append(text)
    return cleaned


def read_filters(url: str) -> dict:
    """Filtres déjà présents dans une URL (pour préremplir l'interface)."""
    _, _, params = _split(url, "www.vinted.fr")
    buckets: dict[str, list[str]] = {
        "size_ids": [],
        "status_ids": [],
        "color_ids": [],
        "material_ids": [],
        "brand_ids": [],
    }
    scalars: dict[str, str] = {}
    for key, value in params:
        normalized = _PARAM_ALIASES.get(key, key)
        if normalized == "size_ids[]":
            buckets["size_ids"].extend(_clean_ids(value))
        elif normalized == "status_ids[]":
            buckets["status_ids"].extend(_clean_ids(value))
        elif normalized == "color_ids[]":
            buckets["color_ids"].extend(_clean_ids(value))
        elif normalized == "material_ids[]":
            buckets["material_ids"].extend(_clean_ids(value))
        elif normalized == "brand_ids[]":
            buckets["brand_ids"].extend(_clean_ids(value))
        elif key in {"price_from", "price_to", "order"}:
            scalars[key] = str(value).strip()
    return {
        "size_ids": buckets["size_ids"],
        "status_ids": buckets["status_ids"],
        "color_ids": buckets["color_ids"],
        "material_ids": buckets["material_ids"],
        "brand_ids": buckets["brand_ids"],
        "price_from": scalars.get("price_from", ""),
        "price_to": scalars.get("price_to", ""),
        "order": scalars.get("order", ""),
        "active": any(buckets.values()) or bool(scalars),
    }


def apply_filters(
    current_url: str,
    *,
    size_ids=(),
    status_ids=(),
    color_ids=(),
    material_ids=(),
    price_from=None,
    price_to=None,
    order=None,
    domain: str = "www.vinted.fr",
) -> str:
    """Réécrit l'URL d'un profil avec les filtres demandés.

    Le reste de l'URL (mots-clés, catégorie, marques) est conservé. Sans aucun
    filtre, on retombe sur la forme historique « chemin » de
    :func:`app.categories.build_profile_url`, afin de ne rien changer aux
    profils existants.
    """
    sizes = _clean_ids(size_ids)
    statuses = _clean_ids(status_ids)
    colors = _clean_ids(color_ids)
    materials = _clean_ids(material_ids)
    price_min = _clean_price(price_from)
    price_max = _clean_price(price_to)
    sort = str(order or "").strip() if str(order or "").strip() in {o for o, _ in ORDERS} else ""

    if not any([sizes, statuses, colors, materials, price_min, price_max, sort]):
        return build_profile_url(current_url, None, None, domain)

    netloc, _, params = _split(current_url, domain)
    cat_id = category_id_from_url(current_url)
    brands = [
        value
        for key, value in params
        if _PARAM_ALIASES.get(key, key) == "brand_ids[]" and str(value).strip().isdigit()
    ]
    brands = list(dict.fromkeys(str(value).strip() for value in brands))

    kept = [
        (key, value)
        for key, value in params
        if key not in MANAGED_PARAMS
        and _PARAM_ALIASES.get(key, key)
        not in {"catalog[]", "brand_ids[]", "size_ids[]", "status_ids[]", "color_ids[]", "material_ids[]"}
    ]

    pairs: list[tuple[str, str]] = []
    if cat_id:
        pairs.append(("catalog[]", cat_id))
    pairs.extend(("brand_ids[]", brand) for brand in brands)
    pairs.extend(("size_ids[]", size) for size in sizes)
    pairs.extend(("status_ids[]", status) for status in statuses)
    pairs.extend(("color_ids[]", color) for color in colors)
    pairs.extend(("material_ids[]", material) for material in materials)
    if price_min:
        pairs.append(("price_from", price_min))
    if price_max:
        pairs.append(("price_to", price_max))
    if sort:
        pairs.append(("order", sort))
    pairs.extend(kept)

    return urlunparse(("https", netloc, "/catalog", "", compose_query(pairs), ""))


def _clean_price(value) -> str:
    """Prix utilisateur → chaîne numérique simple (``13``, ``12.5``)."""
    if value is None or value == "":
        return ""
    try:
        number = float(str(value).replace(",", "."))
    except (TypeError, ValueError):
        return ""
    if number < 0:
        return ""
    return f"{number:g}"


def normalize_size_selection(values) -> list[str]:
    """Garde uniquement les identifiants de taille connus du catalogue.

    Évite d'envoyer à Vinted un identifiant inexistant (qui serait ignoré, mais
    brouillerait la lecture des filtres de l'utilisateur).
    """
    known = {size_id for group in SIZE_GROUPS for size_id, _ in group["sizes"]}
    return [size_id for size_id in _clean_ids(values) if size_id in known]


def describe(size_ids) -> str:
    """Libellés lisibles d'une sélection de tailles (journal, cartes profil)."""
    labels = {
        size_id: label
        for group in SIZE_GROUPS
        for size_id, label in group["sizes"]
    }
    return ", ".join(labels.get(size_id, size_id) for size_id in _clean_ids(size_ids))


def sanitize_path(path: str | None) -> str:
    """Chemin de catégorie sûr (utilisé par les endpoints de filtres)."""
    return normalize_path(path)
