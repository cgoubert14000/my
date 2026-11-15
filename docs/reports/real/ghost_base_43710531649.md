# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-15T13:50:08+00:00 ; durée 118.5 min ; blocs 57765594 → 57801108 (11020 vus)

## Connexion
- Requêtes RPC : 104805 ; erreurs : 10 ; latence p50/p95 : 86.7/899.8 ms
- Rafraîchissements d'état : 11020 ; âge des données au dernier bloc : 11.65 s ; changements de frais LP observés (pools à frais dynamiques) : 3701
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2743 ; cycles déclenchés par événement : 880 ; avance médiane sur le rafraîchissement multicall : 106 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,833.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 436 pools, 253 jetons, 13300 routes
- Par DEX : uniswap_v3 130, aerodrome_slipstream 88, aerodrome 177, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 149 (rejetés 2) → 554 jetons ; pools candidats 3593 (énumérés 264, par paires 0), mesurés 438, sous le plancher de 10000.0 $ : 2 → gardés 436 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 1831.864662, 'cbBTC': 65446.070264, 'AERO': 0.441982}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 87,360,050 | 1,833.418354 | 57801135 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,103,694 | 0.027977 | 57801135 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,797,713 | 0.027973 | 57801135 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,637,514 | 0.000015 | 57801135 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 6,489,388 | 92.996633 | 57801135 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 5,899,982 | 1,832.858519 | 57801135 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,212,246 | 0.027989 | 57801135 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,773,023 | 1,833.662723 | 57801135 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | USDC/AERO | 3000 | 3,760,372 | 2.254087 | 57801135 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,449,328 | 0.999102 | 57801135 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,784,308 | 40,578.246958 | 57801135 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 177 | 2,481,077 | 1,833.409236 | 57801135 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,913,523 | 0.028008 | 57801135 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,713,407 | 1,160,642.103016 | 57801135 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,690,007 | 0.017481 | 57801135 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,517,454 | 0.000015 | 57801135 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,155 | 0.842737 | 57801135 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,404,083 | 0.000000 | 57801135 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,321,643 | 0.006493 | 57801135 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,299,514 | 0.000015 | 57801135 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,246,812 | 440.519066 | 57801135 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,219,724 | 0.000015 | 57801135 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,071,349 | 15,744.212419 | 57801135 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,067,352 | 4,133.414482 | 57801135 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | USDC/SEND | 3000 | 1,061,409 | 86.252803 | 57801135 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/USDC | 3000 | 1,045,623 | 1,834.858822 | 57801135 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,006,763 | 1,833.698714 | 57801135 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/VVV | 10000 | 993,949 | 92.668956 | 57801135 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 975,581 | 20.377539 | 57801135 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| pancakeswap_v3 | WETH/USDC | 500 | 972,312 | 1,832.768538 | 57801135 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 944,221 | 32,426,380.833785 | 57801135 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 850,811 | 552,836.316647 | 57801135 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/MORPHO | 3000 | 829,615 | 1,028.727548 | 57801135 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 823,052 | 0.050769 | 57801135 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | DRB/WETH | 10000 | 807,940 | 0.000000 | 57801135 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 805,548 | 0.001456 | 57801135 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 800,069 | 23,423,858.866242 | 57801135 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 732,328 | 87.703821 | 57801135 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 717,227 | 1,825.746794 | 57801135 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | QUID/USDC | 100 | 691,533 | 0.042590 | 57801135 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 679,819 | 26.240205 | 57801135 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 100 | 628,338 | 1,833.595663 | 57801135 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 622,480 | 0.798414 | 57801135 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 594,204 | 0.444119 | 57801135 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/AERO | 10000 | 588,090 | 4,162.576168 | 57801135 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 576,168 | 4,809,426.064821 | 57801135 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 548,880 | 0.449827 | 57801135 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 538,171 | 147,367.234603 | 57801135 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | USDC/MAI (stable) | 3000 | 521,922 | 1.385672 | 57801135 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 519,101 | 551,908.339959 | 57801135 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | VIRTUAL/WETH | 10000 | 500,636 | 0.000245 | 57801135 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | FLOCK/USDC | 3000 | 494,459 | 0.031362 | 57801135 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 474,554 | 0.000007 | 57801135 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/USDT | 8 | 452,809 | 1.000482 | 57801135 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 434,875 | 1,028.538644 | 57801135 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 425,027 | 0.059840 | 57801135 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 405,485 | 0.563234 | 57801135 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome | cbBTC/EDGE | 7000 | 392,487 | 894,085.946953 | 57801135 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 391,219 | 25.035402 | 57801135 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | WETH/msETH (stable) | 500 | 382,838 | 2.326203 | 57801135 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |

## Recherche d'opportunités
- Cycles : 11899 ; routes examinées : 158163600 ; candidats optimisés : 9224 ; net attendu > 0 : 0 ; dernier cycle 0.0 ms
- Rejets (moteur) : {'spread_below_threshold': 154845679, 'liquidity_below_min': 2524160, 'borrow_bound_too_small': 11892, 'negative_expected_net': 9224}
- Enregistrements de la session : 0 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {} ; motifs de rejet : {}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

## Fiabilité et décision
- Observations ghost : 8573 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
