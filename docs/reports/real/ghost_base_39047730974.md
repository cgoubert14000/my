# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T17:41:27+00:00 ; durée 93.37 min ; blocs 52731965 → 52734766 (2653 vus)

## Connexion
- Requêtes RPC : 33499 ; erreurs : 10 ; latence p50/p95 : 158.0/1,392.1 ms
- Rafraîchissements d'état : 2654 ; âge des données au dernier bloc : 1.32 s ; changements de frais LP observés (pools à frais dynamiques) : 3867
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 28774 ; cycles déclenchés par événement : 1404 ; avance médiane sur le rafraîchissement multicall : 1,673 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,403.19 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21110 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3916 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2411.894998, 'AERO': 0.849168, 'cbBTC': 81312.167025}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,898,882 | 2,403.188918 | 52734766 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,083,867 | 1.178574 | 52734766 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,885,714 | 0.029621 | 52734766 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,135,048 | 0.029612 | 52734766 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,778,478 | 107.049417 | 52734766 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,398,178 | 0.029634 | 52734766 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,741,319 | 0.000012 | 52734766 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,068,618 | 2,405.276177 | 52734766 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,030,169 | 0.000012 | 52734766 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,831,920 | 0.000012 | 52734766 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 609 | 7,207,054 | 2,405.648312 | 52734766 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,104,143 | 0.001659 | 52734766 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,393,382 | 2,404.325836 | 52734766 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,312,618 | 0.029617 | 52734766 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,221,726 | 0.025358 | 52734766 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,218,694 | 1.000855 | 52734766 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,803,619 | 0.802398 | 52734766 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,618,120 | 0.000273 | 52734766 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,462,922 | 1.172907 | 52734766 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,407,684 | 2,405.494117 | 52734766 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,406,778 | 0.998809 | 52734766 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,014,425 | 33,990.111181 | 52734766 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,383,658 | 2,820.409782 | 52734766 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 415 | 3,060,282 | 2,409.934215 | 52734766 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,902,550 | 1.141802 | 52734766 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,832,176 | 0.000012 | 52734766 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,746,487 | 0.000010 | 52734766 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,552,218 | 106.734190 | 52734766 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,279,488 | 407.612408 | 52734766 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,226,841 | 1,182,290.188062 | 52734766 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,133,434 | 1.123444 | 52734766 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,107,462 | 1.199039 | 52734766 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52734766 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/MORPHO | 2733 | 1,912,437 | 1,024.647269 | 52734766 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,848,160 | 15.930136 | 52734766 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,814,828 | 0.021938 | 52734766 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,801,051 | 0.000000 | 52734766 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,784,934 | 0.018042 | 52734766 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,774,454 | 0.000012 | 52734766 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,664,361 | 2.305565 | 52734766 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,535,976 | 0.916547 | 52734766 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,518,581 | 2,834.025413 | 52734766 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,513,383 | 1.105495 | 52734766 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,470,022 | 2,834.495515 | 52734766 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,811 | 0.826630 | 52734766 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,392,352 | 13,776.436661 | 52734766 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,353,883 | 0.000000 | 52734766 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,327,571 | 0.435668 | 52734766 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,302,167 | 0.004696 | 52734766 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,294,299 | 0.000271 | 52734766 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,248,228 | 62.367032 | 52734766 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,242,910 | 23.341717 | 52734766 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,237,556 | 1.131290 | 52734766 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/cbBTC | 3000 | 1,226,559 | 0.029642 | 52734766 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,212,245 | 1.105716 | 52734766 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,191,077 | 35,597,548.307300 | 52734766 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,181,625 | 2,405.392415 | 52734766 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,168,585 | 1,146,876.315919 | 52734766 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,219 | 511,211.436392 | 52734766 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,112,613 | 14.305875 | 52734766 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 4057 ; routes examinées : 85643270 ; candidats optimisés : 777372 ; net attendu > 0 : 224 ; dernier cycle 516.8 ms
- Rejets (moteur) : {'spread_below_threshold': 83857888, 'negative_expected_net': 777148, 'liquidity_below_min': 733696, 'pool_quarantined': 249022, 'cycle_budget_exhausted': 21238, 'borrow_bound_too_small': 4054}
- Enregistrements de la session : 777372 ; net attendu > 0 : 224 ; simulés (eth_call de la vraie tx) : 55 (ok 2, échec 53) ; étiquettes ghost N+1 : 0/34 positives
- Décisions : {'REJECTED': 777372} ; motifs de rejet : {'below_safety_margin': 166, 'negative_expected_net': 777148, 'p_lower_below_threshold': 156, 'price_impact': 68, 'reliability_not_demonstrated': 68, 'simulation_failed': 53}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52732232 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 264.379140 USDC | 0.953137 USDC | 0.000000 USDC | 0.005417 USDC | 0.947720 USDC (0.8719 €) | — | 35.85 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732691 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 82.007926 USDC | 0.093812 USDC | 0.000000 USDC | 0.005413 USDC | 0.088399 USDC (0.0813 €) | — | 10.78 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52733290 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 73.561974 USDC | 0.076184 USDC | 0.000000 USDC | 0.005410 USDC | 0.070774 USDC (0.0651 €) | — | 9.62 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52733325 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.429660 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0639 €) | — | 0.67 | 0.114 (n=81) | REJECTED | below_safety_margin(28823934244612<85931943319960), p_lower_below_threshold(0.11<0.75) |
| 52733326 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.429660 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0639 €) | — | 0.67 | 0.114 (n=81) | REJECTED | below_safety_margin(28823934244612<85931943319960), p_lower_below_threshold(0.11<0.75) |
| 52733325 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,030.836384 USDC | 0.076442 USDC | 0.000000 USDC | 0.007239 USDC | 0.069203 USDC (0.0637 €) | — | 0.67 | 0.114 (n=81) | REJECTED | below_safety_margin(69203<206167), p_lower_below_threshold(0.11<0.75) |
| 52733326 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,030.836384 USDC | 0.076442 USDC | 0.000000 USDC | 0.007239 USDC | 0.069203 USDC (0.0637 €) | — | 0.67 | 0.114 (n=81) | REJECTED | below_safety_margin(69203<206167), p_lower_below_threshold(0.11<0.75) |
| 52732602 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 71.137118 USDC | 0.070045 USDC | 0.000000 USDC | 0.005414 USDC | 0.064631 USDC (0.0595 €) | — | 9.09 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732142 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 66.177836 USDC | 0.061275 USDC | 0.000000 USDC | 0.005418 USDC | 0.055857 USDC (0.0514 €) | — | 8.44 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52733101 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003508 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0501 €) | — | 1.91 | 0.114 (n=81) | REJECTED | below_safety_margin(67<70), p_lower_below_threshold(0.11<0.75) |
| 52733100 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003508 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0501 €) | — | 1.91 | 0.114 (n=81) | REJECTED | below_safety_margin(67<70), p_lower_below_threshold(0.11<0.75) |
| 52733101 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.129765 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0495 €) | — | 1.72 | 0.114 (n=81) | REJECTED | below_safety_margin(22316890957272<25953007010325), p_lower_below_threshold(0.11<0.75) |
| 52733100 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.129765 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0495 €) | — | 1.72 | 0.114 (n=81) | REJECTED | below_safety_margin(22316890957272<25953007010325), p_lower_below_threshold(0.11<0.75) |
| 52732133 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 63.237107 USDC | 0.055672 USDC | 0.000000 USDC | 0.005417 USDC | 0.050255 USDC (0.0462 €) | — | 7.95 | 0.000 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732724 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 57.353428 USDC | 0.045997 USDC | 0.000000 USDC | 0.005413 USDC | 0.040584 USDC (0.0373 €) | — | 7.08 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732707 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 56.643370 USDC | 0.045074 USDC | 0.000000 USDC | 0.005413 USDC | 0.039661 USDC (0.0365 €) | — | 7.00 | 0.000 (n=42) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52733295 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 54.137679 USDC | 0.041686 USDC | 0.000000 USDC | 0.005410 USDC | 0.036276 USDC (0.0334 €) | — | 6.70 | 0.000 (n=44) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52733041 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.029762 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0283 €) | — | 4.29 | 0.187 (n=37) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 52733041 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 71.475973 USDC | 0.038647 USDC | 0.000000 USDC | 0.007973 USDC | 0.030674 USDC (0.0282 €) | — | 4.29 | 0.187 (n=37) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 52731994 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 49.123984 USDC | 0.035056 USDC | 0.000000 USDC | 0.005418 USDC | 0.029638 USDC (0.0273 €) | — | 6.03 | 0.000 (n=38) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732179 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 47.491583 USDC | 0.031398 USDC | 0.000000 USDC | 0.005418 USDC | 0.025980 USDC (0.0239 €) | — | 5.47 | 0.000 (n=40) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52733296 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 45.049630 USDC | 0.029077 USDC | 0.000000 USDC | 0.005410 USDC | 0.023667 USDC (0.0218 €) | — | 5.25 | 0.000 (n=44) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732563 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 43.225845 USDC | 0.026339 USDC | 0.000000 USDC | 0.005413 USDC | 0.020926 USDC (0.0193 €) | 0.020926 USDC | 4.84 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52733185 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 42.695240 USDC | 0.025486 USDC | 0.000000 USDC | 0.005409 USDC | 0.020077 USDC (0.0185 €) | — | 4.70 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52733737 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 40.563502 USDC | 0.023176 USDC | 0.000000 USDC | 0.005406 USDC | 0.017770 USDC (0.0163 €) | 0.017770 USDC | 4.38 | 0.000 (n=46) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 776 ; taux observé 0.117 ; borne inférieure crédible (0.9) 0.103 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
