# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T16:33:55+00:00 ; durée 58.13 min ; blocs 55240823 → 55258263 (2303 vus)

## Connexion
- Requêtes RPC : 33576 ; erreurs : 0 ; latence p50/p95 : 441.7/1,615.8 ms
- Rafraîchissements d'état : 2303 ; âge des données au dernier bloc : 5.98 s ; changements de frais LP observés (pools à frais dynamiques) : 2208
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1283 ; cycles déclenchés par événement : 289 ; avance médiane sur le rafraîchissement multicall : 756 ms
- Gaz : base fee 0.005001 gwei ; prix ETH (pool le plus profond) : 2,128.63 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 274 jetons, 17868 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 102, aerodrome 193, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3663 (énumérés 293, par paires 0), mesurés 475, sous le plancher de 10000.0 $ : 2 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2131.426069, 'cbBTC': 75169.710892, 'AERO': 0.579676}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,837,459 | 2,128.630159 | 55258263 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,639,336 | 0.028439 | 55258263 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,302,653 | 0.000013 | 55258263 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,752,700 | 0.028437 | 55258263 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,333,999 | 2,131.792829 | 55258263 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,241,061 | 100.899604 | 55258263 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,949,992 | 0.028448 | 55258263 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,591,621 | 1.738492 | 55258263 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,000,312 | 2,132.559552 | 55258263 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,943,047 | 0.998660 | 55258263 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,114,946 | 43,703.342283 | 55258263 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 877 | 3,030,945 | 2,132.599108 | 55258263 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,381,819 | 0.028430 | 55258263 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,999,735 | 1,148,554.063045 | 55258263 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,722,047 | 0.000013 | 55258263 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 1,705,233 | 0.000013 | 55258263 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,580,317 | 0.015747 | 55258263 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,571,544 | 0.006605 | 55258263 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,562,906 | 0.000000 | 55258263 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,512,127 | 0.000013 | 55258263 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55258263 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,469,349 | 421.439920 | 55258263 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,737 | 0.821800 | 55258263 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,324,864 | 3,693.557755 | 55258263 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,293,456 | 2,128.849800 | 55258263 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,254,814 | 14,823.887233 | 55258263 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,665 | 2,129.379820 | 55258263 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,257 | 79.257778 | 55258263 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,096,618 | 2,131.633017 | 55258263 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,049,206 | 36,609,682.691449 | 55258263 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,035,100 | 100.750095 | 55258263 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 973,290 | 562,246.271129 | 55258263 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,778 | 21.267277 | 55258263 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 939,650 | 0.001518 | 55258263 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 928,619 | 0.000013 | 55258263 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 925,200 | 23,537,564.740435 | 55258263 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 917,850 | 74.381385 | 55258263 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 912,062 | 1,025.908514 | 55258263 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 911,043 | 0.000000 | 55258263 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 887,652 | 2,127.924141 | 55258263 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 884,153 | 0.047333 | 55258263 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 815,350 | 103,909.429909 | 55258263 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 789,545 | 21.304019 | 55258263 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 772,253 | 0.053245 | 55258263 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 748,340 | 3,692.738593 | 55258263 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 722,632 | 0.798586 | 55258263 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,095 | 0.550008 | 55258263 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 662,016 | 4,893,939.971160 | 55258263 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 647,998 | 0.527352 | 55258263 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 624,663 | 0.000008 | 55258263 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 615,154 | 151,492.712747 | 55258263 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 599,951 | 0.000257 | 55258263 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 596,561 | 564,422.096505 | 55258263 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 575,515 | 0.039373 | 55258263 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 532,311 | 2.393305 | 55258263 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 518,810 | 1,026.503736 | 55258263 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 510,722 | 916,123.514898 | 55258263 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 493,736 | 1.001016 | 55258263 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 490,969 | 6,893.306317 | 55258263 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 474,427 | 0.068485 | 55258263 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 2591 ; routes examinées : 46295988 ; candidats optimisés : 183101 ; net attendu > 0 : 415 ; dernier cycle 534.8 ms
- Rejets (moteur) : {'spread_below_threshold': 45406468, 'liquidity_below_min': 681157, 'negative_expected_net': 182686, 'borrow_bound_too_small': 24921, 'cycle_budget_exhausted': 244}
- Enregistrements de la session : 183101 ; net attendu > 0 : 415 ; simulés (eth_call de la vraie tx) : 32 (ok 26, échec 6) ; étiquettes ghost N+1 : 14/25 positives
- Décisions : {'REJECTED': 183101} ; motifs de rejet : {'below_safety_margin': 356, 'negative_expected_net': 182686, 'p_lower_below_threshold': 381, 'reliability_not_demonstrated': 34, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 3, 'simulation_failed': 6, 'stale_data': 141}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55246974 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.354201 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0729 €) | — | 1.04 | 0.048 (n=30) | REJECTED | below_safety_margin(36995411685845<70840226028216), stale_data(5713ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55246974 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 833.027063 USDC | 0.085597 USDC | 0.000000 USDC | 0.006858 USDC | 0.078739 USDC (0.0724 €) | — | 0.95 | 0.048 (n=30) | REJECTED | below_safety_margin(78739<166605), stale_data(5719ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55246974 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009328 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0721 €) | — | 1.11 | 0.048 (n=30) | REJECTED | below_safety_margin(104<186), stale_data(5726ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55253986 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005697 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0436 €) | — | 1.11 | 0.216 (n=1274) | REJECTED | below_safety_margin(63<113), p_lower_below_threshold(0.22<0.75) |
| 55253986 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.221325 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0435 €) | — | 1.00 | 0.216 (n=1274) | REJECTED | below_safety_margin(22118970982473<44265071018017), p_lower_below_threshold(0.22<0.75) |
| 55253986 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 485.256728 USDC | 0.053353 USDC | 0.000000 USDC | 0.006475 USDC | 0.046878 USDC (0.0431 €) | — | 0.97 | 0.216 (n=1274) | REJECTED | below_safety_margin(46878<97051), p_lower_below_threshold(0.22<0.75) |
| 55253986 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006430 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0408 €) | — | 0.92 | 0.063 (n=307) | REJECTED | below_safety_margin(59<128), p_lower_below_threshold(0.06<0.75) |
| 55253986 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 516.615464 USDC | 0.048879 USDC | 0.000000 USDC | 0.004842 USDC | 0.044037 USDC (0.0405 €) | — | 0.85 | 0.063 (n=307) | REJECTED | below_safety_margin(44037<103323), p_lower_below_threshold(0.06<0.75) |
| 55241295 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002374 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0345 €) | — | 2.11 | 0.027 (n=11) | REJECTED | stale_data(5044ms>4000.0), reliability_not_demonstrated |
| 55241295 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 178.950424 USDC | 0.042177 USDC | 0.000000 USDC | 0.004920 USDC | 0.037257 USDC (0.0343 €) | 0.037257 USDC | 2.08 | 0.027 (n=11) | REJECTED | stale_data(5041ms>4000.0), reliability_not_demonstrated |
| 55246974 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.254344 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0313 €) | — | 0.62 | 0.216 (n=1274) | REJECTED | below_safety_margin(15882804364666<50868729122864), stale_data(5776ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55246974 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 526.304034 USDC | 0.040890 USDC | 0.000000 USDC | 0.006858 USDC | 0.034032 USDC (0.0313 €) | — | 0.65 | 0.216 (n=1274) | REJECTED | below_safety_margin(34032<105260), stale_data(5782ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55246974 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006832 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0312 €) | — | 0.66 | 0.216 (n=1274) | REJECTED | below_safety_margin(45<136), stale_data(5789ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55253986 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 554.197285 USDC | 0.037477 USDC | 0.000000 USDC | 0.006475 USDC | 0.031002 USDC (0.0285 €) | — | 0.56 | 0.048 (n=30) | REJECTED | below_safety_margin(31002<110839), p_lower_below_threshold(0.05<0.75) |
| 55253986 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006040 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0284 €) | — | 0.68 | 0.048 (n=30) | REJECTED | below_safety_margin(41<120), p_lower_below_threshold(0.05<0.75) |
| 55253986 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.274040 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0283 €) | — | 0.52 | 0.048 (n=30) | REJECTED | below_safety_margin(14370286415079<54807926396952), p_lower_below_threshold(0.05<0.75) |
| 55257008 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.137541 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000014 WETH (0.0270 €) | — | 1.00 | 0.063 (n=307) | REJECTED | below_safety_margin(13811691658076<27508111320425), p_lower_below_threshold(0.06<0.75) |
| 55257008 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 291.728136 USDC | 0.034155 USDC | 0.000000 USDC | 0.004833 USDC | 0.029322 USDC (0.0270 €) | — | 1.01 | 0.063 (n=307) | REJECTED | below_safety_margin(29322<58345), p_lower_below_threshold(0.06<0.75) |
| 55244252 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 512.207636 USDC | 0.034934 USDC | 0.000000 USDC | 0.006871 USDC | 0.028063 USDC (0.0258 €) | — | 0.55 | 0.048 (n=30) | REJECTED | below_safety_margin(28063<102441), p_lower_below_threshold(0.05<0.75) |
| 55244253 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 512.207636 USDC | 0.034934 USDC | 0.000000 USDC | 0.006871 USDC | 0.028063 USDC (0.0258 €) | — | 0.55 | 0.048 (n=30) | REJECTED | below_safety_margin(28063<102441), p_lower_below_threshold(0.05<0.75) |
| 55244252 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005980 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0256 €) | — | 0.62 | 0.048 (n=30) | REJECTED | below_safety_margin(37<119), p_lower_below_threshold(0.05<0.75) |
| 55244253 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005980 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0256 €) | — | 0.62 | 0.048 (n=30) | REJECTED | below_safety_margin(37<119), p_lower_below_threshold(0.05<0.75) |
| 55244252 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.223504 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0256 €) | — | 0.58 | 0.048 (n=30) | REJECTED | below_safety_margin(12990862366430<44700750350483), p_lower_below_threshold(0.05<0.75) |
| 55244253 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.223504 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0256 €) | — | 0.58 | 0.048 (n=30) | REJECTED | below_safety_margin(12990862366430<44700750350483), p_lower_below_threshold(0.05<0.75) |
| 55247047 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 53.415374 USDC | 0.030798 USDC | 0.000000 USDC | 0.004886 USDC | 0.025912 USDC (0.0238 €) | 0.025912 USDC | 4.85 | 0.048 (n=425) | REJECTED | stale_data(4171ms>4000.0), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 6937 ; taux observé 0.184 ; borne inférieure crédible (0.9) 0.178 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
