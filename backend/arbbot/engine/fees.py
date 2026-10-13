"""Fee & gas model: every cost that stands between gross spread and money in the wallet.

  flash fee        : provider-specific (Aave FLASHLOAN_PREMIUM_TOTAL read live; Balancer/Morpho 0; UniV3 pool fee)
  swap fees        : already embedded in the exact pool math; reported separately for transparency
  gas              : units(route shape, measured) × (base fee + priority fee) × safety multiplier
  L1 data fee      : OP-stack GasPriceOracle.getL1Fee (Base) / included in Arbitrum's gas estimate
  failure cost     : expected gas burnt by a reverted attempt (reverts are NOT free on L2 sequencers)
  conversion       : native → borrowed token via pool mid prices (flagged when no reference pool exists)
Unknown inputs are reported in `FeeBreakdown.unknowns`; they are never silently replaced by optimistic numbers.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass

from ..config.chains import ChainConfig
from ..config.tunables import TunableParams
from ..core.types import DexKind, FeeBreakdown, FlashSource, Pool, Route, Token
from ..data.collector import GasSnapshot, StateCollector
from ..data.rpc import RpcClient, RpcError, decode_result, encode_call

log = logging.getLogger("arbbot.fees")


@dataclass
class FlashProviderLive:
    source: FlashSource
    address: str
    fee_bps_x100: int  # 1/100 bps: Aave 0.05 % → 500
    capacity: dict[str, int]  # token address (lower) → max borrowable (raw)
    verified: bool = False


class FeeCalculator:
    def __init__(self, rpc: RpcClient, chain: ChainConfig, collector: StateCollector, tunables: TunableParams):
        self.rpc = rpc
        self.chain = chain
        self.collector = collector
        self.t = tunables
        self.providers: dict[FlashSource, FlashProviderLive] = {}
        self.measured_gas: dict[str, list[int]] = {}  # route shape → observed gas used (from sims / receipts)
        self.l1_fee_cache: tuple[int, float] = (0, 0.0)

    # ------------------------------------------------------------------ live provider data

    async def refresh_providers(self, tokens: list[Token]) -> None:
        for cfg in self.chain.flash_providers:
            fee_x100 = int(round(cfg.fee_bps * 100))
            verified = False
            try:
                if cfg.source == FlashSource.AAVE_V3:
                    raw = await self.rpc.call(cfg.address, encode_call("FLASHLOAN_PREMIUM_TOTAL()"))
                    (prem,) = decode_result(["uint128"], raw)  # bps of 1e4 → 5 = 0.05 %
                    fee_x100 = int(prem) * 100
                    verified = True
                elif cfg.source == FlashSource.BALANCER_V2:
                    # ProtocolFeesCollector.getFlashLoanFeePercentage() (1e18 = 100 %). Vault → getProtocolFeesCollector()
                    try:
                        raw = await self.rpc.call(cfg.address, encode_call("getProtocolFeesCollector()"))
                        (pfc,) = decode_result(["address"], raw)
                        raw = await self.rpc.call(pfc, encode_call("getFlashLoanFeePercentage()"))
                        (pct,) = decode_result(["uint256"], raw)
                        fee_x100 = int(pct * 1_000_000 // 10**18)
                        verified = True
                    except RpcError:
                        verified = len(await self.rpc.get_code(cfg.address)) > 0  # devnet mock: fee 0
                elif cfg.source == FlashSource.MORPHO:
                    verified = len(await self.rpc.get_code(cfg.address)) > 0
            except RpcError as e:
                log.warning("provider %s probe failed: %s", cfg.source.name, e)
            capacity: dict[str, int] = {}
            calls = [(t.address, encode_call("balanceOf(address)", [cfg.address])) for t in tokens]
            try:
                res = await self.rpc.multicall(calls)
                for t, (ok, data) in zip(tokens, res):
                    if ok and len(data) >= 32:
                        capacity[t.address.lower()] = int(decode_result(["uint256"], data)[0])
            except RpcError as e:
                log.warning("capacity probe failed for %s: %s", cfg.source.name, e)
            # Aave: liquidity sits in the aToken, not the pool → use getReserveData().aTokenAddress balance
            if cfg.source == FlashSource.AAVE_V3 and verified:
                for t in tokens:
                    try:
                        raw = await self.rpc.call(cfg.address, encode_call("getReserveData(address)", [t.address]))
                        if len(raw) >= 32 * 9:
                            atoken = "0x" + raw[32 * 8 + 12 : 32 * 9].hex()
                            bal = await self.rpc.call(t.address, encode_call("balanceOf(address)", [atoken]))
                            capacity[t.address.lower()] = int(decode_result(["uint256"], bal)[0])
                    except RpcError:
                        pass
            self.providers[cfg.source] = FlashProviderLive(cfg.source, cfg.address, fee_x100, capacity, verified)
        log.info("flash providers: %s", {k.name: (v.fee_bps_x100 / 100, v.verified) for k, v in self.providers.items()})

    def best_provider(self, token: Token, amount: int) -> FlashProviderLive | None:
        """Cheapest verified provider with enough capacity for `amount`."""
        cands = [
            p for p in self.providers.values()
            if p.verified and p.capacity.get(token.address.lower(), 0) >= amount
        ]
        if not cands:
            return None
        return min(cands, key=lambda p: (p.fee_bps_x100, self.t.gas_units_flash.get(p.source.name, 10**9)))

    def provider_capacity(self, token: Token) -> int:
        return max((p.capacity.get(token.address.lower(), 0) for p in self.providers.values() if p.verified), default=0)

    # ------------------------------------------------------------------ gas model

    def shape_key(self, route: Route, source: FlashSource) -> str:
        return source.name + "|" + "+".join(h.pool.kind.name for h in route.hops)

    def gas_units(self, route: Route, source: FlashSource, ticks_crossed: int = 0) -> int:
        key = self.shape_key(route, source)
        obs = self.measured_gas.get(key)
        if obs and len(obs) >= 3:
            obs_sorted = sorted(obs[-50:])
            base = obs_sorted[int(0.8 * (len(obs_sorted) - 1))]  # p80 of observed
        else:
            base = self.t.gas_units_base + self.t.gas_units_flash.get(source.name, 0)
            base += sum(self.t.gas_units_per_hop.get(h.pool.kind.name, 100_000) for h in route.hops)
        base += ticks_crossed * self.t.v3_tick_cross_gas
        return int(base * self.t.gas_safety_multiplier)

    def record_gas(self, route: Route, source: FlashSource, gas_used: int) -> None:
        self.measured_gas.setdefault(self.shape_key(route, source), []).append(int(gas_used))

    async def l1_data_fee(self, calldata_len: int) -> tuple[int, str | None]:
        """OP-stack L1 data fee estimate for a tx with `calldata_len` bytes. Returns (wei, unknown_reason)."""
        if self.chain.l1_fee_model != "opstack":
            return 0, None
        try:
            # getL1FeeUpperBound(unsignedTxSize) exists since Fjord; fall back to getL1Fee(bytes) with zero-ish payload
            try:
                raw = await self.rpc.call(self.chain.opstack_gas_oracle, encode_call("getL1FeeUpperBound(uint256)", [calldata_len + 120]))
                return int(decode_result(["uint256"], raw)[0]), None
            except RpcError:
                payload = b"\x02" + b"\xff" * (calldata_len + 120)
                raw = await self.rpc.call(self.chain.opstack_gas_oracle, encode_call("getL1Fee(bytes)", [payload]))
                return int(decode_result(["uint256"], raw)[0]), None
        except RpcError as e:
            return 0, f"l1 fee oracle unavailable ({e})"

    # ------------------------------------------------------------------ conversions

    def token_price_usd(self, token: Token) -> float | None:
        sym = token.symbol.upper()
        if sym in ("USDC", "USDBC", "USDT", "DAI", "USDCE"):
            return 1.0
        native = self.collector.native_price_usd
        if token.address.lower() == self.chain.wrapped_native.lower():
            return native
        # derive through the deepest pool against WETH or a stable
        best: tuple[float, float] | None = None
        for p in self.collector.pools:
            if p.quarantined or not p.has(token.address):
                continue
            other = p.other(token.address)
            ref = 1.0 if other.symbol.upper() in ("USDC", "USDBC", "USDT", "DAI", "USDCE") else (
                native if other.address.lower() == self.chain.wrapped_native.lower() else None
            )
            if ref is None:
                continue
            x, y = p.liquidity_hint()
            tok_raw, oth_raw = (x, y) if p.is_token0(token.address) else (y, x)
            if tok_raw <= 0:
                continue
            price = (oth_raw / 10**other.decimals) / (tok_raw / 10**token.decimals) * ref
            depth = oth_raw / 10**other.decimals * ref
            if best is None or depth > best[1]:
                best = (price, depth)
        return best[0] if best else None

    def native_to_token(self, wei: int, token: Token) -> tuple[int, float, str | None]:
        """Convert a native amount to token raw units. Returns (raw, native_price_in_token, unknown_reason)."""
        native_usd = self.collector.native_price_usd
        tok_usd = self.token_price_usd(token)
        if not native_usd or not tok_usd:
            return 0, 0.0, "no reference price for native→token conversion"
        per_native = native_usd / tok_usd  # token units per 1 native
        raw = int(wei / 1e18 * per_native * 10**token.decimals)
        return raw, per_native, None

    # ------------------------------------------------------------------ assemble

    async def breakdown(self, route: Route, source: FlashSource, amount_in: int, ticks_crossed: int,
                        swap_fees_token: int, gas: GasSnapshot | None = None) -> FeeBreakdown:
        gas = gas or self.collector.gas
        fb = FeeBreakdown()
        prov = self.providers.get(source)
        from .optimizer import flash_fee_for

        fb.flash_fee = flash_fee_for(amount_in, prov.fee_bps_x100 if prov else 0)
        if prov is None and source != FlashSource.NONE:
            fb.unknowns.append("flash provider not probed")
        fb.swap_fees = swap_fees_token
        fb.gas_units = self.gas_units(route, source, ticks_crossed)
        floor = int(self.t.priority_fee_floor_gwei * 1e9)
        fb.gas_price_wei = gas.base_fee_wei + max(gas.priority_fee_wei, floor)
        calldata_len = 4 + 32 * 8 + 32 * 6 * len(route.hops) + 64
        fb.l1_data_fee_wei, unk = await self.l1_data_fee(calldata_len)
        if unk:
            fb.unknowns.append(unk)
        fb.gas_cost_wei = fb.gas_units * fb.gas_price_wei + fb.l1_data_fee_wei
        fb.failure_cost_wei = int(fb.gas_cost_wei * self.t.failure_gas_fraction)
        token = route.token
        fb.gas_cost_token, fb.native_price_in_token, unk = self.native_to_token(fb.gas_cost_wei, token)
        if unk:
            fb.unknowns.append(unk)
        return fb
