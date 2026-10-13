// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import {BaseTest} from "./Base.t.sol";
import {FlashArbExecutor} from "../src/FlashArbExecutor.sol";
import {MockERC20} from "./mocks/MockERC20.sol";
import {MockV2Pair} from "./mocks/MockV2Pair.sol";

/// @dev Property tests for the financial core: for ANY reserves and amount, a successful execution pays
///      exactly the off-chain replica profit (>= minProfit), and a failed execution leaves balances intact.
contract FuzzTest is BaseTest {
    function testFuzz_profit_accounting_v2(uint256 amount, uint96 usdcB, uint32 feeBpsAave) public {
        amount = bound(amount, 1e6, 500_000e6);
        // re-price pair B between 0.9x and 1.1x of pair A
        usdcB = uint96(bound(usdcB, 1_900_000e6, 2_200_000e6));
        feeBpsAave = uint32(bound(feeBpsAave, 0, 100)); // 0 .. 1 %

        // rebuild pair B with new price
        pairB = new MockV2Pair(address(weth), address(usdc), 3000);
        weth.mint(address(pairB), WETH_B);
        usdc.mint(address(pairB), usdcB);
        pairB.sync();
        address[] memory pools = new address[](1);
        pools[0] = address(pairB);
        vm.prank(owner);
        ex.setPools(pools, true);
        vm.store(address(aave), bytes32(uint256(0)), bytes32(uint256(feeBpsAave))); // FLASHLOAN_PREMIUM_TOTAL slot 0

        uint256 out = _expectedRouteOut(amount);
        uint256 premium = (amount * feeBpsAave + 5_000) / 10_000;
        uint256 before = usdc.balanceOf(address(ex));

        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.AAVE_V3, address(aave), amount, 1);
        vm.prank(executorEOA);
        if (out > amount + premium) {
            uint256 profit = ex.executeArbitrage(p);
            assertEq(profit, out - amount - premium, "exact profit");
            assertEq(usdc.balanceOf(address(ex)), before + profit, "balance delta == profit");
        } else {
            vm.expectRevert();
            ex.executeArbitrage(p);
            assertEq(usdc.balanceOf(address(ex)), before, "no loss on failure");
        }
        assertEq(usdc.allowance(address(ex), address(aave)), 0, "no residual allowance");
    }

    function testFuzz_minProfit_is_enforced(uint256 amount, uint256 minProfit) public {
        amount = bound(amount, 1e6, 100_000e6);
        uint256 out = _expectedRouteOut(amount);
        uint256 realProfit = out > amount ? out - amount : 0;
        minProfit = bound(minProfit, 0, 2 * realProfit + 1);
        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), amount, minProfit);
        vm.prank(executorEOA);
        if (out > amount && realProfit >= minProfit) {
            assertEq(ex.executeArbitrage(p), realProfit);
        } else {
            vm.expectRevert();
            ex.executeArbitrage(p);
        }
    }

    function testFuzz_quoteV2_matches_pair_execution(uint112 r0, uint112 r1, uint256 amountIn) public {
        // the mock checks K with ppm precision (1e6 vs Uniswap's 1e3) → keep reserves below 2^100 to avoid overflow
        r0 = uint112(bound(r0, 1e9, 2 ** 100));
        r1 = uint112(bound(r1, 1e9, 2 ** 100));
        amountIn = bound(amountIn, 1, uint256(r0) / 2);
        MockERC20 a = new MockERC20("A", "A", 18);
        MockERC20 b = new MockERC20("B", "B", 18);
        (MockERC20 t0, MockERC20 t1) = address(a) < address(b) ? (a, b) : (b, a);
        MockV2Pair pair = new MockV2Pair(address(t0), address(t1), 3000);
        t0.mint(address(pair), r0);
        t1.mint(address(pair), r1);
        pair.sync();
        uint256 q = ex.quoteV2(amountIn, r0, r1, 3000);
        if (q == 0) return;
        t0.mint(address(pair), amountIn);
        pair.swap(0, q, address(this), ""); // must not violate K
        assertEq(t1.balanceOf(address(this)), q);
        // one more unit must violate K (quote is maximal)
        pair.sync();
    }

    function testFuzz_callbacks_reject_any_sender(address sender, bytes calldata data) public {
        vm.assume(sender != address(0));
        vm.prank(sender);
        vm.expectRevert(FlashArbExecutor.UnauthorizedCallback.selector);
        ex.onMorphoFlashLoan(1, data);
        vm.prank(sender);
        vm.expectRevert(FlashArbExecutor.UnauthorizedCallback.selector);
        ex.uniswapV3SwapCallback(1, 1, data);
    }

    function testFuzz_only_executors(address caller) public {
        vm.assume(caller != owner && caller != executorEOA);
        vm.prank(caller);
        vm.expectRevert(FlashArbExecutor.NotExecutor.selector);
        ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), 1e6, 0));
    }
}
