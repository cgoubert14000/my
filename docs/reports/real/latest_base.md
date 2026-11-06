# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T08:44:29+00:00 ; durée 9.08 min ; blocs 53818717 → 53821443 (415 vus)

## Connexion
- Requêtes RPC : 6693 ; erreurs : 0 ; latence p50/p95 : 289.6/1,104.4 ms
- Rafraîchissements d'état : 415 ; âge des données au dernier bloc : 5.07 s ; changements de frais LP observés (pools à frais dynamiques) : 333
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 349 ; cycles déclenchés par événement : 176 ; avance médiane sur le rafraîchissement multicall : 539 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,226.04 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 484 pools, 281 jetons, 17914 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 103, aerodrome 201, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3751 (énumérés 303, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 3 → gardés 484 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.035754, 'cbBTC': 75513.528915, 'AERO': 0.590274}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,854,489 | 2,226.035754 | 53821444 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,499,339 | 0.029460 | 53821444 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,212,124 | 0.000013 | 53821444 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,088,524 | 0.029418 | 53821444 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,934,420 | 2,227.682139 | 53821444 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,334,482 | 107.645157 | 53821444 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,401,055 | 0.001554 | 53821444 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,027,562 | 1.695820 | 53821444 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,682,379 | 0.029459 | 53821444 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,113,795 | 2,228.131513 | 53821444 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,983,046 | 0.998447 | 53821444 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,290,009 | 42,843.539338 | 53821444 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,190,671 | 2,228.240959 | 53821444 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,547,957 | 0.029434 | 53821444 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,069,069 | 1,173,302.980369 | 53821444 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,785,846 | 0.007289 | 53821444 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,732,192 | 0.000013 | 53821444 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,647,599 | 0.000013 | 53821444 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,642,118 | 0.016516 | 53821444 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,633,004 | 0.000000 | 53821444 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,161 | 1.444757 | 53821444 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,527,137 | 0.000013 | 53821444 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,518,271 | 437.792313 | 53821444 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,750 | 0.817250 | 53821444 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,359,339 | 3,771.150765 | 53821444 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,322,119 | 2,225.892408 | 53821444 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,320,641 | 2,229.362078 | 53821444 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,264,087 | 14,875.724731 | 53821444 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,167,880 | 2,227.751087 | 53821444 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,934 | 76.923194 | 53821444 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,088,456 | 37,488,423.052990 | 53821444 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,040,734 | 107.774203 | 53821444 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,016,925 | 563,511.117012 | 53821444 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,003,214 | 0.000000 | 53821444 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 990,850 | 22,595,040.061157 | 53821444 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 986,545 | 19.707452 | 53821444 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 940,353 | 1,053.687393 | 53821444 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 933,865 | 2,225.328831 | 53821444 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 923,090 | 73.586550 | 53821444 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 921,648 | 0.000013 | 53821444 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 863,626 | 101,346.878943 | 53821444 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 837,360 | 0.000531 | 53821444 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4675 | 805,733 | 20.677770 | 53821444 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | USDC/VVV | 3000 | 804,149 | 0.048292 | 53821444 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 787,088 | 0.055417 | 53821444 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 786,349 | 3,786.756709 | 53821444 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 755,174 | 0.799699 | 53821444 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 717,576 | 0.571045 | 53821444 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 688,599 | 4,944,856.174691 | 53821444 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 682,739 | 0.000255 | 53821444 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 655,117 | 0.539193 | 53821444 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 655,007 | 145,989.213787 | 53821444 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 643,323 | 0.000008 | 53821444 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 622,846 | 560,711.147397 | 53821444 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 596,766 | 0.914286 | 53821444 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 596,686 | 2.462288 | 53821444 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 555,604 | 0.037542 | 53821444 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 532,240 | 0.080339 | 53821444 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 526,946 | 1,053.887022 | 53821444 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 526,532 | 870,633.900757 | 53821444 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 590 ; routes examinées : 10569260 ; candidats optimisés : 26401 ; net attendu > 0 : 0 ; dernier cycle 42.2 ms
- Rejets (moteur) : {'spread_below_threshold': 10407226, 'liquidity_below_min': 135043, 'negative_expected_net': 26401, 'borrow_bound_too_small': 590}
- Enregistrements de la session : 26401 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 26401} ; motifs de rejet : {'negative_expected_net': 26401}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53820767 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 32.316660 USDC | 0.005649 USDC | 0.000000 USDC | 0.006713 USDC | -0.0010 | -0.33 |
| 53820767 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.014524 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0010 | -0.33 |
| 53818801 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 11.931650 USDC | 0.001844 USDC | 0.000000 USDC | 0.005022 USDC | -0.0029 | -2.66 |
| 53818802 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 11.931650 USDC | 0.001844 USDC | 0.000000 USDC | 0.005022 USDC | -0.0029 | -2.66 |
| 53818802 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 11.931650 USDC | 0.001844 USDC | 0.000000 USDC | 0.005022 USDC | -0.0029 | -2.66 |
| 53819069 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |
| 53819070 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |
| 53819070 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |
| 53819071 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |
| 53819071 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |

## Fiabilité et décision
- Observations ghost : 5801 ; taux observé 0.159 ; borne inférieure crédible (0.9) 0.153 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
