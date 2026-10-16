# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T11:38:24+00:00 ; durée 321.0 min ; blocs 52671044 → 52680671 (8922 vus)

## Connexion
- Requêtes RPC : 115765 ; erreurs : 510 ; latence p50/p95 : 192.4/1,824.7 ms
- Rafraîchissements d'état : 8923 ; âge des données au dernier bloc : 1.5 s ; changements de frais LP observés (pools à frais dynamiques) : 22414
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 93978 ; cycles déclenchés par événement : 4772 ; avance médiane sur le rafraîchissement multicall : 1,289 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,483.74 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 327 jetons, 21788 routes
- Par DEX : uniswap_v3 137, aerodrome 236 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 392, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 3 → gardés 576 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2445.329592, 'AERO': 0.931569, 'cbBTC': 81962.021553}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52680799; aerodrome:fBOMB/cbBTC@0x3d36Cf: simulation failed ×5 (model/chain mismatch) — until block 52680798

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,437,458 | 2,483.742249 | 52680671 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 47,049,565 | 1.088206 | 52680671 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,766,262 | 0.030000 | 52680671 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,775,845 | 100.372437 | 52680671 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,690,728 | 0.030060 | 52680671 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,653,165 | 0.030047 | 52680671 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,784,614 | 0.000012 | 52680671 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,227,907 | 2,478.357562 | 52680671 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 8,148,977 | 0.000012 | 52680671 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 743 | 7,796,457 | 2,477.476092 | 52680671 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/AERO | 10000 | 7,516,777 | 1.084050 | 52680671 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,304,927 | 0.001686 | 52680671 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 6,611,401 | 0.000012 | 52680671 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,507,118 | 0.024788 | 52680671 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,486,606 | 2,484.060735 | 52680671 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,481,275 | 0.029990 | 52680671 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,307,327 | 1.000855 | 52680671 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,964,495 | 0.802398 | 52680671 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,832,894 | 0.000281 | 52680671 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,397,976 | 0.998889 | 52680671 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,371,268 | 2,477.373558 | 52680671 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,120,104 | 34,468.323515 | 52680671 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 436 | 4,108,599 | 2,481.159120 | 52680671 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,589,157 | 2,678.014370 | 52680671 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,083,240 | 1.141841 | 52680671 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 2,927,598 | 997.949421 | 52680671 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,860,084 | 0.000012 | 52680671 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,711,315 | 100.411545 | 52680671 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,690,658 | 0.000011 | 52680671 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,373,318 | 399.819737 | 52680671 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,329,536 | 1,153,986.022708 | 52680671 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,139,712 | 0.000000 | 52680671 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,736 | 1.195936 | 52680671 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,461 | 1.403757 | 52680671 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,867,731 | 0.023310 | 52680671 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,848,909 | 13,330.882619 | 52680671 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,840,808 | 15.116900 | 52680671 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,786,798 | 0.000012 | 52680671 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,784,338 | 0.018938 | 52680671 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,714,822 | 2.312441 | 52680671 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,590,799 | 2,697.084224 | 52680671 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,543,863 | 0.916551 | 52680671 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,535,714 | 1.105492 | 52680671 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3016 | 1,507,998 | 2,696.834117 | 52680671 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,120 | 0.825820 | 52680671 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,393,780 | 0.000000 | 52680671 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,391,378 | 1.125455 | 52680671 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,384,810 | 0.004814 | 52680671 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,356,579 | 0.000281 | 52680671 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,353,997 | 23.275360 | 52680671 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,310,034 | 0.437134 | 52680671 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | USDC/SEND | 3000 | 1,250,232 | 62.167285 | 52680671 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,232,516 | 1.105591 | 52680671 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,230,966 | 0.030036 | 52680671 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,228,655 | 35,677,559.136533 | 52680671 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,223,940 | 0.886678 | 52680671 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,223,214 | 1,118,042.428358 | 52680671 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,220,509 | 2,478.424507 | 52680671 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,185,516 | 496,085.125904 | 52680671 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,150,551 | 81,130.070475 | 52680671 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 13694 ; routes examinées : 298364872 ; candidats optimisés : 1541690 ; net attendu > 0 : 614 ; dernier cycle 605.2 ms
- Rejets (moteur) : {'spread_below_threshold': 293483904, 'liquidity_below_min': 2464141, 'negative_expected_net': 1541076, 'pool_quarantined': 856058, 'borrow_bound_too_small': 13685, 'cycle_budget_exhausted': 5394}
- Enregistrements de la session : 1541690 ; net attendu > 0 : 614 ; simulés (eth_call de la vraie tx) : 119 (ok 32, échec 87) ; étiquettes ghost N+1 : 3/68 positives
- Décisions : {'REJECTED': 1541690} ; motifs de rejet : {'below_safety_margin': 391, 'negative_expected_net': 1541076, 'p_lower_below_threshold': 321, 'price_impact': 127, 'reliability_not_demonstrated': 293, 'simulation_failed': 87, 'stale_data': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52671989 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.028664 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1011 €) | — | 0.47 | 0.001 (n=10) | REJECTED | below_safety_margin(134<573), reliability_not_demonstrated |
| 52671989 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.051068 WETH | 0.000047 WETH | 0.000000 WETH | 0.000002 WETH | 0.000045 WETH (0.1011 €) | — | 0.43 | 0.001 (n=10) | REJECTED | below_safety_margin(44910967314113<210213569031069), reliability_not_demonstrated |
| 52677220 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002693 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0854 €) | — | 4.20 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 221.202314 USDC | 0.099215 USDC | 0.000000 USDC | 0.007377 USDC | 0.091838 USDC (0.0845 €) | — | 4.15 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002694 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0839 €) | — | 4.12 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 219.481750 USDC | 0.098552 USDC | 0.000000 USDC | 0.007377 USDC | 0.091175 USDC (0.0839 €) | — | 4.15 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002694 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0832 €) | — | 4.08 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 222.439475 USDC | 0.097929 USDC | 0.000000 USDC | 0.007749 USDC | 0.090180 USDC (0.0830 €) | — | 4.05 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002359 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0748 €) | — | 4.20 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 187.810486 USDC | 0.087479 USDC | 0.000000 USDC | 0.007377 USDC | 0.080102 USDC (0.0737 €) | — | 4.27 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002015 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0643 €) | — | 4.22 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 174.775027 USDC | 0.076985 USDC | 0.000000 USDC | 0.007749 USDC | 0.069236 USDC (0.0637 €) | — | 3.96 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52679930 | USDC→[uniswap_v3]→AAVE→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 171.898250 USDC | 0.071259 USDC | 0.000000 USDC | 0.007588 USDC | 0.063671 USDC (0.0586 €) | — | 3.70 | 0.117 (n=58) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52679930 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AAVE→[aerodrome_slipstream]→WETH | 0.069453 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0584 €) | 0.000026 WETH | 3.69 | 0.117 (n=58) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52679930 | USDC→[uniswap_v3]→AAVE→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 156.030259 USDC | 0.063710 USDC | 0.000000 USDC | 0.007588 USDC | 0.056122 USDC (0.0516 €) | — | 3.60 | 0.223 (n=24) | REJECTED | reliability_not_demonstrated |
| 52679930 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AAVE→[aerodrome_slipstream]→WETH | 0.063070 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0515 €) | 0.000023 WETH | 3.58 | 0.223 (n=24) | REJECTED | reliability_not_demonstrated |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDC | 146.123767 USDC | 0.045955 USDC | 0.000000 USDC | 0.005174 USDC | 0.040781 USDC (0.0375 €) | — | 2.79 | 0.143 (n=6) | REJECTED | reliability_not_demonstrated |
| 52677221 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDC | 146.123767 USDC | 0.045955 USDC | 0.000000 USDC | 0.005174 USDC | 0.040781 USDC (0.0375 €) | — | 2.79 | 0.143 (n=6) | REJECTED | reliability_not_demonstrated |
| 52679928 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 156.397048 USDC | 0.041581 USDC | 0.000000 USDC | 0.007434 USDC | 0.034147 USDC (0.0314 €) | — | 2.18 | 0.258 (n=37) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 52679928 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.063322 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0313 €) | 0.000014 WETH | 2.17 | 0.258 (n=37) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 52679928 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 161.162358 USDC | 0.038692 USDC | 0.000000 USDC | 0.007434 USDC | 0.031258 USDC (0.0288 €) | — | 1.94 | 0.086 (n=51) | REJECTED | below_safety_margin(31258<32232), p_lower_below_threshold(0.09<0.75) |
| 52679928 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.064954 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0287 €) | — | 1.94 | 0.086 (n=51) | REJECTED | below_safety_margin(12600701074907<12990734768047), p_lower_below_threshold(0.09<0.75) |
| 52671989 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007406 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0264 €) | — | 0.47 | 0.072 (n=50) | REJECTED | below_safety_margin(35<148), p_lower_below_threshold(0.07<0.75) |
| 52671989 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 665.496868 USDC | 0.036012 USDC | 0.000000 USDC | 0.007407 USDC | 0.028605 USDC (0.0263 €) | — | 0.43 | 0.072 (n=50) | REJECTED | below_safety_margin(28605<133099), p_lower_below_threshold(0.07<0.75) |
| 52671989 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.232200 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0262 €) | — | 0.50 | 0.072 (n=50) | REJECTED | below_safety_margin(11661461449146<46439988969480), p_lower_below_threshold(0.07<0.75) |

## Fiabilité et décision
- Observations ghost : 511 ; taux observé 0.119 ; borne inférieure crédible (0.9) 0.102 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
