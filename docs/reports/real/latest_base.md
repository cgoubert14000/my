# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T12:32:10+00:00 ; durée 133.16 min ; blocs 52721493 → 52725487 (3754 vus)

## Connexion
- Requêtes RPC : 50286 ; erreurs : 25 ; latence p50/p95 : 603.7/1,665.3 ms
- Rafraîchissements d'état : 3754 ; âge des données au dernier bloc : 4.07 s ; changements de frais LP observés (pools à frais dynamiques) : 4428
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 53954 ; cycles déclenchés par événement : 3061 ; avance médiane sur le rafraîchissement multicall : 1,234 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,431.20 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 577 pools, 329 jetons, 21508 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3914 (énumérés 394, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 2 → gardés 577 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2430.106481, 'AERO': 0.895375, 'cbBTC': 81495.8779}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,958,007 | 2,431.202194 | 52725487 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,537,852 | 1.153565 | 52725487 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,307,849 | 0.029809 | 52725487 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,014,852 | 105.991289 | 52725487 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,055,083 | 0.029821 | 52725487 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,482,580 | 0.029806 | 52725487 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,769,593 | 0.000012 | 52725487 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,134,133 | 2,428.265872 | 52725487 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 8,743,492 | 0.000012 | 52725487 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,847,678 | 0.000012 | 52725487 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,164,182 | 0.001671 | 52725487 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,061,756 | 2,428.016563 | 52725488 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,424,760 | 2,431.784803 | 52725487 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,354,803 | 0.029810 | 52725487 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,327,140 | 0.025253 | 52725487 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,279,527 | 1.000855 | 52725487 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,961,884 | 1.149861 | 52725487 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,859,508 | 0.802398 | 52725487 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,692,205 | 0.000275 | 52725487 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,428,731 | 0.998803 | 52725487 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,424,279 | 2,427.858793 | 52725487 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,064,132 | 33,941.421720 | 52725487 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 415 | 4,029,587 | 2,432.087208 | 52725487 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,442,513 | 2,785.873089 | 52725487 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,929,580 | 1.141834 | 52725487 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,841,030 | 0.000012 | 52725487 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,723,121 | 403.823776 | 52725487 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,630,766 | 0.000011 | 52725487 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,595,171 | 106.016643 | 52725487 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,275,766 | 1,027.967727 | 52725487 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,249,876 | 1,185,363.337387 | 52725487 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,126,788 | 1.123932 | 52725487 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,805 | 1.197614 | 52725487 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52725487 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,850,628 | 15.671755 | 52725487 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,835,043 | 13,543.789020 | 52725487 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,831,177 | 0.022350 | 52725487 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,820,560 | 0.000000 | 52725487 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,779,442 | 0.000012 | 52725487 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,741,101 | 0.018211 | 52725488 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,682,452 | 2.306988 | 52725487 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,553,879 | 0.916547 | 52725487 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,541,498 | 2,799.404959 | 52725487 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,523,005 | 1.105495 | 52725487 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,509,802 | 2,799.492112 | 52725487 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,550 | 0.826343 | 52725487 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,366,553 | 0.000000 | 52725487 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,326,585 | 0.435935 | 52725487 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,324,629 | 0.004727 | 52725487 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,315,024 | 0.000273 | 52725487 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,253,039 | 23.334297 | 52725487 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299956 | 52725487 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,240,458 | 1.131652 | 52725487 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/cbBTC | 3000 | 1,231,955 | 0.029801 | 52725487 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,231,367 | 1.105714 | 52725487 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,206,380 | 35,455,975.252920 | 52725487 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,200,961 | 2,428.299028 | 52725487 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,187,209 | 1,137,232.165336 | 52725487 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,152,167 | 505,468.924815 | 52725487 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,115,833 | 14.202539 | 52725487 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 6814 ; routes examinées : 146555512 ; candidats optimisés : 723658 ; net attendu > 0 : 71 ; dernier cycle 437.9 ms
- Rejets (moteur) : {'spread_below_threshold': 144402039, 'liquidity_below_min': 1266417, 'negative_expected_net': 723587, 'unquotable': 155057, 'borrow_bound_too_small': 6807, 'cycle_budget_exhausted': 1436}
- Enregistrements de la session : 723658 ; net attendu > 0 : 71 ; simulés (eth_call de la vraie tx) : 9 (ok 5, échec 4) ; étiquettes ghost N+1 : 4/8 positives
- Décisions : {'REJECTED': 723658} ; motifs de rejet : {'below_safety_margin': 47, 'negative_expected_net': 723587, 'p_lower_below_threshold': 58, 'reliability_not_demonstrated': 13, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52722663 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002568 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0427 €) | — | 2.22 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.083058 WETH | 0.000021 WETH | 0.000000 WETH | 0.000002 WETH | 0.000019 WETH (0.0421 €) | — | 2.26 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52724710 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.054040 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0405 €) | 0.000018 WETH | 3.35 | 0.204 (n=34) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 130.733737 USDC | 0.051356 USDC | 0.000000 USDC | 0.007308 USDC | 0.044048 USDC (0.0405 €) | — | 3.37 | 0.204 (n=34) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52724710 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.055100 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0382 €) | 0.000017 WETH | 3.10 | 0.107 (n=71) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 133.489619 USDC | 0.048821 USDC | 0.000000 USDC | 0.007308 USDC | 0.041513 USDC (0.0382 €) | — | 3.11 | 0.107 (n=71) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52722663 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002454 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0374 €) | — | 2.04 | 0.108 (n=78) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52722663 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 185.995824 USDC | 0.047888 USDC | 0.000000 USDC | 0.007307 USDC | 0.040581 USDC (0.0373 €) | — | 2.18 | 0.108 (n=78) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.083058 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0369 €) | — | 1.99 | 0.108 (n=78) | REJECTED | below_safety_margin(16488156450115<16611681200461), p_lower_below_threshold(0.11<0.75) |
| 52724710 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.047569 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0272 €) | 0.000012 WETH | 2.56 | 0.117 (n=79) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 115.187745 USDC | 0.036847 USDC | 0.000000 USDC | 0.007308 USDC | 0.029539 USDC (0.0272 €) | — | 2.56 | 0.117 (n=79) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52722663 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 170.111193 USDC | 0.032966 USDC | 0.000000 USDC | 0.007676 USDC | 0.025290 USDC (0.0233 €) | — | 1.49 | 0.108 (n=78) | REJECTED | below_safety_margin(25290<34022), p_lower_below_threshold(0.11<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.066625 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0232 €) | — | 1.56 | 0.108 (n=78) | REJECTED | below_safety_margin(10381632421486<13324907928011), p_lower_below_threshold(0.11<0.75) |
| 52722663 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001950 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0232 €) | — | 1.59 | 0.108 (n=78) | REJECTED | below_safety_margin(31<38), p_lower_below_threshold(0.11<0.75) |
| 52724710 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.043762 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0217 €) | — | 2.21 | 0.297 (n=50) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 105.765901 USDC | 0.030850 USDC | 0.000000 USDC | 0.007308 USDC | 0.023542 USDC (0.0217 €) | — | 2.23 | 0.297 (n=50) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 39.932995 USDC | 0.025665 USDC | 0.000000 USDC | 0.006972 USDC | 0.018693 USDC (0.0172 €) | — | 4.68 | 0.000 (n=17) | REJECTED | reliability_not_demonstrated |
| 52724710 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDbC→[aerodrome_slipstream]→USDC | 50.785501 USDC | 0.023044 USDC | 0.000000 USDC | 0.006972 USDC | 0.016072 USDC (0.0148 €) | — | 3.16 | 0.012 (n=65) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52724710 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.000763 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0143 €) | — | 2.49 | 0.117 (n=79) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 56.694897 USDC | 0.022350 USDC | 0.000000 USDC | 0.007308 USDC | 0.015042 USDC (0.0138 €) | — | 2.65 | 0.117 (n=79) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52724710 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.020054 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0134 €) | — | 2.99 | 0.297 (n=50) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 48.929762 USDC | 0.021891 USDC | 0.000000 USDC | 0.007308 USDC | 0.014583 USDC (0.0134 €) | — | 2.98 | 0.297 (n=50) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 52724710 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.026614 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0128 €) | — | 2.15 | 0.297 (n=50) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 64.397771 USDC | 0.021580 USDC | 0.000000 USDC | 0.007677 USDC | 0.013903 USDC (0.0128 €) | — | 2.16 | 0.297 (n=50) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 52723367 | WETH→[aerodrome]→BID→[aerodrome_slipstream]→WETH | 0.005509 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0091 €) | 0.000004 WETH | 7.42 | 0.050 (n=6) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 729 ; taux observé 0.125 ; borne inférieure crédible (0.9) 0.110 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
