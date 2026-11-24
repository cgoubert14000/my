# Vérification du réseau `base` (chain id 8453) — 2026-11-24 04:56:46

RPC : `base-rpc.publicnode.com` · verdict : **TOUTES LES VÉRIFICATIONS BLOQUANTES PASSENT**

## Réseau
- block : 61529155
- block_time_measured_s : 0.2
- block_time_config_s : 2.0
- base_fee_gwei : 0.005
- priority_fee_gwei : 0.001
- latency_p50_ms : 16.3
- latency_max_ms : 20.2
- head_age_s : 0.8
- l1_fee_900B_eth : 5.981258364e-09
- native_price_usd : 1700.6738642158266

## Vérifications
- ✅ `rpc_reachable` — base-rpc.publicnode.com in 31 ms
- ✅ `chain_id` — rpc=8453 config=8453
- ✅ `block_time` — measured 0.20 s vs config 2.0 s
- ✅ `head_fresh` — head age 0.8 s
- ✅ `rpc_latency` — p50 16 ms, max 20 ms
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
- ✅ `factory:uniswap_v2` — V2 allPairsLength=3080526
- ✅ `factory:sushiswap_v2` — V2 allPairsLength=6152
- ✅ `factory:sushiswap_v3` — V3 feeAmountTickSpacing(3000)=60
- ✅ `factory:pancakeswap_v3` — V3 feeAmountTickSpacing(2500)=50
- ✅ `factory:pancakeswap_v2` — V2 allPairsLength=64063
- ✅ `factory:aerodrome` — Solidly allPoolsLength=30037
- ✅ `factory:aerodrome_slipstream` — Slipstream tickSpacingToFee(100)=500
- ✅ `l1_fee_oracle` — getL1FeeUpperBound(900 B) = 0.000000006 ETH
- ✅ `pool_discovery` — 425 pools: {'uniswap_v3': 127, 'aerodrome': 172, 'aerodrome_slipstream': 88, 'pancakeswap_v3': 26, 'uniswap_v2': 10, 'sushiswap_v2': 1, 'sushiswap_v3': 1}
- ✅ `pools_with_depth` — 331 pools ≥ 20 000 $ (deepest: WETH/USDC uniswap_v3 82490030.82 $)
- ✅ `native_price` — ETH ≈ 1700.6738642158266 $ (from the deepest WETH/stable pool)
- ✅ `flash:MORPHO` — fee 0.0 bps, capacity WETH 88,702.65, USDC 354,500,387.03, cbBTC 41,146.62
- ✅ `flash:BALANCER_V2` — fee 0.0 bps, capacity WETH 23.02, USDC 53,645.12, cbBTC 0.01
- ✅ `flash:AAVE_V3` — fee 5.0 bps, capacity WETH 20,883.39, USDC 12,763,404.32, cbBTC 3,401.08
- ✅ `flash_any_capacity` — at least one provider can lend a borrowable token

## Fournisseurs de flash loan (capacité en direct)
- MORPHO `0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb` : frais 0.0 bps, vérifié=True, capacité {'WETH': 88702.64741818374, 'USDC': 354500387.027827, 'cbBTC': 41146.6199591}
- BALANCER_V2 `0xBA12222222228d8Ba445958a75a0704d566BF2C8` : frais 0.0 bps, vérifié=True, capacité {'WETH': 23.019115713907066, 'USDC': 53645.124304, 'cbBTC': 0.01474814}
- AAVE_V3 `0xA238Dd80C259a72e81d7e4664a9801593F98d1c5` : frais 5.0 bps, vérifié=True, capacité {'WETH': 20883.389011956882, 'USDC': 12763404.322438, 'cbBTC': 3401.07500142}

## Pools découverts (profondeur en USD, 30 premiers)

| pool | DEX | paire | frais (ppm) | profondeur $ |
|---|---|---|---|---|
| `0x6c561B44…` | uniswap_v3 | WETH/USDC | 3000 | 82490030.82 |
| `0x7AeA2E8A…` | uniswap_v3 | WETH/cbBTC | 500 | 22211583.46 |
| `0xd0b53D92…` | uniswap_v3 | WETH/USDC | 500 | 9861294.92 |
| `0x8c708056…` | uniswap_v3 | WETH/cbBTC | 3000 | 7570105.31 |
| `0x01784ef3…` | aerodrome | WETH/VVV | 3000 | 7022861.15 |
| `0xfBB6Eed8…` | uniswap_v3 | USDC/cbBTC | 500 | 5444501.95 |
| `0xC211e1f8…` | pancakeswap_v3 | WETH/cbBTC | 100 | 3969101.21 |
| `0x6cDcb1C4…` | aerodrome | USDC/AERO | 3000 | 3319085.24 |
| `0x72AB388E…` | pancakeswap_v3 | WETH/USDC | 100 | 2964211.69 |
| `0xd9eDC75a…` | aerodrome | WETH/KTA | 3000 | 2641552.55 |
| `0xb2cc224c…` | aerodrome_slipstream | WETH/USDC | 193 | 2206695.82 |
| `0xeC558e48…` | uniswap_v3 | USDC/cbBTC | 3000 | 1885587.58 |
| `0x70aCDF2A…` | aerodrome_slipstream | WETH/cbBTC | 2500 | 1882453.26 |
| `0x5447F7FE…` | aerodrome | WETH/FAI | 10000 | 1648470.54 |
| `0x80891885…` | aerodrome_slipstream | USDC/ZCHF | 500 | 1457006.45 |
| `0xAEC085E5…` | uniswap_v3 | BNKR/WETH | 10000 | 1297653.57 |
| `0x4e962BB3…` | aerodrome_slipstream | USDC/cbBTC | 496 | 1263660.56 |
| `0x6b0F53cb…` | aerodrome_slipstream | USDC/VELVET | 100 | 1169068.32 |
| `0xC1a6FBeD…` | uniswap_v3 | CLANKER/WETH | 10000 | 1166572.2 |
| `0xb94b2233…` | pancakeswap_v3 | USDC/cbBTC | 100 | 1124072.18 |
| `0x67A11022…` | uniswap_v3 | USDC/VVV | 3000 | 1067090.64 |
| `0x69bc1d35…` | aerodrome | USDC/SEND | 3000 | 1060611.21 |
| `0x1D2bdB71…` | uniswap_v3 | WETH/VVV | 10000 | 1033666.28 |
| `0x0392B12a…` | aerodrome_slipstream | WETH/ZEN | 1500 | 1012858.3 |
| `0x88A43bbD…` | uniswap_v2 | WETH/USDC | 3000 | 979074.16 |
| `0x47f9e291…` | aerodrome_slipstream | cbBTC/ZEN | 2500 | 978050.22 |
| `0x3d5D1433…` | uniswap_v3 | WETH/AERO | 3000 | 969295.84 |
| `0xADE9BcD4…` | uniswap_v3 | WETH/doginme | 10000 | 884105.44 |
| `0x5116773e…` | uniswap_v3 | DRB/WETH | 10000 | 873816.93 |
| `0x85f1Aa3a…` | aerodrome | USDC/NOCK | 3000 | 801930.78 |

Empreinte de configuration : `5ac48b43cfe8a100` (toute modification des adresses exige une nouvelle vérification).