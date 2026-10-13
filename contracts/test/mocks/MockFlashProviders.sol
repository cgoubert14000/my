// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {SafeERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import {
    IBalancerFlashLoanRecipient,
    IAaveFlashLoanSimpleReceiver,
    IMorphoFlashLoanCallback
} from "../../src/interfaces/IFlashLoanProviders.sol";

/// @dev Balancer V2 Vault flash loan semantics: fee (bps, 0 on Balancer), repayment pushed back to vault,
///      balance check after the callback.
contract MockBalancerVault {
    using SafeERC20 for IERC20;

    uint256 public feeBps; // Balancer V2 flash loan fee is 0 (governance could raise it)

    constructor(uint256 _feeBps) {
        feeBps = _feeBps;
    }

    function flashLoan(address recipient, IERC20[] calldata tokens, uint256[] calldata amounts, bytes calldata userData)
        external
    {
        uint256[] memory fees = new uint256[](tokens.length);
        uint256[] memory pre = new uint256[](tokens.length);
        for (uint256 i; i < tokens.length; ++i) {
            pre[i] = tokens[i].balanceOf(address(this));
            fees[i] = (amounts[i] * feeBps) / 10_000;
            tokens[i].safeTransfer(recipient, amounts[i]);
        }
        IBalancerFlashLoanRecipient(recipient).receiveFlashLoan(tokens, amounts, fees, userData);
        for (uint256 i; i < tokens.length; ++i) {
            require(tokens[i].balanceOf(address(this)) >= pre[i] + fees[i], "BAL#528: INSUFFICIENT_FLASH_LOAN_FEE_AMOUNT");
        }
    }
}

/// @dev Aave V3 flashLoanSimple semantics: premium in bps-of-bps (FLASHLOAN_PREMIUM_TOTAL = 5 → 0.05 %),
///      repayment pulled with transferFrom after the callback returns true.
contract MockAavePool {
    using SafeERC20 for IERC20;

    uint128 public FLASHLOAN_PREMIUM_TOTAL; // 5 = 0.05 % (percentMul basis 1e4)

    constructor(uint128 premium) {
        FLASHLOAN_PREMIUM_TOTAL = premium;
    }

    function flashLoanSimple(address receiver, address asset, uint256 amount, bytes calldata params, uint16) external {
        uint256 premium = (amount * FLASHLOAN_PREMIUM_TOTAL + 5_000) / 10_000; // PercentageMath.percentMul (half-up)
        IERC20(asset).safeTransfer(receiver, amount);
        require(
            IAaveFlashLoanSimpleReceiver(receiver).executeOperation(asset, amount, premium, msg.sender, params),
            "Aave: INVALID_FLASHLOAN_EXECUTOR_RETURN"
        );
        IERC20(asset).safeTransferFrom(receiver, address(this), amount + premium);
    }
}

/// @dev Morpho Blue flash loan: zero fee, repayment pulled with transferFrom.
contract MockMorpho {
    using SafeERC20 for IERC20;

    function flashLoan(address token, uint256 assets, bytes calldata data) external {
        IERC20(token).safeTransfer(msg.sender, assets);
        IMorphoFlashLoanCallback(msg.sender).onMorphoFlashLoan(assets, data);
        IERC20(token).safeTransferFrom(msg.sender, address(this), assets);
    }
}

/// @dev A hostile contract that tries to call executor callbacks directly / re-enter.
contract Attacker {
    function callBalancerCallback(address target, IERC20 token, uint256 amount, bytes calldata data) external {
        IERC20[] memory tokens = new IERC20[](1);
        tokens[0] = token;
        uint256[] memory amounts = new uint256[](1);
        amounts[0] = amount;
        uint256[] memory fees = new uint256[](1);
        IBalancerFlashLoanRecipient(target).receiveFlashLoan(tokens, amounts, fees, data);
    }

    function callAaveCallback(address target, address asset, uint256 amount, bytes calldata data) external {
        IAaveFlashLoanSimpleReceiver(target).executeOperation(asset, amount, 0, target, data);
    }

    function callMorphoCallback(address target, uint256 amount, bytes calldata data) external {
        IMorphoFlashLoanCallback(target).onMorphoFlashLoan(amount, data);
    }
}
