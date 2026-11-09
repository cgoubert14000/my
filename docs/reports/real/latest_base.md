# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T04:24:20+00:00 ; durée 3.08 min ; blocs 55038467 → 55039418 (146 vus)

## Connexion
- Requêtes RPC : 1974 ; erreurs : 0 ; latence p50/p95 : 363.3/1,695.5 ms
- Rafraîchissements d'état : 146 ; âge des données au dernier bloc : 8.94 s ; changements de frais LP observés (pools à frais dynamiques) : 83
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 176 ; cycles déclenchés par événement : 59 ; avance médiane sur le rafraîchissement multicall : 402 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,141.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 467 pools, 272 jetons, 17562 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 194, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3664 (énumérés 288, par paires 0), mesurés 469, sous le plancher de 10000.0 $ : 2 → gardés 467 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2141.212816, 'cbBTC': 74926.035696, 'AERO': 0.58265}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,213,577 | 2,141.212766 | 55039405 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,477,272 | 0.028590 | 55039405 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,992,099 | 0.000013 | 55039405 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,820,112 | 0.028533 | 55039405 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,898,179 | 2,140.023530 | 55039405 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,167,937 | 104.259928 | 55039405 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,290,242 | 0.001527 | 55039405 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,632,308 | 1.718518 | 55039405 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,619,701 | 0.028579 | 55039405 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,941,867 | 0.999218 | 55039405 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,860,005 | 2,140.065843 | 55039405 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,160,697 | 42,950.594627 | 55039405 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,051,651 | 2,140.265016 | 55039405 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,384,619 | 0.028551 | 55039405 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,002,174 | 1,159,342.676479 | 55039405 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,712,584 | 0.000013 | 55039405 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,615,691 | 0.006668 | 55039405 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,606,505 | 0.000013 | 55039412 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,565,043 | 0.000000 | 55039405 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,551,675 | 0.015473 | 55039418 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,099 | 1.421539 | 55039405 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,465,307 | 433.957359 | 55039405 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,412,042 | 0.000013 | 55039405 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,336,894 | 3,680.100380 | 55039405 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,297,156 | 2,142.877788 | 55039405 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,242,364 | 15,172.179322 | 55039405 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,226,454 | 2,144.904406 | 55039405 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,120,777 | 77.357246 | 55039405 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,097,688 | 2,140.046877 | 55039405 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,814 | 37,092,779.018412 | 55039405 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,020,161 | 105.025341 | 55039405 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 963,787 | 588,898.684941 | 55039405 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 952,246 | 21.930985 | 55039405 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 948,931 | 22,747,860.254386 | 55039405 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 928,593 | 0.000013 | 55039405 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 918,047 | 74.349545 | 55039405 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | DRB/WETH | 10000 | 914,688 | 0.000000 | 55039405 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 913,806 | 2,137.198475 | 55039405 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 908,867 | 1,044.342905 | 55039405 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 856,251 | 0.824196 | 55039405 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | WETH/EDEL | 7000 | 833,628 | 100,581.196815 | 55039405 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 817,897 | 0.048671 | 55039405 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 780,273 | 0.054409 | 55039405 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 755,585 | 3,677.033511 | 55039405 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 753,095 | 22.755175 | 55039405 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 725,651 | 0.801347 | 55039405 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 701,125 | 0.540680 | 55039405 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 654,886 | 5,060,013.820255 | 55039405 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 643,735 | 0.524790 | 55039405 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 630,065 | 0.000008 | 55039405 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 620,663 | 150,538.805123 | 55039405 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 596,634 | 0.000251 | 55039405 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 585,676 | 588,947.990018 | 55039405 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,744 | 0.038565 | 55039405 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 531,416 | 2.463045 | 55039405 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 515,477 | 1,044.499784 | 55039405 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 507,578 | 927,237.561076 | 55039405 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,516 | 1.001290 | 55039405 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| uniswap_v3 | WETH/USDC | 100 | 492,005 | 2,140.277152 | 55039408 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 489,872 | 7,006.330480 | 55039405 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 204 ; routes examinées : 3582648 ; candidats optimisés : 8366 ; net attendu > 0 : 0 ; dernier cycle 86.1 ms
- Rejets (moteur) : {'spread_below_threshold': 3519023, 'liquidity_below_min': 55055, 'negative_expected_net': 8366, 'borrow_bound_too_small': 204}
- Enregistrements de la session : 8366 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 8366} ; motifs de rejet : {'negative_expected_net': 8366}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 55038502 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 3.092617 USDC | 0.000521 USDC | 0.000000 USDC | 0.004808 USDC | -0.0039 | -13.86 |
| 55038504 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 3.092617 USDC | 0.000521 USDC | 0.000000 USDC | 0.004808 USDC | -0.0039 | -13.86 |
| 55038505 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 3.092617 USDC | 0.000521 USDC | 0.000000 USDC | 0.004808 USDC | -0.0039 | -13.86 |
| 55038506 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 3.092617 USDC | 0.000521 USDC | 0.000000 USDC | 0.004808 USDC | -0.0039 | -13.86 |
| 55038507 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 3.092617 USDC | 0.000521 USDC | 0.000000 USDC | 0.004808 USDC | -0.0039 | -13.86 |
| 55038508 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 3.092617 USDC | 0.000521 USDC | 0.000000 USDC | 0.004808 USDC | -0.0039 | -13.86 |
| 55038570 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.001298 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0041 | -16.06 |
| 55038570 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.001298 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0041 | -16.06 |
| 55038570 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2.723526 USDC | 0.000348 USDC | 0.000000 USDC | 0.004812 USDC | -0.0041 | -16.39 |
| 55038570 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2.723526 USDC | 0.000348 USDC | 0.000000 USDC | 0.004812 USDC | -0.0041 | -16.39 |

## Fiabilité et décision
- Observations ghost : 6650 ; taux observé 0.175 ; borne inférieure crédible (0.9) 0.169 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
