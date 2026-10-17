# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T01:16:22+00:00 ; durée 129.79 min ; blocs 52701320 → 52705215 (3877 vus)

## Connexion
- Requêtes RPC : 48174 ; erreurs : 20 ; latence p50/p95 : 189.2/1,397.7 ms
- Rafraîchissements d'état : 3878 ; âge des données au dernier bloc : 1.55 s ; changements de frais LP observés (pools à frais dynamiques) : 5261
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2483 ; cycles déclenchés par événement : 238 ; avance médiane sur le rafraîchissement multicall : 558 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,418.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 574 pools, 328 jetons, 21010 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 2 → gardés 574 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2418.060843, 'AERO': 0.878781, 'cbBTC': 81702.724694}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,366,680 | 2,418.061038 | 52705215 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,642,070 | 1.147709 | 52705215 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,252,655 | 0.029706 | 52705215 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,867,164 | 106.624991 | 52705215 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,114,918 | 0.029648 | 52705215 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,418,077 | 0.029632 | 52705215 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,780,434 | 0.000012 | 52705215 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 9,572,046 | 0.000012 | 52705215 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 9,083,496 | 2,419.072777 | 52705215 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,841,212 | 0.000012 | 52705215 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 535 | 7,763,093 | 2,419.079144 | 52705215 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,151,694 | 0.001672 | 52705215 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,410,186 | 2,421.821623 | 52705215 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,329,203 | 0.029703 | 52705215 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,322,993 | 0.025296 | 52705215 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,166,978 | 1.000855 | 52705215 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,833,240 | 0.802398 | 52705215 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,678,417 | 0.000276 | 52705215 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,416,736 | 2,419.425679 | 52705215 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,321,930 | 0.998900 | 52705215 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,309,884 | 1.139753 | 52705215 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 4,044,648 | 33,899.757004 | 52705215 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,441,405 | 2,758.085310 | 52705215 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 3,022,670 | 1,018.626686 | 52705215 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,997,323 | 1.141834 | 52705215 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,851,776 | 0.000012 | 52705215 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,778,398 | 0.000011 | 52705215 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,638,896 | 2,422.892631 | 52705215 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,632,263 | 400.871512 | 52705215 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,571,344 | 106.601027 | 52705215 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,273,413 | 1,148,429.551079 | 52705215 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,352 | 1.197871 | 52705215 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,009,230 | 15.658953 | 52705215 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,887 | 1.405725 | 52705215 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,824,377 | 0.022209 | 52705215 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,811,596 | 0.000000 | 52705215 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,774,086 | 0.000012 | 52705215 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,768,077 | 0.018638 | 52705215 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,672,976 | 2.305908 | 52705215 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,600,173 | 1.123670 | 52705215 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,545,473 | 0.916550 | 52705215 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,536,355 | 2,774.254474 | 52705215 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,514,770 | 1.105495 | 52705215 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3012 | 1,508,569 | 2,774.247571 | 52705215 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,637 | 0.826245 | 52705215 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,406,408 | 13,479.167592 | 52705215 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,353,154 | 0.000000 | 52705215 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,935 | 0.435380 | 52705215 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,321,199 | 0.004744 | 52705215 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,311,022 | 0.000276 | 52705215 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,255,487 | 23.247552 | 52705215 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,380 | 62.351801 | 52705215 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,244,298 | 1.131470 | 52705215 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,209,336 | 34,668,237.465817 | 52705215 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,204,570 | 0.029630 | 52705215 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,201,384 | 1.105711 | 52705215 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,188,979 | 2,418.997375 | 52705215 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,185,306 | 1,128,572.072508 | 52705215 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,146,340 | 504,965.986239 | 52705215 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,133,671 | 13.646390 | 52705215 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 4115 ; routes examinées : 86456150 ; candidats optimisés : 485608 ; net attendu > 0 : 11 ; dernier cycle 477.2 ms
- Rejets (moteur) : {'spread_below_threshold': 85342597, 'liquidity_below_min': 621533, 'negative_expected_net': 485597, 'borrow_bound_too_small': 4113, 'unquotable': 2090, 'cycle_budget_exhausted': 209}
- Enregistrements de la session : 485608 ; net attendu > 0 : 11 ; simulés (eth_call de la vraie tx) : 4 (ok 4, échec 0) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 485608} ; motifs de rejet : {'negative_expected_net': 485597, 'reliability_not_demonstrated': 11}

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
| 52703446 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 40.797147 USDC | 0.025094 USDC | 0.000000 USDC | 0.005433 USDC | 0.019661 USDC (0.0181 €) | 0.019661 USDC | 4.82 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 662 ; taux observé 0.131 ; borne inférieure crédible (0.9) 0.115 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
