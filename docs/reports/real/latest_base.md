# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T14:23:17+00:00 ; durée 264.67 min ; blocs 55139673 → 55219032 (8435 vus)

## Connexion
- Requêtes RPC : 132143 ; erreurs : 5 ; latence p50/p95 : 573.8/1,884.1 ms
- Rafraîchissements d'état : 8435 ; âge des données au dernier bloc : 8.47 s ; changements de frais LP observés (pools à frais dynamiques) : 7629
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12556 ; cycles déclenchés par événement : 3715 ; avance médiane sur le rafraîchissement multicall : 586 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,120.68 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 465 pools, 272 jetons, 17388 routes
- Par DEX : uniswap_v3 131, aerodrome_slipstream 99, aerodrome 193, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3672 (énumérés 289, par paires 0), mesurés 467, sous le plancher de 10000.0 $ : 2 → gardés 465 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2109.380964, 'cbBTC': 74235.499826, 'AERO': 0.565393}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 138,645,636 | 2,120.676846 | 55219071 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,459,985 | 0.028431 | 55219071 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,338,239 | 0.000013 | 55219071 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,705,335 | 0.028399 | 55219071 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,311,227 | 2,119.888944 | 55219071 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,210,094 | 101.009110 | 55219071 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,265,656 | 0.001527 | 55219071 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,968,632 | 0.028433 | 55219071 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,602,776 | 1.730076 | 55219071 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,967,481 | 2,120.026961 | 55219071 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,928,763 | 0.998722 | 55219071 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,123,355 | 43,144.092236 | 55219071 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 549 | 3,024,143 | 2,119.819593 | 55219071 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,357,091 | 0.028390 | 55219071 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,992,598 | 1,148,168.304509 | 55219071 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,702,731 | 0.000013 | 55219071 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,700,594 | 0.000013 | 55219071 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,598,976 | 0.006777 | 55219071 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,567,686 | 0.015539 | 55219071 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,556,919 | 0.000000 | 55219071 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55219071 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,462,228 | 423.053018 | 55219071 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,158 | 0.821587 | 55219071 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,433,173 | 0.000013 | 55219071 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,326,441 | 3,674.374060 | 55219071 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,291,014 | 2,120.200477 | 55219071 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,248,257 | 14,902.038412 | 55219071 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,219,380 | 2,122.970379 | 55219071 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,257 | 79.257778 | 55219071 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,092,776 | 2,119.564678 | 55219071 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,045,372 | 36,600,545.361199 | 55219071 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,043,608 | 101.297806 | 55219071 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 969,657 | 562,243.478973 | 55219071 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,963 | 21.254703 | 55219071 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 927,719 | 23,252,265.568290 | 55219071 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 925,585 | 0.000013 | 55219071 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 911,607 | 2,109.526269 | 55219071 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 909,409 | 1,024.231432 | 55219071 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 909,212 | 75.801539 | 55219071 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | DRB/WETH | 10000 | 902,969 | 0.000000 | 55219071 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 881,014 | 0.047696 | 55219071 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 819,770 | 102,025.224188 | 55219071 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 777,427 | 21.772010 | 55219071 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 768,121 | 0.052655 | 55219071 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 748,759 | 3,692.738593 | 55219071 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 719,981 | 0.798479 | 55219071 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 702,495 | 0.544056 | 55219071 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 659,649 | 4,892,326.464761 | 55219071 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 645,400 | 0.527352 | 55219071 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 625,769 | 0.000008 | 55219071 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 609,267 | 153,301.959964 | 55219071 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 594,717 | 0.000255 | 55219071 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 594,323 | 561,198.121301 | 55219071 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 573,102 | 0.039121 | 55219071 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 532,131 | 2.381266 | 55219071 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 517,280 | 1,024.285654 | 55219071 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 507,265 | 919,905.872028 | 55219071 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,575 | 1.001235 | 55219071 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 484,240 | 0.070331 | 55219071 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 482,927 | 7,071.670171 | 55219071 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 12149 ; routes examinées : 211246812 ; candidats optimisés : 839885 ; net attendu > 0 : 2085 ; dernier cycle 365.8 ms
- Rejets (moteur) : {'spread_below_threshold': 207353797, 'liquidity_below_min': 2992922, 'negative_expected_net': 837800, 'borrow_bound_too_small': 39035, 'pool_quarantined': 15816, 'cycle_budget_exhausted': 5357}
- Enregistrements de la session : 839885 ; net attendu > 0 : 2085 ; simulés (eth_call de la vraie tx) : 129 (ok 56, échec 73) ; étiquettes ghost N+1 : 39/113 positives
- Décisions : {'REJECTED': 839885} ; motifs de rejet : {'below_safety_margin': 1429, 'negative_expected_net': 837800, 'p_lower_below_threshold': 2029, 'reliability_not_demonstrated': 56, 'sim_below_estimate': 20, 'simulated_net_nonpositive': 7, 'simulation_failed': 73, 'stale_data': 685}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55182011 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 486.719375 USDC | 1.582566 USDC | 0.000000 USDC | 0.006703 USDC | 1.575863 USDC (1.4498 €) | — | 32.38 | 0.026 (n=55) | REJECTED | stale_data(5103ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 55182011 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.229556 WETH | 0.000746 WETH | 0.000000 WETH | 0.000003 WETH | 0.000743 WETH (1.4472 €) | — | 32.37 | 0.026 (n=55) | REJECTED | stale_data(5096ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 55182011 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 479.507987 USDC | 1.567733 USDC | 0.000000 USDC | 0.006703 USDC | 1.561030 USDC (1.4361 €) | — | 32.55 | 0.026 (n=55) | REJECTED | stale_data(5090ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 55182011 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.226033 WETH | 0.000739 WETH | 0.000000 WETH | 0.000003 WETH | 0.000736 WETH (1.4337 €) | — | 32.56 | 0.026 (n=55) | REJECTED | stale_data(5084ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 55182011 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 453.688411 USDC | 1.502230 USDC | 0.000000 USDC | 0.006703 USDC | 1.495527 USDC (1.3759 €) | — | 32.96 | 0.026 (n=55) | REJECTED | stale_data(5077ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 55182011 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.214123 WETH | 0.000709 WETH | 0.000000 WETH | 0.000003 WETH | 0.000705 WETH (1.3740 €) | — | 32.94 | 0.026 (n=55) | REJECTED | stale_data(5071ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 55180530 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.190815 WETH | 0.000679 WETH | 0.000000 WETH | 0.000002 WETH | 0.000677 WETH (1.3188 €) | — | 35.48 | 0.000 (n=22) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55180530 | WETH→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.226294 WETH | 0.000646 WETH | 0.000000 WETH | 0.000002 WETH | 0.000644 WETH (1.2539 €) | — | 28.45 | 0.000 (n=22) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55180530 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.181758 WETH | 0.000630 WETH | 0.000000 WETH | 0.000003 WETH | 0.000627 WETH (1.2217 €) | — | 34.51 | 0.027 (n=54) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 55180530 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 384.349973 USDC | 1.332766 USDC | 0.000000 USDC | 0.006383 USDC | 1.326383 USDC (1.2203 €) | — | 34.51 | 0.027 (n=54) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 55182011 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 443.280457 USDC | 1.308503 USDC | 0.000000 USDC | 0.006703 USDC | 1.301800 USDC (1.1977 €) | — | 29.37 | 0.026 (n=55) | REJECTED | stale_data(5141ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 55182011 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.209127 WETH | 0.000617 WETH | 0.000000 WETH | 0.000003 WETH | 0.000614 WETH (1.1962 €) | — | 29.37 | 0.026 (n=55) | REJECTED | stale_data(5135ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 55182011 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 433.779740 USDC | 1.280584 USDC | 0.000000 USDC | 0.006703 USDC | 1.273881 USDC (1.1720 €) | — | 29.37 | 0.026 (n=55) | REJECTED | stale_data(5129ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 55182011 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.204607 WETH | 0.000604 WETH | 0.000000 WETH | 0.000003 WETH | 0.000601 WETH (1.1707 €) | — | 29.37 | 0.026 (n=55) | REJECTED | stale_data(5123ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 55180530 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.176096 WETH | 0.000601 WETH | 0.000000 WETH | 0.000003 WETH | 0.000598 WETH (1.1645 €) | — | 33.95 | 0.027 (n=54) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 55180530 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 372.149938 USDC | 1.270427 USDC | 0.000000 USDC | 0.006383 USDC | 1.264044 USDC (1.1629 €) | — | 33.97 | 0.027 (n=54) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 55180530 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.172488 WETH | 0.000589 WETH | 0.000000 WETH | 0.000003 WETH | 0.000586 WETH (1.1405 €) | — | 33.95 | 0.027 (n=54) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 55180530 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 364.248248 USDC | 1.244145 USDC | 0.000000 USDC | 0.006383 USDC | 1.237762 USDC (1.1387 €) | — | 33.98 | 0.027 (n=54) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 55180530 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.175634 WETH | 0.000587 WETH | 0.000000 WETH | 0.000003 WETH | 0.000584 WETH (1.1376 €) | — | 33.25 | 0.027 (n=54) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 55180530 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 370.921653 USDC | 1.241162 USDC | 0.000000 USDC | 0.006383 USDC | 1.234779 USDC (1.1360 €) | — | 33.29 | 0.027 (n=54) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 55180530 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.172655 WETH | 0.000577 WETH | 0.000000 WETH | 0.000003 WETH | 0.000574 WETH (1.1183 €) | — | 33.25 | 0.027 (n=54) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 55182011 | WETH→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.213864 WETH | 0.000576 WETH | 0.000000 WETH | 0.000002 WETH | 0.000574 WETH (1.1181 €) | — | 26.84 | 0.000 (n=24) | REJECTED | stale_data(5159ms>4000.0), reliability_not_demonstrated |
| 55180530 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 364.756326 USDC | 1.220083 USDC | 0.000000 USDC | 0.006383 USDC | 1.213700 USDC (1.1166 €) | — | 33.27 | 0.027 (n=54) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 55180530 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.115976 WETH | 0.000388 WETH | 0.000000 WETH | 0.000003 WETH | 0.000385 WETH (0.7492 €) | — | 33.16 | 0.027 (n=54) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 55180530 | WETH→[aerodrome]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.131262 WETH | 0.000386 WETH | 0.000000 WETH | 0.000003 WETH | 0.000383 WETH (0.7468 €) | — | 29.21 | 0.126 (n=23) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 6853 ; taux observé 0.180 ; borne inférieure crédible (0.9) 0.174 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
