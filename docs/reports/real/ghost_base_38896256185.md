# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T12:48:41+00:00 ; durée 55.46 min ; blocs 52681120 → 52682785 (1638 vus)

## Connexion
- Requêtes RPC : 22405 ; erreurs : 0 ; latence p50/p95 : 117.4/1,016.3 ms
- Rafraîchissements d'état : 1639 ; âge des données au dernier bloc : 1.15 s ; changements de frais LP observés (pools à frais dynamiques) : 3767
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 31624 ; cycles déclenchés par événement : 1572 ; avance médiane sur le rafraîchissement multicall : 516 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,467.48 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 328 jetons, 21482 routes
- Par DEX : uniswap_v3 136, aerodrome 236 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 391, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2482.328501, 'AERO': 0.918334, 'cbBTC': 82582.444221}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52682811; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52682811

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,895,815 | 2,467.478874 | 52682785 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 46,893,517 | 1.095443 | 52682785 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 19,894,380 | 0.030036 | 52682785 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,628,973 | 0.030056 | 52682785 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,603,981 | 101.228950 | 52682785 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,573,212 | 0.030047 | 52682785 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,751,128 | 0.000012 | 52682785 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,190,814 | 2,465.026314 | 52682785 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 366 | 8,098,215 | 0.000012 | 52682785 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 833 | 7,688,381 | 2,464.631977 | 52682785 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,235,287 | 0.001682 | 52682785 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,665,342 | 0.000012 | 52682785 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,489,806 | 0.024802 | 52682785 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,475,375 | 2,467.860742 | 52682785 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,433,070 | 0.030055 | 52682785 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,272,575 | 1.000855 | 52682785 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,931,988 | 0.802398 | 52682785 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,800,748 | 0.000281 | 52682785 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,518,223 | 1.087587 | 52682785 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,361,053 | 0.998889 | 52682785 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,332,268 | 2,464.387052 | 52682785 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,087,616 | 34,561.310960 | 52682785 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,565,542 | 2,681.755196 | 52682785 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 451 | 3,094,492 | 2,468.357265 | 52682785 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,063,052 | 1.141839 | 52682785 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,846,351 | 0.000012 | 52682785 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,751,890 | 0.000011 | 52682785 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2772 | 2,683,510 | 101.241308 | 52682785 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,350,954 | 401.374582 | 52682785 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,315,908 | 1,152,367.436387 | 52682785 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,125,695 | 0.000000 | 52682785 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,750 | 1.195936 | 52682785 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,461 | 1.403757 | 52682785 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,880,933 | 15.236955 | 52682785 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,868,023 | 0.023288 | 52682785 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,779,332 | 0.018848 | 52682785 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,770,736 | 0.000012 | 52682785 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,704,223 | 2.311168 | 52682785 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,580,291 | 2,700.596484 | 52682785 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,533,753 | 0.916551 | 52682785 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,525,658 | 1.105492 | 52682785 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3012 | 1,498,168 | 2,700.795724 | 52682785 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,125 | 0.825814 | 52682785 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,423,005 | 13,341.693057 | 52682785 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,385,244 | 0.000000 | 52682785 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,375,554 | 0.004813 | 52682785 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,347,705 | 0.000280 | 52682785 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,347,020 | 1.124374 | 52682785 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,324,299 | 0.436891 | 52682785 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | USDC/SEND | 3000 | 1,249,107 | 62.279234 | 52682785 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,237,867 | 23.319305 | 52682785 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,224,818 | 35,313,335.067008 | 52682785 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,224,446 | 1.105591 | 52682785 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,221,766 | 0.030036 | 52682785 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,218,720 | 2,465.150413 | 52682785 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,216,650 | 1,115,386.891989 | 52682785 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,197,213 | 0.886457 | 52682785 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,177,754 | 496,085.125904 | 52682785 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,147,030 | 47.901165 | 52682785 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,143,300 | 81,119.943490 | 52682785 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 3210 ; routes examinées : 68957220 ; candidats optimisés : 388214 ; net attendu > 0 : 557 ; dernier cycle 261.2 ms
- Rejets (moteur) : {'spread_below_threshold': 67427670, 'liquidity_below_min': 754785, 'negative_expected_net': 387657, 'pool_quarantined': 382492, 'borrow_bound_too_small': 3204, 'cycle_budget_exhausted': 760}
- Enregistrements de la session : 388212 ; net attendu > 0 : 557 ; simulés (eth_call de la vraie tx) : 54 (ok 18, échec 36) ; étiquettes ghost N+1 : 3/26 positives
- Décisions : {'REJECTED': 388212} ; motifs de rejet : {'below_safety_margin': 411, 'negative_expected_net': 387655, 'p_lower_below_threshold': 480, 'price_impact': 385, 'reliability_not_demonstrated': 77, 'simulation_failed': 36}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52681235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.064584 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1574 €) | 0.000069 WETH | 10.67 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.064584 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1574 €) | 0.000069 WETH | 10.67 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681236 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.064584 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1574 €) | — | 10.67 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 159.458938 USDC | 0.178085 USDC | 0.000000 USDC | 0.007467 USDC | 0.170618 USDC (0.1570 €) | — | 10.70 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 159.458938 USDC | 0.178085 USDC | 0.000000 USDC | 0.007467 USDC | 0.170618 USDC (0.1570 €) | — | 10.70 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681236 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 159.458938 USDC | 0.178085 USDC | 0.000000 USDC | 0.007467 USDC | 0.170618 USDC (0.1570 €) | — | 10.70 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.060495 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1402 €) | 0.000061 WETH | 10.15 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52681235 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.060495 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1402 €) | 0.000061 WETH | 10.15 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52681236 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.060495 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1402 €) | — | 10.15 | 0.009 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 149.414789 USDC | 0.159068 USDC | 0.000000 USDC | 0.007125 USDC | 0.151943 USDC (0.1398 €) | — | 10.17 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 149.414789 USDC | 0.159068 USDC | 0.000000 USDC | 0.007125 USDC | 0.151943 USDC (0.1398 €) | — | 10.17 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52681236 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 149.414789 USDC | 0.159068 USDC | 0.000000 USDC | 0.007125 USDC | 0.151943 USDC (0.1398 €) | — | 10.17 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52681235 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061861 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1393 €) | 0.000061 WETH | 9.86 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061861 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1393 €) | 0.000061 WETH | 9.86 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52681236 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061861 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1393 €) | — | 9.86 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 152.667787 USDC | 0.158388 USDC | 0.000000 USDC | 0.007467 USDC | 0.150921 USDC (0.1388 €) | — | 9.89 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 152.667787 USDC | 0.158388 USDC | 0.000000 USDC | 0.007467 USDC | 0.150921 USDC (0.1388 €) | — | 9.89 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52681236 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 152.667787 USDC | 0.158388 USDC | 0.000000 USDC | 0.007467 USDC | 0.150921 USDC (0.1388 €) | — | 9.89 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061700 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1383 €) | — | 9.81 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061700 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1383 €) | — | 9.81 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681236 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061700 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1383 €) | — | 9.81 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 152.479110 USDC | 0.157286 USDC | 0.000000 USDC | 0.007467 USDC | 0.149819 USDC (0.1378 €) | — | 9.83 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 152.479110 USDC | 0.157286 USDC | 0.000000 USDC | 0.007467 USDC | 0.149819 USDC (0.1378 €) | — | 9.83 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681236 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 152.479110 USDC | 0.157286 USDC | 0.000000 USDC | 0.007467 USDC | 0.149819 USDC (0.1378 €) | — | 9.83 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061232 WETH | 0.000063 WETH | 0.000000 WETH | 0.000003 WETH | 0.000060 WETH (0.1362 €) | — | 9.74 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 539 ; taux observé 0.119 ; borne inférieure crédible (0.9) 0.102 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
