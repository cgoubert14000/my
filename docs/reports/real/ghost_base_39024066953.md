# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T10:58:47+00:00 ; durée 39.77 min ; blocs 52721493 → 52722687 (1128 vus)

## Connexion
- Requêtes RPC : 15039 ; erreurs : 0 ; latence p50/p95 : 467.2/1,397.9 ms
- Rafraîchissements d'état : 1128 ; âge des données au dernier bloc : 4.12 s ; changements de frais LP observés (pools à frais dynamiques) : 1046
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 15196 ; cycles déclenchés par événement : 902 ; avance médiane sur le rafraîchissement multicall : 1,201 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,430.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 577 pools, 329 jetons, 21508 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3914 (énumérés 394, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 2 → gardés 577 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2430.106481, 'AERO': 0.895375, 'cbBTC': 81495.8779}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,783,776 | 2,430.885999 | 52722688 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,408,816 | 1.107715 | 52722688 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,291,972 | 0.029879 | 52722688 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,092,824 | 104.834801 | 52722688 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2520 | 14,216,656 | 0.029821 | 52722688 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,467,444 | 0.029806 | 52722688 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,756,306 | 0.000012 | 52722688 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,133,564 | 2,436.895790 | 52722688 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 8,234,604 | 0.000012 | 52722688 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,864,740 | 0.000012 | 52722688 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,391,263 | 2,435.951661 | 52722688 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,162,675 | 0.001678 | 52722688 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,592,845 | 1.115576 | 52722688 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,436,432 | 0.025270 | 52722688 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,424,409 | 2,434.938114 | 52722688 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,347,488 | 0.029868 | 52722688 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,278,840 | 1.000855 | 52722688 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,858,875 | 0.802398 | 52722688 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,699,225 | 0.000276 | 52722688 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,422,937 | 2,435.919511 | 52722688 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,417,741 | 0.998803 | 52722688 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,064,182 | 33,931.764930 | 52722688 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,513,391 | 2,718.025973 | 52722688 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,929,199 | 1.141834 | 52722688 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,850,724 | 1,023.095509 | 52722688 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,836,773 | 0.000012 | 52722688 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,705,404 | 0.000011 | 52722688 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,678,301 | 402.198941 | 52722688 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,610,032 | 104.850026 | 52722688 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,249,915 | 1,185,014.580488 | 52722688 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,126,302 | 1.123536 | 52722688 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,805 | 1.197614 | 52722688 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,026,647 | 2,440.256518 | 52722688 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52722688 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,991,978 | 15.630065 | 52722688 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,831,343 | 0.022356 | 52722688 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,820,326 | 0.000000 | 52722688 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,776,863 | 0.000012 | 52722688 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,755,010 | 0.018445 | 52722688 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,681,862 | 2.306988 | 52722688 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,668,070 | 13,475.874531 | 52722688 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,561,597 | 2,695.055305 | 52722688 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,553,671 | 0.916549 | 52722688 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,539,586 | 2,697.508539 | 52722688 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,522,807 | 1.105495 | 52722688 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,550 | 0.826343 | 52722688 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,368,336 | 0.004872 | 52722688 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,365,115 | 0.000000 | 52722688 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,326,314 | 0.435854 | 52722688 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,316,995 | 0.000274 | 52722688 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,255,088 | 23.293965 | 52722688 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299956 | 52722688 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,239,971 | 1.131652 | 52722688 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,231,207 | 1.105714 | 52722688 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,230,347 | 0.029801 | 52722688 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,207,220 | 35,368,823.910888 | 52722688 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,202,006 | 2,436.898934 | 52722688 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,187,096 | 1,137,151.572454 | 52722688 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,152,264 | 505,172.671196 | 52722688 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,124,352 | 13.935484 | 52722688 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 2029 ; routes examinées : 43639732 ; candidats optimisés : 273388 ; net attendu > 0 : 20 ; dernier cycle 359.4 ms
- Rejets (moteur) : {'spread_below_threshold': 42910307, 'liquidity_below_min': 408216, 'negative_expected_net': 273368, 'unquotable': 45163, 'borrow_bound_too_small': 2029, 'cycle_budget_exhausted': 629}
- Enregistrements de la session : 273388 ; net attendu > 0 : 20 ; simulés (eth_call de la vraie tx) : 3 (ok 0, échec 3) ; étiquettes ghost N+1 : 3/3 positives
- Décisions : {'REJECTED': 273388} ; motifs de rejet : {'below_safety_margin': 16, 'negative_expected_net': 273368, 'p_lower_below_threshold': 12, 'reliability_not_demonstrated': 8, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52722663 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002568 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0427 €) | — | 2.22 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.083058 WETH | 0.000021 WETH | 0.000000 WETH | 0.000002 WETH | 0.000019 WETH (0.0421 €) | — | 2.26 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52722663 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002454 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0374 €) | — | 2.04 | 0.108 (n=78) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52722663 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 185.995824 USDC | 0.047888 USDC | 0.000000 USDC | 0.007307 USDC | 0.040581 USDC (0.0373 €) | — | 2.18 | 0.108 (n=78) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.083058 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0369 €) | — | 1.99 | 0.108 (n=78) | REJECTED | below_safety_margin(16488156450115<16611681200461), p_lower_below_threshold(0.11<0.75) |
| 52722663 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 170.111193 USDC | 0.032966 USDC | 0.000000 USDC | 0.007676 USDC | 0.025290 USDC (0.0233 €) | — | 1.49 | 0.108 (n=78) | REJECTED | below_safety_margin(25290<34022), p_lower_below_threshold(0.11<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.066625 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0232 €) | — | 1.56 | 0.108 (n=78) | REJECTED | below_safety_margin(10381632421486<13324907928011), p_lower_below_threshold(0.11<0.75) |
| 52722663 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001950 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0232 €) | — | 1.59 | 0.108 (n=78) | REJECTED | below_safety_margin(31<38), p_lower_below_threshold(0.11<0.75) |
| 52722663 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.000850 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.47 | 0.297 (n=50) | REJECTED | below_safety_margin(4<16), p_lower_below_threshold(0.30<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH | 0.033420 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0028 €) | — | 0.37 | 0.297 (n=50) | REJECTED | below_safety_margin(1240888153480<6683910078116), p_lower_below_threshold(0.30<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→WETH | 0.033420 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.32 | 0.297 (n=50) | REJECTED | below_safety_margin(1063662712362<6683910078116), p_lower_below_threshold(0.30<0.75) |
| 52722663 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.000836 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0022 €) | — | 0.36 | 0.108 (n=78) | REJECTED | below_safety_margin(3<16), p_lower_below_threshold(0.11<0.75) |
| 52722663 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.000850 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0022 €) | — | 0.35 | 0.297 (n=50) | REJECTED | below_safety_margin(3<16), p_lower_below_threshold(0.30<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→WETH | 0.026324 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 0.36 | 0.108 (n=78) | REJECTED | below_safety_margin(959946402556<5264717153801), p_lower_below_threshold(0.11<0.75) |
| 52722465 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 22.461917 USDC | 0.007673 USDC | 0.000000 USDC | 0.005458 USDC | 0.002215 USDC (0.0020 €) | — | 0.99 | 0.000 (n=19) | REJECTED | below_safety_margin(2215<4492), reliability_not_demonstrated |
| 52722465 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 22.461917 USDC | 0.007673 USDC | 0.000000 USDC | 0.005458 USDC | 0.002215 USDC (0.0020 €) | — | 0.99 | 0.000 (n=19) | REJECTED | below_safety_margin(2215<4492), reliability_not_demonstrated |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.022720 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0008 €) | — | 0.16 | 0.000 (n=19) | REJECTED | below_safety_margin(356488388203<4544034182921), reliability_not_demonstrated |
| 52722663 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000850 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.12 | 0.000 (n=19) | REJECTED | below_safety_margin(1<16), reliability_not_demonstrated |
| 52721938 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 16.356001 USDC | 0.005913 USDC | 0.000000 USDC | 0.005457 USDC | 0.000456 USDC (0.0004 €) | — | 0.28 | 0.000 (n=19) | REJECTED | below_safety_margin(456<3271), reliability_not_demonstrated |
| 52721938 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 16.356001 USDC | 0.005913 USDC | 0.000000 USDC | 0.005457 USDC | 0.000456 USDC (0.0004 €) | — | 0.28 | 0.000 (n=19) | REJECTED | below_safety_margin(456<3271), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 724 ; taux observé 0.124 ; borne inférieure crédible (0.9) 0.109 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
