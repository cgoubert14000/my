"""The « memecoin bot » reality check runs end to end against the devnet (PairCreated + Sync logs of the local V2
factories): it must reconstruct every WETH pair, price the naive sniper exactly and write the JSON/MD reports."""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

import pytest

from tests.conftest import requires_devnet

pytestmark = [requires_devnet, pytest.mark.devnet]
REPO = pathlib.Path(__file__).resolve().parents[2]


def test_memecoin_reality_check_on_devnet(tmp_path):
    dep = json.loads((REPO / "devnet" / "deployments.local.json").read_text())
    weth = dep["native_wrapped"].lower()
    n_weth_pairs = sum(1 for p in dep["pools"] if p["kind"] == "UNIV2" and weth in (p["token0"].lower(), p["token1"].lower()))
    r = subprocess.run([sys.executable, str(REPO / "scripts" / "memecoin_reality_check.py"), "--devnet", str(REPO / "devnet" / "deployments.local.json"),
                        "--days", "30", "--out-dir", str(tmp_path), "--tag", "t", "--max-pairs", "50"], capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    doc = json.loads((tmp_path / "memecoin_check_local_t.json").read_text())
    s = doc["summary"]
    assert s["pairs_created_with_weth"] == n_weth_pairs and s["pairs_analysed"] == n_weth_pairs
    assert s["rug_count"] == 0  # the devnet never pulls liquidity
    for p in doc["pairs"]:
        assert p["syncs"] >= 1 and p["first_weth"] > 0 and p["peak_weth"] >= p["last_weth"] > 0
        for h, v in p["pnl"].items():
            assert v is None or abs(v) < s["buy_eth"]  # a sniper can never lose more than the buy (and gas) on an AMM
    md = (tmp_path / "memecoin_check_local_t.md").read_text()
    assert "borne supérieure" in md and "Trades gagnants" in md
