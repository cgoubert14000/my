"""Réglages et calculs du mode « temps réel » (détection à la seconde).

Le principe : un profil ne dort pas 60 s entre deux scans. Il interroge le
catalogue en continu avec un intervalle **adaptatif** :

* une nouveauté vient d'être vue → on reste au plus rapide quelques instants
  (rafale), pour attraper les annonces publiées juste après ;
* rien de neuf depuis un moment → l'intervalle croît progressivement jusqu'à
  un plafond raisonnable, pour ne pas se faire bloquer par Datadome.

Tout est calculé ici, hors du moteur, pour rester testable sans réseau.
"""

from __future__ import annotations

import random
from dataclasses import dataclass

#: Bornes de sécurité (en secondes) : jamais plus rapide que ça côté réseau.
HARD_MIN_INTERVAL = 0.5


@dataclass(frozen=True)
class LiveSettings:
    """Paramètres du mode temps réel, lus dans ``config.json``."""

    min_interval: float = 1.5
    max_interval: float = 10.0
    growth: float = 1.6
    burst_seconds: float = 90.0
    jitter: float = 0.15
    turbo: bool = False

    @classmethod
    def from_config(cls, config) -> LiveSettings:
        if config is None:  # pragma: no cover - confort
            return cls()

        def number(key: str, default: float, low: float, high: float) -> float:
            try:
                value = float(config.get(key, default))
            except (TypeError, ValueError):
                return default
            return max(low, min(high, value))

        min_interval = number(
            "engine.realtime_min_interval", 1.5, HARD_MIN_INTERVAL, 60
        )
        max_interval = number("engine.realtime_max_interval", 10.0, 2, 600)
        if max_interval < min_interval:
            max_interval = min_interval
        return cls(
            min_interval=min_interval,
            max_interval=max_interval,
            growth=number("engine.realtime_growth", 1.6, 1.0, 4.0),
            burst_seconds=number("engine.realtime_burst_seconds", 90, 0, 3600),
            jitter=number("engine.realtime_jitter", 0.15, 0, 0.6),
            turbo=bool(config.get("engine.realtime_turbo", False)),
        )

    def describe(self) -> str:
        if self.turbo:
            return f"turbo · {self.min_interval:g}s"
        return f"{self.min_interval:g}–{self.max_interval:g}s"


def next_interval(
    current: float | None,
    *,
    new_items: int = 0,
    since_last_found: float | None = None,
    settings: LiveSettings | None = None,
    rng: random.Random | None = None,
) -> float:
    """Intervalle avant le prochain passage sur un profil.

    * ``new_items > 0`` → rafale : on revient à l'intervalle minimal ;
    * une annonce a été vue récemment (``since_last_found`` < rafale) → minimal ;
    * sinon → croissance géométrique bornée par ``max_interval``.

    Un jitter aléatoire est appliqué pour éviter un rythme parfaitement
    robotique (et pour désynchroniser plusieurs profils).
    """
    settings = settings or LiveSettings()
    randomizer = rng or random
    low = max(HARD_MIN_INTERVAL, settings.min_interval)
    high = max(low, settings.max_interval)

    if settings.turbo:
        base = low
    elif new_items > 0:
        base = low
    elif (
        since_last_found is not None
        and since_last_found >= 0
        and since_last_found < settings.burst_seconds
    ):
        base = low
    else:
        previous = current if current and current > 0 else low
        base = max(low, min(high, previous * max(1.0, settings.growth)))

    if settings.jitter and base > 0:
        spread = base * settings.jitter
        base += randomizer.uniform(-spread / 2, spread / 2)
    return round(max(HARD_MIN_INTERVAL, min(high, base)), 2)


def is_live(profile: dict, config) -> bool:
    """Le profil doit-il être suivi en continu ?"""
    if not bool(config.get("engine.live_mode", True)):
        return False
    return bool(profile.get("live_mode", True))
