#!/usr/bin/env python3
"""Deploy a realistic local arbitrage devnet on anvil.

What gets deployed (all REAL bytecode where it exists on npm):
  - WETH9, USDC(6), DAI(18), WBTC(8)                       (WETH9 real; others MockERC20)
  - Uniswap V2 factory  ("uniswap_v2")  + 5 pairs          (real bytecode)
  - a second V2 factory ("sushiswap")   + 5 pairs          (real bytecode, different prices)
  - Uniswap V3 factory  ("uniswap_v3")  + pools 500/3000/100 with multi-range liquidity (real bytecode)
  - Solidly pools ("aerodrome"): volatile WETH/USDC 30 bps, stable USDC/DAI 5 bps (verbatim Aerodrome math)
  - Flash-loan providers: Balancer-vault mock (0 fee), Aave-pool mock (5 bps), Morpho mock (0 fee)
  - FlashArbExecutor with allowlists configured
Output: devnet/deployments.local.json (consumed by the backend chain registry as chain "local").

Usage:
  anvil --chain-id 31337 --block-time 2 --host 0.0.0.0 &
  python devnet/deploy_devnet.py [--rpc http://127.0.0.1:8545]
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import subprocess
import sys

from eth_account import Account
from web3 import Web3

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent
ART = ROOT / "artifacts"
OUT = REPO / "contracts" / "out"

# anvil default mnemonic accounts
KEYS = {
    "deployer": "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80",
    "executor": "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d",
    "maker": "0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a",
}

Q96 = 2**96
MULTICALL3 = "0xcA11bde05977b3631167028862bE2a173976CA11"


def forge_artifact(name: str, file: str | None = None) -> dict:
    p = OUT / f"{file or name}.sol" / f"{name}.json"
    if not p.exists():
        print(f"[devnet] {p} missing → running `forge build` ...")
        env = dict(**__import__("os").environ)
        subprocess.run(["forge", "build"], cwd=REPO / "contracts", check=True, env=env)
    d = json.loads(p.read_text())
    return {"abi": d["abi"], "bytecode": d["bytecode"]["object"]}


def npm_artifact(name: str) -> dict:
    return json.loads((ART / f"{name}.json").read_text())


class Deployer:
    def __init__(self, w3: Web3, key: str):
        self.w3 = w3
        self.acct = Account.from_key(key)
        self.nonce = w3.eth.get_transaction_count(self.acct.address)

    def send(self, tx: dict) -> dict:
        tx.setdefault("from", self.acct.address)
        tx.setdefault("nonce", self.nonce)
        tx.setdefault("chainId", self.w3.eth.chain_id)
        tx.setdefault("gasPrice", self.w3.eth.gas_price)
        if "gas" not in tx:
            tx["gas"] = int(self.w3.eth.estimate_gas(tx) * 1.3)
        signed = self.acct.sign_transaction(tx)
        h = self.w3.eth.send_raw_transaction(signed.raw_transaction)
        self.nonce += 1
        rcpt = self.w3.eth.wait_for_transaction_receipt(h, timeout=120)
        if rcpt.status != 1:
            raise RuntimeError(f"tx failed: {tx.get('to')} {tx.get('data', '')[:10]}")
        return rcpt

    def deploy(self, art: dict, *args, gas: int = 6_000_000):
        c = self.w3.eth.contract(abi=art["abi"], bytecode=art["bytecode"])
        tx = c.constructor(*args).build_transaction({"from": self.acct.address, "nonce": self.nonce, "gas": gas,
                                                      "gasPrice": self.w3.eth.gas_price, "chainId": self.w3.eth.chain_id})
        rcpt = self.send(tx)
        return self.w3.eth.contract(address=rcpt.contractAddress, abi=art["abi"])

    def call(self, fn, gas: int | None = None):
        tx = fn.build_transaction({"from": self.acct.address, "nonce": self.nonce, "gasPrice": self.w3.eth.gas_price,
                                   "chainId": self.w3.eth.chain_id, **({"gas": gas} if gas else {})})
        return self.send(tx)


def sqrt_price_x96(price_1_per_0: float, dec0: int, dec1: int) -> int:
    raw = price_1_per_0 * 10**dec1 / 10**dec0
    return int(math.sqrt(raw) * Q96)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rpc", default="http://127.0.0.1:8545")
    ap.add_argument("--eth-price", type=float, default=2000.0)
    ap.add_argument("--btc-price", type=float, default=60000.0)
    ap.add_argument("--block-time", type=int, default=2)
    args = ap.parse_args()

    w3 = Web3(Web3.HTTPProvider(args.rpc, request_kwargs={"timeout": 60}))
    assert w3.is_connected(), f"cannot reach {args.rpc} — start anvil first"
    # deploy with instant mining, then switch to interval mining (Base-like 2 s blocks)
    w3.provider.make_request("evm_setAutomine", [True])
    d = Deployer(w3, KEYS["deployer"])
    executor_addr = Account.from_key(KEYS["executor"]).address
    maker_addr = Account.from_key(KEYS["maker"]).address
    print(f"[devnet] chain {w3.eth.chain_id} deployer {d.acct.address}")

    # Multicall3 at its canonical cross-chain address (same as Base/Arbitrum/Ethereum) via anvil_setCode
    mc3 = json.loads((OUT / "Multicall3.sol" / "Multicall3.json").read_text())["deployedBytecode"]["object"]
    w3.provider.make_request("anvil_setCode", [MULTICALL3, mc3])

    erc20 = forge_artifact("MockERC20")
    weth = d.deploy(npm_artifact("WETH9"))
    usdc = d.deploy(erc20, "USD Coin", "USDC", 6)
    dai = d.deploy(erc20, "Dai", "DAI", 18)
    wbtc = d.deploy(erc20, "Wrapped BTC", "WBTC", 8)
    tokens = {"WETH": (weth, 18), "USDC": (usdc, 6), "DAI": (dai, 18), "WBTC": (wbtc, 8)}
    print("[devnet] tokens", {k: v[0].address for k, v in tokens.items()})

    def mint(tok: str, to: str, amount_units: float):
        c, dec = tokens[tok]
        raw = int(amount_units * 10**dec)
        if tok == "WETH":
            tx = c.functions.deposit().build_transaction({"from": d.acct.address, "nonce": d.nonce, "value": raw,
                                                          "gasPrice": w3.eth.gas_price, "chainId": w3.eth.chain_id})
            d.send(tx)
            d.call(c.functions.transfer(to, raw))
        else:
            d.call(c.functions.mint(to, raw))

    # fund deployer's WETH (anvil gives 10k ETH per account)
    prices = {"WETH": args.eth_price, "USDC": 1.0, "DAI": 1.0, "WBTC": args.btc_price}

    # ---------------- V2 factories (two DEXes) ----------------
    v2f = npm_artifact("UniswapV2Factory")
    pair_art = npm_artifact("UniswapV2Pair")
    v2_dexes = {"uniswap_v2": d.deploy(v2f, d.acct.address), "sushiswap": d.deploy(v2f, d.acct.address)}
    # (tokA, tokB, USD depth, price skew for the second dex)
    v2_markets = [("WETH", "USDC", 3_000_000), ("WETH", "DAI", 1_500_000), ("USDC", "DAI", 2_000_000),
                  ("WBTC", "WETH", 1_000_000), ("WBTC", "USDC", 800_000)]
    pools_out: list[dict] = []
    for dex_name, fac in v2_dexes.items():
        for i, (a, b, depth_usd) in enumerate(v2_markets):
            d.call(fac.functions.createPair(tokens[a][0].address, tokens[b][0].address))
            pair_addr = fac.functions.getPair(tokens[a][0].address, tokens[b][0].address).call()
            skew = 1.0 if dex_name == "uniswap_v2" else (1.0 + 0.004 * ((-1) ** i))  # ±0.4 % initial gaps
            amt_a = depth_usd / 2 / prices[a]
            amt_b = depth_usd / 2 / prices[b] * skew
            mint(a, pair_addr, amt_a)
            mint(b, pair_addr, amt_b)
            pair = w3.eth.contract(address=pair_addr, abi=pair_art["abi"])
            d.call(pair.functions.mint(d.acct.address))
            pools_out.append({"address": pair_addr, "dex": dex_name, "kind": "UNIV2", "fee_ppm": 3000,
                              "token0": pair.functions.token0().call(), "token1": pair.functions.token1().call()})
    print(f"[devnet] V2 pairs: {len(pools_out)}")

    # ---------------- Uniswap V3 ----------------
    v3f = d.deploy(npm_artifact("UniswapV3Factory"))
    d.call(v3f.functions.enableFeeAmount(100, 1))  # 1 bps tier (enabled by governance on mainnet, not in the 1.0.1 build)
    v3pool_abi = npm_artifact("UniswapV3Pool")["abi"]
    helper = d.deploy(forge_artifact("V3Helper", "V3Helpers"))
    for tok in tokens:
        mint(tok, helper.address, 50_000_000 / prices[tok])  # ample inventory for minting positions
    v3_markets = [("WETH", "USDC", 500, 2_000_000), ("WETH", "USDC", 3000, 1_000_000), ("WETH", "DAI", 3000, 600_000),
                  ("USDC", "DAI", 100, 1_500_000), ("WBTC", "WETH", 3000, 700_000)]
    spacing = {100: 1, 500: 10, 3000: 60, 10000: 200}
    for a, b, fee, depth_usd in v3_markets:
        ta, tb = tokens[a][0].address, tokens[b][0].address
        d.call(v3f.functions.createPool(ta, tb, fee), gas=6_000_000)
        pool_addr = v3f.functions.getPool(ta, tb, fee).call()
        pool = w3.eth.contract(address=pool_addr, abi=v3pool_abi)
        t0 = pool.functions.token0().call()
        a0, b0 = (a, b) if t0.lower() == ta.lower() else (b, a)
        dec0, dec1 = tokens[a0][1], tokens[b0][1]
        p = prices[a0] / prices[b0]  # token1 per token0
        sp = sqrt_price_x96(p, dec0, dec1)
        d.call(pool.functions.initialize(sp))
        tick = pool.functions.slot0().call()[1]
        ts = spacing[fee]
        base = tick - (tick % ts)
        # liquidity so that the virtual depth ≈ depth_usd: L ≈ sqrt(x*y) with x,y in raw units
        x_raw = depth_usd / 2 / prices[a0] * 10**dec0
        y_raw = depth_usd / 2 / prices[b0] * 10**dec1
        L_full = int(math.sqrt(x_raw * y_raw))
        full = (887272 // ts) * ts
        positions = [(-full, full, L_full // 4)]
        for width_ticks, share in ((ts * 200, 6), (ts * 50, 10), (ts * 10, 14)):
            lo = base - width_ticks
            hi = base + width_ticks + ts
            positions.append((lo, hi, L_full * share))
        for lo, hi, L in positions:
            d.call(helper.functions.mint(pool_addr, lo, hi, L), gas=2_000_000)
        pools_out.append({"address": pool_addr, "dex": "uniswap_v3", "kind": "UNIV3", "fee_ppm": fee, "tick_spacing": ts,
                          "token0": t0, "token1": pool.functions.token1().call()})
    print("[devnet] V3 pools: 5")

    # ---------------- Solidly (Aerodrome-like) ----------------
    sol_art = forge_artifact("MockSolidlyPool")
    for a, b, stable, fee_bps, depth_usd in (("WETH", "USDC", False, 30, 1_200_000), ("USDC", "DAI", True, 5, 3_000_000),
                                              ("WETH", "DAI", False, 30, 500_000)):
        pool = d.deploy(sol_art, tokens[a][0].address, tokens[b][0].address, stable, fee_bps)
        mint(a, pool.address, depth_usd / 2 / prices[a])
        mint(b, pool.address, depth_usd / 2 / prices[b] * 1.003)
        d.call(pool.functions.sync())
        pools_out.append({"address": pool.address, "dex": "aerodrome", "kind": "SOLIDLY", "fee_ppm": fee_bps * 100,
                          "stable": stable, "token0": pool.functions.token0().call(), "token1": pool.functions.token1().call()})
    print("[devnet] Solidly pools: 3")

    # ---------------- Flash loan providers ----------------
    vault = d.deploy(forge_artifact("MockBalancerVault", "MockFlashProviders"), 0)
    aave = d.deploy(forge_artifact("MockAavePool", "MockFlashProviders"), 5)
    morpho = d.deploy(forge_artifact("MockMorpho", "MockFlashProviders"))
    for prov in (vault, aave, morpho):
        for tok in tokens:
            mint(tok, prov.address, 20_000_000 / prices[tok])

    # ---------------- Executor ----------------
    ex = d.deploy(forge_artifact("FlashArbExecutor"), d.acct.address, executor_addr)
    tok_addrs = [c.address for c, _ in tokens.values()]
    d.call(ex.functions.setTokens(tok_addrs, True, [0] * len(tok_addrs)))
    d.call(ex.functions.setPools([p["address"] for p in pools_out], True))
    d.call(ex.functions.setProviders([vault.address, aave.address, morpho.address], True))
    # fund executor EOA + maker with ETH for gas (anvil accounts already have 10k ETH) and maker with tokens
    for tok in tokens:
        mint(tok, maker_addr, 5_000_000 / prices[tok])

    out = {
        "chain_id": w3.eth.chain_id,
        "rpc": args.rpc,
        "tokens": {k: {"address": v[0].address, "decimals": v[1], "symbol": k} for k, v in tokens.items()},
        "native_wrapped": weth.address,
        "pools": pools_out,
        "flash_providers": {"BALANCER_V2": vault.address, "AAVE_V3": aave.address, "MORPHO": morpho.address},
        "executor": ex.address,
        "accounts": {"owner": d.acct.address, "executor": executor_addr, "maker": maker_addr},
        "prices_usd": prices,
        "v2_factories": {k: v.address for k, v in v2_dexes.items()},
        "v3_factory": v3f.address,
        "v3_helper": helper.address,
        "multicall3": MULTICALL3,
    }
    (ROOT / "deployments.local.json").write_text(json.dumps(out, indent=2))
    w3.provider.make_request("evm_setAutomine", [False])
    w3.provider.make_request("evm_setIntervalMining", [args.block_time])
    print(f"[devnet] executor {ex.address}; wrote devnet/deployments.local.json ({len(pools_out)} pools)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
