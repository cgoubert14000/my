# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T11:08:28+00:00 ; durée 130.24 min ; blocs 52762270 → 52766177 (3892 vus)

## Connexion
- Requêtes RPC : 53799 ; erreurs : 0 ; latence p50/p95 : 247.8/707.4 ms
- Rafraîchissements d'état : 3893 ; âge des données au dernier bloc : 1.45 s ; changements de frais LP observés (pools à frais dynamiques) : 8313
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 64511 ; cycles déclenchés par événement : 5413 ; avance médiane sur le rafraîchissement multicall : 369 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,419.40 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 328 jetons, 21580 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2410.986474, 'AERO': 0.834015, 'cbBTC': 81629.281689}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,336,975 | 2,419.395268 | 52766177 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,829,060 | 1.205608 | 52766177 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,278,916 | 0.029466 | 52766177 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,794,573 | 107.365393 | 52766177 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 10,600,090 | 0.029526 | 52766177 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,444,411 | 0.029525 | 52766177 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,779,503 | 0.000012 | 52766177 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,072,622 | 2,416.381648 | 52766177 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,873,651 | 0.000012 | 52766177 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,214,725 | 2,416.254130 | 52766177 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,176,481 | 0.001654 | 52766177 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 6,571,772 | 0.000012 | 52766177 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,496,872 | 2,420.297132 | 52766177 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,337,750 | 0.029463 | 52766177 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,253,888 | 1.000855 | 52766177 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,117,304 | 0.025630 | 52766177 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,836,061 | 0.802398 | 52766177 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,645,923 | 0.000272 | 52766177 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,458,494 | 0.998809 | 52766177 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,451,363 | 2,416.530529 | 52766177 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,077,863 | 33,386.571494 | 52766177 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,010,116 | 1.199286 | 52766177 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,333,983 | 2,900.669684 | 52766177 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 409 | 3,109,613 | 2,420.040994 | 52766177 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,917,325 | 1.141818 | 52766177 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,848,876 | 0.000012 | 52766177 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,741,408 | 408.067151 | 52766177 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,632,031 | 0.000010 | 52766177 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,566,778 | 107.332175 | 52766177 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,243,182 | 1,180,896.116247 | 52766177 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 2,242,643 | 1,002.462256 | 52766177 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,106,813 | 1.199655 | 52766177 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,374 | 1.374087 | 52766177 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,506 | 1.123285 | 52766177 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,871,373 | 0.000000 | 52766177 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,832,948 | 15.733469 | 52766177 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,810,102 | 0.021552 | 52766177 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,774,327 | 0.000012 | 52766177 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,764,593 | 13,843.954390 | 52766177 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,762,264 | 0.018535 | 52766177 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,749,526 | 1.105495 | 52766177 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/msETH (stable) | 500 | 1,675,560 | 2.306584 | 52766177 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,513,481 | 2,912.032598 | 52766177 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,471,459 | 0.916369 | 52766177 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,377 | 0.826256 | 52766177 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,447,675 | 2,912.348678 | 52766177 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,332,276 | 0.000000 | 52766177 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,320,084 | 0.436186 | 52766177 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,302,151 | 0.000271 | 52766177 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,289,066 | 0.004602 | 52766177 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,261,097 | 0.029519 | 52766177 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,248,124 | 62.377421 | 52766177 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,244,080 | 23.359070 | 52766177 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,208,826 | 2,416.336781 | 52766177 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,204,981 | 35,101,236.854252 | 52766177 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,181,665 | 0.885831 | 52766177 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,166,556 | 1,166,457.847044 | 52766177 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,139,912 | 1.131653 | 52766177 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,137,274 | 517,013.914854 | 52766177 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,102,770 | 14.628160 | 52766177 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 9305 ; routes examinées : 200801900 ; candidats optimisés : 1093824 ; net attendu > 0 : 321 ; dernier cycle 126.7 ms
- Rejets (moteur) : {'spread_below_threshold': 198020093, 'liquidity_below_min': 1675438, 'negative_expected_net': 1093503, 'borrow_bound_too_small': 9303, 'pool_quarantined': 2826, 'cycle_budget_exhausted': 306}
- Enregistrements de la session : 1093821 ; net attendu > 0 : 321 ; simulés (eth_call de la vraie tx) : 49 (ok 12, échec 37) ; étiquettes ghost N+1 : 0/37 positives
- Décisions : {'REJECTED': 1093821} ; motifs de rejet : {'below_safety_margin': 228, 'negative_expected_net': 1093500, 'p_lower_below_threshold': 218, 'reliability_not_demonstrated': 103, 'simulation_failed': 37, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52763312 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.045860 WETH | 0.000451 WETH | 0.000000 WETH | 0.000002 WETH | 0.000449 WETH (0.9969 €) | — | 97.84 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52763336 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.044695 WETH | 0.000379 WETH | 0.000000 WETH | 0.000002 WETH | 0.000377 WETH (0.8390 €) | — | 84.36 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 331.897771 USDC | 0.790288 USDC | 0.000000 USDC | 0.007637 USDC | 0.782651 USDC (0.7200 €) | — | 23.58 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.137210 WETH | 0.000326 WETH | 0.000000 WETH | 0.000003 WETH | 0.000323 WETH (0.7192 €) | — | 23.55 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 334.557229 USDC | 0.776637 USDC | 0.000000 USDC | 0.007637 USDC | 0.769000 USDC (0.7075 €) | — | 22.99 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.138268 WETH | 0.000321 WETH | 0.000000 WETH | 0.000003 WETH | 0.000317 WETH (0.7067 €) | — | 22.96 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52762636 | WETH→[aerodrome_slipstream]→KTA→[aerodrome]→WETH | 0.107115 WETH | 0.000278 WETH | 0.000000 WETH | 0.000002 WETH | 0.000276 WETH (0.6125 €) | — | 25.74 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 294.578188 USDC | 0.599486 USDC | 0.000000 USDC | 0.007637 USDC | 0.591849 USDC (0.5445 €) | — | 20.09 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.121496 WETH | 0.000247 WETH | 0.000000 WETH | 0.000003 WETH | 0.000244 WETH (0.5436 €) | — | 20.10 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 287.191677 USDC | 0.570485 USDC | 0.000000 USDC | 0.007637 USDC | 0.562848 USDC (0.5178 €) | — | 19.60 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.118596 WETH | 0.000235 WETH | 0.000000 WETH | 0.000003 WETH | 0.000232 WETH (0.5169 €) | — | 19.58 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 279.567138 USDC | 0.544737 USDC | 0.000000 USDC | 0.007637 USDC | 0.537100 USDC (0.4941 €) | — | 19.21 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.115494 WETH | 0.000225 WETH | 0.000000 WETH | 0.000003 WETH | 0.000222 WETH (0.4932 €) | — | 19.19 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 211.066296 USDC | 0.415657 USDC | 0.000000 USDC | 0.008004 USDC | 0.407653 USDC (0.3750 €) | — | 19.31 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.087085 WETH | 0.000171 WETH | 0.000000 WETH | 0.000003 WETH | 0.000168 WETH (0.3740 €) | — | 19.29 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52763600 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 3,878.632894 USDC | 0.327748 USDC | 0.000000 USDC | 0.007270 USDC | 0.320478 USDC (0.2948 €) | — | 0.83 | 0.322 (n=60) | REJECTED | below_safety_margin(320478<775726), p_lower_below_threshold(0.32<0.75) |
| 52763600 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 1.603094 WETH | 0.000135 WETH | 0.000000 WETH | 0.000003 WETH | 0.000132 WETH (0.2943 €) | — | 0.82 | 0.322 (n=60) | REJECTED | below_safety_margin(132222049332856<320618754324269), p_lower_below_threshold(0.32<0.75) |
| 52765230 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 196.919296 USDC | 0.267588 USDC | 0.000000 USDC | 0.007637 USDC | 0.259951 USDC (0.2392 €) | — | 13.20 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52763327 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.023839 WETH | 0.000109 WETH | 0.000000 WETH | 0.000002 WETH | 0.000107 WETH (0.2388 €) | — | 45.05 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.081360 WETH | 0.000110 WETH | 0.000000 WETH | 0.000003 WETH | 0.000107 WETH (0.2384 €) | — | 13.17 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765037 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 125.143578 USDC | 0.217093 USDC | 0.000000 USDC | 0.005432 USDC | 0.211661 USDC (0.1947 €) | — | 16.91 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 171.889138 USDC | 0.214140 USDC | 0.000000 USDC | 0.007637 USDC | 0.206503 USDC (0.1900 €) | — | 12.01 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.070919 WETH | 0.000088 WETH | 0.000000 WETH | 0.000003 WETH | 0.000085 WETH (0.1893 €) | — | 11.99 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52763600 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 2,367.368873 USDC | 0.209741 USDC | 0.000000 USDC | 0.007638 USDC | 0.202103 USDC (0.1859 €) | — | 0.85 | 0.137 (n=99) | REJECTED | below_safety_margin(202103<473473), p_lower_below_threshold(0.14<0.75) |
| 52763600 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.978603 WETH | 0.000087 WETH | 0.000000 WETH | 0.000003 WETH | 0.000083 WETH (0.1856 €) | — | 0.85 | 0.137 (n=99) | REJECTED | below_safety_margin(83378593383533<195720682064356), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 900 ; taux observé 0.126 ; borne inférieure crédible (0.9) 0.112 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
