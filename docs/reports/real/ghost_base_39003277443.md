# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T05:03:33+00:00 ; durée 21.34 min ; blocs 52711390 → 52712032 (641 vus)

## Connexion
- Requêtes RPC : 8106 ; erreurs : 0 ; latence p50/p95 : 159.2/939.2 ms
- Rafraîchissements d'état : 642 ; âge des données au dernier bloc : 1.53 s ; changements de frais LP observés (pools à frais dynamiques) : 692
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 823 ; cycles déclenchés par événement : 82 ; avance médiane sur le rafraîchissement multicall : 645 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,421.25 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 329 jetons, 21010 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 393, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2421.248535, 'AERO': 0.878353, 'cbBTC': 81453.278136}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,172,355 | 2,421.248096 | 52712032 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,826,405 | 1.138091 | 52712032 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,241,568 | 0.029766 | 52712032 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,087,711 | 0.029719 | 52712032 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 15,995,113 | 105.203327 | 52712032 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,410,339 | 0.029707 | 52712032 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,753,730 | 0.000012 | 52712032 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,109,608 | 2,425.285242 | 52712032 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,840,815 | 0.000012 | 52712032 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 698 | 7,222,923 | 2,426.104101 | 52712032 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,162,315 | 0.001679 | 52712032 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 6,967,567 | 0.000012 | 52712032 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,566,754 | 1.140417 | 52712032 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,413,753 | 2,426.880400 | 52712032 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,346,135 | 0.025281 | 52712032 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,333,375 | 0.029763 | 52712032 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,257,911 | 1.000855 | 52712032 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,839,610 | 0.802398 | 52712032 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,684,647 | 0.000276 | 52712032 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,439,024 | 2,426.224420 | 52712032 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,318,959 | 0.998900 | 52712032 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,048,909 | 33,917.669178 | 52712032 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,458,177 | 2,759.415041 | 52712032 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,917,566 | 1.141834 | 52712032 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,850,578 | 0.000012 | 52712032 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,626,273 | 399.485017 | 52712032 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,594,470 | 105.198612 | 52712032 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,529,390 | 0.000011 | 52712032 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,266,257 | 1,158,742.078326 | 52712032 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,407 | 1.197840 | 52712032 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,097,658 | 2,428.927391 | 52712032 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,002,143 | 1.413593 | 52712032 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,853,078 | 15.589844 | 52712032 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,824,967 | 0.022215 | 52712032 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,814,062 | 0.000000 | 52712032 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,775,837 | 0.000012 | 52712032 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,769,018 | 0.018653 | 52712032 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,674,925 | 2.306475 | 52712032 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,634,217 | 1.123841 | 52712032 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,629,666 | 1,014.494805 | 52712032 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,547,510 | 0.916550 | 52712032 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,542,059 | 2,761.870858 | 52712032 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3012 | 1,516,896 | 2,761.951241 | 52712032 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,516,768 | 1.105495 | 52712032 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,475,964 | 13,437.884738 | 52712032 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,637 | 0.826245 | 52712032 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,358,228 | 0.000000 | 52712032 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,339,869 | 0.004757 | 52712032 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,935 | 0.435380 | 52712032 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,312,787 | 0.000279 | 52712032 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,256,748 | 23.260018 | 52712032 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299956 | 52712032 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,239,379 | 1.131518 | 52712032 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,208,995 | 34,801,915.098400 | 52712032 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,204,951 | 0.029700 | 52712032 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,202,810 | 1.105712 | 52712032 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,189,835 | 2,425.210317 | 52712032 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,182,655 | 1,136,628.171484 | 52712032 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,154,176 | 497,468.150224 | 52712032 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,126,080 | 13.875430 | 52712032 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 723 ; routes examinées : 15190230 ; candidats optimisés : 132205 ; net attendu > 0 : 0 ; dernier cycle 402.2 ms
- Rejets (moteur) : {'spread_below_threshold': 14935508, 'negative_expected_net': 132205, 'liquidity_below_min': 121794, 'borrow_bound_too_small': 723}
- Enregistrements de la session : 132205 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 132205} ; motifs de rejet : {'negative_expected_net': 132205}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52711949 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 18.967025 USDC | 0.005138 USDC | 0.000000 USDC | 0.005439 USDC | -0.0003 | -0.16 |
| 52711793 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 117.162038 USDC | 0.004093 USDC | 0.000000 USDC | 0.005807 USDC | -0.0016 | -0.15 |
| 52711793 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.049205 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.14 |
| 52712024 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 9.011657 USDC | 0.001798 USDC | 0.000000 USDC | 0.005439 USDC | -0.0033 | -4.04 |
| 52712025 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 9.011657 USDC | 0.001798 USDC | 0.000000 USDC | 0.005439 USDC | -0.0033 | -4.04 |
| 52712026 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 9.011657 USDC | 0.001798 USDC | 0.000000 USDC | 0.005439 USDC | -0.0033 | -4.04 |
| 52712027 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 9.011657 USDC | 0.001798 USDC | 0.000000 USDC | 0.005439 USDC | -0.0033 | -4.04 |
| 52712028 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 9.011657 USDC | 0.001798 USDC | 0.000000 USDC | 0.005439 USDC | -0.0033 | -4.04 |
| 52712029 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 9.011657 USDC | 0.001798 USDC | 0.000000 USDC | 0.005439 USDC | -0.0033 | -4.04 |
| 52712030 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 9.011657 USDC | 0.001798 USDC | 0.000000 USDC | 0.005439 USDC | -0.0033 | -4.04 |

## Fiabilité et décision
- Observations ghost : 664 ; taux observé 0.131 ; borne inférieure crédible (0.9) 0.115 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
