# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T08:38:26+00:00 ; durée 3.04 min ; blocs 53818717 → 53819619 (148 vus)

## Connexion
- Requêtes RPC : 2329 ; erreurs : 0 ; latence p50/p95 : 240.8/1,057.6 ms
- Rafraîchissements d'état : 148 ; âge des données au dernier bloc : 7.31 s ; changements de frais LP observés (pools à frais dynamiques) : 118
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 114 ; cycles déclenchés par événement : 61 ; avance médiane sur le rafraîchissement multicall : 794 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,226.04 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 484 pools, 281 jetons, 17914 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 103, aerodrome 201, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3751 (énumérés 303, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 3 → gardés 484 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.035754, 'cbBTC': 75513.528915, 'AERO': 0.590274}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,767,718 | 2,226.035754 | 53819639 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,384,656 | 0.029455 | 53819639 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,214,360 | 0.000013 | 53819639 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,089,164 | 0.029418 | 53819639 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,934,390 | 2,225.540627 | 53819639 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,332,483 | 107.703871 | 53819639 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,398,680 | 0.001552 | 53819639 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,027,562 | 1.695820 | 53819639 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,682,661 | 0.029458 | 53819639 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,106,785 | 2,225.691381 | 53819639 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,983,792 | 0.998447 | 53819639 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,290,009 | 42,843.539338 | 53819639 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,190,667 | 2,225.759435 | 53819639 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,548,101 | 0.029434 | 53819639 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,069,069 | 1,173,302.980369 | 53819639 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,776,681 | 0.007243 | 53819639 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,732,426 | 0.000013 | 53819639 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,647,836 | 0.000013 | 53819639 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,641,474 | 0.016506 | 53819639 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,633,005 | 0.000000 | 53819639 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,161 | 1.444757 | 53819639 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,527,326 | 0.000013 | 53819639 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,518,271 | 437.792313 | 53819639 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,752 | 0.817248 | 53819639 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,359,337 | 3,768.840057 | 53819639 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,322,119 | 2,225.891681 | 53819639 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,320,641 | 2,228.895631 | 53819639 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,264,222 | 14,875.724731 | 53819639 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,167,875 | 2,225.551550 | 53819639 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,934 | 76.923194 | 53819639 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,088,456 | 37,488,423.052990 | 53819639 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,040,339 | 107.774203 | 53819639 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,016,925 | 563,511.117012 | 53819639 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,005,432 | 0.000000 | 53819639 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 995,566 | 22,607,435.074717 | 53819639 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 986,259 | 19.724162 | 53819639 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 940,353 | 1,053.687383 | 53819639 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 933,865 | 2,225.328831 | 53819639 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 924,588 | 73.348217 | 53819639 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 921,795 | 0.000013 | 53819639 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 863,626 | 101,346.878943 | 53819639 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 837,343 | 0.000531 | 53819639 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 803,786 | 0.048435 | 53819639 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4560 | 802,710 | 20.790079 | 53819639 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 787,685 | 0.055505 | 53819639 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 786,349 | 3,786.756709 | 53819639 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 755,174 | 0.799699 | 53819639 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 717,576 | 0.571045 | 53819639 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 688,599 | 4,944,856.174691 | 53819639 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 682,739 | 0.000255 | 53819639 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 655,117 | 0.539193 | 53819639 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 655,007 | 145,989.213787 | 53819639 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 643,367 | 0.000008 | 53819639 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2138 | 622,846 | 560,711.147397 | 53819639 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 596,766 | 0.914286 | 53819639 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 596,686 | 2.462288 | 53819639 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,234 | 0.037607 | 53819639 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 530,666 | 0.079941 | 53819639 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 527,516 | 866,561.170194 | 53819639 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 526,946 | 1,053.887022 | 53819639 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 208 ; routes examinées : 3726112 ; candidats optimisés : 9382 ; net attendu > 0 : 0 ; dernier cycle 40.4 ms
- Rejets (moteur) : {'spread_below_threshold': 3681055, 'liquidity_below_min': 35467, 'negative_expected_net': 9382, 'borrow_bound_too_small': 208}
- Enregistrements de la session : 9382 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 9382} ; motifs de rejet : {'negative_expected_net': 9382}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53818801 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 11.931650 USDC | 0.001844 USDC | 0.000000 USDC | 0.005022 USDC | -0.0029 | -2.66 |
| 53818802 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 11.931650 USDC | 0.001844 USDC | 0.000000 USDC | 0.005022 USDC | -0.0029 | -2.66 |
| 53818802 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 11.931650 USDC | 0.001844 USDC | 0.000000 USDC | 0.005022 USDC | -0.0029 | -2.66 |
| 53819069 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |
| 53819070 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |
| 53819070 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |
| 53819071 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |
| 53819071 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |
| 53819072 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 10.101426 USDC | 0.001292 USDC | 0.000000 USDC | 0.005021 USDC | -0.0034 | -3.69 |
| 53819099 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.002220 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0036 | -7.99 |

## Fiabilité et décision
- Observations ghost : 5801 ; taux observé 0.159 ; borne inférieure crédible (0.9) 0.153 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
