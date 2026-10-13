# Vérification du réseau `local` (chain id 31337) — 2026-10-13 13:42:06

RPC : `127.0.0.1:8545` · verdict : **TOUTES LES VÉRIFICATIONS BLOQUANTES PASSENT**

## Réseau
- block : 2973
- block_time_measured_s : 2.0
- block_time_config_s : 2.0
- base_fee_gwei : 0.012624677
- priority_fee_gwei : 1.0
- latency_p50_ms : 0.3
- latency_max_ms : 0.5
- head_age_s : 1.5
- native_price_usd : 2000.364188924419

## Vérifications
- ✅ `rpc_reachable` — 127.0.0.1:8545 in 1 ms
- ✅ `chain_id` — rpc=31337 config=31337
- ✅ `block_time` — measured 2.00 s vs config 2.0 s
- ✅ `head_fresh` — head age 1.5 s
- ✅ `rpc_latency` — p50 0 ms, max 0 ms
- ✅ `multicall3` — 0xcA11bde05977b3631167028862bE2a173976CA11 aggregate3 ok=True
- ✅ `eth_call_state_override` — supported
- ✅ `debug_traceTransaction` — available
- ✅ `code:multicall3` — 0xcA11bde05977b3631167028862bE2a173976CA11 (3480 bytes)
- ✅ `code:wrapped_native` — 0xD2D5e508C82EFc205cAFA4Ad969a4395Babce026 (2227 bytes)
- ✅ `code:dex:sushiswap` — 0xB468647B04bF657C9ee2de65252037d781eABafD (13859 bytes)
- ✅ `code:dex:uniswap_v2` — 0x7bdd3b028C4796eF0EAf07d11394d0d9d8c24139 (13859 bytes)
- ✅ `code:dex:uniswap_v3` — 0x6F9679BdF5F180a139d01c598839a5df4860431b (24535 bytes)
- ✅ `code:flash:BALANCER_V2` — 0xc075BC0f734EFE6ceD866324fc2A9DBe1065CBB1 (2442 bytes)
- ✅ `code:flash:AAVE_V3` — 0x837a41023CF81234f89F956C94D676918b4791c1 (1441 bytes)
- ✅ `code:flash:MORPHO` — 0x04d7478fDF318C3C22cECE62Da9D78ff94807D77 (910 bytes)
- ✅ `code:token:WETH` — 0xD2D5e508C82EFc205cAFA4Ad969a4395Babce026 (2227 bytes)
- ✅ `code:token:USDC` — 0x2b639Cc84e1Ad3aA92D4Ee7d2755A6ABEf300D72 (2181 bytes)
- ✅ `code:token:DAI` — 0xF85895D097B2C25946BB95C4d11E2F3c035F8f0C (2181 bytes)
- ✅ `code:token:WBTC` — 0x0b27a79cb9C0B38eE06Ca3d94DAA68e0Ed17F953 (2181 bytes)
- ✅ `code:executor` — 0xDC57724Ea354ec925BaFfCA0cCf8A1248a8E5CF1 (14208 bytes)
- ✅ `token:WETH` — on-chain symbol=WETH decimals=18 / config WETH/18
- ✅ `token:USDC` — on-chain symbol=USDC decimals=6 / config USDC/6
- ✅ `token:DAI` — on-chain symbol=DAI decimals=18 / config DAI/18
- ✅ `token:WBTC` — on-chain symbol=WBTC decimals=8 / config WBTC/8
- ✅ `factory:sushiswap` — V2 allPairsLength=5
- ✅ `factory:uniswap_v2` — V2 allPairsLength=5
- ✅ `factory:uniswap_v3` — V3 feeAmountTickSpacing(3000)=60
- ✅ `pool_discovery` — 18 pools: {'uniswap_v2': 5, 'sushiswap': 5, 'uniswap_v3': 5, 'aerodrome': 3}
- ✅ `pools_with_depth` — 18 pools ≥ 20 000 $ (deepest: USDC/WETH uniswap_v3 60505508.11 $)
- ✅ `native_price` — ETH ≈ 2000.364188924419 $ (from the deepest WETH/stable pool)
- ✅ `flash:BALANCER_V2` — fee 0.0 bps, capacity WETH 10,000.00, USDC 20,000,000.00, DAI 20,000,000.00
- ✅ `flash:AAVE_V3` — fee 5.0 bps, capacity WETH 10,000.00, USDC 20,000,000.00, DAI 20,000,000.00
- ✅ `flash:MORPHO` — fee 0.0 bps, capacity WETH 10,000.00, USDC 20,000,000.00, DAI 20,000,000.00
- ✅ `flash_any_capacity` — at least one provider can lend a borrowable token

## Fournisseurs de flash loan (capacité en direct)
- BALANCER_V2 `0xc075BC0f734EFE6ceD866324fc2A9DBe1065CBB1` : frais 0.0 bps, vérifié=True, capacité {'WETH': 10000.0, 'USDC': 20000000.0, 'DAI': 20000000.0}
- AAVE_V3 `0x837a41023CF81234f89F956C94D676918b4791c1` : frais 5.0 bps, vérifié=True, capacité {'WETH': 10000.0, 'USDC': 20000000.0, 'DAI': 20000000.0}
- MORPHO `0x04d7478fDF318C3C22cECE62Da9D78ff94807D77` : frais 0.0 bps, vérifié=True, capacité {'WETH': 10000.0, 'USDC': 20000000.0, 'DAI': 20000000.0}

## Pools découverts (profondeur en USD, 30 premiers)

| pool | DEX | paire | frais (ppm) | profondeur $ |
|---|---|---|---|---|
| `0x8e6D6733…` | uniswap_v3 | USDC/WETH | 500 | 60505508.11 |
| `0xe3d46724…` | uniswap_v3 | USDC/DAI | 100 | 45375002.04 |
| `0x8E0D6aCb…` | uniswap_v3 | USDC/WETH | 3000 | 30252757.73 |
| `0x2Dd661d0…` | uniswap_v3 | WBTC/WETH | 3000 | 21181409.15 |
| `0xF8CB27Ff…` | uniswap_v3 | WETH/DAI | 3000 | 18151655.34 |
| `0xD672B74B…` | uniswap_v2 | USDC/WETH | 3000 | 3307276.8 |
| `0xA1a91bAf…` | sushiswap | USDC/WETH | 3000 | 3291093.75 |
| `0xf201fFeA…` | aerodrome | USDC/DAI (stable) | 500 | 3046198.36 |
| `0x0bbb8bd5…` | sushiswap | USDC/DAI | 3000 | 2337489.76 |
| `0x98Bf79b3…` | uniswap_v2 | USDC/DAI | 3000 | 2191642.39 |
| `0x069B618F…` | uniswap_v2 | WETH/DAI | 3000 | 1576252.13 |
| `0x62a5eDc4…` | sushiswap | WETH/DAI | 3000 | 1572460.04 |
| `0xa85EffB2…` | aerodrome | USDC/WETH | 3000 | 1354290.32 |
| `0x3E499b2c…` | sushiswap | WBTC/WETH | 3000 | 1141254.3 |
| `0x53b0B4E6…` | uniswap_v2 | WBTC/WETH | 3000 | 1058285.29 |
| `0x98248C7C…` | uniswap_v2 | WBTC/USDC | 3000 | 873833.95 |
| `0x4A00c427…` | sushiswap | WBTC/USDC | 3000 | 865103.75 |
| `0x1bEfE2d8…` | aerodrome | WETH/DAI | 3000 | 532006.93 |

Empreinte de configuration : `66f0c3199b1bfacb` (toute modification des adresses exige une nouvelle vérification).