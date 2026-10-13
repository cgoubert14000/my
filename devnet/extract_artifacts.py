"""Extract ABI + creation bytecode of the official Uniswap V2/V3 npm builds into small JSON files.

These artifacts are the *real* production bytecodes (GPL licensed, see NOTICE.md) and are used by:
  - Foundry tests  (contracts/test/RealUniswapV3.t.sol)        -> validate the executor against real pools
  - devnet/deploy_devnet.py                                     -> local anvil chain with real DEX code
  - backend/tests/test_v3_math_vs_chain.py                      -> validate the Python V3/V2 math exactly
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).parent
NM = ROOT / "node_modules" / "@uniswap"
OUT = ROOT / "artifacts"
OUT.mkdir(exist_ok=True)

SOURCES = {
    "UniswapV2Factory": NM / "v2-core/build/UniswapV2Factory.json",
    "UniswapV2Pair": NM / "v2-core/build/UniswapV2Pair.json",
    "UniswapV2Router02": NM / "v2-periphery/build/UniswapV2Router02.json",
    "WETH9": NM / "v2-periphery/build/WETH9.json",
    "UniswapV3Factory": NM / "v3-core/artifacts/contracts/UniswapV3Factory.sol/UniswapV3Factory.json",
    "UniswapV3Pool": NM / "v3-core/artifacts/contracts/UniswapV3Pool.sol/UniswapV3Pool.json",
    "SwapRouter": NM / "v3-periphery/artifacts/contracts/SwapRouter.sol/SwapRouter.json",
    "QuoterV2": NM / "v3-periphery/artifacts/contracts/lens/QuoterV2.sol/QuoterV2.json",
    "TickLens": NM / "v3-periphery/artifacts/contracts/lens/TickLens.sol/TickLens.json",
}

def main() -> int:
    for name, path in SOURCES.items():
        if not path.exists():
            print(f"missing {path} (run `npm install` in devnet/)", file=sys.stderr)
            return 1
        raw = json.loads(path.read_text())
        bytecode = raw.get("bytecode") or raw.get("evm", {}).get("bytecode", {}).get("object")
        if isinstance(bytecode, dict):
            bytecode = bytecode["object"]
        if not bytecode.startswith("0x"):
            bytecode = "0x" + bytecode
        (OUT / f"{name}.json").write_text(json.dumps({"contractName": name, "abi": raw["abi"], "bytecode": bytecode}))
        print(f"{name:<22} {len(bytecode)//2:>7} bytes")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
