# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T15:38:43+00:00 ; durée 225.5 min ; blocs 52681120 → 52687880 (6376 vus)

## Connexion
- Requêtes RPC : 88532 ; erreurs : 225 ; latence p50/p95 : 87.5/1,492.0 ms
- Rafraîchissements d'état : 6377 ; âge des données au dernier bloc : 1.72 s ; changements de frais LP observés (pools à frais dynamiques) : 19035
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 162331 ; cycles déclenchés par événement : 5929 ; avance médiane sur le rafraîchissement multicall : 1,279 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,440.26 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 328 jetons, 21482 routes
- Par DEX : uniswap_v3 136, aerodrome 236, aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 391, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2482.328501, 'AERO': 0.918334, 'cbBTC': 82582.444221}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,074,718 | 2,440.257110 | 52687880 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 46,111,278 | 1.133080 | 52687880 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 20,238,804 | 0.029965 | 52687880 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,453,113 | 0.029932 | 52687880 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,236,330 | 103.544033 | 52687880 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,472,189 | 0.029979 | 52687880 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,749,338 | 0.000012 | 52687880 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,117,497 | 2,442.951955 | 52687880 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,835,522 | 0.000012 | 52687880 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 654 | 7,665,596 | 2,443.660494 | 52687880 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,166,921 | 0.001674 | 52687880 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 6,338,418 | 0.000012 | 52687880 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,445,368 | 2,440.695892 | 52687880 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,374,443 | 0.029941 | 52687880 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,364,016 | 0.025088 | 52687880 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,214,407 | 1.000855 | 52687880 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,025,284 | 1.129235 | 52687880 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,877,579 | 0.802398 | 52687880 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,718,744 | 0.000277 | 52687880 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,407,039 | 2,443.417729 | 52687880 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,330,547 | 0.998889 | 52687880 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,031,673 | 34,747.530863 | 52687880 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,486,260 | 2,753.362123 | 52687880 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 418 | 3,216,520 | 2,445.807881 | 52687880 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,024,807 | 1.141843 | 52687880 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,839,626 | 0.000012 | 52687880 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,759,627 | 401.641708 | 52687880 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,698,523 | 0.000011 | 52687880 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,625,941 | 103.570245 | 52687880 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,324,647 | 1,028.782862 | 52687880 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,288,921 | 1,153,814.531366 | 52687880 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,133 | 1.195719 | 52687880 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,100,704 | 0.000000 | 52687880 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,009,165 | 1.405359 | 52687880 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,942,648 | 15.419971 | 52687880 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,841,253 | 0.022645 | 52687880 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,784,790 | 0.018525 | 52687880 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,763,593 | 0.000012 | 52687880 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,709,310 | 13,416.065209 | 52687880 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,687,475 | 2.307014 | 52687880 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,553,320 | 2,769.296871 | 52687880 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3012 | 1,523,546 | 2,769.401569 | 52687880 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,516,833 | 0.916551 | 52687880 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,508,836 | 1.105492 | 52687880 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,497,092 | 1.124600 | 52687880 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,719 | 0.825441 | 52687880 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,371,858 | 0.000000 | 52687880 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,336,598 | 0.004721 | 52687880 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,324,753 | 0.000276 | 52687880 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,668 | 0.435357 | 52687880 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | USDC/SEND | 3000 | 1,248,947 | 62.295198 | 52687880 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,240,480 | 23.458402 | 52687880 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,211,227 | 35,449,290.457953 | 52687880 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,210,955 | 2,442.947034 | 52687880 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,210,951 | 1.105605 | 52687880 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,210,779 | 0.029984 | 52687880 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,198,995 | 1,123,289.953071 | 52687880 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,182,996 | 1.131531 | 52687880 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,155,442 | 506,670.436529 | 52687880 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,140,439 | 48.456533 | 52687880 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 12305 ; routes examinées : 264336010 ; candidats optimisés : 1697402 ; net attendu > 0 : 1480 ; dernier cycle 519.8 ms
- Rejets (moteur) : {'spread_below_threshold': 258742252, 'liquidity_below_min': 2530246, 'negative_expected_net': 1695922, 'pool_quarantined': 1305940, 'unquotable': 42513, 'borrow_bound_too_small': 12287, 'cycle_budget_exhausted': 5370}
- Enregistrements de la session : 1697402 ; net attendu > 0 : 1480 ; simulés (eth_call de la vraie tx) : 185 (ok 59, échec 126) ; étiquettes ghost N+1 : 22/91 positives
- Décisions : {'REJECTED': 1697402} ; motifs de rejet : {'below_safety_margin': 852, 'negative_expected_net': 1695922, 'p_lower_below_threshold': 1159, 'price_impact': 494, 'reliability_not_demonstrated': 321, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 4, 'simulation_failed': 126, 'stale_data': 12}

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
- Observations ghost : 604 ; taux observé 0.137 ; borne inférieure crédible (0.9) 0.120 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
