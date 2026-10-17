# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T09:18:37+00:00 ; durée 276.42 min ; blocs 52711390 → 52719679 (8172 vus)

## Connexion
- Requêtes RPC : 110784 ; erreurs : 63 ; latence p50/p95 : 183.3/636.4 ms
- Rafraîchissements d'état : 8172 ; âge des données au dernier bloc : 2.68 s ; changements de frais LP observés (pools à frais dynamiques) : 8443
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 89703 ; cycles déclenchés par événement : 8791 ; avance médiane sur le rafraîchissement multicall : 294 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,427.74 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 329 jetons, 21010 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 393, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2421.248535, 'AERO': 0.878353, 'cbBTC': 81453.278136}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,427,537 | 2,427.738234 | 52719680 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,993,420 | 1.129168 | 52719680 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,282,992 | 0.029807 | 52719680 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,578,871 | 0.029752 | 52719680 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,080,752 | 104.720399 | 52719680 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,463,299 | 0.029738 | 52719680 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,760,429 | 0.000012 | 52719680 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,126,650 | 2,432.745281 | 52719680 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 579 | 8,588,757 | 2,432.225535 | 52719680 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,843,302 | 0.000012 | 52719680 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 7,262,148 | 0.000012 | 52719680 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,169,919 | 0.001678 | 52719680 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,420,873 | 2,432.895024 | 52719680 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,409,751 | 1.128125 | 52719680 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,384,062 | 0.025281 | 52719680 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,349,315 | 0.029799 | 52719680 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,272,005 | 1.000855 | 52719680 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,852,583 | 0.802398 | 52719680 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,696,893 | 0.000276 | 52719680 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,481,081 | 2,432.136901 | 52719680 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,422,669 | 0.998803 | 52719680 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,060,701 | 33,901.990356 | 52719680 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 403 | 4,018,357 | 2,436.423257 | 52719680 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,477,563 | 2,742.965571 | 52719680 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,925,406 | 1.141834 | 52719680 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,838,689 | 0.000012 | 52719680 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,757,975 | 0.000011 | 52719680 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,608,009 | 104.698585 | 52719680 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,386,047 | 1,026.755834 | 52719680 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,314,325 | 401.667767 | 52719680 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,272,332 | 1,158,742.078326 | 52719680 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,126,172 | 1.123518 | 52719680 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,805 | 1.197614 | 52719680 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,044,491 | 15.589781 | 52719680 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,000,248 | 1.415889 | 52719680 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,831,048 | 0.022354 | 52719680 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,818,888 | 0.000000 | 52719680 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,897 | 0.000012 | 52719680 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,752,005 | 0.018398 | 52719680 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,679,103 | 2.307070 | 52719680 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,551,658 | 0.916550 | 52719680 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,550,650 | 2,741.289028 | 52719680 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,525,644 | 2,740.569401 | 52719680 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,520,835 | 1.105495 | 52719680 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,347 | 0.826570 | 52719680 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,408,109 | 13,468.299057 | 52719680 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,363,360 | 0.000000 | 52719680 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,355,137 | 0.004867 | 52719680 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,322,237 | 0.435528 | 52719680 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,316,343 | 0.000274 | 52719680 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,263,020 | 23.265369 | 52719680 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299956 | 52719680 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,228,173 | 1.131607 | 52719680 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,208,248 | 35,143,315.521442 | 52719680 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,207,346 | 0.029733 | 52719680 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,205,349 | 1.105714 | 52719680 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,201,098 | 2,432.856751 | 52719680 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,185,545 | 1,137,165.396017 | 52719680 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,153,541 | 501,861.019050 | 52719680 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,123,096 | 13.974219 | 52719680 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 16962 ; routes examinées : 356371620 ; candidats optimisés : 1869995 ; net attendu > 0 : 277 ; dernier cycle 113.7 ms
- Rejets (moteur) : {'spread_below_threshold': 351793114, 'liquidity_below_min': 2518870, 'negative_expected_net': 1869718, 'unquotable': 166397, 'borrow_bound_too_small': 16954, 'pool_quarantined': 5390, 'cycle_budget_exhausted': 900}
- Enregistrements de la session : 1869995 ; net attendu > 0 : 277 ; simulés (eth_call de la vraie tx) : 48 (ok 16, échec 32) ; étiquettes ghost N+1 : 0/35 positives
- Décisions : {'REJECTED': 1869995} ; motifs de rejet : {'below_safety_margin': 160, 'negative_expected_net': 1869718, 'p_lower_below_threshold': 183, 'reliability_not_demonstrated': 94, 'simulation_failed': 32, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52717343 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 171.681101 USDC | 0.431738 USDC | 0.000000 USDC | 0.005454 USDC | 0.426284 USDC (0.3922 €) | — | 24.83 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714900 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 159.449852 USDC | 0.353632 USDC | 0.000000 USDC | 0.005449 USDC | 0.348183 USDC (0.3203 €) | — | 21.84 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714406 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.016230 WETH | 0.000056 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1209 €) | — | 33.40 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52713483 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 88.741675 USDC | 0.113607 USDC | 0.000000 USDC | 0.005439 USDC | 0.108168 USDC (0.0995 €) | — | 12.19 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.036579 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0957 €) | 0.000043 WETH | 11.74 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.036579 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0957 €) | — | 11.74 | 0.042 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.036393 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0947 €) | 0.000043 WETH | 11.68 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.036393 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0947 €) | — | 11.68 | 0.042 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 138.240203 USDC | 0.094365 USDC | 0.000000 USDC | 0.007281 USDC | 0.087084 USDC (0.0801 €) | — | 6.30 | 0.110 (n=69) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52714063 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 138.240203 USDC | 0.094365 USDC | 0.000000 USDC | 0.007281 USDC | 0.087084 USDC (0.0801 €) | — | 6.30 | 0.110 (n=69) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52714063 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001778 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0800 €) | — | 6.02 | 0.110 (n=69) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52714063 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001778 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0800 €) | — | 6.02 | 0.110 (n=69) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52714063 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.033968 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0738 €) | 0.000033 WETH | 9.75 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.033968 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0738 €) | — | 9.75 | 0.042 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 108.176005 USDC | 0.084924 USDC | 0.000000 USDC | 0.006947 USDC | 0.077977 USDC (0.0717 €) | — | 7.21 | 0.013 (n=64) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52714063 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 108.176005 USDC | 0.084924 USDC | 0.000000 USDC | 0.006947 USDC | 0.077977 USDC (0.0717 €) | — | 7.21 | 0.013 (n=64) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52715594 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 76.615035 USDC | 0.082577 USDC | 0.000000 USDC | 0.005445 USDC | 0.077132 USDC (0.0710 €) | — | 10.07 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 75.153821 USDC | 0.080784 USDC | 0.000000 USDC | 0.006947 USDC | 0.073837 USDC (0.0679 €) | — | 9.82 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 75.153821 USDC | 0.080784 USDC | 0.000000 USDC | 0.006947 USDC | 0.073837 USDC (0.0679 €) | — | 9.82 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52716618 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 70.827384 USDC | 0.073103 USDC | 0.000000 USDC | 0.005456 USDC | 0.067647 USDC (0.0622 €) | — | 9.55 | 0.002 (n=3) | REJECTED | stale_data(7796ms>4000.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 67.381396 USDC | 0.071950 USDC | 0.000000 USDC | 0.006947 USDC | 0.065003 USDC (0.0598 €) | — | 9.65 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 67.381396 USDC | 0.071950 USDC | 0.000000 USDC | 0.006947 USDC | 0.065003 USDC (0.0598 €) | — | 9.65 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001452 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0583 €) | — | 5.37 | 0.233 (n=30) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 52714063 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001452 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0583 €) | — | 5.37 | 0.233 (n=30) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 52714063 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 123.508528 USDC | 0.070318 USDC | 0.000000 USDC | 0.007281 USDC | 0.063037 USDC (0.0580 €) | — | 5.10 | 0.233 (n=30) | REJECTED | p_lower_below_threshold(0.23<0.75) |

## Fiabilité et décision
- Observations ghost : 699 ; taux observé 0.124 ; borne inférieure crédible (0.9) 0.109 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
