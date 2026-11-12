# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T22:30:28+00:00 ; durée 18.42 min ; blocs 56655713 → 56661241 (1228 vus)

## Connexion
- Requêtes RPC : 15266 ; erreurs : 0 ; latence p50/p95 : 212.2/960.2 ms
- Rafraîchissements d'état : 1228 ; âge des données au dernier bloc : 4.89 s ; changements de frais LP observés (pools à frais dynamiques) : 459
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1477 ; cycles déclenchés par événement : 578 ; avance médiane sur le rafraîchissement multicall : 318 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,014.53 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 266 jetons, 14822 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3621 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2015.232847, 'cbBTC': 71439.030081, 'AERO': 0.524681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,630,587 | 2,014.532281 | 56661241 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,353,488 | 0.028185 | 56661241 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,530,488 | 0.028170 | 56661241 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,148,371 | 0.000014 | 56661241 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,861,871 | 2,012.768735 | 56661241 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,667,469 | 106.364244 | 56661241 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,210,722 | 0.028176 | 56661241 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,143,050 | 1.909173 | 56661241 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,103,083 | 2,012.338445 | 56661241 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,764,650 | 0.998724 | 56661241 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,959,720 | 43,356.266563 | 56661241 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 107 | 2,804,959 | 2,012.664258 | 56661241 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,154,553 | 0.028182 | 56661241 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,880,753 | 1,163,003.281972 | 56661241 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,640,819 | 0.016678 | 56661241 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,600,985 | 0.000014 | 56661241 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,568,686 | 0.000014 | 56661241 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,504,239 | 0.000000 | 56661241 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,482,794 | 0.006541 | 56661241 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,471,427 | 0.000014 | 56661241 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,867 | 0.831699 | 56661241 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,382,632 | 426.355960 | 56661241 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,258,695 | 2,014.576799 | 56661241 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,226,226 | 3,839.829121 | 56661241 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,188,462 | 15,134.189129 | 56661241 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,143,919 | 2,016.195050 | 56661241 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,099,574 | 2,012.745908 | 56661241 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,906 | 86.334668 | 56661241 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,037,340 | 1.402298 | 56661241 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,005,421 | 35,384,516.220924 | 56661241 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 984,365 | 106.184689 | 56661241 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 982,213 | 19.967701 | 56661241 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 922,012 | 559,964.211944 | 56661241 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 889,657 | 0.001493 | 56661241 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 883,052 | 23,226,178.240886 | 56661241 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 872,205 | 0.052875 | 56661241 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 871,169 | 1,003.516032 | 56661241 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 869,485 | 2,005.198605 | 56661241 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 867,552 | 0.000014 | 56661241 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | DRB/WETH | 10000 | 813,242 | 0.000000 | 56661241 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 784,435 | 76.439627 | 56661241 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 746,462 | 23.067562 | 56661241 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 746,128 | 0.049596 | 56661241 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 687,553 | 3,863.880959 | 56661241 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 682,526 | 0.801801 | 56661241 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 663,283 | 0.523679 | 56661241 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 623,782 | 4,946,140.933560 | 56661241 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 603,649 | 0.458886 | 56661241 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 582,910 | 151,430.597931 | 56661241 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 567,439 | 0.000260 | 56661241 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 566,083 | 555,181.807241 | 56661241 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 559,976 | 0.037928 | 56661241 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 556,988 | 0.000007 | 56661241 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 485,396 | 1,003.776826 | 56661241 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 460,215 | 0.066083 | 56661241 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 449,548 | 1.000977 | 56661241 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 448,732 | 0.499782 | 56661241 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/UNI | 10000 | 435,505 | 333.133817 | 56661241 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 429,614 | 24.862308 | 56661241 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 423,997 | 914,999.414728 | 56661241 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 1805 ; routes examinées : 26753710 ; candidats optimisés : 111388 ; net attendu > 0 : 198 ; dernier cycle 230.1 ms
- Rejets (moteur) : {'spread_below_threshold': 26259993, 'liquidity_below_min': 381996, 'negative_expected_net': 111190, 'borrow_bound_too_small': 277, 'cycle_budget_exhausted': 56}
- Enregistrements de la session : 111388 ; net attendu > 0 : 198 ; simulés (eth_call de la vraie tx) : 13 (ok 8, échec 5) ; étiquettes ghost N+1 : 9/10 positives
- Décisions : {'REJECTED': 111388} ; motifs de rejet : {'below_safety_margin': 178, 'negative_expected_net': 111190, 'p_lower_below_threshold': 190, 'reliability_not_demonstrated': 8, 'sim_below_estimate': 8, 'simulated_net_nonpositive': 5, 'simulation_failed': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56660485 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 26.746133 USDC | 0.021836 USDC | 0.000000 USDC | 0.004527 USDC | 0.017309 USDC (0.0159 €) | — | 6.47 | 0.076 (n=503) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 56660486 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 19.597201 USDC | 0.011690 USDC | 0.000000 USDC | 0.004527 USDC | 0.007163 USDC (0.0066 €) | — | 3.66 | 0.076 (n=503) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 56656791 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 185.539711 USDC | 0.011603 USDC | 0.000000 USDC | 0.006085 USDC | 0.005518 USDC (0.0051 €) | — | 0.30 | 0.270 (n=1622) | REJECTED | below_safety_margin(5518<37107), p_lower_below_threshold(0.27<0.75) |
| 56656795 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 185.539711 USDC | 0.011603 USDC | 0.000000 USDC | 0.006085 USDC | 0.005518 USDC (0.0051 €) | — | 0.30 | 0.270 (n=1622) | REJECTED | below_safety_margin(5518<37107), p_lower_below_threshold(0.27<0.75) |
| 56656791 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.073455 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0049 €) | — | 0.36 | 0.270 (n=1622) | REJECTED | below_safety_margin(2652904339512<14691081269871), p_lower_below_threshold(0.27<0.75) |
| 56656795 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.073455 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0049 €) | — | 0.36 | 0.270 (n=1622) | REJECTED | below_safety_margin(2652904339512<14691081269871), p_lower_below_threshold(0.27<0.75) |
| 56656791 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002789 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0046 €) | — | 0.25 | 0.270 (n=1622) | REJECTED | below_safety_margin(7<55), p_lower_below_threshold(0.27<0.75) |
| 56656795 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002789 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0046 €) | — | 0.25 | 0.270 (n=1622) | REJECTED | below_safety_margin(7<55), p_lower_below_threshold(0.27<0.75) |
| 56656790 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.114811 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(2197903303363<22962287772088), reliability_not_demonstrated |
| 56656793 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.114811 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(2197903303363<22962287772088), reliability_not_demonstrated |
| 56656790 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 227.968388 USDC | 0.008955 USDC | 0.000000 USDC | 0.004547 USDC | 0.004408 USDC (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(4408<45593), reliability_not_demonstrated |
| 56656793 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 227.968388 USDC | 0.008955 USDC | 0.000000 USDC | 0.004547 USDC | 0.004408 USDC (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(4408<45593), reliability_not_demonstrated |
| 56661187 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004725 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0037 €) | 0.000000 WETH | 4.17 | 0.210 (n=1278) | REJECTED | sim_below_estimate(3022261654781<4979512263742), p_lower_below_threshold(0.21<0.75) |
| 56661187 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.413961 USDC | 0.010022 USDC | 0.000000 USDC | 0.006058 USDC | 0.003964 USDC (0.0036 €) | — | 4.21 | 0.210 (n=1278) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 56661008 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004530 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0029 €) | 0.000000 WETH | 3.48 | 0.323 (n=601) | REJECTED | sim_below_estimate(3155800376288<4585638879644), p_lower_below_threshold(0.32<0.75) |
| 56661008 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.999567 USDC | 0.009230 USDC | 0.000000 USDC | 0.006059 USDC | 0.003171 USDC (0.0029 €) | — | 3.52 | 0.323 (n=601) | REJECTED | p_lower_below_threshold(0.32<0.75) |
| 56661008 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004530 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0029 €) | 0.000000 WETH | 3.43 | 0.209 (n=1277) | REJECTED | sim_below_estimate(3131265413094<4561097824658), p_lower_below_threshold(0.21<0.75) |
| 56661008 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.998645 USDC | 0.009181 USDC | 0.000000 USDC | 0.006059 USDC | 0.003122 USDC (0.0029 €) | — | 3.47 | 0.209 (n=1277) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 56661187 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0026 €) | -0.000000 WETH | 3.22 | 0.324 (n=602) | REJECTED | sim_below_estimate(2602237901088<4429092756971), simulated_net_nonpositive, p_lower_below_threshold(0.32<0.75) |
| 56656791 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000636 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0026 €) | — | 0.63 | 0.270 (n=1622) | REJECTED | below_safety_margin(4<12), p_lower_below_threshold(0.27<0.75) |
| 56656795 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000636 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0026 €) | — | 0.63 | 0.270 (n=1622) | REJECTED | below_safety_margin(4<12), p_lower_below_threshold(0.27<0.75) |
| 56661187 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.872237 USDC | 0.008915 USDC | 0.000000 USDC | 0.006058 USDC | 0.002857 USDC (0.0026 €) | — | 3.22 | 0.324 (n=602) | REJECTED | p_lower_below_threshold(0.32<0.75) |
| 56656791 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 45.637786 USDC | 0.008615 USDC | 0.000000 USDC | 0.006085 USDC | 0.002530 USDC (0.0023 €) | — | 0.55 | 0.270 (n=1622) | REJECTED | below_safety_margin(2530<9127), p_lower_below_threshold(0.27<0.75) |
| 56656795 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 45.637786 USDC | 0.008615 USDC | 0.000000 USDC | 0.006085 USDC | 0.002530 USDC (0.0023 €) | — | 0.55 | 0.270 (n=1622) | REJECTED | below_safety_margin(2530<9127), p_lower_below_threshold(0.27<0.75) |
| 56656791 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025189 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | — | 0.50 | 0.270 (n=1622) | REJECTED | below_safety_margin(1250770259656<5037766025930), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8478 ; taux observé 0.224 ; borne inférieure crédible (0.9) 0.218 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
