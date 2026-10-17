# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T11:51:35+00:00 ; durée 92.58 min ; blocs 52721493 → 52724271 (2663 vus)

## Connexion
- Requêtes RPC : 35461 ; erreurs : 5 ; latence p50/p95 : 352.9/1,099.4 ms
- Rafraîchissements d'état : 2663 ; âge des données au dernier bloc : 2.81 s ; changements de frais LP observés (pools à frais dynamiques) : 2525
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 35485 ; cycles déclenchés par événement : 2170 ; avance médiane sur le rafraîchissement multicall : 583 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,431.20 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 577 pools, 329 jetons, 21508 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3914 (énumérés 394, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 2 → gardés 577 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2430.106481, 'AERO': 0.895375, 'cbBTC': 81495.8779}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,810,431 | 2,431.202292 | 52724271 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,986,698 | 1.129594 | 52724271 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 20,063,777 | 0.029821 | 52724271 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,305,092 | 0.029850 | 52724271 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,047,975 | 105.426159 | 52724271 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,480,652 | 0.029806 | 52724271 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,765,037 | 0.000012 | 52724271 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 9,400,352 | 0.000012 | 52724271 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 9,134,358 | 2,431.073922 | 52724271 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,846,358 | 0.000012 | 52724271 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,500,086 | 2,431.436567 | 52724271 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,170,943 | 0.001675 | 52724271 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,424,762 | 2,435.908925 | 52724271 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,382,504 | 0.025250 | 52724271 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,354,533 | 0.029837 | 52724271 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,279,527 | 1.000855 | 52724271 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,859,508 | 0.802398 | 52724271 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,699,888 | 0.000276 | 52724271 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,475,558 | 2,431.163212 | 52724271 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,426,945 | 0.998803 | 52724271 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,064,263 | 33,939.239295 | 52724271 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,478,845 | 2,729.419849 | 52724271 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,929,580 | 1.141834 | 52724271 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,853,486 | 1,023.102084 | 52724271 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,840,334 | 0.000012 | 52724271 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,621,153 | 402.272430 | 52724271 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2784 | 2,602,606 | 105.436983 | 52724271 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,539,061 | 0.000011 | 52724271 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,250,207 | 1,185,014.580488 | 52724271 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,126,176 | 1.123433 | 52724271 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,805 | 1.197614 | 52724271 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,030,707 | 15.630065 | 52724271 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,028,797 | 2,435.528596 | 52724271 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52724271 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,831,115 | 0.022350 | 52724271 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,820,560 | 0.000000 | 52724271 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,779,011 | 0.000012 | 52724271 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,751,503 | 0.018401 | 52724271 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,682,452 | 2.306988 | 52724271 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/AERO | 10000 | 1,676,375 | 1.123994 | 52724271 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,553,876 | 0.916548 | 52724271 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,552,142 | 2,744.475998 | 52724271 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3144 | 1,527,581 | 2,742.723156 | 52724271 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,523,005 | 1.105495 | 52724271 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,550 | 0.826343 | 52724271 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,408,972 | 13,459.026687 | 52724271 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,366,449 | 0.004872 | 52724271 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,365,615 | 0.000000 | 52724271 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,326,341 | 0.435854 | 52724271 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,317,174 | 0.000274 | 52724271 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,255,015 | 23.300859 | 52724271 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299956 | 52724271 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,240,458 | 1.131652 | 52724271 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/cbBTC | 3000 | 1,231,706 | 0.029801 | 52724271 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,231,367 | 1.105714 | 52724271 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,207,377 | 35,368,823.910888 | 52724271 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,202,101 | 2,432.235807 | 52724271 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,187,251 | 1,137,151.572454 | 52724271 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,152,383 | 505,209.211580 | 52724271 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,120,119 | 14.067038 | 52724271 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 4832 ; routes examinées : 103926656 ; candidats optimisés : 523698 ; net attendu > 0 : 31 ; dernier cycle 163.9 ms
- Rejets (moteur) : {'spread_below_threshold': 102373338, 'liquidity_below_min': 914137, 'negative_expected_net': 523667, 'unquotable': 109540, 'borrow_bound_too_small': 4828, 'cycle_budget_exhausted': 1115}
- Enregistrements de la session : 523698 ; net attendu > 0 : 31 ; simulés (eth_call de la vraie tx) : 5 (ok 1, échec 4) ; étiquettes ghost N+1 : 4/4 positives
- Décisions : {'REJECTED': 523698} ; motifs de rejet : {'below_safety_margin': 25, 'negative_expected_net': 523667, 'p_lower_below_threshold': 21, 'reliability_not_demonstrated': 10, 'simulation_failed': 4}

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
| 52723367 | WETH→[aerodrome]→BID→[aerodrome_slipstream]→WETH | 0.005509 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0091 €) | 0.000004 WETH | 7.42 | 0.050 (n=6) | REJECTED | reliability_not_demonstrated |
| 52723367 | WETH→[aerodrome]→BID→[aerodrome_slipstream]→WETH | 0.005212 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0077 €) | — | 6.61 | 0.050 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52722663 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.000850 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.47 | 0.297 (n=50) | REJECTED | below_safety_margin(4<16), p_lower_below_threshold(0.30<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH | 0.033420 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0028 €) | — | 0.37 | 0.297 (n=50) | REJECTED | below_safety_margin(1240888153480<6683910078116), p_lower_below_threshold(0.30<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→WETH | 0.033420 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.32 | 0.297 (n=50) | REJECTED | below_safety_margin(1063662712362<6683910078116), p_lower_below_threshold(0.30<0.75) |
| 52722663 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.000836 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0022 €) | — | 0.36 | 0.108 (n=78) | REJECTED | below_safety_margin(3<16), p_lower_below_threshold(0.11<0.75) |
| 52722663 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.000850 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0022 €) | — | 0.35 | 0.297 (n=50) | REJECTED | below_safety_margin(3<16), p_lower_below_threshold(0.30<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→WETH | 0.026324 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 0.36 | 0.108 (n=78) | REJECTED | below_safety_margin(959946402556<5264717153801), p_lower_below_threshold(0.11<0.75) |
| 52722465 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 22.461917 USDC | 0.007673 USDC | 0.000000 USDC | 0.005458 USDC | 0.002215 USDC (0.0020 €) | — | 0.99 | 0.000 (n=19) | REJECTED | below_safety_margin(2215<4492), reliability_not_demonstrated |
| 52722465 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 22.461917 USDC | 0.007673 USDC | 0.000000 USDC | 0.005458 USDC | 0.002215 USDC (0.0020 €) | — | 0.99 | 0.000 (n=19) | REJECTED | below_safety_margin(2215<4492), reliability_not_demonstrated |
| 52724134 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001851 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0015 €) | — | 0.11 | 0.117 (n=79) | REJECTED | below_safety_margin(2<37), p_lower_below_threshold(0.12<0.75) |
| 52724135 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001851 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0015 €) | — | 0.11 | 0.117 (n=79) | REJECTED | below_safety_margin(2<37), p_lower_below_threshold(0.12<0.75) |
| 52724135 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001852 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0015 €) | — | 0.11 | 0.117 (n=79) | REJECTED | below_safety_margin(2<37), p_lower_below_threshold(0.12<0.75) |
| 52724135 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.076775 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 0.07 | 0.117 (n=79) | REJECTED | below_safety_margin(523392126407<15354960189514), p_lower_below_threshold(0.12<0.75) |
| 52724135 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 144.268562 USDC | 0.008320 USDC | 0.000000 USDC | 0.007308 USDC | 0.001012 USDC (0.0009 €) | — | 0.07 | 0.117 (n=79) | REJECTED | below_safety_margin(1012<28853), p_lower_below_threshold(0.12<0.75) |
| 52724134 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.053425 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.07 | 0.117 (n=79) | REJECTED | below_safety_margin(373649721023<10685045878629), p_lower_below_threshold(0.12<0.75) |
| 52724135 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.053425 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.07 | 0.117 (n=79) | REJECTED | below_safety_margin(373649721023<10685045878629), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 725 ; taux observé 0.126 ; borne inférieure crédible (0.9) 0.110 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
