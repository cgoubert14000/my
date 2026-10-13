"""Devnet market simulator — generates realistic-looking order flow on the local anvil DEX universe.

  * background noise : small random trades on random pools (log-normal size, 0.05–1 % of depth)
  * shocks           : occasional large one-sided trades (2–8 % of depth) that open cross-pool spreads
  * competitors      : with some probability per block, an "other arbitrageur" trades against the widest gap and
                       closes most of it — so opportunities are transient, as on a real chain
  * gas              : base fee pinned around a Base-like level (default 0.01 gwei, noisy)

This is LOCAL DEVNET ACTIVITY ONLY — nothing here is real market data. The UI shows a "devnet" badge whenever
the backend is connected to chain id 31337.

Usage:  python devnet/market_sim.py [--rate 1.0] [--shock-every 25] [--competitor 0.6] [--base-fee-gwei 0.01]
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import random
import sys
import time

from eth_account import Account
from web3 import Web3

ROOT = pathlib.Path(__file__).resolve().parent
MAKER_KEY = "0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a"  # public anvil account #2
ERC20_ABI = json.loads(
    '[{"name":"balanceOf","type":"function","stateMutability":"view","inputs":[{"name":"a","type":"address"}],"outputs":[{"type":"uint256"}]},'
    '{"name":"transfer","type":"function","stateMutability":"nonpayable","inputs":[{"name":"to","type":"address"},{"name":"v","type":"uint256"}],"outputs":[{"type":"bool"}]},'
    '{"name":"decimals","type":"function","stateMutability":"view","inputs":[],"outputs":[{"type":"uint8"}]}]'
)
V2_ABI = json.loads(
    '[{"name":"getReserves","type":"function","stateMutability":"view","inputs":[],"outputs":[{"type":"uint112"},{"type":"uint112"},{"type":"uint32"}]},'
    '{"name":"swap","type":"function","stateMutability":"nonpayable","inputs":[{"name":"a0","type":"uint256"},{"name":"a1","type":"uint256"},{"name":"to","type":"address"},{"name":"d","type":"bytes"}],"outputs":[]}]'
)
SOL_ABI = json.loads(
    '[{"name":"getReserves","type":"function","stateMutability":"view","inputs":[],"outputs":[{"type":"uint256"},{"type":"uint256"},{"type":"uint256"}]},'
    '{"name":"getAmountOut","type":"function","stateMutability":"view","inputs":[{"name":"a","type":"uint256"},{"name":"t","type":"address"}],"outputs":[{"type":"uint256"}]},'
    '{"name":"swap","type":"function","stateMutability":"nonpayable","inputs":[{"name":"a0","type":"uint256"},{"name":"a1","type":"uint256"},{"name":"to","type":"address"},{"name":"d","type":"bytes"}],"outputs":[]}]'
)
V3_ABI = json.loads(
    '[{"name":"slot0","type":"function","stateMutability":"view","inputs":[],"outputs":[{"type":"uint160"},{"type":"int24"},{"type":"uint16"},{"type":"uint16"},{"type":"uint16"},{"type":"uint8"},{"type":"bool"}]},'
    '{"name":"liquidity","type":"function","stateMutability":"view","inputs":[],"outputs":[{"type":"uint128"}]}]'
)
HELPER_ABI = json.loads(
    '[{"name":"swapExactIn","type":"function","stateMutability":"nonpayable","inputs":[{"name":"pool","type":"address"},{"name":"zeroForOne","type":"bool"},{"name":"amountIn","type":"uint256"}],"outputs":[{"type":"uint256"}]}]'
)


class Market:
    def __init__(self, w3: Web3, dep: dict):
        self.w3 = w3
        self.dep = dep
        self.acct = Account.from_key(MAKER_KEY)
        self.tokens = {v["address"].lower(): (k, v["decimals"]) for k, v in dep["tokens"].items()}
        self.prices = dep["prices_usd"]
        self.helper = w3.eth.contract(address=dep["v3_helper"], abi=HELPER_ABI)
        self.pools = dep["pools"]
        self.nonce = w3.eth.get_transaction_count(self.acct.address)
        self.stats = {"trades": 0, "shocks": 0, "competitor": 0, "errors": 0}

    # ------------------------------------------------------------------ chain helpers

    def send(self, fn, gas: int = 600_000) -> bool:
        for attempt in range(3):
            try:
                tx = fn.build_transaction({"from": self.acct.address, "nonce": self.nonce, "gas": gas,
                                           "maxFeePerGas": self.w3.to_wei(1, "gwei"), "maxPriorityFeePerGas": 1000, "chainId": self.dep["chain_id"]})
                signed = self.acct.sign_transaction(tx)
                self.w3.eth.send_raw_transaction(signed.raw_transaction)
                self.nonce += 1
                return True
            except Exception as e:  # noqa: BLE001
                msg = str(e)
                self.nonce = self.w3.eth.get_transaction_count(self.acct.address, "pending")
                if "nonce" in msg.lower() or "underpriced" in msg.lower() or "already known" in msg.lower():
                    continue  # another process shares this account (e.g. tests): refresh the nonce and retry
                self.stats["errors"] += 1
                print(f"[sim] tx failed: {msg[:120]}", file=sys.stderr)
                return False
        self.stats["errors"] += 1
        return False

    def erc20(self, addr: str):
        return self.w3.eth.contract(address=Web3.to_checksum_address(addr), abi=ERC20_ABI)

    def mid(self, p: dict) -> float:
        """token1 per token0 in human units."""
        d0, d1 = self.tokens[p["token0"].lower()][1], self.tokens[p["token1"].lower()][1]
        if p["kind"] in ("UNIV2", "SOLIDLY"):
            abi = V2_ABI if p["kind"] == "UNIV2" else SOL_ABI
            r0, r1, _ = self.w3.eth.contract(address=p["address"], abi=abi).functions.getReserves().call()
            if p.get("stable"):
                return (r1 / 10**d1) / (r0 / 10**d0) if r0 else 0.0  # stable pools: mid ≈ reserve ratio near peg
            return (r1 / 10**d1) / (r0 / 10**d0) if r0 else 0.0
        sp = self.w3.eth.contract(address=p["address"], abi=V3_ABI).functions.slot0().call()[0]
        return (sp / 2**96) ** 2 * 10 ** (d0 - d1)

    def depth_token0(self, p: dict) -> int:
        if p["kind"] in ("UNIV2", "SOLIDLY"):
            abi = V2_ABI if p["kind"] == "UNIV2" else SOL_ABI
            return self.w3.eth.contract(address=p["address"], abi=abi).functions.getReserves().call()[0]
        # V3: virtual reserves overstate executable depth by orders of magnitude for concentrated positions;
        # use the tokens actually held by the pool (all positions) as the depth reference instead.
        return self.erc20(p["token0"]).functions.balanceOf(p["address"]).call()

    # ------------------------------------------------------------------ trading

    def trade(self, p: dict, zero_for_one: bool, amount_in: int) -> bool:
        tin = p["token0"] if zero_for_one else p["token1"]
        if p["kind"] == "UNIV3":
            return self.send(self.helper.functions.swapExactIn(p["address"], zero_for_one, amount_in))
        if p["kind"] == "UNIV2":
            c = self.w3.eth.contract(address=p["address"], abi=V2_ABI)
            r0, r1, _ = c.functions.getReserves().call()
            rin, rout = (r0, r1) if zero_for_one else (r1, r0)
            out = amount_in * 997 * rout // (rin * 1000 + amount_in * 997)
            if out <= 0:
                return False
            if not self.send(self.erc20(tin).functions.transfer(p["address"], amount_in), gas=100_000):
                return False
            return self.send(c.functions.swap(0 if zero_for_one else out, out if zero_for_one else 0, self.acct.address, b""))
        c = self.w3.eth.contract(address=p["address"], abi=SOL_ABI)
        out = c.functions.getAmountOut(amount_in, Web3.to_checksum_address(tin)).call()
        if out <= 0:
            return False
        if not self.send(self.erc20(tin).functions.transfer(p["address"], amount_in), gas=100_000):
            return False
        return self.send(c.functions.swap(0 if zero_for_one else out, out if zero_for_one else 0, self.acct.address, b""))

    def random_trade(self, frac_lo: float, frac_hi: float, pool: dict | None = None, direction: bool | None = None) -> bool:
        p = pool or random.choice(self.pools)
        z41 = random.random() < 0.5 if direction is None else direction
        d0 = self.depth_token0(p)
        frac = math.exp(random.uniform(math.log(frac_lo), math.log(frac_hi)))
        amt0 = int(d0 * frac)
        if z41:
            amount_in = amt0
        else:
            amount_in = int(amt0 * self.mid(p) * 10 ** (self.tokens[p["token1"].lower()][1] - self.tokens[p["token0"].lower()][1]))
        if amount_in <= 0:
            return False
        bal = self.erc20(p["token0"] if z41 else p["token1"]).functions.balanceOf(self.acct.address).call()
        if bal < amount_in:
            return False
        return self.trade(p, z41, amount_in)

    def widest_gap(self) -> tuple[dict, dict, float] | None:
        groups: dict[tuple[str, str], list[tuple[dict, float]]] = {}
        for p in self.pools:
            groups.setdefault((p["token0"].lower(), p["token1"].lower()), []).append((p, self.mid(p)))
        best = None
        for _, lst in groups.items():
            if len(lst) < 2:
                continue
            lo = min(lst, key=lambda x: x[1])
            hi = max(lst, key=lambda x: x[1])
            gap = hi[1] / lo[1] - 1 if lo[1] > 0 else 0
            if best is None or gap > best[2]:
                best = (lo[0], hi[0], gap)
        return best

    def competitor_step(self, min_gap: float = 0.004, close_fraction: float = 0.8) -> bool:
        g = self.widest_gap()
        if not g or g[2] < min_gap:
            return False
        cheap, dear, gap = g
        # buy token0 on the cheap pool (token1 → token0): price there goes up; sell token0 on the dear pool
        # constant-product: relative price move ≈ 2·Δ/R ⇒ Δ ≈ R·(gap·close)/4 on each side
        frac = min(0.03, gap * close_fraction / 4)
        ok1 = self.random_trade(frac, frac, pool=cheap, direction=False)
        ok2 = self.random_trade(frac, frac, pool=dear, direction=True)
        return ok1 or ok2

    def reference_mid(self, p: dict) -> float:
        s0, _ = self.tokens[p["token0"].lower()]
        s1, _ = self.tokens[p["token1"].lower()]
        return self.prices[s0] / self.prices[s1]  # token1 per token0 at the external ("CEX") reference price

    def reversion_step(self, threshold: float = 0.005, step_frac: float = 0.002, max_steps: int = 2) -> int:
        """External arbitrageurs / CEX-DEX flow: push the most mispriced pool back toward the reference price."""
        worst = None
        for p in self.pools:
            if p.get("stable"):
                continue
            dev = self.mid(p) / self.reference_mid(p) - 1
            if worst is None or abs(dev) > abs(worst[1]):
                worst = (p, dev)
        if worst is None or abs(worst[1]) < threshold:
            return 0
        p, dev = worst
        done = 0
        for _ in range(max_steps):
            # price (token1 per token0) too high → sell token0 into the pool (zeroForOne=True) and vice versa
            frac = min(0.02, max(step_frac, abs(dev) / 4))
            if not self.random_trade(frac, frac, pool=p, direction=dev > 0):
                break
            done += 1
            dev = self.mid(p) / self.reference_mid(p) - 1
            if abs(dev) < threshold:
                break
        return done

    def set_base_fee(self, gwei: float) -> None:
        try:
            self.w3.provider.make_request("anvil_setNextBlockBaseFeePerGas", [hex(int(gwei * 1e9))])
        except Exception:  # noqa: BLE001
            pass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--deployments", default=str(ROOT / "deployments.local.json"))
    ap.add_argument("--rate", type=float, default=1.0, help="background trades per second")
    ap.add_argument("--shock-every", type=float, default=25.0, help="mean seconds between shocks")
    ap.add_argument("--competitor", type=float, default=0.15, help="probability per second that a competitor closes the widest gap")
    ap.add_argument("--reversion", type=float, default=0.25, help="probability per second of external flow pulling the worst pool to the reference price")
    ap.add_argument("--base-fee-gwei", type=float, default=0.01)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--duration", type=float, default=0, help="seconds (0 = forever)")
    a = ap.parse_args()
    if a.seed is not None:
        random.seed(a.seed)
    dep = json.loads(pathlib.Path(a.deployments).read_text())
    w3 = Web3(Web3.HTTPProvider(dep["rpc"], request_kwargs={"timeout": 10}))
    m = Market(w3, dep)
    print(f"[sim] maker {m.acct.address} on chain {dep['chain_id']} — {len(m.pools)} pools. DEVNET ONLY, no real markets.")
    t_start = time.time()
    last_report = t_start
    while True:
        if a.duration and time.time() - t_start > a.duration:
            break
        m.set_base_fee(a.base_fee_gwei * math.exp(random.gauss(0, 0.25)))
        if random.random() < a.rate:
            if m.random_trade(0.0002, 0.003):  # 0.02–0.3 % of depth: moves a V2 price by 0.04–0.6 %
                m.stats["trades"] += 1
        if random.random() < 1.0 / max(a.shock_every, 1.0):
            if m.random_trade(0.005, 0.03):  # 0.5–3 % of depth: 1–6 % price move → opens cross-pool gaps
                m.stats["shocks"] += 1
        if random.random() < a.competitor:
            if m.competitor_step():
                m.stats["competitor"] += 1
        if random.random() < a.reversion:
            m.stats["reversion"] = m.stats.get("reversion", 0) + m.reversion_step()
        if time.time() - last_report > 30:
            last_report = time.time()
            g = m.widest_gap()
            print(f"[sim] t+{int(time.time() - t_start)}s {m.stats} widest gap {g[2] * 1e4:.1f} bps" if g else f"[sim] {m.stats}")
        time.sleep(1.0)
    print(f"[sim] done {m.stats}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
