# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T13:52:53+00:00 ; durée 207.17 min ; blocs 52894493 → 52900709 (4695 vus)

## Connexion
- Requêtes RPC : 66264 ; erreurs : 138 ; latence p50/p95 : 292.6/960.7 ms
- Rafraîchissements d'état : 4695 ; âge des données au dernier bloc : 3.17 s ; changements de frais LP observés (pools à frais dynamiques) : 15096
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 69675 ; cycles déclenchés par événement : 3068 ; avance médiane sur le rafraîchissement multicall : 372 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,465.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 326 jetons, 21598 routes
- Par DEX : uniswap_v3 138, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 3 → gardés 578 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2451.17881, 'AERO': 0.838921, 'cbBTC': 83216.410353}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,809,426 | 2,465.729178 | 52900710 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,471,636 | 1.162527 | 52900710 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,925,667 | 94.726333 | 52900710 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,532,052 | 0.029504 | 52900710 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 12,928,190 | 0.029526 | 52900710 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,502,702 | 0.029540 | 52900710 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,896,683 | 0.000012 | 52900710 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,814,304 | 2,471.957751 | 52900710 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,487,988 | 2,465.722164 | 52900710 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 7,411,804 | 0.000012 | 52900710 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,328,321 | 0.001665 | 52900710 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 7,320,699 | 0.000012 | 52900710 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 833 | 7,063,354 | 2,472.325645 | 52900710 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,646,434 | 0.029517 | 52900710 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,983,943 | 0.023127 | 52900710 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,752,283 | 0.802390 | 52900710 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,466,127 | 2,472.465848 | 52900710 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,436,022 | 0.998741 | 52900710 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,360,412 | 1.164397 | 52900710 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,279,306 | 0.000279 | 52900710 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,071,562 | 34,783.771880 | 52900710 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 454 | 3,791,164 | 2,474.849891 | 52900710 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,387,779 | 2,878.747759 | 52900710 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,782,678 | 94.715560 | 52900710 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,551,608 | 1.142099 | 52900710 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,407,209 | 392.155185 | 52900710 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 2,280,414 | 0.915922 | 52900710 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,273,510 | 0.000012 | 52900710 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,257,177 | 1,210,727.444472 | 52900710 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,163,107 | 0.000010 | 52900710 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,074,927 | 0.000012 | 52900710 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,072 | 1.383640 | 52900710 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,973,133 | 0.000000 | 52900710 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,954,943 | 1,041.050095 | 52900710 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | weETH_04c0/WETH | 500 | 1,920,939 | 1.105697 | 52900710 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,873,731 | 15.888805 | 52900710 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,798,307 | 0.018980 | 52900710 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,708,077 | 1.494073 | 52900710 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,701,217 | 2.312831 | 52900710 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,693,785 | 2,871.888570 | 52900710 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,579,689 | 13,298.820190 | 52900710 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,228 | 0.826500 | 52900710 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | fBOMB/USDC | 10000 | 1,447,635 | 0.019927 | 52900710 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,431,197 | 1.123340 | 52900710 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,353,624 | 0.004769 | 52900710 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,347,288 | 0.000000 | 52900710 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,344,806 | 0.000280 | 52900710 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,320,856 | 0.029542 | 52900710 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,276,460 | 2,472.002020 | 52900710 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/NOCK | 3000 | 1,237,041 | 41.175392 | 52900710 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | USDC/SEND | 3000 | 1,232,108 | 64.009584 | 52900710 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,231,155 | 35,025,537.401950 | 52900710 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,220,010 | 1,107,458.177309 | 52900710 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,208,003 | 23.095890 | 52900710 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,202,676 | 71,956.905903 | 52900710 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,196,236 | 0.886561 | 52900710 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | WETH/VVV | 8000 | 1,193,083 | 94.415479 | 52900710 | `0x46D398A5b33709877f50c8918A7eE96F1Be1d7dd` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,188,624 | 483,704.121639 | 52900710 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,182,139 | 0.436970 | 52900710 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,166,930 | 1.106158 | 52900710 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 7762 ; routes examinées : 167643676 ; candidats optimisés : 940042 ; net attendu > 0 : 850 ; dernier cycle 180.3 ms
- Rejets (moteur) : {'spread_below_threshold': 165235256, 'liquidity_below_min': 1312402, 'negative_expected_net': 939192, 'pool_quarantined': 136358, 'cycle_budget_exhausted': 11899, 'borrow_bound_too_small': 7719}
- Enregistrements de la session : 940042 ; net attendu > 0 : 850 ; simulés (eth_call de la vraie tx) : 57 (ok 36, échec 21) ; étiquettes ghost N+1 : 2/43 positives
- Décisions : {'REJECTED': 940042} ; motifs de rejet : {'below_safety_margin': 665, 'negative_expected_net': 939192, 'p_lower_below_threshold': 668, 'price_impact': 67, 'reliability_not_demonstrated': 182, 'simulation_failed': 21, 'stale_data': 51}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52900169 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.581274 WETH | 0.000068 WETH | 0.000000 WETH | 0.000004 WETH | 0.000064 WETH (0.1457 €) | — | 1.10 | 0.116 (n=200) | REJECTED | below_safety_margin(64102908464548<116254832592802), p_lower_below_threshold(0.12<0.75) |
| 52900169 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,429.608629 USDC | 0.167305 USDC | 0.000000 USDC | 0.009459 USDC | 0.157846 USDC (0.1452 €) | — | 1.10 | 0.116 (n=200) | REJECTED | below_safety_margin(157846<285921), p_lower_below_threshold(0.12<0.75) |
| 52900450 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,900.583817 USDC | 0.154025 USDC | 0.000000 USDC | 0.008192 USDC | 0.145833 USDC (0.1342 €) | — | 0.77 | 0.116 (n=200) | REJECTED | below_safety_margin(145833<380116), p_lower_below_threshold(0.12<0.75) |
| 52900450 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.771589 WETH | 0.000063 WETH | 0.000000 WETH | 0.000003 WETH | 0.000059 WETH (0.1340 €) | — | 0.77 | 0.116 (n=200) | REJECTED | below_safety_margin(59189288047738<154317894782081), p_lower_below_threshold(0.12<0.75) |
| 52900242 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 97.699511 USDC | 0.128001 USDC | 0.000000 USDC | 0.006742 USDC | 0.121259 USDC (0.1116 €) | 0.121259 USDC | 12.41 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52900286 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,221.317627 USDC | 0.122303 USDC | 0.000000 USDC | 0.008976 USDC | 0.113327 USDC (0.1043 €) | — | 0.93 | 0.116 (n=200) | REJECTED | below_safety_margin(113327<244263), p_lower_below_threshold(0.12<0.75) |
| 52900286 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,221.317627 USDC | 0.122303 USDC | 0.000000 USDC | 0.008976 USDC | 0.113327 USDC (0.1043 €) | — | 0.93 | 0.116 (n=200) | REJECTED | below_safety_margin(113327<244263), p_lower_below_threshold(0.12<0.75) |
| 52900286 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.495927 WETH | 0.000050 WETH | 0.000000 WETH | 0.000004 WETH | 0.000046 WETH (0.1041 €) | — | 0.93 | 0.116 (n=200) | REJECTED | below_safety_margin(45964345312096<99185305325842), p_lower_below_threshold(0.12<0.75) |
| 52900286 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.495927 WETH | 0.000050 WETH | 0.000000 WETH | 0.000004 WETH | 0.000046 WETH (0.1041 €) | — | 0.93 | 0.116 (n=200) | REJECTED | below_safety_margin(45964345312096<99185305325842), p_lower_below_threshold(0.12<0.75) |
| 52900061 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.468529 WETH | 0.000049 WETH | 0.000000 WETH | 0.000004 WETH | 0.000045 WETH (0.1019 €) | — | 0.96 | 0.116 (n=200) | REJECTED | below_safety_margin(44784266912017<93705786120286), stale_data(5433ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52900061 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,160.370730 USDC | 0.119874 USDC | 0.000000 USDC | 0.009229 USDC | 0.110645 USDC (0.1018 €) | — | 0.95 | 0.116 (n=200) | REJECTED | below_safety_margin(110645<232074), stale_data(5438ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52900169 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.437217 WETH | 0.000041 WETH | 0.000000 WETH | 0.000004 WETH | 0.000037 WETH (0.0849 €) | — | 0.85 | 0.116 (n=200) | REJECTED | below_safety_margin(37333600127996<87443315346783), p_lower_below_threshold(0.12<0.75) |
| 52900169 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 1,072.745064 USDC | 0.101373 USDC | 0.000000 USDC | 0.009459 USDC | 0.091914 USDC (0.0846 €) | — | 0.86 | 0.116 (n=200) | REJECTED | below_safety_margin(91914<214549), p_lower_below_threshold(0.12<0.75) |
| 52900169 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.429981 WETH | 0.000034 WETH | 0.000000 WETH | 0.000004 WETH | 0.000030 WETH (0.0692 €) | — | 0.71 | 0.116 (n=200) | REJECTED | below_safety_margin(30448274547133<85996278112903), p_lower_below_threshold(0.12<0.75) |
| 52900169 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 1,085.120033 USDC | 0.084218 USDC | 0.000000 USDC | 0.009459 USDC | 0.074759 USDC (0.0688 €) | — | 0.69 | 0.116 (n=200) | REJECTED | below_safety_margin(74759<217024), p_lower_below_threshold(0.12<0.75) |
| 52900098 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.311084 WETH | 0.000034 WETH | 0.000000 WETH | 0.000004 WETH | 0.000030 WETH (0.0687 €) | — | 0.97 | 0.116 (n=200) | REJECTED | below_safety_margin(30186260413141<62216731304037), p_lower_below_threshold(0.12<0.75) |
| 52900098 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 767.008244 USDC | 0.083609 USDC | 0.000000 USDC | 0.009208 USDC | 0.074401 USDC (0.0684 €) | — | 0.97 | 0.116 (n=200) | REJECTED | below_safety_margin(74401<153401), p_lower_below_threshold(0.12<0.75) |
| 52900169 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.011426 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0684 €) | — | 0.78 | 0.116 (n=200) | REJECTED | below_safety_margin(89<228), p_lower_below_threshold(0.12<0.75) |
| 52900169 | WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.370922 WETH | 0.000032 WETH | 0.000000 WETH | 0.000004 WETH | 0.000028 WETH (0.0640 €) | — | 0.76 | 0.116 (n=200) | REJECTED | below_safety_margin(28155813190555<74184378683437), p_lower_below_threshold(0.12<0.75) |
| 52900169 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.010008 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0638 €) | — | 0.83 | 0.116 (n=200) | REJECTED | below_safety_margin(83<200), p_lower_below_threshold(0.12<0.75) |
| 52900169 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 884.506146 USDC | 0.078697 USDC | 0.000000 USDC | 0.009459 USDC | 0.069238 USDC (0.0637 €) | — | 0.78 | 0.116 (n=200) | REJECTED | below_safety_margin(69238<176901), p_lower_below_threshold(0.12<0.75) |
| 52899326 | USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 184.388724 USDC | 0.073887 USDC | 0.000000 USDC | 0.009339 USDC | 0.064548 USDC (0.0594 €) | — | 3.50 | 0.115 (n=155) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52899326 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH | 0.074309 WETH | 0.000030 WETH | 0.000000 WETH | 0.000004 WETH | 0.000026 WETH (0.0592 €) | 0.000026 WETH | 3.48 | 0.115 (n=155) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52899325 | USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 176.029615 USDC | 0.066830 USDC | 0.000000 USDC | 0.008706 USDC | 0.058124 USDC (0.0535 €) | — | 3.30 | 0.105 (n=153) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52899325 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH | 0.070579 WETH | 0.000027 WETH | 0.000000 WETH | 0.000004 WETH | 0.000023 WETH (0.0534 €) | 0.000023 WETH | 3.31 | 0.105 (n=153) | REJECTED | p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1696 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
