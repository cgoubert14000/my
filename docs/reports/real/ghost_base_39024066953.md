# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T15:49:17+00:00 ; durée 330.27 min ; blocs 52721493 → 52731397 (8545 vus)

## Connexion
- Requêtes RPC : 114488 ; erreurs : 98 ; latence p50/p95 : 463.9/1,736.7 ms
- Rafraîchissements d'état : 8546 ; âge des données au dernier bloc : 2.02 s ; changements de frais LP observés (pools à frais dynamiques) : 11036
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 105464 ; cycles déclenchés par événement : 6001 ; avance médiane sur le rafraîchissement multicall : 706 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,416.55 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 577 pools, 329 jetons, 21508 routes
- Par DEX : uniswap_v3 136, aerodrome 235 (quarantaine 2), aerodrome_slipstream 156, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3914 (énumérés 394, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 2 → gardés 577 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2430.106481, 'AERO': 0.895375, 'cbBTC': 81495.8779}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52731502; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52731502

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,412,624 | 2,416.552453 | 52731397 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,229,756 | 1.170435 | 52731397 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,239,144 | 0.029630 | 52731397 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,805,607 | 107.509195 | 52731397 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,430,472 | 0.029692 | 52731397 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,451,585 | 0.029703 | 52731397 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,764,364 | 0.000012 | 52731397 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,103,041 | 2,410.460148 | 52731397 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,317,447 | 0.000012 | 52731397 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,847,681 | 0.000012 | 52731397 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,151,183 | 0.001665 | 52731397 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 609 | 7,057,369 | 2,409.929457 | 52731397 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,408,357 | 2,416.619580 | 52731397 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,334,359 | 0.029626 | 52731397 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,273,346 | 0.025288 | 52731397 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,247,714 | 1.000855 | 52731397 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,830,331 | 0.802398 | 52731397 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,648,367 | 0.000273 | 52731397 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,428,874 | 0.998802 | 52731397 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,395,496 | 2,409.460682 | 52731397 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,034,784 | 34,023.214521 | 52731397 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,404,867 | 2,800.568641 | 52731397 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 412 | 3,074,503 | 2,414.261596 | 52731397 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,840,769 | 0.000012 | 52731397 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,737,899 | 1.141575 | 52731397 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,559,885 | 107.481649 | 52731397 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,495,412 | 0.000010 | 52731397 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,315,332 | 406.758184 | 52731397 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,239,224 | 1,182,290.188062 | 52731397 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,233,342 | 1,028.625416 | 52731397 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,125,943 | 1.123522 | 52731397 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,107,462 | 1.199039 | 52731397 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52731397 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,826,091 | 0.022203 | 52731397 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,809,570 | 0.000000 | 52731397 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,779,549 | 0.000012 | 52731397 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,736,189 | 0.018118 | 52731397 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,722,763 | 15.729807 | 52731397 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,673,334 | 2.306138 | 52731397 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/AERO | 10000 | 1,604,028 | 1.162653 | 52731397 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,544,517 | 0.916547 | 52731397 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,527,892 | 2,820.570728 | 52731397 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,513,829 | 1.105495 | 52731397 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3176 | 1,482,613 | 2,820.078570 | 52731397 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,609 | 0.826277 | 52731397 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,400,579 | 13,700.897196 | 52731397 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,361,407 | 0.000000 | 52731397 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,326,772 | 0.435629 | 52731397 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,309,512 | 0.004696 | 52731397 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,302,762 | 0.000272 | 52731397 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,255,084 | 1.131492 | 52731397 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,249,778 | 23.342942 | 52731397 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,868 | 62.303150 | 52731397 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/cbBTC | 3000 | 1,223,330 | 0.029709 | 52731397 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,218,986 | 1.105716 | 52731397 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,197,504 | 35,598,184.590662 | 52731397 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,192,617 | 2,410.488344 | 52731397 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,173,335 | 1,150,294.794828 | 52731397 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,141,176 | 510,413.849663 | 52731397 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,116,987 | 14.165703 | 52731397 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 14546 ; routes examinées : 312855368 ; candidats optimisés : 1836536 ; net attendu > 0 : 310 ; dernier cycle 279.0 ms
- Rejets (moteur) : {'spread_below_threshold': 307981301, 'liquidity_below_min': 2619586, 'negative_expected_net': 1836226, 'unquotable': 301570, 'pool_quarantined': 89892, 'borrow_bound_too_small': 14501, 'cycle_budget_exhausted': 11982}
- Enregistrements de la session : 1836536 ; net attendu > 0 : 310 ; simulés (eth_call de la vraie tx) : 32 (ok 9, échec 23) ; étiquettes ghost N+1 : 4/21 positives
- Décisions : {'REJECTED': 1836536} ; motifs de rejet : {'below_safety_margin': 263, 'negative_expected_net': 1836226, 'p_lower_below_threshold': 245, 'price_impact': 13, 'reliability_not_demonstrated': 65, 'simulation_failed': 23, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52730522 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.170340 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0558 €) | — | 1.47 | 0.297 (n=50) | REJECTED | below_safety_margin(25018456186769<34067907649518), p_lower_below_threshold(0.30<0.75) |
| 52730522 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 409.550339 USDC | 0.068099 USDC | 0.000000 USDC | 0.007667 USDC | 0.060432 USDC (0.0556 €) | — | 1.48 | 0.297 (n=50) | REJECTED | below_safety_margin(60432<81910), p_lower_below_threshold(0.30<0.75) |
| 52722663 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002568 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0427 €) | — | 2.22 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.083058 WETH | 0.000021 WETH | 0.000000 WETH | 0.000002 WETH | 0.000019 WETH (0.0421 €) | — | 2.26 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52724710 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.054040 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0405 €) | 0.000018 WETH | 3.35 | 0.204 (n=34) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 130.733737 USDC | 0.051356 USDC | 0.000000 USDC | 0.007308 USDC | 0.044048 USDC (0.0405 €) | — | 3.37 | 0.204 (n=34) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52724710 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.055100 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0382 €) | 0.000017 WETH | 3.10 | 0.107 (n=71) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 133.489619 USDC | 0.048821 USDC | 0.000000 USDC | 0.007308 USDC | 0.041513 USDC (0.0382 €) | — | 3.11 | 0.107 (n=71) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52722663 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002454 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0374 €) | — | 2.04 | 0.108 (n=78) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52722663 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 185.995824 USDC | 0.047888 USDC | 0.000000 USDC | 0.007307 USDC | 0.040581 USDC (0.0373 €) | — | 2.18 | 0.108 (n=78) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.083058 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0369 €) | — | 1.99 | 0.108 (n=78) | REJECTED | below_safety_margin(16488156450115<16611681200461), p_lower_below_threshold(0.11<0.75) |
| 52730522 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.130064 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0347 €) | — | 1.20 | 0.116 (n=80) | REJECTED | below_safety_margin(15551297699185<26012742532840), p_lower_below_threshold(0.12<0.75) |
| 52730522 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004134 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0346 €) | — | 1.11 | 0.116 (n=80) | REJECTED | below_safety_margin(46<82), p_lower_below_threshold(0.12<0.75) |
| 52728708 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.140277 WETH | 0.000018 WETH | 0.000000 WETH | 0.000002 WETH | 0.000015 WETH (0.0343 €) | — | 1.10 | 0.039 (n=21) | REJECTED | below_safety_margin(15392865644451<28055415318841), reliability_not_demonstrated |
| 52728708 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 338.645864 USDC | 0.042673 USDC | 0.000000 USDC | 0.005451 USDC | 0.037222 USDC (0.0342 €) | — | 1.10 | 0.039 (n=21) | REJECTED | below_safety_margin(37222<67729), reliability_not_demonstrated |
| 52730522 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 285.909391 USDC | 0.044537 USDC | 0.000000 USDC | 0.007667 USDC | 0.036870 USDC (0.0339 €) | — | 1.29 | 0.116 (n=80) | REJECTED | below_safety_margin(36870<57181), p_lower_below_threshold(0.12<0.75) |
| 52730522 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.122617 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0339 €) | — | 1.24 | 0.116 (n=80) | REJECTED | below_safety_margin(15196000673091<24523307319234), p_lower_below_threshold(0.12<0.75) |
| 52730522 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003511 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0338 €) | — | 1.28 | 0.116 (n=80) | REJECTED | below_safety_margin(45<70), p_lower_below_threshold(0.12<0.75) |
| 52730522 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 285.909391 USDC | 0.043962 USDC | 0.000000 USDC | 0.007667 USDC | 0.036295 USDC (0.0334 €) | — | 1.27 | 0.116 (n=80) | REJECTED | below_safety_margin(36295<57181), p_lower_below_threshold(0.12<0.75) |
| 52730522 | WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.136145 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0333 €) | — | 1.10 | 0.297 (n=50) | REJECTED | below_safety_margin(14930187609781<27228972612655), p_lower_below_threshold(0.30<0.75) |
| 52730522 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 338.534320 USDC | 0.043683 USDC | 0.000000 USDC | 0.007667 USDC | 0.036016 USDC (0.0331 €) | — | 1.06 | 0.297 (n=50) | REJECTED | below_safety_margin(36016<67706), p_lower_below_threshold(0.30<0.75) |
| 52730522 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.003774 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0330 €) | — | 1.17 | 0.297 (n=50) | REJECTED | below_safety_margin(44<75), p_lower_below_threshold(0.30<0.75) |
| 52730522 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.139006 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0326 €) | — | 1.05 | 0.297 (n=50) | REJECTED | below_safety_margin(14628199818348<27801223280540), p_lower_below_threshold(0.30<0.75) |
| 52730522 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 335.634474 USDC | 0.042896 USDC | 0.000000 USDC | 0.007667 USDC | 0.035229 USDC (0.0324 €) | — | 1.05 | 0.297 (n=50) | REJECTED | below_safety_margin(35229<67126), p_lower_below_threshold(0.30<0.75) |
| 52730522 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.003985 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0323 €) | — | 1.08 | 0.297 (n=50) | REJECTED | below_safety_margin(43<79), p_lower_below_threshold(0.30<0.75) |

## Fiabilité et décision
- Observations ghost : 742 ; taux observé 0.123 ; borne inférieure crédible (0.9) 0.108 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
