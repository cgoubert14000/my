# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T19:21:31+00:00 ; durée 189.39 min ; blocs 53380086 → 53385768 (4458 vus)

## Connexion
- Requêtes RPC : 57292 ; erreurs : 45 ; latence p50/p95 : 341.8/1,520.1 ms
- Rafraîchissements d'état : 4459 ; âge des données au dernier bloc : 3.73 s ; changements de frais LP observés (pools à frais dynamiques) : 3025
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 45273 ; cycles déclenchés par événement : 6784 ; avance médiane sur le rafraîchissement multicall : 1,306 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,259.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 289 jetons, 18734 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 111, aerodrome 206 (quarantaine 2), pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3737 (énumérés 315, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2264.227713, 'cbBTC': 77906.671325, 'AERO': 0.64119}
- Pools en quarantaine : 2 — aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 53385843; aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 53385843

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,447,942 | 2,259.030447 | 53385767 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,136,674 | 0.029054 | 53385767 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,316,996 | 0.000013 | 53385767 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,140,122 | 0.029102 | 53385767 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,874,443 | 2,256.596441 | 53385767 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,798,305 | 99.150894 | 53385767 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,642,435 | 0.001580 | 53385767 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,584,077 | 1.580308 | 53385767 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,150,356 | 0.029058 | 53385767 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,093,961 | 0.998850 | 53385767 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,042,124 | 2,257.328373 | 53385767 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,959,589 | 2,257.268973 | 53385767 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,532,181 | 38,281.188836 | 53385767 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,694,957 | 0.029087 | 53385767 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2784 | 2,373,720 | 99.168703 | 53385767 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,127,270 | 0.000013 | 53385767 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,084,778 | 1,190,402.585861 | 53385767 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,759,984 | 0.018136 | 53385767 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,752,453 | 0.000000 | 53385767 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,621,102 | 0.000013 | 53385767 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,581,433 | 0.000013 | 53385767 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,547,981 | 429.426292 | 53385767 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,533,296 | 1.503377 | 53385767 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,505,283 | 2,259.025498 | 53385767 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,184 | 0.826015 | 53385767 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,422,558 | 3,563.917446 | 53385767 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,379,330 | 2,260.402874 | 53385767 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,335,041 | 0.005226 | 53385767 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,323,528 | 2,256.535607 | 53385767 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,306,794 | 0.000013 | 53385767 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,302,310 | 14,740.416038 | 53385767 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,169,003 | 71.106813 | 53385767 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,121,168 | 35,770,198.036016 | 53385767 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,067,867 | 513,887.132831 | 53385767 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,051,980 | 0.000000 | 53385767 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,012,188 | 22,273,804.776113 | 53385767 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 990,589 | 98.447427 | 53385767 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 989,231 | 19.550833 | 53385767 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 974,604 | 82,014.611992 | 53385767 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 953,468 | 1,171,019.975226 | 53385767 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 948,355 | 69.607008 | 53385767 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 943,748 | 1,008.076669 | 53385767 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 922,317 | 2,252.785626 | 53385767 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 914,520 | 0.043936 | 53385767 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 867,075 | 3,537.252971 | 53385767 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 862,470 | 0.000546 | 53385767 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 833,853 | 19.589760 | 53385767 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,132 | 0.060496 | 53385767 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,470 | 0.801881 | 53385767 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 726,442 | 0.000261 | 53385767 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 726,376 | 0.587229 | 53385767 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 717,566 | 4,684,118.506591 | 53385767 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 688,966 | 135,631.441151 | 53385767 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 688,477 | 0.000008 | 53385767 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 681,662 | 0.582556 | 53385767 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 662,587 | 518,272.330291 | 53385767 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 658,023 | 2.340198 | 53385767 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 608,347 | 0.092059 | 53385767 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 606,498 | 0.915639 | 53385767 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,971 | 0.038868 | 53385767 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 11242 ; routes examinées : 210607628 ; candidats optimisés : 645214 ; net attendu > 0 : 1089 ; dernier cycle 309.9 ms
- Rejets (moteur) : {'spread_below_threshold': 207381073, 'liquidity_below_min': 2480729, 'negative_expected_net': 644125, 'pool_quarantined': 64638, 'unquotable': 24179, 'borrow_bound_too_small': 11242, 'cycle_budget_exhausted': 553}
- Enregistrements de la session : 645214 ; net attendu > 0 : 1089 ; simulés (eth_call de la vraie tx) : 51 (ok 15, échec 36) ; étiquettes ghost N+1 : 1/33 positives
- Décisions : {'REJECTED': 645214} ; motifs de rejet : {'below_safety_margin': 814, 'negative_expected_net': 644125, 'p_lower_below_threshold': 931, 'price_impact': 5, 'reliability_not_demonstrated': 158, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 1, 'simulation_failed': 36, 'stale_data': 150}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53385529 | WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.876972 WETH | 0.000108 WETH | 0.000000 WETH | 0.000003 WETH | 0.000105 WETH (0.2187 €) | — | 1.20 | 0.137 (n=703) | REJECTED | below_safety_margin(105126532557613<175394338841049), p_lower_below_threshold(0.14<0.75) |
| 53380235 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 158.478005 USDC | 0.223007 USDC | 0.000000 USDC | 0.007148 USDC | 0.215859 USDC (0.1986 €) | — | 13.62 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53380235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.069998 WETH | 0.000098 WETH | 0.000000 WETH | 0.000003 WETH | 0.000095 WETH (0.1983 €) | — | 13.60 | 0.017 (n=85) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53380235 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 156.834999 USDC | 0.211689 USDC | 0.000000 USDC | 0.007148 USDC | 0.204541 USDC (0.1882 €) | — | 13.04 | 0.065 (n=103) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53380235 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.069172 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000090 WETH (0.1879 €) | — | 13.04 | 0.065 (n=103) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53380235 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 155.799299 USDC | 0.208980 USDC | 0.000000 USDC | 0.007148 USDC | 0.201832 USDC (0.1857 €) | — | 12.95 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53380235 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.068819 WETH | 0.000092 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1854 €) | — | 12.93 | 0.017 (n=85) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53385529 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.587098 WETH | 0.000074 WETH | 0.000000 WETH | 0.000003 WETH | 0.000071 WETH (0.1478 €) | — | 1.21 | 0.137 (n=703) | REJECTED | below_safety_margin(71058742290886<117419624951970), p_lower_below_threshold(0.14<0.75) |
| 53385529 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.015779 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1474 €) | — | 1.31 | 0.137 (n=703) | REJECTED | below_safety_margin(206<315), p_lower_below_threshold(0.14<0.75) |
| 53385529 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,390.001571 USDC | 0.166242 USDC | 0.000000 USDC | 0.006794 USDC | 0.159448 USDC (0.1467 €) | — | 1.15 | 0.137 (n=703) | REJECTED | below_safety_margin(159448<278000), p_lower_below_threshold(0.14<0.75) |
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

## Fiabilité et décision
- Observations ghost : 4164 ; taux observé 0.127 ; borne inférieure crédible (0.9) 0.120 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
