"""Petites fonctions partagées : texte, prix, dates, URLs Vinted."""

from __future__ import annotations

import re
import unicodedata
from datetime import datetime, timezone
from urllib.parse import urlparse

# www.vinted.fr, vinted.co.uk, vinted.de, ...
VINTED_HOST_RE = re.compile(
    r"^(?:[a-z0-9-]+\.)*vinted\.[a-z]{2,}(?:\.[a-z]{2,})?$", re.I
)

CURRENCY_SYMBOLS = {
    "EUR": "€",
    "GBP": "£",
    "USD": "$",
    "CHF": "CHF",
    "PLN": "zł",
    "CZK": "Kč",
    "SEK": "kr",
    "DKK": "kr",
    "HUF": "Ft",
    "RON": "lei",
}

_APOSTROPHES = str.maketrans({"’": "'", "‘": "'", "`": "'"})


# ── Texte ──────────────────────────────────────────────────────────────────────


def normalize_text(value: str | None) -> str:
    """Minuscules, sans accents, apostrophes uniformes, espaces compactés."""
    if not value:
        return ""
    text = str(value).translate(_APOSTROPHES)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", text.lower()).strip()


def clean_terms(values) -> list[str]:
    """Nettoie une liste de mots-clés (déduplique, retire les vides)."""
    if not values:
        return []
    if isinstance(values, str):
        values = re.split(r"[,;\n]", values)
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        term = re.sub(r"\s+", " ", str(value)).strip()
        if not term or len(term) > 80:
            continue
        key = normalize_text(term)
        if key in seen:
            continue
        seen.add(key)
        result.append(term)
    return result[:60]


def mask_webhook(url: str | None) -> str:
    """Masque le token d'un webhook Discord pour l'affichage / les logs."""
    if not url:
        return ""
    return re.sub(r"(/api/webhooks/\d+/)([\w-]+)", r"\1••••••", url)


# ── Nombres & prix ────────────────────────────────────────────────────────────


def parse_money(value) -> tuple[float | None, str]:
    """Accepte ``12.5``, ``"12,50"`` ou ``{"amount": "12.50", "currency_code": "EUR"}``."""
    currency = "EUR"
    amount = value
    if isinstance(value, dict):
        currency = value.get("currency_code") or value.get("currency") or currency
        amount = (
            value.get("amount")
            if value.get("amount") is not None
            else value.get("cents")
        )
    if amount is None or amount == "":
        return None, currency
    if isinstance(amount, str):
        cleaned = re.sub(r"[^0-9,.\-]", "", amount).replace(",", ".")
        if cleaned.count(".") > 1:  # séparateurs de milliers : 1.234.56
            cleaned = cleaned.replace(".", "", cleaned.count(".") - 1)
        amount = cleaned
    try:
        number = float(amount)
    except (TypeError, ValueError):
        return None, currency
    return round(number, 2), str(currency).upper()


def format_money(amount: float | None, currency: str = "EUR") -> str:
    if amount is None:
        return "—"
    if abs(amount - round(amount)) < 1e-9:
        rendered = f"{int(round(amount)):,}".replace(",", " ")
    else:
        rendered = f"{amount:.2f}".replace(".", ",")
    symbol = CURRENCY_SYMBOLS.get((currency or "EUR").upper())
    return f"{rendered} {symbol}" if symbol else f"{rendered} {currency}"


def format_rating(reputation) -> float | None:
    """Vinted renvoie une réputation 0→1 : on la convertit en note sur 5."""
    if reputation is None or reputation == "":
        return None
    try:
        value = float(reputation)
    except (TypeError, ValueError):
        return None
    if value <= 1.0001:
        value *= 5
    return round(min(max(value, 0.0), 5.0), 1)


# ── URLs ──────────────────────────────────────────────────────────────────────


def is_vinted_host(host: str | None) -> bool:
    return bool(host) and bool(VINTED_HOST_RE.match(host.split(":")[0]))


def origin_of(url: str) -> str:
    parsed = urlparse(url if "://" in url else f"https://{url}")
    return f"{parsed.scheme or 'https'}://{parsed.netloc}"


def domain_of(url: str | None, default: str = "www.vinted.fr") -> str:
    if not url:
        return default
    raw = url.strip()
    if not raw.startswith(("http://", "https://")):
        raw = f"https://{raw}"
    host = urlparse(raw).netloc.lower()
    return host or default


def absolute_url(value: str | None, origin: str) -> str:
    if not value:
        return origin
    if value.startswith(("http://", "https://")):
        return value
    return f"{origin.rstrip('/')}/{value.lstrip('/')}"


# ── Dates ─────────────────────────────────────────────────────────────────────


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def utcnow_iso() -> str:
    return utcnow().isoformat(timespec="seconds")


def utcnow_iso_ms() -> str:
    """Horodatage à la milliseconde (tri fin du flux d'annonces)."""
    return utcnow().isoformat(timespec="milliseconds")


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def human_duration(seconds: float | int | None) -> str:
    if seconds is None:
        return "—"
    seconds = int(max(0, seconds))
    if seconds < 60:
        return f"{seconds}s"
    minutes, sec = divmod(seconds, 60)
    if minutes < 60:
        return f"{minutes} min {sec:02d}s" if sec and minutes < 10 else f"{minutes} min"
    hours, minutes = divmod(minutes, 60)
    if hours < 24:
        return f"{hours} h {minutes:02d}"
    days, hours = divmod(hours, 24)
    return f"{days} j {hours:02d} h"
