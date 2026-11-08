# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T12:31:55+00:00 ; durée 61.11 min ; blocs 54735330 → 54753654 (3091 vus)

## Connexion
- Requêtes RPC : 43703 ; erreurs : 0 ; latence p50/p95 : 198.0/1,357.8 ms
- Rafraîchissements d'état : 3091 ; âge des données au dernier bloc : 8.35 s ; changements de frais LP observés (pools à frais dynamiques) : 894
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3 ; cycles déclenchés par événement : 2 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,233.79 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 470 pools, 276 jetons, 17574 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 96, aerodrome 197, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3668 (énumérés 291, par paires 0), mesurés 473, sous le plancher de 10000.0 $ : 3 → gardés 470 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2233.787841, 'cbBTC': 75908.696855, 'AERO': 0.601233}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,297,420 | 2,233.789741 | 54753676 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,840,904 | 0.029488 | 54753676 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,269,186 | 0.000013 | 54753676 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,152,736 | 0.029508 | 54753676 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,524,521 | 2,237.352752 | 54753676 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,379,209 | 107.066273 | 54753676 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,398,048 | 0.001544 | 54753676 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,159,106 | 0.029477 | 54753676 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,818,346 | 1.668337 | 54753676 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,238,777 | 2,237.081166 | 54753676 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,986,562 | 0.999609 | 54753676 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,280,778 | 43,385.645567 | 54753676 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,180,487 | 2,237.132423 | 54753676 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,456,092 | 0.029492 | 54753676 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,095,364 | 1,152,023.747540 | 54753676 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,737,691 | 0.000013 | 54753676 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,654,670 | 0.006544 | 54753676 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,649,226 | 0.000013 | 54753676 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,617,396 | 0.000000 | 54753676 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,559,738 | 0.015412 | 54753676 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,514,374 | 447.029342 | 54753676 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,508,318 | 0.000013 | 54753676 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,489,354 | 1.402098 | 54753676 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,403 | 0.824204 | 54753676 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,384,564 | 3,730.553889 | 54753676 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,324,605 | 2,240.626325 | 54753676 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,295,520 | 2,243.430712 | 54753676 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,256,981 | 15,138.482968 | 54753676 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,187,788 | 2,237.922921 | 54753676 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,360 | 77.001845 | 54753676 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,095,675 | 37,171,603.593816 | 54753676 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,043,640 | 106.463704 | 54753676 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,006,194 | 587,582.125068 | 54753676 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 980,442 | 23,108,518.016850 | 54753676 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 970,297 | 20.704734 | 54753676 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 962,557 | 0.000000 | 54753676 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,960 | 2,228.787480 | 54753676 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 929,459 | 1,070.377360 | 54753676 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 925,293 | 0.000013 | 54753676 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 921,514 | 73.791093 | 54753676 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 861,485 | 102,501.700911 | 54753676 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 826,977 | 0.047859 | 54753676 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 784,677 | 3,702.134828 | 54753676 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 783,374 | 0.054864 | 54753676 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4600 | 775,888 | 21.820896 | 54753676 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 757,754 | 0.799805 | 54753676 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 713,982 | 0.562596 | 54753676 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 682,127 | 0.000253 | 54753676 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 680,429 | 5,101,398.354284 | 54753676 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 669,768 | 0.566479 | 54753676 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 652,975 | 0.000008 | 54753676 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 639,276 | 154,393.197681 | 54753676 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2153 | 611,619 | 590,283.552501 | 54753676 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 577,209 | 0.039591 | 54753676 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 554,292 | 2.471831 | 54753676 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 533,545 | 0.080372 | 54753676 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 523,648 | 887,766.100631 | 54753676 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 520,969 | 1,070.113491 | 54753676 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/USDC | 100 | 514,575 | 2,236.803113 | 54753676 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 513,760 | 6,932.670454 | 54753676 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 3092 ; routes examinées : 54338808 ; candidats optimisés : 136798 ; net attendu > 0 : 15 ; dernier cycle 328.1 ms
- Rejets (moteur) : {'spread_below_threshold': 53862052, 'liquidity_below_min': 339905, 'negative_expected_net': 136783, 'cycle_budget_exhausted': 53}
- Enregistrements de la session : 136798 ; net attendu > 0 : 15 ; simulés (eth_call de la vraie tx) : 9 (ok 6, échec 3) ; étiquettes ghost N+1 : 2/9 positives
- Décisions : {'REJECTED': 136798} ; motifs de rejet : {'below_safety_margin': 6, 'negative_expected_net': 136783, 'p_lower_below_threshold': 14, 'reliability_not_demonstrated': 1, 'simulation_failed': 3, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54752261 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 53.033191 USDC | 0.081325 USDC | 0.000000 USDC | 0.005016 USDC | 0.076309 USDC (0.0702 €) | — | 14.39 | 0.000 (n=104) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54751069 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 43.009373 USDC | 0.020298 USDC | 0.000000 USDC | 0.005015 USDC | 0.015283 USDC (0.0141 €) | 0.015283 USDC | 3.55 | 0.038 (n=377) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 54750059 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 19.333266 USDC | 0.015937 USDC | 0.000000 USDC | 0.005015 USDC | 0.010922 USDC (0.0100 €) | 0.010922 USDC | 5.65 | 0.075 (n=101) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54739538 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 36.431398 USDC | 0.014605 USDC | 0.000000 USDC | 0.005015 USDC | 0.009590 USDC (0.0088 €) | 0.009590 USDC | 2.63 | 0.049 (n=273) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54749851 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 19.945901 USDC | 0.011553 USDC | 0.000000 USDC | 0.005015 USDC | 0.006538 USDC (0.0060 €) | — | 3.28 | 0.035 (n=376) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 54751387 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 19.212820 USDC | 0.010745 USDC | 0.000000 USDC | 0.005015 USDC | 0.005730 USDC (0.0053 €) | 0.005730 USDC | 2.98 | 0.048 (n=276) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54750460 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.401332 USDC | 0.008795 USDC | 0.000000 USDC | 0.005015 USDC | 0.003780 USDC (0.0035 €) | 0.003780 USDC | 2.17 | 0.049 (n=275) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54749115 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 17.336217 USDC | 0.008707 USDC | 0.000000 USDC | 0.005017 USDC | 0.003690 USDC (0.0034 €) | 0.003690 USDC | 2.13 | 0.049 (n=274) | REJECTED | stale_data(4431ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54741281 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.003928 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0018 €) | — | 2.18 | 0.228 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54748063 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 24.811378 USDC | 0.006726 USDC | 0.000000 USDC | 0.005017 USDC | 0.001709 USDC (0.0016 €) | — | 0.69 | 0.049 (n=274) | REJECTED | below_safety_margin(1709<4962), p_lower_below_threshold(0.05<0.75) |
| 54752317 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 24.443487 USDC | 0.006595 USDC | 0.000000 USDC | 0.005015 USDC | 0.001580 USDC (0.0015 €) | — | 0.65 | 0.048 (n=277) | REJECTED | below_safety_margin(1580<4888), p_lower_below_threshold(0.05<0.75) |
| 54747242 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 12.283840 USDC | 0.006555 USDC | 0.000000 USDC | 0.005015 USDC | 0.001540 USDC (0.0014 €) | — | 1.25 | 0.050 (n=87) | REJECTED | below_safety_margin(1540<2456), p_lower_below_threshold(0.05<0.75) |
| 54747243 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 12.283840 USDC | 0.006555 USDC | 0.000000 USDC | 0.005015 USDC | 0.001540 USDC (0.0014 €) | — | 1.25 | 0.050 (n=87) | REJECTED | below_safety_margin(1540<2456), p_lower_below_threshold(0.05<0.75) |
| 54753169 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 14.927998 USDC | 0.006519 USDC | 0.000000 USDC | 0.005015 USDC | 0.001504 USDC (0.0014 €) | — | 1.01 | 0.048 (n=277) | REJECTED | below_safety_margin(1504<2985), p_lower_below_threshold(0.05<0.75) |
| 54746227 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 14.218411 USDC | 0.005765 USDC | 0.000000 USDC | 0.005016 USDC | 0.000749 USDC (0.0007 €) | — | 0.53 | 0.049 (n=274) | REJECTED | below_safety_margin(749<2843), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 6197 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
