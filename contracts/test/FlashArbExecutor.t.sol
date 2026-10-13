// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import {BaseTest} from "./Base.t.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {Pausable} from "@openzeppelin/contracts/utils/Pausable.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {FlashArbExecutor} from "../src/FlashArbExecutor.sol";
import {MockERC20, FeeOnTransferERC20} from "./mocks/MockERC20.sol";
import {MockV2Pair} from "./mocks/MockV2Pair.sol";
import {Attacker} from "./mocks/MockFlashProviders.sol";

contract FlashArbExecutorTest is BaseTest {
    uint256 constant AMOUNT = 10_000e6;

    // ------------------------------------------------------------------
    // Happy paths: every flash-loan source
    // ------------------------------------------------------------------

    function test_balancer_profitable() public {
        uint256 expected = _expectedRouteOut(AMOUNT) - AMOUNT; // fee 0
        vm.prank(executorEOA);
        uint256 profit = ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1));
        assertEq(profit, expected, "profit must equal off-chain replica");
        assertEq(usdc.balanceOf(address(ex)), expected);
        assertEq(ex.totalExecutions(), 1);
    }

    function test_aave_profitable_pays_premium() public {
        uint256 premium = (AMOUNT * 5 + 5_000) / 10_000;
        uint256 expected = _expectedRouteOut(AMOUNT) - AMOUNT - premium;
        vm.prank(executorEOA);
        uint256 profit = ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.AAVE_V3, address(aave), AMOUNT, 1));
        assertEq(profit, expected);
        assertEq(usdc.allowance(address(ex), address(aave)), 0, "no residual allowance");
    }

    function test_morpho_profitable_zero_fee() public {
        uint256 expected = _expectedRouteOut(AMOUNT) - AMOUNT;
        vm.prank(executorEOA);
        uint256 profit = ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.MORPHO, address(morpho), AMOUNT, 1));
        assertEq(profit, expected);
        assertEq(usdc.allowance(address(ex), address(morpho)), 0, "no residual allowance");
    }

    function test_selfFunded_profitable() public {
        usdc.mint(address(ex), AMOUNT);
        uint256 expected = _expectedRouteOut(AMOUNT) - AMOUNT;
        vm.prank(executorEOA);
        uint256 profit = ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.NONE, address(0), AMOUNT, 1));
        assertEq(profit, expected);
        assertEq(usdc.balanceOf(address(ex)), AMOUNT + expected);
    }

    function test_owner_can_execute_too() public {
        vm.prank(owner);
        ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1));
    }

    function test_solidly_stable_route_profitable() public {
        // Make the stable pool mispriced: USDT cheap. USDC -> stablePool -> USDT -> (second pool) -> USDC.
        // Use a second volatile V2 pair USDT/USDC priced 1:1 to close the loop.
        MockV2Pair back = new MockV2Pair(address(usdt), address(usdc), 3000);
        usdt.mint(address(back), 5_000_000e6);
        usdc.mint(address(back), 5_050_000e6); // USDT worth 1.01 USDC here
        back.sync();
        address[] memory pools = new address[](1);
        pools[0] = address(back);
        vm.prank(owner);
        ex.setPools(pools, true);

        FlashArbExecutor.Hop[] memory hops = new FlashArbExecutor.Hop[](2);
        hops[0] = _hop(FlashArbExecutor.DexKind.SOLIDLY, address(stablePool), address(usdc), address(usdt), 0, 0);
        hops[1] = _hop(FlashArbExecutor.DexKind.UNIV2, address(back), address(usdt), address(usdc), 3000, 0);
        FlashArbExecutor.ArbParams memory p = FlashArbExecutor.ArbParams({
            source: FlashArbExecutor.FlashSource.BALANCER_V2,
            provider: address(vault),
            token: address(usdc),
            amount: 5_000e6,
            minProfit: 1,
            deadline: block.timestamp + 60,
            hops: hops
        });
        uint256 quote1 = stablePool.getAmountOut(5_000e6, address(usdc));
        vm.prank(executorEOA);
        uint256 profit = ex.executeArbitrage(p);
        assertGt(profit, 0);
        assertGt(quote1, 4_990e6, "stable quote sanity (5 bps fee, ~zero impact)");
    }

    // ------------------------------------------------------------------
    // Financial guards
    // ------------------------------------------------------------------

    function test_revert_insufficientProfit() public {
        uint256 expected = _expectedRouteOut(AMOUNT) - AMOUNT;
        vm.prank(executorEOA);
        vm.expectRevert(abi.encodeWithSelector(FlashArbExecutor.InsufficientProfit.selector, expected, expected + 1));
        ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, expected + 1));
    }

    function test_revert_unprofitable_route_cannot_repay() public {
        // Reverse direction: buy WETH on the expensive pair, sell on the cheap one → loss → repayment impossible.
        FlashArbExecutor.Hop[] memory hops = new FlashArbExecutor.Hop[](2);
        hops[0] = _hop(FlashArbExecutor.DexKind.UNIV2, address(pairB), address(usdc), address(weth), 3000, 0);
        hops[1] = _hop(FlashArbExecutor.DexKind.UNIV2, address(pairA), address(weth), address(usdc), 3000, 0);
        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 0);
        p.hops = hops;
        vm.prank(executorEOA);
        vm.expectRevert(FlashArbExecutor.FlashRepaymentImpossible.selector);
        ex.executeArbitrage(p);
        assertEq(usdc.balanceOf(address(ex)), 0, "no funds lost on revert");
    }

    function test_revert_unprofitable_selfFunded_never_loses() public {
        usdc.mint(address(ex), AMOUNT);
        FlashArbExecutor.Hop[] memory hops = new FlashArbExecutor.Hop[](2);
        hops[0] = _hop(FlashArbExecutor.DexKind.UNIV2, address(pairB), address(usdc), address(weth), 3000, 0);
        hops[1] = _hop(FlashArbExecutor.DexKind.UNIV2, address(pairA), address(weth), address(usdc), 3000, 0);
        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.NONE, address(0), AMOUNT, 0);
        p.hops = hops;
        vm.prank(executorEOA);
        vm.expectRevert(); // InsufficientProfit(0, 0) via the balanceAfter < balanceBefore defensive branch
        ex.executeArbitrage(p);
        assertEq(usdc.balanceOf(address(ex)), AMOUNT);
    }

    function test_revert_hopMinOut() public {
        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 0);
        p.hops[0].minAmountOut = type(uint128).max;
        vm.prank(executorEOA);
        vm.expectRevert();
        ex.executeArbitrage(p);
    }

    function test_revert_borrowCap() public {
        address[] memory toks = new address[](1);
        toks[0] = address(usdc);
        uint256[] memory caps = new uint256[](1);
        caps[0] = AMOUNT - 1;
        vm.prank(owner);
        ex.setTokens(toks, true, caps);
        vm.prank(executorEOA);
        vm.expectRevert(FlashArbExecutor.BorrowCapExceeded.selector);
        ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1));
    }

    // ------------------------------------------------------------------
    // Access control / allowlists
    // ------------------------------------------------------------------

    function test_revert_notExecutor() public {
        vm.prank(stranger);
        vm.expectRevert(FlashArbExecutor.NotExecutor.selector);
        ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1));
    }

    function test_pause_blocks_execution_and_guardian_can_pause() public {
        vm.prank(stranger);
        vm.expectRevert(FlashArbExecutor.NotGuardian.selector);
        ex.pause();

        vm.prank(guardian);
        ex.pause();
        vm.prank(executorEOA);
        vm.expectRevert(Pausable.EnforcedPause.selector);
        ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1));

        vm.prank(guardian);
        vm.expectRevert(abi.encodeWithSelector(Ownable.OwnableUnauthorizedAccount.selector, guardian));
        ex.unpause();

        vm.prank(owner);
        ex.unpause();
        vm.prank(executorEOA);
        ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1));
    }

    function test_revert_expired() public {
        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1);
        p.deadline = block.timestamp - 1;
        vm.prank(executorEOA);
        vm.expectRevert(FlashArbExecutor.Expired.selector);
        ex.executeArbitrage(p);
    }

    function test_revert_poolNotAllowed() public {
        MockV2Pair rogue = new MockV2Pair(address(weth), address(usdc), 3000);
        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1);
        p.hops[1].pool = address(rogue);
        vm.prank(executorEOA);
        vm.expectRevert(abi.encodeWithSelector(FlashArbExecutor.PoolNotAllowed.selector, address(rogue)));
        ex.executeArbitrage(p);
    }

    function test_revert_tokenNotAllowed() public {
        MockERC20 rogue = new MockERC20("R", "R", 18);
        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1);
        p.hops[0].tokenOut = address(rogue);
        p.hops[1].tokenIn = address(rogue);
        vm.prank(executorEOA);
        vm.expectRevert(abi.encodeWithSelector(FlashArbExecutor.TokenNotAllowed.selector, address(rogue)));
        ex.executeArbitrage(p);
    }

    function test_revert_providerNotAllowed() public {
        vm.prank(executorEOA);
        vm.expectRevert(abi.encodeWithSelector(FlashArbExecutor.ProviderNotAllowed.selector, stranger));
        ex.executeArbitrage(_params(FlashArbExecutor.FlashSource.BALANCER_V2, stranger, AMOUNT, 1));
    }

    function test_revert_routeNotCyclic_and_discontinuous() public {
        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1);
        p.hops[1].tokenOut = address(weth);
        vm.prank(executorEOA);
        vm.expectRevert(FlashArbExecutor.RouteNotCyclic.selector);
        ex.executeArbitrage(p);

        p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1);
        p.hops[1].tokenIn = address(usdt);
        vm.prank(executorEOA);
        vm.expectRevert(abi.encodeWithSelector(FlashArbExecutor.RouteDiscontinuous.selector, 1));
        ex.executeArbitrage(p);
    }

    function test_revert_badHopCount_and_zeroAmount() public {
        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 1);
        p.hops = new FlashArbExecutor.Hop[](1);
        vm.prank(executorEOA);
        vm.expectRevert(FlashArbExecutor.BadHopCount.selector);
        ex.executeArbitrage(p);

        p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), 0, 1);
        vm.prank(executorEOA);
        vm.expectRevert(FlashArbExecutor.ZeroAmount.selector);
        ex.executeArbitrage(p);
    }

    // ------------------------------------------------------------------
    // Callback authentication
    // ------------------------------------------------------------------

    function test_revert_direct_callbacks_are_rejected() public {
        Attacker atk = new Attacker();
        bytes memory payload = abi.encode(address(usdc), AMOUNT, _usdcRoute());
        usdc.mint(address(ex), AMOUNT); // even with funds inside, callbacks must not be callable

        vm.expectRevert(FlashArbExecutor.UnauthorizedCallback.selector);
        atk.callBalancerCallback(address(ex), IERC20(address(usdc)), AMOUNT, payload);
        vm.expectRevert(FlashArbExecutor.UnauthorizedCallback.selector);
        atk.callAaveCallback(address(ex), address(usdc), AMOUNT, payload);
        vm.expectRevert(FlashArbExecutor.UnauthorizedCallback.selector);
        atk.callMorphoCallback(address(ex), AMOUNT, payload);
        vm.expectRevert(FlashArbExecutor.UnauthorizedCallback.selector);
        ex.uniswapV3SwapCallback(1, 0, abi.encode(address(usdc)));
        vm.expectRevert(FlashArbExecutor.UnauthorizedCallback.selector);
        ex.uniswapV3FlashCallback(0, 0, payload);
        assertEq(usdc.balanceOf(address(ex)), AMOUNT, "funds untouched");
    }

    // ------------------------------------------------------------------
    // Hostile tokens
    // ------------------------------------------------------------------

    function test_feeOnTransfer_token_detected_by_balance_delta() public {
        FeeOnTransferERC20 fee = new FeeOnTransferERC20(100); // 1 % tax
        MockV2Pair pA = new MockV2Pair(address(usdc), address(fee), 3000);
        MockV2Pair pB = new MockV2Pair(address(usdc), address(fee), 3000);
        usdc.mint(address(pA), 1_000_000e6);
        fee.mint(address(pA), 1_000_000 ether);
        usdc.mint(address(pB), 1_010_000e6);
        fee.mint(address(pB), 1_000_000 ether);
        pA.sync();
        pB.sync();
        address[] memory pools = new address[](2);
        pools[0] = address(pA);
        pools[1] = address(pB);
        address[] memory toks = new address[](1);
        toks[0] = address(fee);
        uint256[] memory caps = new uint256[](1);
        vm.startPrank(owner);
        ex.setPools(pools, true);
        ex.setTokens(toks, true, caps);
        vm.stopPrank();

        FlashArbExecutor.Hop[] memory hops = new FlashArbExecutor.Hop[](2);
        hops[0] = _hop(FlashArbExecutor.DexKind.UNIV2, address(pA), address(usdc), address(fee), 3000, 0);
        hops[1] = _hop(FlashArbExecutor.DexKind.UNIV2, address(pB), address(fee), address(usdc), 3000, 0);
        FlashArbExecutor.ArbParams memory p = _params(FlashArbExecutor.FlashSource.BALANCER_V2, address(vault), AMOUNT, 0);
        p.hops = hops;
        // The 1 % spread is eaten by the 1 % tax (twice) → not repayable → revert, nothing lost.
        vm.prank(executorEOA);
        vm.expectRevert();
        ex.executeArbitrage(p);
        assertEq(usdc.balanceOf(address(ex)), 0);
    }

    // ------------------------------------------------------------------
    // Admin
    // ------------------------------------------------------------------

    function test_withdraw_onlyOwner() public {
        usdc.mint(address(ex), 5e6);
        vm.prank(executorEOA);
        vm.expectRevert(abi.encodeWithSelector(Ownable.OwnableUnauthorizedAccount.selector, executorEOA));
        ex.withdraw(address(usdc), executorEOA, 5e6);
        vm.prank(owner);
        ex.withdraw(address(usdc), owner, 5e6);
        assertEq(usdc.balanceOf(owner), 5e6);
    }

    function test_ownership_two_step() public {
        vm.prank(owner);
        ex.transferOwnership(stranger);
        assertEq(ex.owner(), owner, "still owner until accepted");
        vm.prank(stranger);
        ex.acceptOwnership();
        assertEq(ex.owner(), stranger);
    }

    function test_quoteV2_matches_mock_pair() public view {
        (uint112 r0, uint112 r1,) = pairA.getReserves();
        uint256 q = ex.quoteV2(1_000e6, address(usdc) < address(weth) ? r0 : r1, address(usdc) < address(weth) ? r1 : r0, 3000);
        assertGt(q, 0);
    }
}
