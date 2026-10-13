"""Self-correction loop primitives: OBSERVE → DIAGNOSE → MODIFY → TEST → COMPARE → ACCEPT/ROLLBACK.

Changes are confined to `TunableParams.ALLOWED_KEYS` (anything else raises PermissionError) and are isolated in a
dedicated git repository under data/selfcorr/: every candidate is a commit on its own branch; `main` always holds
the stable reference version; acceptance = fast-forward merge, rollback = branch left for audit, main untouched.
The policy (budget, limits, allowlists, signing rules) lives elsewhere and is never touched by this module.
"""
from __future__ import annotations

import json
import logging
import pathlib
import subprocess
import time
import uuid
from dataclasses import dataclass, field

from ..config.tunables import TunableParams

log = logging.getLogger("arbbot.selfcorr")


class ParamRepo:
    def __init__(self, root: pathlib.Path):
        self.root = pathlib.Path(root)
        self.file = self.root / "tunables.json"
        self._ensure()

    def _git(self, *args: str) -> str:
        res = subprocess.run(["git", *args], cwd=self.root, capture_output=True, text=True, check=False)
        if res.returncode != 0:
            raise RuntimeError(f"git {' '.join(args)}: {res.stderr.strip()}")
        return res.stdout.strip()

    def _ensure(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        if not (self.root / ".git").exists():
            self._git("init", "-q", "-b", "main")
            self._git("config", "user.email", "arbbot@local")
            self._git("config", "user.name", "arbbot self-correction")
            self.file.write_text(json.dumps(TunableParams().as_dict(), indent=2))
            self._git("add", "tunables.json")
            self._git("commit", "-q", "-m", "reference: default tunables")

    def reference(self) -> TunableParams:
        self._git("checkout", "-q", "main")
        return TunableParams.load(self.file)

    def set_reference(self, t: TunableParams, message: str) -> str:
        self._git("checkout", "-q", "main")
        self.file.write_text(json.dumps(t.as_dict(), indent=2))
        self._git("add", "tunables.json")
        if self._git("status", "--porcelain"):
            self._git("commit", "-q", "-m", message)
        return self._git("rev-parse", "--short", "HEAD")

    def propose(self, candidate: TunableParams, description: str) -> str:
        branch = f"cand-{int(time.time())}-{uuid.uuid4().hex[:6]}"
        self._git("checkout", "-q", "main")
        self._git("checkout", "-q", "-b", branch)
        self.file.write_text(json.dumps(candidate.as_dict(), indent=2))
        self._git("add", "tunables.json")
        self._git("commit", "-q", "--allow-empty", "-m", f"candidate: {description}")
        ref = self._git("rev-parse", "--short", "HEAD")
        self._git("checkout", "-q", "main")
        return f"{branch}@{ref}"

    def accept(self, branch_ref: str) -> str:
        branch = branch_ref.split("@")[0]
        self._git("checkout", "-q", "main")
        self._git("merge", "-q", "--ff-only", branch)
        return self._git("rev-parse", "--short", "HEAD")

    def rollback(self, branch_ref: str) -> None:
        # nothing to undo: main was never modified; the branch is kept for audit
        self._git("checkout", "-q", "main")

    def log(self, n: int = 20) -> list[str]:
        return self._git("log", "--all", "--oneline", f"-{n}").splitlines()


@dataclass
class Diagnosis:
    findings: list[str] = field(default_factory=list)
    changes: dict = field(default_factory=dict)
    rationale: list[str] = field(default_factory=list)


def diagnose(obs: dict, t: TunableParams) -> Diagnosis:
    """Rule-based diagnosis from OBSERVED metrics. Every rule states what it saw and what it changes and why."""
    d = Diagnosis()
    sims = obs.get("simulations", 0)
    sim_fail = obs.get("sim_failures", 0)
    sim_below = obs.get("sim_below_estimate", 0)
    unquotable = obs.get("unquotable", 0)
    positives = obs.get("positives", 0)
    candidates = obs.get("candidates", 0)
    near_miss = obs.get("spread_near_threshold", 0)
    gas_ratio = obs.get("gas_estimate_over_model_median")
    cycle_ms = obs.get("cycle_ms_p95")
    block_ms = obs.get("block_time_ms", 2000)
    ghost_rate = obs.get("ghost_positive_rate")
    ghost_n = obs.get("ghost_labeled", 0)

    if sims >= 10 and (sim_fail + sim_below) / sims > 0.05:
        new_margin = min(t.safety_margin_bps + 2, 20)
        d.findings.append(f"{sim_fail + sim_below}/{sims} simulations below estimate or failed")
        d.changes["safety_margin_bps"] = new_margin
        d.rationale.append(f"safety_margin_bps {t.safety_margin_bps} → {new_margin}: estimates not conservative enough")
    if gas_ratio is not None and gas_ratio > 1.0:
        scale = min(gas_ratio * 1.05, 2.0)
        d.findings.append(f"gas estimate / model median = {gas_ratio:.2f} (model under-estimates)")
        d.changes["gas_units_per_hop"] = {k: int(v * scale) for k, v in t.gas_units_per_hop.items()}
        d.rationale.append(f"gas_units_per_hop × {scale:.2f}: under-estimated gas inflates expected net")
    elif gas_ratio is not None and gas_ratio < 0.7:
        d.findings.append(f"gas estimate / model median = {gas_ratio:.2f} (model over-estimates by >30 %)")
        d.changes["gas_units_per_hop"] = {k: max(int(v * 0.9), 40_000) for k, v in t.gas_units_per_hop.items()}
        d.rationale.append("gas_units_per_hop × 0.9: over-estimated gas hides small but real opportunities")
    if positives == 0 and near_miss >= 5:
        new_spread = max(round(t.min_spread_bps * 0.8, 2), 2.0)
        d.findings.append(f"no positive candidate but {near_miss} routes just below the spread threshold")
        d.changes["min_spread_bps"] = new_spread
        d.rationale.append(f"min_spread_bps {t.min_spread_bps} → {new_spread}: screen was too strict")
    if candidates and unquotable / max(candidates, 1) > 0.1:
        new_frac = max(round(t.max_borrow_fraction_of_depth * 0.8, 3), 0.05)
        d.findings.append(f"{unquotable} unquotable sizes (tick window / liquidity exhausted)")
        d.changes["max_borrow_fraction_of_depth"] = new_frac
        d.rationale.append(f"max_borrow_fraction_of_depth {t.max_borrow_fraction_of_depth} → {new_frac}")
    if ghost_n >= 20 and ghost_rate is not None and ghost_rate < 0.6:
        new_spread = round(t.min_spread_bps * 1.2, 2)
        new_age = max(int(t.max_data_age_ms * 0.75), 1000)
        d.findings.append(f"ghost positive rate {ghost_rate:.0%} over {ghost_n} labels: opportunities vanish before N+1")
        d.changes["min_spread_bps"] = new_spread
        d.changes["max_data_age_ms"] = new_age
        d.rationale.append(f"min_spread_bps → {new_spread}, max_data_age_ms → {new_age}: favour wider, fresher gaps")
    if cycle_ms is not None and cycle_ms > block_ms / 2 and t.grid_points > 8:
        d.findings.append(f"cycle p95 {cycle_ms:.0f} ms > half block time {block_ms / 2:.0f} ms")
        d.changes["grid_points"] = max(t.grid_points - 4, 8)
        d.rationale.append(f"grid_points {t.grid_points} → {d.changes['grid_points']}: latency budget")
    return d
