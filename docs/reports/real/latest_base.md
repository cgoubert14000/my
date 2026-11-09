# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T15:44:55+00:00 ; durée 9.13 min ; blocs 55240823 → 55243558 (320 vus)

## Connexion
- Requêtes RPC : 5043 ; erreurs : 0 ; latence p50/p95 : 426.9/1,517.8 ms
- Rafraîchissements d'état : 320 ; âge des données au dernier bloc : 7.97 s ; changements de frais LP observés (pools à frais dynamiques) : 373
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 869 ; cycles déclenchés par événement : 179 ; avance médiane sur le rafraîchissement multicall : 789 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,136.35 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 274 jetons, 17868 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 102, aerodrome 193, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3663 (énumérés 293, par paires 0), mesurés 475, sous le plancher de 10000.0 $ : 2 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2131.426069, 'cbBTC': 75169.710892, 'AERO': 0.579676}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,174,191 | 2,136.348100 | 55243557 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,694,797 | 0.028409 | 55243557 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,351,451 | 0.000013 | 55243557 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,784,122 | 0.028437 | 55243557 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,355,825 | 2,141.778089 | 55243557 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,290,574 | 100.256834 | 55243557 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,310,559 | 0.001524 | 55243557 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,964,869 | 0.028414 | 55243557 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,610,519 | 1.724269 | 55243557 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,012,203 | 2,142.465835 | 55243557 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,960,860 | 0.998725 | 55243557 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,126,577 | 43,693.905251 | 55243557 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,043,321 | 2,142.561177 | 55243557 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 2,374,656 | 0.028430 | 55243557 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,007,323 | 1,148,168.304509 | 55243557 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,728,036 | 0.000013 | 55243557 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 592 | 1,711,029 | 0.000013 | 55243557 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,594,475 | 0.006693 | 55243557 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,570,996 | 0.015614 | 55243557 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,568,572 | 0.000000 | 55243557 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,516,554 | 0.000013 | 55243557 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,476,767 | 419.334118 | 55243557 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55243557 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,404 | 0.821800 | 55243557 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,333,358 | 3,677.694717 | 55243557 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,295,788 | 2,135.732043 | 55243557 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,262,822 | 14,760.889600 | 55243557 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,223,877 | 2,135.807668 | 55243557 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,257 | 79.257778 | 55243557 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,098,954 | 2,141.677893 | 55243557 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/VVV | 10000 | 1,055,382 | 100.748986 | 55243557 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/doginme | 10000 | 1,053,123 | 36,597,833.136154 | 55243557 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 976,821 | 562,245.661576 | 55243557 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 964,355 | 21.094255 | 55243557 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 935,406 | 23,221,908.008456 | 55243557 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 368 | 932,458 | 0.000013 | 55243557 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 917,143 | 1,022.058033 | 55243557 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 916,186 | 74.651850 | 55243557 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | DRB/WETH | 10000 | 913,594 | 0.000000 | 55243557 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 890,885 | 0.046885 | 55243557 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 889,018 | 2,121.101936 | 55243557 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 822,086 | 102,956.109142 | 55243557 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 787,316 | 21.388959 | 55243557 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 769,481 | 0.052849 | 55243557 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 752,781 | 3,692.738593 | 55243557 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 725,290 | 0.798503 | 55243557 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,466 | 0.553327 | 55243557 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 665,059 | 4,884,475.460873 | 55243557 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 645,400 | 0.527352 | 55243557 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 629,003 | 0.000008 | 55243557 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 617,468 | 151,478.289413 | 55243557 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 601,264 | 0.000256 | 55243557 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 598,724 | 557,653.875479 | 55243557 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 577,944 | 0.039630 | 55243557 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 534,331 | 2.392703 | 55243557 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 521,738 | 1,021.823936 | 55243558 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 511,516 | 916,490.618579 | 55243557 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 495,222 | 1.001191 | 55243557 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 491,864 | 6,918.162186 | 55243557 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 478,233 | 0.069197 | 55243557 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 498 ; routes examinées : 8898264 ; candidats optimisés : 49298 ; net attendu > 0 : 93 ; dernier cycle 391.7 ms
- Rejets (moteur) : {'spread_below_threshold': 8693864, 'liquidity_below_min': 148432, 'negative_expected_net': 49205, 'borrow_bound_too_small': 6670}
- Enregistrements de la session : 49298 ; net attendu > 0 : 93 ; simulés (eth_call de la vraie tx) : 6 (ok 3, échec 3) ; étiquettes ghost N+1 : 4/4 positives
- Décisions : {'REJECTED': 49298} ; motifs de rejet : {'below_safety_margin': 77, 'negative_expected_net': 49205, 'p_lower_below_threshold': 79, 'reliability_not_demonstrated': 14, 'simulation_failed': 3, 'stale_data': 47}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55241295 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002374 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0345 €) | — | 2.11 | 0.027 (n=11) | REJECTED | stale_data(5044ms>4000.0), reliability_not_demonstrated |
| 55241295 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 178.950424 USDC | 0.042177 USDC | 0.000000 USDC | 0.004920 USDC | 0.037257 USDC (0.0343 €) | 0.037257 USDC | 2.08 | 0.027 (n=11) | REJECTED | stale_data(5041ms>4000.0), reliability_not_demonstrated |
| 55241295 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 67.238591 USDC | 0.022528 USDC | 0.000000 USDC | 0.006573 USDC | 0.015955 USDC (0.0147 €) | — | 2.37 | 0.216 (n=1274) | REJECTED | stale_data(4945ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55241295 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000928 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0145 €) | — | 2.26 | 0.216 (n=1274) | REJECTED | stale_data(4941ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55241296 | USDC→[aerodrome]→SPARKLET→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 8.567909 USDC | 0.012869 USDC | 0.000000 USDC | 0.005978 USDC | 0.006891 USDC (0.0063 €) | — | 8.04 | 0.065 (n=194) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55241296 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→SPARKLET→[aerodrome]→WETH | 0.004015 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0063 €) | — | 8.00 | 0.065 (n=194) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55241295 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001054 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0055 €) | — | 0.76 | 0.216 (n=1274) | REJECTED | below_safety_margin(8<21), stale_data(5173ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55241295 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 81.456134 USDC | 0.012278 USDC | 0.000000 USDC | 0.006573 USDC | 0.005705 USDC (0.0052 €) | — | 0.70 | 0.216 (n=1274) | REJECTED | below_safety_margin(5705<16291), stale_data(5169ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55241295 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.037777 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0051 €) | — | 0.69 | 0.216 (n=1274) | REJECTED | below_safety_margin(2620073318202<7555354876997), stale_data(5164ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55241295 | USDC→[aerodrome]→SPARKLET→[aerodrome]→WETH→[uniswap_v3]→USDC | 8.061245 USDC | 0.011459 USDC | 0.000000 USDC | 0.005981 USDC | 0.005478 USDC (0.0050 €) | — | 6.80 | 0.139 (n=277) | REJECTED | stale_data(4788ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 55241295 | WETH→[uniswap_v3]→USDC→[aerodrome]→SPARKLET→[aerodrome]→WETH | 0.003791 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0050 €) | 0.000003 WETH | 6.74 | 0.139 (n=277) | REJECTED | stale_data(4786ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 55241296 | USDC→[aerodrome]→SPARKLET→[aerodrome]→WETH→[uniswap_v3]→USDC | 8.060194 USDC | 0.011412 USDC | 0.000000 USDC | 0.005978 USDC | 0.005434 USDC (0.0050 €) | — | 6.74 | 0.139 (n=277) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55241296 | WETH→[uniswap_v3]→USDC→[aerodrome]→SPARKLET→[aerodrome]→WETH | 0.003777 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0050 €) | — | 6.71 | 0.139 (n=277) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 55241296 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000944 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0048 €) | — | 0.74 | 0.216 (n=1274) | REJECTED | below_safety_margin(7<18), p_lower_below_threshold(0.22<0.75) |
| 55241296 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001170 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0048 €) | — | 0.60 | 0.027 (n=11) | REJECTED | below_safety_margin(7<23), reliability_not_demonstrated |
| 55241480 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 114.583577 USDC | 0.010468 USDC | 0.000000 USDC | 0.005220 USDC | 0.005248 USDC (0.0048 €) | — | 0.46 | 0.064 (n=306) | REJECTED | below_safety_margin(5248<22916), p_lower_below_threshold(0.06<0.75) |
| 55241480 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 114.583577 USDC | 0.010468 USDC | 0.000000 USDC | 0.005220 USDC | 0.005248 USDC (0.0048 €) | — | 0.46 | 0.064 (n=306) | REJECTED | below_safety_margin(5248<22916), p_lower_below_threshold(0.06<0.75) |
| 55241480 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.054058 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0048 €) | — | 0.45 | 0.064 (n=306) | REJECTED | below_safety_margin(2449944466310<10811638843443), p_lower_below_threshold(0.06<0.75) |
| 55241480 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.054058 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0048 €) | — | 0.45 | 0.064 (n=306) | REJECTED | below_safety_margin(2449944466310<10811638843443), p_lower_below_threshold(0.06<0.75) |
| 55241296 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 80.991078 USDC | 0.011741 USDC | 0.000000 USDC | 0.006570 USDC | 0.005171 USDC (0.0048 €) | — | 0.64 | 0.216 (n=1274) | REJECTED | below_safety_margin(5171<16198), p_lower_below_threshold(0.22<0.75) |
| 55241296 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.037535 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0047 €) | — | 0.63 | 0.216 (n=1274) | REJECTED | below_safety_margin(2381838014738<7506915087913), p_lower_below_threshold(0.22<0.75) |
| 55241296 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 96.832400 USDC | 0.009930 USDC | 0.000000 USDC | 0.004917 USDC | 0.005013 USDC (0.0046 €) | — | 0.52 | 0.027 (n=11) | REJECTED | below_safety_margin(5013<19366), reliability_not_demonstrated |
| 55241295 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 76.417263 USDC | 0.011436 USDC | 0.000000 USDC | 0.006573 USDC | 0.004863 USDC (0.0045 €) | — | 0.64 | 0.293 (n=472) | REJECTED | below_safety_margin(4863<15283), stale_data(5151ms>4000.0), p_lower_below_threshold(0.29<0.75) |
| 55241295 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.036178 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0044 €) | — | 0.63 | 0.293 (n=472) | REJECTED | below_safety_margin(2266471748418<7235671885922), stale_data(5146ms>4000.0), p_lower_below_threshold(0.29<0.75) |
| 55241295 | USDC→[aerodrome]→SPARKLET→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 7.848983 USDC | 0.010759 USDC | 0.000000 USDC | 0.005981 USDC | 0.004778 USDC (0.0044 €) | — | 6.09 | 0.162 (n=111) | REJECTED | stale_data(4792ms>4000.0), p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 6916 ; taux observé 0.183 ; borne inférieure crédible (0.9) 0.178 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
