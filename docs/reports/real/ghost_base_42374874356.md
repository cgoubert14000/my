# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T16:54:42+00:00 ; durée 229.82 min ; blocs 54331551 → 54400487 (13302 vus)

## Connexion
- Requêtes RPC : 179917 ; erreurs : 3 ; latence p50/p95 : 422.5/1,103.3 ms
- Rafraîchissements d'état : 13302 ; âge des données au dernier bloc : 7.2 s ; changements de frais LP observés (pools à frais dynamiques) : 3959
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8820 ; cycles déclenchés par événement : 3282 ; avance médiane sur le rafraîchissement multicall : 431 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,234.64 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 477 pools, 279 jetons, 17784 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 97, aerodrome 199, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 170 (rejetés 2) → 575 jetons ; pools candidats 3720 (énumérés 294, par paires 0), mesurés 480, sous le plancher de 10000.0 $ : 3 → gardés 477 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2242.465806, 'cbBTC': 75805.716976, 'AERO': 0.595957}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,742,405 | 2,234.639036 | 54400511 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,772,891 | 0.029496 | 54400511 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,350,295 | 0.000013 | 54400511 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,160,239 | 0.029513 | 54400511 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,057,748 | 2,231.473281 | 54400511 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,291,005 | 109.755848 | 54400511 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,407,798 | 0.001549 | 54400511 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,128,442 | 0.029492 | 54400511 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,834,308 | 1.676693 | 54400511 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,166,650 | 2,231.764807 | 54400511 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,986,911 | 0.999644 | 54400511 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,318,371 | 42,440.451164 | 54400511 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,189,224 | 2,231.749571 | 54400511 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,547,155 | 0.029525 | 54400511 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,100,348 | 1,147,435.841537 | 54400511 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,736,644 | 0.000013 | 54400511 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,721,619 | 0.006874 | 54400511 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,644,809 | 0.000013 | 54400511 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,638,924 | 0.000000 | 54400511 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,602,254 | 0.015924 | 54400511 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,522,018 | 440.198313 | 54400511 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,504,122 | 0.000013 | 54400511 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,494,431 | 1.466831 | 54400511 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,111 | 0.819634 | 54400511 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,373,046 | 3,742.067328 | 54400511 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,324,792 | 2,234.209316 | 54400511 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,322,646 | 2,237.802729 | 54400511 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,265,589 | 14,922.953738 | 54400511 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,200,390 | 2,231.480572 | 54400511 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,702 | 76.955062 | 54400511 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,102,551 | 36,064,893.181606 | 54400511 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,028,215 | 109.529456 | 54400511 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,014,487 | 573,481.518104 | 54400511 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 995,258 | 22,537,302.896047 | 54400511 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 987,236 | 19.668172 | 54400511 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 965,691 | 0.000000 | 54400511 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 936,370 | 2,228.787514 | 54400511 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 935,290 | 1,065.206575 | 54400511 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 925,323 | 0.000013 | 54400511 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 915,306 | 74.795464 | 54400511 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 874,560 | 99,594.122357 | 54400511 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 810,472 | 0.049161 | 54400511 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 793,249 | 3,752.660312 | 54400511 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 792,446 | 21.178340 | 54400511 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 788,621 | 0.055639 | 54400511 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,093 | 0.799699 | 54400511 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 719,173 | 0.562932 | 54400511 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,611 | 4,898,258.044705 | 54400511 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 683,318 | 0.000253 | 54400511 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 679,552 | 0.577777 | 54400511 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 656,415 | 146,525.550746 | 54400511 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 649,748 | 0.000008 | 54400511 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 619,666 | 568,240.264551 | 54400511 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 587,057 | 2.473976 | 54400511 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 582,069 | 0.040252 | 54400511 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 523,667 | 1,065.450112 | 54400511 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 516,039 | 910,134.266020 | 54400511 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 515,732 | 2,231.924845 | 54400511 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | ELSA/USDC | 100 | 513,339 | 0.076118 | 54400511 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 504,747 | 7,187.925901 | 54400511 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 16583 ; routes examinées : 294912072 ; candidats optimisés : 357662 ; net attendu > 0 : 220 ; dernier cycle 47.3 ms
- Rejets (moteur) : {'spread_below_threshold': 291611916, 'liquidity_below_min': 2925669, 'negative_expected_net': 357442, 'borrow_bound_too_small': 16583, 'pool_quarantined': 154, 'cycle_budget_exhausted': 88}
- Enregistrements de la session : 357662 ; net attendu > 0 : 220 ; simulés (eth_call de la vraie tx) : 43 (ok 26, échec 17) ; étiquettes ghost N+1 : 2/34 positives
- Décisions : {'REJECTED': 357662} ; motifs de rejet : {'below_safety_margin': 149, 'negative_expected_net': 357442, 'p_lower_below_threshold': 198, 'reliability_not_demonstrated': 22, 'simulation_failed': 17, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54399647 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.057533 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0580 €) | 0.000028 WETH | 4.91 | 0.154 (n=804) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54399647 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001575 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0579 €) | — | 5.27 | 0.154 (n=804) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54348528 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 44.816547 USDC | 0.055181 USDC | 0.000000 USDC | 0.005038 USDC | 0.050143 USDC (0.0461 €) | — | 11.19 | 0.000 (n=100) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54399647 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001250 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0460 €) | — | 5.28 | 0.154 (n=804) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54399647 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.049362 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0455 €) | 0.000022 WETH | 4.48 | 0.154 (n=804) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54381444 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 69.163697 USDC | 0.052915 USDC | 0.000000 USDC | 0.005027 USDC | 0.047888 USDC (0.0441 €) | 0.047888 USDC | 6.92 | 0.026 (n=344) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54390223 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.035909 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0390 €) | 0.000019 WETH | 5.28 | 0.155 (n=800) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54390223 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 80.097722 USDC | 0.049112 USDC | 0.000000 USDC | 0.006721 USDC | 0.042391 USDC (0.0390 €) | — | 5.29 | 0.155 (n=800) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54390223 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.034561 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0368 €) | 0.000018 WETH | 5.17 | 0.155 (n=800) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54390223 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 77.230831 USDC | 0.046685 USDC | 0.000000 USDC | 0.006721 USDC | 0.039964 USDC (0.0368 €) | — | 5.17 | 0.155 (n=800) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54399647 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 105.560331 USDC | 0.046245 USDC | 0.000000 USDC | 0.006716 USDC | 0.039529 USDC (0.0364 €) | — | 3.74 | 0.154 (n=804) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54399647 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001180 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0362 €) | — | 4.41 | 0.154 (n=804) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54355159 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.009080 WETH | 0.000019 WETH | 0.000000 WETH | 0.000002 WETH | 0.000017 WETH (0.0341 €) | 0.000017 WETH | 18.18 | 0.023 (n=35) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 54390223 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.033304 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0333 €) | 0.000016 WETH | 4.85 | 0.155 (n=800) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54390223 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 73.768461 USDC | 0.042834 USDC | 0.000000 USDC | 0.006721 USDC | 0.036113 USDC (0.0332 €) | — | 4.90 | 0.155 (n=800) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54358910 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 56.345718 USDC | 0.036120 USDC | 0.000000 USDC | 0.005035 USDC | 0.031085 USDC (0.0286 €) | — | 5.52 | 0.027 (n=339) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54358911 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 56.345718 USDC | 0.036120 USDC | 0.000000 USDC | 0.005035 USDC | 0.031085 USDC (0.0286 €) | — | 5.52 | 0.027 (n=339) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54361963 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 55.149680 USDC | 0.033617 USDC | 0.000000 USDC | 0.005035 USDC | 0.028582 USDC (0.0263 €) | — | 5.18 | 0.027 (n=341) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54361964 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 55.149680 USDC | 0.033617 USDC | 0.000000 USDC | 0.005035 USDC | 0.028582 USDC (0.0263 €) | — | 5.18 | 0.027 (n=341) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54399647 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001150 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0258 €) | — | 3.22 | 0.277 (n=382) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54399647 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 89.886266 USDC | 0.034433 USDC | 0.000000 USDC | 0.006716 USDC | 0.027717 USDC (0.0255 €) | — | 3.08 | 0.277 (n=382) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54390223 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.022331 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0237 €) | — | 5.15 | 0.155 (n=800) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54390223 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 50.004991 USDC | 0.032418 USDC | 0.000000 USDC | 0.006721 USDC | 0.025697 USDC (0.0236 €) | — | 5.14 | 0.155 (n=800) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54399647 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 91.040506 USDC | 0.031887 USDC | 0.000000 USDC | 0.006716 USDC | 0.025171 USDC (0.0232 €) | — | 2.76 | 0.241 (n=407) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54399647 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000948 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0230 €) | — | 3.48 | 0.277 (n=382) | REJECTED | p_lower_below_threshold(0.28<0.75) |

## Fiabilité et décision
- Observations ghost : 6010 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
