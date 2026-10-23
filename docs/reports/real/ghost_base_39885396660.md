# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T02:53:49+00:00 ; durée 67.51 min ; blocs 52965306 → 52967339 (2025 vus)

## Connexion
- Requêtes RPC : 25622 ; erreurs : 3 ; latence p50/p95 : 214.6/688.6 ms
- Rafraîchissements d'état : 2026 ; âge des données au dernier bloc : 2.02 s ; changements de frais LP observés (pools à frais dynamiques) : 4413
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 37451 ; cycles déclenchés par événement : 1958 ; avance médiane sur le rafraîchissement multicall : 430 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,406.05 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19290 routes
- Par DEX : uniswap_v3 137, aerodrome 221, aerodrome_slipstream 136, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 199 (rejetés 2) → 604 jetons ; pools candidats 3831 (énumérés 358, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2390.436843, 'AERO': 0.786132, 'cbBTC': 81441.109035}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,991,501 | 2,406.045241 | 52967339 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,357,086 | 0.029470 | 52967339 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,488,845 | 92.423615 | 52967339 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 11,964,170 | 1.259295 | 52967339 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,310,408 | 0.029400 | 52967339 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,863,715 | 0.000012 | 52967339 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,964,894 | 0.029414 | 52967339 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,700,632 | 2,411.815402 | 52967339 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,166,950 | 0.001668 | 52967339 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 6,730,454 | 0.000012 | 52967339 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,676,094 | 2,412.529248 | 52967339 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,427,132 | 0.029481 | 52967339 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 5,265,786 | 0.000012 | 52967339 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,608,580 | 2,412.774210 | 52967339 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,300,030 | 0.998772 | 52967339 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,293,930 | 2,406.462045 | 52967339 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 4,002,317 | 34,249.856414 | 52967339 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,427,491 | 0.000274 | 52967339 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,910,423 | 2,415.839792 | 52967339 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,561,804 | 92.446256 | 52967339 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,320,565 | 390.893839 | 52967339 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/AERO | 10000 | 2,277,723 | 3,025.076784 | 52967339 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/FAI | 10000 | 2,236,319 | 1,174,301.538214 | 52967339 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,012,876 | 0.000000 | 52967339 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,924,928 | 0.000012 | 52967339 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,792,502 | 0.018113 | 52967339 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,752,067 | 0.000012 | 52967339 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,641,025 | 1.525684 | 52967339 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,618,314 | 3,031.888478 | 52967339 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,962 | 0.823199 | 52967339 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,422,920 | 13,251.491916 | 52967339 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,374,748 | 0.004986 | 52967339 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,300,212 | 0.000274 | 52967339 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,287,820 | 2.364245 | 52967339 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,283,938 | 2,411.721281 | 52967339 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,275,204 | 0.000000 | 52967339 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,423 | 64.289389 | 52967339 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,582 | 35,837,432.213161 | 52967339 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,175,487 | 16.192902 | 52967339 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,175,208 | 1,105,198.456783 | 52967339 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,165,464 | 46.201998 | 52967339 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,152,447 | 498,148.209539 | 52967339 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | weETH_04c0/WETH | 500 | 1,095,829 | 1.105790 | 52967339 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/EDEL | 7000 | 1,090,044 | 75,056.685778 | 52967339 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,087,145 | 0.038343 | 52967339 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,067,638 | 21,313,449.073659 | 52967339 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,034,258 | 17.240596 | 52967339 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,033,401 | 0.000010 | 52967339 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/cbBTC | 3000 | 1,015,391 | 0.029416 | 52967339 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,010,534 | 23.059192 | 52967339 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 966,803 | 1,055.903923 | 52967339 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 940,622 | 2,389.259097 | 52967339 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 918,297 | 0.000546 | 52967339 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 894,512 | 0.917079 | 52967339 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 884,675 | 17.736066 | 52967339 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 876,906 | 2,406.281551 | 52967339 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 815,096 | 0.803225 | 52967339 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 791,428 | 0.660763 | 52967339 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| pancakeswap_v3 | QUID/USDC | 100 | 787,620 | 0.055585 | 52967339 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 776,549 | 4,529,190.756233 | 52967339 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |

## Recherche d'opportunités
- Cycles : 3983 ; routes examinées : 76832070 ; candidats optimisés : 381531 ; net attendu > 0 : 380 ; dernier cycle 224.7 ms
- Rejets (moteur) : {'spread_below_threshold': 75639870, 'liquidity_below_min': 806275, 'negative_expected_net': 381151, 'borrow_bound_too_small': 3982, 'cycle_budget_exhausted': 412}
- Enregistrements de la session : 381531 ; net attendu > 0 : 380 ; simulés (eth_call de la vraie tx) : 29 (ok 25, échec 4) ; étiquettes ghost N+1 : 5/10 positives
- Décisions : {'REJECTED': 381531} ; motifs de rejet : {'below_safety_margin': 344, 'negative_expected_net': 381151, 'p_lower_below_threshold': 362, 'reliability_not_demonstrated': 18, 'sim_below_estimate': 5, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52966379 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,308.794265 USDC | 0.286204 USDC | 0.000000 USDC | 0.007574 USDC | 0.278630 USDC (0.2563 €) | — | 1.21 | 0.118 (n=233) | REJECTED | below_safety_margin(278630<461758), p_lower_below_threshold(0.12<0.75) |
| 52966379 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.967387 WETH | 0.000119 WETH | 0.000000 WETH | 0.000003 WETH | 0.000116 WETH (0.2560 €) | — | 1.20 | 0.118 (n=233) | REJECTED | below_safety_margin(116243543715568<193477418416083), p_lower_below_threshold(0.12<0.75) |
| 52966379 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.027693 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2558 €) | — | 1.23 | 0.118 (n=233) | REJECTED | below_safety_margin(342<553), p_lower_below_threshold(0.12<0.75) |
| 52966379 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,703.958109 USDC | 0.228588 USDC | 0.000000 USDC | 0.007574 USDC | 0.221014 USDC (0.2033 €) | — | 1.30 | 0.118 (n=233) | REJECTED | below_safety_margin(221014<340791), p_lower_below_threshold(0.12<0.75) |
| 52966379 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.710020 WETH | 0.000095 WETH | 0.000000 WETH | 0.000003 WETH | 0.000092 WETH (0.2029 €) | — | 1.30 | 0.118 (n=233) | REJECTED | below_safety_margin(92131754514676<142004093356591), p_lower_below_threshold(0.12<0.75) |
| 52966379 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,153.167403 USDC | 0.113931 USDC | 0.000000 USDC | 0.007210 USDC | 0.106721 USDC (0.0982 €) | — | 0.93 | 0.118 (n=233) | REJECTED | below_safety_margin(106721<230633), p_lower_below_threshold(0.12<0.75) |
| 52966379 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.480962 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0979 €) | — | 0.92 | 0.118 (n=233) | REJECTED | below_safety_margin(44482247782800<96192357679289), p_lower_below_threshold(0.12<0.75) |
| 52966379 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 989.286532 USDC | 0.092175 USDC | 0.000000 USDC | 0.007210 USDC | 0.084965 USDC (0.0782 €) | — | 0.86 | 0.118 (n=233) | REJECTED | below_safety_margin(84965<197857), p_lower_below_threshold(0.12<0.75) |
| 52966379 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.411914 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0780 €) | — | 0.86 | 0.118 (n=233) | REJECTED | below_safety_margin(35412594736205<82382789108866), p_lower_below_threshold(0.12<0.75) |
| 52966377 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,069.607653 USDC | 0.090215 USDC | 0.000000 USDC | 0.007564 USDC | 0.082651 USDC (0.0760 €) | — | 0.77 | 0.118 (n=233) | REJECTED | below_safety_margin(82651<213921), p_lower_below_threshold(0.12<0.75) |
| 52966377 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,069.607653 USDC | 0.090215 USDC | 0.000000 USDC | 0.007564 USDC | 0.082651 USDC (0.0760 €) | — | 0.77 | 0.118 (n=233) | REJECTED | below_safety_margin(82651<213921), p_lower_below_threshold(0.12<0.75) |
| 52966377 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.446464 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0759 €) | — | 0.77 | 0.118 (n=233) | REJECTED | below_safety_margin(34475136655392<89292700942886), p_lower_below_threshold(0.12<0.75) |
| 52966377 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.446464 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0759 €) | — | 0.77 | 0.118 (n=233) | REJECTED | below_safety_margin(34475136655392<89292700942886), p_lower_below_threshold(0.12<0.75) |
| 52966379 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009114 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0471 €) | — | 0.69 | 0.118 (n=233) | REJECTED | below_safety_margin(63<182), p_lower_below_threshold(0.12<0.75) |
| 52966379 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.333249 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0469 €) | — | 0.64 | 0.118 (n=233) | REJECTED | below_safety_margin(21285597853793<66649723393032), p_lower_below_threshold(0.12<0.75) |
| 52966379 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 783.074179 USDC | 0.058153 USDC | 0.000000 USDC | 0.007210 USDC | 0.050943 USDC (0.0469 €) | — | 0.65 | 0.118 (n=233) | REJECTED | below_safety_margin(50943<156614), p_lower_below_threshold(0.12<0.75) |
| 52966379 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,102.511669 USDC | 0.053648 USDC | 0.000000 USDC | 0.007210 USDC | 0.046438 USDC (0.0427 €) | — | 0.42 | 0.118 (n=233) | REJECTED | below_safety_margin(46438<220502), p_lower_below_threshold(0.12<0.75) |
| 52966379 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.011911 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0426 €) | — | 0.48 | 0.118 (n=233) | REJECTED | below_safety_margin(57<238), p_lower_below_threshold(0.12<0.75) |
| 52966379 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.434508 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0426 €) | — | 0.45 | 0.118 (n=233) | REJECTED | below_safety_margin(19343766994978<86901589110887), p_lower_below_threshold(0.12<0.75) |
| 52966719 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 408.303200 USDC | 0.053232 USDC | 0.000000 USDC | 0.007224 USDC | 0.046008 USDC (0.0423 €) | — | 1.13 | 0.242 (n=116) | REJECTED | below_safety_margin(46008<81660), p_lower_below_threshold(0.24<0.75) |
| 52966719 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.169523 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0422 €) | — | 1.13 | 0.242 (n=116) | REJECTED | below_safety_margin(19076449091706<33904620543176), p_lower_below_threshold(0.24<0.75) |
| 52965328 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 733.579452 USDC | 0.044077 USDC | 0.000000 USDC | 0.005375 USDC | 0.038702 USDC (0.0356 €) | — | 0.53 | 0.021 (n=69) | REJECTED | below_safety_margin(38702<146715), p_lower_below_threshold(0.02<0.75) |
| 52965328 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 733.579452 USDC | 0.044077 USDC | 0.000000 USDC | 0.005375 USDC | 0.038702 USDC (0.0356 €) | — | 0.53 | 0.021 (n=69) | REJECTED | below_safety_margin(38702<146715), p_lower_below_threshold(0.02<0.75) |
| 52965328 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.008336 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0352 €) | — | 0.56 | 0.021 (n=69) | REJECTED | below_safety_margin(47<166), p_lower_below_threshold(0.02<0.75) |
| 52965328 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.008336 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0352 €) | — | 0.56 | 0.021 (n=69) | REJECTED | below_safety_margin(47<166), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 1972 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.089 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
