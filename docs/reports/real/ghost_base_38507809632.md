# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T04:51:49+00:00 ; durée 61.74 min ; blocs 52580225 → 52582078 (1839 vus)

## Connexion
- Requêtes RPC : 24038 ; erreurs : 0 ; latence p50/p95 : 302.2/1,109.1 ms
- Rafraîchissements d'état : 1839 ; âge des données au dernier bloc : 2.94 s ; changements de frais LP observés (pools à frais dynamiques) : 2819
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 41011 ; cycles déclenchés par événement : 1655 ; avance médiane sur le rafraîchissement multicall : 452 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,512.94 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 582 pools, 328 jetons, 21942 routes
- Par DEX : uniswap_v3 141, aerodrome 236, aerodrome_slipstream 156, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3923 (énumérés 393, par paires 0), mesurés 584, sous le plancher de 10000.0 $ : 2 → gardés 582 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2513.126375, 'AERO': 0.908483, 'cbBTC': 83773.517368}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,604,027 | 2,512.936233 | 52582079 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,149,573 | 1.099681 | 52582079 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,399,117 | 0.030034 | 52582079 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,053,188 | 106.932960 | 52582079 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,581,335 | 0.030059 | 52582079 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,743,424 | 0.030073 | 52582079 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,425,190 | 2,512.939424 | 52582079 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,322,447 | 0.000012 | 52582079 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/USDC | 535 | 9,319,283 | 2,513.382979 | 52582079 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 9,129,066 | 2,513.567686 | 52582079 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,612,241 | 0.000012 | 52582079 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,380,076 | 0.001685 | 52582079 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 7,370,302 | 0.000012 | 52582079 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,423,050 | 1.105535 | 52582079 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,587,545 | 0.030035 | 52582079 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,550,273 | 1.000859 | 52582079 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,466,717 | 0.026732 | 52582079 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,797,332 | 0.000281 | 52582079 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,744,821 | 0.802386 | 52582079 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,588,278 | 2,513.215114 | 52582079 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,428,402 | 0.999384 | 52582079 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,104,470 | 35,552.239681 | 52582079 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,739,421 | 2,770.412699 | 52582079 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,048,556 | 1.141617 | 52582079 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,871,397 | 0.000012 | 52582079 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,707,785 | 0.000011 | 52582079 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,671,775 | 401.408433 | 52582079 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2811 | 2,655,649 | 107.008223 | 52582079 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,460,932 | 1,058,498.079298 | 52582079 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 406 | 2,396,848 | 2,516.064817 | 52582079 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,905 | 1.189936 | 52582079 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,115,619 | 0.000000 | 52582079 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,039,504 | 0.024083 | 52582079 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| uniswap_v3 | XDP/USDC | 100 | 1,890,001 | 0.021153 | 52582079 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,888,018 | 0.916708 | 52582079 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,873,547 | 15.562388 | 52582079 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,843,135 | 1.372507 | 52582079 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,827,472 | 13,353.841937 | 52582079 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 1,782,842 | 1,053.476327 | 52582079 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,709,433 | 0.000012 | 52582079 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,617,666 | 2.300609 | 52582079 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,575,424 | 2,763.735345 | 52582079 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,553,671 | 1.105774 | 52582079 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | DRB/WETH | 10000 | 1,476,565 | 0.000000 | 52582079 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,619 | 0.832324 | 52582079 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,409,034 | 0.000282 | 52582079 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,401,237 | 0.004865 | 52582079 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,399,707 | 1.131481 | 52582079 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,399,035 | 2,763.449885 | 52582079 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,320,807 | 1.120869 | 52582079 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,311,705 | 23.407101 | 52582079 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,288,895 | 2,512.935554 | 52582079 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,259,620 | 34,559,706.626089 | 52582079 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,983 | 62.391461 | 52582079 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,244,831 | 1.105594 | 52582079 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,244,102 | 0.886451 | 52582079 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,217,013 | 73,193.752645 | 52582079 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,210,980 | 483,539.485072 | 52582079 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,205,011 | 1,179,286.020225 | 52582079 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,187,055 | 44.724220 | 52582079 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 3493 ; routes examinées : 76643406 ; candidats optimisés : 395654 ; net attendu > 0 : 26 ; dernier cycle 103.8 ms
- Rejets (moteur) : {'spread_below_threshold': 75543462, 'liquidity_below_min': 589585, 'negative_expected_net': 395628, 'borrow_bound_too_small': 87325, 'pool_quarantined': 20268, 'unquotable': 6986, 'cycle_budget_exhausted': 122, 'no_price_reference': 4}
- Enregistrements de la session : 395654 ; net attendu > 0 : 26 ; simulés (eth_call de la vraie tx) : 8 (ok 1, échec 7) ; étiquettes ghost N+1 : 3/4 positives
- Décisions : {'REJECTED': 395654} ; motifs de rejet : {'negative_expected_net': 395628, 'reliability_not_demonstrated': 26, 'simulation_failed': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52581009 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.013241 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.1032 €) | — | 33.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581010 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.013241 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.1032 €) | — | 33.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581009 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000403 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1025 €) | — | 33.01 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581009 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000379 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1025 €) | — | 35.12 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581010 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000403 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1025 €) | — | 33.01 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581010 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000379 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1025 €) | — | 35.12 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581009 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.014644 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.1020 €) | — | 30.13 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581010 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.014644 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.1020 €) | — | 30.13 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581009 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.013241 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0830 €) | — | 27.11 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581010 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.013241 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0830 €) | — | 27.11 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581009 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000337 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0824 €) | — | 31.75 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581010 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000337 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0824 €) | — | 31.75 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581009 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[uniswap_v3]→WETH | 0.012567 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0790 €) | — | 27.20 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581010 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[uniswap_v3]→WETH | 0.012567 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0790 €) | — | 27.20 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581009 | cbBTC→[uniswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000336 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0786 €) | — | 30.38 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581010 | cbBTC→[uniswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000336 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0786 €) | — | 30.38 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581361 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 23.145603 USDC | 0.010695 USDC | 0.000000 USDC | 0.005647 USDC | 0.005048 USDC (0.0046 €) | 0.005048 USDC | 2.18 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581361 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 23.145603 USDC | 0.010695 USDC | 0.000000 USDC | 0.005647 USDC | 0.005048 USDC (0.0046 €) | — | 2.18 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581009 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.003950 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 4.32 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581010 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.003950 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 4.32 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581009 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000126 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0039 €) | — | 3.98 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581010 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000126 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0039 €) | — | 3.98 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581009 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.003950 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0033 €) | — | 3.56 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52581010 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.003950 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0033 €) | — | 3.56 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52581009 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000126 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0031 €) | — | 3.18 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 13 ; taux observé 0.231 ; borne inférieure crédible (0.9) 0.114 ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
