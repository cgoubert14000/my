# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T09:29:19+00:00 ; durée 3.01 min ; blocs 52590312 → 52590406 (92 vus)

## Connexion
- Requêtes RPC : 1266 ; erreurs : 0 ; latence p50/p95 : 223.5/953.2 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 2.35 s ; changements de frais LP observés (pools à frais dynamiques) : 208
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4022 ; cycles déclenchés par événement : 113 ; avance médiane sur le rafraîchissement multicall : 302 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,505.47 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 584 pools, 329 jetons, 21950 routes
- Par DEX : uniswap_v3 142, aerodrome 236, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3924 (énumérés 395, par paires 0), mesurés 586, sous le plancher de 10000.0 $ : 2 → gardés 584 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2506.12853, 'AERO': 0.905993, 'cbBTC': 83225.723803}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,925,347 | 2,505.473728 | 52590405 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,895,323 | 1.106888 | 52590405 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,335,816 | 0.030034 | 52590405 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,276,909 | 108.807078 | 52590405 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,733,472 | 0.030049 | 52590405 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,724,135 | 0.030064 | 52590405 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,427,502 | 2,499.786392 | 52590405 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,308,491 | 0.000012 | 52590405 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,118,233 | 2,505.474651 | 52590405 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 579 | 8,529,237 | 2,499.741727 | 52590405 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 8,236,040 | 0.000012 | 52590405 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,330,576 | 0.001672 | 52590405 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 7,140,495 | 0.000012 | 52590405 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,571,690 | 0.030034 | 52590405 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,533,791 | 1.000859 | 52590405 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,449,552 | 0.026711 | 52590405 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,779,529 | 0.000280 | 52590405 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,730,749 | 0.802392 | 52590405 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,513,034 | 2,499.611777 | 52590405 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,426,212 | 0.999017 | 52590405 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,110,951 | 35,230.053004 | 52590405 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,891,982 | 1.099888 | 52590405 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,722,344 | 2,772.939114 | 52590405 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,031,315 | 1.141618 | 52590405 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,867,060 | 0.000012 | 52590405 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,623,695 | 108.835948 | 52590405 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,558,049 | 0.000011 | 52590405 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,452,938 | 1,059,089.868450 | 52590405 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,421,249 | 404.603326 | 52590405 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/USDT | 406 | 2,284,835 | 2,503.275824 | 52590405 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,960 | 1.189905 | 52590405 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,109,336 | 0.000000 | 52590405 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,040,180 | 0.024089 | 52590405 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,962,648 | 0.916707 | 52590405 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,901,808 | 1,072.243208 | 52590405 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,859,284 | 1.372626 | 52590405 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,829,368 | 15.665008 | 52590405 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,807,893 | 0.019433 | 52590406 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,707,232 | 0.000012 | 52590405 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,679,706 | 2.306245 | 52590405 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,641,032 | 13,469.471789 | 52590405 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,569,024 | 2,768.405422 | 52590405 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,549,058 | 1.105776 | 52590405 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,408 | 0.832294 | 52590405 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,457,913 | 0.000000 | 52590405 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,406,983 | 1.119341 | 52590405 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,403,845 | 0.000278 | 52590405 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,396,424 | 0.004863 | 52590405 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,393,033 | 2,767.473131 | 52590405 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,361,853 | 1.131493 | 52590405 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,306,200 | 23.433195 | 52590405 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,265,824 | 2,499.812713 | 52590405 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,263,734 | 33,942,102.170826 | 52590405 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,679 | 62.421881 | 52590405 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,242,594 | 0.886289 | 52590405 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,241,134 | 1.105594 | 52590405 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,217,752 | 72,906.123027 | 52590405 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,207,394 | 483,539.485072 | 52590405 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,193,962 | 1,194,090.257779 | 52590405 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,500 | 0.436708 | 52590405 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 204 ; routes examinées : 4477800 ; candidats optimisés : 5929 ; net attendu > 0 : 0 ; dernier cycle 54.0 ms
- Rejets (moteur) : {'spread_below_threshold': 4417351, 'liquidity_below_min': 49012, 'negative_expected_net': 5929, 'borrow_bound_too_small': 5100, 'unquotable': 408}
- Enregistrements de la session : 5929 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 5929} ; motifs de rejet : {'negative_expected_net': 5929}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52590405 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.011510 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0029 | -1.10 |
| 52590405 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.011510 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0029 | -1.10 |
| 52590406 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.011510 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0029 | -1.10 |
| 52590395 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→WETH | 0.007816 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0030 | -1.69 |
| 52590395 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→WETH | 0.007816 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0030 | -1.69 |
| 52590405 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.000342 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0031 | -1.17 |
| 52590405 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.000342 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0031 | -1.17 |
| 52590406 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.000342 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0031 | -1.17 |
| 52590396 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.723577 USDC | 0.001820 USDC | 0.000000 USDC | 0.005285 USDC | -0.0032 | -7.34 |
| 52590396 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.723577 USDC | 0.001820 USDC | 0.000000 USDC | 0.005285 USDC | -0.0032 | -7.34 |

## Fiabilité et décision
- Observations ghost : 21 ; taux observé 0.143 ; borne inférieure crédible (0.9) 0.069 ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
