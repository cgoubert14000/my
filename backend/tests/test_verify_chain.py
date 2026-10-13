"""`arbbot verify-chain`: the live pre-flight of a chain configuration. Runs fully against the devnet; the digest /
revocation logic is unit-tested so a configuration change can never keep a stale 'verified' badge."""
from __future__ import annotations

import dataclasses
import json

import pytest

from arbbot.config.chains import ARBITRUM, BASE, address_source, get_chain
from arbbot.config.settings import Settings
from arbbot.ops.verify import config_digest, load_verification, verified_file, verify_chain
from tests.conftest import REPO, requires_devnet


def test_every_mainnet_address_has_a_documented_source():
    for ch in (BASE, ARBITRUM):
        addrs = [ch.wrapped_native, ch.multicall3] + [t.address for t in ch.tokens.values()] + [d.factory for d in ch.dexes] + [p.address for p in ch.flash_providers]
        if ch.l1_fee_model == "opstack":
            addrs.append(ch.opstack_gas_oracle)
        assert all("UNKNOWN" not in address_source(a) for a in addrs), [a for a in addrs if "UNKNOWN" in address_source(a)]
    # unconfirmed factories are disabled by default
    assert not next(d for d in BASE.dexes if d.id == "baseswap_v2").enabled


def test_digest_changes_with_any_address_and_revokes_verification(tmp_path):
    local = get_chain("local", REPO / "devnet" / "deployments.local.json") if (REPO / "devnet" / "deployments.local.json").exists() else BASE
    d0 = config_digest(local)
    changed = dataclasses.replace(local, multicall3="0x" + "12" * 20)
    assert config_digest(changed) != d0
    s = Settings(chain="local", data_dir=tmp_path)
    f = verified_file(s, local)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps({"ok": True, "config_digest": d0, "ts": 1}))
    assert load_verification(s, local) is not None
    assert load_verification(s, changed) is None  # same file, different config → not verified
    f.write_text(json.dumps({"ok": False, "config_digest": d0, "ts": 1}))
    assert load_verification(s, local) is None  # a failed run never counts


async def test_real_chain_config_with_unreachable_rpc_fails_closed(tmp_path):
    s = Settings(chain="base", rpc_http_url="http://127.0.0.1:1", rpc_timeout_s=0.5, data_dir=tmp_path)
    rep = await verify_chain(s, write=False, log=lambda *_: None)
    assert rep.ok is False
    assert rep.checks[0].name == "rpc_reachable" and rep.checks[0].ok is False
    assert load_verification(s, BASE) is None


@pytest.mark.devnet
@requires_devnet
async def test_verify_chain_passes_on_devnet_and_records_digest(tmp_path):
    s = Settings(chain="local", data_dir=tmp_path)
    rep = await verify_chain(s, write=True, log=lambda *_: None)
    names = {c.name: c for c in rep.checks}
    assert rep.ok, [c for c in rep.checks if not c.ok]
    assert names["chain_id"].ok and names["multicall3"].ok and names["eth_call_state_override"].ok
    assert names["pool_discovery"].ok and len(rep.pools) == 18
    assert all(r["depth_usd"] and r["depth_usd"] > 0 for r in rep.pools)
    assert names["flash_any_capacity"].ok and rep.providers["MORPHO"]["fee_bps"] == 0.0 and rep.providers["AAVE_V3"]["fee_bps"] == 5.0
    assert rep.network["block_time_measured_s"] == pytest.approx(2.0, abs=0.5)
    chain = get_chain("local", REPO / "devnet" / "deployments.local.json")
    stored = load_verification(s, chain)
    assert stored and stored["config_digest"] == config_digest(chain) and stored["pools"] == 18
