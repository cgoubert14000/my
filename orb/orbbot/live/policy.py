"""Politique de risque gelée (ops/orb/policy.json) : le moteur la lit, la journalise (empreinte SHA-256) et ne la
modifie jamais. Toute exécution réelle est refusée si `enabled` est faux ou si une limite est atteinte."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import pathlib

from pydantic import BaseModel, Field


class RiskPolicy(BaseModel):
    enabled: bool = False                       # faux ⇒ aucune exécution (même paper) ; le journal continue
    mode: str = "paper"                         # "paper" | "oanda_practice" | "oanda_live" (live : jamais sans décision humaine)
    instrument: str = "XAU_USD"                 # nom courtier
    data_instrument: str = "XAUUSD"             # nom Dukascopy (coûts par défaut, replay)
    variant: str = "R30_fvg_rr1_structure_ma0_p0_n1_cut1130"
    risk_pct_per_trade: float = Field(0.5, ge=0.01, le=2.0)   # % du capital risqué entre entrée et stop
    max_daily_loss_r: float = Field(2.0, ge=0.5)              # perte journalière max (en R) ⇒ plus d'entrée
    max_trades_per_day: int = Field(2, ge=1, le=4)
    max_units: float = Field(5.0, gt=0)                       # taille max d'une position (unités courtier)
    max_consecutive_losses: int = Field(6, ge=1)              # série perdante ⇒ suspension (kill switch à réarmer)
    allowed_weekdays: list[int] = Field(default_factory=lambda: [0, 1, 2, 3, 4])
    kill_switch_file: str = "ops/orb/STOP"                    # présent ⇒ aucune entrée, positions fermées
    paper_equity: float = 10_000.0                            # capital fictif du mode paper
    note: str = ""

    def sha256(self) -> str:
        return hashlib.sha256(self.model_dump_json().encode()).hexdigest()[:16]

    @classmethod
    def load(cls, path: pathlib.Path) -> "RiskPolicy":
        return cls.model_validate(json.loads(path.read_text(encoding="utf-8")))

    def kill_switch_active(self, root: pathlib.Path) -> bool:
        return (root / self.kill_switch_file).exists()


class DayState(BaseModel):
    day: str = ""
    trades: int = 0
    r_total: float = 0.0
    consecutive_losses: int = 0
    refused: int = 0


def can_enter(policy: RiskPolicy, state: DayState, kill: bool, now_ny: dt.datetime) -> tuple[bool, str]:
    if not policy.enabled:
        return False, "politique désactivée (enabled=false)"
    if kill:
        return False, "kill switch actif"
    if now_ny.weekday() not in policy.allowed_weekdays:
        return False, "jour non autorisé"
    if state.trades >= policy.max_trades_per_day:
        return False, f"max {policy.max_trades_per_day} trades/jour atteint"
    if state.r_total <= -policy.max_daily_loss_r:
        return False, f"perte journalière {state.r_total:.2f} R ≤ −{policy.max_daily_loss_r} R"
    if state.consecutive_losses >= policy.max_consecutive_losses:
        return False, f"{state.consecutive_losses} pertes consécutives ≥ {policy.max_consecutive_losses} : suspendu"
    return True, "ok"


def position_units(equity: float, risk_pct: float, risk_per_unit: float, max_units: float, step: float = 1.0) -> float:
    """Taille telle que (entrée − stop) × unités = equity × risk %. Arrondie au pas inférieur, bornée, 0 si trop petit."""
    if risk_per_unit <= 0 or equity <= 0:
        return 0.0
    raw = equity * risk_pct / 100.0 / risk_per_unit
    units = (raw // step) * step
    return float(max(0.0, min(units, max_units)))
