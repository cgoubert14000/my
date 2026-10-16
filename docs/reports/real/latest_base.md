# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T14:01:21+00:00 ; durée 128.13 min ; blocs 52681120 → 52684962 (3678 vus)

## Connexion
- Requêtes RPC : 50634 ; erreurs : 45 ; latence p50/p95 : 155.3/1,101.2 ms
- Rafraîchissements d'état : 3679 ; âge des données au dernier bloc : 1.95 s ; changements de frais LP observés (pools à frais dynamiques) : 9405
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 82883 ; cycles déclenchés par événement : 3415 ; avance médiane sur le rafraîchissement multicall : 653 ms
- Gaz : base fee 0.005043 gwei ; prix ETH (pool le plus profond) : 2,454.12 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 328 jetons, 21482 routes
- Par DEX : uniswap_v3 136, aerodrome 236, aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 391, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2482.328501, 'AERO': 0.918334, 'cbBTC': 82582.444221}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,503,840 | 2,454.118709 | 52684962 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 46,793,769 | 1.100247 | 52684962 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,552,177 | 0.029980 | 52684962 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,495,404 | 101.458683 | 52684962 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,738,258 | 0.030033 | 52684962 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,523,451 | 0.030046 | 52684962 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,734,765 | 0.000012 | 52684962 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,150,596 | 2,456.143253 | 52684962 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,872,878 | 0.000012 | 52684962 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 7,634,445 | 0.000012 | 52684962 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,321,291 | 2,456.025676 | 52684962 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,216,149 | 0.001683 | 52684962 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,899,215 | 1.097820 | 52684962 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,460,532 | 2,454.151992 | 52684962 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,452,342 | 0.024857 | 52684962 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,412,355 | 0.029976 | 52684962 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,244,027 | 1.000855 | 52684962 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,905,284 | 0.802398 | 52684962 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,771,727 | 0.000280 | 52684962 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,425,229 | 2,456.048471 | 52684962 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,348,461 | 0.998889 | 52684962 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 400 | 4,078,555 | 2,458.827447 | 52684962 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,066,826 | 34,538.496131 | 52684962 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,548,080 | 2,692.036861 | 52684962 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,046,287 | 1.141839 | 52684962 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,843,498 | 0.000012 | 52684962 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,689,559 | 400.827178 | 52684962 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2730 | 2,666,034 | 101.486465 | 52684962 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,651,340 | 0.000011 | 52684962 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,303,368 | 1,152,367.436387 | 52684962 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,114,185 | 0.000000 | 52684962 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,807 | 1.195904 | 52684962 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,048,237 | 15.300884 | 52684962 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,009,165 | 1.405359 | 52684962 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,859,535 | 0.023101 | 52684962 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,777,155 | 0.018809 | 52684962 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,767,940 | 0.000012 | 52684962 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,762,334 | 13,364.770422 | 52684962 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,695,814 | 2.309541 | 52684962 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,572,460 | 2,701.019486 | 52684962 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3120 | 1,547,990 | 2,700.151836 | 52684962 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,525,449 | 0.916551 | 52684962 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,517,407 | 1.105492 | 52684962 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | EURC/USDC | 79 | 1,470,890 | 1.125696 | 52684962 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,106 | 0.825837 | 52684962 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,377,747 | 0.000000 | 52684962 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,368,106 | 0.004813 | 52684962 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,339,606 | 0.000279 | 52684962 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,322,390 | 0.435776 | 52684962 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,254,345 | 23.391607 | 52684962 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,249,107 | 62.279234 | 52684962 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,218,219 | 35,439,611.021332 | 52684962 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,217,830 | 1.105605 | 52684962 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,216,691 | 0.030036 | 52684962 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,214,371 | 2,456.187873 | 52684962 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,209,922 | 1,115,660.755315 | 52684962 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,162,368 | 506,722.172098 | 52684962 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,150,414 | 47.619913 | 52684962 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,143,717 | 1.131884 | 52684962 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/EDEL | 7000 | 1,142,276 | 80,387.830127 | 52684962 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 7093 ; routes examinées : 152371826 ; candidats optimisés : 991314 ; net attendu > 0 : 945 ; dernier cycle 179.3 ms
- Rejets (moteur) : {'spread_below_threshold': 148849403, 'liquidity_below_min': 1510673, 'pool_quarantined': 1011042, 'negative_expected_net': 990369, 'borrow_bound_too_small': 7080, 'cycle_budget_exhausted': 2314}
- Enregistrements de la session : 991314 ; net attendu > 0 : 945 ; simulés (eth_call de la vraie tx) : 92 (ok 18, échec 74) ; étiquettes ghost N+1 : 6/47 positives
- Décisions : {'REJECTED': 991314} ; motifs de rejet : {'below_safety_margin': 510, 'negative_expected_net': 990369, 'p_lower_below_threshold': 715, 'price_impact': 414, 'reliability_not_demonstrated': 230, 'simulation_failed': 74, 'stale_data': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52683619 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.005432 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000010 cbBTC (0.7377 €) | — | 18.00 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.184099 WETH | 0.000328 WETH | 0.000000 WETH | 0.000003 WETH | 0.000325 WETH (0.7375 €) | — | 17.68 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52683619 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004389 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6683 €) | — | 20.18 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004389 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6683 €) | — | 20.18 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 368.787596 USDC | 0.732861 USDC | 0.000000 USDC | 0.007083 USDC | 0.725778 USDC (0.6677 €) | — | 19.68 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 368.787596 USDC | 0.732861 USDC | 0.000000 USDC | 0.007083 USDC | 0.725778 USDC (0.6677 €) | — | 19.68 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004423 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6661 €) | — | 19.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004423 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6661 €) | — | 19.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 372.440191 USDC | 0.729818 USDC | 0.000000 USDC | 0.007083 USDC | 0.722735 USDC (0.6649 €) | — | 19.41 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 372.440191 USDC | 0.729818 USDC | 0.000000 USDC | 0.007083 USDC | 0.722735 USDC (0.6649 €) | — | 19.41 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004388 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6645 €) | — | 20.08 | 0.036 (n=23) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004388 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6645 €) | — | 20.08 | 0.036 (n=23) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 373.580952 USDC | 0.728182 USDC | 0.000000 USDC | 0.007083 USDC | 0.721099 USDC (0.6634 €) | — | 19.30 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 373.580952 USDC | 0.728182 USDC | 0.000000 USDC | 0.007083 USDC | 0.721099 USDC (0.6634 €) | — | 19.30 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004258 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6223 €) | — | 19.38 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004258 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6223 €) | — | 19.38 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 356.229227 USDC | 0.682506 USDC | 0.000000 USDC | 0.007083 USDC | 0.675423 USDC (0.6214 €) | — | 18.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 356.229227 USDC | 0.682506 USDC | 0.000000 USDC | 0.007083 USDC | 0.675423 USDC (0.6214 €) | — | 18.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.162066 WETH | 0.000260 WETH | 0.000000 WETH | 0.000003 WETH | 0.000257 WETH (0.5831 €) | — | 15.87 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52683620 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.004828 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5831 €) | — | 16.01 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.004932 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5823 €) | — | 15.65 | 0.008 (n=39) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52683619 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→WETH | 0.162065 WETH | 0.000260 WETH | 0.000000 WETH | 0.000003 WETH | 0.000257 WETH (0.5817 €) | — | 15.84 | 0.008 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52683619 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.004147 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5371 €) | — | 17.17 | 0.008 (n=39) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52683619 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.142392 WETH | 0.000240 WETH | 0.000000 WETH | 0.000003 WETH | 0.000237 WETH (0.5370 €) | — | 16.64 | 0.008 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52683619 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.003608 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5273 €) | — | 19.37 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 560 ; taux observé 0.120 ; borne inférieure crédible (0.9) 0.103 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
