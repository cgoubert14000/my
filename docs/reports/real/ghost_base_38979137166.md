# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T03:41:34+00:00 ; durée 274.99 min ; blocs 52701320 → 52709567 (8153 vus)

## Connexion
- Requêtes RPC : 98093 ; erreurs : 75 ; latence p50/p95 : 263.6/1,606.7 ms
- Rafraîchissements d'état : 8153 ; âge des données au dernier bloc : 4.5 s ; changements de frais LP observés (pools à frais dynamiques) : 11609
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2483 ; cycles déclenchés par événement : 238 ; avance médiane sur le rafraîchissement multicall : 558 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,421.25 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 574 pools, 328 jetons, 21010 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 2 → gardés 574 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2418.060843, 'AERO': 0.878781, 'cbBTC': 81702.724694}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,231,001 | 2,421.248631 | 52709567 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,894,291 | 1.134289 | 52709567 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,741,182 | 0.029719 | 52709567 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,241,083 | 0.029762 | 52709567 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,027,260 | 104.781761 | 52709567 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,405,326 | 0.029707 | 52709567 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 9,892,032 | 0.000012 | 52709567 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,760,862 | 0.000012 | 52709567 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,109,494 | 2,425.621037 | 52709567 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,866,167 | 0.000012 | 52709567 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,416,205 | 2,426.257203 | 52709567 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,167,347 | 0.001681 | 52709567 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,413,751 | 2,424.706851 | 52709567 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,354,678 | 0.025281 | 52709567 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,333,741 | 0.029773 | 52709567 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,257,912 | 1.000855 | 52709567 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,839,611 | 0.802398 | 52709567 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,780,952 | 1.140417 | 52709567 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,684,648 | 0.000276 | 52709567 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,441,026 | 2,426.599692 | 52709567 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,319,489 | 0.998900 | 52709567 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 400 | 4,063,360 | 2,429.095108 | 52709567 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,048,328 | 33,927.427969 | 52709567 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,463,977 | 2,759.058423 | 52709567 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,917,566 | 1.141834 | 52709567 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,850,785 | 0.000012 | 52709567 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,705,157 | 0.000011 | 52709567 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,599,859 | 104.752234 | 52709567 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,585,919 | 399.841090 | 52709567 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,276,410 | 1,148,429.551079 | 52709567 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,407 | 1.197840 | 52709567 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,002,143 | 1.413593 | 52709567 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,824,710 | 0.022212 | 52709567 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,814,001 | 0.000000 | 52709567 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,779,647 | 0.018798 | 52709567 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,775,875 | 0.000012 | 52709567 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,731,035 | 15.617346 | 52709567 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,680,835 | 13,437.143537 | 52709567 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,674,925 | 2.306475 | 52709567 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,634,232 | 1.123859 | 52709567 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,547,510 | 0.916550 | 52709567 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,543,693 | 2,751.114367 | 52709567 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,519,319 | 2,754.085017 | 52709567 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,516,768 | 1.105495 | 52709567 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,637 | 0.826245 | 52709567 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,358,229 | 0.000000 | 52709567 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,325,891 | 0.004757 | 52709567 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,935 | 0.435380 | 52709567 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,312,781 | 0.000278 | 52709567 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,256,762 | 23.259597 | 52709567 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,700 | 62.319855 | 52709567 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,239,366 | 1.131518 | 52709567 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,210,438 | 34,679,508.453663 | 52709567 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,209,872 | 2,425.632869 | 52709567 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/cbBTC | 3000 | 1,205,023 | 0.029699 | 52709567 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,202,810 | 1.105712 | 52709567 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,183,772 | 1,134,483.911280 | 52709567 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,154,176 | 497,468.150224 | 52709567 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,129,106 | 13.783280 | 52709567 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,113,013 | 82,424.958600 | 52709567 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 8390 ; routes examinées : 176273900 ; candidats optimisés : 1052597 ; net attendu > 0 : 23 ; dernier cycle 604.5 ms
- Rejets (moteur) : {'spread_below_threshold': 173935032, 'liquidity_below_min': 1274989, 'negative_expected_net': 1052574, 'borrow_bound_too_small': 8384, 'unquotable': 2090, 'cycle_budget_exhausted': 808}
- Enregistrements de la session : 1052597 ; net attendu > 0 : 23 ; simulés (eth_call de la vraie tx) : 5 (ok 5, échec 0) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 1052597} ; motifs de rejet : {'below_safety_margin': 11, 'negative_expected_net': 1052574, 'p_lower_below_threshold': 6, 'reliability_not_demonstrated': 17}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52704816 | cbBTC→[aerodrome_slipstream]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001987 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2142 €) | — | 14.39 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52704816 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→EDGE→[uniswap_v3]→USDC | 154.923652 USDC | 0.239370 USDC | 0.000000 USDC | 0.007272 USDC | 0.232098 USDC (0.2135 €) | 0.232098 USDC | 14.98 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52704816 | cbBTC→[aerodrome_slipstream]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001786 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1805 €) | — | 13.50 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52704816 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→EDGE→[uniswap_v3]→USDC | 151.640227 USDC | 0.202681 USDC | 0.000000 USDC | 0.007272 USDC | 0.195409 USDC (0.1798 €) | 0.195409 USDC | 12.89 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52704816 | cbBTC→[aerodrome_slipstream]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001709 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1722 €) | — | 13.46 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52704816 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→EDGE→[uniswap_v3]→USDC | 137.167639 USDC | 0.193763 USDC | 0.000000 USDC | 0.007272 USDC | 0.186491 USDC (0.1716 €) | 0.186491 USDC | 13.60 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52704816 | cbBTC→[aerodrome_slipstream]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001635 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1655 €) | — | 13.51 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52704816 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→EDGE→[uniswap_v3]→USDC | 137.194017 USDC | 0.187041 USDC | 0.000000 USDC | 0.007272 USDC | 0.179769 USDC (0.1654 €) | — | 13.10 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52704816 | cbBTC→[aerodrome_slipstream]→EDGE→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.001655 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1565 €) | — | 12.63 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52704816 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→EDGE→[uniswap_v3]→USDC | 137.541413 USDC | 0.177077 USDC | 0.000000 USDC | 0.007272 USDC | 0.169805 USDC (0.1562 €) | — | 12.35 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52709100 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 55.743622 USDC | 0.045465 USDC | 0.000000 USDC | 0.005433 USDC | 0.040032 USDC (0.0368 €) | 0.040032 USDC | 7.18 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 52703446 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 40.797147 USDC | 0.025094 USDC | 0.000000 USDC | 0.005433 USDC | 0.019661 USDC (0.0181 €) | 0.019661 USDC | 4.82 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |
| 52706582 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 23.865242 USDC | 0.008427 USDC | 0.000000 USDC | 0.005432 USDC | 0.002995 USDC (0.0028 €) | — | 1.25 | 0.001 (n=12) | REJECTED | below_safety_margin(2995<4773), reliability_not_demonstrated |
| 52709324 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.001497 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0022 €) | — | 0.20 | 0.114 (n=74) | REJECTED | below_safety_margin(3<29), p_lower_below_threshold(0.11<0.75) |
| 52709324 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH | 0.046271 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 0.19 | 0.114 (n=74) | REJECTED | below_safety_margin(857844411028<9254278657269), p_lower_below_threshold(0.11<0.75) |
| 52706887 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 17.773630 USDC | 0.007104 USDC | 0.000000 USDC | 0.005432 USDC | 0.001672 USDC (0.0015 €) | — | 0.94 | 0.001 (n=12) | REJECTED | below_safety_margin(1672<3554), reliability_not_demonstrated |
| 52709324 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.001353 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0015 €) | — | 0.15 | 0.114 (n=74) | REJECTED | below_safety_margin(2<27), p_lower_below_threshold(0.11<0.75) |
| 52709324 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.001227 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0015 €) | — | 0.16 | 0.114 (n=74) | REJECTED | below_safety_margin(2<24), p_lower_below_threshold(0.11<0.75) |
| 52709324 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→WETH | 0.055689 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 0.12 | 0.114 (n=74) | REJECTED | below_safety_margin(669673092443<11137879016764), p_lower_below_threshold(0.11<0.75) |
| 52707819 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 22.199794 USDC | 0.007050 USDC | 0.000000 USDC | 0.005432 USDC | 0.001618 USDC (0.0015 €) | — | 0.73 | 0.001 (n=12) | REJECTED | below_safety_margin(1618<4439), reliability_not_demonstrated |
| 52706716 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 21.861275 USDC | 0.006996 USDC | 0.000000 USDC | 0.005433 USDC | 0.001563 USDC (0.0014 €) | — | 0.71 | 0.001 (n=12) | REJECTED | below_safety_margin(1563<4372), reliability_not_demonstrated |
| 52709324 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→WETH | 0.055637 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 0.10 | 0.114 (n=74) | REJECTED | below_safety_margin(543286409196<11127403168035), p_lower_below_threshold(0.11<0.75) |
| 52709126 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 20.023713 USDC | 0.005956 USDC | 0.000000 USDC | 0.005432 USDC | 0.000524 USDC (0.0005 €) | — | 0.26 | 0.001 (n=12) | REJECTED | below_safety_margin(524<4004), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 663 ; taux observé 0.131 ; borne inférieure crédible (0.9) 0.115 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
