# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T21:38:22+00:00 ; durée 330.28 min ; blocs 52731965 → 52741868 (9212 vus)

## Connexion
- Requêtes RPC : 109641 ; erreurs : 10 ; latence p50/p95 : 152.7/1,942.4 ms
- Rafraîchissements d'état : 9212 ; âge des données au dernier bloc : 3.18 s ; changements de frais LP observés (pools à frais dynamiques) : 13171
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 28774 ; cycles déclenchés par événement : 1404 ; avance médiane sur le rafraîchissement multicall : 1,673 ms
- Gaz : base fee 0.005515 gwei ; prix ETH (pool le plus profond) : 2,378.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21110 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3916 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2411.894998, 'AERO': 0.849168, 'cbBTC': 81312.167025}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,906,841 | 2,378.210820 | 52741869 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,754,855 | 1.189587 | 52741869 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,979,016 | 0.029322 | 52741869 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,579,112 | 107.372615 | 52741869 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,329,987 | 0.029393 | 52741869 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2695 | 10,097,102 | 0.029387 | 52741869 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,734,437 | 0.000012 | 52741869 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,035,869 | 2,372.138031 | 52741869 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 7,832,876 | 0.000012 | 52741869 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,066,113 | 0.001640 | 52741869 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 1414 | 6,875,511 | 2,372.404336 | 52741869 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 6,537,139 | 0.000012 | 52741869 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,365,285 | 2,377.945104 | 52741869 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,274,640 | 0.029311 | 52741869 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,164,453 | 1.000855 | 52741869 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,146,077 | 0.025517 | 52741869 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,753,718 | 0.802398 | 52741869 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,569,098 | 0.000273 | 52741869 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,404,223 | 0.998808 | 52741869 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,348,624 | 2,371.541639 | 52741869 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,053,643 | 32,646.249470 | 52741869 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,349,075 | 2,822.442307 | 52741869 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 565 | 3,046,751 | 2,377.579558 | 52741869 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,870,744 | 1.141813 | 52741869 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,827,777 | 0.000012 | 52741869 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,731,068 | 1.181239 | 52741869 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,663,181 | 409.167063 | 52741869 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,547,512 | 0.000010 | 52741869 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,521,523 | 107.391418 | 52741869 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,207,604 | 1,178,108.382435 | 52741869 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,129,059 | 1.123343 | 52741869 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,582 | 1.200159 | 52741869 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,540 | 1.418010 | 52741869 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,846,981 | 15.845897 | 52741869 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,845,318 | 0.000000 | 52741869 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,797,296 | 0.021508 | 52741869 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,770,740 | 0.000012 | 52741869 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,704,852 | 0.017548 | 52741869 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,648,498 | 2.303757 | 52741869 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,520,017 | 0.916544 | 52741869 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,505,534 | 13,930.543093 | 52741869 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,503,432 | 2,834.777085 | 52741869 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,497,654 | 1.105495 | 52741869 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 1,463,607 | 1,015.559630 | 52741869 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,401 | 0.826229 | 52741869 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3008 | 1,455,380 | 2,835.427637 | 52741869 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,320,326 | 0.000000 | 52741869 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,315,676 | 0.435103 | 52741869 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,289,847 | 0.004702 | 52741869 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,280,574 | 0.000271 | 52741869 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,249,201 | 62.269945 | 52741869 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,241,470 | 1.130902 | 52741869 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/cbBTC | 3000 | 1,219,801 | 0.029406 | 52741869 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,218,154 | 23.365780 | 52741869 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,199,646 | 1.105716 | 52741869 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,176,354 | 35,814,934.488960 | 52741869 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,165,208 | 2,371.946917 | 52741869 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,154,749 | 1,150,234.390163 | 52741869 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,120,379 | 513,801.475547 | 52741869 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,113,509 | 14.281059 | 52741869 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 10614 ; routes examinées : 224061540 ; candidats optimisés : 1525315 ; net attendu > 0 : 936 ; dernier cycle 1202.5 ms
- Rejets (moteur) : {'spread_below_threshold': 220537444, 'liquidity_below_min': 1715268, 'negative_expected_net': 1524379, 'pool_quarantined': 249022, 'cycle_budget_exhausted': 23671, 'borrow_bound_too_small': 10606}
- Enregistrements de la session : 1525312 ; net attendu > 0 : 936 ; simulés (eth_call de la vraie tx) : 94 (ok 41, échec 53) ; étiquettes ghost N+1 : 16/69 positives
- Décisions : {'REJECTED': 1525312} ; motifs de rejet : {'below_safety_margin': 473, 'negative_expected_net': 1524376, 'p_lower_below_threshold': 652, 'price_impact': 68, 'reliability_not_demonstrated': 284, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 1, 'simulation_failed': 53, 'stale_data': 126}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52732232 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 264.379140 USDC | 0.953137 USDC | 0.000000 USDC | 0.005417 USDC | 0.947720 USDC (0.8719 €) | — | 35.85 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52739066 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 5,817.804447 USDC | 0.920842 USDC | 0.000000 USDC | 0.005416 USDC | 0.915426 USDC (0.8422 €) | — | 1.57 | 0.060 (n=5) | REJECTED | below_safety_margin(915426<1163560), reliability_not_demonstrated |
| 52739066 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.071462 cbBTC | 0.000011 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000011 cbBTC (0.8413 €) | — | 1.57 | 0.060 (n=5) | REJECTED | below_safety_margin(1124<1429), reliability_not_demonstrated |
| 52741693 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.585526 WETH | 0.000329 WETH | 0.000000 WETH | 0.000003 WETH | 0.000327 WETH (0.7198 €) | 0.000327 WETH | 5.58 | 0.114 (n=13) | REJECTED | reliability_not_demonstrated |
| 52741693 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 1,396.717391 USDC | 0.786124 USDC | 0.000000 USDC | 0.006133 USDC | 0.779991 USDC (0.7176 €) | — | 5.58 | 0.114 (n=13) | REJECTED | reliability_not_demonstrated |
| 52741693 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.235327 WETH | 0.000248 WETH | 0.000000 WETH | 0.000003 WETH | 0.000245 WETH (0.5399 €) | 0.000245 WETH | 10.42 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52741693 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 561.448637 USDC | 0.592298 USDC | 0.000000 USDC | 0.007596 USDC | 0.584702 USDC (0.5379 €) | — | 10.41 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52741694 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.390231 WETH | 0.000164 WETH | 0.000000 WETH | 0.000003 WETH | 0.000161 WETH (0.3547 €) | 0.000161 WETH | 4.13 | 0.124 (n=75) | REJECTED | stale_data(5424ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741694 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011320 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3547 €) | — | 4.19 | 0.124 (n=75) | REJECTED | stale_data(5415ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741694 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 918.499648 USDC | 0.391601 USDC | 0.000000 USDC | 0.007778 USDC | 0.383823 USDC (0.3531 €) | — | 4.18 | 0.124 (n=75) | REJECTED | stale_data(5432ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52739066 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.056698 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3234 €) | — | 0.76 | 0.060 (n=5) | REJECTED | below_safety_margin(432<1133), reliability_not_demonstrated |
| 52739066 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 4,835.644447 USDC | 0.356364 USDC | 0.000000 USDC | 0.005416 USDC | 0.350948 USDC (0.3229 €) | — | 0.73 | 0.060 (n=5) | REJECTED | below_safety_margin(350948<967128), reliability_not_demonstrated |
| 52741694 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.281407 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.3011 €) | 0.000137 WETH | 4.86 | 0.124 (n=75) | REJECTED | stale_data(5278ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741694 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.008048 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3008 €) | — | 4.99 | 0.124 (n=75) | REJECTED | stale_data(5294ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741694 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.010431 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3000 €) | — | 3.84 | 0.124 (n=75) | REJECTED | stale_data(5558ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741694 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.372769 WETH | 0.000139 WETH | 0.000000 WETH | 0.000003 WETH | 0.000136 WETH (0.3000 €) | 0.000136 WETH | 3.65 | 0.124 (n=75) | REJECTED | stale_data(5541ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741694 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 669.712502 USDC | 0.333420 USDC | 0.000000 USDC | 0.007405 USDC | 0.326015 USDC (0.2999 €) | — | 4.87 | 0.124 (n=75) | REJECTED | stale_data(5286ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741694 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 848.830014 USDC | 0.332682 USDC | 0.000000 USDC | 0.007778 USDC | 0.324904 USDC (0.2989 €) | — | 3.83 | 0.124 (n=75) | REJECTED | stale_data(5549ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741694 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.010039 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2671 €) | — | 3.56 | 0.124 (n=75) | REJECTED | stale_data(5652ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741694 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.366024 WETH | 0.000124 WETH | 0.000000 WETH | 0.000003 WETH | 0.000121 WETH (0.2664 €) | — | 3.30 | 0.124 (n=75) | REJECTED | stale_data(5643ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741694 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 830.708541 USDC | 0.296803 USDC | 0.000000 USDC | 0.007778 USDC | 0.289025 USDC (0.2659 €) | — | 3.48 | 0.124 (n=75) | REJECTED | stale_data(5661ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52741693 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.177788 WETH | 0.000103 WETH | 0.000000 WETH | 0.000003 WETH | 0.000100 WETH (0.2197 €) | 0.000100 WETH | 5.61 | 0.189 (n=41) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 52741693 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 423.273637 USDC | 0.245511 USDC | 0.000000 USDC | 0.007596 USDC | 0.237915 USDC (0.2189 €) | — | 5.62 | 0.189 (n=41) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 52741693 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.075368 WETH | 0.000096 WETH | 0.000000 WETH | 0.000003 WETH | 0.000093 WETH (0.2055 €) | — | 12.38 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52741693 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 179.948765 USDC | 0.229722 USDC | 0.000000 USDC | 0.007231 USDC | 0.222491 USDC (0.2047 €) | — | 12.36 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 811 ; taux observé 0.132 ; borne inférieure crédible (0.9) 0.117 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
