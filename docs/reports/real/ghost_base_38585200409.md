# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T15:13:04+00:00 ; durée 9.13 min ; blocs 52600436 → 52600711 (139 vus)

## Connexion
- Requêtes RPC : 2249 ; erreurs : 0 ; latence p50/p95 : 563.0/3,510.0 ms
- Rafraîchissements d'état : 139 ; âge des données au dernier bloc : 15.26 s ; changements de frais LP observés (pools à frais dynamiques) : 676
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2456 ; cycles déclenchés par événement : 66 ; avance médiane sur le rafraîchissement multicall : 977 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,425.33 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 140, aerodrome 235 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3920 (énumérés 391, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 5 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2425.371992, 'AERO': 0.862121, 'cbBTC': 81739.3593}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52600872; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52600872

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,051,022 | 2,425.333993 | 52600715 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,325,653 | 1.165140 | 52600715 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,833,877 | 0.029665 | 52600715 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,779,517 | 108.619000 | 52600715 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,693,790 | 0.029647 | 52600715 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,459,923 | 0.029633 | 52600715 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,248,863 | 0.000012 | 52600715 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,165,949 | 2,422.382573 | 52600715 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,959,510 | 2,425.643525 | 52600715 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 8,106,710 | 0.000012 | 52600715 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 684 | 7,653,841 | 2,422.305269 | 52600715 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,151,199 | 0.001657 | 52600715 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 6,969,019 | 0.000012 | 52600715 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,404,954 | 0.029671 | 52600715 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,356,788 | 1.000859 | 52600715 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,207,947 | 0.026573 | 52600715 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,609,879 | 0.000278 | 52600715 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,561,447 | 0.802388 | 52600715 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,374,334 | 2,421.648674 | 52600715 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,341,187 | 0.998901 | 52600715 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,993,085 | 34,990.015219 | 52600715 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,571,960 | 2,804.290000 | 52600715 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,934,335 | 1.141640 | 52600715 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,839,231 | 0.000012 | 52600715 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,645,835 | 404.339586 | 52600715 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,627,154 | 0.000010 | 52600715 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,543,742 | 108.665623 | 52600715 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,436,745 | 1.157179 | 52600715 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/FAI | 10000 | 2,365,869 | 1,066,812.609594 | 52600715 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 436 | 2,286,154 | 2,425.444891 | 52600715 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,947 | 1.189919 | 52600715 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,090,394 | 0.000000 | 52600715 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,013,517 | 0.023446 | 52600715 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,899,872 | 0.916707 | 52600715 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,884,576 | 15.592970 | 52600715 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,840,035 | 1.397535 | 52600715 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,764,897 | 0.018830 | 52600715 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,735,942 | 0.000012 | 52600715 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,706,051 | 13,642.408927 | 52600715 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,627,044 | 2.304293 | 52600715 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2772 | 1,516,754 | 1,050.327717 | 52600715 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/AERO | 3000 | 1,509,737 | 2,821.080077 | 52600715 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,499,505 | 1.105776 | 52600715 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,465,055 | 0.836119 | 52600715 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,417,860 | 0.000000 | 52600715 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,354,063 | 0.000278 | 52600715 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,340,439 | 0.004814 | 52600715 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3044 | 1,336,222 | 2,820.947960 | 52600715 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,270,767 | 23.392853 | 52600715 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,248,453 | 2,422.402637 | 52600715 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,247,308 | 62.459029 | 52600715 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,231,826 | 33,248,712.924017 | 52600715 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,212,266 | 1.130961 | 52600715 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,209,730 | 1.105594 | 52600715 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,184,836 | 72,281.659931 | 52600715 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,177,290 | 45.469728 | 52600715 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,160,240 | 493,173.304965 | 52600715 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,155,982 | 1,193,657.968819 | 52600715 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,133,732 | 13.645757 | 52600715 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/bsdETH | 100 | 1,029,844 | 0.916698 | 52600715 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 204 ; routes examinées : 4284816 ; candidats optimisés : 32947 ; net attendu > 0 : 34 ; dernier cycle 438.0 ms
- Rejets (moteur) : {'spread_below_threshold': 4189624, 'liquidity_below_min': 41905, 'negative_expected_net': 32913, 'pool_quarantined': 14170, 'unquotable': 5304, 'cycle_budget_exhausted': 662, 'borrow_bound_too_small': 204}
- Enregistrements de la session : 32947 ; net attendu > 0 : 34 ; simulés (eth_call de la vraie tx) : 6 (ok 0, échec 6) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 32947} ; motifs de rejet : {'below_safety_margin': 28, 'negative_expected_net': 32913, 'price_impact': 6, 'reliability_not_demonstrated': 34, 'simulation_failed': 6, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52600662 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.040166 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0167 €) | — | 1.86 | 0.001 (n=14) | REJECTED | below_safety_margin(7462223959115<8033240989289), reliability_not_demonstrated |
| 52600662 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.040166 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0167 €) | — | 1.86 | 0.001 (n=14) | REJECTED | below_safety_margin(7462223959115<8033240989289), reliability_not_demonstrated |
| 52600662 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 96.811949 USDC | 0.025634 USDC | 0.000000 USDC | 0.007567 USDC | 0.018067 USDC (0.0166 €) | — | 1.87 | 0.001 (n=14) | REJECTED | below_safety_margin(18067<19362), reliability_not_demonstrated |
| 52600662 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 96.811949 USDC | 0.025634 USDC | 0.000000 USDC | 0.007567 USDC | 0.018067 USDC (0.0166 €) | — | 1.87 | 0.001 (n=14) | REJECTED | below_safety_margin(18067<19362), reliability_not_demonstrated |
| 52600662 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.037884 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0163 €) | — | 1.92 | 0.001 (n=14) | REJECTED | below_safety_margin(7288814456798<7576712545240), reliability_not_demonstrated |
| 52600662 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.037884 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0163 €) | — | 1.92 | 0.001 (n=14) | REJECTED | below_safety_margin(7288814456798<7576712545240), reliability_not_demonstrated |
| 52600662 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 91.779652 USDC | 0.025214 USDC | 0.000000 USDC | 0.007567 USDC | 0.017647 USDC (0.0162 €) | — | 1.92 | 0.001 (n=14) | REJECTED | below_safety_margin(17647<18355), reliability_not_demonstrated |
| 52600662 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 91.779652 USDC | 0.025214 USDC | 0.000000 USDC | 0.007567 USDC | 0.017647 USDC (0.0162 €) | — | 1.92 | 0.001 (n=14) | REJECTED | below_safety_margin(17647<18355), reliability_not_demonstrated |
| 52600662 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.027332 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.70 | 0.001 (n=14) | REJECTED | below_safety_margin(1917208714190<5466499241195), reliability_not_demonstrated |
| 52600662 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.027332 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.70 | 0.001 (n=14) | REJECTED | below_safety_margin(1917208714190<5466499241195), reliability_not_demonstrated |
| 52600662 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 66.443922 USDC | 0.012200 USDC | 0.000000 USDC | 0.007567 USDC | 0.004633 USDC (0.0043 €) | — | 0.70 | 0.001 (n=14) | REJECTED | below_safety_margin(4633<13288), reliability_not_demonstrated |
| 52600662 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 66.443922 USDC | 0.012200 USDC | 0.000000 USDC | 0.007567 USDC | 0.004633 USDC (0.0043 €) | — | 0.70 | 0.001 (n=14) | REJECTED | below_safety_margin(4633<13288), reliability_not_demonstrated |
| 52600662 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.014547 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0034 €) | — | 1.05 | 0.001 (n=14) | REJECTED | below_safety_margin(1533801009405<2909351261172), reliability_not_demonstrated |
| 52600662 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.014547 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0034 €) | — | 1.05 | 0.001 (n=14) | REJECTED | below_safety_margin(1533801009405<2909351261172), reliability_not_demonstrated |
| 52600662 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 34.827642 USDC | 0.011637 USDC | 0.000000 USDC | 0.007935 USDC | 0.003702 USDC (0.0034 €) | — | 1.06 | 0.001 (n=14) | REJECTED | below_safety_margin(3702<6965), reliability_not_demonstrated |
| 52600662 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 34.827642 USDC | 0.011637 USDC | 0.000000 USDC | 0.007935 USDC | 0.003702 USDC (0.0034 €) | — | 1.06 | 0.001 (n=14) | REJECTED | below_safety_margin(3702<6965), reliability_not_demonstrated |
| 52600662 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.018216 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 0.36 | 0.001 (n=14) | REJECTED | below_safety_margin(653822901890<3643208975084), reliability_not_demonstrated |
| 52600662 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.018216 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 0.36 | 0.001 (n=14) | REJECTED | below_safety_margin(653822901890<3643208975084), reliability_not_demonstrated |
| 52600662 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 43.641288 USDC | 0.009139 USDC | 0.000000 USDC | 0.007567 USDC | 0.001572 USDC (0.0014 €) | — | 0.36 | 0.001 (n=14) | REJECTED | below_safety_margin(1572<8728), reliability_not_demonstrated |
| 52600662 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 43.641288 USDC | 0.009139 USDC | 0.000000 USDC | 0.007567 USDC | 0.001572 USDC (0.0014 €) | — | 0.36 | 0.001 (n=14) | REJECTED | below_safety_margin(1572<8728), reliability_not_demonstrated |
| 52600711 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.012660 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0008 €) | — | 0.28 | 0.003 (n=2) | REJECTED | below_safety_margin(352581114352<2532091133652), reliability_not_demonstrated |
| 52600711 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.012660 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0008 €) | — | 0.28 | 0.003 (n=2) | REJECTED | below_safety_margin(352581114352<2532091133652), reliability_not_demonstrated |
| 52600711 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 30.453077 USDC | 0.006579 USDC | 0.000000 USDC | 0.005733 USDC | 0.000846 USDC (0.0008 €) | — | 0.28 | 0.003 (n=2) | REJECTED | below_safety_margin(846<6090), reliability_not_demonstrated |
| 52600711 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 30.453077 USDC | 0.006579 USDC | 0.000000 USDC | 0.005733 USDC | 0.000846 USDC (0.0008 €) | — | 0.28 | 0.003 (n=2) | REJECTED | below_safety_margin(846<6090), reliability_not_demonstrated |
| 52600570 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.007619 USDC | 0.000000 USDC | 0.006877 USDC | 0.000742 USDC (0.0007 €) | — | 7.42 | 0.027 (n=11) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 139 ; taux observé 0.209 ; borne inférieure crédible (0.9) 0.168 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
