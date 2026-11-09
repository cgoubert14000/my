# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T15:51:05+00:00 ; durée 15.3 min ; blocs 55240823 → 55245396 (514 vus)

## Connexion
- Requêtes RPC : 8196 ; erreurs : 0 ; latence p50/p95 : 421.3/1,561.8 ms
- Rafraîchissements d'état : 514 ; âge des données au dernier bloc : 11.29 s ; changements de frais LP observés (pools à frais dynamiques) : 618
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1283 ; cycles déclenchés par événement : 289 ; avance médiane sur le rafraîchissement multicall : 756 ms
- Gaz : base fee 0.005011 gwei ; prix ETH (pool le plus profond) : 2,143.29 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 274 jetons, 17868 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 102, aerodrome 193, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3663 (énumérés 293, par paires 0), mesurés 475, sous le plancher de 10000.0 $ : 2 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2131.426069, 'cbBTC': 75169.710892, 'AERO': 0.579676}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,511,061 | 2,143.287384 | 55245426 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,743,907 | 0.028443 | 55245426 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,362,179 | 0.000013 | 55245426 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,809,666 | 0.028437 | 55245426 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,375,064 | 2,146.048146 | 55245426 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,305,269 | 100.503653 | 55245426 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,321,402 | 0.001524 | 55245426 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,983,442 | 0.028431 | 55245426 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,619,043 | 1.717911 | 55245426 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,022,945 | 2,145.425140 | 55245426 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,968,102 | 0.998725 | 55245426 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,136,566 | 43,698.566396 | 55245426 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,051,710 | 2,145.434016 | 55245426 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,381,766 | 0.028430 | 55245426 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,013,843 | 1,148,168.304509 | 55245426 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,730,325 | 0.000013 | 55245426 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,713,274 | 0.000013 | 55245426 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,599,654 | 0.006693 | 55245426 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,574,474 | 0.015663 | 55245426 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,573,667 | 0.000000 | 55245426 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,518,256 | 0.000013 | 55245426 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,480,300 | 420.600547 | 55245426 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55245426 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,404 | 0.821800 | 55245426 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,338,055 | 3,680.366991 | 55245426 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,297,895 | 2,144.258402 | 55245426 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,264,276 | 14,783.014602 | 55245426 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,225,863 | 2,143.557880 | 55245426 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,257 | 79.257778 | 55245426 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,102,124 | 2,146.275235 | 55245426 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/VVV | 10000 | 1,057,563 | 100.748986 | 55245426 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/doginme | 10000 | 1,056,544 | 36,597,833.136154 | 55245426 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 979,993 | 562,246.472007 | 55245426 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 964,002 | 21.117746 | 55245426 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 938,444 | 23,221,908.008456 | 55245426 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 933,947 | 0.000013 | 55245426 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 920,122 | 1,022.058033 | 55245426 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 917,320 | 74.467388 | 55245426 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | DRB/WETH | 10000 | 916,562 | 0.000000 | 55245426 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 891,395 | 0.046885 | 55245426 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 890,261 | 2,127.924141 | 55245426 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 822,856 | 103,432.206755 | 55245426 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4550 | 787,946 | 21.364929 | 55245426 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 769,506 | 0.052853 | 55245426 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 755,397 | 3,692.738593 | 55245426 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 727,637 | 0.798523 | 55245426 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 674,981 | 0.555549 | 55245426 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 667,219 | 4,884,475.460873 | 55245426 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,000 | 0.527352 | 55245426 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 630,913 | 0.000008 | 55245426 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 619,975 | 151,233.983299 | 55245426 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 603,613 | 0.000257 | 55245426 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 600,667 | 558,407.806149 | 55245426 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 578,553 | 0.039694 | 55245426 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 535,976 | 2.393305 | 55245426 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 523,437 | 1,022.288205 | 55245426 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 512,385 | 916,490.618579 | 55245426 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | WETH/DRV | 3000 | 493,389 | 6,920.197377 | 55245426 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | USDC/USDT | 100 | 491,729 | 1.001181 | 55245426 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 477,598 | 0.069052 | 55245426 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 802 ; routes examinées : 14330136 ; candidats optimisés : 80165 ; net attendu > 0 : 198 ; dernier cycle 507.4 ms
- Rejets (moteur) : {'spread_below_threshold': 13989124, 'liquidity_below_min': 248207, 'negative_expected_net': 79967, 'borrow_bound_too_small': 12640}
- Enregistrements de la session : 80165 ; net attendu > 0 : 198 ; simulés (eth_call de la vraie tx) : 6 (ok 3, échec 3) ; étiquettes ghost N+1 : 4/4 positives
- Décisions : {'REJECTED': 80165} ; motifs de rejet : {'below_safety_margin': 182, 'negative_expected_net': 79967, 'p_lower_below_threshold': 172, 'reliability_not_demonstrated': 26, 'simulation_failed': 3, 'stale_data': 59}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55241295 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002374 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0345 €) | — | 2.11 | 0.027 (n=11) | REJECTED | stale_data(5044ms>4000.0), reliability_not_demonstrated |
| 55241295 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 178.950424 USDC | 0.042177 USDC | 0.000000 USDC | 0.004920 USDC | 0.037257 USDC (0.0343 €) | 0.037257 USDC | 2.08 | 0.027 (n=11) | REJECTED | stale_data(5041ms>4000.0), reliability_not_demonstrated |
| 55244252 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 512.207636 USDC | 0.034934 USDC | 0.000000 USDC | 0.006871 USDC | 0.028063 USDC (0.0258 €) | — | 0.55 | 0.048 (n=30) | REJECTED | below_safety_margin(28063<102441), p_lower_below_threshold(0.05<0.75) |
| 55244253 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 512.207636 USDC | 0.034934 USDC | 0.000000 USDC | 0.006871 USDC | 0.028063 USDC (0.0258 €) | — | 0.55 | 0.048 (n=30) | REJECTED | below_safety_margin(28063<102441), p_lower_below_threshold(0.05<0.75) |
| 55244252 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005980 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0256 €) | — | 0.62 | 0.048 (n=30) | REJECTED | below_safety_margin(37<119), p_lower_below_threshold(0.05<0.75) |
| 55244253 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005980 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0256 €) | — | 0.62 | 0.048 (n=30) | REJECTED | below_safety_margin(37<119), p_lower_below_threshold(0.05<0.75) |
| 55244252 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.223504 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0256 €) | — | 0.58 | 0.048 (n=30) | REJECTED | below_safety_margin(12990862366430<44700750350483), p_lower_below_threshold(0.05<0.75) |
| 55244253 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.223504 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0256 €) | — | 0.58 | 0.048 (n=30) | REJECTED | below_safety_margin(12990862366430<44700750350483), p_lower_below_threshold(0.05<0.75) |
| 55244252 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.230315 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0223 €) | — | 0.49 | 0.216 (n=1274) | REJECTED | below_safety_margin(11287587140945<46062925023518), p_lower_below_threshold(0.22<0.75) |
| 55244253 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.230315 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0223 €) | — | 0.49 | 0.216 (n=1274) | REJECTED | below_safety_margin(11287587140945<46062925023518), p_lower_below_threshold(0.22<0.75) |
| 55244252 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006957 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0222 €) | — | 0.46 | 0.216 (n=1274) | REJECTED | below_safety_margin(32<139), p_lower_below_threshold(0.22<0.75) |
| 55244253 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006957 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0222 €) | — | 0.46 | 0.216 (n=1274) | REJECTED | below_safety_margin(32<139), p_lower_below_threshold(0.22<0.75) |
| 55244252 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 437.124045 USDC | 0.030818 USDC | 0.000000 USDC | 0.006871 USDC | 0.023947 USDC (0.0220 €) | — | 0.55 | 0.216 (n=1274) | REJECTED | below_safety_margin(23947<87424), p_lower_below_threshold(0.22<0.75) |
| 55244253 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 437.124045 USDC | 0.030818 USDC | 0.000000 USDC | 0.006871 USDC | 0.023947 USDC (0.0220 €) | — | 0.55 | 0.216 (n=1274) | REJECTED | below_safety_margin(23947<87424), p_lower_below_threshold(0.22<0.75) |
| 55245019 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 555.717787 USDC | 0.028199 USDC | 0.000000 USDC | 0.004907 USDC | 0.023292 USDC (0.0214 €) | — | 0.42 | 0.064 (n=306) | REJECTED | below_safety_margin(23292<111143), p_lower_below_threshold(0.06<0.75) |
| 55245021 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 555.717787 USDC | 0.028199 USDC | 0.000000 USDC | 0.004907 USDC | 0.023292 USDC (0.0214 €) | — | 0.42 | 0.064 (n=306) | REJECTED | below_safety_margin(23292<111143), p_lower_below_threshold(0.06<0.75) |
| 55245019 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.259272 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0214 €) | — | 0.42 | 0.064 (n=306) | REJECTED | below_safety_margin(10858129588009<51854403046535), p_lower_below_threshold(0.06<0.75) |
| 55245021 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.259272 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0214 €) | — | 0.42 | 0.064 (n=306) | REJECTED | below_safety_margin(10858129588009<51854403046535), p_lower_below_threshold(0.06<0.75) |
| 55241295 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 67.238591 USDC | 0.022528 USDC | 0.000000 USDC | 0.006573 USDC | 0.015955 USDC (0.0147 €) | — | 2.37 | 0.216 (n=1274) | REJECTED | stale_data(4945ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55241295 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000928 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0145 €) | — | 2.26 | 0.216 (n=1274) | REJECTED | stale_data(4941ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55241296 | USDC→[aerodrome]→SPARKLET→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 8.567909 USDC | 0.012869 USDC | 0.000000 USDC | 0.005978 USDC | 0.006891 USDC (0.0063 €) | — | 8.04 | 0.065 (n=194) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55241296 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→SPARKLET→[aerodrome]→WETH | 0.004015 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0063 €) | — | 8.00 | 0.065 (n=194) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55241295 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001054 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0055 €) | — | 0.76 | 0.216 (n=1274) | REJECTED | below_safety_margin(8<21), stale_data(5173ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55241295 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 81.456134 USDC | 0.012278 USDC | 0.000000 USDC | 0.006573 USDC | 0.005705 USDC (0.0052 €) | — | 0.70 | 0.216 (n=1274) | REJECTED | below_safety_margin(5705<16291), stale_data(5169ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55241295 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.037777 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0051 €) | — | 0.69 | 0.216 (n=1274) | REJECTED | below_safety_margin(2620073318202<7555354876997), stale_data(5164ms>4000.0), p_lower_below_threshold(0.22<0.75) |

## Fiabilité et décision
- Observations ghost : 6916 ; taux observé 0.183 ; borne inférieure crédible (0.9) 0.178 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
