# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T13:10:56+00:00 ; durée 6.06 min ; blocs 54331551 → 54333371 (430 vus)

## Connexion
- Requêtes RPC : 5269 ; erreurs : 0 ; latence p50/p95 : 219.5/1,150.9 ms
- Rafraîchissements d'état : 430 ; âge des données au dernier bloc : 7.19 s ; changements de frais LP observés (pools à frais dynamiques) : 59
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 412 ; cycles déclenchés par événement : 158 ; avance médiane sur le rafraîchissement multicall : 365 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,242.47 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 477 pools, 279 jetons, 17784 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 97, aerodrome 199, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 170 (rejetés 2) → 575 jetons ; pools candidats 3720 (énumérés 294, par paires 0), mesurés 480, sous le plancher de 10000.0 $ : 3 → gardés 477 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2242.465806, 'cbBTC': 75805.716976, 'AERO': 0.595957}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,093,265 | 2,242.465826 | 54333392 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,819,403 | 0.029533 | 54333392 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,347,888 | 0.000013 | 54333392 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,193,160 | 0.029513 | 54333392 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,087,095 | 2,239.162052 | 54333392 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,391,745 | 107.539827 | 54333392 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,422,622 | 0.001549 | 54333392 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,835,463 | 1.677974 | 54333392 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,774,606 | 0.029532 | 54333392 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,230,224 | 2,238.715336 | 54333392 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,995,271 | 0.999831 | 54333392 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,322,834 | 42,623.541659 | 54333392 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,204,263 | 2,238.767543 | 54333392 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,557,922 | 0.029529 | 54333392 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,101,174 | 1,154,578.522736 | 54333392 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,742,750 | 0.000013 | 54333392 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,682,958 | 0.006663 | 54333392 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,670,317 | 0.000000 | 54333392 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,636,306 | 0.000013 | 54333392 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,604,056 | 0.015950 | 54333392 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,527,729 | 439.812919 | 54333392 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,509,755 | 0.000013 | 54333392 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,481,374 | 1.493422 | 54333392 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,012 | 0.819738 | 54333392 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,374,431 | 3,757.073913 | 54333392 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,327,093 | 2,242.909100 | 54333392 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,325,364 | 2,244.896073 | 54333392 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,269,574 | 14,865.017060 | 54333392 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,205,689 | 2,239.371904 | 54333392 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,702 | 76.955062 | 54333392 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,128 | 35,986,410.507242 | 54333392 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,051,298 | 107.612003 | 54333392 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,024,619 | 562,741.413400 | 54333392 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 998,821 | 22,537,302.896047 | 54333392 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 993,585 | 0.000000 | 54333392 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 986,205 | 19.739322 | 54333392 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 943,144 | 1,057.636477 | 54333392 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,072 | 2,228.788739 | 54333392 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 927,073 | 0.000013 | 54333392 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 915,386 | 74.782485 | 54333392 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 880,192 | 99,013.843178 | 54333392 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 811,013 | 0.048071 | 54333392 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 795,639 | 21.056579 | 54333392 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 793,419 | 3,730.217456 | 54333392 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,284 | 0.055294 | 54333392 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,748 | 0.799699 | 54333392 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 721,160 | 0.564974 | 54333392 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 692,746 | 4,959,129.129587 | 54333392 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 685,711 | 0.000253 | 54333392 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 683,461 | 0.584145 | 54333392 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 658,950 | 146,401.360874 | 54333392 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 649,623 | 0.000008 | 54333392 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 627,962 | 566,355.468447 | 54333392 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 589,114 | 2.473976 | 54333392 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 584,407 | 0.040507 | 54333392 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 529,998 | 1,057.319630 | 54333392 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 523,103 | 0.078147 | 54333392 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 513,229 | 923,172.781202 | 54333392 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | WETH/DRV | 3000 | 512,576 | 7,018.929564 | 54333392 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | WETH/USDC | 100 | 511,555 | 2,238.788372 | 54333392 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 587 ; routes examinées : 10439208 ; candidats optimisés : 22740 ; net attendu > 0 : 0 ; dernier cycle 252.2 ms
- Rejets (moteur) : {'spread_below_threshold': 10346233, 'liquidity_below_min': 69643, 'negative_expected_net': 22740, 'borrow_bound_too_small': 587, 'cycle_budget_exhausted': 5}
- Enregistrements de la session : 22740 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 22740} ; motifs de rejet : {'negative_expected_net': 22740}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 54332693 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.009240 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.85 |
| 54332694 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.009240 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.85 |
| 54332695 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.009240 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.85 |
| 54332696 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.009240 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.85 |
| 54332697 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.009240 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.85 |
| 54332717 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.009240 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.85 |
| 54332718 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.009240 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.85 |
| 54332719 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.009240 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.85 |
| 54332720 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.009240 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.85 |
| 54332720 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.009240 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -0.85 |

## Fiabilité et décision
- Observations ghost : 5976 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
