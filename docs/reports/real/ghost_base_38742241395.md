# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T16:40:09+00:00 ; durée 191.55 min ; blocs 52640781 → 52646527 (4975 vus)

## Connexion
- Requêtes RPC : 64952 ; erreurs : 363 ; latence p50/p95 : 239.0/2,382.3 ms
- Rafraîchissements d'état : 4975 ; âge des données au dernier bloc : 3.03 s ; changements de frais LP observés (pools à frais dynamiques) : 24146
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005120 gwei ; prix ETH (pool le plus profond) : 2,428.37 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 570 pools, 326 jetons, 21328 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 152, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3864 (énumérés 389, par paires 0), mesurés 572, sous le plancher de 10000.0 $ : 2 → gardés 570 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2346.001193, 'AERO': 0.837627, 'cbBTC': 80168.530844}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,926,004 | 2,428.368373 | 52646527 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,210,518 | 1.126000 | 52646527 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,248,774 | 0.029584 | 52646527 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,704,836 | 98.189090 | 52646527 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,635,654 | 0.029569 | 52646527 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,525,031 | 0.029554 | 52646527 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,749,310 | 0.000012 | 52646527 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,083,958 | 2,426.176676 | 52646527 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,980,035 | 0.000012 | 52646527 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,220,515 | 0.001676 | 52646527 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 7,052,296 | 2,425.255441 | 52646527 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 6,803,885 | 0.000012 | 52646527 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,906,904 | 2,428.602931 | 52646527 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,801,846 | 1.122170 | 52646527 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,351,091 | 0.025943 | 52646527 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,337,807 | 0.029584 | 52646527 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,711,381 | 0.000278 | 52646527 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,701,288 | 0.802387 | 52646527 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,330,944 | 0.997987 | 52646527 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,321,379 | 2,425.203117 | 52646527 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,987,429 | 35,177.636318 | 52646527 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,487,750 | 2,737.108403 | 52646527 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,854,925 | 0.000012 | 52646527 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,661,586 | 98.210745 | 52646527 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,433,762 | 0.000011 | 52646527 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,358,219 | 1.141818 | 52646527 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 2,348,877 | 1,008.078689 | 52646527 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,311,542 | 403.089331 | 52646527 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,241,884 | 1,191,047.664842 | 52646527 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,377 | 1.196132 | 52646527 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,087,162 | 2,430.077498 | 52646527 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,062,487 | 0.000000 | 52646527 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,019,578 | 15.622111 | 52646527 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52646527 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,831,061 | 0.022942 | 52646527 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,793,897 | 0.019099 | 52646527 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,149 | 0.000012 | 52646527 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,743,754 | 13,622.896690 | 52646527 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,718,467 | 2.306977 | 52646527 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,539,743 | 2,728.167395 | 52646527 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,501,437 | 1.105494 | 52646527 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,823 | 0.831292 | 52646527 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,380,590 | 2,727.563510 | 52646527 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,369,955 | 0.000000 | 52646527 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,343,866 | 23.138756 | 52646527 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,320,463 | 0.000278 | 52646527 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,290,095 | 0.004590 | 52646527 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,248,950 | 62.294927 | 52646527 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,239,397 | 0.916559 | 52646527 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,236,496 | 1.131592 | 52646527 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,229,942 | 1.120336 | 52646527 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,212,987 | 2,426.328116 | 52646527 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,208,996 | 34,982,065.471673 | 52646527 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,203,671 | 1.105591 | 52646527 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,166,745 | 1,174,700.778356 | 52646527 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | WETH/cbBTC | 3000 | 1,162,593 | 0.029550 | 52646527 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,160,619 | 494,391.959510 | 52646527 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,153,821 | 77,077.078976 | 52646527 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,125,586 | 13.890459 | 52646527 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,118,817 | 50.347206 | 52646527 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 4974 ; routes examinées : 106085472 ; candidats optimisés : 733129 ; net attendu > 0 : 1581 ; dernier cycle 593.1 ms
- Rejets (moteur) : {'spread_below_threshold': 104016442, 'liquidity_below_min': 1051566, 'negative_expected_net': 731548, 'pool_quarantined': 156410, 'borrow_bound_too_small': 109868, 'unquotable': 11126, 'cycle_budget_exhausted': 6931}
- Enregistrements de la session : 733129 ; net attendu > 0 : 1581 ; simulés (eth_call de la vraie tx) : 117 (ok 89, échec 28) ; étiquettes ghost N+1 : 6/95 positives
- Décisions : {'REJECTED': 733129} ; motifs de rejet : {'below_safety_margin': 848, 'negative_expected_net': 731548, 'p_lower_below_threshold': 605, 'price_impact': 98, 'reliability_not_demonstrated': 976, 'simulation_failed': 28, 'stale_data': 235}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 442.062489 USDC | 0.298836 USDC | 0.000000 USDC | 0.008229 USDC | 0.290607 USDC (0.2674 €) | — | 6.57 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.186091 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000122 WETH (0.2667 €) | 0.000122 WETH | 6.57 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52643960 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 2,414.723624 USDC | 0.292685 USDC | 0.000000 USDC | 0.007510 USDC | 0.285175 USDC (0.2624 €) | — | 1.18 | 0.241 (n=29) | REJECTED | below_safety_margin(285175<482944), reliability_not_demonstrated |
| 52643960 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.998317 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2622 €) | — | 1.18 | 0.241 (n=29) | REJECTED | below_safety_margin(117845714349323<199663382839724), reliability_not_demonstrated |
| 52643631 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 402.676128 USDC | 0.291853 USDC | 0.000000 USDC | 0.007764 USDC | 0.284089 USDC (0.2614 €) | — | 7.06 | 0.324 (n=17) | REJECTED | stale_data(4844ms>4000.0), reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.167552 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2605 €) | 0.000118 WETH | 7.05 | 0.324 (n=17) | REJECTED | stale_data(4838ms>4000.0), reliability_not_demonstrated |
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 420.852464 USDC | 0.288482 USDC | 0.000000 USDC | 0.007844 USDC | 0.280638 USDC (0.2582 €) | — | 6.67 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.177158 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2575 €) | 0.000118 WETH | 6.66 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52643631 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 448.930237 USDC | 0.265334 USDC | 0.000000 USDC | 0.007399 USDC | 0.257935 USDC (0.2373 €) | — | 5.75 | 0.324 (n=17) | REJECTED | stale_data(4899ms>4000.0), reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.186788 WETH | 0.000110 WETH | 0.000000 WETH | 0.000003 WETH | 0.000107 WETH (0.2366 €) | 0.000107 WETH | 5.75 | 0.324 (n=17) | REJECTED | stale_data(4893ms>4000.0), reliability_not_demonstrated |
| 52643631 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.009293 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2117 €) | — | 3.03 | 0.324 (n=17) | REJECTED | stale_data(5421ms>4000.0), reliability_not_demonstrated |
| 52643631 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.009293 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2117 €) | — | 3.03 | 0.324 (n=17) | REJECTED | stale_data(5453ms>4000.0), reliability_not_demonstrated |
| 52643631 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 796.521943 USDC | 0.238242 USDC | 0.000000 USDC | 0.008129 USDC | 0.230113 USDC (0.2117 €) | — | 2.89 | 0.251 (n=28) | REJECTED | stale_data(5446ms>4000.0), reliability_not_demonstrated |
| 52643631 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 796.568874 USDC | 0.238083 USDC | 0.000000 USDC | 0.008129 USDC | 0.229954 USDC (0.2116 €) | — | 2.89 | 0.251 (n=28) | REJECTED | stale_data(5434ms>4000.0), reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.322276 WETH | 0.000099 WETH | 0.000000 WETH | 0.000003 WETH | 0.000096 WETH (0.2113 €) | 0.000096 WETH | 2.97 | 0.251 (n=28) | REJECTED | stale_data(5440ms>4000.0), reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.310416 WETH | 0.000099 WETH | 0.000000 WETH | 0.000003 WETH | 0.000096 WETH (0.2107 €) | — | 3.08 | 0.324 (n=17) | REJECTED | stale_data(5427ms>4000.0), reliability_not_demonstrated |
| 52643631 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 400.018425 USDC | 0.223531 USDC | 0.000000 USDC | 0.007399 USDC | 0.216132 USDC (0.1988 €) | — | 5.40 | 0.152 (n=45) | REJECTED | stale_data(4979ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 52643631 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.166652 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000090 WETH (0.1982 €) | — | 5.40 | 0.152 (n=45) | REJECTED | stale_data(4973ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 52643631 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 403.086292 USDC | 0.215122 USDC | 0.000000 USDC | 0.007399 USDC | 0.207723 USDC (0.1911 €) | — | 5.15 | 0.324 (n=17) | REJECTED | stale_data(5023ms>4000.0), reliability_not_demonstrated |
| 52642968 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→BRETT→[uniswap_v3]→WETH | 0.021903 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1910 €) | 0.000087 WETH | 39.89 | 0.102 (n=3) | REJECTED | reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.167680 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000086 WETH (0.1905 €) | — | 5.15 | 0.324 (n=17) | REJECTED | stale_data(5018ms>4000.0), reliability_not_demonstrated |
| 52642968 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[uniswap_v3]→WETH | 0.021775 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1903 €) | 0.000087 WETH | 40.00 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52642968 | WETH→[uniswap_v3]→AERO→[aerodrome]→BRETT→[uniswap_v3]→WETH | 0.020798 WETH | 0.000082 WETH | 0.000000 WETH | 0.000003 WETH | 0.000079 WETH (0.1724 €) | 0.000079 WETH | 37.92 | 0.102 (n=3) | REJECTED | reliability_not_demonstrated |
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 307.929676 USDC | 0.182750 USDC | 0.000000 USDC | 0.007844 USDC | 0.174906 USDC (0.1609 €) | — | 5.68 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52642035 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.129817 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1606 €) | 0.000074 WETH | 5.67 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 373 ; taux observé 0.155 ; borne inférieure crédible (0.9) 0.133 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 13.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
