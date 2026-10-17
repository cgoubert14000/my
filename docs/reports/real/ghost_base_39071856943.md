# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T22:49:35+00:00 ; durée 64.6 min ; blocs 52742072 → 52744009 (1746 vus)

## Connexion
- Requêtes RPC : 23405 ; erreurs : 0 ; latence p50/p95 : 397.6/1,368.6 ms
- Rafraîchissements d'état : 1746 ; âge des données au dernier bloc : 7.99 s ; changements de frais LP observés (pools à frais dynamiques) : 4545
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 39450 ; cycles déclenchés par événement : 1741 ; avance médiane sur le rafraîchissement multicall : 1,583 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,388.32 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21034 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3915 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2370.395845, 'AERO': 0.840439, 'cbBTC': 80973.333664}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,339,509 | 2,388.315715 | 52744008 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,841,330 | 1.184308 | 52744008 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,048,439 | 0.029429 | 52744008 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,696,434 | 106.770581 | 52744009 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,362,672 | 0.029355 | 52744008 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 10,127,227 | 0.029371 | 52744008 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,738,081 | 0.000012 | 52744008 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,014,419 | 2,394.308011 | 52744008 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 8,414,020 | 0.000012 | 52744008 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 7,834,707 | 0.000012 | 52744008 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 639 | 7,713,522 | 2,395.077329 | 52744008 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,095,388 | 0.001655 | 52744008 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,451,994 | 2,388.334050 | 52744009 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,290,251 | 0.029441 | 52744008 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,186,396 | 1.000855 | 52744008 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,157,638 | 0.025517 | 52744008 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 415 | 5,069,737 | 2,398.506548 | 52744008 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,773,919 | 0.802399 | 52744008 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,588,514 | 0.000273 | 52744008 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,406,890 | 0.998808 | 52744008 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,374,328 | 2,395.501142 | 52744008 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,040,524 | 33,138.407732 | 52744008 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,002,952 | 1.184582 | 52744008 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,360,839 | 2,822.533196 | 52744008 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,882,948 | 1.141815 | 52744008 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,873,828 | 0.000010 | 52744008 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,829,003 | 0.000012 | 52744008 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,540,478 | 106.804099 | 52744008 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,520,788 | 405.681613 | 52744008 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,221,601 | 1,173,215.805170 | 52744008 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,128,776 | 1.123117 | 52744008 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,878 | 1.199991 | 52744008 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,540 | 1.418010 | 52744008 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,909,020 | 15.803407 | 52744008 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,875,938 | 0.000000 | 52744008 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,797,375 | 0.021509 | 52744008 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,771,521 | 0.000012 | 52744008 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,721,336 | 0.017834 | 52744008 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,655,310 | 2.304324 | 52744008 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,526,479 | 0.916543 | 52744008 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,509,982 | 2,828.370848 | 52744008 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,504,019 | 1.105497 | 52744008 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,461,477 | 2,827.820871 | 52744008 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,611 | 0.825994 | 52744008 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,391,957 | 13,795.671379 | 52744008 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,326,572 | 0.435397 | 52744008 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,322,690 | 0.000000 | 52744008 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,295,414 | 0.004702 | 52744008 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,286,016 | 0.000272 | 52744008 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,249,143 | 62.275669 | 52744008 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,234,166 | 1.131046 | 52744008 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,226,904 | 23.328227 | 52744008 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,222,757 | 0.029351 | 52744008 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,204,743 | 1.105716 | 52744008 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 1,197,127 | 1,009.651963 | 52744008 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/doginme | 10000 | 1,181,852 | 35,769,306.429768 | 52744008 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,172,884 | 2,394.311831 | 52744008 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,159,657 | 1,150,233.361698 | 52744008 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,129,396 | 508,554.536905 | 52744008 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,112,216 | 14.322854 | 52744008 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 3486 ; routes examinées : 73324524 ; candidats optimisés : 456214 ; net attendu > 0 : 356 ; dernier cycle 919.4 ms
- Rejets (moteur) : {'spread_below_threshold': 72264508, 'liquidity_below_min': 598084, 'negative_expected_net': 455858, 'borrow_bound_too_small': 3485, 'cycle_budget_exhausted': 2233}
- Enregistrements de la session : 456214 ; net attendu > 0 : 356 ; simulés (eth_call de la vraie tx) : 10 (ok 0, échec 10) ; étiquettes ghost N+1 : 0/10 positives
- Décisions : {'REJECTED': 456214} ; motifs de rejet : {'below_safety_margin': 334, 'negative_expected_net': 455858, 'p_lower_below_threshold': 260, 'reliability_not_demonstrated': 96, 'simulation_failed': 10, 'stale_data': 52}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52742532 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,627.590133 USDC | 0.324655 USDC | 0.000000 USDC | 0.007868 USDC | 0.316787 USDC (0.2914 €) | — | 1.21 | 0.123 (n=89) | REJECTED | below_safety_margin(316787<525518), p_lower_below_threshold(0.12<0.75) |
| 52742534 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,627.590133 USDC | 0.324655 USDC | 0.000000 USDC | 0.007868 USDC | 0.316787 USDC (0.2914 €) | — | 1.21 | 0.123 (n=89) | REJECTED | below_safety_margin(316787<525518), p_lower_below_threshold(0.12<0.75) |
| 52742532 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 1.105763 WETH | 0.000136 WETH | 0.000000 WETH | 0.000003 WETH | 0.000133 WETH (0.2910 €) | — | 1.20 | 0.123 (n=89) | REJECTED | below_safety_margin(133054947841915<221152665279037), p_lower_below_threshold(0.12<0.75) |
| 52742534 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 1.105763 WETH | 0.000136 WETH | 0.000000 WETH | 0.000003 WETH | 0.000133 WETH (0.2910 €) | — | 1.20 | 0.123 (n=89) | REJECTED | below_safety_margin(133054947841915<221152665279037), p_lower_below_threshold(0.12<0.75) |
| 52742448 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 141.795680 USDC | 0.315193 USDC | 0.000000 USDC | 0.005342 USDC | 0.309851 USDC (0.2851 €) | — | 21.85 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52742532 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,178.935293 USDC | 0.240926 USDC | 0.000000 USDC | 0.007508 USDC | 0.233418 USDC (0.2147 €) | — | 1.07 | 0.123 (n=89) | REJECTED | below_safety_margin(233418<435787), p_lower_below_threshold(0.12<0.75) |
| 52742534 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,178.935293 USDC | 0.240926 USDC | 0.000000 USDC | 0.007508 USDC | 0.233418 USDC (0.2147 €) | — | 1.07 | 0.123 (n=89) | REJECTED | below_safety_margin(233418<435787), p_lower_below_threshold(0.12<0.75) |
| 52742532 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.915653 WETH | 0.000101 WETH | 0.000000 WETH | 0.000003 WETH | 0.000098 WETH (0.2144 €) | — | 1.07 | 0.123 (n=89) | REJECTED | below_safety_margin(98033504696544<183130570773975), p_lower_below_threshold(0.12<0.75) |
| 52742534 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.915653 WETH | 0.000101 WETH | 0.000000 WETH | 0.000003 WETH | 0.000098 WETH (0.2144 €) | — | 1.07 | 0.123 (n=89) | REJECTED | below_safety_margin(98033504696544<183130570773975), p_lower_below_threshold(0.12<0.75) |
| 52742255 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 123.814998 USDC | 0.238334 USDC | 0.000000 USDC | 0.006798 USDC | 0.231536 USDC (0.2130 €) | — | 18.70 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52742202 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.611295 WETH | 0.000081 WETH | 0.000000 WETH | 0.000003 WETH | 0.000078 WETH (0.1709 €) | — | 1.28 | 0.123 (n=89) | REJECTED | below_safety_margin(78164265599601<122258937150799), p_lower_below_threshold(0.12<0.75) |
| 52742202 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,454.331007 USDC | 0.193676 USDC | 0.000000 USDC | 0.007891 USDC | 0.185785 USDC (0.1709 €) | — | 1.28 | 0.123 (n=89) | REJECTED | below_safety_margin(185785<290866), p_lower_below_threshold(0.12<0.75) |
| 52742236 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.065212 WETH | 0.000075 WETH | 0.000000 WETH | 0.000003 WETH | 0.000072 WETH (0.1570 €) | — | 11.01 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52742236 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 154.844888 USDC | 0.177856 USDC | 0.000000 USDC | 0.007525 USDC | 0.170331 USDC (0.1567 €) | — | 11.00 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52742236 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.060658 WETH | 0.000068 WETH | 0.000000 WETH | 0.000003 WETH | 0.000065 WETH (0.1411 €) | — | 10.64 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52742236 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 143.497973 USDC | 0.160321 USDC | 0.000000 USDC | 0.007164 USDC | 0.153157 USDC (0.1409 €) | — | 10.67 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52743151 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,836.598040 USDC | 0.147712 USDC | 0.000000 USDC | 0.007523 USDC | 0.140189 USDC (0.1290 €) | — | 0.76 | 0.123 (n=89) | REJECTED | below_safety_margin(140189<367319), p_lower_below_threshold(0.12<0.75) |
| 52743151 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.771221 WETH | 0.000062 WETH | 0.000000 WETH | 0.000003 WETH | 0.000059 WETH (0.1287 €) | — | 0.76 | 0.123 (n=89) | REJECTED | below_safety_margin(58739251048944<154244103015132), p_lower_below_threshold(0.12<0.75) |
| 52742936 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,749.464866 USDC | 0.144476 USDC | 0.000000 USDC | 0.007521 USDC | 0.136955 USDC (0.1260 €) | — | 0.78 | 0.123 (n=89) | REJECTED | below_safety_margin(136955<349892), p_lower_below_threshold(0.12<0.75) |
| 52742937 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,749.464866 USDC | 0.144476 USDC | 0.000000 USDC | 0.007521 USDC | 0.136955 USDC (0.1260 €) | — | 0.78 | 0.123 (n=89) | REJECTED | below_safety_margin(136955<349892), p_lower_below_threshold(0.12<0.75) |
| 52742936 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.730698 WETH | 0.000060 WETH | 0.000000 WETH | 0.000003 WETH | 0.000057 WETH (0.1256 €) | — | 0.78 | 0.123 (n=89) | REJECTED | below_safety_margin(57324053377808<146139637499554), p_lower_below_threshold(0.12<0.75) |
| 52742937 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.730698 WETH | 0.000060 WETH | 0.000000 WETH | 0.000003 WETH | 0.000057 WETH (0.1256 €) | — | 0.78 | 0.123 (n=89) | REJECTED | below_safety_margin(57324053377808<146139637499554), p_lower_below_threshold(0.12<0.75) |
| 52742912 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,653.852284 USDC | 0.122035 USDC | 0.000000 USDC | 0.007517 USDC | 0.114518 USDC (0.1054 €) | — | 0.69 | 0.123 (n=89) | REJECTED | below_safety_margin(114518<330770), p_lower_below_threshold(0.12<0.75) |
| 52742912 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.694232 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000048 WETH (0.1050 €) | — | 0.69 | 0.123 (n=89) | REJECTED | below_safety_margin(47974627546761<138846464674553), p_lower_below_threshold(0.12<0.75) |
| 52742936 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,515.804120 USDC | 0.118254 USDC | 0.000000 USDC | 0.007521 USDC | 0.110733 USDC (0.1019 €) | — | 0.73 | 0.123 (n=89) | REJECTED | below_safety_margin(110733<303160), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 821 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.116 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
