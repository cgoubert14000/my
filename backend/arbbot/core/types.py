"""Core domain types shared by every module. Pure data, no I/O."""
from __future__ import annotations

import time
from dataclasses import dataclass, field, asdict
from enum import Enum, IntEnum
from typing import Any

from .math_v3 import V3PoolState
from .math_solidly import SolidlyPoolState


class DexKind(IntEnum):
    """Must match FlashArbExecutor.DexKind ordering."""

    UNIV2 = 0
    UNIV3 = 1
    SOLIDLY = 2
    PANCAKE_V3 = 3


class FlashSource(IntEnum):
    """Must match FlashArbExecutor.FlashSource ordering."""

    NONE = 0
    BALANCER_V2 = 1
    AAVE_V3 = 2
    MORPHO = 3
    UNISWAP_V3 = 4


@dataclass(frozen=True)
class Token:
    address: str
    symbol: str
    decimals: int

    def to_units(self, raw: int) -> float:
        return raw / 10**self.decimals

    def from_units(self, amount: float) -> int:
        return int(amount * 10**self.decimals)


@dataclass
class Pool:
    address: str
    dex: str  # human dex id: "uniswap_v3", "aerodrome", ...
    kind: DexKind
    token0: Token
    token1: Token
    fee_ppm: int  # V2: LP fee ppm; V3: fee pips (same unit); Solidly: fee_bps*100
    stable: bool = False  # Solidly only
    tick_spacing: int = 0  # V3 only
    # Live state (refreshed by the collector)
    reserve0: int = 0
    reserve1: int = 0
    v3: V3PoolState | None = None
    updated_block: int = 0
    updated_at: float = 0.0
    quarantined: bool = False
    quarantine_reason: str = ""

    def other(self, token: str) -> Token:
        return self.token1 if token.lower() == self.token0.address.lower() else self.token0

    def has(self, token: str) -> bool:
        t = token.lower()
        return t == self.token0.address.lower() or t == self.token1.address.lower()

    def is_token0(self, token: str) -> bool:
        return token.lower() == self.token0.address.lower()

    def solidly_state(self) -> SolidlyPoolState:
        return SolidlyPoolState(
            self.reserve0, self.reserve1, 10**self.token0.decimals, 10**self.token1.decimals, self.stable, self.fee_ppm // 100
        )

    def liquidity_hint(self) -> tuple[int, int]:
        """Approximate (token0, token1) depth usable for sanity bounds."""
        if self.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3) and self.v3:
            # virtual reserves at current price: x = L / sqrtP, y = L * sqrtP
            from .math_v3 import Q96

            if self.v3.sqrt_price_x96 == 0:
                return 0, 0
            x = (self.v3.liquidity * Q96) // self.v3.sqrt_price_x96
            y = (self.v3.liquidity * self.v3.sqrt_price_x96) // Q96
            return x, y
        return self.reserve0, self.reserve1

    def short(self) -> str:
        return f"{self.dex}:{self.token0.symbol}/{self.token1.symbol}@{self.address[:8]}"


@dataclass
class Hop:
    pool: Pool
    token_in: Token
    token_out: Token

    def to_contract_tuple(self, min_amount_out: int = 0) -> tuple:
        return (
            int(self.pool.kind),
            self.pool.address,
            self.token_in.address,
            self.token_out.address,
            self.pool.fee_ppm if self.pool.kind == DexKind.UNIV2 else 0,
            min_amount_out,
        )


@dataclass
class Route:
    hops: list[Hop]

    @property
    def token(self) -> Token:
        return self.hops[0].token_in

    @property
    def key(self) -> str:
        return ">".join(f"{h.pool.address.lower()}:{h.token_in.symbol}" for h in self.hops)

    def describe(self) -> str:
        parts = [self.hops[0].token_in.symbol]
        for h in self.hops:
            parts.append(f"→[{h.pool.dex}]→{h.token_out.symbol}")
        return "".join(parts)

    @property
    def dexes(self) -> list[str]:
        return [h.pool.dex for h in self.hops]

    @property
    def pools(self) -> list[str]:
        return [h.pool.address for h in self.hops]


class Decision(str, Enum):
    CANDIDATE = "CANDIDATE"
    REJECTED = "REJECTED"
    ELIGIBLE = "ELIGIBLE"
    SELECTED = "SELECTED"
    EXECUTED = "EXECUTED"
    FAILED = "FAILED"


@dataclass
class FeeBreakdown:
    """All amounts in raw units of the borrowed token unless suffixed."""

    flash_fee: int = 0
    swap_fees: int = 0  # sum of LP fees across hops (informational: already included in outputs)
    gas_units: int = 0
    gas_price_wei: int = 0  # effective gas price (base + priority)
    l1_data_fee_wei: int = 0
    l1_data_fee_wei: int = 0  # OP-stack L1 data fee (0 when not applicable)
    gas_cost_wei: int = 0  # gas_units * gas_price + l1 fee
    gas_cost_token: int = 0  # converted into borrowed token
    native_price_in_token: float = 0.0  # token units per 1 native
    failure_cost_wei: int = 0  # expected cost of a reverted attempt
    unknowns: list[str] = field(default_factory=list)


@dataclass
class ProfitBreakdown:
    amount_in: int
    amount_out: int
    gross_profit: int  # amount_out - amount_in (before flash fee & gas)
    expected_net: int  # gross - flash fee - gas (token units)
    simulated_net: int | None = None  # from eth_call (None = not simulated)
    realized_net: int | None = None  # from receipt (None = not executed)
    expected_net_eur: float | None = None
    fees: FeeBreakdown = field(default_factory=FeeBreakdown)
    margin_bps: float = 0.0  # expected_net / amount_in in bps
    price_impact_bps: float = 0.0


@dataclass
class Opportunity:
    id: str
    ts: float
    chain_id: int
    block_number: int
    route: Route
    flash_source: FlashSource
    flash_provider: str
    profit: ProfitBreakdown
    spread_bps: float
    decision: Decision = Decision.CANDIDATE
    reasons: list[str] = field(default_factory=list)
    p_success: float | None = None  # calibrated probability of positive net profit
    p_lower: float | None = None  # conservative lower bound
    p_upper: float | None = None
    p_n: int = 0  # observations behind the estimate
    uncertainty: str = "UNKNOWN"
    ev: float = 0.0  # expected value used for ranking (token units)
    features: dict[str, Any] = field(default_factory=dict)
    sim: dict[str, Any] | None = None  # last simulation result (ok, profit, error, gas_estimate, mode, block, latency_ms)
    sim_ok: bool | None = None
    sim_error: str | None = None
    sim_gas_used: int | None = None
    data_age_ms: float = 0.0
    ghost_next_block_net: int | None = None  # ghost: net profit re-simulated at the landing block
    tx_hash: str | None = None

    def to_record(self) -> dict[str, Any]:
        d = {
            "id": self.id,
            "ts": self.ts,
            "chain_id": self.chain_id,
            "block_number": self.block_number,
            "route": self.route.describe(),
            "route_key": self.route.key,
            "dexes": self.route.dexes,
            "pools": self.route.pools,
            "token": self.route.token.symbol,
            "token_address": self.route.token.address,
            "token_decimals": self.route.token.decimals,
            "flash_source": self.flash_source.name,
            "flash_provider": self.flash_provider,
            "amount_in": self.profit.amount_in,
            "amount_out": self.profit.amount_out,
            "gross_profit": self.profit.gross_profit,
            "expected_net": self.profit.expected_net,
            "simulated_net": self.profit.simulated_net,
            "realized_net": self.profit.realized_net,
            "expected_net_eur": self.profit.expected_net_eur,
            "margin_bps": self.profit.margin_bps,
            "price_impact_bps": self.profit.price_impact_bps,
            "spread_bps": self.spread_bps,
            "fees": asdict(self.profit.fees),
            "decision": self.decision.value,
            "reasons": self.reasons,
            "p_success": self.p_success,
            "p_lower": self.p_lower,
            "p_upper": self.p_upper,
            "p_n": self.p_n,
            "ev": self.ev,
            "features": self.features,
            "sim": self.sim,
            "uncertainty": self.uncertainty,
            "sim_ok": self.sim_ok,
            "sim_error": self.sim_error,
            "sim_gas_used": self.sim_gas_used,
            "data_age_ms": self.data_age_ms,
            "ghost_next_block_net": self.ghost_next_block_net,
            "tx_hash": self.tx_hash,
        }
        return d


def now() -> float:
    return time.time()
