// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import {Script, console} from "forge-std/Script.sol";
import {FlashArbExecutor} from "../src/FlashArbExecutor.sol";

/// @notice Deploys FlashArbExecutor. NEVER run against mainnet before the full test suite and the
///         lab/ghost validation have passed (see docs/06_first_real_test_procedure.md).
///
/// Usage (local devnet):
///   forge script script/Deploy.s.sol --rpc-url http://127.0.0.1:8545 --broadcast \
///       --private-key $DEPLOYER_KEY --sig "run(address,address)" $OWNER $EXECUTOR
///
/// Usage (Base / Arbitrum): same, with --rpc-url $RPC_URL and a hardware-wallet / keystore signer
///   (forge supports --ledger, --trezor, --keystore). The owner should be a cold key or a Safe.
contract Deploy is Script {
    function run(address owner, address executor) external returns (FlashArbExecutor ex) {
        vm.startBroadcast();
        ex = new FlashArbExecutor(owner, executor);
        vm.stopBroadcast();
        console.log("FlashArbExecutor deployed at", address(ex));
        console.log("owner   ", owner);
        console.log("executor", executor);
    }
}
