"""Paramètres d'une variante ORB et génération de la grille.

Chaque dimension correspond à une question du cahier des charges (« 5, 15 ou 30 minutes ? RR 1, 2 ou 3 ?
retest/confirmation ? filtres ? TP partiel + break-even ? ») ; la grille complète compte 1 296 variantes.
"""
from __future__ import annotations

import itertools
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class OrbParams:
    range_minutes: int = 30       # durée du range d'ouverture (minutes à partir de 09:30 New York)
    confirm: str = "close"        # "close" : clôture 1 min au-delà du range ; "fvg" : cassure puis retest d'une FVG
    rr: float = 1.0               # take-profit = rr × risque
    stop: str = "opposite"        # "opposite" : autre borne du range ; "mid" : milieu du range ; "structure" : extrême de la bougie de cassure / bord opposé de la FVG
    ma: int = 0                   # 0 : pas de filtre ; 50/200 : EMA sur clôtures 1 min, on ne prend que dans le sens de la tendance
    partial: bool = False         # 50 % à 1R puis stop au point d'entrée, le reste à rr (sans effet si rr ≤ 1)
    max_trades: int = 1           # trades par jour (1, ou 2 : un second signal après la sortie du premier)
    entry_cutoff: str = "11:30"   # heure New York après laquelle aucune nouvelle entrée
    flat_at: str = "15:55"        # heure New York à laquelle tout est clôturé

    def key(self) -> str:
        return (f"R{self.range_minutes}_{self.confirm}_rr{self.rr:g}_{self.stop}_ma{self.ma}_p{int(self.partial)}"
                f"_n{self.max_trades}_cut{self.entry_cutoff.replace(':', '')}")

    def as_dict(self) -> dict:
        return asdict(self)

    def describe(self) -> str:
        c = {"close": "clôture hors range", "fvg": "cassure + retest FVG"}[self.confirm]
        s = {"opposite": "stop = borne opposée", "mid": "stop = milieu du range", "structure": "stop = structure (bougie/FVG)"}[self.stop]
        extra = []
        if self.ma:
            extra.append(f"filtre EMA{self.ma}")
        if self.partial and self.rr > 1:
            extra.append("TP partiel 1R + break-even")
        if self.max_trades > 1:
            extra.append(f"{self.max_trades} trades/jour")
        return f"range {self.range_minutes} min, {c}, RR {self.rr:g}, {s}, entrées jusqu'à {self.entry_cutoff}" + (", " + ", ".join(extra) if extra else "")


def hhmm_to_minutes(s: str) -> int:
    h, m = s.split(":")
    return int(h) * 60 + int(m)


FULL_GRID = {
    "range_minutes": (5, 15, 30),
    "confirm": ("close", "fvg"),
    "rr": (1.0, 2.0, 3.0),
    "stop": ("opposite", "mid", "structure"),
    "ma": (0, 50, 200),
    "partial": (False, True),
    "max_trades": (1, 2),
    "entry_cutoff": ("11:30", "13:00"),
}

QUICK_GRID = {
    "range_minutes": (15, 30),
    "confirm": ("close", "fvg"),
    "rr": (1.0, 2.0),
    "stop": ("opposite", "structure"),
    "ma": (0, 200),
    "partial": (False,),
    "max_trades": (1,),
    "entry_cutoff": ("11:30",),
}


def grid(spec: dict | None = None) -> list[OrbParams]:
    spec = spec or FULL_GRID
    keys = list(spec)
    out: list[OrbParams] = []
    seen: set[str] = set()
    for combo in itertools.product(*(spec[k] for k in keys)):
        p = OrbParams(**dict(zip(keys, combo)))
        if p.partial and p.rr <= 1:  # identique à partial=False : ne pas compter deux fois la même variante
            p = OrbParams(**{**p.as_dict(), "partial": False})
        if p.key() in seen:
            continue
        seen.add(p.key())
        out.append(p)
    return out


VIDEO_CLAIM = OrbParams(range_minutes=30, confirm="fvg", rr=1.0, stop="structure", ma=0, partial=False, max_trades=1, entry_cutoff="11:30")
"""La variante annoncée dans la vidéo (« or, range 30 min, exécution 1 min, retest FVG, RR 1 → profit factor ≈ 1,75 ») —
à vérifier, jamais supposée vraie."""
