// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {SafeERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import {Ownable2Step, Ownable} from "@openzeppelin/contracts/access/Ownable2Step.sol";
import {Pausable} from "@openzeppelin/contracts/utils/Pausable.sol";
import {ReentrancyGuardTransient} from "@openzeppelin/contracts/utils/ReentrancyGuardTransient.sol";

import {
    IBalancerV2Vault,
    IBalancerFlashLoanRecipient,
    IAaveV3Pool,
    IAaveFlashLoanSimpleReceiver,
    IMorphoBlue,
    IMorphoFlashLoanCallback,
    IUniswapV3PoolFlash,
    IUniswapV3FlashCallback
} from "./interfaces/IFlashLoanProviders.sol";
import {
    IUniswapV2Pair,
    IUniswapV3Pool,
    IUniswapV3SwapCallback,
    IPancakeV3SwapCallback,
    ISolidlyPool
} from "./interfaces/IDexPools.sol";

/// @title FlashArbExecutor
/// @notice Atomic flash-loan arbitrage executor with strict allowlists, authenticated callbacks, and an
///         on-chain net-profit guard. Every revert path makes the whole transaction fail: the contract can
///         never end a successful transaction with fewer `token` than it started with.
/// @dev Security model
///      - owner  (cold key): allowlists, executors, guardian, pause, withdrawals. Two-step transfer.
///      - executor (hot key, held by the signer service): can only call `executeArbitrage`.
///      - guardian: can only `pause`.
///      - Flash-loan callbacks are accepted only from the provider recorded in transient storage for the
///        current call, and only if the payload hash matches. Swap callbacks are accepted only from the
///        pool recorded in transient storage for the current hop.
///      - No standing allowances: approvals are granted for the exact owed amount and only to the provider.
///      - Hop outputs are measured by balance deltas (fee-on-transfer / malicious tokens cannot inflate them).
contract FlashArbExecutor is
    Ownable2Step,
    Pausable,
    ReentrancyGuardTransient,
    IBalancerFlashLoanRecipient,
    IAaveFlashLoanSimpleReceiver,
    IMorphoFlashLoanCallback,
    IUniswapV3FlashCallback,
    IUniswapV3SwapCallback,
    IPancakeV3SwapCallback
{
    using SafeERC20 for IERC20;

    // ------------------------------------------------------------------
    // Types
    // ------------------------------------------------------------------

    enum FlashSource {
        NONE, // self-funded (uses the contract's own balance)
        BALANCER_V2,
        AAVE_V3,
        MORPHO,
        UNISWAP_V3
    }

    enum DexKind {
        UNIV2, // Uniswap V2 / SushiSwap / PancakeSwap V2 / BaseSwap ...
        UNIV3, // Uniswap V3 / SushiSwap V3 / Aerodrome Slipstream (uniswapV3SwapCallback)
        SOLIDLY, // Aerodrome / Velodrome V2 (stable + volatile)
        PANCAKE_V3 // PancakeSwap V3 (pancakeV3SwapCallback)
    }

    struct Hop {
        DexKind kind;
        address pool;
        address tokenIn;
        address tokenOut;
        /// @dev UNIV2 only: LP fee in parts-per-million (3000 = 0.30 %, 2500 = 0.25 %). Ignored otherwise.
        uint32 feePpm;
        /// @dev Minimum output of this hop (0 = no per-hop check; the final profit check always applies).
        uint256 minAmountOut;
    }

    struct ArbParams {
        FlashSource source;
        address provider; // Balancer vault / Aave pool / Morpho / Uniswap V3 pool; ignored for NONE
        address token; // borrowed token; must open and close the route
        uint256 amount; // borrowed amount
        uint256 minProfit; // required net gain in `token` units (after flash fee)
        uint256 deadline; // unix timestamp
        Hop[] hops;
    }

    // ------------------------------------------------------------------
    // Constants / storage
    // ------------------------------------------------------------------

    uint256 public constant MAX_HOPS = 4;
    uint32 public constant PPM = 1_000_000;
    uint160 internal constant MIN_SQRT_RATIO = 4295128739;
    uint160 internal constant MAX_SQRT_RATIO = 1461446703485210103287273052203988822378723970342;

    mapping(address => bool) public isExecutor;
    address public guardian;

    mapping(address => bool) public allowedTokens;
    mapping(address => bool) public allowedPools;
    mapping(address => bool) public allowedProviders;
    /// @dev Optional per-token borrow cap (0 = no cap).
    mapping(address => uint256) public borrowCap;

    uint256 public totalExecutions;

    // Transient (per-transaction) state used to authenticate callbacks.
    address private transient _pendingProvider;
    bytes32 private transient _pendingHash;
    address private transient _expectedSwapPool;

    // ------------------------------------------------------------------
    // Events / errors
    // ------------------------------------------------------------------

    event ArbitrageExecuted(
        address indexed executor, address indexed token, FlashSource source, uint256 amount, uint256 profit, uint256 hops
    );
    event ExecutorSet(address indexed account, bool allowed);
    event GuardianSet(address indexed account);
    event TokenAllowed(address indexed token, bool allowed, uint256 cap);
    event PoolAllowed(address indexed pool, bool allowed);
    event ProviderAllowed(address indexed provider, bool allowed);
    event Withdrawn(address indexed token, address indexed to, uint256 amount);

    error NotExecutor();
    error NotGuardian();
    error Expired();
    error BadHopCount();
    error TokenNotAllowed(address token);
    error PoolNotAllowed(address pool);
    error ProviderNotAllowed(address provider);
    error RouteNotCyclic();
    error RouteDiscontinuous(uint256 index);
    error BorrowCapExceeded();
    error InsufficientProfit(uint256 profit, uint256 minProfit);
    error InsufficientSelfFunds();
    error UnauthorizedCallback();
    error BadCallbackPayload();
    error HopOutputTooLow(uint256 index, uint256 got, uint256 min);
    error ZeroAmount();
    error BadFee();
    error FlashRepaymentImpossible();

    // ------------------------------------------------------------------
    // Construction / admin
    // ------------------------------------------------------------------

    constructor(address initialOwner, address initialExecutor) Ownable(initialOwner) {
        if (initialExecutor != address(0)) {
            isExecutor[initialExecutor] = true;
            emit ExecutorSet(initialExecutor, true);
        }
    }

    modifier onlyExecutor() {
        if (!isExecutor[msg.sender] && msg.sender != owner()) revert NotExecutor();
        _;
    }

    function setExecutor(address account, bool allowed) external onlyOwner {
        isExecutor[account] = allowed;
        emit ExecutorSet(account, allowed);
    }

    function setGuardian(address account) external onlyOwner {
        guardian = account;
        emit GuardianSet(account);
    }

    function setTokens(address[] calldata tokens, bool allowed, uint256[] calldata caps) external onlyOwner {
        for (uint256 i; i < tokens.length; ++i) {
            allowedTokens[tokens[i]] = allowed;
            uint256 cap = caps.length > i ? caps[i] : 0;
            borrowCap[tokens[i]] = allowed ? cap : 0;
            emit TokenAllowed(tokens[i], allowed, cap);
        }
    }

    function setPools(address[] calldata pools, bool allowed) external onlyOwner {
        for (uint256 i; i < pools.length; ++i) {
            allowedPools[pools[i]] = allowed;
            emit PoolAllowed(pools[i], allowed);
        }
    }

    function setProviders(address[] calldata providers, bool allowed) external onlyOwner {
        for (uint256 i; i < providers.length; ++i) {
            allowedProviders[providers[i]] = allowed;
            emit ProviderAllowed(providers[i], allowed);
        }
    }

    /// @notice Emergency stop. Guardian or owner.
    function pause() external {
        if (msg.sender != guardian && msg.sender != owner()) revert NotGuardian();
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    /// @notice Withdraw profits (or rescue any token). Owner only.
    function withdraw(address token, address to, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(to, amount);
        emit Withdrawn(token, to, amount);
    }

    // ------------------------------------------------------------------
    // Entry point
    // ------------------------------------------------------------------

    /// @notice Execute an atomic arbitrage. Reverts unless net profit >= minProfit.
    /// @dev Can be simulated with eth_call (optionally with state overrides) to obtain the exact profit.
    function executeArbitrage(ArbParams calldata p)
        external
        onlyExecutor
        whenNotPaused
        nonReentrant
        returns (uint256 profit)
    {
        _validate(p);

        IERC20 token = IERC20(p.token);
        uint256 balanceBefore = token.balanceOf(address(this));

        if (p.source == FlashSource.NONE) {
            if (balanceBefore < p.amount) revert InsufficientSelfFunds();
            _runRoute(p.hops, p.amount);
        } else {
            bytes memory payload = abi.encode(p.token, p.amount, p.hops);
            _pendingProvider = p.provider;
            _pendingHash = keccak256(payload);
            _startFlashLoan(p, payload);
            _pendingProvider = address(0);
            _pendingHash = bytes32(0);
        }

        uint256 balanceAfter = token.balanceOf(address(this));
        if (balanceAfter < balanceBefore) revert InsufficientProfit(0, p.minProfit); // defensive: should be unreachable
        profit = balanceAfter - balanceBefore;
        if (profit < p.minProfit) revert InsufficientProfit(profit, p.minProfit);

        unchecked {
            ++totalExecutions;
        }
        emit ArbitrageExecuted(msg.sender, p.token, p.source, p.amount, profit, p.hops.length);
    }

    // ------------------------------------------------------------------
    // Validation
    // ------------------------------------------------------------------

    function _validate(ArbParams calldata p) internal view {
        // forge-lint: disable-next-line(block-timestamp)
        if (block.timestamp > p.deadline) revert Expired();
        if (p.amount == 0) revert ZeroAmount();
        uint256 n = p.hops.length;
        if (n < 2 || n > MAX_HOPS) revert BadHopCount();
        if (!allowedTokens[p.token]) revert TokenNotAllowed(p.token);
        uint256 cap = borrowCap[p.token];
        if (cap != 0 && p.amount > cap) revert BorrowCapExceeded();
        if (p.source != FlashSource.NONE && !allowedProviders[p.provider]) revert ProviderNotAllowed(p.provider);
        if (p.hops[0].tokenIn != p.token || p.hops[n - 1].tokenOut != p.token) revert RouteNotCyclic();
        for (uint256 i; i < n; ++i) {
            Hop calldata h = p.hops[i];
            if (!allowedPools[h.pool]) revert PoolNotAllowed(h.pool);
            if (!allowedTokens[h.tokenIn]) revert TokenNotAllowed(h.tokenIn);
            if (!allowedTokens[h.tokenOut]) revert TokenNotAllowed(h.tokenOut);
            if (i > 0 && p.hops[i - 1].tokenOut != h.tokenIn) revert RouteDiscontinuous(i);
            if (h.kind == DexKind.UNIV2 && h.feePpm >= PPM) revert BadFee();
        }
    }

    // ------------------------------------------------------------------
    // Flash loan dispatch + callbacks
    // ------------------------------------------------------------------

    function _startFlashLoan(ArbParams calldata p, bytes memory payload) internal {
        if (p.source == FlashSource.BALANCER_V2) {
            IERC20[] memory tokens = new IERC20[](1);
            tokens[0] = IERC20(p.token);
            uint256[] memory amounts = new uint256[](1);
            amounts[0] = p.amount;
            IBalancerV2Vault(p.provider).flashLoan(address(this), tokens, amounts, payload);
        } else if (p.source == FlashSource.AAVE_V3) {
            IAaveV3Pool(p.provider).flashLoanSimple(address(this), p.token, p.amount, payload, 0);
        } else if (p.source == FlashSource.MORPHO) {
            IMorphoBlue(p.provider).flashLoan(p.token, p.amount, payload);
        } else if (p.source == FlashSource.UNISWAP_V3) {
            IUniswapV3PoolFlash pool = IUniswapV3PoolFlash(p.provider);
            bool isToken0 = pool.token0() == p.token;
            if (!isToken0 && pool.token1() != p.token) revert RouteNotCyclic();
            pool.flash(address(this), isToken0 ? p.amount : 0, isToken0 ? 0 : p.amount, payload);
        } else {
            revert ProviderNotAllowed(p.provider);
        }
    }

    /// @dev Shared callback authentication: sender must be the pending provider and payload must match.
    function _authenticateFlashCallback(bytes calldata payload)
        internal
        view
        returns (address token, uint256 amount, Hop[] memory hops)
    {
        if (msg.sender == address(0) || msg.sender != _pendingProvider) revert UnauthorizedCallback();
        if (keccak256(payload) != _pendingHash) revert BadCallbackPayload();
        (token, amount, hops) = abi.decode(payload, (address, uint256, Hop[]));
    }

    /// @inheritdoc IBalancerFlashLoanRecipient
    function receiveFlashLoan(
        IERC20[] calldata tokens,
        uint256[] calldata amounts,
        uint256[] calldata feeAmounts,
        bytes calldata userData
    ) external override {
        (address token, uint256 amount, Hop[] memory hops) = _authenticateFlashCallback(userData);
        if (tokens.length != 1 || address(tokens[0]) != token || amounts[0] != amount) revert BadCallbackPayload();
        _runRoute(hops, amount);
        uint256 owed = amount + feeAmounts[0];
        if (IERC20(token).balanceOf(address(this)) < owed) revert FlashRepaymentImpossible();
        IERC20(token).safeTransfer(msg.sender, owed); // Balancer: push repayment
    }

    /// @inheritdoc IAaveFlashLoanSimpleReceiver
    function executeOperation(address asset, uint256 amount, uint256 premium, address initiator, bytes calldata params)
        external
        override
        returns (bool)
    {
        (address token, uint256 amt, Hop[] memory hops) = _authenticateFlashCallback(params);
        if (initiator != address(this) || asset != token || amount != amt) revert BadCallbackPayload();
        _runRoute(hops, amount);
        uint256 owed = amount + premium;
        if (IERC20(token).balanceOf(address(this)) < owed) revert FlashRepaymentImpossible();
        IERC20(token).forceApprove(msg.sender, owed); // Aave: pull repayment
        return true;
    }

    /// @inheritdoc IMorphoFlashLoanCallback
    function onMorphoFlashLoan(uint256 assets, bytes calldata data) external override {
        (address token, uint256 amount, Hop[] memory hops) = _authenticateFlashCallback(data);
        if (assets != amount) revert BadCallbackPayload();
        _runRoute(hops, amount);
        if (IERC20(token).balanceOf(address(this)) < assets) revert FlashRepaymentImpossible();
        IERC20(token).forceApprove(msg.sender, assets); // Morpho: pull repayment, zero fee
    }

    /// @inheritdoc IUniswapV3FlashCallback
    function uniswapV3FlashCallback(uint256 fee0, uint256 fee1, bytes calldata data) external override {
        (address token, uint256 amount, Hop[] memory hops) = _authenticateFlashCallback(data);
        _runRoute(hops, amount);
        bool isToken0 = IUniswapV3PoolFlash(msg.sender).token0() == token;
        uint256 owed = amount + (isToken0 ? fee0 : fee1);
        if (IERC20(token).balanceOf(address(this)) < owed) revert FlashRepaymentImpossible();
        IERC20(token).safeTransfer(msg.sender, owed); // Uniswap V3: push repayment
    }

    // ------------------------------------------------------------------
    // Route execution
    // ------------------------------------------------------------------

    function _runRoute(Hop[] memory hops, uint256 amountIn) internal returns (uint256 amount) {
        amount = amountIn;
        for (uint256 i; i < hops.length; ++i) {
            Hop memory h = hops[i];
            IERC20 out = IERC20(h.tokenOut);
            uint256 before = out.balanceOf(address(this));
            if (h.kind == DexKind.UNIV2) {
                _swapV2(h, amount);
            } else if (h.kind == DexKind.SOLIDLY) {
                _swapSolidly(h, amount);
            } else {
                _swapV3(h, amount);
            }
            uint256 received = out.balanceOf(address(this)) - before;
            if (received < h.minAmountOut || received == 0) revert HopOutputTooLow(i, received, h.minAmountOut);
            amount = received;
        }
    }

    function _swapV2(Hop memory h, uint256 amountIn) internal {
        IUniswapV2Pair pair = IUniswapV2Pair(h.pool);
        (uint112 r0, uint112 r1,) = pair.getReserves();
        bool zeroForOne = h.tokenIn == pair.token0();
        (uint256 rIn, uint256 rOut) = zeroForOne ? (uint256(r0), uint256(r1)) : (uint256(r1), uint256(r0));
        uint256 amountInWithFee = amountIn * (PPM - h.feePpm);
        uint256 amountOut = (amountInWithFee * rOut) / (rIn * PPM + amountInWithFee);
        IERC20(h.tokenIn).safeTransfer(h.pool, amountIn);
        pair.swap(zeroForOne ? 0 : amountOut, zeroForOne ? amountOut : 0, address(this), "");
    }

    function _swapSolidly(Hop memory h, uint256 amountIn) internal {
        ISolidlyPool pool = ISolidlyPool(h.pool);
        uint256 amountOut = pool.getAmountOut(amountIn, h.tokenIn);
        bool zeroForOne = h.tokenIn == pool.token0();
        IERC20(h.tokenIn).safeTransfer(h.pool, amountIn);
        pool.swap(zeroForOne ? 0 : amountOut, zeroForOne ? amountOut : 0, address(this), "");
    }

    function _swapV3(Hop memory h, uint256 amountIn) internal {
        IUniswapV3Pool pool = IUniswapV3Pool(h.pool);
        bool zeroForOne = h.tokenIn == pool.token0();
        if (amountIn > uint256(type(int256).max)) revert ZeroAmount();
        _expectedSwapPool = h.pool;
        pool.swap(
            address(this),
            zeroForOne,
            // forge-lint: disable-next-line(unsafe-typecast)
            int256(amountIn),
            zeroForOne ? MIN_SQRT_RATIO + 1 : MAX_SQRT_RATIO - 1,
            abi.encode(h.tokenIn)
        );
        _expectedSwapPool = address(0);
    }

    function _onV3SwapCallback(int256 amount0Delta, int256 amount1Delta, bytes calldata data) internal {
        if (msg.sender == address(0) || msg.sender != _expectedSwapPool) revert UnauthorizedCallback();
        address tokenIn = abi.decode(data, (address));
        if (amount0Delta <= 0 && amount1Delta <= 0) revert BadCallbackPayload();
        // forge-lint: disable-next-line(unsafe-typecast)
        uint256 owed = amount0Delta > 0 ? uint256(amount0Delta) : uint256(amount1Delta);
        IERC20(tokenIn).safeTransfer(msg.sender, owed);
    }

    /// @inheritdoc IUniswapV3SwapCallback
    function uniswapV3SwapCallback(int256 amount0Delta, int256 amount1Delta, bytes calldata data) external override {
        _onV3SwapCallback(amount0Delta, amount1Delta, data);
    }

    /// @inheritdoc IPancakeV3SwapCallback
    function pancakeV3SwapCallback(int256 amount0Delta, int256 amount1Delta, bytes calldata data) external override {
        _onV3SwapCallback(amount0Delta, amount1Delta, data);
    }

    // ------------------------------------------------------------------
    // Views
    // ------------------------------------------------------------------

    /// @notice Pure helper mirroring the on-chain V2 formula (used by tests and off-chain cross-checks).
    function quoteV2(uint256 amountIn, uint256 reserveIn, uint256 reserveOut, uint32 feePpm)
        external
        pure
        returns (uint256)
    {
        uint256 amountInWithFee = amountIn * (PPM - feePpm);
        return (amountInWithFee * reserveOut) / (reserveIn * PPM + amountInWithFee);
    }
}
