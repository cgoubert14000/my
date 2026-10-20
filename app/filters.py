"""Moteur de filtrage local : prix, mots-clés, blacklist, vendeur.

Vinted applique déjà le prix et la recherche plein texte, mais la blacklist
stricte (copie, faux, défaut, taché…) et les seuils vendeur sont vérifiés ici,
sur le titre **et** la description, pour ne jamais envoyer une alerte indésirable.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache

from .utils import normalize_text


@dataclass
class MatchResult:
    matched: bool
    reason: str = ""

    def __bool__(self) -> bool:  # pragma: no cover - confort
        return self.matched


def _term_pattern(term: str) -> re.Pattern[str]:
    """Mot-clé → regex tolérante (accents déjà retirés, pluriels/féminins)."""
    normalized = normalize_text(term)
    if not normalized:
        return re.compile(r"(?!x)x")
    escaped = re.escape(normalized)
    # \b ne fonctionne pas sur les accents supprimés d'où la frontière explicite.
    return re.compile(rf"(?<![a-z0-9]){escaped}", re.I)


@lru_cache(maxsize=2048)
def _cached_pattern(term: str) -> re.Pattern[str]:
    return _term_pattern(term)


def find_terms(haystack: str, terms: list[str]) -> list[str]:
    text = normalize_text(haystack)
    return [term for term in terms if _cached_pattern(term).search(text)]


def build_haystack(item: dict) -> str:
    return " ".join(
        str(item.get(key) or "")
        for key in ("title", "description", "brand", "size", "condition")
    )


def matches_profile(profile: dict, item: dict) -> MatchResult:
    """Applique tous les filtres d'un profil à une annonce normalisée."""
    price = item.get("price")
    min_price = profile.get("min_price")
    max_price = profile.get("max_price")
    if price is None:
        return MatchResult(False, "prix illisible")
    if min_price is not None and float(price) < float(min_price):
        return MatchResult(False, f"prix {price} < minimum {min_price}")
    if max_price is not None and float(price) > float(max_price):
        return MatchResult(False, f"prix {price} > maximum {max_price}")

    if item.get("is_closed"):
        return MatchResult(False, "annonce clôturée")
    if item.get("is_hidden"):
        return MatchResult(False, "annonce masquée")

    haystack = build_haystack(item)
    blacklist = profile.get("blacklist") or []
    blocked = find_terms(haystack, blacklist)
    if blocked:
        return MatchResult(False, f"blacklist : « {blocked[0]} »")

    whitelist = profile.get("whitelist") or []
    if whitelist:
        hits = find_terms(haystack, whitelist)
        mode = (profile.get("keyword_mode") or "any").lower()
        if mode == "all" and len({normalize_text(hit) for hit in hits}) < len(
            {normalize_text(term) for term in whitelist}
        ):
            missing = [
                term
                for term in whitelist
                if normalize_text(term) not in {normalize_text(hit) for hit in hits}
            ]
            return MatchResult(False, f"mots-clés manquants : {', '.join(missing[:3])}")
        if mode != "all" and not hits:
            return MatchResult(False, "aucun mot-clé de la whitelist")

    rating = item.get("seller_rating")
    min_rating = profile.get("min_seller_rating")
    if (
        min_rating is not None
        and rating is not None
        and float(rating) < float(min_rating)
    ):
        return MatchResult(False, f"note vendeur {rating}/5 < {min_rating}/5")

    min_feedback = profile.get("min_seller_feedback")
    feedback = item.get("seller_feedback")
    if (
        min_feedback is not None
        and feedback is not None
        and int(feedback) < int(min_feedback)
    ):
        return MatchResult(False, f"{feedback} avis vendeur < {min_feedback}")
    if min_feedback and feedback is None:
        return MatchResult(False, "nombre d'avis vendeur inconnu (seuil défini)")

    return MatchResult(True)


def needs_description(profile: dict) -> bool:
    """Une description est-elle nécessaire pour trancher les filtres ?"""
    return bool(
        profile.get("check_description", True)
        and ((profile.get("blacklist") or []) or (profile.get("whitelist") or []))
    )
