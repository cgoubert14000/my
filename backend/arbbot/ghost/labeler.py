"""Ghost mode labeler: turns every positive-expected-net opportunity into a measured outcome.

For an opportunity detected at block N we re-simulate the exact same transaction (same route, same amount,
same on-chain minProfit=1) against the state of block N+1 — the earliest block in which our transaction could
have been included. The label is 1 when the re-simulated profit minus the gas cost (at N+1 base fee) is > 0.

This is a conservative proxy: if a competitor captured the spread anywhere in block N+1, the re-simulation
fails or returns less, and the observation is labelled 0. It cannot know whether we would have been ordered
before that competitor, so it under-estimates rather than over-estimates the success probability.
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass

from ..core.types import Opportunity
from ..reliability.model import Observation, ReliabilityModel
from ..simulation.simulator import Simulator
from ..storage.db import Database

log = logging.getLogger("arbbot.ghost")


@dataclass
class PendingLabel:
    opp: Opportunity
    detected_block: int
    label_block: int
    created: float


class GhostLabeler:
    def __init__(self, simulator: Simulator, reliability: ReliabilityModel, db: Database, fees):
        self.sim = simulator
        self.rel = reliability
        self.db = db
        self.fees = fees
        self.pending: list[PendingLabel] = []
        self.labeled = 0
        self.positives = 0
        self.errors = 0
        self.recent: list[dict] = []
        self.last_labeled_block: dict[str, int] = {}  # route_key → block of the last observation
        self.relabel_every_blocks = 30  # a persistent gap yields at most one observation per 30 blocks

    def enqueue(self, opp: Opportunity, block: int) -> bool:
        """Queue for labelling. One observation per route per block, and at most one per `relabel_every_blocks`
        for a gap that persists (ghost mode cannot close gaps, so repeats are not independent evidence)."""
        key = opp.route.key
        if any(p.opp.route.key == key and p.detected_block == block for p in self.pending):
            return False
        last = self.last_labeled_block.get(key)
        if last is not None and block - last < self.relabel_every_blocks:
            return False
        self.last_labeled_block[key] = block
        self.pending.append(PendingLabel(opp, block, block + 1, time.time()))
        if len(self.pending) > 500:
            del self.pending[:100]
        return True

    async def on_block(self, block: int) -> list[dict]:
        """Label everything whose landing block has been reached. Returns the new observations (dicts)."""
        due = [p for p in self.pending if p.label_block <= block]
        if not due:
            return []
        self.pending = [p for p in self.pending if p.label_block > block]
        out: list[dict] = []
        for p in due:
            try:
                sim = await self.sim.simulate(p.opp, min_profit=1, block=p.label_block)
            except Exception as e:  # noqa: BLE001
                self.errors += 1
                log.debug("ghost sim error: %s", e)
                continue
            fb = p.opp.profit.fees
            if sim.ok and sim.profit is not None:
                net_after = sim.profit - fb.gas_cost_token
            else:
                net_after = -int(fb.failure_cost_wei / 1e18 * fb.native_price_in_token * 10**p.opp.route.token.decimals) if fb.native_price_in_token else -fb.gas_cost_token
            label = 1 if net_after > 0 else 0
            feats = dict(p.opp.features) if p.opp.features else {}
            if not feats:
                from ..reliability.model import features_of

                feats = features_of(p.opp)
            obs = Observation(ts=time.time(), features=feats, label=label, source="ghost", route_key=p.opp.route.key,
                              net_after=float(net_after), net_expected=float(p.opp.profit.expected_net))
            self.rel.add(obs)
            self.db.add_observation(obs.ts, obs.source, obs.route_key, label, obs.net_after, obs.net_expected, feats)
            p.opp.ghost_next_block_net = net_after
            rec = p.opp.to_record()
            rec["ghost_label"] = label
            rec["ghost_sim_error"] = sim.error
            self.db.upsert_opportunity(rec)
            self.labeled += 1
            self.positives += label
            item = {"id": p.opp.id, "block": p.detected_block, "label_block": p.label_block, "label": label,
                    "expected_net": p.opp.profit.expected_net, "net_after": net_after, "sim_error": sim.error,
                    "route": p.opp.route.describe(), "token": p.opp.route.token.symbol, "decimals": p.opp.route.token.decimals}
            self.recent.append(item)
            del self.recent[:-200]
            out.append(item)
        return out

    def stats(self) -> dict:
        return {"pending": len(self.pending), "labeled": self.labeled, "positives": self.positives, "errors": self.errors,
                "rate": (self.positives / self.labeled) if self.labeled else None}
