# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T14:56:04+00:00 ; durée 42.94 min ; blocs 53117317 → 53118607 (1252 vus)

## Connexion
- Requêtes RPC : 15536 ; erreurs : 55 ; latence p50/p95 : 94.0/857.1 ms
- Rafraîchissements d'état : 1252 ; âge des données au dernier bloc : 4.01 s ; changements de frais LP observés (pools à frais dynamiques) : 3968
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 14286 ; cycles déclenchés par événement : 1021 ; avance médiane sur le rafraîchissement multicall : 406 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,316.64 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 529 pools, 304 jetons, 19426 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 128, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 341, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 3 → gardés 529 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2307.602823, 'cbBTC': 79842.460004, 'AERO': 0.67568}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,872,256 | 2,316.635836 | 53118607 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,719,350 | 0.028949 | 53118607 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,156,955 | 0.028964 | 53118607 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,466,863 | 0.000012 | 53118607 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,847,297 | 92.774369 | 53118607 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,317,870 | 2,320.236877 | 53118607 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,153,999 | 1.455034 | 53118607 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,004,560 | 0.001658 | 53118607 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,350,414 | 0.028943 | 53118607 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 549 | 5,334,626 | 2,319.795649 | 53118607 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,456,410 | 2,319.676751 | 53118607 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,211,594 | 0.999582 | 53118607 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,796,519 | 34,852.241980 | 53118607 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,362,069 | 2,316.840625 | 53118607 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,198,593 | 0.028949 | 53118607 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,501,342 | 92.794697 | 53118607 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 2,474,761 | 0.000012 | 53118607 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,203,100 | 404.593218 | 53118607 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,120,350 | 1,210,234.968788 | 53118607 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,887,390 | 0.000012 | 53118607 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,881,492 | 0.000000 | 53118607 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,816,384 | 0.018449 | 53118607 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,713,353 | 0.000012 | 53118607 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 1,697,322 | 0.000012 | 53118607 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,551,917 | 0.000265 | 53118607 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,509,133 | 0.005881 | 53118607 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,402 | 0.825253 | 53118607 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53118607 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,444,091 | 3,371.453454 | 53118607 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,368,728 | 13,985.337987 | 53118607 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,231,562 | 0.000267 | 53118607 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,560 | 65.119739 | 53118607 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,218,837 | 3,391.667395 | 53118607 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,209,691 | 2,320.034670 | 53118607 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,166,651 | 0.000000 | 53118607 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,135,040 | 1,092,963.972182 | 53118607 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,130,688 | 37,583,073.447680 | 53118607 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,105,389 | 498,453.331873 | 53118607 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,067,141 | 20,085,608.129299 | 53118607 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,065,477 | 72,445.739323 | 53118607 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,055,881 | 56.181041 | 53118607 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,030,105 | 17.436035 | 53118607 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 975,652 | 0.039958 | 53118607 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 941,732 | 2,311.179728 | 53118607 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 905,728 | 2.308515 | 53118607 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,773 | 0.000557 | 53118607 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/MORPHO | 3000 | 884,391 | 1,133.574793 | 53118607 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 883,784 | 16.957516 | 53118607 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 879,097 | 17.968496 | 53118607 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 869,635 | 93.363735 | 53118607 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 844,210 | 2,316.313906 | 53118607 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 805,773 | 0.000009 | 53118607 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 799,107 | 0.057274 | 53118607 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 784,373 | 0.803142 | 53118607 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 744,094 | 0.620433 | 53118607 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 730,954 | 4,741,912.428264 | 53118607 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 700,405 | 137,702.948760 | 53118607 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 698,257 | 0.613395 | 53118607 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 690,815 | 494,433.836661 | 53118607 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 681,738 | 0.110889 | 53118607 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 2272 ; routes examinées : 44135872 ; candidats optimisés : 128286 ; net attendu > 0 : 374 ; dernier cycle 79.0 ms
- Rejets (moteur) : {'spread_below_threshold': 43312247, 'liquidity_below_min': 651751, 'negative_expected_net': 127912, 'unquotable': 41316, 'borrow_bound_too_small': 2272}
- Enregistrements de la session : 128286 ; net attendu > 0 : 374 ; simulés (eth_call de la vraie tx) : 20 (ok 3, échec 17) ; étiquettes ghost N+1 : 0/17 positives
- Décisions : {'REJECTED': 128286} ; motifs de rejet : {'below_safety_margin': 325, 'negative_expected_net': 127912, 'p_lower_below_threshold': 318, 'price_impact': 4, 'reliability_not_demonstrated': 56, 'simulation_failed': 17, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53118454 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,957.544562 USDC | 0.246475 USDC | 0.000000 USDC | 0.005575 USDC | 0.240900 USDC (0.2216 €) | — | 1.23 | 0.022 (n=95) | REJECTED | below_safety_margin(240900<391508), p_lower_below_threshold(0.02<0.75) |
| 53118454 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.844193 WETH | 0.000106 WETH | 0.000000 WETH | 0.000002 WETH | 0.000104 WETH (0.2214 €) | — | 1.23 | 0.022 (n=95) | REJECTED | below_safety_margin(103914578896718<168838500260664), p_lower_below_threshold(0.02<0.75) |
| 53118454 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,607.937014 USDC | 0.166668 USDC | 0.000000 USDC | 0.005224 USDC | 0.161444 USDC (0.1485 €) | — | 1.00 | 0.022 (n=95) | REJECTED | below_safety_margin(161444<321587), p_lower_below_threshold(0.02<0.75) |
| 53118454 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.695940 WETH | 0.000072 WETH | 0.000000 WETH | 0.000002 WETH | 0.000070 WETH (0.1484 €) | — | 1.00 | 0.022 (n=95) | REJECTED | below_safety_margin(69637879384958<139188046494659), p_lower_below_threshold(0.02<0.75) |
| 53117984 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 86.226081 USDC | 0.161516 USDC | 0.000000 USDC | 0.005222 USDC | 0.156294 USDC (0.1438 €) | — | 18.13 | 0.000 (n=52) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53118377 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,240.658245 USDC | 0.099339 USDC | 0.000000 USDC | 0.005572 USDC | 0.093767 USDC (0.0863 €) | — | 0.76 | 0.022 (n=95) | REJECTED | below_safety_margin(93767<248131), p_lower_below_threshold(0.02<0.75) |
| 53118377 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.537206 WETH | 0.000043 WETH | 0.000000 WETH | 0.000002 WETH | 0.000040 WETH (0.0860 €) | — | 0.75 | 0.022 (n=95) | REJECTED | below_safety_margin(40441239565660<107441233745586), p_lower_below_threshold(0.02<0.75) |
| 53118362 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 65.570830 USDC | 0.094423 USDC | 0.000000 USDC | 0.005574 USDC | 0.088849 USDC (0.0817 €) | — | 13.55 | 0.000 (n=53) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 166.418370 USDC | 0.044255 USDC | 0.000000 USDC | 0.001203 USDC | 0.043052 USDC (0.0396 €) | — | 2.59 | 0.138 (n=346) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.071718 WETH | 0.000019 WETH | 0.000000 WETH | 0.000001 WETH | 0.000019 WETH (0.0395 €) | 0.000019 WETH | 2.59 | 0.138 (n=346) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53118438 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 103.765844 USDC | 0.040232 USDC | 0.000000 USDC | 0.006988 USDC | 0.033244 USDC (0.0306 €) | — | 3.20 | 0.087 (n=284) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53118437 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 103.765844 USDC | 0.040232 USDC | 0.000000 USDC | 0.006988 USDC | 0.033244 USDC (0.0306 €) | — | 3.20 | 0.087 (n=284) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53118438 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001142 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0302 €) | — | 3.59 | 0.087 (n=284) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53118437 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001142 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0302 €) | — | 3.59 | 0.087 (n=284) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53117512 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 493.169353 USDC | 0.029918 USDC | 0.000000 USDC | 0.001203 USDC | 0.028715 USDC (0.0264 €) | — | 0.58 | 0.138 (n=346) | REJECTED | below_safety_margin(28715<98633), p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.214196 WETH | 0.000013 WETH | 0.000000 WETH | 0.000001 WETH | 0.000012 WETH (0.0261 €) | — | 0.57 | 0.138 (n=346) | REJECTED | below_safety_margin(12232716902053<42839285508129), p_lower_below_threshold(0.14<0.75) |
| 53117512 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005431 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0257 €) | — | 0.64 | 0.138 (n=346) | REJECTED | below_safety_margin(35<108), p_lower_below_threshold(0.14<0.75) |
| 53118438 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001254 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0235 €) | — | 2.55 | 0.137 (n=348) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53118437 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001254 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0235 €) | — | 2.55 | 0.137 (n=348) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53118438 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.042689 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0228 €) | — | 2.51 | 0.137 (n=348) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53118437 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.042689 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0228 €) | — | 2.51 | 0.137 (n=348) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53118454 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 492.494503 USDC | 0.028677 USDC | 0.000000 USDC | 0.005224 USDC | 0.023453 USDC (0.0216 €) | — | 0.48 | 0.022 (n=95) | REJECTED | below_safety_margin(23453<98498), p_lower_below_threshold(0.02<0.75) |
| 53118454 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006201 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0213 €) | — | 0.47 | 0.022 (n=95) | REJECTED | below_safety_margin(29<124), p_lower_below_threshold(0.02<0.75) |
| 53118438 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001045 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0213 €) | — | 2.78 | 0.180 (n=180) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53118437 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001045 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0213 €) | — | 2.78 | 0.180 (n=180) | REJECTED | p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 2641 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
