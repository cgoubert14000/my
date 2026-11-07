# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T18:49:21+00:00 ; durée 9.07 min ; blocs 54432179 → 54434892 (771 vus)

## Connexion
- Requêtes RPC : 7473 ; erreurs : 0 ; latence p50/p95 : 92.7/1,619.5 ms
- Rafraîchissements d'état : 771 ; âge des données au dernier bloc : 7.06 s ; changements de frais LP observés (pools à frais dynamiques) : 136
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1036 ; cycles déclenchés par événement : 292 ; avance médiane sur le rafraîchissement multicall : 176 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,234.64 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 277 jetons, 17824 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 96, aerodrome 198, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 169 (rejetés 2) → 574 jetons ; pools candidats 3672 (énumérés 292, par paires 0), mesurés 476, sous le plancher de 10000.0 $ : 3 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2234.638115, 'cbBTC': 75748.316454, 'AERO': 0.612979}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,734,611 | 2,234.637584 | 54434893 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,805,861 | 0.029499 | 54434893 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,339,938 | 0.000013 | 54434893 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,159,870 | 0.029513 | 54434893 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,057,750 | 2,234.473591 | 54434893 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,323,086 | 108.796160 | 54434893 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,407,072 | 0.001549 | 54434893 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,164,572 | 0.029498 | 54434893 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,895,944 | 1.634708 | 54434893 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,219,707 | 2,234.334443 | 54434893 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,986,494 | 0.999657 | 54434893 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,329,971 | 42,145.232745 | 54434893 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,189,312 | 2,234.298402 | 54434893 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,547,056 | 0.029525 | 54434893 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,100,357 | 1,147,424.274597 | 54434893 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,736,525 | 0.000013 | 54434893 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,721,940 | 0.006874 | 54434893 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,644,725 | 0.000013 | 54434893 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,634,131 | 0.000000 | 54434893 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,603,245 | 0.016036 | 54434893 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,524,032 | 438.285685 | 54434893 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,504,114 | 0.000013 | 54434893 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,494,357 | 1.466903 | 54434893 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,111 | 0.819634 | 54434893 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,394,983 | 3,651.303252 | 54434893 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,324,791 | 2,234.420089 | 54434893 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,322,646 | 2,240.800129 | 54434893 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,267,900 | 14,851.223217 | 54434893 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,200,305 | 2,234.481025 | 54434893 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,471 | 76.986684 | 54434893 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,106,148 | 36,110,001.238542 | 54434893 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,042,280 | 109.511501 | 54434893 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,016,449 | 570,246.919979 | 54434893 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 995,404 | 22,537,303.536336 | 54434893 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 983,196 | 19.906183 | 54434893 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 967,642 | 0.000000 | 54434893 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/MORPHO | 3000 | 939,905 | 1,057.945325 | 54434893 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,369 | 2,228.787514 | 54434893 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 925,328 | 0.000013 | 54434893 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 919,157 | 74.170071 | 54434893 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 875,062 | 99,479.785313 | 54434893 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 816,246 | 0.048692 | 54434893 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 794,610 | 3,663.435290 | 54434893 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 793,459 | 21.140028 | 54434893 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,639 | 0.055346 | 54434893 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,092 | 0.799699 | 54434893 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 718,351 | 0.564803 | 54434893 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,760 | 4,896,153.855377 | 54434893 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 683,152 | 0.000253 | 54434893 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 674,688 | 0.574487 | 54434893 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 659,938 | 0.000008 | 54434893 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 649,454 | 149,689.351998 | 54434893 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 621,541 | 569,597.485111 | 54434893 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 587,322 | 2.472336 | 54434893 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 585,535 | 0.040623 | 54434893 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2850 | 526,569 | 1,057.786673 | 54434893 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 520,310 | 901,923.129580 | 54434893 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 515,634 | 2,234.348992 | 54434893 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | ELSA/USDC | 100 | 515,616 | 0.076581 | 54434893 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 504,518 | 7,194.447926 | 54434893 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 1062 ; routes examinées : 18929088 ; candidats optimisés : 4234 ; net attendu > 0 : 19 ; dernier cycle 7.2 ms
- Rejets (moteur) : {'spread_below_threshold': 18667762, 'liquidity_below_min': 255813, 'negative_expected_net': 4215, 'borrow_bound_too_small': 1062, 'pool_quarantined': 216, 'cycle_budget_exhausted': 1}
- Enregistrements de la session : 4234 ; net attendu > 0 : 19 ; simulés (eth_call de la vraie tx) : 7 (ok 0, échec 7) ; étiquettes ghost N+1 : 1/3 positives
- Décisions : {'REJECTED': 4234} ; motifs de rejet : {'below_safety_margin': 12, 'negative_expected_net': 4215, 'p_lower_below_threshold': 19, 'simulation_failed': 7, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54434682 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.012724 WETH | 0.000032 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0612 €) | — | 23.40 | 0.000 (n=33) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54434684 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.012724 WETH | 0.000032 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0612 €) | — | 23.40 | 0.000 (n=33) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54434479 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.284702 WETH | 0.000031 WETH | 0.000000 WETH | 0.000002 WETH | 0.000028 WETH (0.0581 €) | — | 0.99 | 0.050 (n=266) | REJECTED | below_safety_margin(28236311157226<56940397032977), stale_data(4254ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54434479 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 634.607403 USDC | 0.068450 USDC | 0.000000 USDC | 0.005356 USDC | 0.063094 USDC (0.0580 €) | — | 0.99 | 0.050 (n=266) | REJECTED | below_safety_margin(63094<126921), stale_data(4260ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54434479 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 393.937658 USDC | 0.050344 USDC | 0.000000 USDC | 0.005356 USDC | 0.044988 USDC (0.0414 €) | — | 1.14 | 0.051 (n=85) | REJECTED | below_safety_margin(44988<78787), stale_data(4248ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54434479 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.176431 WETH | 0.000023 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0414 €) | — | 1.14 | 0.051 (n=85) | REJECTED | below_safety_margin(20131146646179<35286103490181), stale_data(4241ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54434479 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.004090 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0118 €) | — | 0.42 | 0.182 (n=1058) | REJECTED | below_safety_margin(17<81), stale_data(4297ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54434479 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 339.884453 USDC | 0.018952 USDC | 0.000000 USDC | 0.006715 USDC | 0.012237 USDC (0.0113 €) | — | 0.36 | 0.182 (n=1058) | REJECTED | below_safety_margin(12237<67976), stale_data(4314ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54434479 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.138632 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0112 €) | — | 0.39 | 0.182 (n=1058) | REJECTED | below_safety_margin(5463948704396<27726309434859), stale_data(4305ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54432297 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.004737 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0049 €) | — | 5.00 | 0.259 (n=67) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.26<0.75) |
| 54432297 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.004737 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0049 €) | — | 5.00 | 0.259 (n=67) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.26<0.75) |
| 54432298 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.004737 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0049 €) | — | 5.00 | 0.255 (n=68) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.26<0.75) |
| 54433983 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.004372 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0036 €) | — | 4.04 | 0.255 (n=68) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.26<0.75) |
| 54433984 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.004372 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0036 €) | — | 4.04 | 0.255 (n=68) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.26<0.75) |
| 54433437 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 14.888511 USDC | 0.006289 USDC | 0.000000 USDC | 0.005017 USDC | 0.001272 USDC (0.0012 €) | — | 0.85 | 0.050 (n=266) | REJECTED | below_safety_margin(1272<2977), p_lower_below_threshold(0.05<0.75) |
| 54433438 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 14.888511 USDC | 0.006289 USDC | 0.000000 USDC | 0.005017 USDC | 0.001272 USDC (0.0012 €) | — | 0.85 | 0.050 (n=266) | REJECTED | below_safety_margin(1272<2977), p_lower_below_threshold(0.05<0.75) |
| 54434479 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001694 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.06 | 0.182 (n=1058) | REJECTED | below_safety_margin(1<33), stale_data(4339ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54434479 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 166.165373 USDC | 0.007249 USDC | 0.000000 USDC | 0.006715 USDC | 0.000534 USDC (0.0005 €) | — | 0.03 | 0.182 (n=1058) | REJECTED | below_safety_margin(534<33233), stale_data(4353ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54434479 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.073944 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.02 | 0.182 (n=1058) | REJECTED | below_safety_margin(174419908597<14788875350976), stale_data(4346ms>4000.0), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 6074 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
