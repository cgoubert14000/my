# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T09:35:25+00:00 ; durée 9.1 min ; blocs 52590312 → 52590588 (274 vus)

## Connexion
- Requêtes RPC : 3694 ; erreurs : 0 ; latence p50/p95 : 234.4/821.7 ms
- Rafraîchissements d'état : 275 ; âge des données au dernier bloc : 1.9 s ; changements de frais LP observés (pools à frais dynamiques) : 649
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12855 ; cycles déclenchés par événement : 326 ; avance médiane sur le rafraîchissement multicall : 328 ms
- Gaz : base fee 0.005080 gwei ; prix ETH (pool le plus profond) : 2,502.75 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 584 pools, 329 jetons, 21950 routes
- Par DEX : uniswap_v3 142, aerodrome 236, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3924 (énumérés 395, par paires 0), mesurés 586, sous le plancher de 10000.0 $ : 2 → gardés 584 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2506.12853, 'AERO': 0.905993, 'cbBTC': 83225.723803}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,829,419 | 2,502.754143 | 52590588 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,847,870 | 1.109455 | 52590588 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,317,840 | 0.030019 | 52590588 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,235,738 | 109.122698 | 52590588 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,288,709 | 0.030049 | 52590588 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,714,777 | 0.030064 | 52590588 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,400,513 | 2,496.526151 | 52590588 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,306,416 | 0.000012 | 52590588 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,113,283 | 2,502.889656 | 52590588 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 713 | 8,137,600 | 2,495.759163 | 52590588 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,134,278 | 0.000012 | 52590588 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,327,821 | 0.001673 | 52590588 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 6,657,235 | 0.000012 | 52590588 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,565,230 | 0.030007 | 52590588 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,527,784 | 1.000859 | 52590588 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,443,242 | 0.026711 | 52590588 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,770,774 | 0.000280 | 52590588 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,725,614 | 0.802392 | 52590588 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,499,908 | 2,495.463932 | 52590588 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,423,608 | 0.999017 | 52590588 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,106,489 | 35,230.053004 | 52590588 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,716,019 | 2,773.230969 | 52590588 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,028,025 | 1.141618 | 52590588 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,866,153 | 0.000012 | 52590588 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,839,366 | 0.000011 | 52590588 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,682,571 | 405.735002 | 52590588 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,616,586 | 109.151127 | 52590588 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,450,276 | 1,059,089.868450 | 52590588 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 433 | 2,284,250 | 2,499.302300 | 52590588 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 2,194,947 | 1,072.313602 | 52590588 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,960 | 1.189905 | 52590588 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,107,046 | 0.000000 | 52590588 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,040,180 | 0.024089 | 52590588 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,960,518 | 0.916707 | 52590588 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,950,417 | 15.674688 | 52590588 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,859,284 | 1.372626 | 52590588 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | USDC/AERO | 10000 | 1,843,855 | 1.101649 | 52590588 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | XDP/USDC | 100 | 1,794,320 | 0.019200 | 52590588 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,706,697 | 0.000012 | 52590588 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,677,939 | 2.306168 | 52590588 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,566,694 | 2,771.206866 | 52590588 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,566,556 | 13,497.925832 | 52590588 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,547,377 | 1.105776 | 52590588 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,408 | 0.832294 | 52590588 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,456,332 | 0.000000 | 52590588 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,406,861 | 1.119192 | 52590588 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,401,266 | 0.000278 | 52590588 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,394,683 | 0.004862 | 52590588 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3036 | 1,390,657 | 2,771.904298 | 52590588 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,367,059 | 1.131434 | 52590588 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,301,834 | 23.444104 | 52590588 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,264,483 | 2,496.576188 | 52590588 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,262,181 | 33,956,462.271768 | 52590588 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,679 | 62.421881 | 52590588 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,239,787 | 1.105594 | 52590588 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,235,335 | 0.886221 | 52590588 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,216,430 | 72,906.123027 | 52590588 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,206,084 | 483,539.485072 | 52590588 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,192,666 | 1,194,090.257779 | 52590588 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,296 | 0.436583 | 52590588 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 600 ; routes examinées : 13170000 ; candidats optimisés : 18409 ; net attendu > 0 : 0 ; dernier cycle 143.9 ms
- Rejets (moteur) : {'spread_below_threshold': 12984776, 'liquidity_below_min': 150615, 'negative_expected_net': 18409, 'borrow_bound_too_small': 15000, 'unquotable': 1200}
- Enregistrements de la session : 18409 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 18409} ; motifs de rejet : {'negative_expected_net': 18409}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52590582 | WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.005794 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0027 | -2.02 |
| 52590583 | WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.005794 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0027 | -2.02 |
| 52590582 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC | 14.525469 USDC | 0.004733 USDC | 0.000000 USDC | 0.007683 USDC | -0.0027 | -2.03 |
| 52590583 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC | 14.525469 USDC | 0.004733 USDC | 0.000000 USDC | 0.007683 USDC | -0.0027 | -2.03 |
| 52590583 | WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.005794 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0027 | -2.05 |
| 52590583 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC | 14.525469 USDC | 0.004733 USDC | 0.000000 USDC | 0.007712 USDC | -0.0027 | -2.05 |
| 52590405 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.011510 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0029 | -1.10 |
| 52590405 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.011510 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0029 | -1.10 |
| 52590406 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.011510 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0029 | -1.10 |
| 52590406 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.011510 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0029 | -1.10 |

## Fiabilité et décision
- Observations ghost : 21 ; taux observé 0.143 ; borne inférieure crédible (0.9) 0.069 ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
