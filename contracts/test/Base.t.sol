// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import {Test} from "forge-std/Test.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {FlashArbExecutor} from "../src/FlashArbExecutor.sol";
import {MockERC20} from "./mocks/MockERC20.sol";
import {MockV2Pair} from "./mocks/MockV2Pair.sol";
import {MockSolidlyPool} from "./mocks/MockSolidlyPool.sol";
import {MockBalancerVault, MockAavePool, MockMorpho} from "./mocks/MockFlashProviders.sol";

/// @dev Shared fixture: WETH/USDC with a deliberate price gap between two V2 pairs.
///      pairA: 1 WETH = 2000 USDC, pairB: 1 WETH = 2060 USDC (3 % gap: enough to beat 2 x 0.3 % fees + price impact)  → buy WETH on A, sell on B.
abstract contract BaseTest is Test {
    address owner = makeAddr("owner");
    address executorEOA = makeAddr("executor");
    address guardian = makeAddr("guardian");
    address stranger = makeAddr("stranger");

    MockERC20 weth;
    MockERC20 usdc;
    MockV2Pair pairA;
    MockV2Pair pairB;
    MockSolidlyPool stablePool; // USDC/DAI-like, here USDC/USDT 6 decimals both
    MockERC20 usdt;
    MockBalancerVault vault;
    MockAavePool aave;
    MockMorpho morpho;
    FlashArbExecutor ex;

    uint256 constant WETH_A = 1_000 ether;
    uint256 constant USDC_A = 2_000_000e6;
    uint256 constant WETH_B = 1_000 ether;
    uint256 constant USDC_B = 2_060_000e6;

    function setUp() public virtual {
        weth = new MockERC20("Wrapped Ether", "WETH", 18);
        usdc = new MockERC20("USD Coin", "USDC", 6);
        usdt = new MockERC20("Tether", "USDT", 6);

        pairA = new MockV2Pair(address(weth), address(usdc), 3000);
        pairB = new MockV2Pair(address(weth), address(usdc), 3000);
        weth.mint(address(pairA), WETH_A);
        usdc.mint(address(pairA), USDC_A);
        weth.mint(address(pairB), WETH_B);
        usdc.mint(address(pairB), USDC_B);
        pairA.sync();
        pairB.sync();

        stablePool = new MockSolidlyPool(address(usdc), address(usdt), true, 5);
        usdc.mint(address(stablePool), 5_000_000e6);
        usdt.mint(address(stablePool), 5_000_000e6);
        stablePool.sync();

        vault = new MockBalancerVault(0);
        aave = new MockAavePool(5);
        morpho = new MockMorpho();
        usdc.mint(address(vault), 50_000_000e6);
        usdc.mint(address(aave), 50_000_000e6);
        usdc.mint(address(morpho), 50_000_000e6);
        weth.mint(address(vault), 10_000 ether);

        vm.startPrank(owner);
        ex = new FlashArbExecutor(owner, executorEOA);
        ex.setGuardian(guardian);
        address[] memory toks = new address[](3);
        toks[0] = address(weth);
        toks[1] = address(usdc);
        toks[2] = address(usdt);
        uint256[] memory caps = new uint256[](3);
        ex.setTokens(toks, true, caps);
        address[] memory pools = new address[](3);
        pools[0] = address(pairA);
        pools[1] = address(pairB);
        pools[2] = address(stablePool);
        ex.setPools(pools, true);
        address[] memory provs = new address[](3);
        provs[0] = address(vault);
        provs[1] = address(aave);
        provs[2] = address(morpho);
        ex.setProviders(provs, true);
        vm.stopPrank();
    }

    // ---- helpers ------------------------------------------------------

    function _hop(FlashArbExecutor.DexKind kind, address pool, address tIn, address tOut, uint32 feePpm, uint256 minOut)
        internal
        pure
        returns (FlashArbExecutor.Hop memory)
    {
        return FlashArbExecutor.Hop({kind: kind, pool: pool, tokenIn: tIn, tokenOut: tOut, feePpm: feePpm, minAmountOut: minOut});
    }

    /// @dev USDC -> pairA -> WETH -> pairB -> USDC
    function _usdcRoute() internal view returns (FlashArbExecutor.Hop[] memory hops) {
        hops = new FlashArbExecutor.Hop[](2);
        hops[0] = _hop(FlashArbExecutor.DexKind.UNIV2, address(pairA), address(usdc), address(weth), 3000, 0);
        hops[1] = _hop(FlashArbExecutor.DexKind.UNIV2, address(pairB), address(weth), address(usdc), 3000, 0);
    }

    function _params(FlashArbExecutor.FlashSource src, address provider, uint256 amount, uint256 minProfit)
        internal
        view
        returns (FlashArbExecutor.ArbParams memory p)
    {
        p = FlashArbExecutor.ArbParams({
            source: src,
            provider: provider,
            token: address(usdc),
            amount: amount,
            minProfit: minProfit,
            deadline: block.timestamp + 60,
            hops: _usdcRoute()
        });
    }

    function _v2Out(uint256 amountIn, uint256 rIn, uint256 rOut, uint32 feePpm) internal pure returns (uint256) {
        uint256 aw = amountIn * (1_000_000 - feePpm);
        return (aw * rOut) / (rIn * 1_000_000 + aw);
    }

    /// @dev Off-chain replica of the expected route output (what the Python engine computes).
    function _expectedRouteOut(uint256 amountIn) internal view returns (uint256) {
        (uint112 a0, uint112 a1,) = pairA.getReserves();
        (uint112 b0, uint112 b1,) = pairB.getReserves();
        bool usdcIs0 = address(usdc) < address(weth);
        (uint256 aIn, uint256 aOut) = usdcIs0 ? (uint256(a0), uint256(a1)) : (uint256(a1), uint256(a0));
        uint256 wethOut = _v2Out(amountIn, aIn, aOut, 3000);
        (uint256 bIn, uint256 bOut) = usdcIs0 ? (uint256(b1), uint256(b0)) : (uint256(b0), uint256(b1));
        return _v2Out(wethOut, bIn, bOut, 3000);
    }
}
