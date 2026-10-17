# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T14:59:03+00:00 ; durée 280.04 min ; blocs 52721493 → 52729890 (7210 vus)

## Connexion
- Requêtes RPC : 97366 ; erreurs : 58 ; latence p50/p95 : 481.8/1,504.8 ms
- Rafraîchissements d'état : 7210 ; âge des données au dernier bloc : 5.58 s ; changements de frais LP observés (pools à frais dynamiques) : 8791
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 94434 ; cycles déclenchés par événement : 5305 ; avance médiane sur le rafraîchissement multicall : 1,085 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,424.79 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 577 pools, 329 jetons, 21508 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3914 (énumérés 394, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 2 → gardés 577 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2430.106481, 'AERO': 0.895375, 'cbBTC': 81495.8779}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,704,921 | 2,424.785467 | 52729890 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,487,367 | 1.156254 | 52729890 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,276,101 | 0.029760 | 52729890 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,922,578 | 106.658143 | 52729890 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,407,178 | 0.029788 | 52729890 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,466,864 | 0.029802 | 52729890 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 10,068,129 | 0.000012 | 52729890 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,762,304 | 0.000012 | 52729890 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,124,553 | 2,425.190514 | 52729890 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 549 | 8,745,566 | 2,425.208869 | 52729890 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,869,478 | 0.000012 | 52729890 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,156,299 | 0.001670 | 52729890 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,417,596 | 2,425.722090 | 52729890 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,345,202 | 0.029761 | 52729890 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,313,004 | 0.025256 | 52729890 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,265,593 | 1.000855 | 52729890 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,019,320 | 1.153367 | 52729890 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,846,683 | 0.802398 | 52729890 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,664,204 | 0.000273 | 52729890 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,431,379 | 2,425.066173 | 52729890 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,424,351 | 0.998803 | 52729890 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,048,530 | 34,023.214521 | 52729890 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,431,471 | 2,794.199552 | 52729890 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 403 | 3,075,599 | 2,429.615188 | 52729890 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,839,169 | 0.000012 | 52729890 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,747,071 | 1.141484 | 52729890 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,736,717 | 404.325143 | 52729890 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,580,194 | 106.682066 | 52729890 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,517,688 | 0.000011 | 52729890 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,246,853 | 1,182,290.188062 | 52729890 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,126,038 | 1.123603 | 52729890 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,107,462 | 1.199039 | 52729890 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52729890 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,924,704 | 15.717294 | 52729890 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,828,765 | 0.022283 | 52729890 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,815,717 | 0.000000 | 52729890 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,784,765 | 13,571.837090 | 52729890 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,299 | 0.000012 | 52729890 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,751,329 | 0.018392 | 52729890 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,678,071 | 2.306907 | 52729890 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,549,779 | 0.916547 | 52729890 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,537,628 | 2,801.104903 | 52729890 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,518,986 | 1.105495 | 52729890 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,496,299 | 2,800.935972 | 52729890 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,594 | 0.826294 | 52729890 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,366,220 | 0.000000 | 52729890 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,327,010 | 0.435746 | 52729890 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,321,751 | 0.004702 | 52729890 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,307,191 | 0.000273 | 52729890 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,249,274 | 23.345508 | 52729890 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,868 | 62.303150 | 52729890 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,243,462 | 1.131606 | 52729890 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,237,340 | 1.105716 | 52729890 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,224,812 | 0.029801 | 52729890 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,201,584 | 35,598,184.590662 | 52729890 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,195,434 | 2,425.188484 | 52729890 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,177,333 | 1,150,294.794828 | 52729890 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,145,064 | 510,413.849663 | 52729890 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,123,832 | 13.951440 | 52729890 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,101,569 | 0.885573 | 52729890 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |

## Recherche d'opportunités
- Cycles : 12514 ; routes examinées : 269151112 ; candidats optimisés : 1624393 ; net attendu > 0 : 141 ; dernier cycle 398.0 ms
- Rejets (moteur) : {'spread_below_threshold': 264870604, 'liquidity_below_min': 2307438, 'negative_expected_net': 1624252, 'unquotable': 285332, 'pool_quarantined': 39336, 'borrow_bound_too_small': 12471, 'cycle_budget_exhausted': 11538}
- Enregistrements de la session : 1624393 ; net attendu > 0 : 141 ; simulés (eth_call de la vraie tx) : 15 (ok 6, échec 9) ; étiquettes ghost N+1 : 4/11 positives
- Décisions : {'REJECTED': 1624393} ; motifs de rejet : {'below_safety_margin': 111, 'negative_expected_net': 1624252, 'p_lower_below_threshold': 93, 'price_impact': 7, 'reliability_not_demonstrated': 48, 'simulation_failed': 9, 'stale_data': 2}

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
| 52728708 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.140277 WETH | 0.000018 WETH | 0.000000 WETH | 0.000002 WETH | 0.000015 WETH (0.0343 €) | — | 1.10 | 0.039 (n=21) | REJECTED | below_safety_margin(15392865644451<28055415318841), reliability_not_demonstrated |
| 52728708 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 338.645864 USDC | 0.042673 USDC | 0.000000 USDC | 0.005451 USDC | 0.037222 USDC (0.0342 €) | — | 1.10 | 0.039 (n=21) | REJECTED | below_safety_margin(37222<67729), reliability_not_demonstrated |
| 52724710 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.047569 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0272 €) | 0.000012 WETH | 2.56 | 0.117 (n=79) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 115.187745 USDC | 0.036847 USDC | 0.000000 USDC | 0.007308 USDC | 0.029539 USDC (0.0272 €) | — | 2.56 | 0.117 (n=79) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52728622 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002085 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0248 €) | — | 1.58 | 0.039 (n=21) | REJECTED | below_safety_margin(33<41), reliability_not_demonstrated |
| 52728624 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002085 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0248 €) | — | 1.58 | 0.039 (n=21) | REJECTED | below_safety_margin(33<41), reliability_not_demonstrated |
| 52728622 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.069745 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0242 €) | — | 1.55 | 0.039 (n=21) | REJECTED | below_safety_margin(10837232421786<13948985379343), reliability_not_demonstrated |
| 52728624 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.069745 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0242 €) | — | 1.55 | 0.039 (n=21) | REJECTED | below_safety_margin(10837232421786<13948985379343), reliability_not_demonstrated |
| 52722663 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 170.111193 USDC | 0.032966 USDC | 0.000000 USDC | 0.007676 USDC | 0.025290 USDC (0.0233 €) | — | 1.49 | 0.108 (n=78) | REJECTED | below_safety_margin(25290<34022), p_lower_below_threshold(0.11<0.75) |
| 52722663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.066625 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0232 €) | — | 1.56 | 0.108 (n=78) | REJECTED | below_safety_margin(10381632421486<13324907928011), p_lower_below_threshold(0.11<0.75) |
| 52722663 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001950 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0232 €) | — | 1.59 | 0.108 (n=78) | REJECTED | below_safety_margin(31<38), p_lower_below_threshold(0.11<0.75) |
| 52724710 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.043762 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0217 €) | — | 2.21 | 0.297 (n=50) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 105.765901 USDC | 0.030850 USDC | 0.000000 USDC | 0.007308 USDC | 0.023542 USDC (0.0217 €) | — | 2.23 | 0.297 (n=50) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 52724710 | USDC→[uniswap_v3]→AERO→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 39.932995 USDC | 0.025665 USDC | 0.000000 USDC | 0.006972 USDC | 0.018693 USDC (0.0172 €) | — | 4.68 | 0.000 (n=17) | REJECTED | reliability_not_demonstrated |
| 52724710 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDbC→[aerodrome_slipstream]→USDC | 50.785501 USDC | 0.023044 USDC | 0.000000 USDC | 0.006972 USDC | 0.016072 USDC (0.0148 €) | — | 3.16 | 0.012 (n=65) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52728622 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.001865 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0143 €) | — | 1.02 | 0.075 (n=4) | REJECTED | below_safety_margin(19<37), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 732 ; taux observé 0.124 ; borne inférieure crédible (0.9) 0.109 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
