# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T04:41:29+00:00 ; durée 287.61 min ; blocs 53177940 → 53186563 (8040 vus)

## Connexion
- Requêtes RPC : 94607 ; erreurs : 300 ; latence p50/p95 : 280.1/3,094.8 ms
- Rafraîchissements d'état : 8040 ; âge des données au dernier bloc : 11.48 s ; changements de frais LP observés (pools à frais dynamiques) : 8856
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 19618 ; cycles déclenchés par événement : 2246 ; avance médiane sur le rafraîchissement multicall : 485 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,356.47 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 303 jetons, 19128 routes
- Par DEX : uniswap_v3 147, aerodrome 211, aerodrome_slipstream 123, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 185 (rejetés 2) → 590 jetons ; pools candidats 3771 (énumérés 333, par paires 0), mesurés 526, sous le plancher de 10000.0 $ : 2 → gardés 524 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2351.399953, 'cbBTC': 80864.599929, 'AERO': 0.698092}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,150,475 | 2,356.467107 | 53186564 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,685,046 | 0.029091 | 53186564 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,648,426 | 0.000012 | 53186564 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,497,230 | 0.029105 | 53186564 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 8,444,550 | 94.543908 | 53186564 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,432,717 | 2,354.899021 | 53186564 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,066,089 | 0.001648 | 53186564 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,886,962 | 1.434070 | 53186564 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,745,564 | 0.029095 | 53186564 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,049,367 | 2,354.774967 | 53186564 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,476,869 | 2,354.686379 | 53186564 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,265,152 | 0.998870 | 53186564 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,775,005 | 36,473.214508 | 53186564 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,966,639 | 0.029118 | 53186564 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,546,148 | 94.564825 | 53186564 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,471,387 | 0.000012 | 53186564 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 2,369,524 | 2,357.711312 | 53186564 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/FAI | 10000 | 2,151,295 | 1,216,444.063428 | 53186564 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,838,103 | 0.018942 | 53186564 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,831,237 | 0.000000 | 53186564 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,800,296 | 394.986719 | 53186564 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,700,518 | 0.000012 | 53186564 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,693,626 | 0.000012 | 53186564 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,688,990 | 0.000012 | 53186564 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,529,419 | 0.005853 | 53186564 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,280 | 1.658893 | 53186564 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,656 | 0.826410 | 53186564 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,459,383 | 3,370.256059 | 53186564 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,401,030 | 13,589.752808 | 53186564 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,261,689 | 0.000269 | 53186564 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,245,506 | 2,354.892045 | 53186564 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,207,150 | 3,357.634058 | 53186564 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,194,235 | 68.133836 | 53186564 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,192,685 | 0.000267 | 53186564 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,168,188 | 1,067,022.071576 | 53186564 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,165,915 | 36,230,754.358062 | 53186564 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,138,147 | 0.000000 | 53186564 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,130,118 | 498,229.837341 | 53186564 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,083,819 | 72,227.811137 | 53186564 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,060,400 | 55.671411 | 53186564 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,055,816 | 21,110,022.865565 | 53186564 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,052,212 | 16.468714 | 53186564 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,012,814 | 0.040217 | 53186564 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 1,007,095 | 93.885311 | 53186564 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 945,635 | 2,342.370626 | 53186564 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 934,436 | 1,059.537241 | 53186564 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 910,780 | 0.000560 | 53186564 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 889,812 | 2.313211 | 53186564 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 883,509 | 17.831034 | 53186564 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 852,733 | 17.421278 | 53186564 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 850,945 | 2,356.535942 | 53186564 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 803,747 | 0.057975 | 53186564 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 797,840 | 0.803180 | 53186564 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 757,899 | 0.000009 | 53186564 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 756,992 | 0.631993 | 53186564 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 755,943 | 4,587,570.874854 | 53186564 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 713,444 | 137,359.632940 | 53186564 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2135 | 702,013 | 498,424.014092 | 53186564 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 686,381 | 0.592914 | 53186564 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 672,570 | 0.108338 | 53186564 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 10285 ; routes examinées : 196731480 ; candidats optimisés : 536136 ; net attendu > 0 : 204 ; dernier cycle 101.1 ms
- Rejets (moteur) : {'spread_below_threshold': 193308755, 'liquidity_below_min': 2673322, 'negative_expected_net': 535932, 'borrow_bound_too_small': 209310, 'cycle_budget_exhausted': 3805, 'unquotable': 152}
- Enregistrements de la session : 536136 ; net attendu > 0 : 204 ; simulés (eth_call de la vraie tx) : 13 (ok 10, échec 3) ; étiquettes ghost N+1 : 4/13 positives
- Décisions : {'REJECTED': 536136} ; motifs de rejet : {'below_safety_margin': 156, 'negative_expected_net': 535932, 'p_lower_below_threshold': 177, 'reliability_not_demonstrated': 27, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53184987 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 111.281894 USDC | 1.260540 USDC | 0.000000 USDC | 0.007088 USDC | 1.253452 USDC (1.1532 €) | — | 112.64 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53184987 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.047128 WETH | 0.000534 WETH | 0.000000 WETH | 0.000003 WETH | 0.000531 WETH (1.1520 €) | — | 112.64 | 0.000 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53184987 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 110.837212 USDC | 1.255915 USDC | 0.000000 USDC | 0.007088 USDC | 1.248827 USDC (1.1489 €) | — | 112.67 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.046944 WETH | 0.000532 WETH | 0.000000 WETH | 0.000003 WETH | 0.000529 WETH (1.1478 €) | — | 112.67 | 0.000 (n=31) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53184987 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 106.180323 USDC | 1.244362 USDC | 0.000000 USDC | 0.007088 USDC | 1.237274 USDC (1.1383 €) | — | 116.53 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53184987 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.044969 WETH | 0.000527 WETH | 0.000000 WETH | 0.000003 WETH | 0.000524 WETH (1.1371 €) | — | 116.52 | 0.000 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53184987 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 106.261839 USDC | 1.218279 USDC | 0.000000 USDC | 0.007088 USDC | 1.211191 USDC (1.1143 €) | — | 113.98 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.045015 WETH | 0.000516 WETH | 0.000000 WETH | 0.000003 WETH | 0.000513 WETH (1.1134 €) | — | 113.98 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 103.116389 USDC | 1.210251 USDC | 0.000000 USDC | 0.007446 USDC | 1.202805 USDC (1.1066 €) | — | 116.65 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.043696 WETH | 0.000513 WETH | 0.000000 WETH | 0.000003 WETH | 0.000510 WETH (1.1061 €) | — | 116.64 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 104.325641 USDC | 1.185733 USDC | 0.000000 USDC | 0.007088 USDC | 1.178645 USDC (1.0844 €) | — | 112.98 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.044205 WETH | 0.000502 WETH | 0.000000 WETH | 0.000003 WETH | 0.000499 WETH (1.0838 €) | — | 112.98 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.040650 WETH | 0.000466 WETH | 0.000000 WETH | 0.000004 WETH | 0.000462 WETH (1.0031 €) | — | 113.71 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 95.722949 USDC | 1.097329 USDC | 0.000000 USDC | 0.008878 USDC | 1.088451 USDC (1.0014 €) | — | 113.71 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | WETH→[aerodrome]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.031471 WETH | 0.000364 WETH | 0.000000 WETH | 0.000003 WETH | 0.000361 WETH (0.7836 €) | — | 114.74 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53184987 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome]→USDC | 74.097302 USDC | 0.856945 USDC | 0.000000 USDC | 0.006762 USDC | 0.850183 USDC (0.7822 €) | — | 114.74 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53184987 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.031844 WETH | 0.000324 WETH | 0.000000 WETH | 0.000003 WETH | 0.000321 WETH (0.6967 €) | — | 100.82 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 74.886759 USDC | 0.762100 USDC | 0.000000 USDC | 0.007088 USDC | 0.755012 USDC (0.6946 €) | — | 100.82 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53184987 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.030934 WETH | 0.000322 WETH | 0.000000 WETH | 0.000003 WETH | 0.000320 WETH (0.6934 €) | — | 103.30 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53184987 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 72.729750 USDC | 0.757642 USDC | 0.000000 USDC | 0.006356 USDC | 0.751286 USDC (0.6912 €) | — | 103.30 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53182278 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.007259 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0699 €) | — | 1.29 | 0.003 (n=2) | REJECTED | below_safety_margin(94<145), reliability_not_demonstrated |
| 53182278 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.250456 WETH | 0.000034 WETH | 0.000000 WETH | 0.000002 WETH | 0.000032 WETH (0.0693 €) | — | 1.28 | 0.003 (n=2) | REJECTED | below_safety_margin(31960218814645<50091270569155), reliability_not_demonstrated |
| 53182278 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,017.145501 USDC | 0.059728 USDC | 0.000000 USDC | 0.005654 USDC | 0.054074 USDC (0.0497 €) | — | 0.53 | 0.020 (n=106) | REJECTED | below_safety_margin(54074<203429), p_lower_below_threshold(0.02<0.75) |
| 53182278 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.430558 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0497 €) | — | 0.53 | 0.020 (n=106) | REJECTED | below_safety_margin(22887495811158<86111678777983), p_lower_below_threshold(0.02<0.75) |
| 53182278 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 379.948769 USDC | 0.054366 USDC | 0.000000 USDC | 0.005296 USDC | 0.049070 USDC (0.0451 €) | — | 1.29 | 0.013 (n=22) | REJECTED | below_safety_margin(49070<75989), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2891 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
