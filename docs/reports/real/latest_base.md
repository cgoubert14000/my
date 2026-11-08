# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T03:25:43+00:00 ; durée 188.38 min ; blocs 54533288 → 54589778 (8983 vus)

## Connexion
- Requêtes RPC : 123379 ; erreurs : 13 ; latence p50/p95 : 437.4/1,429.1 ms
- Rafraîchissements d'état : 8983 ; âge des données au dernier bloc : 8.56 s ; changements de frais LP observés (pools à frais dynamiques) : 3003
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2408 ; cycles déclenchés par événement : 1110 ; avance médiane sur le rafraîchissement multicall : 427 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,231.65 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 470 pools, 276 jetons, 17708 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 96, aerodrome 197, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3668 (énumérés 291, par paires 0), mesurés 473, sous le plancher de 10000.0 $ : 3 → gardés 470 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2231.621019, 'cbBTC': 75753.631297, 'AERO': 0.627658}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,530,600 | 2,231.649182 | 54589805 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,839,222 | 0.029496 | 54589805 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,270,266 | 0.000013 | 54589805 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,149,859 | 0.029508 | 54589805 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,066,740 | 2,235.055609 | 54589805 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,291,262 | 109.454641 | 54589805 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,384,408 | 0.001541 | 54589805 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,156,377 | 0.029484 | 54589805 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,898,985 | 1.631927 | 54589805 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,158,416 | 2,234.441451 | 54589805 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,982,341 | 0.999166 | 54589805 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,319,973 | 42,286.119668 | 54589805 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,179,079 | 2,234.112051 | 54589805 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,543,215 | 0.029493 | 54589805 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,096,791 | 1,148,252.607284 | 54589805 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,736,155 | 0.000013 | 54589805 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,651,962 | 0.000013 | 54589805 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,617,105 | 0.000000 | 54589805 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,612,929 | 0.006356 | 54589805 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,581,340 | 0.015686 | 54589805 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,515,267 | 444.753864 | 54589805 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,502,716 | 0.000013 | 54589805 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,469,421 | 1.434825 | 54589805 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,111 | 0.819634 | 54589805 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,397,765 | 3,641.945279 | 54589805 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,922 | 2,233.806177 | 54589805 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,294,986 | 2,238.104897 | 54589805 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,258,369 | 15,054.240677 | 54589805 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,184,635 | 2,235.350410 | 54589805 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,406 | 76.995559 | 54589805 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,100,189 | 36,563,454.380097 | 54589805 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,036,227 | 109.174227 | 54589805 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,007,125 | 583,676.516690 | 54589805 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 985,656 | 22,865,729.300087 | 54589805 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 974,024 | 20.467692 | 54589805 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 959,307 | 0.000000 | 54589805 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,580 | 2,228.787514 | 54589805 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 932,817 | 1,067.468578 | 54589805 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 924,722 | 73.280105 | 54589805 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 924,318 | 0.000013 | 54589805 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 864,945 | 101,548.417217 | 54589805 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 811,330 | 0.048962 | 54589805 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 792,943 | 3,616.178478 | 54589805 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,481 | 0.055322 | 54589805 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 779,676 | 21.671995 | 54589805 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 757,028 | 0.799805 | 54589805 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 713,276 | 0.561460 | 54589805 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 689,804 | 4,953,876.676071 | 54589805 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 681,408 | 0.000253 | 54589805 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 672,375 | 0.570721 | 54589805 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 660,413 | 0.000008 | 54589805 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 637,388 | 155,008.638292 | 54589805 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 613,205 | 587,739.009351 | 54589805 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 586,573 | 2.472111 | 54589805 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 581,545 | 0.040040 | 54589805 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 521,720 | 1,067.789574 | 54589805 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 519,628 | 0.077407 | 54589805 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 518,742 | 903,129.466679 | 54589805 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 514,109 | 2,234.320705 | 54589805 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 511,268 | 6,987.007380 | 54589805 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 10092 ; routes examinées : 178709136 ; candidats optimisés : 461427 ; net attendu > 0 : 66 ; dernier cycle 336.1 ms
- Rejets (moteur) : {'spread_below_threshold': 175669080, 'liquidity_below_min': 2570168, 'negative_expected_net': 461361, 'borrow_bound_too_small': 8401, 'cycle_budget_exhausted': 60}
- Enregistrements de la session : 461427 ; net attendu > 0 : 66 ; simulés (eth_call de la vraie tx) : 10 (ok 10, échec 0) ; étiquettes ghost N+1 : 2/10 positives
- Décisions : {'REJECTED': 461427} ; motifs de rejet : {'below_safety_margin': 45, 'negative_expected_net': 461361, 'p_lower_below_threshold': 66, 'stale_data': 21}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54565087 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.014916 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0347 €) | 0.000017 WETH | 11.35 | 0.128 (n=47) | REJECTED | stale_data(4168ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 54565087 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 33.235198 USDC | 0.044155 USDC | 0.000000 USDC | 0.006396 USDC | 0.037759 USDC (0.0347 €) | — | 11.36 | 0.128 (n=47) | REJECTED | stale_data(4171ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 54565087 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.014700 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0334 €) | 0.000016 WETH | 11.08 | 0.065 (n=180) | REJECTED | stale_data(4173ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54565087 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 32.629907 USDC | 0.042728 USDC | 0.000000 USDC | 0.006396 USDC | 0.036332 USDC (0.0334 €) | — | 11.13 | 0.065 (n=180) | REJECTED | stale_data(4176ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54565087 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.014543 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0327 €) | 0.000016 WETH | 10.95 | 0.065 (n=180) | REJECTED | stale_data(4178ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54565087 | USDC→[uniswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 32.289475 USDC | 0.041914 USDC | 0.000000 USDC | 0.006396 USDC | 0.035518 USDC (0.0327 €) | — | 11.00 | 0.065 (n=180) | REJECTED | stale_data(4181ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54588088 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 85.628475 USDC | 0.027085 USDC | 0.000000 USDC | 0.007044 USDC | 0.020041 USDC (0.0184 €) | 0.020041 USDC | 2.34 | 0.245 (n=412) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54588088 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000976 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0181 €) | 0.000000 cbBTC | 2.66 | 0.245 (n=412) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54565087 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 23.269684 USDC | 0.021621 USDC | 0.000000 USDC | 0.006396 USDC | 0.015225 USDC (0.0140 €) | — | 6.54 | 0.268 (n=177) | REJECTED | stale_data(4190ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 54565087 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.010444 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0140 €) | — | 6.53 | 0.268 (n=177) | REJECTED | stale_data(4193ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 54565087 | USDC→[uniswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 23.111222 USDC | 0.021433 USDC | 0.000000 USDC | 0.006396 USDC | 0.015037 USDC (0.0138 €) | — | 6.51 | 0.137 (n=268) | REJECTED | stale_data(4195ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 54565087 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.010382 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0138 €) | — | 6.49 | 0.137 (n=268) | REJECTED | stale_data(4198ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 54565087 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 21.119206 USDC | 0.021428 USDC | 0.000000 USDC | 0.006735 USDC | 0.014693 USDC (0.0135 €) | — | 6.96 | 0.137 (n=268) | REJECTED | stale_data(4187ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 54565087 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.009484 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0135 €) | — | 6.94 | 0.137 (n=268) | REJECTED | stale_data(4184ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 54576574 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 20.067459 USDC | 0.017036 USDC | 0.000000 USDC | 0.005010 USDC | 0.012026 USDC (0.0111 €) | 0.012026 USDC | 5.99 | 0.077 (n=98) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54588088 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 58.885536 USDC | 0.018768 USDC | 0.000000 USDC | 0.007044 USDC | 0.011724 USDC (0.0108 €) | — | 1.99 | 0.183 (n=1067) | REJECTED | below_safety_margin(11724<11777), p_lower_below_threshold(0.18<0.75) |
| 54588088 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 58.885536 USDC | 0.018632 USDC | 0.000000 USDC | 0.007044 USDC | 0.011588 USDC (0.0107 €) | — | 1.97 | 0.245 (n=412) | REJECTED | below_safety_margin(11588<11777), p_lower_below_threshold(0.24<0.75) |
| 54565087 | USDC→[sushiswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 20.123817 USDC | 0.017977 USDC | 0.000000 USDC | 0.006396 USDC | 0.011581 USDC (0.0107 €) | — | 5.75 | 0.137 (n=268) | REJECTED | stale_data(4204ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 54565087 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.009061 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0106 €) | — | 5.72 | 0.137 (n=268) | REJECTED | stale_data(4201ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 54588088 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000915 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0104 €) | — | 1.64 | 0.183 (n=1067) | REJECTED | below_safety_margin(15<18), p_lower_below_threshold(0.18<0.75) |
| 54588088 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000915 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0104 €) | — | 1.64 | 0.245 (n=412) | REJECTED | below_safety_margin(15<18), p_lower_below_threshold(0.24<0.75) |
| 54551500 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000853 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0090 €) | — | 1.52 | 0.183 (n=1067) | REJECTED | below_safety_margin(13<17), p_lower_below_threshold(0.18<0.75) |
| 54551501 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000853 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0090 €) | — | 1.52 | 0.183 (n=1067) | REJECTED | below_safety_margin(13<17), p_lower_below_threshold(0.18<0.75) |
| 54551501 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.036255 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | — | 1.15 | 0.183 (n=1067) | REJECTED | below_safety_margin(4185190097130<7251029877697), p_lower_below_threshold(0.18<0.75) |
| 54551500 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.036255 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | — | 1.15 | 0.183 (n=1067) | REJECTED | below_safety_margin(4184205607098<7251029877697), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 6127 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
