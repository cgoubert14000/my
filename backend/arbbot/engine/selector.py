"""Best-opportunity selection: eligibility gates in a fixed order, then expected-value ranking.

EV(opportunity) = p_lower · expected_net − (1 − p_lower) · failure_cost
(p_lower = lower credible bound from the reliability engine; failure_cost = expected gas burnt by a revert).
A candidate becomes ELIGIBLE only if every gate passes; the first failing gate is recorded as the reason.
"""
from __future__ import annotations

from dataclasses import dataclass

from ..config.policy import AuthorizationPolicy
from ..config.tunables import TunableParams
from ..core.types import Decision, Opportunity
from ..reliability.model import ReliabilityModel, features_of


@dataclass
class SelectionContext:
    tunables: TunableParams
    policy: AuthorizationPolicy | None
    remaining_budget_native: float | None
    native_price_usd: float | None
    block_number: int


class Selector:
    def __init__(self, reliability: ReliabilityModel):
        self.rel = reliability

    def gate(self, opp: Opportunity, ctx: SelectionContext) -> list[str]:
        t = ctx.tunables
        reasons: list[str] = []
        pb = opp.profit
        if pb.expected_net <= 0:
            reasons.append("negative_expected_net")
        else:
            # the contract reverts below minProfit = gas + safety margin (see executor.preflight); a candidate that cannot
            # clear that floor would only burn gas, so it is never eligible — selection and execution use the same rule
            safety = int(pb.amount_in * t.safety_margin_bps) // 10_000
            if pb.expected_net < safety:
                reasons.append(f"below_safety_margin({pb.expected_net}<{safety})")
        if opp.data_age_ms > t.max_data_age_ms:
            reasons.append(f"stale_data({opp.data_age_ms:.0f}ms>{t.max_data_age_ms})")
        if pb.price_impact_bps > t.max_price_impact_bps:
            reasons.append(f"price_impact({pb.price_impact_bps:.0f}bps>{t.max_price_impact_bps})")
        if pb.fees.unknowns:
            reasons.append("unknown_costs:" + "|".join(pb.fees.unknowns))
        if opp.sim is not None:
            if not opp.sim.get("ok"):
                reasons.append(f"simulation_failed:{opp.sim.get('error')}")
            else:
                sim_profit = int(opp.sim.get("profit", 0))
                tol = int(pb.amount_in * t.sim_tolerance_bps) // 10_000
                if sim_profit + tol < pb.gross_profit - pb.fees.flash_fee:
                    reasons.append(f"sim_below_estimate({sim_profit}<{pb.gross_profit - pb.fees.flash_fee})")
                sim_net = sim_profit - pb.fees.gas_cost_token
                pb.simulated_net = sim_net
                if sim_net <= 0:
                    reasons.append("simulated_net_nonpositive")
        pol = ctx.policy
        if pol is not None:
            dexes = {h.pool.dex for h in opp.route.hops}
            if not dexes <= set(pol.allowed_dexes):
                reasons.append("dex_not_allowed:" + ",".join(sorted(dexes - set(pol.allowed_dexes))))
            if opp.flash_source.name not in pol.allowed_flash_providers:
                reasons.append(f"flash_provider_not_allowed:{opp.flash_source.name}")
            toks = {opp.route.token.symbol} | {h.token_out.symbol for h in opp.route.hops}
            if pol.allowed_tokens and not toks <= set(pol.allowed_tokens):
                reasons.append("token_not_allowed:" + ",".join(sorted(toks - set(pol.allowed_tokens))))
            if ctx.native_price_usd and pb.fees.native_price_in_token:
                net_native = pb.expected_net / pb.fees.native_price_in_token / 10**opp.route.token.decimals
                if net_native < pol.min_net_profit_native:
                    reasons.append(f"net_below_policy_min({net_native:.6f}<{pol.min_net_profit_native})")
            if ctx.remaining_budget_native is not None and pb.fees.gas_cost_wei / 1e18 > ctx.remaining_budget_native:
                reasons.append("gas_exceeds_remaining_budget")
        return reasons

    def evaluate(self, opps: list[Opportunity], ctx: SelectionContext, threshold: float) -> list[Opportunity]:
        for opp in opps:
            if opp.decision == Decision.REJECTED and "negative_expected_net" in opp.reasons:
                continue
            feats = features_of(opp)
            est = self.rel.estimate(feats)
            opp.p_success = est.p_mean
            opp.p_lower = est.p_lower
            opp.p_upper = est.p_upper
            opp.p_n = est.n
            opp.uncertainty = est.label
            feats["p_at_decision"] = est.p_lower if est.p_lower is not None else 0.0
            opp.features = feats
            reasons = self.gate(opp, ctx)
            if not est.sufficient:
                reasons.append("reliability_not_demonstrated")
            elif est.p_lower is not None and est.p_lower < threshold:
                reasons.append(f"p_lower_below_threshold({est.p_lower:.2f}<{threshold})")
            fail_cost = opp.profit.fees.failure_cost_wei / 1e18 * (opp.profit.fees.native_price_in_token or 0) * 10**opp.route.token.decimals
            p = est.p_lower if est.p_lower is not None else 0.0
            opp.ev = p * opp.profit.expected_net - (1 - p) * fail_cost
            kept = [r for r in opp.reasons if r.startswith(("unknown:", "ghost_mode:"))]
            opp.reasons = kept + [r for r in reasons if r not in kept]
            opp.decision = Decision.ELIGIBLE if not reasons else Decision.REJECTED
        return opps

    def pick(self, opps: list[Opportunity]) -> Opportunity | None:
        elig = [o for o in opps if o.decision == Decision.ELIGIBLE]
        if not elig:
            return None
        best = max(elig, key=lambda o: o.ev)
        best.decision = Decision.SELECTED
        return best
