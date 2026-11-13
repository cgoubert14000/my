# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-13T18:22:10+00:00 ; durée 201.18 min ; blocs 56958393 → 57018742 (12946 vus)

## Connexion
- Requêtes RPC : 146258 ; erreurs : 229 ; latence p50/p95 : 260.3/1,100.0 ms
- Rafraîchissements d'état : 12938 ; âge des données au dernier bloc : 6.62 s ; changements de frais LP observés (pools à frais dynamiques) : 10478
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 20762 ; cycles déclenchés par événement : 6554 ; avance médiane sur le rafraîchissement multicall : 310 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,939.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 263 jetons, 14680 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 185, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 155 (rejetés 2) → 560 jetons ; pools candidats 3602 (énumérés 281, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 1950.558247, 'cbBTC': 68886.665163, 'AERO': 0.48173}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 125,397,805 | 1,939.061902 | 57018763 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 14,718,693 | 0.028155 | 57018763 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,250,201 | 0.028120 | 57018763 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 7,063,545 | 0.000015 | 57018763 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,681,425 | 1,938.711012 | 57018763 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,558,174 | 101.823461 | 57018763 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,342,845 | 0.028156 | 57018763 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,945,238 | 2.077057 | 57018763 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,908,655 | 1,938.059259 | 57018763 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,629,452 | 0.998515 | 57018763 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,883,303 | 42,326.003396 | 57018763 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 107 | 2,640,830 | 1,938.375015 | 57018763 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,070,794 | 0.028109 | 57018763 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,831,385 | 1,136,370.993126 | 57018763 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,683,251 | 0.017367 | 57018763 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,550,603 | 0.000015 | 57018763 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,510,569 | 0.000015 | 57018763 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,543 | 0.835716 | 57018763 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,458,351 | 0.000000 | 57018763 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,430,227 | 0.006563 | 57018763 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,325,094 | 432.894557 | 57018763 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,318,481 | 0.000015 | 57018763 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,146,484 | 4,024.490364 | 57018763 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,137,221 | 15,365.117260 | 57018763 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,093,528 | 1,942.513132 | 57018763 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,061,189 | 86.288594 | 57018763 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v2 | WETH/USDC | 3000 | 1,049,713 | 1,938.530412 | 57018763 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,045,314 | 1.383906 | 57018763 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,042,277 | 1,938.643811 | 57018763 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,003,753 | 18.754367 | 57018763 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 991,009 | 102.294010 | 57018763 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/doginme | 10000 | 990,195 | 33,146,451.471097 | 57018763 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 907,695 | 524,280.436076 | 57018763 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 865,953 | 0.001523 | 57018763 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | USDC/VVV | 3000 | 864,014 | 0.052494 | 57018763 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 862,529 | 22,668,399.843655 | 57018763 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 840,057 | 982.377673 | 57018763 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 779,291 | 0.000000 | 57018763 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 758,434 | 81.770573 | 57018763 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 743,143 | 0.049188 | 57018763 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 739,788 | 23.365149 | 57018763 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 738,611 | 1,931.926746 | 57018763 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/wstETH | 3000 | 657,420 | 0.800670 | 57018763 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 652,045 | 0.518984 | 57018763 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/AERO | 10000 | 639,022 | 4,053.582496 | 57018763 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 613,365 | 4,741,197.591412 | 57018763 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 603,637 | 0.458255 | 57018763 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 596,664 | 133,997.029539 | 57018763 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 564,002 | 528,353.163263 | 57018763 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | VIRTUAL/WETH | 10000 | 553,250 | 0.000266 | 57018763 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | FLOCK/USDC | 3000 | 548,636 | 0.036746 | 57018763 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v3 | WETH/USDC | 100 | 534,077 | 1,938.147848 | 57018763 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 510,055 | 0.000007 | 57018763 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | ELSA/USDC | 100 | 475,880 | 0.068939 | 57018763 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 471,459 | 982.897112 | 57018763 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | USDC/USDT | 11 | 448,527 | 1.001105 | 57018763 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 444,750 | 0.505351 | 57018763 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/UNI | 10000 | 419,565 | 333.657424 | 57018763 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 416,571 | 24.465768 | 57018763 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 414,376 | 886,978.589891 | 57018763 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 19491 ; routes examinées : 286127880 ; candidats optimisés : 33691 ; net attendu > 0 : 0 ; dernier cycle 1262.7 ms
- Rejets (moteur) : {'spread_below_threshold': 280051415, 'liquidity_below_min': 4198538, 'negative_expected_net': 33691, 'borrow_bound_too_small': 10846, 'cycle_budget_exhausted': 120}
- Enregistrements de la session : 6 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 6} ; motifs de rejet : {'negative_expected_net': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 57011057 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 57011057 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 57014342 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 57014342 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 57014342 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 57014342 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC | 0.999999 USDC | -0.001163 USDC | 0.000000 USDC | 0.005574 USDC | -0.0062 | -67.37 |

## Fiabilité et décision
- Observations ghost : 8573 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
