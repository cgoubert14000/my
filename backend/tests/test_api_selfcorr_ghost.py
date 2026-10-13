"""Self-correction repository (git-isolated), ghost dedup, and the HTTP API driven through ASGI with an injected
runtime (devnet). Emergency stop is exercised through the API exactly as the dashboard button does it."""
from __future__ import annotations

import asyncio

import httpx
import pytest

from arbbot.config.tunables import TunableParams
from arbbot.lab.selfcorr import ParamRepo
from arbbot.risk.manager import BotStatus
from tests.conftest import requires_devnet

# ---------------------------------------------------------------------------- self-correction (no chain needed)


def test_param_repo_propose_accept_rollback_are_git_isolated(tmp_path):
    repo = ParamRepo(tmp_path / "selfcorr")
    ref = repo.reference()
    assert ref.min_spread_bps == TunableParams().min_spread_bps
    cand = ref.with_changes(min_spread_bps=ref.min_spread_bps + 2.0)
    branch = repo.propose(cand, "widen spread")
    # proposing never touches the reference
    assert repo.reference().min_spread_bps == ref.min_spread_bps
    repo.rollback(branch)
    assert repo.reference().min_spread_bps == ref.min_spread_bps
    # accepting fast-forwards main onto the candidate
    branch2 = repo.propose(cand, "widen spread again")
    sha = repo.accept(branch2)
    assert sha
    assert repo.reference().min_spread_bps == ref.min_spread_bps + 2.0
    log = repo.log()
    assert any("candidate: widen spread" in line for line in log) and any("reference" in line for line in log)


def test_self_correction_cannot_touch_financial_controls():
    t = TunableParams()
    for forbidden in ("max_total_budget_native", "max_slippage_bps", "min_success_probability", "wallet_address", "allowed_contracts", "reliability_threshold"):
        with pytest.raises(PermissionError):
            t.with_changes(**{forbidden: 1})
    # and the allowlist itself is explicit and small
    assert "min_spread_bps" in TunableParams.ALLOWED_KEYS
    assert not any(k.startswith(("max_total", "allowed_", "min_success")) for k in TunableParams.ALLOWED_KEYS)


# ---------------------------------------------------------------------------- devnet-backed tests

pytestmark_devnet = [requires_devnet, pytest.mark.devnet]


@pytest.mark.devnet
@requires_devnet
async def test_ghost_dedup_one_observation_per_route_per_window(tmp_path, devnet_cfg):
    from tests.test_devnet_e2e import _positive_candidates, _runtime

    rt = await _runtime(tmp_path)
    try:
        b, pos = await _positive_candidates(rt, devnet_cfg)
        opp = pos[0]
        g = rt.ghost
        g.pending.clear()
        g.last_labeled_block.clear()
        assert g.enqueue(opp, b + 100) is True
        assert g.enqueue(opp, b + 100) is False  # same route, same block
        assert g.enqueue(opp, b + 105) is False  # same persistent gap inside the window
        assert g.enqueue(opp, b + 100 + g.relabel_every_blocks) is True  # new window → new evidence
        g.pending.clear()
    finally:
        await rt.stop()


@pytest.mark.devnet
@requires_devnet
async def test_api_status_opportunities_emergency_stop_and_tunable_guard(tmp_path, devnet_cfg):
    from arbbot.api.server import create_app
    from tests.test_devnet_e2e import _next_block, _positive_candidates, _runtime

    rt = await _runtime(tmp_path)
    try:
        b0, _ = await _positive_candidates(rt, devnet_cfg)
        app = create_app(rt.settings, runtime=rt)
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
            h = (await c.get("/api/health")).json()
            assert h["ok"] is True
            st = (await c.get("/api/status")).json()
            assert st["chain"]["is_devnet"] is True and st["mode"] == "ghost" and st["paused"] is False
            assert st["risk"]["status_code"] in (BotStatus.LEARNING.name, BotStatus.SIMULATION.name, BotStatus.RELIABILITY_INSUFFICIENT.name)
            opps = (await c.get("/api/opportunities/live?limit=50")).json()
            assert opps and {"expected_net", "fees", "decision", "reasons", "p_lower", "uncertainty", "sim"} <= set(opps[0])
            assert all(o["decision"] != "EXECUTED" for o in opps)  # ghost mode: nothing executed
            rel = (await c.get("/api/reliability")).json()
            assert "label" in rel and rel["threshold"] == pytest.approx(0.75)
            sg = (await c.get("/api/signer")).json()
            assert sg["configured"] is False and "AUTORISATION FINANCIÈRE MANQUANTE" in sg["message"]

            # the strategy engine's tunables can be changed by the operator, financial controls cannot
            r = await c.post("/api/control/tunables", json={"min_spread_bps": 7.5})
            assert r.status_code == 200 and rt.tunables.min_spread_bps == 7.5
            r = await c.post("/api/control/tunables", json={"max_total_budget_native": 100})
            assert r.status_code == 403
            r = await c.post("/api/control/tunables", json={"no_such_param": 1})
            assert r.status_code in (400, 403)

            # emergency stop via the API: suspended, no decisions while paused, resume goes back to simulation
            r = await c.post("/api/control/emergency-stop", json={"reason": "test"})
            assert r.status_code == 200 and r.json()["status_code"] == BotStatus.SUSPENDED.name
            assert rt.paused is True
            b = await _next_block(rt, b0)  # a fresh block (the previous one is cached by the cycle lock)
            await rt.collector.refresh(b)
            cyc = await rt.process_block(b)
            assert cyc.get("paused") is True and "candidates" not in cyc
            st = (await c.get("/api/status")).json()
            assert st["paused"] is True and st["risk"]["status_code"] == BotStatus.SUSPENDED.name
            r = await c.post("/api/control/resume")
            assert r.status_code == 200 and rt.paused is False
            st = (await c.get("/api/status")).json()
            assert st["risk"]["status_code"] != BotStatus.SUSPENDED.name and st["mode"] == "ghost"

            # activate-live without signer / criteria must be refused
            r = await c.post("/api/control/activate-live")
            assert r.status_code == 200 and r.json()["ok"] is False
            ev = (await c.get("/api/events?limit=20")).json()
            assert any(e["kind"] in ("emergency_stop", "control") for e in ev)
    finally:
        await rt.stop()
        await asyncio.sleep(0)


@pytest.mark.devnet
@requires_devnet
async def test_ghost_session_report_counts_closest_and_latest_files(tmp_path, devnet_cfg):
    """Session report: exact counts, closest-to-profit table when nothing is positive, stable latest_<chain> files."""
    import json
    import time

    from arbbot.ops import ghost_report
    from tests.test_devnet_e2e import _positive_candidates, _runtime

    rt = await _runtime(tmp_path)
    try:
        t0 = time.time() - 1
        b, _ = await _positive_candidates(rt, devnet_cfg)
        out = tmp_path / "rep"
        files = ghost_report.write(rt, out, started_at=t0, started_block=b, tag="t")
        rep = json.loads((out / "ghost_local_t.json").read_text())
        assert rep["opportunities"]["total"] == rt.db.count_opportunities(since=t0)
        assert rep["generated_ts"] > t0 and rep["chain"]["is_devnet"] is True
        assert (out / "latest_local.json").exists() and (out / "latest_local.md").exists()
        assert (out / "latest_local.json").read_text() == (out / "ghost_local_t.json").read_text()
        md = (out / "ghost_local_t.md").read_text()
        assert "DEVNET" in md.upper()
        if not rep["opportunities"]["best"]:
            assert rep["opportunities"]["closest"] and "plus proches de la rentabilité" in md
        assert set(files) >= {"json", "md", "csv"}
    finally:
        await rt.stop()
