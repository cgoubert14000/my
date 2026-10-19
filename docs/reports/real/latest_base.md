# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T08:38:01+00:00 ; durée 70.63 min ; blocs 52802745 → 52804864 (2117 vus)

## Connexion
- Requêtes RPC : 27688 ; erreurs : 3 ; latence p50/p95 : 165.9/725.0 ms
- Rafraîchissements d'état : 2117 ; âge des données au dernier bloc : 4.06 s ; changements de frais LP observés (pools à frais dynamiques) : 4359
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12407 ; cycles déclenchés par événement : 1110 ; avance médiane sur le rafraîchissement multicall : 290 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,433.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 328 jetons, 21198 routes
- Par DEX : uniswap_v3 138, aerodrome 234, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2427.085029, 'AERO': 0.802709, 'cbBTC': 82780.001526}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,992,025 | 2,433.419163 | 52804865 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,339,981 | 1.257038 | 52804865 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,661,693 | 0.029379 | 52804865 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,429,662 | 0.029404 | 52804865 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,305,883 | 102.155805 | 52804865 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,486,551 | 0.029365 | 52804865 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,842,148 | 0.000012 | 52804865 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,488,697 | 2,434.942097 | 52804865 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 7,850,047 | 0.000012 | 52804865 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 743 | 7,433,853 | 2,435.699001 | 52804865 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,262,766 | 0.001668 | 52804865 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 6,806,953 | 0.000012 | 52804865 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,501,588 | 2,434.590809 | 52804865 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,391,093 | 0.029409 | 52804865 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,284,342 | 1.000854 | 52804865 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,915,440 | 0.025847 | 52804865 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 433 | 4,907,099 | 2,438.366214 | 52804865 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,864,096 | 0.802398 | 52804865 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,676,100 | 0.000273 | 52804865 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,472,776 | 2,435.721049 | 52804865 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,384,903 | 0.998772 | 52804865 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,113,735 | 33,188.300563 | 52804865 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,288,412 | 3,042.010740 | 52804865 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,073,497 | 1.251298 | 52804865 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,932,513 | 1.141829 | 52804865 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,866,958 | 0.000012 | 52804865 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2718 | 2,840,556 | 983.158551 | 52804865 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,658,784 | 102.183778 | 52804865 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,521,795 | 0.000010 | 52804865 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,380,077 | 405.792872 | 52804865 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,242,624 | 1,195,220.787603 | 52804865 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,890 | 1.233041 | 52804865 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,045,265 | 0.000000 | 52804865 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52804865 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,986,490 | 15.889945 | 52804865 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,883,865 | 13,806.726139 | 52804865 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,784,995 | 0.000012 | 52804865 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,759,562 | 1.105523 | 52804865 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,757,457 | 0.018511 | 52804865 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | fBOMB/USDC | 10000 | 1,731,155 | 0.020723 | 52804865 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,679,308 | 2.310770 | 52804865 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,620,921 | 3,059.172326 | 52804865 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 79 | 1,477,601 | 1.121066 | 52804865 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,476,382 | 0.916352 | 52804865 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,738 | 0.827106 | 52804865 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,340,627 | 0.436773 | 52804865 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,330,174 | 0.000000 | 52804865 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,310,701 | 0.000273 | 52804865 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,293,868 | 0.004561 | 52804865 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,291,224 | 23.118248 | 52804865 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,288,546 | 0.029358 | 52804865 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,232,995 | 63.917537 | 52804865 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,225,732 | 1,068,621.946331 | 52804865 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,223,692 | 0.886320 | 52804865 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,214,628 | 2,434.930221 | 52804865 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,213,263 | 35,040,930.127724 | 52804865 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,141,718 | 519,758.450592 | 52804865 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,091,165 | 52.921898 | 52804865 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,085,778 | 15.202985 | 52804865 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,073,027 | 1.105810 | 52804865 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 3226 ; routes examinées : 68384748 ; candidats optimisés : 342570 ; net attendu > 0 : 55 ; dernier cycle 315.3 ms
- Rejets (moteur) : {'spread_below_threshold': 67353993, 'liquidity_below_min': 557522, 'negative_expected_net': 342515, 'pool_quarantined': 97812, 'borrow_bound_too_small': 32511, 'cycle_budget_exhausted': 340}
- Enregistrements de la session : 342570 ; net attendu > 0 : 55 ; simulés (eth_call de la vraie tx) : 12 (ok 2, échec 10) ; étiquettes ghost N+1 : 2/9 positives
- Décisions : {'REJECTED': 342570} ; motifs de rejet : {'below_safety_margin': 38, 'negative_expected_net': 342515, 'p_lower_below_threshold': 32, 'reliability_not_demonstrated': 23, 'simulation_failed': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52802789 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 103.887016 USDC | 0.252695 USDC | 0.000000 USDC | 0.005449 USDC | 0.247246 USDC (0.2275 €) | — | 23.80 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52802771 | WETH→[uniswap_v3]→NPC→[uniswap_v2]→WETH | 0.015606 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000024 WETH (0.0534 €) | — | 15.33 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52802789 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 20.416455 USDC | 0.042548 USDC | 0.000000 USDC | 0.005114 USDC | 0.037434 USDC (0.0344 €) | — | 18.34 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52802956 | USDC→[aerodrome]→MET→[aerodrome]→WETH→[uniswap_v3]→USDC | 49.367589 USDC | 0.035707 USDC | 0.000000 USDC | 0.006635 USDC | 0.029072 USDC (0.0267 €) | — | 5.89 | 0.031 (n=92) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52802956 | WETH→[uniswap_v3]→USDC→[aerodrome]→MET→[aerodrome]→WETH | 0.020334 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0266 €) | — | 5.86 | 0.031 (n=92) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 52802956 | USDC→[aerodrome]→MET→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 45.876940 USDC | 0.030372 USDC | 0.000000 USDC | 0.006635 USDC | 0.023737 USDC (0.0218 €) | — | 5.17 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52802956 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→MET→[aerodrome]→WETH | 0.018878 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0217 €) | — | 5.15 | 0.009 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52803331 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.227161 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(5909103348279<45432209893061), p_lower_below_threshold(0.10<0.75) |
| 52803331 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.227161 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(5909103348279<45432209893061), p_lower_below_threshold(0.10<0.75) |
| 52803331 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 547.409941 USDC | 0.022032 USDC | 0.000000 USDC | 0.007686 USDC | 0.014346 USDC (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(14346<109481), p_lower_below_threshold(0.10<0.75) |
| 52803331 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 547.409941 USDC | 0.022032 USDC | 0.000000 USDC | 0.007686 USDC | 0.014346 USDC (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(14346<109481), p_lower_below_threshold(0.10<0.75) |
| 52804839 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 26.372935 USDC | 0.016089 USDC | 0.000000 USDC | 0.005465 USDC | 0.010624 USDC (0.0098 €) | 0.010624 USDC | 4.03 | 0.000 (n=84) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52804839 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 26.372935 USDC | 0.016089 USDC | 0.000000 USDC | 0.005465 USDC | 0.010624 USDC (0.0098 €) | 0.010624 USDC | 4.03 | 0.000 (n=84) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52802956 | USDC→[aerodrome]→MET→[aerodrome]→WETH→[uniswap_v3]→USDC | 34.391612 USDC | 0.016977 USDC | 0.000000 USDC | 0.006635 USDC | 0.010342 USDC (0.0095 €) | — | 3.01 | 0.031 (n=92) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52802956 | WETH→[uniswap_v3]→USDC→[aerodrome]→MET→[aerodrome]→WETH | 0.014144 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0095 €) | — | 2.99 | 0.115 (n=59) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52802956 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 209.007372 USDC | 0.015592 USDC | 0.000000 USDC | 0.005451 USDC | 0.010141 USDC (0.0093 €) | — | 0.49 | 0.017 (n=49) | REJECTED | below_safety_margin(10141<41801), p_lower_below_threshold(0.02<0.75) |
| 52802956 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.086618 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0093 €) | — | 0.48 | 0.017 (n=49) | REJECTED | below_safety_margin(4153962327923<17323616190629), p_lower_below_threshold(0.02<0.75) |
| 52802956 | USDC→[aerodrome]→MET→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 31.222601 USDC | 0.014222 USDC | 0.000000 USDC | 0.006635 USDC | 0.007587 USDC (0.0070 €) | — | 2.43 | 0.053 (n=40) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 52802956 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→MET→[aerodrome]→WETH | 0.012910 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0069 €) | — | 2.40 | 0.053 (n=40) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 52802955 | USDC→[aerodrome]→MET→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 30.850837 USDC | 0.013801 USDC | 0.000000 USDC | 0.006625 USDC | 0.007176 USDC (0.0066 €) | — | 2.33 | 0.056 (n=38) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 52802955 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→MET→[aerodrome]→WETH | 0.012775 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0066 €) | — | 2.30 | 0.056 (n=38) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 52802825 | WETH→[uniswap_v3]→NPC→[uniswap_v2]→WETH | 0.006657 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0062 €) | — | 4.15 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52802818 | WETH→[uniswap_v3]→NPC→[uniswap_v2]→WETH | 0.006610 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0060 €) | — | 4.08 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52802955 | USDC→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 40.745436 USDC | 0.009653 USDC | 0.000000 USDC | 0.005116 USDC | 0.004537 USDC (0.0042 €) | — | 1.11 | 0.001 (n=6) | REJECTED | below_safety_margin(4537<8149), reliability_not_demonstrated |
| 52802955 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→cbBTC | 0.000474 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0038 €) | — | 1.05 | 0.001 (n=6) | REJECTED | below_safety_margin(5<9), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1264 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
