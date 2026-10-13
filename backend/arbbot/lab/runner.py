"""60-minute autonomous optimisation lab.

Phases (fractions of the total duration; default 60 min):
  0–5    DIAGNOSTIC          RPC, chain, pools, data freshness, gas, providers, executor, signer, policy, test reports
  5–15   DATA VALIDATION     exact math vs chain on live pools; estimate vs full simulation on live candidates
  15–30  SEARCH + SIM        observe the engine (candidates, positives, sims, ghost labels, latency)
  30–45  SELF-CORRECTION     OBSERVE → DIAGNOSE → MODIFY (git-isolated) → TEST (A/B same blocks) → ACCEPT/ROLLBACK
  45–55  COMPARATIVE VALID.  accepted params vs original reference on fresh blocks (holdout)
  55–60  REPORT              JSON + Markdown (FR) + maturity decision; never "ready" because time elapsed
Every number in the report is measured in this run; nothing is extrapolated.
"""
from __future__ import annotations

import asyncio
import json
import logging
import pathlib
import statistics
import time

from ..config.settings import REPO_ROOT
from ..config.tunables import TunableParams
from ..core.pricing import QuoteError, quote_hop
from ..core.types import DexKind
from ..data.rpc import RpcError, decode_result, encode_call
from ..engine.detector import OpportunityDetector
from ..engine.fees import FeeCalculator
from ..risk.manager import BotStatus
from .selfcorr import ParamRepo, diagnose

log = logging.getLogger("arbbot.lab")

PHASES = [
    ("diagnostic", 0, 5), ("data_validation", 5, 15), ("search_simulation", 15, 30),
    ("self_correction", 30, 45), ("comparative_validation", 45, 55), ("report", 55, 60),
]


class LabRunner:
    def __init__(self, runtime, total_minutes: float = 60.0, reports_dir: pathlib.Path | None = None):
        self.rt = runtime
        self.total = total_minutes * 60
        self.reports_dir = reports_dir or (REPO_ROOT / "docs" / "reports")
        self.running = False
        self._stop = False
        self.started = 0.0
        self.phase = ""
        self.results: dict = {"phases": {}, "log": []}
        self.run_id: int | None = None
        self.repo = ParamRepo(self.rt.settings.data_dir / "selfcorr")

    # ------------------------------------------------------------------ utils

    def log(self, msg: str) -> None:
        line = f"[{(time.time() - self.started) / 60:5.1f} min] {msg}"
        self.results["log"].append(line)
        log.info("lab %s", msg)
        self.rt.bus.publish("lab", {"phase": self.phase, "message": line})

    def stop(self) -> None:
        self._stop = True

    def snapshot(self) -> dict:
        return {"running": self.running, "phase": self.phase, "elapsed_s": time.time() - self.started if self.started else 0,
                "total_s": self.total, "results": self.results, "run_id": self.run_id}

    def _deadline(self, end_min: float) -> float:
        return self.started + self.total * end_min / 60

    async def _sleep_until(self, deadline: float, step: float = 1.0) -> None:
        while time.time() < deadline and not self._stop:
            await asyncio.sleep(min(step, max(0.0, deadline - time.time())))

    # ------------------------------------------------------------------ run

    async def run(self) -> dict:
        self.running = True
        self.started = time.time()
        self.run_id = self.rt.db.add_lab_run(self.started, None, "running", {})
        self.rt.db.add_event("info", "lab", f"lab started ({self.total / 60:.0f} min)")
        try:
            for name, a, b in PHASES:
                if self._stop:
                    break
                self.phase = name
                self.log(f"=== phase {name} ({a}–{b} min) ===")
                fn = getattr(self, f"phase_{name}")
                try:
                    self.results["phases"][name] = await fn(self._deadline(b))
                except Exception as e:  # noqa: BLE001
                    log.exception("lab phase %s failed", name)
                    self.results["phases"][name] = {"error": str(e)}
                    self.log(f"phase {name} FAILED: {e}")
                self.rt.db.update_lab_run(self.run_id, None, "running", self.results)
            status = "stopped" if self._stop else "finished"
        finally:
            self.running = False
            self.rt.db.update_lab_run(self.run_id, time.time(), status, self.results)
            self.rt.db.add_event("info", "lab", f"lab {status}")
        return self.results

    # ------------------------------------------------------------------ phases

    async def phase_diagnostic(self, deadline: float) -> dict:
        rt = self.rt
        lat = []
        for _ in range(10):
            t0 = time.perf_counter()
            try:
                await rt.rpc.block_number()
                lat.append((time.perf_counter() - t0) * 1000)
            except RpcError as e:
                self.log(f"rpc error: {e}")
        cid = int(await rt.rpc.request("eth_chainId"), 16)
        code = await rt.rpc.get_code(rt.simulator.executor) if rt.simulator.executor else b""
        res = {
            "chain_id": cid, "chain": rt.chain.id, "is_devnet": rt.chain.id == "local", "verified_addresses": rt.chain.verified,
            "rpc_latency_ms": {"p50": statistics.median(lat) if lat else None, "max": max(lat) if lat else None, "samples": len(lat)},
            "pools": len(rt.pools), "quarantined": sum(1 for p in rt.pools if p.quarantined), "routes": len(rt.routes),
            "data_age_ms": rt.collector.data_age_ms(rt.pools), "gas": rt.collector.gas.as_dict(), "native_price_usd": rt.collector.native_price_usd,
            "flash_providers": {k.name: {"fee_bps": v.fee_bps_x100 / 100, "verified": v.verified} for k, v in rt.fees.providers.items()},
            "executor_deployed": len(code) > 0, "executor": rt.simulator.executor,
            "signer_configured": rt.signer is not None, "signer_health": rt.signer_health,
            "policy": rt.policy.summary(), "tunables_version": rt.tunables.version, "observations": rt.reliability.n,
            "test_reports": self._read_test_reports(),
        }
        issues = []
        if not res["executor_deployed"]:
            issues.append("executor not deployed (simulation via state override only)")
        if res["data_age_ms"] > rt.tunables.max_data_age_ms:
            issues.append("stale data")
        if res["rpc_latency_ms"]["p50"] and res["rpc_latency_ms"]["p50"] > 500:
            issues.append("slow RPC")
        if not rt.collector.native_price_usd:
            issues.append("no native price reference")
        res["issues"] = issues
        self.log(f"diagnostic: {len(rt.pools)} pools, {len(rt.routes)} routes, rpc p50 {res['rpc_latency_ms']['p50']:.0f} ms, issues={issues}")
        await self._sleep_until(min(deadline, time.time() + 2))
        return res

    def _read_test_reports(self) -> dict:
        out = {}
        for name in ("forge_tests.json", "pytest_results.json"):
            p = self.reports_dir / name
            if p.exists():
                try:
                    out[name] = json.loads(p.read_text())
                except Exception:  # noqa: BLE001
                    out[name] = {"error": "unreadable"}
        return out

    async def phase_data_validation(self, deadline: float) -> dict:
        """Exact math vs chain on live pools (V2 via pair reserves K-check, Solidly getAmountOut, V3 via helper when
        available) + estimate vs full simulation on live positive candidates."""
        rt = self.rt
        res = {"v2": {"exact": 0, "mismatch": 0}, "solidly": {"exact": 0, "mismatch": 0}, "v3": {"exact": 0, "mismatch": 0, "skipped": 0},
               "sim_vs_estimate": {"exact": 0, "within_tolerance": 0, "below": 0, "failed": 0, "samples": []}}
        helper = rt.chain.extra.get("v3_helper")
        maker = rt.chain.extra.get("accounts", {}).get("maker")
        for p in rt.pools:
            if p.quarantined or time.time() > deadline - 5:
                continue
            x, y = p.liquidity_hint()
            for frac in (0.001, 0.01, 0.05):
                for tin in (p.token0, p.token1):
                    amount = int((x if tin is p.token0 else y) * frac)
                    if amount <= 0:
                        continue
                    try:
                        q = quote_hop(p, tin, amount)
                    except QuoteError:
                        if p.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3):
                            res["v3"]["skipped"] += 1
                        continue
                    try:
                        if p.kind == DexKind.UNIV2:
                            raw = await rt.rpc.call(p.address, encode_call("getReserves()"))
                            r0, r1 = decode_result(["uint112", "uint112"], raw[:64])
                            rin, rout = (r0, r1) if p.is_token0(tin.address) else (r1, r0)
                            fee = 1_000_000 - p.fee_ppm
                            onchain = amount * fee * rout // (rin * 1_000_000 + amount * fee)
                            key = "v2"
                        elif p.kind == DexKind.SOLIDLY:
                            raw = await rt.rpc.call(p.address, encode_call("getAmountOut(uint256,address)", [amount, tin.address]))
                            (onchain,) = decode_result(["uint256"], raw)
                            key = "solidly"
                        else:
                            if not helper or not maker:
                                continue
                            raw = await rt.rpc.call(helper, encode_call("swapExactIn(address,bool,uint256)", [p.address, p.is_token0(tin.address), amount]), sender=maker, gas=5_000_000)
                            (onchain,) = decode_result(["uint256"], raw)
                            key = "v3"
                    except RpcError:
                        continue
                    res[key]["exact" if int(onchain) == q.amount_out else "mismatch"] += 1
                    if int(onchain) != q.amount_out:
                        self.log(f"MISMATCH {p.short()} {tin.symbol} in={amount}: ours={q.amount_out} chain={onchain}")
        self.log(f"math vs chain: v2 {res['v2']}, solidly {res['solidly']}, v3 {res['v3']}")
        # estimate vs simulation on live candidates until the deadline
        while time.time() < deadline - 2 and not self._stop:
            opps = [o for o in rt.recent_opps if o.profit.expected_net > 0 and o.sim]
            seen = {s["id"] for s in res["sim_vs_estimate"]["samples"]}
            for o in opps[:20]:
                if o.id in seen:
                    continue
                sim = o.sim
                exp = o.profit.gross_profit - o.profit.fees.flash_fee
                if not sim.get("ok"):
                    res["sim_vs_estimate"]["failed"] += 1
                    kind = "failed"
                elif sim["profit"] == exp:
                    res["sim_vs_estimate"]["exact"] += 1
                    kind = "exact"
                elif sim["profit"] + int(o.profit.amount_in * rt.tunables.sim_tolerance_bps) // 10_000 >= exp:
                    res["sim_vs_estimate"]["within_tolerance"] += 1
                    kind = "within_tolerance"
                else:
                    res["sim_vs_estimate"]["below"] += 1
                    kind = "below"
                res["sim_vs_estimate"]["samples"].append({"id": o.id, "route": o.route.describe(), "amount_in": o.profit.amount_in,
                                                          "estimate": exp, "sim": sim.get("profit"), "error": sim.get("error"), "kind": kind})
            await asyncio.sleep(2)
        s = res["sim_vs_estimate"]
        res["sim_vs_estimate"]["samples"] = s["samples"][-50:]
        self.log(f"simulation vs estimate: exact {s['exact']}, within tol {s['within_tolerance']}, below {s['below']}, failed {s['failed']}")
        return res

    def _observe_window(self) -> dict:
        rt = self.rt
        return {"detector": dict(rt.detector.stats.as_dict()), "ghost": rt.ghost.stats(), "sims_ok": rt.risk.flags["simulations_ok"],
                "sims_failed": rt.risk.flags["simulations_failed"], "rpc": rt.rpc.metrics.summary(), "block": rt.last_block, "ts": time.time()}

    async def phase_search_simulation(self, deadline: float) -> dict:
        rt = self.rt
        start = self._observe_window()
        cycle_ms: list[float] = []
        best_nets: list[float] = []
        sim_below = 0
        gas_ratios: list[float] = []
        q = rt.bus.subscribe()
        try:
            while time.time() < deadline and not self._stop:
                try:
                    evt = await asyncio.wait_for(q.get(), timeout=5)
                except asyncio.TimeoutError:
                    continue
                if evt["kind"] != "cycle":
                    continue
                d = evt["data"]
                cycle_ms.append(d.get("cycle_ms", 0))
                best_nets.append(d.get("best_expected_net_eur", 0) or 0)
                for o in d.get("opportunities", []):
                    if any(str(r).startswith("sim_below") for r in o.get("reasons", [])):
                        sim_below += 1
                    sim = o.get("sim") or {}
                    if sim.get("gas_estimate") and o.get("fees", {}).get("gas_units"):
                        gas_ratios.append(sim["gas_estimate"] / o["fees"]["gas_units"])
        finally:
            rt.bus.unsubscribe(q)
        end = self._observe_window()
        det0, det1 = start["detector"], end["detector"]
        res = {
            "blocks": end["block"] - start["block"], "cycles": len(cycle_ms),
            "cycle_ms_p50": statistics.median(cycle_ms) if cycle_ms else None,
            "cycle_ms_p95": sorted(cycle_ms)[int(0.95 * (len(cycle_ms) - 1))] if cycle_ms else None,
            "candidates": det1["candidates"] - det0["candidates"], "positives": det1["positive_net"] - det0["positive_net"],
            "routes_optimized": det1["routes_optimized"] - det0["routes_optimized"],
            "simulations": (end["sims_ok"] + end["sims_failed"]) - (start["sims_ok"] + start["sims_failed"]),
            "sim_failures": end["sims_failed"] - start["sims_failed"], "sim_below_estimate": sim_below,
            "ghost_labeled": end["ghost"]["labeled"] - start["ghost"]["labeled"],
            "ghost_positives": end["ghost"]["positives"] - start["ghost"]["positives"],
            "best_expected_net_eur_max": max(best_nets) if best_nets else 0, "best_expected_net_eur_median": statistics.median(best_nets) if best_nets else 0,
            "gas_estimate_over_model_median": statistics.median(gas_ratios) if gas_ratios else None,
            "rejections": det1["rejections"], "rpc": end["rpc"],
        }
        res["ghost_positive_rate"] = res["ghost_positives"] / res["ghost_labeled"] if res["ghost_labeled"] else None
        self.log(f"search: {res['blocks']} blocks, {res['candidates']} candidates, {res['positives']} positive, {res['simulations']} sims "
                 f"({res['sim_failures']} failed, {sim_below} below estimate), ghost {res['ghost_positives']}/{res['ghost_labeled']}, cycle p95 {res['cycle_ms_p95']}")
        return res

    # ------------------------------------------------------------------ A/B evaluation

    async def _ab_window(self, ref: TunableParams, cand: TunableParams, deadline: float, max_blocks: int = 60) -> dict:
        """Evaluate two parameter sets on the SAME blocks, scored the way reality scores them: the best candidate each
        detector picks at block N is re-simulated at block N+1 (the earliest block a real transaction could land in).
        Score = simulated net at N+1 (token→EUR) when the route is still profitable, minus the expected failure cost
        (gas of a reverted tx) when it is not. Nothing is signed."""
        rt = self.rt

        def mk(t: TunableParams):
            f = FeeCalculator(rt.rpc, rt.chain, rt.collector, t)
            f.providers = rt.fees.providers
            f.measured_gas = rt.fees.measured_gas
            return OpportunityDetector(rt.chain, rt.collector, f, t, rt.settings.eur_per_usd)

        det_ref, det_cand = mk(ref), mk(cand)
        score = {"ref": 0.0, "cand": 0.0}
        counts = {n: {"positives": 0, "picked": 0, "ok_next": 0, "fail_next": 0, "blocks": 0} for n in ("ref", "cand")}
        pending: dict[str, tuple] = {}
        q = rt.collector.subscribe()
        blocks = 0
        try:
            while time.time() < deadline and blocks < max_blocks and not self._stop:
                try:
                    block = await asyncio.wait_for(q.get(), timeout=10)
                except asyncio.TimeoutError:
                    continue
                blocks += 1
                # 1) settle last block's picks against the new state (N+1)
                for name, (best, b0) in list(pending.items()):
                    if block <= b0:
                        continue
                    sim = await rt.simulator.simulate(best, min_profit=1, block=block)
                    usd = rt.fees.token_price_usd(best.route.token) or 0
                    scale = usd * rt.settings.eur_per_usd / 10**best.route.token.decimals
                    net_after = (sim.profit - best.profit.fees.gas_cost_token) if (sim.ok and sim.profit is not None) else None
                    if net_after is not None and net_after > 0:
                        counts[name]["ok_next"] += 1
                        score[name] += net_after * scale
                    else:
                        counts[name]["fail_next"] += 1
                        score[name] -= best.profit.fees.failure_cost_wei / 1e18 * (rt.collector.native_price_usd or 0) * rt.settings.eur_per_usd
                    del pending[name]
                # 2) each detector picks its best candidate on the shared state of this block
                for name, det in (("ref", det_ref), ("cand", det_cand)):
                    opps = await det.scan(rt.routes, block, max_borrow_usd=rt.policy.max_borrow_usd or None, only_positive=True)
                    counts[name]["blocks"] += 1
                    counts[name]["positives"] += len(opps)
                    if not opps:
                        continue
                    best = max(opps, key=lambda o: o.profit.expected_net)
                    sim = await rt.simulator.simulate(best, min_profit=1, block=block)
                    if not sim.ok:  # would never be sent: a failed simulation at N is a rejection, not a loss
                        continue
                    counts[name]["picked"] += 1
                    pending[name] = (best, block)
        finally:
            rt.collector._subscribers.remove(q)
        return {"blocks": blocks, "score_eur": score, "counts": counts, "metric": "simulated net at N+1 minus failure cost (EUR)"}

    async def phase_self_correction(self, deadline: float) -> dict:
        rt = self.rt
        search = self.results["phases"].get("search_simulation", {})
        obs = dict(search)
        obs["block_time_ms"] = rt.chain.block_time_s * 1000
        rej = search.get("rejections", {}) or {}
        obs["unquotable"] = rej.get("unquotable", 0) + rej.get("borrow_bound_too_small", 0)
        obs["spread_near_threshold"] = rej.get("spread_below_threshold", 0) // 20  # conservative proxy
        obs["threshold"] = rt.policy.min_success_probability
        try:
            rel = rt.reliability.calibration_report()
        except Exception:  # noqa: BLE001
            rel = {}
        obs["bucket_rates"] = {k: (v.get("n"), v.get("mean")) for k, v in (rel.get("buckets") or {}).items()}
        reference = rt.tunables
        self.repo.set_reference(reference, f"reference v{reference.version} before lab self-correction")
        diag = diagnose(obs, reference)
        res: dict = {"observe": {k: v for k, v in obs.items() if k != "rejections"}, "diagnose": {"findings": diag.findings, "rationale": diag.rationale},
                     "changes": diag.changes, "iterations": [], "reference": reference.as_dict()}
        if not diag.changes:
            self.log("self-correction: no actionable finding — reference kept unchanged")
            res["decision"] = "no_change"
            await self._sleep_until(min(deadline, time.time() + 5))
            return res
        try:
            candidate = reference.with_changes(**diag.changes)
        except PermissionError as e:
            res["decision"] = f"refused: {e}"
            self.log(f"self-correction refused a non-tunable change: {e}")
            return res
        branch = self.repo.propose(candidate, "; ".join(diag.rationale))
        self.log(f"candidate v{candidate.version} on {branch}: {diag.changes}")
        ab = await self._ab_window(reference, candidate, deadline - 5)
        res["iterations"].append({"branch": branch, "ab": ab})
        ref_s, cand_s = ab["score_eur"]["ref"], ab["score_eur"]["cand"]
        safer = ab["counts"]["cand"]["fail_next"] <= ab["counts"]["ref"]["fail_next"]
        better = cand_s > ref_s * 1.01 + 1e-9 if ref_s > 0 else cand_s > ref_s
        if ab["blocks"] >= 5 and better and safer:
            git_ref = self.repo.accept(branch)
            rt.set_tunables(candidate)
            rt.db.add_change("self-correction", "; ".join(diag.rationale), reference.as_dict(), candidate.as_dict(), ref_s, cand_s, True, git_ref)
            res["decision"] = "accepted"
            self.log(f"ACCEPTED: candidate {cand_s:.4f} € vs reference {ref_s:.4f} € over {ab['blocks']} blocks (merged {git_ref})")
        else:
            self.repo.rollback(branch)
            rt.db.add_change("self-correction", "; ".join(diag.rationale), reference.as_dict(), candidate.as_dict(), ref_s, cand_s, False, branch)
            res["decision"] = "rolled_back"
            self.log(f"ROLLBACK: candidate {cand_s:.4f} € vs reference {ref_s:.4f} € over {ab['blocks']} blocks (safer={safer})")
        res["git_log"] = self.repo.log(10)
        return res

    async def phase_comparative_validation(self, deadline: float) -> dict:
        rt = self.rt
        sc = self.results["phases"].get("self_correction", {})
        if sc.get("decision") != "accepted":
            self.log("comparative validation: nothing accepted — observing the reference only")
            before = self._observe_window()
            await self._sleep_until(deadline - 2)
            after = self._observe_window()
            return {"decision": "reference_only", "ghost_labels": after["ghost"]["labeled"] - before["ghost"]["labeled"],
                    "ghost_positives": after["ghost"]["positives"] - before["ghost"]["positives"]}
        base = rt.tunables  # the accepted candidate (now on main)
        prior = TunableParams(**sc["reference"])  # the pre-lab reference, kept for the holdout comparison
        ab = await self._ab_window(prior, base, deadline - 5)
        ref_s, cand_s = ab["score_eur"]["ref"], ab["score_eur"]["cand"]
        res = {"ab": ab}
        if ab["blocks"] >= 5 and cand_s >= ref_s:
            res["decision"] = "confirmed"
            self.log(f"holdout CONFIRMED: {cand_s:.4f} € vs {ref_s:.4f} € over {ab['blocks']} blocks")
        else:
            rt.set_tunables(prior)
            self.repo.set_reference(prior, "rollback after holdout validation")
            rt.db.add_change("self-correction", "holdout rollback", base.as_dict(), prior.as_dict(), cand_s, ref_s, False, "holdout")
            res["decision"] = "rolled_back_on_holdout"
            self.log(f"holdout ROLLBACK: {cand_s:.4f} € vs {ref_s:.4f} € over {ab['blocks']} blocks")
        return res

    async def phase_report(self, deadline: float) -> dict:
        rt = self.rt
        rt.risk.evaluate(policy_signer_ok=bool(rt.signer_health and rt.signer_health.get("policy_valid")),
                         data_age_ms=rt.collector.data_age_ms(rt.pools), rpc_ok=True)
        rel = rt.reliability.calibration_report()
        report = {
            "generated": time.time(), "duration_min": (time.time() - self.started) / 60, "chain": rt.chain.id, "is_devnet": rt.chain.id == "local",
            "phases": self.results["phases"], "reliability": rel, "risk": rt.risk.as_dict(), "cumulative": rt.cumulative,
            "status": rt.risk.state.status.value, "sub_status": rt.risk.state.sub_status,
            "tunables_final": rt.tunables.as_dict(), "policy_digest": rt.policy.digest(),
        }
        ts = time.strftime("%Y%m%d-%H%M%S")
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        (self.reports_dir / f"lab_{ts}.json").write_text(json.dumps(report, indent=1, default=str))
        md = self.render_markdown(report)
        (self.reports_dir / f"lab_{ts}.md").write_text(md)
        self.results["report_files"] = [f"docs/reports/lab_{ts}.json", f"docs/reports/lab_{ts}.md"]
        self.log(f"report written: docs/reports/lab_{ts}.md — statut {report['status']} ({report['sub_status']})")
        return {"files": self.results["report_files"], "status": report["status"], "sub_status": report["sub_status"]}

    # ------------------------------------------------------------------ markdown

    def render_markdown(self, r: dict) -> str:
        ph = r["phases"]
        d = ph.get("diagnostic", {})
        v = ph.get("data_validation", {})
        s = ph.get("search_simulation", {})
        sc = ph.get("self_correction", {})
        cv = ph.get("comparative_validation", {})
        rel = r["reliability"]
        lines = [
            f"# Rapport du laboratoire d'optimisation ({r['duration_min']:.1f} min)",
            "",
            f"**Réseau :** {r['chain']}{' — DEVNET LOCAL (anvil), aucune donnée de marché réelle' if r['is_devnet'] else ''}  ",
            f"**Statut de maturité :** {r['status']} — {r['sub_status']}  ",
            f"**Empreinte de la politique d'autorisation :** `{r['policy_digest']}`",
            "",
            "## 1. Diagnostic (0–5 min)",
            f"- Chain id {d.get('chain_id')}, {d.get('pools')} pools ({d.get('quarantined')} en quarantaine), {d.get('routes')} routes",
            f"- Latence RPC p50 {fmt(d.get('rpc_latency_ms', {}).get('p50'))} ms, âge des données {fmt(d.get('data_age_ms'))} ms",
            f"- Fournisseurs de flash loan : {d.get('flash_providers')}",
            f"- Exécuteur déployé : {d.get('executor_deployed')} ({d.get('executor')}) ; signer configuré : {d.get('signer_configured')}",
            f"- Problèmes : {d.get('issues') or 'aucun'}",
            "",
            "## 2. Validation des données (5–15 min)",
            f"- Maths vs chaîne — V2 : {v.get('v2')}, Solidly : {v.get('solidly')}, V3 : {v.get('v3')}",
            "- Simulation complète vs estimation : " + str({k: val for k, val in (v.get('sim_vs_estimate') or {}).items() if k != 'samples'}),
            "",
            "## 3. Recherche + simulation (15–30 min)",
            f"- {s.get('blocks')} blocs, {s.get('candidates')} candidats, {s.get('positives')} à net attendu > 0, {s.get('simulations')} simulations ({s.get('sim_failures')} échecs, {s.get('sim_below_estimate')} sous l'estimation)",
            f"- Étiquettes ghost (re-simulation au bloc N+1) : {s.get('ghost_positives')}/{s.get('ghost_labeled')} positives",
            f"- Latence du cycle p50/p95 : {fmt(s.get('cycle_ms_p50'))}/{fmt(s.get('cycle_ms_p95'))} ms ; meilleur net attendu max {fmt(s.get('best_expected_net_eur_max'), 4)} €",
            f"- Rejets : {s.get('rejections')}",
            "",
            "## 4. Auto-correction (30–45 min)",
            f"- Constats : {sc.get('diagnose', {}).get('findings') or 'aucun'}",
            f"- Changements proposés (paramètres autorisés uniquement) : {sc.get('changes') or 'aucun'}",
            f"- Décision : **{sc.get('decision')}**",
        ]
        for it in sc.get("iterations", []):
            ab = it["ab"]
            lines.append(f"- A/B sur {ab['blocks']} blocs identiques : référence {ab['score_eur']['ref']:.4f} € vs candidat {ab['score_eur']['cand']:.4f} € ; {ab['counts']}")
        lines += [
            "",
            "## 5. Validation comparative (45–55 min)",
            f"- Décision : **{cv.get('decision')}** {cv.get('ab', {}).get('score_eur', '')}",
            "",
            "## 6. Fiabilité mesurée",
            f"- Observations : {rel.get('n')} (minimum requis {rel.get('min_observations')}), taux observé {fmt(rel.get('rate'), 3)}",
            f"- Borne inférieure crédible ({rel.get('credible_level')}) : {fmt(rel.get('global_lower'), 3)} ; seuil {rel.get('threshold')}",
            f"- Verdict : **{rel.get('label')}**",
            f"- Régression logistique : {rel.get('logistic')}",
            "",
            "## 7. Décision de maturité",
        ]
        for c in r["risk"]["criteria"]:
            lines.append(f"- {'✅' if c['ok'] else '❌'} {c['name']} — {c['detail']}")
        lines += ["", f"**Conclusion :** {r['status']} — {r['sub_status']}.",
                  "Aucun critère n'a été assoupli ; le passage au réel reste conditionné à l'ensemble des critères ci-dessus et à une politique d'autorisation signée par l'opérateur."]
        return "\n".join(lines)


def fmt(x, nd: int = 0) -> str:
    if x is None:
        return "n/a"
    try:
        return f"{float(x):.{nd}f}"
    except (TypeError, ValueError):
        return str(x)
