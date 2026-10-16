# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T22:20:12+00:00 ; durée 290.64 min ; blocs 52691210 → 52699922 (8279 vus)

## Connexion
- Requêtes RPC : 112272 ; erreurs : 135 ; latence p50/p95 : 107.0/1,358.9 ms
- Rafraîchissements d'état : 8279 ; âge des données au dernier bloc : 4.72 s ; changements de frais LP observés (pools à frais dynamiques) : 19373
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 164537 ; cycles déclenchés par événement : 7644 ; avance médiane sur le rafraîchissement multicall : 967 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,414.84 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21274 routes
- Par DEX : uniswap_v3 134, aerodrome 235, aerodrome_slipstream 152, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3918 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2397.934409, 'AERO': 0.857255, 'cbBTC': 80846.375646}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,273,328 | 2,414.841664 | 52699922 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 46,094,944 | 1.134597 | 52699922 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,243,778 | 0.029640 | 52699922 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,929,600 | 105.508447 | 52699922 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,233,362 | 0.029609 | 52699922 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,410,688 | 0.029623 | 52699922 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,784,665 | 0.000012 | 52699922 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,077,905 | 2,420.544037 | 52699922 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,842,629 | 0.000012 | 52699922 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 7,830,781 | 0.000012 | 52699922 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 535 | 7,179,250 | 2,421.091270 | 52699922 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,151,990 | 0.001669 | 52699922 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,655,582 | 1.137988 | 52699922 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,406,506 | 2,415.008926 | 52699922 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,352,420 | 0.025295 | 52699922 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,334,366 | 0.029640 | 52699922 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,160,099 | 1.000855 | 52699922 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,826,804 | 0.802398 | 52699922 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,672,399 | 0.000276 | 52699922 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,387,993 | 2,421.325254 | 52699922 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,328,346 | 0.998887 | 52699922 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 403 | 4,277,008 | 2,424.317554 | 52699922 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,016,035 | 34,293.027806 | 52699922 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,461,781 | 2,755.610632 | 52699922 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,993,332 | 1.141835 | 52699922 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,871,713 | 1,021.593924 | 52699922 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,853,492 | 0.000012 | 52699922 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,701,786 | 399.403094 | 52699922 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,696,138 | 0.000011 | 52699922 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,582,411 | 105.472841 | 52699922 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,270,386 | 1,148,429.551079 | 52699922 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,352 | 1.197871 | 52699922 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,011,001 | 15.650766 | 52699922 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,825 | 1.405769 | 52699922 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,823,678 | 0.022200 | 52699922 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,811,187 | 0.000000 | 52699922 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,798,837 | 0.018840 | 52699922 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,768,215 | 0.000012 | 52699922 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,670,458 | 2.306265 | 52699922 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,637,218 | 13,476.387097 | 52699922 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,555,671 | 1.123503 | 52699922 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,540,700 | 2,747.308669 | 52699922 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3004 | 1,516,161 | 2,744.561214 | 52699922 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,512,666 | 1.105494 | 52699922 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,501,035 | 0.916552 | 52699922 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,637 | 0.826245 | 52699922 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,351,993 | 0.000000 | 52699922 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,327,414 | 0.004730 | 52699922 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,320,972 | 0.434984 | 52699922 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,309,403 | 0.000278 | 52699922 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,248,380 | 62.351801 | 52699922 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,246,882 | 1.131438 | 52699922 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,242,018 | 23.316368 | 52699922 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,210,107 | 2,420.911142 | 52699922 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/cbBTC | 3000 | 1,204,316 | 0.029619 | 52699922 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,202,337 | 35,126,265.709409 | 52699922 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,198,340 | 1.105606 | 52699922 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,185,204 | 1,125,763.824709 | 52699922 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,141,997 | 508,392.386813 | 52699922 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,126,495 | 13.862494 | 52699922 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 15922 ; routes examinées : 338724628 ; candidats optimisés : 1891707 ; net attendu > 0 : 384 ; dernier cycle 450.1 ms
- Rejets (moteur) : {'spread_below_threshold': 333139011, 'liquidity_below_min': 3328968, 'negative_expected_net': 1891323, 'unquotable': 279754, 'pool_quarantined': 61648, 'borrow_bound_too_small': 15908, 'cycle_budget_exhausted': 7632}
- Enregistrements de la session : 1891707 ; net attendu > 0 : 384 ; simulés (eth_call de la vraie tx) : 34 (ok 9, échec 25) ; étiquettes ghost N+1 : 1/27 positives
- Décisions : {'REJECTED': 1891707} ; motifs de rejet : {'below_safety_margin': 264, 'negative_expected_net': 1891323, 'p_lower_below_threshold': 267, 'price_impact': 12, 'reliability_not_demonstrated': 117, 'simulation_failed': 25}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52691349 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 6,452.347890 USDC | 4.060264 USDC | 0.000000 USDC | 0.010197 USDC | 4.050067 USDC (3.7261 €) | — | 6.28 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 2.679657 WETH | 0.001684 WETH | 0.000000 WETH | 0.000004 WETH | 0.001680 WETH (3.7143 €) | — | 6.27 | 0.115 (n=66) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52691349 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.079584 cbBTC | 0.000050 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000050 cbBTC (3.7120 €) | — | 6.27 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 5,655.448400 USDC | 3.376283 USDC | 0.000000 USDC | 0.010561 USDC | 3.365722 USDC (3.0965 €) | — | 5.95 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52691349 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 2.329365 WETH | 0.001400 WETH | 0.000000 WETH | 0.000004 WETH | 0.001396 WETH (3.0868 €) | — | 5.99 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52691349 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.069143 cbBTC | 0.000042 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000041 cbBTC (3.0844 €) | — | 5.99 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52691349 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 4,064.598917 USDC | 2.904825 USDC | 0.000000 USDC | 0.007643 USDC | 2.897182 USDC (2.6654 €) | — | 7.13 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.049738 cbBTC | 0.000036 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000036 cbBTC (2.6548 €) | — | 7.17 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 3,732.629577 USDC | 2.667963 USDC | 0.000000 USDC | 0.009102 USDC | 2.658861 USDC (2.4462 €) | — | 7.12 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52691349 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.561691 WETH | 0.001107 WETH | 0.000000 WETH | 0.000004 WETH | 0.001103 WETH (2.4391 €) | — | 7.06 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52691349 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.045815 cbBTC | 0.000033 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000033 cbBTC (2.4360 €) | — | 7.14 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52691349 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 3,610.960875 USDC | 2.555547 USDC | 0.000000 USDC | 0.008372 USDC | 2.547175 USDC (2.3434 €) | — | 7.05 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.044251 cbBTC | 0.000031 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000031 cbBTC (2.3340 €) | — | 7.08 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 3,367.491529 USDC | 1.652012 USDC | 0.000000 USDC | 0.008007 USDC | 1.644005 USDC (1.5125 €) | — | 4.88 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 1.410458 WETH | 0.000685 WETH | 0.000000 WETH | 0.000003 WETH | 0.000682 WETH (1.5078 €) | — | 4.83 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.040440 cbBTC | 0.000020 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000020 cbBTC (1.5061 €) | — | 5.00 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,597.655178 USDC | 1.259016 USDC | 0.000000 USDC | 0.007643 USDC | 1.251373 USDC (1.1513 €) | — | 7.83 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.660039 WETH | 0.000522 WETH | 0.000000 WETH | 0.000003 WETH | 0.000519 WETH (1.1473 €) | — | 7.86 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.019370 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.1465 €) | — | 7.95 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,737.688056 USDC | 1.237931 USDC | 0.000000 USDC | 0.007643 USDC | 1.230288 USDC (1.1319 €) | — | 7.08 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.720814 WETH | 0.000513 WETH | 0.000000 WETH | 0.000003 WETH | 0.000510 WETH (1.1276 €) | — | 7.07 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.020879 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.1264 €) | — | 7.25 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,630.050722 USDC | 1.114794 USDC | 0.000000 USDC | 0.008007 USDC | 1.106787 USDC (1.0182 €) | — | 6.79 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.020092 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0147 €) | — | 6.78 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52691349 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.669591 WETH | 0.000462 WETH | 0.000000 WETH | 0.000003 WETH | 0.000459 WETH (1.0145 €) | — | 6.85 | 0.115 (n=66) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 658 ; taux observé 0.132 ; borne inférieure crédible (0.9) 0.116 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
