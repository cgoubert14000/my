// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import {Test} from "forge-std/Test.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {FlashArbExecutor} from "../src/FlashArbExecutor.sol";
import {MockERC20} from "./mocks/MockERC20.sol";
import {MockV2Pair} from "./mocks/MockV2Pair.sol";
import {MockBalancerVault} from "./mocks/MockFlashProviders.sol";
import {V3Helper, IUniswapV3PoolFull, IUniswapV3FactoryLike, Sqrt} from "./mocks/V3Helpers.sol";

/// @notice Deploys the REAL Uniswap V3 factory/pool bytecode (official npm build, see devnet/artifacts)
///         and runs a V3 <-> V2 arbitrage through the executor, including the V3 pool flash-loan source.
contract RealUniswapV3Test is Test {
    address owner = makeAddr("owner");
    address executorEOA = makeAddr("executor");

    MockERC20 weth;
    MockERC20 usdc;
    IUniswapV3FactoryLike factory;
    IUniswapV3PoolFull pool;
    MockV2Pair pairV2;
    MockBalancerVault vault;
    V3Helper helper;
    FlashArbExecutor ex;
    bool wethIs0;

    function _deployArtifact(string memory name) internal returns (address addr) {
        string memory json = vm.readFile(string.concat("../devnet/artifacts/", name, ".json"));
        bytes memory code = vm.parseJsonBytes(json, ".bytecode");
        assembly {
            addr := create(0, add(code, 0x20), mload(code))
        }
        require(addr != address(0), "deploy failed");
    }

    function setUp() public {
        weth = new MockERC20("WETH", "WETH", 18);
        usdc = new MockERC20("USDC", "USDC", 6);
        wethIs0 = address(weth) < address(usdc);

        factory = IUniswapV3FactoryLike(_deployArtifact("UniswapV3Factory"));
        pool = IUniswapV3PoolFull(factory.createPool(address(weth), address(usdc), 3000));

        // price: 2000 USDC per WETH (raw: 2000e6 / 1e18)
        uint256 ratioX192 = wethIs0 ? (uint256(2000e6) << 192) / 1e18 : (uint256(1e18) << 192) / 2000e6;
        uint160 sqrtP = uint160(Sqrt.sqrt(ratioX192));
        pool.initialize(sqrtP);

        helper = new V3Helper();
        weth.mint(address(helper), 1_000_000 ether);
        usdc.mint(address(helper), 1_000_000_000e6);
        // full-range liquidity ~ sqrt(1000 WETH * 2M USDC)
        helper.mint(address(pool), -887220, 887220, uint128(44_721_359_549_995_793));

        // V2 pair priced 3 % higher (WETH more expensive) → buy WETH on V3, sell on V2
        pairV2 = new MockV2Pair(address(weth), address(usdc), 3000);
        weth.mint(address(pairV2), 1_000 ether);
        usdc.mint(address(pairV2), 2_060_000e6);
        pairV2.sync();

        vault = new MockBalancerVault(0);
        usdc.mint(address(vault), 10_000_000e6);

        vm.startPrank(owner);
        ex = new FlashArbExecutor(owner, executorEOA);
        address[] memory toks = new address[](2);
        toks[0] = address(weth);
        toks[1] = address(usdc);
        ex.setTokens(toks, true, new uint256[](0));
        address[] memory pools = new address[](2);
        pools[0] = address(pool);
        pools[1] = address(pairV2);
        ex.setPools(pools, true);
        address[] memory provs = new address[](2);
        provs[0] = address(vault);
        provs[1] = address(pool); // V3 pool as flash source
        ex.setProviders(provs, true);
        vm.stopPrank();
    }

    function _route() internal view returns (FlashArbExecutor.Hop[] memory hops) {
        hops = new FlashArbExecutor.Hop[](2);
        hops[0] = FlashArbExecutor.Hop(FlashArbExecutor.DexKind.UNIV3, address(pool), address(usdc), address(weth), 0, 0);
        hops[1] = FlashArbExecutor.Hop(FlashArbExecutor.DexKind.UNIV2, address(pairV2), address(weth), address(usdc), 3000, 0);
    }

    /// @dev Reference computation: perform the same swaps manually from the helper in a snapshot.
    function _reference(uint256 amountIn) internal returns (uint256 out) {
        uint256 snap = vm.snapshotState();
        uint256 wethOut = helper.swapExactIn(address(pool), !wethIs0, amountIn); // usdc -> weth
        (uint112 r0, uint112 r1,) = pairV2.getReserves();
        (uint256 rIn, uint256 rOut) = wethIs0 ? (uint256(r0), uint256(r1)) : (uint256(r1), uint256(r0));
        out = ex.quoteV2(wethOut, rIn, rOut, 3000);
        vm.revertToState(snap);
    }

    function test_real_v3_pool_arbitrage_balancer_source() public {
        uint256 amount = 5_000e6;
        uint256 expected = _reference(amount) - amount;
        FlashArbExecutor.ArbParams memory p = FlashArbExecutor.ArbParams({
            source: FlashArbExecutor.FlashSource.BALANCER_V2,
            provider: address(vault),
            token: address(usdc),
            amount: amount,
            minProfit: 1,
            deadline: block.timestamp + 60,
            hops: _route()
        });
        vm.prank(executorEOA);
        uint256 profit = ex.executeArbitrage(p);
        assertEq(profit, expected, "V3 path profit must match reference swaps");
        assertGt(profit, 0);
    }

    function test_real_v3_pool_as_flash_source() public {
        // Borrow USDC from the V3 pool itself (fee = 0.3 %), route through V3 then V2 — route must still be
        // cyclic and the pool flash fee is paid. Profit lower than Balancer (0 %) by the flash fee.
        uint256 amount = 5_000e6;
        FlashArbExecutor.ArbParams memory p = FlashArbExecutor.ArbParams({
            source: FlashArbExecutor.FlashSource.UNISWAP_V3,
            provider: address(pool),
            token: address(usdc),
            amount: amount,
            minProfit: 0,
            deadline: block.timestamp + 60,
            hops: _route()
        });
        // Trading on the very pool we flash from is allowed by Uniswap V3 (flash and swap share no lock)?
        // No: the pool is locked during flash → swap on the same pool reverts with "LOK". The executor must
        // surface that as a revert and lose nothing.
        vm.prank(executorEOA);
        vm.expectRevert();
        ex.executeArbitrage(p);
        assertEq(usdc.balanceOf(address(ex)), 0);
    }

    function testFuzz_real_v3_profit_matches_reference(uint256 amount) public {
        amount = bound(amount, 1e6, 100_000e6);
        uint256 ref = _reference(amount);
        FlashArbExecutor.ArbParams memory p = FlashArbExecutor.ArbParams({
            source: FlashArbExecutor.FlashSource.BALANCER_V2,
            provider: address(vault),
            token: address(usdc),
            amount: amount,
            minProfit: 0,
            deadline: block.timestamp + 60,
            hops: _route()
        });
        vm.prank(executorEOA);
        if (ref > amount) {
            assertEq(ex.executeArbitrage(p), ref - amount);
        } else {
            vm.expectRevert();
            ex.executeArbitrage(p);
        }
    }
}
