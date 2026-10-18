# Vérification du réseau `base` (chain id 8453) — 2026-10-18 08:56:02

RPC : `base-rpc.publicnode.com` · verdict : **TOUTES LES VÉRIFICATIONS BLOQUANTES PASSENT**

## Réseau
- block : 52762207
- block_time_measured_s : 2.0
- block_time_config_s : 2.0
- base_fee_gwei : 0.005
- priority_fee_gwei : 0.001
- latency_p50_ms : 60.8
- latency_max_ms : 73.2
- head_age_s : 2.4
- l1_fee_900B_eth : 3.145345382e-09
- native_price_usd : 2410.9864741015767

## Vérifications
- ✅ `rpc_reachable` — base-rpc.publicnode.com in 91 ms
- ✅ `chain_id` — rpc=8453 config=8453
- ✅ `block_time` — measured 2.00 s vs config 2.0 s
- ✅ `head_fresh` — head age 2.4 s
- ✅ `rpc_latency` — p50 61 ms, max 73 ms
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
- ✅ `factory:uniswap_v2` — V2 allPairsLength=3070682
- ✅ `factory:sushiswap_v2` — V2 allPairsLength=6131
- ✅ `factory:sushiswap_v3` — V3 feeAmountTickSpacing(3000)=60
- ✅ `factory:pancakeswap_v3` — V3 feeAmountTickSpacing(2500)=50
- ✅ `factory:pancakeswap_v2` — V2 allPairsLength=39099
- ✅ `factory:aerodrome` — Solidly allPoolsLength=29803
- ✅ `factory:aerodrome_slipstream` — Slipstream tickSpacingToFee(100)=500
- ✅ `l1_fee_oracle` — getL1FeeUpperBound(900 B) = 0.000000003 ETH
- ✅ `pool_discovery` — 580 pools: {'uniswap_v3': 137, 'aerodrome': 236, 'aerodrome_slipstream': 157, 'pancakeswap_v3': 32, 'uniswap_v2': 14, 'sushiswap_v2': 1, 'sushiswap_v3': 3}
- ✅ `pools_with_depth` — 467 pools ≥ 20 000 $ (deepest: WETH/USDC uniswap_v3 146000733.76 $)
- ✅ `native_price` — ETH ≈ 2410.9864741015767 $ (from the deepest WETH/stable pool)
- ✅ `flash:MORPHO` — fee 0.0 bps, capacity WETH 82,479.97, USDC 239,255,658.57, cbBTC 39,839.16
- ✅ `flash:BALANCER_V2` — fee 0.0 bps, capacity WETH 20.35, USDC 69,232.93, cbBTC 0.02
- ✅ `flash:AAVE_V3` — fee 5.0 bps, capacity WETH 19,800.99, USDC 18,856,376.59, cbBTC 2,855.93
- ✅ `flash_any_capacity` — at least one provider can lend a borrowable token

## Fournisseurs de flash loan (capacité en direct)
- MORPHO `0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb` : frais 0.0 bps, vérifié=True, capacité {'WETH': 82479.97280604695, 'USDC': 239255658.572587, 'cbBTC': 39839.16074091}
- BALANCER_V2 `0xBA12222222228d8Ba445958a75a0704d566BF2C8` : frais 0.0 bps, vérifié=True, capacité {'WETH': 20.35113798607517, 'USDC': 69232.933151, 'cbBTC': 0.02202393}
- AAVE_V3 `0xA238Dd80C259a72e81d7e4664a9801593F98d1c5` : frais 5.0 bps, vérifié=True, capacité {'WETH': 19800.986886635397, 'USDC': 18856376.592678, 'cbBTC': 2855.9289812}

## Pools découverts (profondeur en USD, 30 premiers)

| pool | DEX | paire | frais (ppm) | profondeur $ |
|---|---|---|---|---|
| `0x6c561B44…` | uniswap_v3 | WETH/USDC | 3000 | 146000733.76 |
| `0x6cDcb1C4…` | aerodrome | USDC/AERO | 3000 | 41943400.04 |
| `0x7AeA2E8A…` | uniswap_v3 | WETH/cbBTC | 500 | 18202569.35 |
| `0x01784ef3…` | aerodrome | WETH/VVV | 3000 | 16710647.94 |
| `0x70aCDF2A…` | aerodrome_slipstream | WETH/cbBTC | 2500 | 16315552.34 |
| `0x8c708056…` | uniswap_v3 | WETH/cbBTC | 3000 | 10400686.13 |
| `0xfBB6Eed8…` | uniswap_v3 | USDC/cbBTC | 500 | 9761165.71 |
| `0x4e962BB3…` | aerodrome_slipstream | USDC/cbBTC | 400 | 9205184.18 |
| `0xd0b53D92…` | uniswap_v3 | WETH/USDC | 500 | 9056987.05 |
| `0xb2cc224c…` | aerodrome_slipstream | WETH/USDC | 609 | 8302348.66 |
| `0x3e66e55e…` | aerodrome_slipstream | USDC/cbBTC | 332 | 7856669.87 |
| `0xcDAC0d6c…` | aerodrome | WETH/USDC | 3000 | 5487489.96 |
| `0xC211e1f8…` | pancakeswap_v3 | WETH/cbBTC | 100 | 5327313.5 |
| `0x6446021F…` | aerodrome_slipstream | WETH/superOETHb | 400 | 5235627.55 |
| `0xbBf71AAD…` | aerodrome | fBOMB/AERO | 10000 | 5130975.79 |
| `0x861A2922…` | aerodrome_slipstream | WETH/wstETH | 90 | 4819252.23 |
| `0x21594b99…` | aerodrome | VIRTUAL/WETH | 10000 | 4622279.75 |
| `0x9785eF59…` | aerodrome_slipstream | WETH/USDT | 406 | 4468894.8 |
| `0x72AB388E…` | pancakeswap_v3 | WETH/USDC | 100 | 4445728.21 |
| `0xd9eDC75a…` | aerodrome | WETH/KTA | 3000 | 4085116.71 |
| `0xBE00fF35…` | aerodrome_slipstream | USDC/AERO | 10000 | 3956316.98 |
| `0x7f670f78…` | aerodrome | WETH/AERO | 10000 | 3337332.85 |
| `0x47cA96Ea…` | aerodrome_slipstream | cbETH/WETH | 60 | 2910439.13 |
| `0xeC558e48…` | uniswap_v3 | USDC/cbBTC | 3000 | 2841231.63 |
| `0x516025F6…` | aerodrome_slipstream | USDC/BtcUSD | 1000 | 2766881.81 |
| `0xdFe5F275…` | aerodrome_slipstream | AERO/cbBTC | 750 | 2624859.08 |
| `0x0392B12a…` | aerodrome_slipstream | WETH/ZEN | 1500 | 2563349.91 |
| `0x7eC6C9D9…` | aerodrome_slipstream | WETH/VVV | 2700 | 2540204.99 |
| `0x5447F7FE…` | aerodrome | WETH/FAI | 10000 | 2234422.97 |
| `0xB5F0b4aE…` | aerodrome_slipstream | WETH/MORPHO | 2700 | 2174265.35 |

Empreinte de configuration : `5ac48b43cfe8a100` (toute modification des adresses exige une nouvelle vérification).