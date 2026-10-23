# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T19:00:56+00:00 ; durée 24.48 min ; blocs 52995614 → 52996353 (690 vus)

## Connexion
- Requêtes RPC : 8438 ; erreurs : 0 ; latence p50/p95 : 285.7/1,853.5 ms
- Rafraîchissements d'état : 690 ; âge des données au dernier bloc : 2.47 s ; changements de frais LP observés (pools à frais dynamiques) : 1024
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1748 ; cycles déclenchés par événement : 174 ; avance médiane sur le rafraîchissement multicall : 655 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,404.30 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 317 jetons, 19488 routes
- Par DEX : uniswap_v3 138, aerodrome 222, aerodrome_slipstream 137, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 200 (rejetés 2) → 605 jetons ; pools candidats 3880 (énumérés 359, par paires 0), mesurés 548, sous le plancher de 10000.0 $ : 2 → gardés 546 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2404.297357, 'AERO': 0.765849, 'cbBTC': 81434.30056}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,321,273 | 2,404.297310 | 52996353 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,597,002 | 0.029491 | 52996353 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,655,557 | 94.890980 | 52996353 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 10,571,013 | 1.320249 | 52996353 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,291,398 | 0.029437 | 52996353 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,778,191 | 0.000012 | 52996353 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,854,903 | 0.029452 | 52996353 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,694,648 | 2,399.004220 | 52996353 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,159,289 | 0.001670 | 52996353 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 6,348,866 | 0.000012 | 52996353 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,479,226 | 2,398.086662 | 52996353 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,453,971 | 0.029481 | 52996353 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 4,926,057 | 0.000012 | 52996353 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,558,768 | 2,397.955182 | 52996353 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,290,658 | 0.999604 | 52996353 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,242,737 | 2,404.852450 | 52996353 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,996,103 | 34,299.717183 | 52996353 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,412,261 | 0.000275 | 52996353 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 430 | 2,810,461 | 2,402.353694 | 52996353 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,539,739 | 94.903181 | 52996353 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,312,300 | 394.767569 | 52996353 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,213,232 | 1,196,441.544061 | 52996353 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,059,277 | 3,147.955966 | 52996353 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,947,573 | 0.000000 | 52996353 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,929,843 | 0.000012 | 52996353 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,769,263 | 0.017963 | 52996353 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,746,335 | 0.000012 | 52996353 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,812 | 1.605727 | 52996353 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,526,972 | 3,162.162355 | 52996353 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,629 | 0.824389 | 52996353 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,416,468 | 13,376.517420 | 52996353 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,386,309 | 0.005033 | 52996353 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,300,099 | 0.000275 | 52996353 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,293,307 | 2,398.915967 | 52996353 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,266,235 | 0.000000 | 52996353 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/msETH (stable) | 500 | 1,258,502 | 2.309413 | 52996353 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,228,362 | 64.400566 | 52996353 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,806 | 35,714,679.691501 | 52996353 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,170,179 | 483,625.137105 | 52996353 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,169,135 | 1,114,911.728779 | 52996353 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,148,284 | 47.515766 | 52996353 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,146,382 | 16.265509 | 52996353 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,081,831 | 75,730.833584 | 52996353 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,077,365 | 20,962,238.217469 | 52996353 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,073,454 | 0.039565 | 52996353 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,052,023 | 16.467959 | 52996353 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 994,920 | 23.117911 | 52996353 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 961,347 | 1,050.556895 | 52996353 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 940,240 | 2,390.810405 | 52996353 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 914,713 | 0.000543 | 52996353 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 907,061 | 0.000009 | 52996353 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 894,239 | 17.430364 | 52996353 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 859,977 | 2,404.471911 | 52996353 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 831,230 | 1.105789 | 52996353 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| pancakeswap_v3 | QUID/USDC | 100 | 828,246 | 0.061847 | 52996353 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 814,646 | 0.803225 | 52996353 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 780,137 | 0.658896 | 52996353 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 777,841 | 4,508,196.212624 | 52996353 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 732,481 | 135,492.844770 | 52996353 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 731,579 | 0.670931 | 52996353 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 863 ; routes examinées : 16818144 ; candidats optimisés : 113013 ; net attendu > 0 : 6 ; dernier cycle 635.5 ms
- Rejets (moteur) : {'spread_below_threshold': 16538464, 'liquidity_below_min': 165709, 'negative_expected_net': 113007, 'borrow_bound_too_small': 863, 'cycle_budget_exhausted': 95}
- Enregistrements de la session : 113013 ; net attendu > 0 : 6 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 113013} ; motifs de rejet : {'below_safety_margin': 6, 'negative_expected_net': 113007, 'p_lower_below_threshold': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52996140 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003969 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.75 | 0.121 (n=244) | REJECTED | below_safety_margin(299216607808<793839115648), p_lower_below_threshold(0.12<0.75) |
| 52996140 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.463325 USDC | 0.007965 USDC | 0.000000 USDC | 0.007255 USDC | 0.000710 USDC (0.0007 €) | — | 0.75 | 0.121 (n=244) | REJECTED | below_safety_margin(710<1892), p_lower_below_threshold(0.12<0.75) |
| 52996140 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.003799 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.10 | 0.241 (n=120) | REJECTED | below_safety_margin(37245108349<759733478683), p_lower_below_threshold(0.24<0.75) |
| 52996140 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.089971 USDC | 0.007337 USDC | 0.000000 USDC | 0.007255 USDC | 0.000082 USDC (0.0001 €) | — | 0.09 | 0.241 (n=120) | REJECTED | below_safety_margin(82<1817), p_lower_below_threshold(0.24<0.75) |
| 52996140 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003779 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.01 | 0.241 (n=120) | REJECTED | below_safety_margin(5649287560<755701593562), p_lower_below_threshold(0.24<0.75) |
| 52996140 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.019665 USDC | 0.007261 USDC | 0.000000 USDC | 0.007255 USDC | 0.000006 USDC (0.0000 €) | — | 0.01 | 0.241 (n=120) | REJECTED | below_safety_margin(6<1803), p_lower_below_threshold(0.24<0.75) |

## Fiabilité et décision
- Observations ghost : 2049 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
