# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T18:28:17+00:00 ; durée 136.17 min ; blocs 53380086 → 53384173 (3574 vus)

## Connexion
- Requêtes RPC : 44232 ; erreurs : 0 ; latence p50/p95 : 334.8/1,374.2 ms
- Rafraîchissements d'état : 3574 ; âge des données au dernier bloc : 6.4 s ; changements de frais LP observés (pools à frais dynamiques) : 1941
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 28783 ; cycles déclenchés par événement : 4619 ; avance médiane sur le rafraîchissement multicall : 1,403 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,264.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 289 jetons, 18734 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 111, aerodrome 206, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3737 (énumérés 315, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2264.227713, 'cbBTC': 77906.671325, 'AERO': 0.64119}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,666,418 | 2,264.225466 | 53384172 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,174,867 | 0.029043 | 53384172 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,305,285 | 0.000013 | 53384172 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,162,520 | 0.029102 | 53384172 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,888,028 | 2,261.422622 | 53384173 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,843,015 | 98.475029 | 53384172 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,670,835 | 0.001586 | 53384172 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,614,302 | 1.563447 | 53384172 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,162,169 | 0.029054 | 53384172 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,104,960 | 0.998845 | 53384172 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,048,617 | 2,262.167178 | 53384172 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,016,957 | 2,262.277221 | 53384172 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,541,211 | 38,261.586885 | 53384172 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,701,392 | 0.029087 | 53384172 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,387,689 | 98.506707 | 53384172 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,181,186 | 0.000013 | 53384172 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,089,572 | 1,190,402.585861 | 53384172 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,772,516 | 0.018356 | 53384172 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,756,496 | 0.000000 | 53384172 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,638,390 | 0.000013 | 53384173 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,583,807 | 0.000013 | 53384172 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,554,598 | 426.523286 | 53384172 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,533,296 | 1.503377 | 53384172 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,507,012 | 2,262.007070 | 53384172 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,184 | 0.826015 | 53384172 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,432,622 | 3,539.141623 | 53384172 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,380,916 | 2,268.336317 | 53384172 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,344,259 | 0.005255 | 53384172 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,329,998 | 2,261.505799 | 53384172 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,309,320 | 14,666.161467 | 53384172 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,309,292 | 0.000013 | 53384172 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,017 | 71.105107 | 53384172 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,122,640 | 35,875,424.896823 | 53384172 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,072,741 | 510,696.510158 | 53384172 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,054,425 | 0.000000 | 53384172 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,014,637 | 22,273,804.776113 | 53384172 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 996,585 | 97.851577 | 53384172 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 990,651 | 19.469434 | 53384172 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 976,693 | 82,040.231415 | 53384172 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 956,471 | 1,169,036.200386 | 53384172 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 949,035 | 999.407650 | 53384172 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 943,738 | 0.043558 | 53384172 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 936,248 | 71.418888 | 53384172 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 923,206 | 2,252.785626 | 53384172 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 872,736 | 3,514.646394 | 53384172 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,699 | 0.000546 | 53384172 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 838,043 | 19.440291 | 53384172 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 819,920 | 0.060462 | 53384172 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 767,230 | 0.801881 | 53384172 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 728,230 | 0.000261 | 53384172 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 727,862 | 0.593404 | 53384172 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 712,454 | 4,773,323.447973 | 53384172 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 693,512 | 0.000008 | 53384172 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 686,216 | 137,337.013674 | 53384172 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 681,395 | 0.582155 | 53384172 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 666,279 | 514,917.043320 | 53384172 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 659,536 | 2.340198 | 53384172 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 611,110 | 0.092701 | 53384172 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 607,969 | 0.915407 | 53384172 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| uniswap_v3 | FLOCK/USDC | 3000 | 568,606 | 0.038896 | 53384172 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 8192 ; routes examinées : 153468928 ; candidats optimisés : 447289 ; net attendu > 0 : 291 ; dernier cycle 150.8 ms
- Rejets (moteur) : {'spread_below_threshold': 151504524, 'liquidity_below_min': 1492423, 'negative_expected_net': 446998, 'unquotable': 16380, 'borrow_bound_too_small': 8192, 'cycle_budget_exhausted': 120}
- Enregistrements de la session : 447289 ; net attendu > 0 : 291 ; simulés (eth_call de la vraie tx) : 19 (ok 9, échec 10) ; étiquettes ghost N+1 : 0/14 positives
- Décisions : {'REJECTED': 447289} ; motifs de rejet : {'below_safety_margin': 234, 'negative_expected_net': 446998, 'p_lower_below_threshold': 227, 'reliability_not_demonstrated': 64, 'simulation_failed': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53380235 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 158.478005 USDC | 0.223007 USDC | 0.000000 USDC | 0.007148 USDC | 0.215859 USDC (0.1986 €) | — | 13.62 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53380235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.069998 WETH | 0.000098 WETH | 0.000000 WETH | 0.000003 WETH | 0.000095 WETH (0.1983 €) | — | 13.60 | 0.017 (n=85) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53380235 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 156.834999 USDC | 0.211689 USDC | 0.000000 USDC | 0.007148 USDC | 0.204541 USDC (0.1882 €) | — | 13.04 | 0.065 (n=103) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53380235 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.069172 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000090 WETH (0.1879 €) | — | 13.04 | 0.065 (n=103) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53380235 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 155.799299 USDC | 0.208980 USDC | 0.000000 USDC | 0.007148 USDC | 0.201832 USDC (0.1857 €) | — | 12.95 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53380235 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.068819 WETH | 0.000092 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1854 €) | — | 12.93 | 0.017 (n=85) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53381335 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.570288 WETH | 0.000070 WETH | 0.000000 WETH | 0.000003 WETH | 0.000067 WETH (0.1393 €) | — | 1.17 | 0.000 (n=18) | REJECTED | below_safety_margin(66872132995536<114057586661070), reliability_not_demonstrated |
| 53381335 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.015460 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1391 €) | — | 1.25 | 0.000 (n=18) | REJECTED | below_safety_margin(194<309), reliability_not_demonstrated |
| 53381335 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,363.148149 USDC | 0.158575 USDC | 0.000000 USDC | 0.007491 USDC | 0.151084 USDC (0.1390 €) | — | 1.11 | 0.000 (n=18) | REJECTED | below_safety_margin(151084<272629), reliability_not_demonstrated |
| 53381677 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,192.811264 USDC | 0.154774 USDC | 0.000000 USDC | 0.007146 USDC | 0.147628 USDC (0.1358 €) | — | 1.24 | 0.138 (n=691) | REJECTED | below_safety_margin(147628<238562), p_lower_below_threshold(0.14<0.75) |
| 53381678 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,192.811264 USDC | 0.154774 USDC | 0.000000 USDC | 0.007146 USDC | 0.147628 USDC (0.1358 €) | — | 1.24 | 0.138 (n=691) | REJECTED | below_safety_margin(147628<238562), p_lower_below_threshold(0.14<0.75) |
| 53381677 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.015042 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1355 €) | — | 1.26 | 0.138 (n=691) | REJECTED | below_safety_margin(189<300), p_lower_below_threshold(0.14<0.75) |
| 53381678 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.015042 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1355 €) | — | 1.26 | 0.138 (n=691) | REJECTED | below_safety_margin(189<300), p_lower_below_threshold(0.14<0.75) |
| 53381677 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.528775 WETH | 0.000068 WETH | 0.000000 WETH | 0.000003 WETH | 0.000065 WETH (0.1354 €) | — | 1.23 | 0.138 (n=691) | REJECTED | below_safety_margin(65014853912624<105755020338891), p_lower_below_threshold(0.14<0.75) |
| 53381678 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.528775 WETH | 0.000068 WETH | 0.000000 WETH | 0.000003 WETH | 0.000065 WETH (0.1354 €) | — | 1.23 | 0.138 (n=691) | REJECTED | below_safety_margin(65014853912624<105755020338891), p_lower_below_threshold(0.14<0.75) |
| 53383267 | WETH→[uniswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.061918 WETH | 0.000063 WETH | 0.000000 WETH | 0.000002 WETH | 0.000061 WETH (0.1276 €) | — | 9.89 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53380235 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 100.256151 USDC | 0.139787 USDC | 0.000000 USDC | 0.006805 USDC | 0.132982 USDC (0.1223 €) | — | 13.26 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53380235 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.044238 WETH | 0.000062 WETH | 0.000000 WETH | 0.000003 WETH | 0.000059 WETH (0.1223 €) | — | 13.27 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53381677 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,226.014420 USDC | 0.138233 USDC | 0.000000 USDC | 0.007146 USDC | 0.131087 USDC (0.1206 €) | — | 1.07 | 0.000 (n=18) | REJECTED | below_safety_margin(131087<245202), reliability_not_demonstrated |
| 53381678 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,226.014420 USDC | 0.138233 USDC | 0.000000 USDC | 0.007146 USDC | 0.131087 USDC (0.1206 €) | — | 1.07 | 0.000 (n=18) | REJECTED | below_safety_margin(131087<245202), reliability_not_demonstrated |
| 53381677 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.015090 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1204 €) | — | 1.11 | 0.000 (n=18) | REJECTED | below_safety_margin(168<301), reliability_not_demonstrated |
| 53381678 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.015090 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1204 €) | — | 1.11 | 0.000 (n=18) | REJECTED | below_safety_margin(168<301), reliability_not_demonstrated |
| 53381677 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.557458 WETH | 0.000061 WETH | 0.000000 WETH | 0.000003 WETH | 0.000058 WETH (0.1200 €) | — | 1.03 | 0.000 (n=18) | REJECTED | below_safety_margin(57601762593697<111491687483259), reliability_not_demonstrated |
| 53381678 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.557458 WETH | 0.000061 WETH | 0.000000 WETH | 0.000003 WETH | 0.000058 WETH (0.1200 €) | — | 1.03 | 0.000 (n=18) | REJECTED | below_safety_margin(57601762593697<111491687483259), reliability_not_demonstrated |
| 53381440 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.014041 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1104 €) | — | 1.10 | 0.000 (n=18) | REJECTED | below_safety_margin(154<280), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4145 ; taux observé 0.127 ; borne inférieure crédible (0.9) 0.121 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
