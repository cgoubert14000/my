# Vérification du réseau `base` (chain id 8453) — 2026-11-25 15:14:44

RPC : `base-rpc.publicnode.com` · verdict : **TOUTES LES VÉRIFICATIONS BLOQUANTES PASSENT**

## Réseau
- block : 62146545
- block_time_measured_s : 0.2
- block_time_config_s : 2.0
- base_fee_gwei : 0.006130962
- priority_fee_gwei : 0.001
- latency_p50_ms : 127.7
- latency_max_ms : 646.7
- head_age_s : 3.3
- l1_fee_900B_eth : 1.23408580331e-07
- native_price_usd : 1633.6280617417408

## Vérifications
- ✅ `rpc_reachable` — base-rpc.publicnode.com in 128 ms
- ✅ `chain_id` — rpc=8453 config=8453
- ✅ `block_time` — measured 0.20 s vs config 2.0 s
- ✅ `head_fresh` — head age 3.3 s
- ✅ `rpc_latency` — p50 128 ms, max 647 ms
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
- ✅ `factory:uniswap_v2` — V2 allPairsLength=3081011
- ✅ `factory:sushiswap_v2` — V2 allPairsLength=6152
- ✅ `factory:sushiswap_v3` — V3 feeAmountTickSpacing(3000)=60
- ✅ `factory:pancakeswap_v3` — V3 feeAmountTickSpacing(2500)=50
- ✅ `factory:pancakeswap_v2` — V2 allPairsLength=64920
- ✅ `factory:aerodrome` — Solidly allPoolsLength=30043
- ✅ `factory:aerodrome_slipstream` — Slipstream tickSpacingToFee(100)=500
- ✅ `l1_fee_oracle` — getL1FeeUpperBound(900 B) = 0.000000123 ETH
- ✅ `pool_discovery` — 414 pools: {'uniswap_v3': 123, 'aerodrome': 169, 'aerodrome_slipstream': 85, 'pancakeswap_v3': 26, 'uniswap_v2': 9, 'sushiswap_v2': 1, 'sushiswap_v3': 1}
- ✅ `pools_with_depth` — 326 pools ≥ 20 000 $ (deepest: WETH/USDC uniswap_v3 92275416.33 $)
- ✅ `native_price` — ETH ≈ 1633.6280617417408 $ (from the deepest WETH/stable pool)
- ✅ `flash:MORPHO` — fee 0.0 bps, capacity WETH 89,018.07, USDC 389,058,261.59, cbBTC 41,051.89
- ✅ `flash:BALANCER_V2` — fee 0.0 bps, capacity WETH 23.21, USDC 52,153.38, cbBTC 0.01
- ✅ `flash:AAVE_V3` — fee 5.0 bps, capacity WETH 20,390.34, USDC 14,166,064.00, cbBTC 3,417.32
- ✅ `flash_any_capacity` — at least one provider can lend a borrowable token

## Fournisseurs de flash loan (capacité en direct)
- MORPHO `0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb` : frais 0.0 bps, vérifié=True, capacité {'WETH': 89018.07027571257, 'USDC': 389058261.593738, 'cbBTC': 41051.89129167}
- BALANCER_V2 `0xBA12222222228d8Ba445958a75a0704d566BF2C8` : frais 0.0 bps, vérifié=True, capacité {'WETH': 23.205192633197512, 'USDC': 52153.380297, 'cbBTC': 0.01482109}
- AAVE_V3 `0xA238Dd80C259a72e81d7e4664a9801593F98d1c5` : frais 5.0 bps, vérifié=True, capacité {'WETH': 20390.342224381642, 'USDC': 14166063.999703, 'cbBTC': 3417.31601126}

## Pools découverts (profondeur en USD, 30 premiers)

| pool | DEX | paire | frais (ppm) | profondeur $ |
|---|---|---|---|---|
| `0x6c561B44…` | uniswap_v3 | WETH/USDC | 3000 | 92275416.33 |
| `0x7AeA2E8A…` | uniswap_v3 | WETH/cbBTC | 500 | 21800441.57 |
| `0x8c708056…` | uniswap_v3 | WETH/cbBTC | 3000 | 7149096.0 |
| `0xd0b53D92…` | uniswap_v3 | WETH/USDC | 500 | 6920521.17 |
| `0x01784ef3…` | aerodrome | WETH/VVV | 3000 | 6802447.37 |
| `0xfBB6Eed8…` | uniswap_v3 | USDC/cbBTC | 500 | 6049109.31 |
| `0xC211e1f8…` | pancakeswap_v3 | WETH/cbBTC | 100 | 3913645.19 |
| `0x6cDcb1C4…` | aerodrome | USDC/AERO | 3000 | 3191000.76 |
| `0x72AB388E…` | pancakeswap_v3 | WETH/USDC | 100 | 2926018.27 |
| `0xd9eDC75a…` | aerodrome | WETH/KTA | 3000 | 2549479.29 |
| `0xb2cc224c…` | aerodrome_slipstream | WETH/USDC | 208 | 2127794.05 |
| `0xeC558e48…` | uniswap_v3 | USDC/cbBTC | 3000 | 1834211.98 |
| `0x70aCDF2A…` | aerodrome_slipstream | WETH/cbBTC | 2600 | 1801575.11 |
| `0x5447F7FE…` | aerodrome | WETH/FAI | 10000 | 1562569.38 |
| `0x80891885…` | aerodrome_slipstream | USDC/ZCHF | 500 | 1454852.71 |
| `0xAEC085E5…` | uniswap_v3 | BNKR/WETH | 10000 | 1249422.63 |
| `0x4e962BB3…` | aerodrome_slipstream | USDC/cbBTC | 448 | 1198104.53 |
| `0x6b0F53cb…` | aerodrome_slipstream | USDC/VELVET | 100 | 1189220.98 |
| `0xb94b2233…` | pancakeswap_v3 | USDC/cbBTC | 100 | 1090851.38 |
| `0xC1a6FBeD…` | uniswap_v3 | CLANKER/WETH | 10000 | 1068585.05 |
| `0x67A11022…` | uniswap_v3 | USDC/VVV | 3000 | 1059698.14 |
| `0x69bc1d35…` | aerodrome | USDC/SEND | 3000 | 1057207.91 |
| `0x1D2bdB71…` | uniswap_v3 | WETH/VVV | 10000 | 1020117.58 |
| `0x0392B12a…` | aerodrome_slipstream | WETH/ZEN | 1500 | 965854.76 |
| `0x88A43bbD…` | uniswap_v2 | WETH/USDC | 3000 | 959883.7 |
| `0x47f9e291…` | aerodrome_slipstream | cbBTC/ZEN | 2500 | 925102.26 |
| `0x3d5D1433…` | uniswap_v3 | WETH/AERO | 3000 | 906790.99 |
| `0xADE9BcD4…` | uniswap_v3 | WETH/doginme | 10000 | 848799.25 |
| `0x5116773e…` | uniswap_v3 | DRB/WETH | 10000 | 797494.16 |
| `0x4b0Aaf3E…` | uniswap_v3 | WETH/TOSHI | 10000 | 766472.04 |

Empreinte de configuration : `5ac48b43cfe8a100` (toute modification des adresses exige une nouvelle vérification).