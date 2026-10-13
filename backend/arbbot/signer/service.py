"""Signer service — a SEPARATE process that owns the private key and enforces its OWN copy of the policy.

Threat model: the strategy engine (and anything it runs: lab, self-correction, API) is treated as untrusted.
It can only POST unsigned transactions here. The signer:
  * loads the key from an encrypted keystore (ARB_SIGNER_KEYSTORE + ARB_SIGNER_KEYSTORE_PASSWORD) — never from the
    repository, never from chat. ARB_SIGNER_PRIVATE_KEY is accepted only when ARB_SIGNER_ALLOW_RAW_KEY=1 (devnet).
  * re-validates every request against authorization.json independently (target, chain, selector, token,
    borrow cap, gas limit, fee cap, per-tx and cumulative gas budget, tx count, validity window, minProfit > 0).
  * persists its own counters (tx count, worst-case gas committed) so a restart of the engine cannot reset them.
  * requires a shared secret header (ARB_SIGNER_TOKEN) and binds to 127.0.0.1 by default.
It never returns the key, never signs arbitrary messages, and never signs `value > 0` or a non-executor target.
"""
from __future__ import annotations

import json
import logging
import os
import pathlib
import sys
import time

from eth_abi import decode as abi_decode
from eth_account import Account
from eth_utils import to_checksum_address
from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel

from ..config.policy import AuthorizationPolicy, load_policy
from ..data.rpc import selector

log = logging.getLogger("arbbot.signer")

ARB_PARAMS_T = "(uint8,address,address,uint256,uint256,uint256,(uint8,address,address,address,uint32,uint256)[])"
EXECUTE_SELECTOR = selector(f"executeArbitrage({ARB_PARAMS_T})")


class SignRequest(BaseModel):
    chain_id: int
    to: str
    data: str
    nonce: int
    gas: int
    max_fee_per_gas: int
    max_priority_fee_per_gas: int
    value: int = 0
    context: dict = {}


class SignerState:
    def __init__(self, path: pathlib.Path):
        self.path = path
        self.tx_count = 0
        self.committed_gas_wei = 0  # worst-case gas of every tx signed (gas × maxFee)
        self.history: list[dict] = []
        if path.exists():
            d = json.loads(path.read_text())
            self.tx_count = d.get("tx_count", 0)
            self.committed_gas_wei = d.get("committed_gas_wei", 0)
            self.history = d.get("history", [])[-200:]

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps({"tx_count": self.tx_count, "committed_gas_wei": self.committed_gas_wei,
                                         "history": self.history[-200:]}, indent=1))


class Signer:
    def __init__(self, policy: AuthorizationPolicy, account, state: SignerState, policy_path: str):
        self.policy = policy
        self.policy_path = policy_path
        self.account = account
        self.state = state

    @property
    def address(self) -> str:
        return self.account.address

    def check(self, req: SignRequest) -> tuple[bool, str]:
        p = self.policy
        ok, why = p.is_valid_now()
        if not ok:
            return False, f"policy: {why}"
        if p.wallet_address.lower() != self.address.lower():
            return False, "policy wallet_address does not match the loaded key"
        if req.chain_id not in p.chain_ids:
            return False, f"chain {req.chain_id} not authorised"
        if req.value != 0:
            return False, "value must be 0"
        if req.to.lower() != p.executor_contract.lower():
            return False, "target is not the authorised executor contract"
        data = bytes.fromhex(req.data[2:] if req.data.startswith("0x") else req.data)
        if data[:4] != EXECUTE_SELECTOR:
            return False, "only executeArbitrage(ArbParams) may be signed"
        try:
            (params,) = abi_decode([ARB_PARAMS_T], data[4:])
        except Exception as e:  # noqa: BLE001
            return False, f"undecodable calldata: {e}"
        source, provider, token, amount, min_profit, deadline, hops = params
        if min_profit <= 0:
            return False, "minProfit must be > 0 (on-chain profit guard)"
        if deadline < time.time() or deadline > time.time() + 900:
            return False, "deadline must be within the next 15 minutes"
        if not 2 <= len(hops) <= 4:
            return False, "hop count out of range"
        rule = next((r for r in p.tokens.values() if r.address.lower() == token.lower()), None)
        if rule is None:
            return False, f"token {token} not in policy.tokens"
        if rule.max_borrow <= 0 or amount > int(rule.max_borrow * 10**rule.decimals):
            return False, f"borrow {amount} exceeds policy cap for {token}"
        if req.gas > p.max_gas_limit:
            return False, f"gas limit {req.gas} > {p.max_gas_limit}"
        if req.max_fee_per_gas > int(p.max_fee_per_gas_gwei * 1e9):
            return False, "maxFeePerGas above policy cap"
        worst = req.gas * req.max_fee_per_gas
        if worst > p.max_gas_per_tx_native * 1e18:
            return False, f"worst-case gas {worst / 1e18:.6f} ETH > per-tx cap"
        if self.state.committed_gas_wei + worst > p.max_total_budget_native * 1e18:
            return False, "cumulative worst-case gas budget would be exceeded"
        if self.state.tx_count >= p.max_transactions:
            return False, "transaction cap reached"
        return True, "ok"

    def sign(self, req: SignRequest) -> dict:
        ok, why = self.check(req)
        if not ok:
            self.state.history.append({"ts": time.time(), "ok": False, "reason": why, "ctx": req.context})
            self.state.save()
            raise HTTPException(status_code=403, detail=why)
        tx = {
            "chainId": req.chain_id, "to": to_checksum_address(req.to), "data": req.data, "nonce": req.nonce, "gas": req.gas,
            "maxFeePerGas": req.max_fee_per_gas, "maxPriorityFeePerGas": req.max_priority_fee_per_gas, "value": 0, "type": 2,
        }
        signed = self.account.sign_transaction(tx)
        self.state.tx_count += 1
        self.state.committed_gas_wei += req.gas * req.max_fee_per_gas
        self.state.history.append({"ts": time.time(), "ok": True, "hash": signed.hash.hex(), "ctx": req.context})
        self.state.save()
        return {"raw_tx": "0x" + signed.raw_transaction.hex(), "hash": "0x" + signed.hash.hex()}


def load_account():
    ks = os.environ.get("ARB_SIGNER_KEYSTORE")
    if ks:
        pw = os.environ.get("ARB_SIGNER_KEYSTORE_PASSWORD")
        if pw is None:
            import getpass

            pw = getpass.getpass("Keystore password: ")
        return Account.from_key(Account.decrypt(json.loads(pathlib.Path(ks).read_text()), pw))
    raw = os.environ.get("ARB_SIGNER_PRIVATE_KEY")
    if raw and os.environ.get("ARB_SIGNER_ALLOW_RAW_KEY") == "1":
        log.warning("raw private key from environment — acceptable ONLY on a local devnet")
        return Account.from_key(raw)
    raise SystemExit("No key: set ARB_SIGNER_KEYSTORE (+ ARB_SIGNER_KEYSTORE_PASSWORD) — see docs/06_wallet_securise.md")


def build_app() -> FastAPI:
    policy_path = os.environ.get("ARB_POLICY_PATH", "authorization.json")
    policy = load_policy(policy_path)
    account = load_account()
    state = SignerState(pathlib.Path(os.environ.get("ARB_SIGNER_STATE", "data/signer_state.json")))
    signer = Signer(policy, account, state, policy_path)
    token = os.environ.get("ARB_SIGNER_TOKEN", "")
    if not token:
        raise SystemExit("ARB_SIGNER_TOKEN must be set (shared secret between engine and signer)")
    app = FastAPI(title="arbbot signer", docs_url=None, redoc_url=None)

    def auth(x_signer_token: str | None):
        if x_signer_token != token:
            raise HTTPException(status_code=401, detail="bad token")

    @app.get("/health")
    def health(x_signer_token: str | None = Header(default=None)):
        auth(x_signer_token)
        ok, why = policy.is_valid_now()
        return {
            "address": account.address, "policy_digest": policy.digest(), "policy_valid": ok, "policy_reason": why,
            "tx_count": state.tx_count, "committed_gas_native": state.committed_gas_wei / 1e18,
            "budget_native": policy.max_total_budget_native, "max_transactions": policy.max_transactions,
        }

    @app.post("/sign")
    async def sign(req: SignRequest, request: Request, x_signer_token: str | None = Header(default=None)):
        auth(x_signer_token)
        return signer.sign(req)

    @app.get("/history")
    def history(x_signer_token: str | None = Header(default=None)):
        auth(x_signer_token)
        return state.history[-50:]

    return app


def main() -> None:
    import uvicorn

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    host = os.environ.get("ARB_SIGNER_HOST", "127.0.0.1")
    port = int(os.environ.get("ARB_SIGNER_PORT", "8787"))
    uvicorn.run(build_app(), host=host, port=port, log_level="warning")


if __name__ == "__main__":
    sys.exit(main())
