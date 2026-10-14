# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T12:42:39+00:00 ; durée 196.34 min ; blocs 52590312 → 52596201 (5845 vus)

## Connexion
- Requêtes RPC : 77669 ; erreurs : 0 ; latence p50/p95 : 266.2/672.7 ms
- Rafraîchissements d'état : 5846 ; âge des données au dernier bloc : 1.79 s ; changements de frais LP observés (pools à frais dynamiques) : 12255
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 158220 ; cycles déclenchés par événement : 6452 ; avance médiane sur le rafraîchissement multicall : 361 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,483.27 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 584 pools, 329 jetons, 21950 routes
- Par DEX : uniswap_v3 142, aerodrome 236, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3924 (énumérés 395, par paires 0), mesurés 586, sous le plancher de 10000.0 $ : 2 → gardés 584 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2506.12853, 'AERO': 0.905993, 'cbBTC': 83225.723803}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,986,924 | 2,483.266883 | 52596201 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,594,826 | 1.122810 | 52596201 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,222,308 | 0.029999 | 52596201 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,117,310 | 109.146919 | 52596201 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,283,657 | 0.029966 | 52596201 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,639,372 | 0.029951 | 52596201 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,353,495 | 2,479.060137 | 52596201 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,278,551 | 0.000012 | 52596201 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,077,748 | 2,483.055011 | 52596201 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 8,114,287 | 0.000012 | 52596201 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 833 | 7,899,346 | 2,478.499845 | 52596201 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,271,073 | 0.001670 | 52596201 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 6,624,046 | 0.000012 | 52596201 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,521,542 | 0.029987 | 52596201 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,484,743 | 1.000859 | 52596201 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,363,748 | 0.026511 | 52596201 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,723,970 | 0.000279 | 52596201 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,683,330 | 0.802388 | 52596201 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,467,781 | 2,478.845415 | 52596201 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,394,370 | 0.998938 | 52596201 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,134,483 | 34,215.480931 | 52596201 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,681,076 | 2,764.678167 | 52596201 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,004,529 | 1.141636 | 52596201 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,856,506 | 0.000012 | 52596201 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2751 | 2,596,790 | 109.173922 | 52596201 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,531,002 | 0.000011 | 52596201 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,495,364 | 1.114852 | 52596201 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/FAI | 10000 | 2,430,133 | 1,060,017.930553 | 52596201 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,378,860 | 406.184916 | 52596201 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/USDT | 466 | 2,350,730 | 2,481.295154 | 52596201 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,118,698 | 0.000000 | 52596201 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,951 | 1.189914 | 52596201 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 2,092,026 | 1,072.368746 | 52596201 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | fBOMB/USDbC | 10000 | 2,033,410 | 0.023922 | 52596201 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,945,253 | 0.916707 | 52596201 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,868,044 | 15.718781 | 52596201 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,859,884 | 1.371858 | 52596201 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,778,985 | 0.019097 | 52596201 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,762,921 | 0.000012 | 52596201 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,702,263 | 13,556.954636 | 52596201 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,664,655 | 2.306880 | 52596201 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,552,088 | 2,786.969480 | 52596201 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,535,324 | 1.105776 | 52596201 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,930 | 0.835722 | 52596201 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,448,079 | 0.000000 | 52596201 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,387,533 | 0.000278 | 52596201 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/AERO | 3028 | 1,378,185 | 2,783.113165 | 52596201 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,372,849 | 0.004815 | 52596201 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | EURC/USDC | 82 | 1,304,503 | 1.113861 | 52596201 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,286,642 | 23.451707 | 52596201 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,267,185 | 32,968,616.263544 | 52596201 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,262,173 | 2,479.061379 | 52596201 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,247,381 | 62.451789 | 52596201 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,230,134 | 1.105594 | 52596201 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,215,840 | 1.131665 | 52596201 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/EDEL | 7000 | 1,207,249 | 72,988.584324 | 52596201 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,196,573 | 483,670.332625 | 52596201 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,183,344 | 1,194,163.262045 | 52596201 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,168,290 | 46.172843 | 52596201 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,116,291 | 14.173192 | 52596201 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 12297 ; routes examinées : 269919150 ; candidats optimisés : 1423515 ; net attendu > 0 : 2336 ; dernier cycle 81.4 ms
- Rejets (moteur) : {'spread_below_threshold': 265818078, 'liquidity_below_min': 2290331, 'negative_expected_net': 1421179, 'borrow_bound_too_small': 307425, 'cycle_budget_exhausted': 55207, 'unquotable': 24594}
- Enregistrements de la session : 1423515 ; net attendu > 0 : 2336 ; simulés (eth_call de la vraie tx) : 75 (ok 48, échec 27) ; étiquettes ghost N+1 : 12/58 positives
- Décisions : {'REJECTED': 1423515} ; motifs de rejet : {'below_safety_margin': 888, 'negative_expected_net': 1421179, 'reliability_not_demonstrated': 2336, 'simulation_failed': 27}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52591461 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 4.060766 WETH | 0.005574 WETH | 0.000000 WETH | 0.000003 WETH | 0.005572 WETH (12.8002 €) | — | 13.72 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.120287 cbBTC | 0.000167 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000166 cbBTC (12.7602 €) | — | 13.84 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 3.396471 WETH | 0.002780 WETH | 0.000000 WETH | 0.000004 WETH | 0.002776 WETH (6.3600 €) | — | 8.17 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.100054 cbBTC | 0.000083 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000083 cbBTC (6.3572 €) | — | 8.29 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 8,421.081624 USDC | 6.911616 USDC | 0.000000 USDC | 0.010892 USDC | 6.900724 USDC (6.3487 €) | — | 8.19 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 3.359749 WETH | 0.002767 WETH | 0.000000 WETH | 0.000004 WETH | 0.002762 WETH (6.3461 €) | — | 8.22 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.099416 cbBTC | 0.000083 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000083 cbBTC (6.3272 €) | — | 8.30 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 8,421.081624 USDC | 6.877173 USDC | 0.000000 USDC | 0.010921 USDC | 6.866252 USDC (6.3170 €) | — | 8.15 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.344257 WETH | 0.002578 WETH | 0.000000 WETH | 0.000003 WETH | 0.002575 WETH (5.9158 €) | — | 7.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.098050 cbBTC | 0.000077 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000077 cbBTC (5.8979 €) | — | 7.85 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.790945 WETH | 0.002564 WETH | 0.000000 WETH | 0.000004 WETH | 0.002560 WETH (5.8664 €) | — | 6.75 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.112756 cbBTC | 0.000077 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000077 cbBTC (5.8636 €) | — | 6.79 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 9,526.367052 USDC | 6.374898 USDC | 0.000000 USDC | 0.010513 USDC | 6.364385 USDC (5.8552 €) | — | 6.68 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.798303 WETH | 0.002549 WETH | 0.000000 WETH | 0.000004 WETH | 0.002545 WETH (5.8470 €) | — | 6.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.112948 cbBTC | 0.000076 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000076 cbBTC (5.8304 €) | — | 6.73 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 9,459.488712 USDC | 6.336151 USDC | 0.000000 USDC | 0.010542 USDC | 6.325609 USDC (5.8196 €) | — | 6.69 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 4.383100 WETH | 0.002288 WETH | 0.000000 WETH | 0.000003 WETH | 0.002285 WETH (5.2487 €) | — | 5.21 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10,891.997010 USDC | 5.686515 USDC | 0.000000 USDC | 0.008265 USDC | 5.678250 USDC (5.2240 €) | — | 5.21 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 2.460880 WETH | 0.002090 WETH | 0.000000 WETH | 0.000003 WETH | 0.002087 WETH (4.7807 €) | — | 8.48 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 6,115.785412 USDC | 5.195578 USDC | 0.000000 USDC | 0.007864 USDC | 5.187714 USDC (4.7727 €) | — | 8.48 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 2.454511 WETH | 0.002080 WETH | 0.000000 WETH | 0.000003 WETH | 0.002077 WETH (4.7707 €) | — | 8.46 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 6,101.302985 USDC | 5.170641 USDC | 0.000000 USDC | 0.007886 USDC | 5.162755 USDC (4.7497 €) | — | 8.46 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.678239 WETH | 0.001980 WETH | 0.000000 WETH | 0.000004 WETH | 0.001976 WETH (4.5272 €) | — | 5.37 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.108217 cbBTC | 0.000059 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000059 cbBTC (4.5248 €) | — | 5.46 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 9,085.107890 USDC | 4.921764 USDC | 0.000000 USDC | 0.010135 USDC | 4.911629 USDC (4.5187 €) | — | 5.41 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 79 ; taux observé 0.190 ; borne inférieure crédible (0.9) 0.139 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 13.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
