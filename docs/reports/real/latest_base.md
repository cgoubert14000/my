# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T07:36:29+00:00 ; durée 174.28 min ; blocs 52711390 → 52716616 (5190 vus)

## Connexion
- Requêtes RPC : 69475 ; erreurs : 58 ; latence p50/p95 : 229.6/747.2 ms
- Rafraîchissements d'état : 5191 ; âge des données au dernier bloc : 0.97 s ; changements de frais LP observés (pools à frais dynamiques) : 5532
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 52578 ; cycles déclenchés par événement : 4985 ; avance médiane sur le rafraîchissement multicall : 296 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,427.74 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 329 jetons, 21010 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 393, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2421.248535, 'AERO': 0.878353, 'cbBTC': 81453.278136}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,432,466 | 2,427.740457 | 52716617 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,069,121 | 1.125357 | 52716617 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,280,896 | 0.029812 | 52716617 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,607,743 | 0.029752 | 52716617 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,062,771 | 104.879197 | 52716617 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,445,993 | 0.029738 | 52716617 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,758,752 | 0.000012 | 52716617 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 9,192,911 | 0.000012 | 52716617 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 9,125,894 | 2,432.743804 | 52716617 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 7,842,789 | 0.000012 | 52716617 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,172,796 | 0.001680 | 52716617 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,087,905 | 2,433.423990 | 52716617 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,421,799 | 1.128118 | 52716617 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,420,873 | 2,430.689822 | 52716617 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,378,130 | 0.025281 | 52716617 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,350,071 | 0.029808 | 52716617 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,272,010 | 1.000855 | 52716617 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,852,588 | 0.802398 | 52716617 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,696,806 | 0.000276 | 52716617 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,421,949 | 0.998803 | 52716617 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,401,545 | 2,433.608269 | 52716617 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,056,374 | 33,974.422859 | 52716617 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,483,444 | 2,742.235434 | 52716617 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,925,407 | 1.141834 | 52716617 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,838,409 | 0.000012 | 52716617 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,717,240 | 401.226821 | 52716617 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,677,085 | 0.000011 | 52716617 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,606,598 | 1,024.216467 | 52716617 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,605,854 | 104.848803 | 52716617 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,272,334 | 1,158,742.078326 | 52716617 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,110,297 | 1.123724 | 52716617 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,407 | 1.197840 | 52716617 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/USDT | 400 | 2,075,970 | 2,436.242441 | 52716617 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,000,248 | 1.415889 | 52716617 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,848,060 | 15.589863 | 52716617 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,825,796 | 0.022229 | 52716617 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,818,921 | 0.000000 | 52716617 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,086 | 0.000012 | 52716617 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,750,515 | 0.018374 | 52716617 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,679,170 | 2.306979 | 52716617 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,665,945 | 13,459.610095 | 52716617 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,551,659 | 0.916550 | 52716617 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,550,617 | 2,732.097234 | 52716617 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3004 | 1,527,928 | 2,731.381087 | 52716617 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,520,835 | 1.105495 | 52716617 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,637 | 0.826245 | 52716617 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,363,368 | 0.000000 | 52716617 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,343,431 | 0.004762 | 52716617 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,322,237 | 0.435528 | 52716617 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,316,323 | 0.000275 | 52716617 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,265,250 | 23.260894 | 52716617 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299956 | 52716617 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,231,019 | 1.131603 | 52716617 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,212,236 | 34,801,915.098400 | 52716617 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,207,248 | 0.029732 | 52716617 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,206,450 | 1.105712 | 52716617 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,193,257 | 2,432.725160 | 52716617 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,185,826 | 1,136,628.171484 | 52716617 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,155,481 | 499,567.970432 | 52716617 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,124,469 | 13.925711 | 52716617 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 10174 ; routes examinées : 213755740 ; candidats optimisés : 1369402 ; net attendu > 0 : 244 ; dernier cycle 122.1 ms
- Rejets (moteur) : {'spread_below_threshold': 210774822, 'liquidity_below_min': 1571694, 'negative_expected_net': 1369158, 'unquotable': 27684, 'borrow_bound_too_small': 10169, 'pool_quarantined': 1366, 'cycle_budget_exhausted': 603}
- Enregistrements de la session : 1369402 ; net attendu > 0 : 244 ; simulés (eth_call de la vraie tx) : 32 (ok 12, échec 20) ; étiquettes ghost N+1 : 0/22 positives
- Décisions : {'REJECTED': 1369402} ; motifs de rejet : {'below_safety_margin': 143, 'negative_expected_net': 1369158, 'p_lower_below_threshold': 177, 'reliability_not_demonstrated': 67, 'simulation_failed': 20, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
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
| 52714063 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 67.381396 USDC | 0.071950 USDC | 0.000000 USDC | 0.006947 USDC | 0.065003 USDC (0.0598 €) | — | 9.65 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 67.381396 USDC | 0.071950 USDC | 0.000000 USDC | 0.006947 USDC | 0.065003 USDC (0.0598 €) | — | 9.65 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001452 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0583 €) | — | 5.37 | 0.233 (n=30) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 52714063 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001452 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0583 €) | — | 5.37 | 0.233 (n=30) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 52714063 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 123.508528 USDC | 0.070318 USDC | 0.000000 USDC | 0.007281 USDC | 0.063037 USDC (0.0580 €) | — | 5.10 | 0.233 (n=30) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 52714063 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 123.508528 USDC | 0.070318 USDC | 0.000000 USDC | 0.007281 USDC | 0.063037 USDC (0.0580 €) | — | 5.10 | 0.233 (n=30) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 52714063 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→AERO→[uniswap_v3]→USDC | 88.089406 USDC | 0.068831 USDC | 0.000000 USDC | 0.006947 USDC | 0.061884 USDC (0.0569 €) | — | 7.03 | 0.013 (n=64) | REJECTED | p_lower_below_threshold(0.01<0.75) |

## Fiabilité et décision
- Observations ghost : 686 ; taux observé 0.127 ; borne inférieure crédible (0.9) 0.111 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.1% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
