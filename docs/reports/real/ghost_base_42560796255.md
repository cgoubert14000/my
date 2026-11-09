# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T05:34:41+00:00 ; durée 73.44 min ; blocs 55038467 → 55060466 (3007 vus)

## Connexion
- Requêtes RPC : 42488 ; erreurs : 0 ; latence p50/p95 : 474.9/1,831.9 ms
- Rafraîchissements d'état : 3007 ; âge des données au dernier bloc : 11.9 s ; changements de frais LP observés (pools à frais dynamiques) : 1692
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3897 ; cycles déclenchés par événement : 1340 ; avance médiane sur le rafraîchissement multicall : 574 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,134.38 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 467 pools, 272 jetons, 17562 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 194, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3664 (énumérés 288, par paires 0), mesurés 469, sous le plancher de 10000.0 $ : 2 → gardés 467 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2141.212816, 'cbBTC': 74926.035696, 'AERO': 0.58265}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,862,319 | 2,134.381170 | 55060499 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,432,829 | 0.028628 | 55060499 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,963,067 | 0.000013 | 55060499 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,794,227 | 0.028593 | 55060499 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,484,764 | 2,128.994635 | 55060499 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,140,812 | 104.384113 | 55060499 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,268,113 | 0.001530 | 55060499 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,656,643 | 0.028632 | 55060499 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,590,046 | 1.750309 | 55060499 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,924,799 | 2,128.169387 | 55060499 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,924,060 | 0.999218 | 55060499 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,151,255 | 42,933.072823 | 55060499 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,043,434 | 2,128.334448 | 55060499 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,367,692 | 0.028602 | 55060499 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,995,786 | 1,159,342.676479 | 55060499 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,706,924 | 0.000013 | 55060499 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,600,701 | 0.000013 | 55060499 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,597,894 | 0.006635 | 55060499 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,562,649 | 0.015470 | 55060499 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,560,049 | 0.000000 | 55060499 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,099 | 1.421539 | 55060499 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,460,046 | 434.553091 | 55060499 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,031 | 0.824196 | 55060499 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,407,966 | 0.000013 | 55060499 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,320,444 | 3,727.846505 | 55060499 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,295,089 | 2,134.400183 | 55060499 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,236,736 | 15,166.568870 | 55060499 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,224,495 | 2,134.804564 | 55060499 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,120,777 | 77.357246 | 55060499 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,098,119 | 2,129.114858 | 55060499 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,902 | 36,726,215.701874 | 55060499 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,015,991 | 104.274538 | 55060499 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 960,716 | 588,891.975444 | 55060499 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 948,919 | 22.156696 | 55060499 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 945,902 | 22,747,912.769938 | 55060499 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 924,868 | 0.000013 | 55060499 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 913,375 | 75.112060 | 55060499 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 912,495 | 2,137.198475 | 55060499 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 911,945 | 0.000000 | 55060499 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/MORPHO | 3000 | 904,848 | 1,046.493156 | 55060499 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 829,179 | 101,015.755039 | 55060499 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 815,087 | 0.048967 | 55060499 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 779,862 | 0.054349 | 55060499 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 750,505 | 22.864528 | 55060499 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 747,505 | 3,701.404575 | 55060499 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 723,501 | 0.800980 | 55060499 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 699,230 | 0.536539 | 55060499 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 653,006 | 5,056,771.046765 | 55060499 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 643,735 | 0.524790 | 55060499 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 621,686 | 0.000008 | 55060499 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 621,195 | 149,330.117787 | 55060499 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 594,731 | 0.000251 | 55060499 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 583,813 | 589,727.737190 | 55060499 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 565,233 | 0.038303 | 55060499 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 529,631 | 2.463662 | 55060499 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 513,139 | 1,046.915603 | 55060499 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 506,408 | 924,724.831785 | 55060499 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,524 | 1.001272 | 55060499 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 491,210 | 0.071671 | 55060499 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 490,677 | 2,128.497330 | 55060499 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 4346 ; routes examinées : 76324452 ; candidats optimisés : 224348 ; net attendu > 0 : 292 ; dernier cycle 283.8 ms
- Rejets (moteur) : {'spread_below_threshold': 75072252, 'liquidity_below_min': 1023275, 'negative_expected_net': 224056, 'borrow_bound_too_small': 4344, 'cycle_budget_exhausted': 233}
- Enregistrements de la session : 224348 ; net attendu > 0 : 292 ; simulés (eth_call de la vraie tx) : 16 (ok 8, échec 8) ; étiquettes ghost N+1 : 4/12 positives
- Décisions : {'REJECTED': 224348} ; motifs de rejet : {'below_safety_margin': 265, 'negative_expected_net': 224056, 'p_lower_below_threshold': 276, 'reliability_not_demonstrated': 16, 'simulation_failed': 8, 'stale_data': 36}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55045434 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.355434 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0857 €) | — | 1.22 | 0.048 (n=30) | REJECTED | below_safety_margin(43516011434452<71086872293656), p_lower_below_threshold(0.05<0.75) |
| 55045434 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.355434 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0857 €) | — | 1.22 | 0.048 (n=30) | REJECTED | below_safety_margin(43516011434452<71086872293656), p_lower_below_threshold(0.05<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 732.198649 USDC | 0.099587 USDC | 0.000000 USDC | 0.006433 USDC | 0.093154 USDC (0.0857 €) | — | 1.27 | 0.048 (n=30) | REJECTED | below_safety_margin(93154<146439), p_lower_below_threshold(0.05<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 732.198649 USDC | 0.099587 USDC | 0.000000 USDC | 0.006433 USDC | 0.093154 USDC (0.0857 €) | — | 1.27 | 0.048 (n=30) | REJECTED | below_safety_margin(93154<146439), p_lower_below_threshold(0.05<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009259 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0855 €) | — | 1.34 | 0.048 (n=30) | REJECTED | below_safety_margin(124<185), p_lower_below_threshold(0.05<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009259 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0855 €) | — | 1.34 | 0.048 (n=30) | REJECTED | below_safety_margin(124<185), p_lower_below_threshold(0.05<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006493 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0690 €) | — | 1.54 | 0.204 (n=1207) | REJECTED | below_safety_margin(100<129), p_lower_below_threshold(0.20<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006493 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0690 €) | — | 1.54 | 0.204 (n=1207) | REJECTED | below_safety_margin(100<129), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 501.136491 USDC | 0.080969 USDC | 0.000000 USDC | 0.006433 USDC | 0.074536 USDC (0.0686 €) | — | 1.49 | 0.204 (n=1207) | REJECTED | below_safety_margin(74536<100227), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 501.136491 USDC | 0.080969 USDC | 0.000000 USDC | 0.006433 USDC | 0.074536 USDC (0.0686 €) | — | 1.49 | 0.204 (n=1207) | REJECTED | below_safety_margin(74536<100227), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.226863 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0684 €) | — | 1.53 | 0.204 (n=1207) | REJECTED | below_safety_margin(34746748358204<45372651029136), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.226863 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0684 €) | — | 1.53 | 0.204 (n=1207) | REJECTED | below_safety_margin(34746748358204<45372651029136), p_lower_below_threshold(0.20<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003032 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0331 €) | — | 1.58 | 0.204 (n=1207) | REJECTED | below_safety_margin(48<60), p_lower_below_threshold(0.20<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003032 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0331 €) | — | 1.58 | 0.204 (n=1207) | REJECTED | below_safety_margin(48<60), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 206.733463 USDC | 0.042103 USDC | 0.000000 USDC | 0.006433 USDC | 0.035670 USDC (0.0328 €) | — | 1.73 | 0.204 (n=1207) | REJECTED | below_safety_margin(35670<41346), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 206.733463 USDC | 0.042103 USDC | 0.000000 USDC | 0.006433 USDC | 0.035670 USDC (0.0328 €) | — | 1.73 | 0.204 (n=1207) | REJECTED | below_safety_margin(35670<41346), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.111121 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0327 €) | — | 1.50 | 0.204 (n=1207) | REJECTED | below_safety_margin(16614882044691<22224232427663), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.111121 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0327 €) | — | 1.50 | 0.204 (n=1207) | REJECTED | below_safety_margin(16614882044691<22224232427663), p_lower_below_threshold(0.20<0.75) |
| 55052013 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 33.934998 USDC | 0.034553 USDC | 0.000000 USDC | 0.004799 USDC | 0.029754 USDC (0.0274 €) | — | 8.77 | 0.003 (n=108) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 55053638 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SLC→[aerodrome]→WETH | 0.013568 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0262 €) | 0.000013 WETH | 9.81 | 0.145 (n=53) | REJECTED | stale_data(4445ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 55053638 | USDC→[uniswap_v3]→SLC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 28.810779 USDC | 0.034510 USDC | 0.000000 USDC | 0.006128 USDC | 0.028382 USDC (0.0261 €) | — | 9.85 | 0.145 (n=53) | REJECTED | stale_data(4450ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 55053638 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SLC→[aerodrome]→WETH | 0.012269 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0208 €) | 0.000011 WETH | 8.61 | 0.066 (n=191) | REJECTED | stale_data(4466ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55053638 | USDC→[uniswap_v3]→SLC→[aerodrome]→WETH→[uniswap_v3]→USDC | 26.003079 USDC | 0.028650 USDC | 0.000000 USDC | 0.006128 USDC | 0.022522 USDC (0.0207 €) | — | 8.66 | 0.066 (n=191) | REJECTED | stale_data(4471ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55040533 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 27.623305 USDC | 0.022893 USDC | 0.000000 USDC | 0.004807 USDC | 0.018086 USDC (0.0166 €) | — | 6.55 | 0.045 (n=412) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 55053638 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SLC→[aerodrome]→WETH | 0.010123 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0120 €) | 0.000006 WETH | 6.04 | 0.134 (n=273) | REJECTED | stale_data(4494ms>4000.0), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 6662 ; taux observé 0.175 ; borne inférieure crédible (0.9) 0.169 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
