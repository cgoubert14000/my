// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import {Test} from "forge-std/Test.sol";
import {BaseTest} from "./Base.t.sol";
import {FlashArbExecutor} from "../src/FlashArbExecutor.sol";
import {MockERC20} from "./mocks/MockERC20.sol";
import {MockV2Pair} from "./mocks/MockV2Pair.sol";
import {MockBalancerVault, MockAavePool, MockMorpho} from "./mocks/MockFlashProviders.sol";

/// @dev Random sequences of (profitable | unprofitable | forged) executions, pauses and allowlist edits.
contract Handler is Test {
    FlashArbExecutor public ex;
    MockERC20 public usdc;
    MockERC20 public weth;
    MockV2Pair public pairA;
    MockV2Pair public pairB;
    MockBalancerVault public vault;
    MockAavePool public aave;
    MockMorpho public morpho;
    address public owner;
    address public executorEOA;

    uint256 public successes;
    uint256 public failures;
    uint256 public sumProfits;

    constructor(
        FlashArbExecutor _ex,
        MockERC20 _usdc,
        MockERC20 _weth,
        MockV2Pair _a,
        MockV2Pair _b,
        MockBalancerVault _v,
        MockAavePool _aave,
        MockMorpho _m,
        address _owner,
        address _exec
    ) {
        ex = _ex;
        usdc = _usdc;
        weth = _weth;
        pairA = _a;
        pairB = _b;
        vault = _v;
        aave = _aave;
        morpho = _m;
        owner = _owner;
        executorEOA = _exec;
    }

    function _route(bool forward) internal view returns (FlashArbExecutor.Hop[] memory hops) {
        hops = new FlashArbExecutor.Hop[](2);
        (address p1, address p2) = forward ? (address(pairA), address(pairB)) : (address(pairB), address(pairA));
        hops[0] = FlashArbExecutor.Hop(FlashArbExecutor.DexKind.UNIV2, p1, address(usdc), address(weth), 3000, 0);
        hops[1] = FlashArbExecutor.Hop(FlashArbExecutor.DexKind.UNIV2, p2, address(weth), address(usdc), 3000, 0);
    }

    function arb(uint256 amount, uint8 src, bool forward, uint256 minProfit) external {
        amount = bound(amount, 1e6, 200_000e6);
        minProfit = bound(minProfit, 0, 1_000e6);
        FlashArbExecutor.FlashSource source = FlashArbExecutor.FlashSource(bound(src, 1, 3));
        address provider = source == FlashArbExecutor.FlashSource.BALANCER_V2
            ? address(vault)
            : source == FlashArbExecutor.FlashSource.AAVE_V3 ? address(aave) : address(morpho);
        FlashArbExecutor.ArbParams memory p = FlashArbExecutor.ArbParams({
            source: source,
            provider: provider,
            token: address(usdc),
            amount: amount,
            minProfit: minProfit,
            deadline: block.timestamp + 1,
            hops: _route(forward)
        });
        uint256 before = usdc.balanceOf(address(ex));
        vm.prank(executorEOA);
        try ex.executeArbitrage(p) returns (uint256 profit) {
            successes++;
            sumProfits += profit;
            require(usdc.balanceOf(address(ex)) == before + profit, "accounting");
            require(profit >= minProfit, "minProfit");
        } catch {
            failures++;
            require(usdc.balanceOf(address(ex)) == before, "loss on revert");
        }
    }

    function trade_against_pools(uint256 amount, bool buyWeth) external {
        // A third party moves the price on pair A, creating / destroying opportunities.
        amount = bound(amount, 1e6, 100_000e6);
        if (buyWeth) {
            (uint112 r0, uint112 r1,) = pairA.getReserves();
            bool usdcIs0 = address(usdc) < address(weth);
            (uint256 rIn, uint256 rOut) = usdcIs0 ? (uint256(r0), uint256(r1)) : (uint256(r1), uint256(r0));
            uint256 out = ex.quoteV2(amount, rIn, rOut, 3000);
            if (out == 0) return;
            usdc.mint(address(pairA), amount);
            pairA.swap(usdcIs0 ? 0 : out, usdcIs0 ? out : 0, address(this), "");
        } else {
            uint256 wamt = amount * 1e12 / 2000;
            (uint112 r0, uint112 r1,) = pairA.getReserves();
            bool usdcIs0 = address(usdc) < address(weth);
            (uint256 rIn, uint256 rOut) = usdcIs0 ? (uint256(r1), uint256(r0)) : (uint256(r0), uint256(r1));
            uint256 out = ex.quoteV2(wamt, rIn, rOut, 3000);
            if (out == 0) return;
            weth.mint(address(pairA), wamt);
            pairA.swap(usdcIs0 ? out : 0, usdcIs0 ? 0 : out, address(this), "");
        }
    }

    function togglePause(bool on) external {
        vm.prank(owner);
        if (on && !ex.paused()) ex.pause();
        if (!on && ex.paused()) ex.unpause();
    }

    function forgeCallback(uint256 amount) external {
        bytes memory payload = abi.encode(address(usdc), amount, _route(true));
        try ex.onMorphoFlashLoan(amount, payload) {
            revert("forged callback accepted");
        } catch {}
    }
}

contract InvariantTest is BaseTest {
    Handler handler;

    function setUp() public override {
        super.setUp();
        handler = new Handler(ex, usdc, weth, pairA, pairB, vault, aave, morpho, owner, executorEOA);
        targetContract(address(handler));
    }

    /// @dev The executor's borrowed-token balance can only grow: sum of profits == balance.
    function invariant_balance_equals_sum_of_profits() public view {
        assertEq(usdc.balanceOf(address(ex)), handler.sumProfits());
    }

    function invariant_no_residual_allowances() public view {
        assertEq(usdc.allowance(address(ex), address(aave)), 0);
        assertEq(usdc.allowance(address(ex), address(morpho)), 0);
        assertEq(usdc.allowance(address(ex), address(vault)), 0);
    }

    function invariant_owner_and_executor_unchanged() public view {
        assertEq(ex.owner(), owner);
        assertTrue(ex.isExecutor(executorEOA));
    }

    function invariant_execution_counter_matches() public view {
        assertEq(ex.totalExecutions(), handler.successes());
    }
}
