// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @dev Uniswap V2 style pair (Uniswap V2, SushiSwap, PancakeSwap V2, BaseSwap ...).
interface IUniswapV2Pair {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function swap(uint256 amount0Out, uint256 amount1Out, address to, bytes calldata data) external;
}

/// @dev Uniswap V3 style pool (Uniswap V3, PancakeSwap V3, SushiSwap V3, Aerodrome Slipstream*).
///      *Slipstream uses the same swap/callback shape but a different callback name is NOT used: it keeps
///      uniswapV3SwapCallback. Fee is read off-chain.
interface IUniswapV3Pool {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function fee() external view returns (uint24);
    function swap(address recipient, bool zeroForOne, int256 amountSpecified, uint160 sqrtPriceLimitX96, bytes calldata data)
        external
        returns (int256 amount0, int256 amount1);
}

interface IUniswapV3SwapCallback {
    function uniswapV3SwapCallback(int256 amount0Delta, int256 amount1Delta, bytes calldata data) external;
}

/// @dev PancakeSwap V3 uses a differently named callback.
interface IPancakeV3SwapCallback {
    function pancakeV3SwapCallback(int256 amount0Delta, int256 amount1Delta, bytes calldata data) external;
}

/// @dev Solidly style pool (Aerodrome / Velodrome V2). Same low-level swap as V2, plus an exact on-chain quote.
interface ISolidlyPool {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function stable() external view returns (bool);
    function getAmountOut(uint256 amountIn, address tokenIn) external view returns (uint256);
    function swap(uint256 amount0Out, uint256 amount1Out, address to, bytes calldata data) external;
}
