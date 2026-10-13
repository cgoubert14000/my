// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {SafeERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

interface IUniswapV3PoolFull {
    function initialize(uint160 sqrtPriceX96) external;
    function mint(address recipient, int24 tickLower, int24 tickUpper, uint128 amount, bytes calldata data)
        external
        returns (uint256 amount0, uint256 amount1);
    function swap(address recipient, bool zeroForOne, int256 amountSpecified, uint160 sqrtPriceLimitX96, bytes calldata data)
        external
        returns (int256 amount0, int256 amount1);
    function slot0()
        external
        view
        returns (uint160 sqrtPriceX96, int24 tick, uint16, uint16, uint16, uint8, bool);
    function liquidity() external view returns (uint128);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

interface IUniswapV3FactoryLike {
    function createPool(address tokenA, address tokenB, uint24 fee) external returns (address pool);
    function getPool(address, address, uint24) external view returns (address);
}

/// @dev Minimal LP + trader helper for the real Uniswap V3 pool bytecode (mint & swap callbacks).
contract V3Helper {
    using SafeERC20 for IERC20;

    address internal _pool;

    function mint(address pool, int24 lower, int24 upper, uint128 liquidity) external returns (uint256, uint256) {
        _pool = pool;
        (uint256 a0, uint256 a1) = IUniswapV3PoolFull(pool).mint(address(this), lower, upper, liquidity, "");
        _pool = address(0);
        return (a0, a1);
    }

    function swapExactIn(address pool, bool zeroForOne, uint256 amountIn) external returns (uint256 amountOut) {
        _pool = pool;
        (int256 a0, int256 a1) = IUniswapV3PoolFull(pool).swap(
            address(this),
            zeroForOne,
            int256(amountIn),
            zeroForOne ? 4295128739 + 1 : 1461446703485210103287273052203988822378723970342 - 1,
            ""
        );
        _pool = address(0);
        amountOut = uint256(-(zeroForOne ? a1 : a0));
    }

    function uniswapV3MintCallback(uint256 amount0Owed, uint256 amount1Owed, bytes calldata) external {
        require(msg.sender == _pool, "bad pool");
        if (amount0Owed > 0) IERC20(IUniswapV3PoolFull(msg.sender).token0()).safeTransfer(msg.sender, amount0Owed);
        if (amount1Owed > 0) IERC20(IUniswapV3PoolFull(msg.sender).token1()).safeTransfer(msg.sender, amount1Owed);
    }

    function uniswapV3SwapCallback(int256 amount0Delta, int256 amount1Delta, bytes calldata) external {
        require(msg.sender == _pool, "bad pool");
        if (amount0Delta > 0) IERC20(IUniswapV3PoolFull(msg.sender).token0()).safeTransfer(msg.sender, uint256(amount0Delta));
        if (amount1Delta > 0) IERC20(IUniswapV3PoolFull(msg.sender).token1()).safeTransfer(msg.sender, uint256(amount1Delta));
    }
}

library Sqrt {
    function sqrt(uint256 x) internal pure returns (uint256 y) {
        if (x == 0) return 0;
        uint256 z = (x + 1) / 2;
        y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
    }
}
