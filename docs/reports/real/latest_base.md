# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T16:47:37+00:00 ; durée 291.44 min ; blocs 52854009 → 52862750 (8373 vus)

## Connexion
- Requêtes RPC : 106419 ; erreurs : 45 ; latence p50/p95 : 344.9/1,036.1 ms
- Rafraîchissements d'état : 8373 ; âge des données au dernier bloc : 3.68 s ; changements de frais LP observés (pools à frais dynamiques) : 29708
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 85283 ; cycles déclenchés par événement : 3792 ; avance médiane sur le rafraîchissement multicall : 704 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,438.74 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21172 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156 (quarantaine 2), pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 393, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2381.795213, 'AERO': 0.801082, 'cbBTC': 81409.268719}
- Pools en quarantaine : 2 — aerodrome_slipstream:USDC/VELVET@0x6b0F53: simulation failed ×5 (model/chain mismatch) — until block 52862910; aerodrome_slipstream:WETH/VELVET@0xF579B1: simulation failed ×5 (model/chain mismatch) — until block 52862910

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,502,319 | 2,438.740584 | 52862750 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 39,869,586 | 1.173389 | 52862750 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,869,770 | 96.098595 | 52862750 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,310,940 | 0.029598 | 52862750 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,976,206 | 0.029540 | 52862750 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,506,405 | 0.029553 | 52862750 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,917,469 | 0.000012 | 52862750 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,563,531 | 2,442.940244 | 52862750 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,368,307 | 2,438.187119 | 52862750 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 8,152,144 | 0.000012 | 52862750 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 624 | 7,486,590 | 2,443.324523 | 52862750 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,257,267 | 0.001680 | 52862750 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 6,767,821 | 0.000012 | 52862750 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,419,565 | 0.029603 | 52862750 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,216,904 | 0.024832 | 52862750 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,709,528 | 0.000275 | 52862750 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,701,985 | 0.802394 | 52862750 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,415,962 | 2,443.908013 | 52862750 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,366,947 | 0.998767 | 52862750 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,275,680 | 1.174447 | 52862750 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 4,044,747 | 34,480.401412 | 52862750 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 409 | 3,462,745 | 2,446.152314 | 52862750 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,354,586 | 2,851.714075 | 52862750 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,970,567 | 1.142084 | 52862750 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,918,534 | 1,022.750052 | 52862750 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,881,878 | 0.000012 | 52862750 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,794,384 | 403.933370 | 52862750 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2817 | 2,731,063 | 96.081646 | 52862750 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,225,254 | 1,219,268.722629 | 52862750 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,169,256 | 0.000010 | 52862750 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,058,857 | 1.238895 | 52862750 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,028,987 | 1.381848 | 52862750 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,970,420 | 0.000000 | 52862750 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,891,952 | 16.049080 | 52862750 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,814,047 | 0.019400 | 52862750 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,771,918 | 0.000012 | 52862750 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,764,278 | 1.105512 | 52862750 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,736,435 | 13,663.020636 | 52862750 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,705,706 | 0.021154 | 52862750 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,682,579 | 2.311794 | 52862750 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,668,899 | 2,863.615086 | 52862750 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,566,805 | 0.916062 | 52862750 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,783 | 0.826046 | 52862750 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,416,315 | 1.123268 | 52862750 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,355,578 | 0.004842 | 52862750 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,339,885 | 0.000000 | 52862750 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,320,426 | 0.000276 | 52862750 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,304,308 | 0.029557 | 52862750 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,288,239 | 23.114716 | 52862750 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,255,998 | 2,442.888809 | 52862750 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,075 | 63.599454 | 52862750 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/EDEL | 7000 | 1,226,467 | 67,577.889803 | 52862750 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/doginme | 10000 | 1,210,960 | 35,656,571.832345 | 52862750 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,180,663 | 0.436750 | 52862750 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,166,190 | 494,160.495614 | 52862750 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,157,130 | 1,204,349.706497 | 52862750 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,151,761 | 0.886363 | 52862750 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,141,291 | 48.374022 | 52862750 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,082,633 | 21,261,604.476198 | 52862750 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,072,166 | 1.001314 | 52862750 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 12164 ; routes examinées : 257536208 ; candidats optimisés : 1515259 ; net attendu > 0 : 1314 ; dernier cycle 232.0 ms
- Rejets (moteur) : {'spread_below_threshold': 253538286, 'liquidity_below_min': 2097504, 'negative_expected_net': 1513945, 'pool_quarantined': 231236, 'borrow_bound_too_small': 138828, 'cycle_budget_exhausted': 15095}
- Enregistrements de la session : 1515259 ; net attendu > 0 : 1314 ; simulés (eth_call de la vraie tx) : 157 (ok 104, échec 53) ; étiquettes ghost N+1 : 17/116 positives
- Décisions : {'REJECTED': 1515259} ; motifs de rejet : {'below_safety_margin': 913, 'negative_expected_net': 1513945, 'p_lower_below_threshold': 1080, 'price_impact': 45, 'reliability_not_demonstrated': 234, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 2, 'simulation_failed': 53, 'stale_data': 91}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52860553 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.269723 WETH | 0.000149 WETH | 0.000000 WETH | 0.000003 WETH | 0.000146 WETH (0.3266 €) | — | 5.41 | 0.109 (n=132) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52860553 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.007574 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3264 €) | — | 5.68 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860377 | WETH→[aerodrome_slipstream]→BRETT→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.028655 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000123 WETH (0.2754 €) | 0.000123 WETH | 42.94 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52861527 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,289.600704 USDC | 0.246212 USDC | 0.000000 USDC | 0.005934 USDC | 0.240278 USDC (0.2211 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(240278<457920), p_lower_below_threshold(0.01<0.75) |
| 52861528 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,289.600704 USDC | 0.246212 USDC | 0.000000 USDC | 0.005934 USDC | 0.240278 USDC (0.2211 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(240278<457920), p_lower_below_threshold(0.01<0.75) |
| 52861527 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.939641 WETH | 0.000101 WETH | 0.000000 WETH | 0.000002 WETH | 0.000098 WETH (0.2205 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(98465456722515<187928164483069), p_lower_below_threshold(0.01<0.75) |
| 52861528 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.939641 WETH | 0.000101 WETH | 0.000000 WETH | 0.000002 WETH | 0.000098 WETH (0.2205 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(98465456722515<187928164483069), p_lower_below_threshold(0.01<0.75) |
| 52860553 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 484.914616 USDC | 0.189088 USDC | 0.000000 USDC | 0.007536 USDC | 0.181552 USDC (0.1670 €) | — | 3.74 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860553 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.005832 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1670 €) | — | 3.77 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860553 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003379 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1374 €) | — | 5.36 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860553 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.115149 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1369 €) | — | 5.31 | 0.109 (n=132) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52860377 | WETH→[aerodrome_slipstream]→BRETT→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.019105 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1181 €) | 0.000053 WETH | 27.61 | 0.005 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52860553 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002547 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1070 €) | — | 5.54 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860553 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 204.066511 USDC | 0.123690 USDC | 0.000000 USDC | 0.007536 USDC | 0.116154 USDC (0.1069 €) | — | 5.69 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 713.236514 USDC | 0.118318 USDC | 0.000000 USDC | 0.005387 USDC | 0.112931 USDC (0.1039 €) | — | 1.58 | 0.037 (n=8) | REJECTED | below_safety_margin(112931<142647), reliability_not_demonstrated |
| 52855720 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.298322 WETH | 0.000049 WETH | 0.000000 WETH | 0.000002 WETH | 0.000047 WETH (0.1039 €) | — | 1.58 | 0.037 (n=8) | REJECTED | below_safety_margin(47156112269631<59664491208030), reliability_not_demonstrated |
| 52860553 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.151034 WETH | 0.000044 WETH | 0.000000 WETH | 0.000003 WETH | 0.000041 WETH (0.0909 €) | — | 2.69 | 0.117 (n=183) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52860553 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003932 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0903 €) | — | 3.03 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860377 | WETH→[aerodrome_slipstream]→BRETT→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.016502 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000039 WETH (0.0862 €) | 0.000039 WETH | 23.35 | 0.005 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 538.043039 USDC | 0.088374 USDC | 0.000000 USDC | 0.007208 USDC | 0.081166 USDC (0.0747 €) | — | 1.51 | 0.105 (n=170) | REJECTED | below_safety_margin(81166<107608), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.220537 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0743 €) | — | 1.53 | 0.105 (n=170) | REJECTED | below_safety_margin(33743439129325<44107398343291), p_lower_below_threshold(0.10<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006168 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0742 €) | — | 1.61 | 0.105 (n=170) | REJECTED | below_safety_margin(99<123), p_lower_below_threshold(0.10<0.75) |
| 52860553 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.106303 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0726 €) | — | 3.05 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860553 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003688 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0721 €) | — | 2.58 | 0.117 (n=183) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52858173 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 233.952408 USDC | 0.082506 USDC | 0.000000 USDC | 0.008077 USDC | 0.074429 USDC (0.0685 €) | — | 3.18 | 0.111 (n=129) | REJECTED | p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1529 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
