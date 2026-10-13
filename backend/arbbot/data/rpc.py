"""Async JSON-RPC client with rate limiting, retries, fallbacks, latency metrics and Multicall3 batching.

Deliberately thin: raw eth_call / ABI encoding with eth_abi (no web3 contract objects on the hot path).
"""
from __future__ import annotations

import asyncio
import logging
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Sequence

import aiohttp
import orjson
from eth_abi import decode as abi_decode, encode as abi_encode
from eth_utils import keccak, to_checksum_address

log = logging.getLogger("arbbot.rpc")


def selector(signature: str) -> bytes:
    return keccak(text=signature)[:4]


def event_topic(signature: str) -> str:
    """0x-prefixed keccak of an event signature (topic0)."""
    return "0x" + keccak(text=signature).hex()


def encode_call(signature: str, args: Sequence[Any] = ()) -> bytes:
    """signature like 'getReserves()' or 'getPool(address,address,uint24)'."""
    sel = selector(signature)
    types = signature[signature.index("(") + 1 : -1]
    if not types:
        return sel
    return sel + abi_encode(_split_types(types), list(args))


def _split_types(types: str) -> list[str]:
    out, depth, cur = [], 0, ""
    for ch in types:
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        cur += ch
    if cur:
        out.append(cur)
    return out


def decode_result(types: Sequence[str], data: bytes) -> tuple:
    return abi_decode(list(types), data)


class RpcError(Exception):
    def __init__(self, message: str, code: int | None = None, data: Any = None):
        super().__init__(message)
        self.code = code
        self.data = data


class RevertError(RpcError):
    pass


@dataclass
class RpcMetrics:
    requests: int = 0
    errors: int = 0
    retries: int = 0
    latencies_ms: deque = field(default_factory=lambda: deque(maxlen=500))

    def record(self, ms: float) -> None:
        self.requests += 1
        self.latencies_ms.append(ms)

    def summary(self) -> dict:
        lat = sorted(self.latencies_ms)
        pct = lambda p: (lat[min(len(lat) - 1, int(p * len(lat)))] if lat else None)  # noqa: E731
        return {
            "requests": self.requests,
            "errors": self.errors,
            "retries": self.retries,
            "latency_p50_ms": pct(0.5),
            "latency_p95_ms": pct(0.95),
            "latency_max_ms": lat[-1] if lat else None,
            "error_rate": (self.errors / self.requests) if self.requests else 0.0,
        }


class _RateLimiter:
    def __init__(self, rps: float):
        self.rps = max(rps, 0.1)
        self._tokens = self.rps
        self._last = time.monotonic()
        self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        async with self._lock:
            now = time.monotonic()
            self._tokens = min(self.rps, self._tokens + (now - self._last) * self.rps)
            self._last = now
            if self._tokens < 1:
                await asyncio.sleep((1 - self._tokens) / self.rps)
                self._tokens = 0
            else:
                self._tokens -= 1


class RpcClient:
    def __init__(self, url: str, fallbacks: Sequence[str] = (), timeout_s: float = 10.0, max_rps: float = 20.0,
                 multicall3: str = "0xcA11bde05977b3631167028862bE2a173976CA11"):
        self.urls = [url, *fallbacks]
        self._idx = 0
        self.timeout = aiohttp.ClientTimeout(total=timeout_s)
        self.metrics = RpcMetrics()
        self._limiter = _RateLimiter(max_rps)
        self._session: aiohttp.ClientSession | None = None
        self._id = 0
        self.multicall3 = to_checksum_address(multicall3)
        self.chain_id: int | None = None

    @property
    def url(self) -> str:
        return self.urls[self._idx]

    async def __aenter__(self) -> "RpcClient":
        await self.open()
        return self

    async def __aexit__(self, *exc) -> None:
        await self.close()

    async def open(self) -> None:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(timeout=self.timeout, json_serialize=lambda o: orjson.dumps(o).decode())
        if self.chain_id is None:
            self.chain_id = int(await self.request("eth_chainId"), 16)

    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()

    # ------------------------------------------------------------------ core

    async def request(self, method: str, params: list | None = None, retries: int = 3) -> Any:
        if self._session is None or self._session.closed:
            await self.open()
        last_exc: Exception | None = None
        for attempt in range(retries + 1):
            await self._limiter.acquire()
            self._id += 1
            payload = {"jsonrpc": "2.0", "id": self._id, "method": method, "params": params or []}
            t0 = time.perf_counter()
            try:
                async with self._session.post(self.url, data=orjson.dumps(payload),
                                              headers={"content-type": "application/json"}) as resp:
                    body = await resp.read()
                self.metrics.record((time.perf_counter() - t0) * 1000)
                if resp.status >= 500 or resp.status == 429:
                    raise RpcError(f"http {resp.status}", code=resp.status)
                msg = orjson.loads(body)
                if "error" in msg:
                    err = msg["error"]
                    text = str(err.get("message", ""))
                    if "revert" in text.lower() or err.get("code") == 3:
                        raise RevertError(text, code=err.get("code"), data=err.get("data"))
                    raise RpcError(text, code=err.get("code"), data=err.get("data"))
                return msg.get("result")
            except RevertError:
                raise
            except (aiohttp.ClientError, asyncio.TimeoutError, RpcError, orjson.JSONDecodeError) as e:
                last_exc = e
                self.metrics.errors += 1
                if attempt < retries:
                    self.metrics.retries += 1
                    if len(self.urls) > 1:
                        self._idx = (self._idx + 1) % len(self.urls)
                        log.warning("rpc error (%s) → switching to %s", e, self.url)
                    await asyncio.sleep(min(0.25 * 2**attempt, 2.0))
        raise RpcError(f"rpc failed after retries: {last_exc}") from last_exc

    async def batch(self, calls: list[tuple[str, list]]) -> list[Any]:
        """JSON-RPC batch (one HTTP round-trip). Falls back to sequential if the provider rejects batches."""
        if not calls:
            return []
        if self._session is None or self._session.closed:
            await self.open()
        await self._limiter.acquire()
        payload = []
        for method, params in calls:
            self._id += 1
            payload.append({"jsonrpc": "2.0", "id": self._id, "method": method, "params": params})
        t0 = time.perf_counter()
        try:
            async with self._session.post(self.url, data=orjson.dumps(payload),
                                          headers={"content-type": "application/json"}) as resp:
                body = await resp.read()
            self.metrics.record((time.perf_counter() - t0) * 1000)
            msgs = orjson.loads(body)
            if not isinstance(msgs, list):
                raise RpcError("batch not supported")
            by_id = {m["id"]: m for m in msgs}
            out = []
            for p in payload:
                m = by_id.get(p["id"], {})
                out.append(m.get("result") if "error" not in m else RpcError(str(m["error"].get("message"))))
            return out
        except (aiohttp.ClientError, asyncio.TimeoutError, RpcError, orjson.JSONDecodeError):
            self.metrics.errors += 1
            return [await self._safe(method, params) for method, params in calls]

    async def _safe(self, method: str, params: list) -> Any:
        try:
            return await self.request(method, params)
        except RpcError as e:
            return e

    # ------------------------------------------------------------------ helpers

    async def block_number(self) -> int:
        return int(await self.request("eth_blockNumber"), 16)

    async def get_block(self, tag: str | int = "latest", full: bool = False) -> dict:
        t = hex(tag) if isinstance(tag, int) else tag
        return await self.request("eth_getBlockByNumber", [t, full])

    async def gas_price(self) -> int:
        return int(await self.request("eth_gasPrice"), 16)

    async def fee_history(self, blocks: int = 10, percentiles: list[int] | None = None) -> dict:
        return await self.request("eth_feeHistory", [hex(blocks), "latest", percentiles or [25, 50, 75]])

    async def get_code(self, address: str) -> bytes:
        return bytes.fromhex((await self.request("eth_getCode", [address, "latest"]))[2:])

    async def get_balance(self, address: str) -> int:
        return int(await self.request("eth_getBalance", [address, "latest"]), 16)

    async def nonce(self, address: str, tag: str = "pending") -> int:
        return int(await self.request("eth_getTransactionCount", [address, tag]), 16)

    async def call(self, to: str, data: bytes, block: str | int = "latest", sender: str | None = None,
                   overrides: dict | None = None, gas: int | None = None) -> bytes:
        tx: dict[str, Any] = {"to": to, "data": "0x" + data.hex()}
        if sender:
            tx["from"] = sender
        if gas:
            tx["gas"] = hex(gas)
        params: list[Any] = [tx, hex(block) if isinstance(block, int) else block]
        if overrides:
            params.append(overrides)
        res = await self.request("eth_call", params)
        return bytes.fromhex(res[2:]) if res else b""

    async def estimate_gas(self, tx: dict) -> int:
        return int(await self.request("eth_estimateGas", [tx]), 16)

    async def send_raw(self, raw: bytes | str) -> str:
        hexraw = raw if isinstance(raw, str) else "0x" + raw.hex()
        return await self.request("eth_sendRawTransaction", [hexraw])

    async def receipt(self, tx_hash: str) -> dict | None:
        return await self.request("eth_getTransactionReceipt", [tx_hash])

    async def wait_receipt(self, tx_hash: str, timeout: float = 90.0, poll: float = 0.5) -> dict | None:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            r = await self.receipt(tx_hash)
            if r is not None:
                return r
            await asyncio.sleep(poll)
        return None

    async def get_nonce(self, address: str, tag: str = "pending") -> int:
        return await self.nonce(address, tag)

    async def get_logs(self, params: dict) -> list[dict]:
        return await self.request("eth_getLogs", [params])

    async def multicall(self, calls: Sequence[tuple[str, bytes]], block: str | int = "latest",
                        chunk: int = 300) -> list[tuple[bool, bytes]]:
        """Multicall3.aggregate3 with allowFailure=true. Returns [(success, returndata), ...] in order."""
        if not calls:
            return []

        async def one(part: Sequence[tuple[str, bytes]]) -> list[tuple[bool, bytes]]:
            data = encode_call("aggregate3((address,bool,bytes)[])", [[(to_checksum_address(t), True, d) for t, d in part]])
            raw = await self.call(self.multicall3, data, block)
            (results,) = decode_result(["(bool,bytes)[]"], raw)
            return [(bool(s), bytes(r)) for s, r in results]

        parts = [calls[i : i + chunk] for i in range(0, len(calls), chunk)]
        if len(parts) == 1:
            return await one(parts[0])
        # chunks run concurrently (bounded by the client-side rate limiter) — on a public RPC with 2 s blocks the
        # per-block refresh must not serialise several hundred-millisecond round trips
        out: list[tuple[bool, bytes]] = []
        for res in await asyncio.gather(*(one(p) for p in parts)):
            out.extend(res)
        return out
