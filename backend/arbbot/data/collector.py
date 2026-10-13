"""State collector: refreshes pool reserves / V3 state / gas data every block with minimal RPC calls.

Per block:  1 multicall for all V2+Solidly reserves and V3 slot0+liquidity (≈ 2 calls per pool, batched),
            V3 tick words are refreshed every `tick_refresh_blocks` or when the price leaves the fetched window.
New heads:  WebSocket `newHeads` when a WS URL is configured, else HTTP polling of eth_blockNumber.
"""
from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass, field

from ..config.chains import ChainConfig
from ..core.math_v3 import V3PoolState
from ..core.types import DexKind, Pool
from .rpc import RpcClient, decode_result, encode_call

log = logging.getLogger("arbbot.collector")

SIG_RESERVES = encode_call("getReserves()")
SIG_SLOT0 = encode_call("slot0()")
SIG_LIQ = encode_call("liquidity()")


@dataclass
class GasSnapshot:
    block_number: int = 0
    base_fee_wei: int = 0
    priority_fee_wei: int = 0
    gas_price_wei: int = 0  # base + priority (what we'd pay)
    l1_base_fee_wei: int = 0
    ts: float = 0.0

    def as_dict(self) -> dict:
        return {
            "block_number": self.block_number,
            "base_fee_gwei": self.base_fee_wei / 1e9,
            "priority_fee_gwei": self.priority_fee_wei / 1e9,
            "gas_price_gwei": self.gas_price_wei / 1e9,
            "l1_base_fee_gwei": self.l1_base_fee_wei / 1e9,
            "ts": self.ts,
        }


@dataclass
class CollectorStats:
    blocks_seen: int = 0
    refreshes: int = 0
    last_refresh_ms: float = 0.0
    last_block: int = 0
    last_block_ts: float = 0.0
    ws_connected: bool = False
    ws_reconnects: int = 0
    errors: int = 0
    stale_pools: int = 0
    refresh_latencies: list[float] = field(default_factory=list)

    def as_dict(self) -> dict:
        lat = sorted(self.refresh_latencies[-200:])
        return {
            "blocks_seen": self.blocks_seen,
            "refreshes": self.refreshes,
            "last_refresh_ms": round(self.last_refresh_ms, 1),
            "last_block": self.last_block,
            "block_age_s": round(time.time() - self.last_block_ts, 2) if self.last_block_ts else None,
            "ws_connected": self.ws_connected,
            "ws_reconnects": self.ws_reconnects,
            "errors": self.errors,
            "stale_pools": self.stale_pools,
            "refresh_p50_ms": lat[len(lat) // 2] if lat else None,
            "refresh_p95_ms": lat[int(0.95 * (len(lat) - 1))] if lat else None,
        }


class StateCollector:
    def __init__(self, rpc: RpcClient, chain: ChainConfig, pools: list[Pool], *, tick_words_each_side: int = 3,
                 tick_refresh_blocks: int = 10, poll_interval_s: float = 1.0, ws_url: str = ""):
        self.rpc = rpc
        self.chain = chain
        self.pools = pools
        self.tick_words = tick_words_each_side
        self.tick_refresh_blocks = tick_refresh_blocks
        self.poll_interval = poll_interval_s
        self.ws_url = ws_url
        self.gas = GasSnapshot()
        self.stats = CollectorStats()
        self._tick_fetched_block: dict[str, int] = {}
        self._tick_window: dict[str, tuple[int, int]] = {}
        self._subscribers: list[asyncio.Queue] = []
        self._stop = asyncio.Event()
        self.native_price_usd: float | None = None

    # ------------------------------------------------------------------ pub/sub

    def subscribe(self) -> asyncio.Queue:
        q: asyncio.Queue = asyncio.Queue(maxsize=64)
        self._subscribers.append(q)
        return q

    def _publish(self, block: int) -> None:
        for q in self._subscribers:
            if q.full():
                try:
                    q.get_nowait()
                except asyncio.QueueEmpty:
                    pass
            q.put_nowait(block)

    # ------------------------------------------------------------------ main loop

    async def run(self) -> None:
        """Block-driven refresh loop. Never raises; errors are counted and retried."""
        self._stop.clear()
        if self.ws_url:
            asyncio.create_task(self._ws_heads())
        last = 0
        while not self._stop.is_set():
            try:
                bn = await self.rpc.block_number()
                if bn != last:
                    last = bn
                    self.stats.blocks_seen += 1
                    await self.refresh(bn)
                    self._publish(bn)
            except Exception as e:  # noqa: BLE001
                self.stats.errors += 1
                log.warning("collector error: %s", e)
                await asyncio.sleep(min(2.0, self.poll_interval * 2))
            await asyncio.sleep(self.poll_interval if not self.ws_url else self.poll_interval * 3)

    def stop(self) -> None:
        self._stop.set()

    async def _ws_heads(self) -> None:
        """newHeads subscription (optional). On any failure, reconnect with backoff; polling keeps working."""
        try:
            import websockets
        except ImportError:  # pragma: no cover
            return
        backoff = 1.0
        while not self._stop.is_set():
            try:
                async with websockets.connect(self.ws_url, ping_interval=20, max_size=2**22) as ws:
                    self.stats.ws_connected = True
                    backoff = 1.0
                    await ws.send('{"jsonrpc":"2.0","id":1,"method":"eth_subscribe","params":["newHeads"]}')
                    async for raw in ws:
                        if self._stop.is_set():
                            break
                        if b'"number"' in (raw if isinstance(raw, bytes) else raw.encode()):
                            import orjson

                            msg = orjson.loads(raw)
                            head = msg.get("params", {}).get("result", {})
                            if "number" in head:
                                bn = int(head["number"], 16)
                                self.stats.blocks_seen += 1
                                await self.refresh(bn)
                                self._publish(bn)
            except Exception as e:  # noqa: BLE001
                self.stats.ws_connected = False
                self.stats.ws_reconnects += 1
                log.warning("ws disconnected (%s); reconnecting in %.1fs", e, backoff)
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 30.0)

    # ------------------------------------------------------------------ refresh

    async def refresh_pools(self, pools: list[Pool]) -> int:
        """Targeted refresh of a subset (pre-flight): reserves/slot0 + ticks at the latest block."""
        block = await self.rpc.block_number()
        for p in pools:
            self._tick_fetched_block.pop(p.address, None)  # force tick re-fetch for these pools
        return await self.refresh(block, pools)

    async def refresh(self, block: int | None = None, pools: list[Pool] | None = None) -> int:
        t0 = time.perf_counter()
        if block is None:
            block = await self.rpc.block_number()
        subset = pools if pools is not None else self.pools
        calls: list[tuple[str, bytes]] = []
        idx: list[tuple[Pool, str]] = []
        for p in subset:
            if p.kind in (DexKind.UNIV2, DexKind.SOLIDLY):
                calls.append((p.address, SIG_RESERVES))
                idx.append((p, "reserves"))
            else:
                calls.append((p.address, SIG_SLOT0))
                idx.append((p, "slot0"))
                calls.append((p.address, SIG_LIQ))
                idx.append((p, "liquidity"))
        # gas: block header for base fee (one call) — fetched in the same loop iteration
        results, header = await asyncio.gather(self.rpc.multicall(calls, block), self.rpc.get_block(block))
        now = time.time()
        slot_cache: dict[str, tuple[int, int]] = {}
        for (ok, data), (p, what) in zip(results, idx):
            if not ok or not data:
                p.quarantined, p.quarantine_reason = True, f"{what} call failed"
                continue
            if what == "reserves":
                r0, r1 = decode_result(["uint256", "uint256"], data[:64])
                p.reserve0, p.reserve1 = int(r0), int(r1)
                p.updated_block, p.updated_at = block, now
                if p.quarantined and p.quarantine_reason.endswith("call failed"):
                    p.quarantined, p.quarantine_reason = False, ""
            elif what == "slot0":
                sqrt_p, tick = decode_result(["uint160", "int24"], data[:64])
                slot_cache[p.address] = (int(sqrt_p), int(tick))
            elif what == "liquidity":
                (liq,) = decode_result(["uint128"], data[:32])
                sqrt_p, tick = slot_cache.get(p.address, (0, 0))
                if p.v3 is None:
                    p.v3 = V3PoolState(sqrt_p, tick, int(liq), p.fee_ppm, p.tick_spacing or 1)
                else:
                    p.v3.sqrt_price_x96, p.v3.tick, p.v3.liquidity = sqrt_p, tick, int(liq)
                    p.v3.fee_pips = p.fee_ppm
                p.updated_block, p.updated_at = block, now
        await self._refresh_ticks(block, subset)
        self._update_gas(block, header)
        self._update_native_price()
        dt = (time.perf_counter() - t0) * 1000
        if pools is None:
            self.stats.refreshes += 1
            self.stats.last_refresh_ms = dt
            self.stats.refresh_latencies.append(dt)
            if len(self.stats.refresh_latencies) > 1000:
                del self.stats.refresh_latencies[:500]
            self.stats.last_block = block
            self.stats.last_block_ts = int(header["timestamp"], 16) if header and "timestamp" in header else now
            self.stats.stale_pools = sum(1 for p in self.pools if p.updated_block < block)
        return block

    async def _refresh_ticks(self, block: int, subset: list[Pool] | None = None) -> None:
        need: list[Pool] = []
        for p in (subset if subset is not None else self.pools):
            if p.kind not in (DexKind.UNIV3, DexKind.PANCAKE_V3) or p.v3 is None or p.quarantined:
                continue
            last = self._tick_fetched_block.get(p.address, -1)
            win = self._tick_window.get(p.address)
            word = (p.v3.tick // (p.tick_spacing or 1)) >> 8
            out_of_window = win is None or not (win[0] < word < win[1])
            if last < 0 or block - last >= self.tick_refresh_blocks or out_of_window:
                need.append(p)
        if not need:
            return
        # 1) bitmap words
        calls: list[tuple[str, bytes]] = []
        idx: list[tuple[Pool, int]] = []
        for p in need:
            ts = p.tick_spacing or 1
            center = (p.v3.tick // ts) >> 8
            for w in range(center - self.tick_words, center + self.tick_words + 1):
                calls.append((p.address, encode_call("tickBitmap(int16)", [w])))
                idx.append((p, w))
        results = await self.rpc.multicall(calls, block)
        words: dict[str, dict[int, int]] = {p.address: {} for p in need}
        for (ok, data), (p, w) in zip(results, idx):
            if ok and data:
                words[p.address][w] = int.from_bytes(data[:32], "big")
        # 2) initialized ticks within those words
        calls, idx2 = [], []
        for p in need:
            ts = p.tick_spacing or 1
            for w, bits in words[p.address].items():
                b = bits
                while b:
                    low = b & -b
                    bit = low.bit_length() - 1
                    tick = ((w << 8) + bit) * ts
                    calls.append((p.address, encode_call("ticks(int24)", [tick])))
                    idx2.append((p, tick))
                    b ^= low
        results = await self.rpc.multicall(calls, block) if calls else []
        nets: dict[str, dict[int, int]] = {p.address: {} for p in need}
        for (ok, data), (p, tick) in zip(results, idx2):
            if ok and len(data) >= 64:
                _, net = decode_result(["uint128", "int128"], data[:64])
                nets[p.address][tick] = int(net)
        for p in need:
            p.v3.tick_bitmap = words[p.address]
            p.v3.ticks_liquidity_net = nets[p.address]
            center = (p.v3.tick // (p.tick_spacing or 1)) >> 8
            self._tick_window[p.address] = (center - self.tick_words, center + self.tick_words)
            self._tick_fetched_block[p.address] = block

    def _update_gas(self, block: int, header: dict | None) -> None:
        base = int(header.get("baseFeePerGas", "0x0"), 16) if header else 0
        # priority fee: L2 sequencers accept very low tips; use a floor and let the executor bump if needed
        prio = max(int(base * 0.1), 1_000) if base else 1_000_000
        self.gas = GasSnapshot(block, base, prio, base + prio, 0, time.time())

    def _update_native_price(self) -> None:
        """Native (ETH) price in USD from the deepest WETH/stable pool, for display and gas conversion."""
        wn = self.chain.wrapped_native.lower()
        best = None
        for p in self.pools:
            if p.quarantined or not (p.token0.address.lower() == wn or p.token1.address.lower() == wn):
                continue
            other = p.token1 if p.token0.address.lower() == wn else p.token0
            if other.symbol.upper() not in ("USDC", "USDBC", "USDT", "DAI", "USDCE"):
                continue
            x, y = p.liquidity_hint()
            if p.token0.address.lower() == wn:
                weth_raw, stable_raw, sd = x, y, other.decimals
            else:
                weth_raw, stable_raw, sd = y, x, other.decimals
            if weth_raw <= 0:
                continue
            price = (stable_raw / 10**sd) / (weth_raw / 1e18)
            depth = stable_raw / 10**sd
            if best is None or depth > best[1]:
                best = (price, depth)
        if best:
            self.native_price_usd = best[0]

    # ------------------------------------------------------------------ helpers

    def data_age_ms(self, pools: list[Pool]) -> float:
        now = time.time()
        return max((now - p.updated_at) * 1000 for p in pools) if pools else 0.0
