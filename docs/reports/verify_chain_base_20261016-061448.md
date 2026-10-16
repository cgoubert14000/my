# Vérification du réseau `base` (chain id 8453) — 2026-10-16 06:14:48

RPC : `base-rpc.publicnode.com` · verdict : **TOUTES LES VÉRIFICATIONS BLOQUANTES PASSENT**

## Réseau
- block : 52670970
- block_time_measured_s : 2.0
- block_time_config_s : 2.0
- base_fee_gwei : 0.005
- priority_fee_gwei : 0.001
- latency_p50_ms : 55.1
- latency_max_ms : 73.5
- head_age_s : 2.5
- l1_fee_900B_eth : 4.997704841e-09
- native_price_usd : 2445.8566664049044

## Vérifications
- ✅ `rpc_reachable` — base-rpc.publicnode.com in 81 ms
- ✅ `chain_id` — rpc=8453 config=8453
- ✅ `block_time` — measured 2.00 s vs config 2.0 s
- ✅ `head_fresh` — head age 2.5 s
- ✅ `rpc_latency` — p50 55 ms, max 73 ms
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
- ✅ `factory:uniswap_v2` — V2 allPairsLength=3070108
- ✅ `factory:sushiswap_v2` — V2 allPairsLength=6131
- ✅ `factory:sushiswap_v3` — V3 feeAmountTickSpacing(3000)=60
- ✅ `factory:pancakeswap_v3` — V3 feeAmountTickSpacing(2500)=50
- ✅ `factory:pancakeswap_v2` — V2 allPairsLength=36345
- ✅ `factory:aerodrome` — Solidly allPoolsLength=29783
- ✅ `factory:aerodrome_slipstream` — Slipstream tickSpacingToFee(100)=500
- ✅ `l1_fee_oracle` — getL1FeeUpperBound(900 B) = 0.000000005 ETH
- ✅ `pool_discovery` — 579 pools: {'uniswap_v3': 138, 'aerodrome': 237, 'aerodrome_slipstream': 154, 'pancakeswap_v3': 32, 'uniswap_v2': 14, 'sushiswap_v2': 1, 'sushiswap_v3': 3}
- ✅ `pools_with_depth` — 468 pools ≥ 20 000 $ (deepest: WETH/USDC uniswap_v3 146827598.28 $)
- ✅ `native_price` — ETH ≈ 2445.8566664049044 $ (from the deepest WETH/stable pool)
- ✅ `flash:MORPHO` — fee 0.0 bps, capacity WETH 82,306.53, USDC 237,397,361.03, cbBTC 39,778.52
- ✅ `flash:BALANCER_V2` — fee 0.0 bps, capacity WETH 19.48, USDC 68,007.29, cbBTC 0.02
- ✅ `flash:AAVE_V3` — fee 5.0 bps, capacity WETH 19,593.80, USDC 19,710,478.41, cbBTC 2,802.59
- ✅ `flash_any_capacity` — at least one provider can lend a borrowable token

## Fournisseurs de flash loan (capacité en direct)
- MORPHO `0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb` : frais 0.0 bps, vérifié=True, capacité {'WETH': 82306.53100938513, 'USDC': 237397361.028118, 'cbBTC': 39778.51903375}
- BALANCER_V2 `0xBA12222222228d8Ba445958a75a0704d566BF2C8` : frais 0.0 bps, vérifié=True, capacité {'WETH': 19.480247330511723, 'USDC': 68007.293456, 'cbBTC': 0.02228416}
- AAVE_V3 `0xA238Dd80C259a72e81d7e4664a9801593F98d1c5` : frais 5.0 bps, vérifié=True, capacité {'WETH': 19593.79529266167, 'USDC': 19710478.413009, 'cbBTC': 2802.58549165}

## Pools découverts (profondeur en USD, 30 premiers)

| pool | DEX | paire | frais (ppm) | profondeur $ |
|---|---|---|---|---|
| `0x6c561B44…` | uniswap_v3 | WETH/USDC | 3000 | 146827598.28 |
| `0x6cDcb1C4…` | aerodrome | USDC/AERO | 3000 | 47400167.98 |
| `0x7AeA2E8A…` | uniswap_v3 | WETH/cbBTC | 500 | 18501172.11 |
| `0x01784ef3…` | aerodrome | WETH/VVV | 3000 | 16540964.87 |
| `0x70aCDF2A…` | aerodrome_slipstream | WETH/cbBTC | 2500 | 16475859.19 |
| `0x8c708056…` | uniswap_v3 | WETH/cbBTC | 3000 | 10588287.51 |
| `0xfBB6Eed8…` | uniswap_v3 | USDC/cbBTC | 500 | 9747236.48 |
| `0xd0b53D92…` | uniswap_v3 | WETH/USDC | 500 | 9132710.29 |
| `0x3e66e55e…` | aerodrome_slipstream | USDC/cbBTC | 336 | 8089865.86 |
| `0xb2cc224c…` | aerodrome_slipstream | WETH/USDC | 579 | 7273298.27 |
| `0x4e962BB3…` | aerodrome_slipstream | USDC/cbBTC | 436 | 6360205.39 |
| `0xBE00fF35…` | aerodrome_slipstream | USDC/AERO | 10000 | 5753797.63 |
| `0xbBf71AAD…` | aerodrome | fBOMB/AERO | 10000 | 5508345.22 |
| `0xcDAC0d6c…` | aerodrome | WETH/USDC | 3000 | 5444822.94 |
| `0xC211e1f8…` | pancakeswap_v3 | WETH/cbBTC | 100 | 5404750.3 |
| `0x6446021F…` | aerodrome_slipstream | WETH/superOETHb | 400 | 5226371.91 |
| `0x861A2922…` | aerodrome_slipstream | WETH/wstETH | 90 | 4888907.88 |
| `0x21594b99…` | aerodrome | VIRTUAL/WETH | 10000 | 4754244.74 |
| `0x72AB388E…` | pancakeswap_v3 | WETH/USDC | 100 | 4407780.73 |
| `0xd9eDC75a…` | aerodrome | WETH/KTA | 3000 | 4063608.7 |
| `0x7f670f78…` | aerodrome | WETH/AERO | 10000 | 3586174.05 |
| `0x47cA96Ea…` | aerodrome_slipstream | cbETH/WETH | 60 | 3044089.44 |
| `0xeC558e48…` | uniswap_v3 | USDC/cbBTC | 3000 | 2847666.04 |
| `0x516025F6…` | aerodrome_slipstream | USDC/BtcUSD | 1000 | 2766881.81 |
| `0x0392B12a…` | aerodrome_slipstream | WETH/ZEN | 1500 | 2684120.97 |
| `0x7eC6C9D9…` | aerodrome_slipstream | WETH/VVV | 2700 | 2671893.69 |
| `0xB5F0b4aE…` | aerodrome_slipstream | WETH/MORPHO | 2712 | 2558384.89 |
| `0xdFe5F275…` | aerodrome_slipstream | AERO/cbBTC | 2700 | 2471603.54 |
| `0x5447F7FE…` | aerodrome | WETH/FAI | 10000 | 2294491.26 |
| `0x2a1463Ce…` | aerodrome | USDC/MAI (stable) | 3000 | 2111735.83 |

Empreinte de configuration : `5ac48b43cfe8a100` (toute modification des adresses exige une nouvelle vérification).