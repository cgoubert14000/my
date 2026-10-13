"""Opportunity detector: per block, screen routes by spread, optimise size, price every cost, emit candidates.

Produces `Opportunity` objects with a full ProfitBreakdown and a list of rejection reasons (kept for every
negative result — ghost mode needs the negatives as much as the positives).
"""
from __future__ import annotations

import logging
import time
import uuid
from dataclasses import dataclass, field

from ..config.chains import ChainConfig
from ..config.tunables import TunableParams
from ..core.pricing import QuoteError
from ..core.types import Decision, DexKind, FlashSource, Opportunity, ProfitBreakdown, Route, Token
from ..data.collector import StateCollector
from .fees import FeeCalculator
from .optimizer import max_borrow_for_route, optimize_amount
from .routes import RouteTable
from .screen import RouteScreen

log = logging.getLogger("arbbot.detector")


@dataclass
class DetectorStats:
    cycles: int = 0
    routes_screened: int = 0
    routes_optimized: int = 0
    candidates: int = 0
    positive_net: int = 0
    last_cycle_ms: float = 0.0
    last_screen_ms: float = 0.0
    rejections: dict[str, int] = field(default_factory=dict)

    def reject(self, reason: str) -> None:
        self.rejections[reason] = self.rejections.get(reason, 0) + 1

    def as_dict(self) -> dict:
        return {
            "cycles": self.cycles,
            "routes_screened": self.routes_screened,
            "routes_optimized": self.routes_optimized,
            "candidates": self.candidates,
            "positive_net": self.positive_net,
            "last_cycle_ms": round(self.last_cycle_ms, 1),
            "last_screen_ms": round(self.last_screen_ms, 1),
            "rejections": dict(sorted(self.rejections.items(), key=lambda kv: -kv[1])[:12]),
        }


class OpportunityDetector:
    def __init__(self, chain: ChainConfig, collector: StateCollector, fees: FeeCalculator, tunables: TunableParams,
                 eur_per_usd: float = 0.92):
        self.chain = chain
        self.collector = collector
        self.fees = fees
        self.t = tunables
        self.eur_per_usd = eur_per_usd
        self.stats = DetectorStats()
        self.false_positive_counts: dict[str, int] = {}
        self._screen: RouteScreen | None = None
        self._screen_key: tuple[int, int] = (0, 0)

    def _screen_for(self, routes: "RouteTable | list[Route]") -> RouteScreen:
        """Index/sign matrices are rebuilt only when the route set object or its length changes."""
        key = (id(routes), len(routes))
        if self._screen is None or key != self._screen_key:
            self._screen = RouteScreen(routes)
            self._screen_key = key
        return self._screen

    def set_tunables(self, t: TunableParams) -> None:
        self.t = t
        self.fees.t = t

    # ------------------------------------------------------------------

    def _min_amount(self, token: Token) -> int:
        usd = self.fees.token_price_usd(token) or 1.0
        return max(1, int(1.0 / usd * 10**token.decimals))  # ≈ $1

    def _policy_cap(self, token: Token, max_borrow_usd: float | None) -> int | None:
        if not max_borrow_usd:
            return None
        usd = self.fees.token_price_usd(token)
        if not usd:
            return None
        return int(max_borrow_usd / usd * 10**token.decimals)

    async def scan(self, routes: "RouteTable | list[Route]", block: int, *, max_borrow_usd: float | None = None,
                   only_positive: bool = False) -> list[Opportunity]:
        t0 = time.perf_counter()
        self.stats.cycles += 1
        out: list[Opportunity] = []
        gas = self.collector.gas
        # 1) cheap screen: a cycle whose raw mid-price spread is below the sum of LP fees cannot have a positive gross
        #    profit at ANY size (out = in · ∏mid · ∏(1−fee) · impact ≤ in · ∏mid · ∏(1−fee)); min_spread_bps is the
        #    extra margin required on top of the fees. Survivors are sized best-edge first within a time budget.
        #    (vectorised: ~ms for 2e5 routes, see engine/screen.py — the per-route Python loop took 7 s on Base)
        screen = self._screen_for(routes)
        sr = screen.run(min_spread_bps=self.t.min_spread_bps, min_liquidity_usd=self.t.min_liquidity_usd, price_usd=self.fees.token_price_usd)
        self.stats.routes_screened += len(routes)
        for why, n in sr.rejections.items():
            self.stats.rejections[why] = self.stats.rejections.get(why, 0) + n
        self.stats.last_screen_ms = (time.perf_counter() - t0) * 1000
        budget_s = self.t.cycle_time_budget_ms / 1000.0
        for i, ri in enumerate(sr.survivors):
            if i >= self.t.max_optimizations_per_cycle or (time.perf_counter() - t0) > budget_s:
                self.stats.reject("cycle_budget_exhausted")
                continue
            route = screen.table.route(int(ri))
            spread = float(sr.spread_bps[ri])
            token = route.token
            cap_policy = self._policy_cap(token, max_borrow_usd)
            provider_cap = self.fees.provider_capacity(token) or None
            upper = max_borrow_for_route(route, self.t.max_borrow_fraction_of_depth, provider_cap, cap_policy)
            lower = self._min_amount(token)
            if upper <= lower:
                self.stats.reject("borrow_bound_too_small")
                continue
            # provider choice (cheapest with capacity for the upper bound; refined after sizing)
            prov = self.fees.best_provider(token, lower)
            if prov is None:
                self.stats.reject("no_flash_provider")
                continue
            self.stats.routes_optimized += 1
            res = optimize_amount(route, flash_fee_bps_x100=prov.fee_bps_x100, min_amount=lower, max_amount=upper,
                                  grid_points=self.t.grid_points, golden_iters=self.t.golden_iters,
                                  max_impact_bps=self.t.max_price_impact_bps)
            if res.quote is None:
                self.stats.reject("unquotable")
                continue
            prov2 = self.fees.best_provider(token, res.amount_in) or prov
            if prov2.source != prov.source:
                res = optimize_amount(route, flash_fee_bps_x100=prov2.fee_bps_x100, min_amount=lower, max_amount=upper,
                                      grid_points=self.t.grid_points, golden_iters=self.t.golden_iters,
                                      max_impact_bps=self.t.max_price_impact_bps)
                prov = prov2
                if res.quote is None:
                    self.stats.reject("unquotable")
                    continue
            q = res.quote
            fb = await self.fees.breakdown(route, prov.source, res.amount_in, q.ticks_crossed, q.swap_fees_in_start_token, gas)
            gross = q.amount_out - res.amount_in
            expected_net = gross - fb.flash_fee - fb.gas_cost_token
            pb = ProfitBreakdown(
                amount_in=res.amount_in, amount_out=q.amount_out, gross_profit=gross, expected_net=expected_net, fees=fb,
                margin_bps=(expected_net / res.amount_in * 10_000) if res.amount_in else 0.0,
                price_impact_bps=q.price_impact_bps,
            )
            usd = self.fees.token_price_usd(token)
            if usd:
                pb.expected_net_eur = expected_net / 10**token.decimals * usd * self.eur_per_usd
            opp = Opportunity(
                id=uuid.uuid4().hex[:12], ts=time.time(), chain_id=self.chain.chain_id, block_number=block, route=route,
                flash_source=prov.source, flash_provider=prov.address, profit=pb, spread_bps=spread,
                data_age_ms=self.collector.data_age_ms([h.pool for h in route.hops]),
            )
            self.stats.candidates += 1
            if expected_net <= 0:
                opp.decision = Decision.REJECTED
                opp.reasons.append("negative_expected_net")
                self.stats.reject("negative_expected_net")
                if only_positive:
                    continue
            else:
                self.stats.positive_net += 1
            if fb.unknowns:
                opp.reasons.extend(f"unknown:{u}" for u in fb.unknowns)
            out.append(opp)
        self.stats.last_cycle_ms = (time.perf_counter() - t0) * 1000
        return out
