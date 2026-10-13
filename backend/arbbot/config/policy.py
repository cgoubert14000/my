"""AuthorizationPolicy — the pre-authorised financial envelope. READ-ONLY for the engine.

The strategy engine, the lab and the self-correction loop can only *read* this object. It is loaded from a JSON
file the operator writes by hand (see authorization.example.json), hashed, and the hash is logged with every
decision report. The signer service loads its own copy and enforces the same limits independently, so a bug
(or a compromise) in the engine cannot widen the envelope.

No private key or seed phrase ever appears here: `wallet_address` is only used to verify that the signer holds
the expected key and to check its balance.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import time
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class TokenRule(BaseModel):
    """Concrete, address-level rule the signer can enforce without any price feed."""

    model_config = ConfigDict(frozen=True, extra="forbid")
    address: str
    decimals: int
    max_borrow: float = Field(0.0, description="Max flash-loan notional in token units (0 = not allowed to borrow).")


class AuthorizationPolicy(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    enabled: bool = Field(False, description="Master switch. False => read-only / ghost mode only.")
    wallet_address: str = Field("", description="Executor hot wallet (address only).")
    chain_ids: tuple[int, ...] = Field(default=(), description="Networks where live execution is allowed.")
    executor_contract: str = Field("", description="Deployed FlashArbExecutor address (the only allowed tx target).")
    allowed_flash_providers: tuple[str, ...] = ()
    allowed_dexes: tuple[str, ...] = ()
    allowed_tokens: tuple[str, ...] = Field(default=(), description="Token symbols that may be borrowed/traded.")
    tokens: dict[str, TokenRule] = Field(default_factory=dict, description="symbol -> address/decimals/max_borrow (signer-enforced).")

    max_total_budget_native: float = Field(0.0, description="Total gas budget (ETH) over the policy lifetime.")
    max_gas_per_tx_native: float = Field(0.0, description="Max gas spend per transaction (ETH) = gasLimit*maxFee.")
    max_gas_limit: int = Field(1_200_000)
    max_fee_per_gas_gwei: float = Field(0.5)
    max_transactions: int = Field(0, description="Max number of live transactions over the policy lifetime.")
    min_net_profit_native: float = Field(0.0, description="Min expected net profit (ETH equivalent) per trade.")
    max_slippage_bps: int = Field(30)
    max_cumulative_loss_native: float = Field(0.0, description="Stop when realised losses + failed gas exceed this.")
    max_consecutive_failures: int = Field(2)
    min_success_probability: float = Field(0.75)
    max_borrow_usd: float = Field(0.0, description="Cap on the flash-loan notional per trade.")
    valid_from: float = Field(0.0, description="Unix timestamp.")
    valid_until: float = Field(0.0, description="Unix timestamp. 0 => never valid.")
    auto_resume_after_suspension: bool = Field(False)
    submission: Literal["public_rpc", "private_rpc"] = "public_rpc"
    private_rpc_url: str = ""

    @field_validator("wallet_address", "executor_contract")
    @classmethod
    def _addr(cls, v: str) -> str:
        if v and not (v.startswith("0x") and len(v) == 42):
            raise ValueError("must be a 0x-prefixed 20-byte address")
        return v

    # ------------------------------------------------------------------

    def is_valid_now(self, now: float | None = None) -> tuple[bool, str]:
        now = now or time.time()
        if not self.enabled:
            return False, "policy disabled"
        if not self.wallet_address or not self.executor_contract:
            return False, "wallet_address / executor_contract missing"
        if not self.chain_ids:
            return False, "no chain authorised"
        if now < self.valid_from:
            return False, "policy not yet valid"
        if self.valid_until <= now:
            return False, "policy expired"
        if self.max_total_budget_native <= 0 or self.max_transactions <= 0:
            return False, "budget or transaction cap is zero"
        if self.max_gas_per_tx_native <= 0:
            return False, "max_gas_per_tx_native is zero"
        return True, "ok"

    def digest(self) -> str:
        return hashlib.sha256(json.dumps(self.model_dump(), sort_keys=True).encode()).hexdigest()[:16]

    def summary(self) -> dict:
        ok, why = self.is_valid_now()
        return {
            "enabled": self.enabled,
            "valid": ok,
            "reason": why,
            "digest": self.digest(),
            "wallet_address": self.wallet_address,
            "chain_ids": list(self.chain_ids),
            "executor_contract": self.executor_contract,
            "max_total_budget_native": self.max_total_budget_native,
            "max_gas_per_tx_native": self.max_gas_per_tx_native,
            "max_transactions": self.max_transactions,
            "min_net_profit_native": self.min_net_profit_native,
            "max_slippage_bps": self.max_slippage_bps,
            "max_cumulative_loss_native": self.max_cumulative_loss_native,
            "min_success_probability": self.min_success_probability,
            "max_borrow_usd": self.max_borrow_usd,
            "valid_until": self.valid_until,
            "auto_resume_after_suspension": self.auto_resume_after_suspension,
            "submission": self.submission,
        }


def load_policy(path: pathlib.Path | str) -> AuthorizationPolicy:
    p = pathlib.Path(path)
    if not p.exists():
        return AuthorizationPolicy()  # disabled by default
    return AuthorizationPolicy.model_validate(json.loads(p.read_text()))


EXAMPLE = {
    "enabled": False,
    "wallet_address": "0x0000000000000000000000000000000000000000",
    "chain_ids": [8453],
    "executor_contract": "0x0000000000000000000000000000000000000000",
    "allowed_flash_providers": ["MORPHO", "BALANCER_V2", "AAVE_V3"],
    "allowed_dexes": ["uniswap_v3", "aerodrome", "uniswap_v2", "sushiswap_v2", "pancakeswap_v3"],
    "allowed_tokens": ["WETH", "USDC"],
    "tokens": {
        "WETH": {"address": "0x4200000000000000000000000000000000000006", "decimals": 18, "max_borrow": 12.0},
        "USDC": {"address": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", "decimals": 6, "max_borrow": 25000.0},
    },
    "max_total_budget_native": 0.004,
    "max_gas_per_tx_native": 0.0004,
    "max_gas_limit": 900000,
    "max_fee_per_gas_gwei": 0.2,
    "max_transactions": 10,
    "min_net_profit_native": 0.0005,
    "max_slippage_bps": 30,
    "max_cumulative_loss_native": 0.003,
    "max_consecutive_failures": 2,
    "min_success_probability": 0.75,
    "max_borrow_usd": 25000,
    "valid_from": 0,
    "valid_until": 0,
    "auto_resume_after_suspension": False,
    "submission": "public_rpc",
    "private_rpc_url": "",
}
