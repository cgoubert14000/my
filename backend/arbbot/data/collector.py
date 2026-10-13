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
from .rpc import RpcError, RpcClient, decode_result, encode_call, event_topic

log = logging.getLogger("arbbot.collector")

SIG_RESERVES = encode_call("getReserves()")
SIG_SLOT0 = encode_call("slot0()")

# Event feed (WebSocket `logs` subscription): the pool state is updated the instant a swap is included, instead of
# after the next multicall refresh — on a public RPC that refresh costs 0.3–4 s, i.e. most of a 2 s Base block.
TOPIC_SYNC_V2 = event_topic("Sync(uint112,uint112)")  # Uniswap V2 / Sushi V2 / Pancake V2
TOPIC_SYNC_SOLIDLY = event_topic("Sync(uint256,uint256)")  # Aerodrome (Solidly) pools
TOPIC_SWAP_V3 = event_topic("Swap(address,address,int256,int256,uint160,uint128,int24)")  # Uniswap V3, Sushi V3, Slipstream
TOPIC_SWAP_PANCAKE_V3 = event_topic("Swap(address,address,int256,int256,uint160,uint128,int24,uint128,uint128)")
TOPIC_MINT_V3 = event_topic("Mint(address,address,int24,int24,uint128,uint256,uint256)")
TOPIC_BURN_V3 = event_topic("Burn(address,int24,int24,uint128,uint256,uint256)")
EVENT_TOPICS = (TOPIC_SYNC_V2, TOPIC_SYNC_SOLIDLY, TOPIC_SWAP_V3, TOPIC_SWAP_PANCAKE_V3, TOPIC_MINT_V3, TOPIC_BURN_V3)


def _int24(word: bytes) -> int:
    v = int.from_bytes(word, "big")
    return v - (1 << 256) if v >> 255 else v


SIG_LIQ = encode_call("liquidity()")
SIG_FEE = encode_call("fee()")
MULTICALL_CHUNK = 800  # calls per aggregate3 request: ~3-4 M gas and <100 KB of return data — fine on public RPCs
FEE_RECHECK_BLOCKS = 300  # immutable V3 fee tiers are still re-read now and then (cheap safety net)


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
    fee_changes: int = 0  # dynamic LP fee changes observed (Slipstream fee modules)
    events_applied: int = 0  # swap/sync logs applied to the pool state before the block refresh
    events_ignored: int = 0  # logs for pools we do not watch, stale or malformed
    events_lead_ms: list[float] = field(default_factory=list)  # how long before the multicall refresh the event arrived
    last_event_at: float = 0.0
    refresh_latencies: list[float] = field(default_factory=list)

    def as_dict(self) -> dict:
        lat = sorted(self.refresh_latencies[-200:])
        return {
            "blocks_seen": self.blocks_seen,
            "refreshes": self.refreshes,
            "last_refresh_ms": round(self.last_refresh_ms, 1),
            "last_block": self.last_block,
            "block_age_s": round(time.time() - self.last_block_ts, 2) if self.last_block_ts else None,
            "last_block_ts": self.last_block_ts or None,
            "ws_connected": self.ws_connected,
            "ws_reconnects": self.ws_reconnects,
            "errors": self.errors,
            "stale_pools": self.stale_pools,
            "fee_changes": self.fee_changes,
            "refresh_p50_ms": lat[len(lat) // 2] if lat else None,
            "refresh_p95_ms": lat[int(0.95 * (len(lat) - 1))] if lat else None,
            "events_applied": self.events_applied,
            "events_ignored": self.events_ignored,
            "event_lead_p50_ms": (sorted(self.events_lead_ms[-200:])[len(self.events_lead_ms[-200:]) // 2] if self.events_lead_ms else None),
            "last_event_age_s": round(time.time() - self.last_event_at, 1) if self.last_event_at else None,
        }


class StateCollector:
    def __init__(self, rpc: RpcClient, chain: ChainConfig, pools: list[Pool], *, tick_words_each_side: int = 3,
                 tick_refresh_blocks: int = 10, poll_interval_s: float = 1.0, ws_url: str = ""):
        self.rpc = rpc
        self.chain = chain
        self.pools = pools
        self.tick_words = tick_words_each_side
        self.tick_refresh_blocks = tick_refresh_blocks
        self.balance_refresh_blocks = 30
        self._dynamic_fee_dexes = {d.id for d in chain.dexes if getattr(d, "dynamic_fee", False)}
        self.poll_interval = poll_interval_s
        self.ws_url = ws_url
        self.gas = GasSnapshot()
        self.stats = CollectorStats()
        self._tick_fetched_block: dict[str, int] = {}
        self._tick_window: dict[str, tuple[int, int]] = {}
        self._subscribers: list[asyncio.Queue] = []
        self._stop = asyncio.Event()
        self._last_head = 0
        self._by_addr: dict[str, Pool] = {p.address.lower(): p for p in pools}
        self._force_tick_refresh: set[str] = set()
        self._event_block_seen: dict[str, int] = {}  # pool → block of the last applied event (lead-time measurement)
        self.subscribe_logs = True  # second subscription on the same WebSocket (needs ws_url)
        self.on_pool_event = None  # callback(pool, block) set by the runtime → immediate scan
        self._head_lock = asyncio.Lock()
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
        while not self._stop.is_set():
            try:
                bn = await self.rpc.block_number()
                await self._on_head(bn)
            except Exception as e:  # noqa: BLE001
                self.stats.errors += 1
                log.warning("collector error: %s", e)
                await asyncio.sleep(min(2.0, self.poll_interval * 2))
            await asyncio.sleep(self.poll_interval if not self.ws_url else self.poll_interval * 3)

    def stop(self) -> None:
        self._stop.set()

    async def _on_head(self, bn: int) -> bool:
        """Refresh once per new head, whichever source (WebSocket newHeads or polling) sees it first."""
        if bn <= self._last_head:
            return False
        async with self._head_lock:
            if bn <= self._last_head:
                return False
            self._last_head = bn
            self.stats.blocks_seen += 1
            await self.refresh(bn)
            self._publish(bn)
            return True

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
                    if self.subscribe_logs:
                        import orjson

                        # topics-only filter (an address list of 1 500 pools exceeds most providers' limits); the
                        # pools we do not watch are dropped locally in apply_log
                        await ws.send(orjson.dumps({"jsonrpc": "2.0", "id": 2, "method": "eth_subscribe",
                                                    "params": ["logs", {"topics": [list(EVENT_TOPICS)]}]}))
                    async for raw in ws:
                        if self._stop.is_set():
                            break
                        buf = raw if isinstance(raw, bytes) else raw.encode()
                        if b'"topics"' in buf:
                            import orjson

                            msg = orjson.loads(raw)
                            lg = msg.get("params", {}).get("result")
                            if isinstance(lg, dict):
                                self.apply_log(lg)
                        elif b'"number"' in buf:
                            import orjson

                            msg = orjson.loads(raw)
                            head = msg.get("params", {}).get("result", {})
                            if "number" in head:
                                await self._on_head(int(head["number"], 16))
            except Exception as e:  # noqa: BLE001
                self.stats.ws_connected = False
                self.stats.ws_reconnects += 1
                log.warning("ws disconnected (%s); reconnecting in %.1fs", e, backoff)
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 30.0)

    # ------------------------------------------------------------------ event feed

    def apply_log(self, lg: dict) -> Pool | None:
        """Apply one `logs` entry to the watched pool it belongs to; returns the pool when its state changed.
        Swap (CL pools) carries the complete post-swap state (sqrtPrice, liquidity, tick); Sync (V2/Solidly) carries
        the reserves. Mint/Burn only flag the pool for a tick re-fetch at the next refresh. Logs older than the pool's
        last refresh block, reorged (`removed`) logs and logs of unknown pools are ignored."""
        try:
            p = self._by_addr.get(str(lg.get("address", "")).lower())
            if p is None:
                self.stats.events_ignored += 1
                return None
            topics = lg.get("topics") or []
            t0 = str(topics[0]).lower() if topics else ""
            block = int(lg.get("blockNumber", "0x0"), 16)
            if lg.get("removed"):
                self._tick_fetched_block.pop(p.address, None)
                self._force_tick_refresh.add(p.address)
                self.stats.events_ignored += 1
                return None
            if block < p.updated_block:
                self.stats.events_ignored += 1
                return None
            data = bytes.fromhex(str(lg.get("data", "0x"))[2:])
            now = time.time()
            if t0 in (TOPIC_SYNC_V2, TOPIC_SYNC_SOLIDLY) and p.kind in (DexKind.UNIV2, DexKind.SOLIDLY) and len(data) >= 64:
                p.reserve0, p.reserve1 = int.from_bytes(data[:32], "big"), int.from_bytes(data[32:64], "big")
            elif t0 in (TOPIC_SWAP_V3, TOPIC_SWAP_PANCAKE_V3) and p.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3) and len(data) >= 160:
                sqrt_p = int.from_bytes(data[64:96], "big")
                liq = int.from_bytes(data[96:128], "big")
                tick = _int24(data[128:160])
                if sqrt_p == 0:
                    self.stats.events_ignored += 1
                    return None
                if p.v3 is None:
                    p.v3 = V3PoolState(sqrt_p, tick, liq, p.fee_ppm, p.tick_spacing or 1)
                else:
                    p.v3.sqrt_price_x96, p.v3.tick, p.v3.liquidity = sqrt_p, tick, liq
            elif t0 in (TOPIC_MINT_V3, TOPIC_BURN_V3) and p.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3):
                self._force_tick_refresh.add(p.address)  # liquidity_net of the touched ticks changed
                self.stats.events_ignored += 1
                return None
            else:
                self.stats.events_ignored += 1
                return None
            p.updated_block, p.updated_at = block, now
            self._event_block_seen[p.address] = block
            self.stats.events_applied += 1
            self.stats.last_event_at = now
            if self.on_pool_event is not None:
                try:
                    self.on_pool_event(p, block)
                except Exception as e:  # noqa: BLE001 - never let the engine callback break the feed
                    log.warning("on_pool_event failed: %s", e)
            return p
        except (ValueError, TypeError, IndexError) as e:
            self.stats.events_ignored += 1
            log.debug("malformed log ignored: %s", e)
            return None

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
        dynamic = self._dynamic_fee_dexes
        recheck_fees = block % FEE_RECHECK_BLOCKS == 0
        for p in subset:
            if p.kind in (DexKind.UNIV2, DexKind.SOLIDLY):
                calls.append((p.address, SIG_RESERVES))
                idx.append((p, "reserves"))
            else:
                calls.append((p.address, SIG_SLOT0))
                idx.append((p, "slot0"))
                calls.append((p.address, SIG_LIQ))
                idx.append((p, "liquidity"))
                if p.dex in dynamic or recheck_fees:
                    calls.append((p.address, SIG_FEE))
                    idx.append((p, "fee"))
        # gas: block header for base fee (one call) — fetched in the same loop iteration
        t_req = time.time()
        results, header = await asyncio.gather(self.rpc.multicall(calls, block, chunk=MULTICALL_CHUNK), self.rpc.get_block(block))
        now = time.time()
        if pools is None and self._event_block_seen:
            # pools whose swap event for this very block was applied before this refresh completed: the event feed
            # led the multicall by (now - updated_at)
            leads = [(now - p.updated_at) * 1000 for p in subset if self._event_block_seen.get(p.address) == block and p.updated_at <= now]
            if leads:
                self.stats.events_lead_ms.extend(leads[:50])
                if len(self.stats.events_lead_ms) > 1000:
                    del self.stats.events_lead_ms[:500]
            del t_req
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
            elif what == "fee":
                (fee,) = decode_result(["uint24"], data[:32])
                fee = int(fee)
                if 0 < fee < 1_000_000 and fee != p.fee_ppm:
                    log.info("pool %s (%s) fee changed %d → %d ppm", p.address, p.dex, p.fee_ppm, fee)
                    self.stats.fee_changes += 1
                    p.fee_ppm = fee
                    if p.v3 is not None:
                        p.v3.fee_pips = fee
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
        await self._refresh_balances(block, subset)
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
        n_stagger = max(1, self.tick_refresh_blocks)
        for i, p in enumerate(subset if subset is not None else self.pools):
            if p.kind not in (DexKind.UNIV3, DexKind.PANCAKE_V3) or p.v3 is None or p.quarantined:
                continue
            last = self._tick_fetched_block.get(p.address, -1)
            win = self._tick_window.get(p.address)
            word = (p.v3.tick // (p.tick_spacing or 1)) >> 8
            out_of_window = win is None or not (win[0] < word < win[1])
            # periodic refresh is staggered (pool i every N + i mod N blocks) so that only a fraction of the concentrated
            # pools is re-fetched per block instead of all of them every N blocks (which stalled the collector for
            # seconds on a rate-limited public RPC — real-market session 38425105547, refresh p95 3.9 s). A price move
            # out of the fetched window still triggers an immediate re-fetch.
            due = block - last >= n_stagger + (0 if subset is not None else i % n_stagger)
            if last < 0 or due or out_of_window or p.address in self._force_tick_refresh:
                need.append(p)
        self._force_tick_refresh.difference_update(p.address for p in need)
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
        results = await self.rpc.multicall(calls, block, chunk=MULTICALL_CHUNK)
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
        results = await self.rpc.multicall(calls, block, chunk=MULTICALL_CHUNK) if calls else []
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

    async def _refresh_balances(self, block: int, subset: list[Pool] | None = None) -> None:
        """Real ERC-20 balances held by each pool (TVL), every `balance_refresh_blocks` — virtual reserves of
        concentrated pools are useless as a depth/TVL measure."""
        need = [p for p in (subset if subset is not None else self.pools)
                if not p.quarantined and (not p.balances_block or block - p.balances_block >= self.balance_refresh_blocks)]
        if not need:
            return
        calls: list[tuple[str, bytes]] = []
        for p in need:
            calls.append((p.token0.address, encode_call("balanceOf(address)", [p.address])))
            calls.append((p.token1.address, encode_call("balanceOf(address)", [p.address])))
        try:
            results = await self.rpc.multicall(calls, block, chunk=MULTICALL_CHUNK)
        except RpcError as e:
            log.warning("balance refresh failed: %s", e)
            return
        for i, p in enumerate(need):
            ok0, d0 = results[2 * i]
            ok1, d1 = results[2 * i + 1]
            if ok0 and ok1 and len(d0) >= 32 and len(d1) >= 32:
                p.balance0, p.balance1 = int.from_bytes(d0[:32], "big"), int.from_bytes(d1[:32], "big")
                p.balances_block = block

    def _update_gas(self, block: int, header: dict | None) -> None:
        base = int(header.get("baseFeePerGas", "0x0"), 16) if header else 0
        # priority fee: L2 sequencers accept very low tips; use a floor and let the executor bump if needed
        prio = max(int(base * 0.1), 1_000) if base else 1_000_000
        self.gas = GasSnapshot(block, base, prio, base + prio, 0, time.time())

    def _update_native_price(self) -> None:
        """Native (ETH) price in USD from the deepest WETH/stable pool, for display and gas conversion."""
        wn = self.chain.wrapped_native.lower()
        stables = self.chain.stable_addresses() if hasattr(self.chain, "stable_addresses") else set()
        best = None
        for p in self.pools:
            if p.quarantined or not (p.token0.address.lower() == wn or p.token1.address.lower() == wn):
                continue
            other = p.token1 if p.token0.address.lower() == wn else p.token0
            if other.address.lower() not in stables:  # verified stable addresses only (never by symbol)
                continue
            x, y = p.liquidity_hint()  # price = ratio of (virtual) reserves at the current tick
            bx, by = p.depth_tokens()  # depth = what the pool really holds
            if p.token0.address.lower() == wn:
                weth_raw, stable_raw, sd, depth_raw = x, y, other.decimals, by
            else:
                weth_raw, stable_raw, sd, depth_raw = y, x, other.decimals, bx
            if weth_raw <= 0:
                continue
            price = (stable_raw / 10**sd) / (weth_raw / 1e18)
            depth = depth_raw / 10**sd
            if best is None or depth > best[1]:
                best = (price, depth)
        if best:
            self.native_price_usd = best[0]

    # ------------------------------------------------------------------ helpers

    def data_age_ms(self, pools: list[Pool]) -> float:
        now = time.time()
        return max((now - p.updated_at) * 1000 for p in pools) if pools else 0.0
