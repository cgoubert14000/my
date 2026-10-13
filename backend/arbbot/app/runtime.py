"""Runtime: wires every module together and runs the block-driven decision loop.

Loop per block (collector → detector → selector → simulator → ghost/live):
  1. collector refreshed pool states for block N (multicall) and published N
  2. detector: screen routes, optimise borrow size, price all costs → candidates (positives and negatives)
  3. selector: reliability estimate + eligibility gates → ELIGIBLE / REJECTED with reasons
  4. simulator: eth_call of the full tx for the top candidates (positive expected net) → sim net
  5. risk manager: status machine decides ghost (record only) vs live (pre-flight → signer → broadcast)
  6. ghost labeler: at N+1, re-simulate the N candidates → observations → reliability model
Everything is persisted; the API only reads the state kept here.
"""
from __future__ import annotations

import asyncio
import logging
import time
from typing import Any

from ..config.chains import ChainConfig, get_chain
from ..config.policy import AuthorizationPolicy, load_policy
from ..config.settings import Settings
from ..config.tunables import TunableParams
from ..core.types import Decision, FlashSource, Opportunity
from ..data.collector import StateCollector
from ..data.indexer import PoolIndexer
from ..data.rpc import RpcClient, RpcError
from ..engine.detector import OpportunityDetector
from ..engine.fees import FeeCalculator
from ..engine.routes import RouteTable
from ..engine.selector import SelectionContext, Selector
from ..execution.executor import LiveExecutor, SignerClient
from ..ghost.labeler import GhostLabeler
from ..reliability.model import Observation, ReliabilityModel
from ..risk.manager import BotStatus, RiskManager
from ..simulation.simulator import Simulator
from ..storage.db import Database

log = logging.getLogger("arbbot.runtime")


class EventBus:
    def __init__(self) -> None:
        self.subscribers: list[asyncio.Queue] = []
        self.history: list[dict] = []

    def subscribe(self) -> asyncio.Queue:
        q: asyncio.Queue = asyncio.Queue(maxsize=256)
        self.subscribers.append(q)
        return q

    def unsubscribe(self, q: asyncio.Queue) -> None:
        if q in self.subscribers:
            self.subscribers.remove(q)

    def publish(self, kind: str, data: Any) -> None:
        evt = {"kind": kind, "ts": time.time(), "data": data}
        self.history.append(evt)
        del self.history[:-300]
        for q in list(self.subscribers):
            if q.full():
                try:
                    q.get_nowait()
                except asyncio.QueueEmpty:
                    pass
            q.put_nowait(evt)


class Runtime:
    def __init__(self, settings: Settings, chain: ChainConfig | None = None):
        self.settings = settings
        self.chain = chain or get_chain(settings.chain, settings.devnet_deployments)
        # Real networks: "verified" is only true when `arbbot verify-chain` passed for exactly this configuration.
        self.verification: dict | None = None
        if self.chain.id != "local":
            from ..ops.verify import load_verification

            self.verification = load_verification(settings, self.chain)
            self.chain.verified = self.verification is not None
        self.tunables = TunableParams.load(settings.tunables_path)
        self.policy: AuthorizationPolicy = load_policy(settings.policy_path)
        self.db = Database(settings.db_path)
        self.bus = EventBus()
        self.rpc = RpcClient(settings.rpc_http_url, settings.fallback_urls, settings.rpc_timeout_s, settings.rpc_max_rps,
                             self.chain.multicall3)
        self.indexer = PoolIndexer(self.rpc, self.chain, use_tokenlists=settings.discovery_tokenlists,
                                   factory_enum=settings.discovery_factory_enum, factory_enum_max=settings.discovery_factory_enum_max,
                                   min_pool_usd=settings.discovery_min_pool_usd, max_pools=settings.discovery_max_pools)
        self.pools = []
        self.routes = []
        self.sim_fail_counts: dict[str, int] = {}
        self.quarantine_until: dict[str, int] = {}
        self.collector: StateCollector | None = None
        self.fees: FeeCalculator | None = None
        self.detector: OpportunityDetector | None = None
        self.reliability = ReliabilityModel(min_observations=self.tunables.reliability_min_observations,
                                            credible_level=self.tunables.reliability_credible_level,
                                            threshold=self.policy.min_success_probability)
        self.selector = Selector(self.reliability)
        self.risk = RiskManager(self.policy, self.reliability)
        self.simulator: Simulator | None = None
        self.ghost: GhostLabeler | None = None
        self.signer: SignerClient | None = SignerClient(settings.signer_url, settings.signer_token) if settings.signer_token else None
        self.executor: LiveExecutor | None = None
        self.started_at = 0.0
        self.last_block = 0
        self.last_cycle: dict = {}
        self.recent_opps: list[Opportunity] = []
        self.episodes: dict[str, dict] = {}  # route_key → {first_block, last_block, count, best_net}
        self.cumulative = {"expected_net_eur_selected": 0.0, "ghost_net_after_eur": 0.0, "realized_net_native": 0.0,
                           "failed_gas_native": 0.0, "executions": 0, "failures": 0}
        self._tasks: list[asyncio.Task] = []
        self._stop = asyncio.Event()
        self._cycle_lock = asyncio.Lock()
        self.mode = "ghost"  # "ghost" | "live" (live only when risk status == LIVE_ACTIVE and policy valid)
        self.signer_health: dict | None = None
        self.wallet = self.policy.wallet_address or self.chain.extra.get("accounts", {}).get("executor", "")
        self.paused = False

    # ------------------------------------------------------------------ lifecycle

    async def start(self) -> None:
        self.started_at = time.time()
        await self.rpc.open()
        cid = int(await self.rpc.request("eth_chainId"), 16)
        if cid != self.chain.chain_id:
            raise RuntimeError(f"RPC chain id {cid} != configured {self.chain.chain_id}")
        self.pools = await self.indexer.discover()
        self.collector = StateCollector(self.rpc, self.chain, self.pools, poll_interval_s=self.settings.poll_interval_s,
                                        ws_url=self.settings.rpc_ws_url)
        await self.collector.refresh()
        if self.settings.native_usd_fallback and not self.collector.native_price_usd:
            self.collector.native_price_usd = self.settings.native_usd_fallback
        self.fees = FeeCalculator(self.rpc, self.chain, self.collector, self.tunables)
        await self.fees.refresh_providers([self.chain.tokens[s] for s in self.chain.borrowable if s in self.chain.tokens]
                                          + [t for t in self.chain.hub_tokens() if t.symbol not in self.chain.borrowable])
        self.detector = OpportunityDetector(self.chain, self.collector, self.fees, self.tunables, self.settings.eur_per_usd)
        exec_addr = self.settings.executor_address or self.chain.executor or self.policy.executor_contract
        sender = self.wallet or "0x" + "11" * 20
        self.simulator = Simulator(self.rpc, exec_addr, sender, self.settings.executor_artifact, self.settings.simulate_with_state_override)
        self.ghost = GhostLabeler(self.simulator, self.reliability, self.db, self.fees)
        self.executor = LiveExecutor(self.rpc, self.collector, self.fees, self.selector, self.simulator, self.risk, self.policy,
                                     self.signer, sender, dry_run=self.signer is None)
        start_tokens = [self.chain.tokens[s] for s in self.chain.borrowable if s in self.chain.tokens]
        self.routes = RouteTable.build(self.pools, start_tokens, self.tunables.max_hops, self.settings.discovery_max_routes)
        # reload observations (this DB + the file exported by previous sessions of this chain)
        if self.chain.id != "local":
            try:
                n_imp = self.db.import_observations(self._read_observations_file())
                if n_imp:
                    log.info("imported %d observations from previous sessions", n_imp)
            except Exception as e:  # noqa: BLE001 - never block start-up on the history file
                log.warning("observations import failed: %s", e)
        obs = self.db.observations()
        self.reliability.extend([Observation(o["ts"], o["features"], o["label"], o["source"], o["route_key"], o["net_after"], o["net_expected"]) for o in obs])
        self.risk.flags.update(self.db.kv_get("verification_flags", {}))
        self._load_test_reports()
        log.info("runtime ready: %d pools, %d routes, %d observations, executor=%s", len(self.pools), len(self.routes), len(obs), exec_addr or "(state override)")
        self.db.add_event("info", "startup", f"{len(self.pools)} pools, {len(self.routes)} routes", {"chain": self.chain.id})
        self._tasks = [asyncio.create_task(self.collector.run(), name="collector"),
                       asyncio.create_task(self._engine_loop(), name="engine"),
                       asyncio.create_task(self._housekeeping(), name="housekeeping")]

    def observations_path(self):
        import pathlib

        from ..config.settings import REPO_ROOT

        return pathlib.Path(self.settings.observations_file) if self.settings.observations_file else \
            REPO_ROOT / "docs" / "reports" / "real" / f"observations_{self.chain.id}.jsonl"

    def _read_observations_file(self) -> list[dict]:
        import json

        f = self.observations_path()
        if not f.exists():
            return []
        rows = []
        for line in f.read_text().splitlines():
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    continue
        return rows

    def export_observations(self) -> int:
        """Append this DB's observations that are not yet in the chain's history file (called at every snapshot)."""
        import json

        f = self.observations_path()
        f.parent.mkdir(parents=True, exist_ok=True)
        have = {(float(r["ts"]), r.get("source", "ghost"), r["route_key"]) for r in self._read_observations_file()}
        n = 0
        with f.open("a") as out:
            for r in self.db.observations():
                key = (float(r["ts"]), r["source"], r["route_key"])
                if key in have:
                    continue
                have.add(key)
                out.write(json.dumps({"ts": r["ts"], "source": r["source"], "route_key": r["route_key"], "label": r["label"],
                                      "net_after": r["net_after"], "net_expected": r["net_expected"], "features": r["features"],
                                      "chain_id": self.chain.chain_id}) + "\n")
                n += 1
        return n

    def _load_test_reports(self) -> None:
        """Maturity flags come from the *executed* test reports written by scripts/run_tests.py (never asserted by hand)."""
        import json

        from ..config.settings import REPO_ROOT

        rep = REPO_ROOT / "docs" / "reports"
        try:
            py = json.loads((rep / "pytest_results.json").read_text()) if (rep / "pytest_results.json").exists() else None
            fg = json.loads((rep / "forge_tests.json").read_text()) if (rep / "forge_tests.json").exists() else None
        except (OSError, json.JSONDecodeError):
            py, fg = None, None
        max_age = 7 * 86400
        now = time.time()
        if py and py.get("failed", 1) == 0 and py.get("errors", 1) == 0 and py.get("passed", 0) > 0 and now - py.get("ts", 0) < max_age:
            self.risk.flags["tests_passed"] = True
            tests = py.get("tests", {})
            math_ok = [k for k, v in tests.items() if "test_math_vs_chain" in k and v["status"] == "passed"]
            e2e_ok = [k for k, v in tests.items() if "test_detection_simulation_exact" in k and v["status"] == "passed"]
            self.risk.flags["financial_math_validated"] = bool(math_ok) and bool(e2e_ok)
            self.risk.flags["emergency_stop_ok"] = any("emergency_stop" in k and v["status"] == "passed" for k, v in tests.items())
        else:
            self.risk.flags["tests_passed"] = False
        if fg and not fg.get("skipped") and fg.get("failed", 1) == 0 and fg.get("passed", 0) > 0 and now - fg.get("ts", 0) < max_age:
            self.risk.flags["contract_tested"] = True
        else:
            self.risk.flags["contract_tested"] = False
        self.risk.flags["test_reports"] = {"pytest": None if not py else {"ts": py.get("ts"), "passed": py.get("passed"), "failed": py.get("failed")},
                                           "forge": None if not fg else {"ts": fg.get("ts"), "passed": fg.get("passed"), "failed": fg.get("failed")}}

    async def stop(self) -> None:
        self._stop.set()
        if self.collector:
            self.collector.stop()
        for t in self._tasks:
            t.cancel()
        await asyncio.gather(*self._tasks, return_exceptions=True)
        await self.rpc.close()
        self.db.close()

    # ------------------------------------------------------------------ operator controls (API)

    def emergency_stop(self, reason: str = "operator") -> None:
        self.risk.kill(reason)
        self.paused = True
        self.db.add_event("critical", "emergency_stop", reason)
        self.bus.publish("emergency_stop", {"reason": reason})

    def resume(self) -> None:
        self.risk.clear_kill()
        self.paused = False
        self.risk.state.status = BotStatus.SIMULATION
        self.db.add_event("info", "resume", "operator resumed")
        self.bus.publish("resume", {})

    def set_tunables(self, t: TunableParams) -> None:
        self.tunables = t
        if self.detector:
            self.detector.set_tunables(t)
        self.reliability.min_obs = t.reliability_min_observations
        self.reliability.level = t.reliability_credible_level
        t.save(self.settings.tunables_path)

    # ------------------------------------------------------------------ main loop

    def _ctx(self, block: int) -> SelectionContext:
        remaining = None
        if self.policy.enabled:
            remaining = self.policy.max_total_budget_native - self.risk.ledger.gas_spent_wei / 1e18
        return SelectionContext(self.tunables, self.policy if self.policy.enabled else None, remaining,
                                self.collector.native_price_usd if self.collector else None, block)

    async def _engine_loop(self) -> None:
        q = self.collector.subscribe()
        while not self._stop.is_set():
            try:
                block = await asyncio.wait_for(q.get(), timeout=30)
            except asyncio.TimeoutError:
                self.risk.flags["data_stale"] = True
                continue
            try:
                await self.process_block(block)
            except Exception as e:  # noqa: BLE001
                log.exception("engine cycle failed at block %s: %s", block, e)
                self.db.add_event("error", "engine", str(e), {"block": block})

    async def process_block(self, block: int) -> dict:
        async with self._cycle_lock:
            if block <= self.last_block and self.last_cycle.get("block") == block:
                return self.last_cycle
            return await self._process_block(block)

    async def _process_block(self, block: int) -> dict:
        t0 = time.perf_counter()
        self.last_block = block
        # ghost labels for block-1 candidates
        labels = await self.ghost.on_block(block)
        for lb in labels:
            usd = self.fees.token_price_usd(self.chain.tokens.get(lb["token"])) if lb["token"] in self.chain.tokens else None
            if usd:
                self.cumulative["ghost_net_after_eur"] += lb["net_after"] / 10**lb["decimals"] * usd * self.settings.eur_per_usd
        if labels:
            self.bus.publish("ghost_labels", labels)
        if self.paused:
            self.last_cycle = {"block": block, "paused": True}
            return self.last_cycle
        ctx = self._ctx(block)
        opps = await self.detector.scan(self.routes, block, max_borrow_usd=self.policy.max_borrow_usd or None)
        self.selector.evaluate(opps, ctx, self.policy.min_success_probability)
        # simulate the best positive candidates (cap RPC usage)
        # (only candidates that clear the on-chain floor — the same population the executor may submit — are simulated
        #  and labelled, so the reliability statistics describe exactly the trades that could be executed)
        positives = sorted([o for o in opps if o.profit.expected_net > 0 and not any(r.startswith("below_safety_margin") for r in o.reasons)],
                           key=lambda o: -o.profit.expected_net)[:3]
        self._lift_expired_quarantines(block)
        for o in positives:
            sim = await self.simulator.simulate(o, min_profit=1, block=block)
            o.sim = sim.__dict__
            o.sim_ok, o.sim_error, o.sim_gas_used = sim.ok, sim.error, sim.gas_estimate
            if sim.ok:
                self.risk.flags["simulations_ok"] += 1
                o.profit.simulated_net = sim.profit - o.profit.fees.gas_cost_token
                for h in o.route.hops:
                    self.sim_fail_counts.pop(h.pool.address.lower(), None)
            else:
                self.risk.flags["simulations_failed"] += 1
                o.profit.simulated_net = None
                self._note_sim_failure(o, block)
            self.ghost.enqueue(o, block)
        # re-run gates now that simulation results exist
        for o in positives:
            o.reasons = [r for r in o.reasons if not r.startswith(("simulation_failed", "sim_below", "simulated_net"))]
        self.selector.evaluate(positives, ctx, self.policy.min_success_probability)
        best = self.selector.pick(positives)
        decision_log: dict = {"block": block, "candidates": len(opps), "positives": len(positives), "selected": None}
        if best is not None:
            decision_log["selected"] = best.to_record()
            if self.risk.state.status == BotStatus.LIVE_ACTIVE and self.executor and not self.executor.dry_run:
                res = await self.executor.execute(best, ctx)
                self._record_execution(best, res)
                decision_log["execution"] = res.status
            else:
                best.reasons.append(f"ghost_mode:{self.risk.state.status.name}")
        # persistence + episode dedup
        for o in opps:
            self._track_episode(o, block)
            self.db.upsert_opportunity(o.to_record())
        self.recent_opps = (opps + self.recent_opps)[:400]
        dt = (time.perf_counter() - t0) * 1000
        best_net = max((o.profit.expected_net_eur or 0.0 for o in opps), default=0.0)
        self.db.add_metric("cycle_ms", dt)
        self.db.add_metric("candidates", len(opps))
        self.db.add_metric("positives", len(positives))
        self.db.add_metric("best_expected_net_eur", best_net)
        self.db.add_metric("gas_price_gwei", self.collector.gas.base_fee_wei / 1e9)
        if self.collector.native_price_usd:
            self.db.add_metric("native_usd", self.collector.native_price_usd)
        self.last_cycle = {**decision_log, "cycle_ms": round(dt, 1), "block": block, "best_expected_net_eur": best_net,
                           "ts": time.time()}
        self.bus.publish("cycle", {**self.last_cycle, "opportunities": [o.to_record() for o in opps[:50]]})
        return self.last_cycle

    def _track_episode(self, o: Opportunity, block: int) -> None:
        ep = self.episodes.get(o.route.key)
        if o.profit.expected_net <= 0:
            if ep and ep.get("open"):
                ep["open"] = False
            return
        if ep and ep.get("open") and block - ep["last_block"] <= 2:
            ep["last_block"] = block
            ep["count"] += 1
            ep["best_net"] = max(ep["best_net"], o.profit.expected_net)
        else:
            self.episodes[o.route.key] = {"first_block": block, "last_block": block, "count": 1, "best_net": o.profit.expected_net, "open": True}

    def _record_execution(self, opp: Opportunity, res) -> None:
        rec = {"ts": time.time(), "opportunity_id": opp.id, "tx_hash": res.tx_hash, "status": res.status, "gas_used": res.gas_used,
               "effective_gas_price": res.effective_gas_price, "gas_cost_wei": res.gas_cost_wei, "realized_net": res.realized_net_token,
               "expected_net": opp.profit.expected_net, "error": res.error, "block_number": res.block_number}
        self.db.add_execution(rec)
        self.db.add_event("info" if res.status == "success" else "warning", "execution", f"{res.status}: {res.error or res.tx_hash}", rec)
        if res.status in ("success", "reverted"):
            self.cumulative["executions"] += 1
            if res.status != "success" or (res.realized_net_token or 0) <= 0:
                self.cumulative["failures"] += 1
                self.cumulative["failed_gas_native"] += res.gas_cost_wei / 1e18
            fb = opp.profit.fees
            if fb.native_price_in_token:
                self.cumulative["realized_net_native"] += (res.realized_net_token or 0) / 10**opp.route.token.decimals / fb.native_price_in_token
            # live observation for the reliability model
            feats = dict(opp.features)
            label = 1 if (res.realized_net_token or 0) > 0 else 0
            obs = Observation(time.time(), feats, label, "live", opp.route.key, float(res.realized_net_token or 0), float(opp.profit.expected_net))
            self.reliability.add(obs)
            self.db.add_observation(obs.ts, "live", opp.route.key, label, obs.net_after, obs.net_expected, feats)
        if res.status in ("reverted", "dropped", "error"):
            self.risk.degrade(f"execution {res.status}: {res.error}")
        self.bus.publish("execution", rec)

    # ------------------------------------------------------------------ housekeeping

    # ------------------------------------------------------------------ model/chain mismatch protection

    QUARANTINE_BLOCKS = 300  # ≈ 10 min on Base; the pool is re-admitted afterwards and must prove itself again

    def _note_sim_failure(self, o, block: int) -> None:
        """A route the model priced positive but the contract simulation rejects = model/chain mismatch somewhere on
        the route. Hub/hub pools (both tokens verified) are exempt — they are deep and shared by every route; the
        long-tail pool that keeps appearing in failed routes is quarantined for QUARANTINE_BLOCKS once it reaches
        `quarantine_after_false_positives` consecutive failures (counts reset on any successful simulation)."""
        hubs = self.chain._hub_set() if hasattr(self.chain, "_hub_set") else set()
        limit = max(1, int(self.tunables.quarantine_after_false_positives))
        for h in o.route.hops:
            p = h.pool
            if p.token0.address.lower() in hubs and p.token1.address.lower() in hubs:
                continue
            key = p.address.lower()
            self.sim_fail_counts[key] = self.sim_fail_counts.get(key, 0) + 1
            if self.sim_fail_counts[key] >= limit and not p.quarantined:
                p.quarantined = True
                p.quarantine_reason = f"simulation failed ×{self.sim_fail_counts[key]} (model/chain mismatch) — until block {block + self.QUARANTINE_BLOCKS}"
                self.quarantine_until[key] = block + self.QUARANTINE_BLOCKS
                self.cumulative["pools_quarantined"] = self.cumulative.get("pools_quarantined", 0) + 1
                log.warning("quarantine %s: %s (last error: %s)", p.short(), p.quarantine_reason, o.sim_error)
                self.db.add_event("warning", "quarantine", f"{p.short()}: {p.quarantine_reason}", {"error": o.sim_error, "route": o.route.describe()})

    def _lift_expired_quarantines(self, block: int) -> None:
        for key, until in list(self.quarantine_until.items()):
            if block >= until:
                del self.quarantine_until[key]
                self.sim_fail_counts.pop(key, None)
                for p in self.pools:
                    if p.address.lower() == key and p.quarantined and p.quarantine_reason.startswith("simulation failed"):
                        p.quarantined, p.quarantine_reason = False, ""
                        self.db.add_event("info", "quarantine_lifted", p.short(), {})

    async def _housekeeping(self) -> None:
        while not self._stop.is_set():
            try:
                if self.signer:
                    self.signer_health = await self.signer.health()
                signer_ok = bool(self.signer_health and self.signer_health.get("policy_valid")
                                 and self.signer_health.get("address", "").lower() == self.policy.wallet_address.lower())
                age = self.collector.data_age_ms(self.pools) if self.collector else None
                rpc_ok = self.rpc.metrics.summary().get("error_rate", 1.0) < 0.2 if hasattr(self.rpc, "metrics") else True
                self.risk.flags["data_stale"] = age is not None and age > 15_000
                self.risk.evaluate(policy_signer_ok=signer_ok, data_age_ms=age, rpc_ok=rpc_ok, chain_verified=self.chain.verified,
                                   chain_detail=("devnet (generated addresses)" if self.chain.id == "local" else
                                                 (f"verified {time.strftime('%Y-%m-%d %H:%M', time.localtime(self.verification['ts']))} on {self.verification.get('rpc_host')}"
                                                  if self.verification else "NOT verified for this configuration — run `arbbot verify-chain`")))
                # continuous post-activation protection
                if self.risk.state.status == BotStatus.LIVE_ACTIVE:
                    drift, msg = self.reliability.drift_detected()
                    if drift:
                        self.risk.degrade(f"model drift: {msg}")
                    if self.risk.flags["data_stale"]:
                        self.risk.degrade("stale data")
                self.db.add_metric("status", list(BotStatus).index(self.risk.state.status))
                self.bus.publish("status", self.status())
            except Exception as e:  # noqa: BLE001
                log.warning("housekeeping: %s", e)
            await asyncio.sleep(5)

    # ------------------------------------------------------------------ views

    def status(self) -> dict:
        col = self.collector.stats.as_dict() if self.collector else {}
        return {
            "chain": {"id": self.chain.id, "chain_id": self.chain.chain_id, "name": self.chain.name, "verified": self.chain.verified,
                      "is_devnet": self.chain.id == "local", "rpc_host": self.settings.rpc_http_url.split("//")[-1].split("/")[0],
                      "verification": None if not self.verification else {"ts": self.verification.get("ts"), "pools": self.verification.get("pools"),
                                                                            "rpc_host": self.verification.get("rpc_host")}},
            "uptime_s": time.time() - self.started_at if self.started_at else 0,
            "mode": "live" if self.risk.state.status == BotStatus.LIVE_ACTIVE else "ghost",
            "paused": self.paused,
            "risk": self.risk.as_dict(),
            "collector": col,
            "rpc": self.rpc.metrics.summary() if hasattr(self.rpc, "metrics") else {},
            "gas": self.collector.gas.as_dict() if self.collector else {},
            "native_price_usd": self.collector.native_price_usd if self.collector else None,
            "pools": len(self.pools), "routes": len(self.routes),
            "detector": self.detector.stats.as_dict() if self.detector else {},
            "ghost": self.ghost.stats() if self.ghost else {},
            "reliability": self.reliability.calibration_report(),
            "cumulative": self.cumulative,
            "executions": self.db.execution_summary(),
            "last_cycle": {k: v for k, v in self.last_cycle.items() if k != "selected"},
            "tunables": self.tunables.as_dict(),
            "policy": self.policy.summary(),
            "signer": self.signer_health,
            "flash_providers": {k.name: {"fee_bps": v.fee_bps_x100 / 100, "verified": v.verified,
                                          "capacity": {a: str(c) for a, c in v.capacity.items()}} for k, v in (self.fees.providers.items() if self.fees else {})},
            "episodes_open": sum(1 for e in self.episodes.values() if e.get("open")),
        }
