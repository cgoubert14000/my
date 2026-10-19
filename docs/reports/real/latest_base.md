# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T05:48:21+00:00 ; durée 238.68 min ; blocs 52792613 → 52799768 (6468 vus)

## Connexion
- Requêtes RPC : 88926 ; erreurs : 50 ; latence p50/p95 : 395.0/1,514.7 ms
- Rafraîchissements d'état : 6468 ; âge des données au dernier bloc : 4.03 s ; changements de frais LP observés (pools à frais dynamiques) : 11860
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 117508 ; cycles déclenchés par événement : 6494 ; avance médiane sur le rafraîchissement multicall : 1,110 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,424.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 574 pools, 328 jetons, 21112 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 2 → gardés 574 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2418.692382, 'AERO': 0.800914, 'cbBTC': 82392.905144}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,845,232 | 2,424.761815 | 52799768 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,339,407 | 1.257835 | 52799768 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,322,949 | 0.029364 | 52799768 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,296,951 | 0.029377 | 52799768 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,367,792 | 100.719315 | 52799768 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,462,018 | 0.029365 | 52799768 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,836,567 | 0.000012 | 52799768 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,742,129 | 0.000012 | 52799768 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,464,543 | 2,426.369682 | 52799768 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 549 | 8,434,924 | 2,426.782357 | 52799768 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,849,973 | 0.000012 | 52799768 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,243,679 | 0.001666 | 52799768 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,491,176 | 2,426.952890 | 52799768 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,309,405 | 0.029374 | 52799768 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,265,542 | 1.000854 | 52799768 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,913,627 | 0.025832 | 52799768 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,846,791 | 0.802398 | 52799768 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,659,464 | 0.000273 | 52799768 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,504,119 | 2,426.536755 | 52799768 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,455,478 | 1.255616 | 52799768 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,399,260 | 0.998050 | 52799768 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 403 | 4,390,274 | 2,429.870227 | 52799768 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,103,010 | 33,125.072733 | 52799768 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,281,448 | 3,041.199214 | 52799768 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,922,075 | 1.141828 | 52799768 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,863,410 | 0.000012 | 52799768 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,677,874 | 407.398722 | 52799768 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,644,806 | 100.746996 | 52799768 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,390,406 | 0.000010 | 52799768 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,234,062 | 1,195,844.662003 | 52799768 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,866 | 1.233066 | 52799768 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52799768 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,993,727 | 0.000000 | 52799768 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,800,699 | 15.893238 | 52799768 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,782,235 | 0.000012 | 52799768 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,756,207 | 0.018492 | 52799768 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,753,303 | 1.105523 | 52799768 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,730,201 | 0.020721 | 52799768 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,684,706 | 2.310001 | 52799768 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,666,505 | 13,884.646022 | 52799768 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,618,370 | 3,055.267832 | 52799768 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,479,150 | 1.122950 | 52799768 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,471,130 | 0.916352 | 52799768 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,560 | 0.827303 | 52799768 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,329,892 | 0.000000 | 52799768 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,125 | 0.436559 | 52799768 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,306,030 | 0.000272 | 52799768 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,287,437 | 0.004582 | 52799768 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,286,653 | 23.118209 | 52799768 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,278,971 | 0.029358 | 52799768 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,282 | 63.887836 | 52799768 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,212,273 | 2,426.505325 | 52799768 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,208,947 | 35,040,930.127724 | 52799768 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,205,021 | 0.886176 | 52799768 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,166,908 | 1,170,699.598270 | 52799768 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,737 | 523,491.512620 | 52799768 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,096,763 | 52.383050 | 52799768 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,089,519 | 15.069004 | 52799768 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,081,168 | 1.132141 | 52799768 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,069,209 | 1.105811 | 52799768 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 12961 ; routes examinées : 273632632 ; candidats optimisés : 1873205 ; net attendu > 0 : 235 ; dernier cycle 431.8 ms
- Rejets (moteur) : {'spread_below_threshold': 269222357, 'liquidity_below_min': 2145893, 'negative_expected_net': 1872970, 'pool_quarantined': 264466, 'borrow_bound_too_small': 125255, 'cycle_budget_exhausted': 1424, 'unquotable': 32}
- Enregistrements de la session : 1873205 ; net attendu > 0 : 235 ; simulés (eth_call de la vraie tx) : 43 (ok 2, échec 41) ; étiquettes ghost N+1 : 1/25 positives
- Décisions : {'REJECTED': 1873205} ; motifs de rejet : {'below_safety_margin': 174, 'negative_expected_net': 1872970, 'p_lower_below_threshold': 208, 'price_impact': 83, 'reliability_not_demonstrated': 27, 'simulation_failed': 41, 'stale_data': 5}

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
| 52799711 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 80.673261 USDC | 0.101641 USDC | 0.000000 USDC | 0.005812 USDC | 0.095829 USDC (0.0882 €) | — | 11.88 | 0.000 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52799710 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 80.673261 USDC | 0.101641 USDC | 0.000000 USDC | 0.005812 USDC | 0.095829 USDC (0.0882 €) | — | 11.88 | 0.000 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
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

## Fiabilité et décision
- Observations ghost : 1245 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
