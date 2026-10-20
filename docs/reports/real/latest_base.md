# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T12:54:40+00:00 ; durée 58.48 min ; blocs 52854009 → 52855763 (1724 vus)

## Connexion
- Requêtes RPC : 23636 ; erreurs : 0 ; latence p50/p95 : 379.1/953.8 ms
- Rafraîchissements d'état : 1724 ; âge des données au dernier bloc : 3.1 s ; changements de frais LP observés (pools à frais dynamiques) : 3531
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 33793 ; cycles déclenchés par événement : 1642 ; avance médiane sur le rafraîchissement multicall : 758 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,393.84 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21172 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 393, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2381.795213, 'AERO': 0.801082, 'cbBTC': 81409.268719}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,351,651 | 2,393.844550 | 52855764 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,301,971 | 1.249973 | 52855764 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,366,537 | 98.321078 | 52855764 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,054,826 | 0.029369 | 52855764 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,907,583 | 0.029322 | 52855764 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,332,472 | 0.029310 | 52855764 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,876,069 | 0.000012 | 52855764 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 9,207,103 | 0.000012 | 52855764 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,319,550 | 2,395.442321 | 52855764 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,290,896 | 2,393.962678 | 52855764 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 8,140,233 | 0.000012 | 52855764 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,242,135 | 2,395.108432 | 52855764 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,163,195 | 0.001672 | 52855764 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,362,954 | 0.029362 | 52855764 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,941,426 | 0.025412 | 52855764 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,769,246 | 0.802395 | 52855764 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,617,543 | 0.000275 | 52855764 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,354,182 | 2,395.327795 | 52855764 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,319,686 | 0.998767 | 52855764 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 406 | 4,008,149 | 2,398.910824 | 52855764 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 3,987,991 | 34,174.907805 | 52855764 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,632,194 | 1.242540 | 52855764 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,220,209 | 2,968.820315 | 52855764 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,868,541 | 0.000012 | 52855764 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,738,821 | 1.142101 | 52855764 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,652,295 | 98.295442 | 52855764 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,398,177 | 401.144443 | 52855764 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,184,350 | 1,219,199.413671 | 52855764 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,144,766 | 0.000010 | 52855764 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,548 | 1.237984 | 52855764 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,015 | 1.373598 | 52855764 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,934,837 | 0.000000 | 52855764 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 1,920,644 | 985.129491 | 52855764 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,862,038 | 16.030712 | 52855764 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,836,938 | 13,669.240409 | 52855764 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,803,825 | 0.019162 | 52855764 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,758,141 | 0.000012 | 52855764 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,732,046 | 1.105526 | 52855764 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,678,633 | 0.020328 | 52855764 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,652,679 | 2.306463 | 52855764 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,614,829 | 2,989.926231 | 52855764 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,550,536 | 0.916340 | 52855764 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,757 | 0.826075 | 52855764 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,407,689 | 1.122522 | 52855764 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,303,144 | 0.004722 | 52855764 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,301,112 | 0.000000 | 52855764 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,294,652 | 0.000275 | 52855764 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,285,283 | 0.029315 | 52855764 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,240,959 | 2,395.486658 | 52855764 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,136 | 63.593116 | 52855764 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,211,872 | 23.001673 | 52855764 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,237 | 35,338,545.602743 | 52855764 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,178,385 | 0.435540 | 52855764 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/WELL | 10000 | 1,163,014 | 1,148,702.566422 | 52855764 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | WETH/EDEL | 7000 | 1,148,562 | 74,951.643645 | 52855764 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,143,983 | 1.131507 | 52855764 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,131,158 | 509,977.897248 | 52855764 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,115,570 | 50.630083 | 52855764 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,096,991 | 0.885429 | 52855764 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | WETH/VVV | 8000 | 1,075,275 | 98.341899 | 52855764 | `0x46D398A5b33709877f50c8918A7eE96F1Be1d7dd` |

## Recherche d'opportunités
- Cycles : 3364 ; routes examinées : 71222608 ; candidats optimisés : 421295 ; net attendu > 0 : 48 ; dernier cycle 292.1 ms
- Rejets (moteur) : {'spread_below_threshold': 70238708, 'liquidity_below_min': 478063, 'negative_expected_net': 421247, 'borrow_bound_too_small': 84025, 'cycle_budget_exhausted': 517}
- Enregistrements de la session : 421295 ; net attendu > 0 : 48 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 421295} ; motifs de rejet : {'below_safety_margin': 48, 'negative_expected_net': 421247, 'p_lower_below_threshold': 41, 'reliability_not_demonstrated': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52855720 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 713.236514 USDC | 0.118318 USDC | 0.000000 USDC | 0.005387 USDC | 0.112931 USDC (0.1039 €) | — | 1.58 | 0.037 (n=8) | REJECTED | below_safety_margin(112931<142647), reliability_not_demonstrated |
| 52855720 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.298322 WETH | 0.000049 WETH | 0.000000 WETH | 0.000002 WETH | 0.000047 WETH (0.1039 €) | — | 1.58 | 0.037 (n=8) | REJECTED | below_safety_margin(47156112269631<59664491208030), reliability_not_demonstrated |
| 52855720 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 538.043039 USDC | 0.088374 USDC | 0.000000 USDC | 0.007208 USDC | 0.081166 USDC (0.0747 €) | — | 1.51 | 0.105 (n=170) | REJECTED | below_safety_margin(81166<107608), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.220537 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0743 €) | — | 1.53 | 0.105 (n=170) | REJECTED | below_safety_margin(33743439129325<44107398343291), p_lower_below_threshold(0.10<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006168 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0742 €) | — | 1.61 | 0.105 (n=170) | REJECTED | below_safety_margin(99<123), p_lower_below_threshold(0.10<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 536.977543 USDC | 0.072310 USDC | 0.000000 USDC | 0.005387 USDC | 0.066923 USDC (0.0616 €) | — | 1.25 | 0.015 (n=55) | REJECTED | below_safety_margin(66923<107395), p_lower_below_threshold(0.01<0.75) |
| 52855720 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.223989 WETH | 0.000030 WETH | 0.000000 WETH | 0.000002 WETH | 0.000028 WETH (0.0615 €) | — | 1.25 | 0.015 (n=55) | REJECTED | below_safety_margin(27946824524775<44797787505007), p_lower_below_threshold(0.01<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.004024 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0225 €) | — | 0.75 | 0.105 (n=170) | REJECTED | below_safety_margin(30<80), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.149644 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0223 €) | — | 0.68 | 0.105 (n=170) | REJECTED | below_safety_margin(10137837285679<29928744395192), p_lower_below_threshold(0.10<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 356.300100 USDC | 0.031278 USDC | 0.000000 USDC | 0.007208 USDC | 0.024070 USDC (0.0221 €) | — | 0.68 | 0.105 (n=170) | REJECTED | below_safety_margin(24070<71260), p_lower_below_threshold(0.10<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002845 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 0.98 | 0.105 (n=170) | REJECTED | below_safety_margin(28<56), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.101917 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0208 €) | — | 0.93 | 0.105 (n=170) | REJECTED | below_safety_margin(9435113610228<20383429878557), p_lower_below_threshold(0.10<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 235.351875 USDC | 0.029739 USDC | 0.000000 USDC | 0.007208 USDC | 0.022531 USDC (0.0207 €) | — | 0.96 | 0.105 (n=170) | REJECTED | below_safety_margin(22531<47070), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.044009 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0110 €) | — | 1.14 | 0.105 (n=170) | REJECTED | below_safety_margin(5008385979697<8801774534475), p_lower_below_threshold(0.10<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 104.563635 USDC | 0.019457 USDC | 0.000000 USDC | 0.007572 USDC | 0.011885 USDC (0.0109 €) | — | 1.14 | 0.105 (n=170) | REJECTED | below_safety_margin(11885<20912), p_lower_below_threshold(0.10<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001405 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0105 €) | — | 1.00 | 0.105 (n=170) | REJECTED | below_safety_margin(14<28), p_lower_below_threshold(0.10<0.75) |
| 52855680 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 84.613405 USDC | 0.018485 USDC | 0.000000 USDC | 0.007212 USDC | 0.011273 USDC (0.0104 €) | — | 1.33 | 0.105 (n=170) | REJECTED | below_safety_margin(11273<16922), p_lower_below_threshold(0.10<0.75) |
| 52855680 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.035564 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0104 €) | — | 1.32 | 0.105 (n=170) | REJECTED | below_safety_margin(4702508601311<7112792044539), p_lower_below_threshold(0.10<0.75) |
| 52855680 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 87.399957 USDC | 0.018089 USDC | 0.000000 USDC | 0.007212 USDC | 0.010877 USDC (0.0100 €) | — | 1.24 | 0.105 (n=170) | REJECTED | below_safety_margin(10877<17479), p_lower_below_threshold(0.10<0.75) |
| 52855680 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.036623 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0100 €) | — | 1.24 | 0.105 (n=170) | REJECTED | below_safety_margin(4536792122586<7324657206735), p_lower_below_threshold(0.10<0.75) |
| 52855680 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001150 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.52 | 0.105 (n=170) | REJECTED | below_safety_margin(6<22), p_lower_below_threshold(0.10<0.75) |
| 52855680 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001576 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.38 | 0.002 (n=5) | REJECTED | below_safety_margin(6<31), reliability_not_demonstrated |
| 52855680 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.030290 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.64 | 0.105 (n=170) | REJECTED | below_safety_margin(1935056188454<6058086925961), p_lower_below_threshold(0.10<0.75) |
| 52855680 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 80.815561 USDC | 0.012105 USDC | 0.000000 USDC | 0.007575 USDC | 0.004530 USDC (0.0042 €) | — | 0.56 | 0.105 (n=170) | REJECTED | below_safety_margin(4530<16163), p_lower_below_threshold(0.10<0.75) |
| 52855680 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 118.443396 USDC | 0.011526 USDC | 0.000000 USDC | 0.007212 USDC | 0.004314 USDC (0.0040 €) | — | 0.36 | 0.002 (n=5) | REJECTED | below_safety_margin(4314<23688), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1413 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
