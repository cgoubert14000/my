# Vérification du réseau `base` (chain id 8453) — 2026-11-21 03:09:25

RPC : `base-rpc.publicnode.com` · verdict : **TOUTES LES VÉRIFICATIONS BLOQUANTES PASSENT**

## Réseau
- block : 60200949
- block_time_measured_s : 0.2
- block_time_config_s : 2.0
- base_fee_gwei : 0.005000557
- priority_fee_gwei : 0.001
- latency_p50_ms : 19.1
- latency_max_ms : 28.8
- head_age_s : 0.6
- l1_fee_900B_eth : 1.4154939017e-08
- native_price_usd : 1607.5558997467256

## Vérifications
- ✅ `rpc_reachable` — base-rpc.publicnode.com in 43 ms
- ✅ `chain_id` — rpc=8453 config=8453
- ✅ `block_time` — measured 0.20 s vs config 2.0 s
- ✅ `head_fresh` — head age 0.6 s
- ✅ `rpc_latency` — p50 19 ms, max 29 ms
- ✅ `multicall3` — 0xcA11bde05977b3631167028862bE2a173976CA11 aggregate3 ok=True
- ✅ `eth_call_state_override` — supported
- ⚠️ `debug_traceTransaction` — unavailable (rpc failed after retries: unexpected character, expected a JSON value: line 1 column 1 (char 0)) → revert reasons come from eth_call replay
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
- ✅ `factory:uniswap_v2` — V2 allPairsLength=3079547
- ✅ `factory:sushiswap_v2` — V2 allPairsLength=6152
- ✅ `factory:sushiswap_v3` — V3 feeAmountTickSpacing(3000)=60
- ✅ `factory:pancakeswap_v3` — V3 feeAmountTickSpacing(2500)=50
- ✅ `factory:pancakeswap_v2` — V2 allPairsLength=63909
- ✅ `factory:aerodrome` — Solidly allPoolsLength=30030
- ✅ `factory:aerodrome_slipstream` — Slipstream tickSpacingToFee(100)=500
- ✅ `l1_fee_oracle` — getL1FeeUpperBound(900 B) = 0.000000014 ETH
- ✅ `pool_discovery` — 410 pools: {'uniswap_v3': 121, 'aerodrome': 167, 'aerodrome_slipstream': 86, 'pancakeswap_v3': 25, 'uniswap_v2': 9, 'sushiswap_v2': 1, 'sushiswap_v3': 1}
- ✅ `pools_with_depth` — 321 pools ≥ 20 000 $ (deepest: WETH/USDC uniswap_v3 76903105.51 $)
- ✅ `native_price` — ETH ≈ 1607.5558997467256 $ (from the deepest WETH/stable pool)
- ✅ `flash:MORPHO` — fee 0.0 bps, capacity WETH 85,961.55, USDC 245,320,289.98, cbBTC 41,102.63
- ✅ `flash:BALANCER_V2` — fee 0.0 bps, capacity WETH 23.30, USDC 51,890.97, cbBTC 0.01
- ✅ `flash:AAVE_V3` — fee 5.0 bps, capacity WETH 22,099.89, USDC 14,435,186.15, cbBTC 3,330.27
- ✅ `flash_any_capacity` — at least one provider can lend a borrowable token

## Fournisseurs de flash loan (capacité en direct)
- MORPHO `0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb` : frais 0.0 bps, vérifié=True, capacité {'WETH': 85961.55046680605, 'USDC': 245320289.98262, 'cbBTC': 41102.62904302}
- BALANCER_V2 `0xBA12222222228d8Ba445958a75a0704d566BF2C8` : frais 0.0 bps, vérifié=True, capacité {'WETH': 23.300077195752472, 'USDC': 51890.967331, 'cbBTC': 0.01448577}
- AAVE_V3 `0xA238Dd80C259a72e81d7e4664a9801593F98d1c5` : frais 5.0 bps, vérifié=True, capacité {'WETH': 22099.886473711842, 'USDC': 14435186.154127, 'cbBTC': 3330.26683279}

## Pools découverts (profondeur en USD, 30 premiers)

| pool | DEX | paire | frais (ppm) | profondeur $ |
|---|---|---|---|---|
| `0x6c561B44…` | uniswap_v3 | WETH/USDC | 3000 | 76903105.51 |
| `0x7AeA2E8A…` | uniswap_v3 | WETH/cbBTC | 500 | 20335308.41 |
| `0xd0b53D92…` | uniswap_v3 | WETH/USDC | 500 | 10250124.81 |
| `0x8c708056…` | uniswap_v3 | WETH/cbBTC | 3000 | 7030908.17 |
| `0x01784ef3…` | aerodrome | WETH/VVV | 3000 | 6209712.87 |
| `0xfBB6Eed8…` | uniswap_v3 | USDC/cbBTC | 500 | 5479929.04 |
| `0xC211e1f8…` | pancakeswap_v3 | WETH/cbBTC | 100 | 3746605.68 |
| `0x6cDcb1C4…` | aerodrome | USDC/AERO | 3000 | 3284715.33 |
| `0x72AB388E…` | pancakeswap_v3 | WETH/USDC | 100 | 2852584.98 |
| `0xd9eDC75a…` | aerodrome | WETH/KTA | 3000 | 2474669.37 |
| `0xb2cc224c…` | aerodrome_slipstream | WETH/USDC | 340 | 2095429.17 |
| `0xeC558e48…` | uniswap_v3 | USDC/cbBTC | 3000 | 1745190.17 |
| `0x70aCDF2A…` | aerodrome_slipstream | WETH/cbBTC | 2500 | 1575312.57 |
| `0x5447F7FE…` | aerodrome | WETH/FAI | 10000 | 1531672.45 |
| `0x80891885…` | aerodrome_slipstream | USDC/ZCHF | 500 | 1454318.44 |
| `0xAEC085E5…` | uniswap_v3 | BNKR/WETH | 10000 | 1244240.98 |
| `0x4e962BB3…` | aerodrome_slipstream | USDC/cbBTC | 600 | 1242309.24 |
| `0xC1a6FBeD…` | uniswap_v3 | CLANKER/WETH | 10000 | 1151645.56 |
| `0xb94b2233…` | pancakeswap_v3 | USDC/cbBTC | 100 | 1079707.91 |
| `0x6b0F53cb…` | aerodrome_slipstream | USDC/VELVET | 100 | 1072742.26 |
| `0x69bc1d35…` | aerodrome | USDC/SEND | 3000 | 1059483.73 |
| `0x0392B12a…` | aerodrome_slipstream | WETH/ZEN | 1500 | 956330.1 |
| `0x88A43bbD…` | uniswap_v2 | WETH/USDC | 3000 | 951194.82 |
| `0x1D2bdB71…` | uniswap_v3 | WETH/VVV | 10000 | 940178.91 |
| `0x47f9e291…` | aerodrome_slipstream | cbBTC/ZEN | 2500 | 932579.63 |
| `0x3d5D1433…` | uniswap_v3 | WETH/AERO | 3000 | 916006.39 |
| `0x67A11022…` | uniswap_v3 | USDC/VVV | 3000 | 907973.86 |
| `0xADE9BcD4…` | uniswap_v3 | WETH/doginme | 10000 | 848460.24 |
| `0xBA3F9458…` | uniswap_v3 | WETH/BRETT | 10000 | 759251.78 |
| `0x85f1Aa3a…` | aerodrome | USDC/NOCK | 3000 | 747157.93 |

Empreinte de configuration : `5ac48b43cfe8a100` (toute modification des adresses exige une nouvelle vérification).