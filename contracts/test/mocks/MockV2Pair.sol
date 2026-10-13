// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {SafeERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/// @dev Faithful re-implementation of the UniswapV2Pair swap invariant check (K with configurable fee),
///      without LP tokens. Used for unit/fuzz tests; the devnet uses the real Uniswap bytecode instead.
contract MockV2Pair {
    using SafeERC20 for IERC20;

    address public immutable token0;
    address public immutable token1;
    uint32 public immutable feePpm; // 3000 = 0.3 %

    uint112 private reserve0;
    uint112 private reserve1;
    uint32 private blockTimestampLast;

    constructor(address a, address b, uint32 _feePpm) {
        (token0, token1) = a < b ? (a, b) : (b, a);
        feePpm = _feePpm;
    }

    function getReserves() external view returns (uint112, uint112, uint32) {
        return (reserve0, reserve1, blockTimestampLast);
    }

    function sync() public {
        reserve0 = uint112(IERC20(token0).balanceOf(address(this)));
        reserve1 = uint112(IERC20(token1).balanceOf(address(this)));
        blockTimestampLast = uint32(block.timestamp);
    }

    function swap(uint256 amount0Out, uint256 amount1Out, address to, bytes calldata) external {
        require(amount0Out > 0 || amount1Out > 0, "V2: INSUFFICIENT_OUTPUT_AMOUNT");
        (uint112 _r0, uint112 _r1) = (reserve0, reserve1);
        require(amount0Out < _r0 && amount1Out < _r1, "V2: INSUFFICIENT_LIQUIDITY");
        if (amount0Out > 0) IERC20(token0).safeTransfer(to, amount0Out);
        if (amount1Out > 0) IERC20(token1).safeTransfer(to, amount1Out);
        uint256 balance0 = IERC20(token0).balanceOf(address(this));
        uint256 balance1 = IERC20(token1).balanceOf(address(this));
        uint256 amount0In = balance0 > _r0 - amount0Out ? balance0 - (_r0 - amount0Out) : 0;
        uint256 amount1In = balance1 > _r1 - amount1Out ? balance1 - (_r1 - amount1Out) : 0;
        require(amount0In > 0 || amount1In > 0, "V2: INSUFFICIENT_INPUT_AMOUNT");
        uint256 b0Adj = balance0 * 1_000_000 - amount0In * feePpm;
        uint256 b1Adj = balance1 * 1_000_000 - amount1In * feePpm;
        require(b0Adj * b1Adj >= uint256(_r0) * _r1 * 1_000_000 ** 2, "V2: K");
        reserve0 = uint112(balance0);
        reserve1 = uint112(balance1);
        blockTimestampLast = uint32(block.timestamp);
    }
}
