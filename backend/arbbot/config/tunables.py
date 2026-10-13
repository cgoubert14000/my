"""Tunable (non-critical) strategy parameters — the ONLY configuration the self-correction loop may modify.

Everything financial (budget, loss limits, allowlists, signing) lives in AuthorizationPolicy and is immutable from
the engine's point of view. `TunableParams.ALLOWED_KEYS` is the hard allowlist enforced by SelfCorrector.
"""
from __future__ import annotations

import json
import pathlib
from dataclasses import asdict, dataclass, fields


@dataclass
class TunableParams:
    version: int = 1
    # detection
    min_spread_bps: float = 1.0  # margin (bps) the raw spread must show ABOVE the sum of LP fees to be sized
    max_hops: int = 3
    max_price_impact_bps: float = 150.0
    max_data_age_ms: float = 4000.0
    min_liquidity_usd: float = 20_000.0
    # optimisation
    grid_points: int = 18
    golden_iters: int = 24
    max_optimizations_per_cycle: int = 300  # routes sized per block, best fee-adjusted spread first
    cycle_time_budget_ms: float = 1200.0  # stop sizing routes when the cycle exceeds this (keeps up with 2 s blocks)
    max_borrow_fraction_of_depth: float = 0.25  # cap borrow at a fraction of the shallowest pool depth
    # fee / gas model
    gas_safety_multiplier: float = 1.15
    gas_units_base: int = 70_000
    gas_units_per_hop: dict | None = None  # {"UNIV2":65000,"UNIV3":110000,"SOLIDLY":90000,"PANCAKE_V3":110000}
    gas_units_flash: dict | None = None  # {"BALANCER_V2":45000,"AAVE_V3":130000,"MORPHO":35000,"UNISWAP_V3":55000}
    v3_tick_cross_gas: int = 22_000
    priority_fee_floor_gwei: float = 0.001
    failure_gas_fraction: float = 0.55  # share of gas consumed by a typical revert (measured in lab)
    # selection
    safety_margin_bps: float = 2.0  # extra margin required on top of all costs
    sim_tolerance_bps: float = 1.0  # max |sim - estimate| / amount before flagging the model
    # reliability
    reliability_min_observations: int = 30
    reliability_credible_level: float = 0.90
    # pool quarantine
    quarantine_after_false_positives: int = 5

    ALLOWED_KEYS = (
        "min_spread_bps", "max_hops", "max_price_impact_bps", "max_data_age_ms", "min_liquidity_usd", "grid_points",
        "golden_iters", "max_borrow_fraction_of_depth", "gas_safety_multiplier", "gas_units_base", "gas_units_per_hop",
        "gas_units_flash", "v3_tick_cross_gas", "priority_fee_floor_gwei", "failure_gas_fraction", "safety_margin_bps",
        "sim_tolerance_bps", "reliability_min_observations", "reliability_credible_level",
        "quarantine_after_false_positives", "max_optimizations_per_cycle", "cycle_time_budget_ms",
    )

    def __post_init__(self) -> None:
        if self.gas_units_per_hop is None:
            self.gas_units_per_hop = {"UNIV2": 65_000, "UNIV3": 110_000, "SOLIDLY": 90_000, "PANCAKE_V3": 110_000}
        if self.gas_units_flash is None:
            self.gas_units_flash = {"BALANCER_V2": 45_000, "AAVE_V3": 130_000, "MORPHO": 35_000, "UNISWAP_V3": 55_000, "NONE": 0}

    def as_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def load(cls, path: pathlib.Path) -> "TunableParams":
        path = pathlib.Path(path)
        if path.exists():
            data = json.loads(path.read_text())
            known = {f.name for f in fields(cls)}
            return cls(**{k: v for k, v in data.items() if k in known})
        return cls()

    def save(self, path: pathlib.Path) -> None:
        path = pathlib.Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.as_dict(), indent=2))

    def with_changes(self, **changes) -> "TunableParams":
        for k in changes:
            if k not in self.ALLOWED_KEYS:
                raise PermissionError(f"'{k}' is not a tunable parameter (self-correction may not change it)")
        d = self.as_dict()
        d.update(changes)
        d["version"] = self.version + 1
        return TunableParams(**d)
