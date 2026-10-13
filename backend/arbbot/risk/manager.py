"""Risk manager: bot status state machine, maturity decision, budget/loss accounting, kill switch.

Statuses (FR labels are what the UI shows):
  LEARNING                 APPRENTISSAGE            – collecting data, reliability not estimable yet
  SIMULATION               SIMULATION               – ghost mode active, criteria not all met
  RELIABILITY_INSUFFICIENT FIABILITÉ INSUFFISANTE   – enough data, measured reliability < threshold
  READY_LIMITED_LIVE       PRÊT POUR TEST RÉEL LIMITÉ (+ "AUTORISATION FINANCIÈRE MANQUANTE" when no policy)
  LIVE_ACTIVE              MODE RÉEL ACTIF
  SUSPENDED                SUSPENDU

The strategy engine cannot touch anything in here except through `record_*` observations; thresholds come
from the (read-only) AuthorizationPolicy. Suspension reasons are explicit and persisted.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum

from ..config.policy import AuthorizationPolicy
from ..reliability.model import INSUFFICIENT, ReliabilityModel


class BotStatus(str, Enum):
    LEARNING = "APPRENTISSAGE"
    SIMULATION = "SIMULATION"
    RELIABILITY_INSUFFICIENT = "FIABILITÉ INSUFFISANTE"
    READY_LIMITED_LIVE = "PRÊT POUR TEST RÉEL LIMITÉ"
    LIVE_ACTIVE = "MODE RÉEL ACTIF"
    SUSPENDED = "SUSPENDU"


@dataclass
class Criterion:
    name: str
    ok: bool
    detail: str


@dataclass
class LiveLedger:
    """Hard accounting of real spend. Only the risk manager writes here."""

    tx_count: int = 0
    gas_spent_wei: int = 0
    realized_net_native: float = 0.0  # realised profit (ETH-equivalent), can be negative
    failures: int = 0
    consecutive_failures: int = 0
    reserved_wei: int = 0  # gas reserved for in-flight transactions
    last_tx_ts: float = 0.0

    def as_dict(self) -> dict:
        return {
            "tx_count": self.tx_count, "gas_spent_native": self.gas_spent_wei / 1e18, "realized_net_native": self.realized_net_native,
            "failures": self.failures, "consecutive_failures": self.consecutive_failures, "reserved_native": self.reserved_wei / 1e18,
            "last_tx_ts": self.last_tx_ts,
        }


@dataclass
class RiskState:
    status: BotStatus = BotStatus.LEARNING
    sub_status: str = ""
    suspended_reason: str = ""
    suspended_at: float = 0.0
    kill_switch: bool = False
    criteria: list[Criterion] = field(default_factory=list)
    last_eval_ts: float = 0.0


class RiskManager:
    def __init__(self, policy: AuthorizationPolicy, reliability: ReliabilityModel, *, tests_passed: bool = False,
                 contract_tested: bool = False, financial_math_validated: bool = False, emergency_stop_ok: bool = True):
        self.policy = policy
        self.rel = reliability
        self.state = RiskState()
        self.ledger = LiveLedger()
        self.flags = {
            "tests_passed": tests_passed,
            "contract_tested": contract_tested,
            "financial_math_validated": financial_math_validated,
            "emergency_stop_ok": emergency_stop_ok,
            "critical_issues": [],
            "simulations_ok": 0,
            "simulations_failed": 0,
            "sim_mismatch_recent": 0,
            "data_stale": False,
            "rpc_degraded": False,
        }
        self.manual_live_enabled = True  # operator can forbid live even if everything is green

    # ------------------------------------------------------------------ kill switch & suspension

    def kill(self, reason: str) -> None:
        self.state.kill_switch = True
        self.suspend(f"kill switch: {reason}")

    def suspend(self, reason: str) -> None:
        if self.state.status != BotStatus.SUSPENDED:
            self.state.suspended_at = time.time()
        self.state.status = BotStatus.SUSPENDED
        self.state.suspended_reason = reason

    def clear_kill(self) -> None:
        """Operator action only (API/CLI); never called by the engine."""
        self.state.kill_switch = False
        self.state.suspended_reason = ""

    # ------------------------------------------------------------------ live accounting

    def can_afford(self, gas_limit: int, max_fee_per_gas: int) -> tuple[bool, str]:
        worst = gas_limit * max_fee_per_gas
        p = self.policy
        if worst > p.max_gas_per_tx_native * 1e18:
            return False, f"worst-case gas {worst / 1e18:.6f} > per-tx cap {p.max_gas_per_tx_native}"
        if self.ledger.gas_spent_wei + self.ledger.reserved_wei + worst > p.max_total_budget_native * 1e18:
            return False, "total gas budget would be exceeded"
        if self.ledger.tx_count >= p.max_transactions:
            return False, "transaction count cap reached"
        if gas_limit > p.max_gas_limit:
            return False, f"gas limit {gas_limit} > policy max {p.max_gas_limit}"
        if max_fee_per_gas > p.max_fee_per_gas_gwei * 1e9:
            return False, "max fee per gas above policy cap"
        return True, "ok"

    def reserve(self, wei: int) -> None:
        self.ledger.reserved_wei += wei

    def release(self, wei: int) -> None:
        self.ledger.reserved_wei = max(0, self.ledger.reserved_wei - wei)

    def record_execution(self, *, success: bool, gas_cost_wei: int, realized_net_native: float) -> None:
        self.ledger.tx_count += 1
        self.ledger.gas_spent_wei += gas_cost_wei
        self.ledger.realized_net_native += realized_net_native
        self.ledger.last_tx_ts = time.time()
        if success and realized_net_native > 0:
            self.ledger.consecutive_failures = 0
        else:
            self.ledger.failures += 1
            self.ledger.consecutive_failures += 1
        self._check_live_limits()

    def _check_live_limits(self) -> None:
        p = self.policy
        loss = -min(self.ledger.realized_net_native, 0.0)
        if loss >= p.max_cumulative_loss_native > 0:
            self.suspend(f"loss limit reached ({loss:.6f} ≥ {p.max_cumulative_loss_native})")
        elif self.ledger.consecutive_failures >= p.max_consecutive_failures > 0:
            self.suspend(f"{self.ledger.consecutive_failures} consecutive failures")
        elif self.ledger.gas_spent_wei >= p.max_total_budget_native * 1e18 > 0:
            self.suspend("gas budget exhausted")
        elif self.ledger.tx_count >= p.max_transactions > 0:
            self.suspend("transaction cap reached")

    # ------------------------------------------------------------------ maturity decision

    def evaluate(self, *, policy_signer_ok: bool, data_age_ms: float | None, rpc_ok: bool) -> RiskState:
        rel = self.rel.calibration_report()
        crit: list[Criterion] = []
        crit.append(Criterion("tests_passed", self.flags["tests_passed"], "pytest + forge suites green"))
        crit.append(Criterion("contract_tested", self.flags["contract_tested"], "unit/fuzz/invariant + real-V3 tests"))
        crit.append(Criterion("financial_math_validated", self.flags["financial_math_validated"], "bit-exact vs chain + sim≈estimate"))
        crit.append(Criterion("no_critical_issues", not self.flags["critical_issues"], "; ".join(self.flags["critical_issues"]) or "none"))
        sims_ok, sims_fail = self.flags["simulations_ok"], self.flags["simulations_failed"]
        crit.append(Criterion("simulations_realistic", sims_ok >= 20 and sims_fail <= sims_ok, f"{sims_ok} ok / {sims_fail} failed"))
        n = rel.get("n", 0)
        sufficient = n >= self.rel.min_obs
        crit.append(Criterion("reliability_documented", sufficient, f"n={n} (min {self.rel.min_obs}); {rel.get('label')}"))
        lower = rel.get("global_lower")
        crit.append(Criterion("p_success_ge_threshold", bool(sufficient and lower is not None and lower >= self.policy.min_success_probability),
                              f"lower bound {lower:.3f} vs {self.policy.min_success_probability}" if lower is not None else "n/a"))
        crit.append(Criterion("emergency_stop_ok", self.flags["emergency_stop_ok"] and not self.state.kill_switch, "pause + kill switch tested"))
        ok_pol, why_pol = self.policy.is_valid_now()
        crit.append(Criterion("budget_and_limits_configured", ok_pol, why_pol))
        crit.append(Criterion("signer_available", policy_signer_ok, "signer service reachable & key matches policy wallet"))
        fresh = data_age_ms is not None and data_age_ms < 10_000
        crit.append(Criterion("data_fresh", fresh and rpc_ok, f"data age {data_age_ms:.0f} ms, rpc_ok={rpc_ok}" if data_age_ms is not None else "no data"))
        drift, drift_msg = self.rel.drift_detected()
        crit.append(Criterion("model_calibrated", not drift, drift_msg))
        self.state.criteria = crit
        self.state.last_eval_ts = time.time()

        if self.state.kill_switch:
            self.state.status = BotStatus.SUSPENDED
            return self.state
        if self.state.status == BotStatus.SUSPENDED:
            # may only leave suspension when everything is green AND the policy allows auto-resume
            if all(c.ok for c in crit) and self.policy.auto_resume_after_suspension:
                self.state.status = BotStatus.READY_LIMITED_LIVE
                self.state.sub_status = "auto-resumed after suspension"
            return self.state

        technical = [c for c in crit if c.name not in ("budget_and_limits_configured", "signer_available")]
        if not sufficient:
            self.state.status = BotStatus.LEARNING
            self.state.sub_status = INSUFFICIENT
        elif lower is not None and lower < self.policy.min_success_probability:
            self.state.status = BotStatus.RELIABILITY_INSUFFICIENT
            self.state.sub_status = f"borne inférieure {lower:.1%} < {self.policy.min_success_probability:.0%}"
        elif not all(c.ok for c in technical):
            self.state.status = BotStatus.SIMULATION
            self.state.sub_status = "critères techniques non satisfaits: " + ", ".join(c.name for c in technical if not c.ok)
        elif not (ok_pol and policy_signer_ok):
            self.state.status = BotStatus.READY_LIMITED_LIVE
            self.state.sub_status = "PRÊT POUR TEST RÉEL — AUTORISATION FINANCIÈRE MANQUANTE"
        elif not self.manual_live_enabled:
            self.state.status = BotStatus.READY_LIMITED_LIVE
            self.state.sub_status = "exécution réelle désactivée par l'opérateur"
        else:
            self.state.status = BotStatus.LIVE_ACTIVE if self.state.status == BotStatus.LIVE_ACTIVE else BotStatus.READY_LIMITED_LIVE
            self.state.sub_status = "tous les critères satisfaits"
        return self.state

    def activate_live(self) -> bool:
        if self.state.status == BotStatus.READY_LIMITED_LIVE and self.state.sub_status == "tous les critères satisfaits":
            self.state.status = BotStatus.LIVE_ACTIVE
            return True
        return False

    def degrade(self, reason: str) -> None:
        """Called by the live loop when conditions deteriorate: back to simulation (not a hard suspension)."""
        if self.state.status == BotStatus.LIVE_ACTIVE:
            self.state.status = BotStatus.SIMULATION
            self.state.sub_status = f"retour en simulation: {reason}"

    def as_dict(self) -> dict:
        return {
            "status": self.state.status.value,
            "status_code": self.state.status.name,
            "sub_status": self.state.sub_status,
            "suspended_reason": self.state.suspended_reason,
            "kill_switch": self.state.kill_switch,
            "criteria": [{"name": c.name, "ok": c.ok, "detail": c.detail} for c in self.state.criteria],
            "ledger": self.ledger.as_dict(),
            "policy": self.policy.summary(),
            "flags": {k: v for k, v in self.flags.items()},
            "manual_live_enabled": self.manual_live_enabled,
        }
