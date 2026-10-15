# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T20:51:57+00:00 ; durée 107.76 min ; blocs 52650847 → 52654081 (2710 vus)

## Connexion
- Requêtes RPC : 33004 ; erreurs : 685 ; latence p50/p95 : 140.3/2,034.9 ms
- Rafraîchissements d'état : 2710 ; âge des données au dernier bloc : 4.99 s ; changements de frais LP observés (pools à frais dynamiques) : 5653
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4 ; cycles déclenchés par événement : 3 ; avance médiane sur le rafraîchissement multicall : 25,539 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,455.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21444 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 154, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3921 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 3 → gardés 573 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2444.445842, 'AERO': 0.898266, 'cbBTC': 82361.329534}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,940,733 | 2,455.773327 | 52654081 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,675,589 | 1.100737 | 52654081 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,495,070 | 0.029885 | 52654081 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,790,463 | 98.204289 | 52654081 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,179,331 | 0.029833 | 52654081 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,608,572 | 0.029819 | 52654081 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,750,804 | 0.000012 | 52654081 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,161,344 | 2,453.125351 | 52654081 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 368 | 7,991,920 | 0.000012 | 52654081 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 758 | 7,728,525 | 2,453.528461 | 52654081 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,241,286 | 0.001682 | 52654081 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 7,157,335 | 0.000012 | 52654081 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,183,759 | 1.106340 | 52654081 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,454,875 | 2,457.352663 | 52654081 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,396,614 | 0.029897 | 52654081 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,370,063 | 0.024882 | 52654081 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,811,827 | 0.802398 | 52654081 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,763,282 | 0.000278 | 52654081 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,392,702 | 2,453.542159 | 52654081 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,335,448 | 0.997995 | 52654081 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 454 | 4,256,610 | 2,456.523793 | 52654081 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 3,985,310 | 36,014.369677 | 52654081 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,547,411 | 2,717.026082 | 52654081 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,857,268 | 403.826808 | 52654081 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,847,055 | 0.000012 | 52654081 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,764,550 | 0.000011 | 52654081 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,687,709 | 98.242826 | 52654081 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,553,756 | 1.141722 | 52654081 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome | WETH/FAI | 10000 | 2,281,382 | 1,176,270.195541 | 52654081 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,377 | 1.196132 | 52654081 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,083,216 | 0.000000 | 52654081 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52654081 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,932,485 | 15.689864 | 52654081 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,817,758 | 0.022587 | 52654081 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,603 | 0.019023 | 52654081 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,779,581 | 0.000012 | 52654081 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,712,337 | 13,537.943516 | 52654081 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,694,179 | 2.310794 | 52654081 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,571,813 | 2,704.986854 | 52654081 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,518,383 | 1.105497 | 52654081 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,497,458 | 0.916551 | 52654081 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,445 | 0.830186 | 52654081 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,453,768 | 2,703.584254 | 52654081 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,394,120 | 0.000000 | 52654081 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,374,644 | 0.004830 | 52654081 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,345,242 | 23.248367 | 52654081 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,335,025 | 0.000279 | 52654081 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,326,992 | 1.121894 | 52654081 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,248,937 | 62.296194 | 52654081 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,233,950 | 2,453.130155 | 52654081 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,224,203 | 34,858,596.145764 | 52654081 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,219,426 | 0.029816 | 52654081 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,218,160 | 1.105591 | 52654081 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,215,427 | 0.886359 | 52654081 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,196,006 | 1,143,300.017384 | 52654081 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,170,193 | 498,440.584433 | 52654081 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,165,252 | 0.436872 | 52654081 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,134,294 | 13.627966 | 52654081 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,123,507 | 83,165.165293 | 52654081 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,085,205 | 53.514353 | 52654081 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 2712 ; routes examinées : 58156128 ; candidats optimisés : 346123 ; net attendu > 0 : 112 ; dernier cycle 288.8 ms
- Rejets (moteur) : {'spread_below_threshold': 57230967, 'liquidity_below_min': 570730, 'negative_expected_net': 346011, 'cycle_budget_exhausted': 5504, 'borrow_bound_too_small': 2712}
- Enregistrements de la session : 346123 ; net attendu > 0 : 112 ; simulés (eth_call de la vraie tx) : 6 (ok 6, échec 0) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 346123} ; motifs de rejet : {'below_safety_margin': 80, 'negative_expected_net': 346011, 'p_lower_below_threshold': 51, 'reliability_not_demonstrated': 61, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52651372 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 199.591538 USDC | 0.055396 USDC | 0.000000 USDC | 0.007374 USDC | 0.048022 USDC (0.0442 €) | — | 2.41 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.081382 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0440 €) | 0.000020 WETH | 2.40 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001652 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0288 €) | — | 2.30 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 143.482480 USDC | 0.038444 USDC | 0.000000 USDC | 0.007374 USDC | 0.031070 USDC (0.0286 €) | — | 2.17 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.058126 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0280 €) | 0.000012 WETH | 2.14 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 45.757782 USDC | 0.022825 USDC | 0.000000 USDC | 0.007036 USDC | 0.015789 USDC (0.0145 €) | — | 3.45 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.018813 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0145 €) | 0.000006 WETH | 3.41 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52651372 | USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 40.516789 USDC | 0.021229 USDC | 0.000000 USDC | 0.007374 USDC | 0.013855 USDC (0.0127 €) | — | 3.42 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH | 0.016648 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0127 €) | — | 3.38 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52651372 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 32.066029 USDC | 0.017671 USDC | 0.000000 USDC | 0.007036 USDC | 0.010635 USDC (0.0098 €) | — | 3.32 | 0.008 (n=38) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52651372 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.013070 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0097 €) | — | 3.31 | 0.008 (n=38) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52651372 | USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 30.055472 USDC | 0.017279 USDC | 0.000000 USDC | 0.007374 USDC | 0.009905 USDC (0.0091 €) | — | 3.30 | 0.244 (n=22) | REJECTED | reliability_not_demonstrated |
| 52651372 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH | 0.012291 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0091 €) | — | 3.27 | 0.244 (n=22) | REJECTED | reliability_not_demonstrated |
| 52651372 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 37.938496 USDC | 0.015405 USDC | 0.000000 USDC | 0.007036 USDC | 0.008369 USDC (0.0077 €) | — | 2.21 | 0.151 (n=10) | REJECTED | reliability_not_demonstrated |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.015548 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0077 €) | — | 2.18 | 0.151 (n=10) | REJECTED | reliability_not_demonstrated |
| 52651372 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 49.975566 USDC | 0.015592 USDC | 0.000000 USDC | 0.007374 USDC | 0.008218 USDC (0.0076 €) | — | 1.64 | 0.080 (n=45) | REJECTED | below_safety_margin(8218<9995), p_lower_below_threshold(0.08<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.020337 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0075 €) | — | 1.64 | 0.080 (n=45) | REJECTED | below_safety_margin(3333735924263<4067342478717), p_lower_below_threshold(0.08<0.75) |
| 52651373 | USDC→[aerodrome]→OVER→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 19.664202 USDC | 0.014349 USDC | 0.000000 USDC | 0.006723 USDC | 0.007626 USDC (0.0070 €) | — | 3.88 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52651373 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→OVER→[aerodrome]→WETH | 0.008074 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0070 €) | 0.000003 WETH | 3.83 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52651372 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000522 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0068 €) | — | 1.72 | 0.080 (n=45) | REJECTED | below_safety_margin(9<10), p_lower_below_threshold(0.08<0.75) |
| 52651372 | USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 33.993600 USDC | 0.014616 USDC | 0.000000 USDC | 0.007374 USDC | 0.007242 USDC (0.0067 €) | — | 2.13 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH | 0.013880 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0066 €) | — | 2.12 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 43.445532 USDC | 0.014290 USDC | 0.000000 USDC | 0.007374 USDC | 0.006916 USDC (0.0064 €) | — | 1.59 | 0.282 (n=31) | REJECTED | below_safety_margin(6916<8689), p_lower_below_threshold(0.28<0.75) |
| 52651372 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.017763 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0063 €) | — | 1.58 | 0.282 (n=31) | REJECTED | below_safety_margin(2806582179664<3552507083952), p_lower_below_threshold(0.28<0.75) |
| 52651373 | USDC→[aerodrome]→OVER→[aerodrome]→WETH→[uniswap_v3]→USDC | 18.715192 USDC | 0.013098 USDC | 0.000000 USDC | 0.006723 USDC | 0.006375 USDC (0.0059 €) | — | 3.41 | 0.008 (n=38) | REJECTED | p_lower_below_threshold(0.01<0.75) |

## Fiabilité et décision
- Observations ghost : 390 ; taux observé 0.149 ; borne inférieure crédible (0.9) 0.127 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
