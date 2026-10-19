# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T05:08:48+00:00 ; durée 199.13 min ; blocs 52792613 → 52798582 (5475 vus)

## Connexion
- Requêtes RPC : 75017 ; erreurs : 0 ; latence p50/p95 : 387.0/1,429.9 ms
- Rafraîchissements d'état : 5475 ; âge des données au dernier bloc : 5.8 s ; changements de frais LP observés (pools à frais dynamiques) : 9395
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 100049 ; cycles déclenchés par événement : 5539 ; avance médiane sur le rafraîchissement multicall : 1,250 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,424.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 574 pools, 328 jetons, 21112 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 2 → gardés 574 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2418.692382, 'AERO': 0.800914, 'cbBTC': 82392.905144}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,756,821 | 2,424.767372 | 52798582 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,394,085 | 1.254021 | 52798582 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,324,552 | 0.029340 | 52798582 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,231,151 | 0.029377 | 52798582 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,322,700 | 101.244818 | 52798582 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,473,466 | 0.029365 | 52798582 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,839,757 | 0.000012 | 52798582 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,464,065 | 2,422.718071 | 52798582 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,852,346 | 0.000012 | 52798582 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 639 | 7,609,994 | 2,423.079465 | 52798582 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,249,036 | 0.001666 | 52798582 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 7,047,576 | 0.000012 | 52798582 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,491,182 | 2,426.013565 | 52798582 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,310,422 | 0.029348 | 52798582 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,265,554 | 1.000854 | 52798582 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,920,983 | 0.025831 | 52798582 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,846,802 | 0.802398 | 52798582 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,648,600 | 0.000271 | 52798582 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,474,998 | 1.255616 | 52798582 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,454,750 | 2,422.901164 | 52798582 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,402,846 | 0.998050 | 52798582 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,098,591 | 33,196.677133 | 52798582 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 415 | 3,844,993 | 2,426.262052 | 52798582 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,286,507 | 3,024.846350 | 52798582 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,922,080 | 1.141828 | 52798582 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,864,733 | 0.000012 | 52798582 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,750,989 | 408.493604 | 52798582 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,638,499 | 101.198427 | 52798582 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,490,388 | 0.000010 | 52798582 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,221,105 | 1,209,843.204873 | 52798582 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,866 | 1.233066 | 52798582 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 2,063,543 | 1,027.551152 | 52798582 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52798582 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,007,715 | 0.000000 | 52798582 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,823,459 | 13,921.914455 | 52798582 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,813,128 | 15.972959 | 52798582 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,783,772 | 0.000012 | 52798582 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,761,569 | 0.018484 | 52798582 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,753,307 | 1.105523 | 52798582 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,730,139 | 0.020720 | 52798582 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,684,710 | 2.310001 | 52798582 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,620,031 | 3,033.687598 | 52798582 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,479,189 | 1.123004 | 52798582 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,471,133 | 0.916352 | 52798582 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,560 | 0.827303 | 52798582 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,330,955 | 0.000000 | 52798582 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,059 | 0.436559 | 52798582 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,302,990 | 0.000272 | 52798582 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,294,305 | 0.004582 | 52798582 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,285,559 | 23.118201 | 52798582 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,279,494 | 0.029360 | 52798582 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,231 | 63.893053 | 52798582 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,208,950 | 35,040,930.127724 | 52798582 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,205,000 | 0.886176 | 52798582 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,202,750 | 2,422.554801 | 52798582 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,166,898 | 1,170,712.653342 | 52798582 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,740 | 523,491.512620 | 52798582 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,095,188 | 52.533817 | 52798582 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,087,430 | 15.143509 | 52798582 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,081,171 | 1.132141 | 52798582 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |

## Recherche d'opportunités
- Cycles : 11013 ; routes examinées : 232506456 ; candidats optimisés : 1530403 ; net attendu > 0 : 233 ; dernier cycle 623.2 ms
- Rejets (moteur) : {'spread_below_threshold': 228767729, 'liquidity_below_min': 1820431, 'negative_expected_net': 1530170, 'pool_quarantined': 264466, 'borrow_bound_too_small': 122331, 'cycle_budget_exhausted': 1064, 'unquotable': 32}
- Enregistrements de la session : 1530403 ; net attendu > 0 : 233 ; simulés (eth_call de la vraie tx) : 41 (ok 2, échec 39) ; étiquettes ghost N+1 : 1/24 positives
- Décisions : {'REJECTED': 1530403} ; motifs de rejet : {'below_safety_margin': 174, 'negative_expected_net': 1530170, 'p_lower_below_threshold': 206, 'price_impact': 83, 'reliability_not_demonstrated': 27, 'simulation_failed': 39, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52792917 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 2,540.515336 USDC | 0.620948 USDC | 0.000000 USDC | 0.009104 USDC | 0.611844 USDC (0.5629 €) | — | 2.41 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52792917 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.030002 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5624 €) | — | 2.48 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52792917 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.062362 WETH | 0.000256 WETH | 0.000000 WETH | 0.000004 WETH | 0.000253 WETH (0.5619 €) | — | 2.38 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52796577 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.432597 WETH | 0.000137 WETH | 0.000000 WETH | 0.000003 WETH | 0.000134 WETH (0.2989 €) | — | 3.10 | 0.000 (n=78) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52796577 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,047.046138 USDC | 0.331114 USDC | 0.000000 USDC | 0.006920 USDC | 0.324194 USDC (0.2983 €) | — | 3.10 | 0.000 (n=78) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52792917 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 726.896227 USDC | 0.187828 USDC | 0.000000 USDC | 0.007636 USDC | 0.180192 USDC (0.1658 €) | — | 2.48 | 0.100 (n=143) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52792917 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.008649 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1658 €) | — | 2.53 | 0.100 (n=143) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52792917 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.293799 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1654 €) | — | 2.53 | 0.100 (n=143) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52796577 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 666.112986 USDC | 0.148860 USDC | 0.000000 USDC | 0.008394 USDC | 0.140466 USDC (0.1292 €) | — | 2.11 | 0.099 (n=145) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52796577 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007829 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1292 €) | — | 2.17 | 0.099 (n=145) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52796577 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.263016 WETH | 0.000061 WETH | 0.000000 WETH | 0.000003 WETH | 0.000058 WETH (0.1289 €) | — | 2.20 | 0.099 (n=145) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52796000 | WETH→[aerodrome_slipstream]→DRB→[uniswap_v3]→WETH | 0.083311 WETH | 0.000055 WETH | 0.000000 WETH | 0.000002 WETH | 0.000053 WETH (0.1179 €) | — | 6.34 | 0.073 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52792917 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 1,123.674556 USDC | 0.100037 USDC | 0.000000 USDC | 0.006165 USDC | 0.093872 USDC (0.0864 €) | — | 0.84 | 0.017 (n=47) | REJECTED | below_safety_margin(93872<224734), p_lower_below_threshold(0.02<0.75) |
| 52792917 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.013002 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0863 €) | — | 0.88 | 0.017 (n=47) | REJECTED | below_safety_margin(114<260), p_lower_below_threshold(0.02<0.75) |
| 52795958 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.574926 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0614 €) | — | 0.48 | 0.099 (n=145) | REJECTED | below_safety_margin(27487400276779<114985243818911), p_lower_below_threshold(0.10<0.75) |
| 52795958 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,388.010819 USDC | 0.074147 USDC | 0.000000 USDC | 0.007660 USDC | 0.066487 USDC (0.0612 €) | — | 0.48 | 0.099 (n=145) | REJECTED | below_safety_margin(66487<277602), p_lower_below_threshold(0.10<0.75) |
| 52797418 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 57.675462 USDC | 0.050662 USDC | 0.000000 USDC | 0.005444 USDC | 0.045218 USDC (0.0416 €) | — | 7.84 | 0.000 (n=81) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52797341 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 56.683252 USDC | 0.049627 USDC | 0.000000 USDC | 0.005445 USDC | 0.044182 USDC (0.0406 €) | — | 7.79 | 0.000 (n=80) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52792917 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 207.774774 USDC | 0.049529 USDC | 0.000000 USDC | 0.008370 USDC | 0.041159 USDC (0.0379 €) | — | 1.98 | 0.100 (n=143) | REJECTED | below_safety_margin(41159<41554), p_lower_below_threshold(0.10<0.75) |
| 52792917 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.082983 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0378 €) | — | 2.05 | 0.100 (n=143) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52792917 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002420 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0378 €) | — | 2.07 | 0.100 (n=143) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52792917 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 176.238869 USDC | 0.044327 USDC | 0.000000 USDC | 0.008370 USDC | 0.035957 USDC (0.0331 €) | — | 2.04 | 0.100 (n=143) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52792917 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.066738 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0328 €) | — | 2.21 | 0.100 (n=143) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52792917 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001932 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0325 €) | — | 2.23 | 0.100 (n=143) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52794394 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 825.799444 USDC | 0.032405 USDC | 0.000000 USDC | 0.005432 USDC | 0.026973 USDC (0.0248 €) | — | 0.33 | 0.017 (n=47) | REJECTED | below_safety_margin(26973<165159), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 1244 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
