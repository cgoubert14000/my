# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T07:52:30+00:00 ; durée 141.78 min ; blocs 53188044 → 53192297 (4111 vus)

## Connexion
- Requêtes RPC : 48964 ; erreurs : 80 ; latence p50/p95 : 195.7/1,597.5 ms
- Rafraîchissements d'état : 4111 ; âge des données au dernier bloc : 5.18 s ; changements de frais LP observés (pools à frais dynamiques) : 2937
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 22306 ; cycles déclenchés par événement : 3885 ; avance médiane sur le rafraîchissement multicall : 657 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,355.40 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 521 pools, 302 jetons, 18962 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 121, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 184 (rejetés 2) → 589 jetons ; pools candidats 3762 (énumérés 330, par paires 0), mesurés 523, sous le plancher de 10000.0 $ : 2 → gardés 521 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2356.459313, 'cbBTC': 80857.377983, 'AERO': 0.694089}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,148,899 | 2,355.400261 | 53192298 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,713,595 | 0.029088 | 53192298 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,646,969 | 0.000012 | 53192298 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,505,170 | 0.029105 | 53192298 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,444,420 | 2,354.284117 | 53192298 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,277,158 | 98.317512 | 53192298 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,064,395 | 0.001648 | 53192298 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,873,493 | 1.437405 | 53192298 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,743,950 | 0.029093 | 53192298 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,046,353 | 2,355.109071 | 53192298 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,483,964 | 2,355.216267 | 53192298 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,263,681 | 0.998869 | 53192298 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,780,864 | 36,327.350084 | 53192298 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 2,962,466 | 0.029107 | 53192298 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,521,255 | 98.303400 | 53192298 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 2,458,740 | 0.000012 | 53192298 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,149,976 | 1,216,833.680738 | 53192298 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,922,498 | 2,354.963798 | 53192298 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,844,190 | 0.019064 | 53192298 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,829,272 | 0.000000 | 53192298 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,797,151 | 397.026320 | 53192298 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 1,700,208 | 0.000012 | 53192298 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,693,344 | 0.000012 | 53192298 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,693,305 | 0.000012 | 53192298 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,509,350 | 0.005763 | 53192298 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,274 | 1.655260 | 53192298 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,231 | 0.826726 | 53192298 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,457,309 | 3,383.603315 | 53192298 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,397,851 | 13,653.161971 | 53192298 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,258,064 | 0.000268 | 53192298 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,242,367 | 2,354.220036 | 53192298 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,203,393 | 3,369.352247 | 53192298 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,194,374 | 68.117912 | 53192298 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,189,179 | 0.000267 | 53192298 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,167,583 | 1,067,162.121901 | 53192298 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,165,387 | 36,230,754.358062 | 53192298 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,165,016 | 0.000000 | 53192298 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,126,183 | 500,862.203904 | 53192298 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,081,531 | 72,468.020081 | 53192298 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,065,316 | 21,185,769.720926 | 53192298 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,059,935 | 55.720296 | 53192298 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,046,194 | 16.720780 | 53192298 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 987,758 | 97.628880 | 53192298 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 986,926 | 0.041750 | 53192298 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 940,979 | 2,342.370626 | 53192298 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 932,058 | 1,062.370365 | 53192298 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 910,370 | 0.000560 | 53192298 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 889,282 | 2.313703 | 53192298 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 882,640 | 17.859977 | 53192298 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 851,835 | 17.446284 | 53192298 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 850,755 | 2,355.292413 | 53192298 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 811,808 | 0.059215 | 53192298 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 797,479 | 0.803180 | 53192298 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 756,926 | 0.000009 | 53192298 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 754,113 | 0.629669 | 53192298 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 750,887 | 4,645,449.046906 | 53192298 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 713,848 | 137,080.383040 | 53192298 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 699,768 | 499,029.209747 | 53192298 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 672,349 | 0.108278 | 53192298 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 667,880 | 0.562522 | 53192298 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 7995 ; routes examinées : 151601190 ; candidats optimisés : 460506 ; net attendu > 0 : 158 ; dernier cycle 274.7 ms
- Rejets (moteur) : {'spread_below_threshold': 149488213, 'liquidity_below_min': 1460998, 'negative_expected_net': 460348, 'borrow_bound_too_small': 127967, 'pool_quarantined': 62814, 'cycle_budget_exhausted': 692}
- Enregistrements de la session : 460506 ; net attendu > 0 : 158 ; simulés (eth_call de la vraie tx) : 21 (ok 1, échec 20) ; étiquettes ghost N+1 : 1/19 positives
- Décisions : {'REJECTED': 460506} ; motifs de rejet : {'below_safety_margin': 20, 'negative_expected_net': 460348, 'p_lower_below_threshold': 106, 'price_impact': 41, 'reliability_not_demonstrated': 52, 'simulation_failed': 20}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53188413 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 139.105675 USDC | 6.970905 USDC | 0.000000 USDC | 0.004965 USDC | 6.965940 USDC (6.4087 €) | — | 500.77 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53190872 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→WETH | 0.030970 WETH | 0.001205 WETH | 0.000000 WETH | 0.000002 WETH | 0.001203 WETH (2.6071 €) | — | 388.47 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53190872 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.035468 WETH | 0.000712 WETH | 0.000000 WETH | 0.000003 WETH | 0.000709 WETH (1.5369 €) | — | 199.97 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 83.365828 USDC | 1.674102 USDC | 0.000000 USDC | 0.007083 USDC | 1.667019 USDC (1.5337 €) | — | 199.96 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53190872 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.034928 WETH | 0.000707 WETH | 0.000000 WETH | 0.000003 WETH | 0.000704 WETH (1.5248 €) | — | 201.46 | 0.000 (n=36) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 82.080099 USDC | 1.660987 USDC | 0.000000 USDC | 0.007441 USDC | 1.653546 USDC (1.5213 €) | — | 201.46 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.034548 WETH | 0.000694 WETH | 0.000000 WETH | 0.000003 WETH | 0.000691 WETH (1.4974 €) | — | 200.01 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 81.200053 USDC | 1.631135 USDC | 0.000000 USDC | 0.007083 USDC | 1.624052 USDC (1.4941 €) | — | 200.01 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.028014 WETH | 0.000560 WETH | 0.000000 WETH | 0.000003 WETH | 0.000557 WETH (1.2070 €) | — | 198.82 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 65.812975 USDC | 1.315568 USDC | 0.000000 USDC | 0.007083 USDC | 1.308485 USDC (1.2038 €) | — | 198.82 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.027940 WETH | 0.000558 WETH | 0.000000 WETH | 0.000003 WETH | 0.000555 WETH (1.2035 €) | — | 198.77 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 65.636014 USDC | 1.311744 USDC | 0.000000 USDC | 0.007083 USDC | 1.304661 USDC (1.2003 €) | — | 198.77 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53190872 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.025335 WETH | 0.000501 WETH | 0.000000 WETH | 0.000003 WETH | 0.000498 WETH (1.0798 €) | — | 196.68 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 59.386962 USDC | 1.175437 USDC | 0.000000 USDC | 0.007441 USDC | 1.167996 USDC (1.0746 €) | — | 196.68 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.022567 WETH | 0.000453 WETH | 0.000000 WETH | 0.000003 WETH | 0.000450 WETH (0.9750 €) | — | 199.38 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 52.612578 USDC | 1.056021 USDC | 0.000000 USDC | 0.007083 USDC | 1.048938 USDC (0.9650 €) | — | 199.37 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.029300 WETH | 0.000161 WETH | 0.000000 WETH | 0.000003 WETH | 0.000158 WETH (0.3435 €) | — | 54.09 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.029241 WETH | 0.000161 WETH | 0.000000 WETH | 0.000003 WETH | 0.000158 WETH (0.3430 €) | — | 54.13 | 0.000 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53190406 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 68.839715 USDC | 0.379669 USDC | 0.000000 USDC | 0.007081 USDC | 0.372588 USDC (0.3428 €) | — | 54.12 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53190406 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 68.639366 USDC | 0.379194 USDC | 0.000000 USDC | 0.007081 USDC | 0.372113 USDC (0.3423 €) | — | 54.21 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.029027 WETH | 0.000158 WETH | 0.000000 WETH | 0.000003 WETH | 0.000155 WETH (0.3369 €) | — | 53.55 | 0.000 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53190406 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 68.252205 USDC | 0.372548 USDC | 0.000000 USDC | 0.007081 USDC | 0.365467 USDC (0.3362 €) | — | 53.55 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.027508 WETH | 0.000143 WETH | 0.000000 WETH | 0.000003 WETH | 0.000140 WETH (0.3024 €) | — | 50.71 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 64.762850 USDC | 0.335283 USDC | 0.000000 USDC | 0.007081 USDC | 0.328202 USDC (0.3019 €) | — | 50.68 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.027467 WETH | 0.000142 WETH | 0.000000 WETH | 0.000003 WETH | 0.000139 WETH (0.3006 €) | — | 50.49 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2911 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
