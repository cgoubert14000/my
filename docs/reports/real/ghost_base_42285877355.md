# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T22:02:39+00:00 ; durée 108.4 min ; blocs 54028370 → 54060820 (6280 vus)

## Connexion
- Requêtes RPC : 78449 ; erreurs : 0 ; latence p50/p95 : 309.5/1,650.0 ms
- Rafraîchissements d'état : 6280 ; âge des données au dernier bloc : 15.96 s ; changements de frais LP observés (pools à frais dynamiques) : 2401
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6519 ; cycles déclenchés par événement : 2663 ; avance médiane sur le rafraîchissement multicall : 433 ms
- Gaz : base fee 0.005010 gwei ; prix ETH (pool le plus profond) : 2,237.08 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 482 pools, 282 jetons, 17936 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 103, aerodrome 198 (quarantaine 2), pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3742 (énumérés 299, par paires 0), mesurés 485, sous le plancher de 10000.0 $ : 3 → gardés 482 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2228.731074, 'cbBTC': 75812.648558, 'AERO': 0.606832}
- Pools en quarantaine : 2 — aerodrome:fBOMB/cbBTC@0x3d36Cf: simulation failed ×5 (model/chain mismatch) — until block 54060884; aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 54060884

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,361,049 | 2,237.079525 | 54060872 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,759,111 | 0.029535 | 54060872 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,399,227 | 0.000013 | 54060872 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,149,265 | 0.029462 | 54060872 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,009,192 | 2,242.769879 | 54060872 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,406,108 | 106.622815 | 54060872 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,427,257 | 0.001559 | 54060872 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,925,789 | 1.619560 | 54060872 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,738,237 | 0.029527 | 54060872 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,160,419 | 2,242.914963 | 54060872 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,992,117 | 0.998508 | 54060872 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,336,180 | 42,080.315078 | 54060872 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,201,824 | 2,242.988590 | 54060872 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2560 | 2,557,500 | 0.029475 | 54060872 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,085,104 | 1,166,818.518415 | 54060872 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,743,920 | 0.007001 | 54060872 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,734,178 | 0.000013 | 54060872 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,660,910 | 0.000000 | 54060872 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,653,738 | 0.000013 | 54060872 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,621,799 | 0.016214 | 54060872 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54060872 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,537,338 | 0.000013 | 54060872 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,536,756 | 427.600668 | 54060872 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,358 | 0.818979 | 54060872 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,402,439 | 3,631.647378 | 54060872 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,325,473 | 2,236.462362 | 54060872 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,323,582 | 2,236.795637 | 54060872 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,281,477 | 14,521.576343 | 54060872 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,166,311 | 2,242.594175 | 54060872 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,122,706 | 77.091623 | 54060872 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,099,824 | 36,916,209.311164 | 54060872 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,052,669 | 106.727216 | 54060872 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,027,541 | 554,471.546907 | 54060872 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,021,581 | 0.000000 | 54060872 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,000,576 | 22,508,235.864785 | 54060872 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 977,276 | 20.264381 | 54060872 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 944,464 | 1,055.889792 | 54060872 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 935,718 | 2,225.576719 | 54060872 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 368 | 924,102 | 0.000013 | 54060872 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 921,109 | 73.856041 | 54060872 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 884,943 | 97,483.286628 | 54060872 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 839,127 | 0.000527 | 54060872 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 813,438 | 0.047690 | 54060872 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 806,632 | 3,655.879950 | 54060872 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4535 | 806,164 | 20.668502 | 54060872 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 794,356 | 0.056497 | 54060872 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,921 | 0.799699 | 54060872 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 725,252 | 0.570739 | 54060872 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 696,382 | 4,883,389.796727 | 54060872 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 689,738 | 0.000258 | 54060872 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 666,269 | 0.556660 | 54060872 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 663,546 | 143,672.700517 | 54060872 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 662,190 | 0.000008 | 54060872 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2150 | 631,302 | 555,764.541467 | 54060872 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 589,845 | 0.041101 | 54060872 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 588,124 | 2.471342 | 54060872 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 529,026 | 1,056.087794 | 54060872 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 528,031 | 871,096.873719 | 54060872 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 524,439 | 0.078529 | 54060872 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 519,580 | 2,242.880321 | 54060872 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 8942 ; routes examinées : 160383712 ; candidats optimisés : 484105 ; net attendu > 0 : 51 ; dernier cycle 329.6 ms
- Rejets (moteur) : {'spread_below_threshold': 157592396, 'liquidity_below_min': 2282763, 'negative_expected_net': 484054, 'pool_quarantined': 14896, 'borrow_bound_too_small': 8940, 'cycle_budget_exhausted': 612}
- Enregistrements de la session : 484105 ; net attendu > 0 : 51 ; simulés (eth_call de la vraie tx) : 16 (ok 0, échec 16) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 484105} ; motifs de rejet : {'below_safety_margin': 35, 'negative_expected_net': 484054, 'p_lower_below_threshold': 48, 'price_impact': 15, 'reliability_not_demonstrated': 3, 'simulation_failed': 16, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54060684 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 837.885496 USDC | 0.111051 USDC | 0.000000 USDC | 0.005054 USDC | 0.105997 USDC (0.0975 €) | — | 1.27 | 0.047 (n=247) | REJECTED | below_safety_margin(105997<167577), p_lower_below_threshold(0.05<0.75) |
| 54060684 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.374447 WETH | 0.000050 WETH | 0.000000 WETH | 0.000002 WETH | 0.000047 WETH (0.0972 €) | — | 1.26 | 0.047 (n=247) | REJECTED | below_safety_margin(47277268623202<74889389706557), p_lower_below_threshold(0.05<0.75) |
| 54060684 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 757.927748 USDC | 0.070574 USDC | 0.000000 USDC | 0.006764 USDC | 0.063810 USDC (0.0587 €) | — | 0.84 | 0.029 (n=28) | REJECTED | below_safety_margin(63810<151585), reliability_not_demonstrated |
| 54060684 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.008755 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0585 €) | — | 0.96 | 0.029 (n=28) | REJECTED | below_safety_margin(84<175), reliability_not_demonstrated |
| 54060684 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.329385 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0581 €) | — | 0.86 | 0.029 (n=28) | REJECTED | below_safety_margin(28267304274076<65877091333329), reliability_not_demonstrated |
| 54057958 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 68.807723 USDC | 0.056511 USDC | 0.000000 USDC | 0.005004 USDC | 0.051507 USDC (0.0474 €) | — | 7.49 | 0.026 (n=319) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54060684 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 304.872182 USDC | 0.038933 USDC | 0.000000 USDC | 0.005395 USDC | 0.033538 USDC (0.0309 €) | — | 1.10 | 0.053 (n=82) | REJECTED | below_safety_margin(33538<60974), p_lower_below_threshold(0.05<0.75) |
| 54060684 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.136291 WETH | 0.000017 WETH | 0.000000 WETH | 0.000002 WETH | 0.000015 WETH (0.0308 €) | — | 1.10 | 0.053 (n=82) | REJECTED | below_safety_margin(14951957098203<27258137402606), p_lower_below_threshold(0.05<0.75) |
| 54060684 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 242.850703 USDC | 0.021390 USDC | 0.000000 USDC | 0.006764 USDC | 0.014626 USDC (0.0135 €) | — | 0.60 | 0.171 (n=1029) | REJECTED | below_safety_margin(14626<48570), p_lower_below_threshold(0.17<0.75) |
| 54060684 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0132 €) | — | 0.63 | 0.171 (n=1029) | REJECTED | below_safety_margin(19<60), p_lower_below_threshold(0.17<0.75) |
| 54060684 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.102975 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | — | 0.61 | 0.171 (n=1029) | REJECTED | below_safety_margin(6327976085958<20595093319702), p_lower_below_threshold(0.17<0.75) |
| 54042831 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.102166 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(2470642400570<20433118273996), p_lower_below_threshold(0.05<0.75) |
| 54042832 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.102166 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(2470642400570<20433118273996), p_lower_below_threshold(0.05<0.75) |
| 54042831 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 226.836687 USDC | 0.010504 USDC | 0.000000 USDC | 0.005007 USDC | 0.005497 USDC (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(5497<45367), p_lower_below_threshold(0.05<0.75) |
| 54042832 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 226.836687 USDC | 0.010504 USDC | 0.000000 USDC | 0.005007 USDC | 0.005497 USDC (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(5497<45367), p_lower_below_threshold(0.05<0.75) |
| 54029815 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 28.179939 USDC | 0.009524 USDC | 0.000000 USDC | 0.005016 USDC | 0.004508 USDC (0.0041 €) | — | 1.60 | 0.047 (n=247) | REJECTED | below_safety_margin(4508<5635), p_lower_below_threshold(0.05<0.75) |
| 54029969 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.735224 USDC | 0.009268 USDC | 0.000000 USDC | 0.005016 USDC | 0.004252 USDC (0.0039 €) | — | 1.53 | 0.047 (n=247) | REJECTED | below_safety_margin(4252<5547), p_lower_below_threshold(0.05<0.75) |
| 54029971 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.735224 USDC | 0.009268 USDC | 0.000000 USDC | 0.005016 USDC | 0.004252 USDC (0.0039 €) | — | 1.53 | 0.047 (n=247) | REJECTED | below_safety_margin(4252<5547), p_lower_below_threshold(0.05<0.75) |
| 54029970 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.735224 USDC | 0.009268 USDC | 0.000000 USDC | 0.005016 USDC | 0.004252 USDC (0.0039 €) | — | 1.53 | 0.047 (n=247) | REJECTED | below_safety_margin(4252<5547), p_lower_below_threshold(0.05<0.75) |
| 54053172 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.327820 USDC | 0.008809 USDC | 0.000000 USDC | 0.005007 USDC | 0.003802 USDC (0.0035 €) | — | 1.39 | 0.047 (n=247) | REJECTED | below_safety_margin(3802<5465), p_lower_below_threshold(0.05<0.75) |
| 54056604 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 17.713838 USDC | 0.008325 USDC | 0.000000 USDC | 0.005005 USDC | 0.003320 USDC (0.0031 €) | — | 1.87 | 0.047 (n=247) | REJECTED | below_safety_margin(3320<3542), p_lower_below_threshold(0.05<0.75) |
| 54056604 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 17.713838 USDC | 0.008325 USDC | 0.000000 USDC | 0.005005 USDC | 0.003320 USDC (0.0031 €) | — | 1.87 | 0.047 (n=247) | REJECTED | below_safety_margin(3320<3542), p_lower_below_threshold(0.05<0.75) |
| 54046177 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.752637 USDC | 0.008278 USDC | 0.000000 USDC | 0.005007 USDC | 0.003271 USDC (0.0030 €) | — | 1.84 | 0.047 (n=247) | REJECTED | below_safety_margin(3271<3550), p_lower_below_threshold(0.05<0.75) |
| 54046178 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.752637 USDC | 0.008278 USDC | 0.000000 USDC | 0.005007 USDC | 0.003271 USDC (0.0030 €) | — | 1.84 | 0.047 (n=247) | REJECTED | below_safety_margin(3271<3550), p_lower_below_threshold(0.05<0.75) |
| 54029756 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 15.252967 USDC | 0.006188 USDC | 0.000000 USDC | 0.005016 USDC | 0.001172 USDC (0.0011 €) | — | 0.77 | 0.047 (n=247) | REJECTED | below_safety_margin(1172<3050), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5901 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
