"""Read-only mode on a real network has NO deployed executor: simulation then injects the compiled executor bytecode
at a scratch address through eth_call state overrides. This proves the override simulation returns exactly the same
profit as the deployed contract (same block, same route, same amount) — including flash-loan callbacks."""
from __future__ import annotations

import pytest

from arbbot.simulation.simulator import Simulator
from tests.conftest import requires_devnet

pytestmark = [requires_devnet, pytest.mark.devnet]


async def test_state_override_simulation_equals_deployed(tmp_path, devnet_cfg):
    from tests.test_devnet_e2e import _positive_candidates, _runtime

    rt = await _runtime(tmp_path)
    try:
        b, pos = await _positive_candidates(rt, devnet_cfg)
        override_sim = Simulator(rt.rpc, "", rt.simulator.sender, rt.settings.executor_artifact, True)
        checked = 0
        for opp in pos[:3]:
            dep = await rt.simulator.simulate(opp, min_profit=1, block=b)
            ovr = await override_sim.simulate(opp, min_profit=1, block=b)
            assert dep.mode == "deployed" and ovr.mode == "state-override"
            assert dep.ok and ovr.ok, (dep.error, ovr.error)
            assert ovr.profit == dep.profit == opp.profit.gross_profit - opp.profit.fees.flash_fee
            checked += 1
        assert checked >= 1
        # and a route that cannot repay must revert identically in both modes (never a silent success)
        bad = pos[0]
        dep = await rt.simulator.simulate(bad, min_profit=bad.profit.gross_profit * 10 + 1, block=b)
        ovr = await override_sim.simulate(bad, min_profit=bad.profit.gross_profit * 10 + 1, block=b)
        assert not dep.ok and not ovr.ok and "InsufficientProfit" in (dep.error or "") and "InsufficientProfit" in (ovr.error or "")
    finally:
        await rt.stop()
