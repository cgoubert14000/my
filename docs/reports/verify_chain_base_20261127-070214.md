# Vérification du réseau `base` (chain id 8453) — 2026-11-27 07:02:14

RPC : `base-rpc.publicnode.com` · verdict : **TOUTES LES VÉRIFICATIONS BLOQUANTES PASSENT**

## Réseau
- block : 62862796
- block_time_measured_s : 0.2
- block_time_config_s : 2.0
- base_fee_gwei : 0.005
- priority_fee_gwei : 0.001
- latency_p50_ms : 16.1
- latency_max_ms : 22.1
- head_age_s : 1.0
- l1_fee_900B_eth : 1.7309487169e-08
- native_price_usd : 1734.5010683663368

## Vérifications
- ✅ `rpc_reachable` — base-rpc.publicnode.com in 36 ms
- ✅ `chain_id` — rpc=8453 config=8453
- ✅ `block_time` — measured 0.20 s vs config 2.0 s
- ✅ `head_fresh` — head age 1.0 s
- ✅ `rpc_latency` — p50 16 ms, max 22 ms
- ✅ `multicall3` — 0xcA11bde05977b3631167028862bE2a173976CA11 aggregate3 ok=True
- ✅ `eth_call_state_override` — supported
- ⚠️ `debug_traceTransaction` — unavailable (rpc failed after retries: http 429) → revert reasons come from eth_call replay
- ✅ `code:multicall3` — 0xcA11bde05977b3631167028862bE2a173976CA11 (3808 bytes) — source: mds1/multicall Multicall3 (same address on all chains)
- ✅ `code:wrapped_native` — 0x4200000000000000000000000000000000000006 (2041 bytes) — source: OP-stack WETH predeploy; bgd-labs/aave-address-book AaveV3Base WETH_UNDERLYING
- ✅ `code:dex:uniswap_v3` — 0x33128a8fC17869897dcE68Ed026d694621f6FDfD (24535 bytes) — source: @uniswap/sdk-core 7.19 BASE_ADDRESSES.v3CoreFactoryAddress
- ✅ `code:dex:uniswap_v2` — 0x8909Dc15e40173Ff4699343b6eB8132c65e18eC6 (13859 bytes) — source: @uniswap/sdk-core 7.19 V2_FACTORY_ADDRESSES[BASE]
- ✅ `code:dex:sushiswap_v2` — 0x71524B4f93c58fcbF659783284E38825f0622859 (11264 bytes) — source: sushi npm package evm/config/features/sushiswap-v2 (BASE factory)
- ✅ `code:dex:sushiswap_v3` — 0xc35DADB65012eC5796536bD9864eD8773aBc74C4 (24535 bytes) — source: sushi npm package: SushiSwap V3 factory on BASE / V2 factory on ARBITRUM
- ✅ `code:dex:pancakeswap_v3` — 0x0BFbCF9fa4f9C56B0F40a671Ad40E0805A091865 (5151 bytes) — source: @pancakeswap/v3-sdk FACTORY_ADDRESSES (BASE, ARBITRUM_ONE)
- ✅ `code:dex:pancakeswap_v2` — 0x02a84c1b3BBD7401a5f7fa98a384EBC70bB5749E (14075 bytes) — source: @pancakeswap/v2-sdk FACTORY_ADDRESS_MAP (BASE, ARBITRUM_ONE)
- ✅ `code:dex:aerodrome` — 0x420DD381b31aEf6683db6B902084cB0FFECe40Da (3516 bytes) — source: aerodrome-finance/contracts README (PoolFactory)
- ✅ `code:dex:aerodrome_slipstream` — 0x5e7BB104d84c7CB9B682AaC2F3d509f5F406809A (4958 bytes) — source: aerodrome-finance/slipstream README (CL PoolFactory, Base)
- ✅ `code:flash:MORPHO` — 0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb (15623 bytes) — source: @morpho-org/morpho-ts addresses (BaseMainnet.blue / EthMainnet.blue)
- ✅ `code:flash:BALANCER_V2` — 0xBA12222222228d8Ba445958a75a0704d566BF2C8 (24512 bytes) — source: balancer/balancer-deployments addresses/base.json 20210418-vault
- ✅ `code:flash:AAVE_V3` — 0xA238Dd80C259a72e81d7e4664a9801593F98d1c5 (1933 bytes) — source: bgd-labs/aave-address-book AaveV3Base.POOL
- ✅ `code:token:WETH` — 0x4200000000000000000000000000000000000006 (2041 bytes) — source: OP-stack WETH predeploy; bgd-labs/aave-address-book AaveV3Base WETH_UNDERLYING
- ✅ `code:token:USDC` — 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 (1852 bytes) — source: bgd-labs/aave-address-book AaveV3Base USDC_UNDERLYING (Circle native USDC)
- ✅ `code:token:USDbC` — 0xd9aAEc86B65D86f6A7B5B1b0c42FFA531710b6CA (2096 bytes) — source: bgd-labs/aave-address-book AaveV3Base USDbC_UNDERLYING; sushi npm tokens/base/USDbC
- ✅ `code:token:DAI` — 0x50c5725949A6F0c72E6C4a641F24049A917DB0Cb (5835 bytes) — source: sushi npm package evm/config/tokens/DAI (BASE)
- ✅ `code:token:cbETH` — 0x2Ae3F1Ec7F1F5012CFEab0185bfc7aa3cf0DEc22 (2096 bytes) — source: bgd-labs/aave-address-book AaveV3Base cbETH_UNDERLYING
- ✅ `code:token:cbBTC` — 0xcbB7C0000aB88B473b1f5aFd9ef808440eed33Bf (1550 bytes) — source: bgd-labs/aave-address-book AaveV3Base cbBTC_UNDERLYING
- ✅ `code:token:AERO` — 0x940181a94A35A4569E4529A3CDfB74e38FD98631 (4736 bytes) — source: sushi npm package evm/config/tokens/AERO (BASE)
- ✅ `code:opstack_gas_oracle` — 0x420000000000000000000000000000000000000F (2055 bytes) — source: OP-stack GasPriceOracle predeploy
- ✅ `token:WETH` — on-chain symbol=WETH decimals=18 / config WETH/18
- ✅ `token:USDC` — on-chain symbol=USDC decimals=6 / config USDC/6
- ✅ `token:USDbC` — on-chain symbol=USDbC decimals=6 / config USDbC/6
- ✅ `token:DAI` — on-chain symbol=DAI decimals=18 / config DAI/18
- ✅ `token:cbETH` — on-chain symbol=cbETH decimals=18 / config cbETH/18
- ✅ `token:cbBTC` — on-chain symbol=cbBTC decimals=8 / config cbBTC/8
- ✅ `token:AERO` — on-chain symbol=AERO decimals=18 / config AERO/18
- ✅ `factory:uniswap_v3` — V3 feeAmountTickSpacing(3000)=60
- ✅ `factory:uniswap_v2` — V2 allPairsLength=3086191
- ✅ `factory:sushiswap_v2` — V2 allPairsLength=6152
- ✅ `factory:sushiswap_v3` — V3 feeAmountTickSpacing(3000)=60
- ✅ `factory:pancakeswap_v3` — V3 feeAmountTickSpacing(2500)=50
- ✅ `factory:pancakeswap_v2` — V2 allPairsLength=65722
- ✅ `factory:aerodrome` — Solidly allPoolsLength=30049
- ✅ `factory:aerodrome_slipstream` — Slipstream tickSpacingToFee(100)=500
- ✅ `l1_fee_oracle` — getL1FeeUpperBound(900 B) = 0.000000017 ETH
- ✅ `pool_discovery` — 429 pools: {'uniswap_v3': 130, 'aerodrome': 172, 'aerodrome_slipstream': 89, 'pancakeswap_v3': 26, 'uniswap_v2': 10, 'sushiswap_v2': 1, 'sushiswap_v3': 1}
- ✅ `pools_with_depth` — 332 pools ≥ 20 000 $ (deepest: WETH/USDC uniswap_v3 96814846.33 $)
- ✅ `native_price` — ETH ≈ 1734.5010683663368 $ (from the deepest WETH/stable pool)
- ✅ `flash:MORPHO` — fee 0.0 bps, capacity WETH 89,050.80, USDC 268,471,678.84, cbBTC 41,138.23
- ✅ `flash:BALANCER_V2` — fee 0.0 bps, capacity WETH 22.19, USDC 53,925.85, cbBTC 0.01
- ✅ `flash:AAVE_V3` — fee 5.0 bps, capacity WETH 20,371.76, USDC 14,014,081.64, cbBTC 3,416.86
- ✅ `flash_any_capacity` — at least one provider can lend a borrowable token

## Fournisseurs de flash loan (capacité en direct)
- MORPHO `0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb` : frais 0.0 bps, vérifié=True, capacité {'WETH': 89050.7999668119, 'USDC': 268471678.842268, 'cbBTC': 41138.22637187}
- BALANCER_V2 `0xBA12222222228d8Ba445958a75a0704d566BF2C8` : frais 0.0 bps, vérifié=True, capacité {'WETH': 22.191052122107664, 'USDC': 53925.853141, 'cbBTC': 0.01473233}
- AAVE_V3 `0xA238Dd80C259a72e81d7e4664a9801593F98d1c5` : frais 5.0 bps, vérifié=True, capacité {'WETH': 20371.756695729124, 'USDC': 14014081.637576, 'cbBTC': 3416.85928776}

## Pools découverts (profondeur en USD, 30 premiers)

| pool | DEX | paire | frais (ppm) | profondeur $ |
|---|---|---|---|---|
| `0x6c561B44…` | uniswap_v3 | WETH/USDC | 3000 | 96814846.33 |
| `0x7AeA2E8A…` | uniswap_v3 | WETH/cbBTC | 500 | 23515691.3 |
| `0x8c708056…` | uniswap_v3 | WETH/cbBTC | 3000 | 7615360.46 |
| `0x01784ef3…` | aerodrome | WETH/VVV | 3000 | 7390201.64 |
| `0xd0b53D92…` | uniswap_v3 | WETH/USDC | 500 | 7306853.51 |
| `0xfBB6Eed8…` | uniswap_v3 | USDC/cbBTC | 500 | 5928814.99 |
| `0xC211e1f8…` | pancakeswap_v3 | WETH/cbBTC | 100 | 4167231.52 |
| `0x6cDcb1C4…` | aerodrome | USDC/AERO | 3000 | 3281190.93 |
| `0x72AB388E…` | pancakeswap_v3 | WETH/USDC | 100 | 3051079.36 |
| `0xd9eDC75a…` | aerodrome | WETH/KTA | 3000 | 2708286.46 |
| `0xb2cc224c…` | aerodrome_slipstream | WETH/USDC | 185 | 2214265.72 |
| `0xeC558e48…` | uniswap_v3 | USDC/cbBTC | 3000 | 1979244.81 |
| `0x70aCDF2A…` | aerodrome_slipstream | WETH/cbBTC | 2505 | 1892871.88 |
| `0x5447F7FE…` | aerodrome | WETH/FAI | 10000 | 1661201.99 |
| `0x80891885…` | aerodrome_slipstream | USDC/ZCHF | 500 | 1458744.67 |
| `0xAEC085E5…` | uniswap_v3 | BNKR/WETH | 10000 | 1317181.67 |
| `0x4e962BB3…` | aerodrome_slipstream | USDC/cbBTC | 472 | 1262312.28 |
| `0x6b0F53cb…` | aerodrome_slipstream | USDC/VELVET | 100 | 1260094.93 |
| `0xC1a6FBeD…` | uniswap_v3 | CLANKER/WETH | 10000 | 1212270.81 |
| `0xb94b2233…` | pancakeswap_v3 | USDC/cbBTC | 100 | 1144453.03 |
| `0x67A11022…` | uniswap_v3 | USDC/VVV | 3000 | 1124926.54 |
| `0x69bc1d35…` | aerodrome | USDC/SEND | 3000 | 1061616.53 |
| `0x0392B12a…` | aerodrome_slipstream | WETH/ZEN | 1500 | 1035706.57 |
| `0x1D2bdB71…` | uniswap_v3 | WETH/VVV | 10000 | 1023651.46 |
| `0x47f9e291…` | aerodrome_slipstream | cbBTC/ZEN | 2500 | 1003724.92 |
| `0x88A43bbD…` | uniswap_v2 | WETH/USDC | 3000 | 989299.71 |
| `0x3d5D1433…` | uniswap_v3 | WETH/AERO | 3000 | 978384.93 |
| `0xADE9BcD4…` | uniswap_v3 | WETH/doginme | 10000 | 906319.77 |
| `0x5116773e…` | uniswap_v3 | DRB/WETH | 10000 | 872124.28 |
| `0x4b0Aaf3E…` | uniswap_v3 | WETH/TOSHI | 10000 | 809400.19 |

Empreinte de configuration : `5ac48b43cfe8a100` (toute modification des adresses exige une nouvelle vérification).