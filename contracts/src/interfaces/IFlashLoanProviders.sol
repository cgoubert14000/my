// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/// @dev Balancer V2 Vault flash loan surface (same Vault address on every chain: 0xBA12...F2C8).
interface IBalancerV2Vault {
    function flashLoan(address recipient, IERC20[] calldata tokens, uint256[] calldata amounts, bytes calldata userData)
        external;
}

interface IBalancerFlashLoanRecipient {
    function receiveFlashLoan(
        IERC20[] calldata tokens,
        uint256[] calldata amounts,
        uint256[] calldata feeAmounts,
        bytes calldata userData
    ) external;
}

/// @dev Aave V3 Pool flash loan surface.
interface IAaveV3Pool {
    function flashLoanSimple(address receiverAddress, address asset, uint256 amount, bytes calldata params, uint16 referralCode)
        external;
    function FLASHLOAN_PREMIUM_TOTAL() external view returns (uint128);
}

interface IAaveFlashLoanSimpleReceiver {
    function executeOperation(address asset, uint256 amount, uint256 premium, address initiator, bytes calldata params)
        external
        returns (bool);
}

/// @dev Morpho Blue flash loan surface (0 fee; repayment pulled with transferFrom).
interface IMorphoBlue {
    function flashLoan(address token, uint256 assets, bytes calldata data) external;
}

interface IMorphoFlashLoanCallback {
    function onMorphoFlashLoan(uint256 assets, bytes calldata data) external;
}

/// @dev Uniswap V3 pool flash surface (fee = pool fee tier, repayment pushed).
interface IUniswapV3PoolFlash {
    function flash(address recipient, uint256 amount0, uint256 amount1, bytes calldata data) external;
    function token0() external view returns (address);
    function token1() external view returns (address);
}

interface IUniswapV3FlashCallback {
    function uniswapV3FlashCallback(uint256 fee0, uint256 fee1, bytes calldata data) external;
}
