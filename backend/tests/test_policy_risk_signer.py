"""Financial guard-rails: policy immutability, tunables allowlist, risk state machine, signer refusals."""
from __future__ import annotations

import json
import time

import pytest
from eth_abi import encode as abi_encode
from eth_account import Account

from arbbot.config.policy import AuthorizationPolicy, EXAMPLE, TokenRule, load_policy
from arbbot.config.tunables import TunableParams
from arbbot.reliability.model import INSUFFICIENT, Observation, ReliabilityModel
from arbbot.risk.manager import BotStatus, RiskManager
from arbbot.signer.service import ARB_PARAMS_T, EXECUTE_SELECTOR, SignRequest, Signer, SignerState

KEY = "0x" + "11" * 32
ACCT = Account.from_key(KEY)
EXECUTOR = "0x" + "e1" * 20
TOKEN = "0x" + "aa" * 20


def make_policy(**over) -> AuthorizationPolicy:
    base = dict(EXAMPLE)
    base.update({
        "enabled": True, "wallet_address": ACCT.address, "chain_ids": [31337], "executor_contract": EXECUTOR,
        "tokens": {"USDC": {"address": TOKEN, "decimals": 6, "max_borrow": 10_000.0}},
        "valid_from": 0, "valid_until": time.time() + 3600,
    })
    base.update(over)
    return AuthorizationPolicy.model_validate(base)


def calldata(token=TOKEN, amount=1_000 * 10**6, min_profit=1, deadline=None, hops=2) -> str:
    deadline = deadline or int(time.time()) + 120
    hop = (0, "0x" + "01" * 20, token, token, 3000, 0)
    params = (2, "0x" + "02" * 20, token, amount, min_profit, deadline, [hop] * hops)
    return "0x" + (EXECUTE_SELECTOR + abi_encode([ARB_PARAMS_T], [params])).hex()


def req(**over) -> SignRequest:
    d = dict(chain_id=31337, to=EXECUTOR, data=calldata(), nonce=0, gas=600_000, max_fee_per_gas=int(0.1e9),
             max_priority_fee_per_gas=1000, value=0)
    d.update(over)
    return SignRequest(**d)


# ---------------------------------------------------------------- policy / tunables


def test_policy_is_frozen_and_rejects_unknown_fields():
    p = make_policy()
    with pytest.raises(Exception):
        p.max_total_budget_native = 100  # type: ignore[misc]
    with pytest.raises(Exception):
        AuthorizationPolicy.model_validate({**EXAMPLE, "backdoor": True})


def test_policy_disabled_or_expired_is_invalid(tmp_path):
    assert make_policy(enabled=False).is_valid_now()[0] is False
    assert make_policy(valid_until=time.time() - 1).is_valid_now()[0] is False
    assert make_policy(max_transactions=0).is_valid_now()[0] is False
    assert make_policy().is_valid_now()[0] is True
    # missing file → disabled policy, never an exception
    assert load_policy(tmp_path / "missing.json").enabled is False


def test_self_correction_cannot_touch_financial_limits():
    t = TunableParams()
    for forbidden in ("max_total_budget_native", "min_success_probability", "allowed_dexes", "executor_contract",
                      "max_cumulative_loss_native", "wallet_address", "enabled"):
        with pytest.raises(PermissionError):
            t.with_changes(**{forbidden: 1})
    t2 = t.with_changes(min_spread_bps=7.5)
    assert t2.min_spread_bps == 7.5 and t2.version == t.version + 1 and t.min_spread_bps == TunableParams.min_spread_bps
    assert "min_success_probability" not in TunableParams.ALLOWED_KEYS


def test_tunables_roundtrip(tmp_path):
    t = TunableParams().with_changes(grid_points=12)
    t.save(tmp_path / "t.json")
    assert TunableParams.load(tmp_path / "t.json").grid_points == 12


# ---------------------------------------------------------------- reliability


def test_reliability_insufficient_then_ok():
    m = ReliabilityModel(min_observations=30, credible_level=0.9, threshold=0.75)
    feats = {"margin_bps": 10, "hops": 2, "route_class": "UNIV2"}
    e = m.estimate(feats)
    assert e.sufficient is False and e.label == INSUFFICIENT and e.p_lower is None
    for i in range(29):
        m.add(Observation(time.time(), feats, 1, "ghost"))
    assert m.estimate(feats).sufficient is False  # 29 < 30: still not demonstrated
    m.add(Observation(time.time(), feats, 1, "ghost"))
    e = m.estimate(feats)
    assert e.sufficient is True and e.p_lower is not None and e.p_lower >= 0.75 and e.label == "OK"


def test_reliability_bad_outcomes_fail_threshold():
    m = ReliabilityModel(min_observations=30, credible_level=0.9, threshold=0.75)
    feats = {"margin_bps": 10, "hops": 2, "route_class": "UNIV2"}
    for i in range(40):
        m.add(Observation(time.time(), feats, 1 if i % 2 == 0 else 0, "ghost"))
    e = m.estimate(feats)
    assert e.sufficient and e.p_lower < 0.75 and e.label == "FIABILITÉ INSUFFISANTE"


def test_reliability_never_fabricates_from_other_buckets():
    m = ReliabilityModel(min_observations=30, credible_level=0.9, threshold=0.75)
    good = {"margin_bps": 10, "hops": 2, "route_class": "UNIV2"}
    other = {"margin_bps": 60, "hops": 3, "route_class": "UNIV3"}
    for _ in range(100):
        m.add(Observation(time.time(), good, 1, "ghost"))
    assert m.estimate(other).sufficient is False


# ---------------------------------------------------------------- risk manager


def _rm(policy=None, n_obs=0, rate=1.0) -> RiskManager:
    rel = ReliabilityModel(min_observations=30, credible_level=0.9, threshold=0.75)
    feats = {"margin_bps": 10, "hops": 2, "route_class": "UNIV2"}
    for i in range(n_obs):
        rel.add(Observation(time.time(), feats, 1 if i < n_obs * rate else 0, "ghost"))
    rm = RiskManager(policy or make_policy(), rel, tests_passed=True, contract_tested=True, financial_math_validated=True)
    rm.flags["simulations_ok"] = 50
    return rm


def test_status_learning_without_data():
    rm = _rm()
    st = rm.evaluate(policy_signer_ok=True, data_age_ms=100, rpc_ok=True)
    assert st.status == BotStatus.LEARNING and INSUFFICIENT in st.sub_status


def test_status_reliability_insufficient():
    rm = _rm(n_obs=60, rate=0.6)
    assert rm.evaluate(policy_signer_ok=True, data_age_ms=100, rpc_ok=True).status == BotStatus.RELIABILITY_INSUFFICIENT


def test_status_ready_but_authorization_missing():
    rm = _rm(policy=make_policy(enabled=False), n_obs=60, rate=1.0)
    st = rm.evaluate(policy_signer_ok=False, data_age_ms=100, rpc_ok=True)
    assert st.status == BotStatus.READY_LIMITED_LIVE and "AUTORISATION FINANCIÈRE MANQUANTE" in st.sub_status


def test_status_ready_then_live_then_suspended_on_losses():
    rm = _rm(n_obs=60, rate=1.0)
    st = rm.evaluate(policy_signer_ok=True, data_age_ms=100, rpc_ok=True)
    assert st.status == BotStatus.READY_LIMITED_LIVE and rm.activate_live()
    assert rm.state.status == BotStatus.LIVE_ACTIVE
    # two consecutive failures → suspended (policy max_consecutive_failures = 2)
    rm.record_execution(success=False, gas_cost_wei=int(0.0001e18), realized_net_native=-0.0001)
    assert rm.state.status == BotStatus.LIVE_ACTIVE
    rm.record_execution(success=False, gas_cost_wei=int(0.0001e18), realized_net_native=-0.0001)
    assert rm.state.status == BotStatus.SUSPENDED and "consecutive" in rm.state.suspended_reason
    # no auto-resume unless policy says so
    rm.evaluate(policy_signer_ok=True, data_age_ms=100, rpc_ok=True)
    assert rm.state.status == BotStatus.SUSPENDED


def test_budget_checks_and_kill_switch():
    rm = _rm(n_obs=60)
    ok, why = rm.can_afford(900_000, int(0.2e9))  # 0.00018 ETH < 0.0004 cap
    assert ok, why
    assert rm.can_afford(900_000, int(0.5e9))[0] is False  # above max fee cap
    assert rm.can_afford(2_000_000, int(0.2e9))[0] is False  # gas limit
    rm.kill("test")
    assert rm.state.status == BotStatus.SUSPENDED and rm.state.kill_switch
    rm.evaluate(policy_signer_ok=True, data_age_ms=100, rpc_ok=True)
    assert rm.state.status == BotStatus.SUSPENDED
    rm.degrade("x")  # degrade only acts in LIVE_ACTIVE
    assert rm.state.status == BotStatus.SUSPENDED


def test_cumulative_loss_limit():
    rm = _rm(n_obs=60)
    rm.evaluate(policy_signer_ok=True, data_age_ms=100, rpc_ok=True)
    rm.activate_live()
    rm.record_execution(success=True, gas_cost_wei=10**14, realized_net_native=-0.0031)  # loss beyond 0.003
    assert rm.state.status == BotStatus.SUSPENDED and "loss limit" in rm.state.suspended_reason


# ---------------------------------------------------------------- signer


def _signer(tmp_path, policy=None) -> Signer:
    return Signer(policy or make_policy(), ACCT, SignerState(tmp_path / "state.json"), "mem")


def test_signer_signs_valid_request(tmp_path):
    s = _signer(tmp_path)
    out = s.sign(req())
    assert out["raw_tx"].startswith("0x") and s.state.tx_count == 1


@pytest.mark.parametrize("bad, field", [
    ({"to": "0x" + "ff" * 20}, "target"),
    ({"chain_id": 8453}, "chain"),
    ({"value": 1}, "value"),
    ({"gas": 5_000_000}, "gas limit"),
    ({"max_fee_per_gas": int(5e9)}, "maxFeePerGas"),
    ({"data": "0x12345678" + "00" * 64}, "executeArbitrage"),
    ({"data": calldata(min_profit=0)}, "minProfit"),
    ({"data": calldata(amount=20_000 * 10**6)}, "borrow"),
    ({"data": calldata(token="0x" + "cc" * 20)}, "not in policy"),
    ({"data": calldata(deadline=int(time.time()) + 3600)}, "deadline"),
])
def test_signer_refuses(tmp_path, bad, field):
    s = _signer(tmp_path)
    ok, why = s.check(req(**bad))
    assert ok is False and field.lower().split()[0] in why.lower(), why


def test_signer_enforces_cumulative_budget_and_count(tmp_path):
    s = _signer(tmp_path, make_policy(max_transactions=2, max_total_budget_native=0.0003, max_gas_per_tx_native=0.0002))
    r = req(gas=750_000, max_fee_per_gas=int(0.2e9))  # worst case 0.00015 ETH
    s.sign(r)
    s.sign(r)  # cumulative 0.0003 → budget reached
    ok, why = s.check(r)
    assert ok is False and ("budget" in why or "cap" in why)
    # state survives a restart
    s2 = Signer(s.policy, ACCT, SignerState(tmp_path / "state.json"), "mem")
    assert s2.state.tx_count == 2


def test_signer_refuses_when_policy_wallet_differs(tmp_path):
    other = Account.from_key("0x" + "22" * 32)
    s = Signer(make_policy(wallet_address=other.address), ACCT, SignerState(tmp_path / "s.json"), "mem")
    assert s.check(req())[0] is False


def test_load_account_from_encrypted_keystore_only(tmp_path, monkeypatch):
    """Outside the devnet the signer key comes from an encrypted keystore (password via env or prompt); a raw key in
    the environment is refused unless ARB_SIGNER_ALLOW_RAW_KEY=1 — the engine never sees key material."""
    from arbbot.signer.service import load_account

    acct = Account.create()
    ks = tmp_path / "executor.json"
    ks.write_text(json.dumps(Account.encrypt(acct.key, "correct horse battery staple")))
    monkeypatch.setenv("ARB_SIGNER_KEYSTORE", str(ks))
    monkeypatch.setenv("ARB_SIGNER_KEYSTORE_PASSWORD", "correct horse battery staple")
    loaded = load_account()
    assert loaded.address == acct.address
    signed = loaded.sign_transaction({"to": acct.address, "value": 0, "gas": 21_000, "maxFeePerGas": 10**8,
                                      "maxPriorityFeePerGas": 10**6, "nonce": 0, "chainId": 8453, "data": b""})
    assert Account.recover_transaction(signed.raw_transaction) == acct.address
    # wrong password → no account, no silent fallback
    monkeypatch.setenv("ARB_SIGNER_KEYSTORE_PASSWORD", "wrong")
    with pytest.raises(ValueError):
        load_account()
    # raw key refused without the explicit devnet-only flag
    monkeypatch.delenv("ARB_SIGNER_KEYSTORE")
    monkeypatch.delenv("ARB_SIGNER_KEYSTORE_PASSWORD")
    monkeypatch.setenv("ARB_SIGNER_PRIVATE_KEY", acct.key.hex())
    monkeypatch.delenv("ARB_SIGNER_ALLOW_RAW_KEY", raising=False)
    with pytest.raises(SystemExit):
        load_account()
