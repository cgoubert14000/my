# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T19:47:00+00:00 ; durée 251.21 min ; blocs 55240823 → 55316177 (7708 vus)

## Connexion
- Requêtes RPC : 136909 ; erreurs : 0 ; latence p50/p95 : 491.4/1,575.7 ms
- Rafraîchissements d'état : 7708 ; âge des données au dernier bloc : 9.78 s ; changements de frais LP observés (pools à frais dynamiques) : 6966
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 24191 ; cycles déclenchés par événement : 7952 ; avance médiane sur le rafraîchissement multicall : 413 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,134.44 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 274 jetons, 17868 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 102, aerodrome 193, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3663 (énumérés 293, par paires 0), mesurés 475, sous le plancher de 10000.0 $ : 2 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2131.426069, 'cbBTC': 75169.710892, 'AERO': 0.579676}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,057,827 | 2,134.436127 | 55316173 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,722,515 | 0.028472 | 55316173 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,305,787 | 0.000013 | 55316173 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,811,719 | 0.028437 | 55316173 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,361,230 | 98.168129 | 55316173 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,351,163 | 2,133.268940 | 55316173 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,935,742 | 0.028470 | 55316173 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,590,712 | 1.739032 | 55316173 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,017,660 | 2,133.172200 | 55316173 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,899,407 | 1.000033 | 55316173 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,122,910 | 43,718.219993 | 55316173 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,036,707 | 2,133.429435 | 55316173 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,371,231 | 0.028435 | 55316173 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,036,425 | 1,113,590.528783 | 55316173 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,726,823 | 0.000013 | 55316173 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,707,294 | 0.000013 | 55316173 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,587,225 | 0.006664 | 55316173 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,583,979 | 0.015798 | 55316173 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,567,152 | 0.000000 | 55316173 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,513,862 | 0.000013 | 55316173 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,481,281 | 1.407587 | 55316173 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,472,826 | 421.994086 | 55316173 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,959 | 0.821800 | 55316173 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,326,113 | 3,712.387288 | 55316173 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,295,230 | 2,134.388333 | 55316173 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,256,728 | 14,819.391692 | 55316173 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,223,330 | 2,137.679498 | 55316173 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,252 | 79.258498 | 55316173 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,105,304 | 2,133.242841 | 55316173 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,048,119 | 36,587,832.049640 | 55316173 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 991,421 | 98.508698 | 55316173 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 980,532 | 0.045975 | 55316173 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/BRETT | 10000 | 973,691 | 566,059.921823 | 55316173 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,984 | 21.253361 | 55316173 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 940,443 | 0.001516 | 55316173 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 938,555 | 23,247,998.494614 | 55316173 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 930,012 | 0.000013 | 55316173 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 919,751 | 74.074214 | 55316173 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 912,848 | 1,032.301131 | 55316173 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 888,795 | 2,127.924155 | 55316173 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 887,283 | 0.000000 | 55316173 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 818,761 | 103,608.176686 | 55316173 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 778,751 | 21.723811 | 55316173 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 771,350 | 0.053116 | 55316173 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 749,246 | 3,692.738593 | 55316173 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 724,683 | 0.798410 | 55316173 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 674,029 | 0.555280 | 55316173 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 666,797 | 4,850,487.115309 | 55316173 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,271 | 0.527774 | 55316173 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 624,882 | 0.000008 | 55316173 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 615,748 | 152,031.638397 | 55316173 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 602,970 | 0.000258 | 55316173 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 596,092 | 563,812.755839 | 55316173 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,125 | 0.039224 | 55316173 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 518,387 | 1,032.519498 | 55316173 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 510,945 | 906,092.862722 | 55316173 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | WETH/msETH (stable) | 500 | 500,850 | 2.392584 | 55316173 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | USDC/USDT | 100 | 493,616 | 1.001011 | 55316173 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 490,468 | 6,945.149928 | 55316173 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 473,757 | 0.068358 | 55316173 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 15659 ; routes examinées : 279795012 ; candidats optimisés : 956003 ; net attendu > 0 : 2819 ; dernier cycle 49.9 ms
- Rejets (moteur) : {'spread_below_threshold': 274306353, 'liquidity_below_min': 4475355, 'negative_expected_net': 953184, 'borrow_bound_too_small': 51052, 'pool_quarantined': 5544, 'cycle_budget_exhausted': 691, 'no_price_reference': 14}
- Enregistrements de la session : 956003 ; net attendu > 0 : 2819 ; simulés (eth_call de la vraie tx) : 201 (ok 81, échec 120) ; étiquettes ghost N+1 : 42/147 positives
- Décisions : {'REJECTED': 956003} ; motifs de rejet : {'below_safety_margin': 2273, 'negative_expected_net': 953184, 'p_lower_below_threshold': 2694, 'reliability_not_demonstrated': 125, 'sim_below_estimate': 9, 'simulated_net_nonpositive': 3, 'simulation_failed': 120, 'stale_data': 1083}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55292046 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.628604 WETH | 0.000161 WETH | 0.000000 WETH | 0.000002 WETH | 0.000159 WETH (0.3108 €) | — | 2.53 | 0.048 (n=91) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,328.473302 USDC | 0.341590 USDC | 0.000000 USDC | 0.004798 USDC | 0.336792 USDC (0.3098 €) | — | 2.54 | 0.048 (n=91) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55299317 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,145.230033 USDC | 0.328294 USDC | 0.000000 USDC | 0.005110 USDC | 0.323184 USDC (0.2973 €) | — | 2.82 | 0.063 (n=311) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55299317 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.540159 WETH | 0.000155 WETH | 0.000000 WETH | 0.000002 WETH | 0.000152 WETH (0.2971 €) | — | 2.82 | 0.063 (n=311) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55292046 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.489407 WETH | 0.000128 WETH | 0.000000 WETH | 0.000002 WETH | 0.000126 WETH (0.2460 €) | — | 2.58 | 0.063 (n=309) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,032.952111 USDC | 0.271387 USDC | 0.000000 USDC | 0.004798 USDC | 0.266589 USDC (0.2453 €) | — | 2.58 | 0.063 (n=309) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55292068 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.486339 WETH | 0.000127 WETH | 0.000000 WETH | 0.000002 WETH | 0.000125 WETH (0.2438 €) | — | 2.57 | 0.063 (n=309) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55292068 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,028.744064 USDC | 0.268963 USDC | 0.000000 USDC | 0.004798 USDC | 0.264165 USDC (0.2430 €) | — | 2.57 | 0.063 (n=309) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55299524 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.101373 WETH | 0.000112 WETH | 0.000000 WETH | 0.000003 WETH | 0.000109 WETH (0.2127 €) | — | 10.75 | 0.129 (n=215) | REJECTED | stale_data(4279ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 55299524 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002849 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2125 €) | — | 10.88 | 0.129 (n=215) | REJECTED | stale_data(4284ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 55292046 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.011792 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2107 €) | — | 2.60 | 0.219 (n=1279) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 55292046 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.435109 WETH | 0.000111 WETH | 0.000000 WETH | 0.000003 WETH | 0.000108 WETH (0.2101 €) | — | 2.47 | 0.219 (n=1279) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 927.984639 USDC | 0.233918 USDC | 0.000000 USDC | 0.006417 USDC | 0.227501 USDC (0.2093 €) | — | 2.45 | 0.219 (n=1279) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 55292046 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.461965 WETH | 0.000106 WETH | 0.000000 WETH | 0.000002 WETH | 0.000104 WETH (0.2032 €) | — | 2.25 | 0.048 (n=91) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 976.657356 USDC | 0.224972 USDC | 0.000000 USDC | 0.004798 USDC | 0.220174 USDC (0.2026 €) | — | 2.25 | 0.048 (n=91) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55299524 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.097442 WETH | 0.000101 WETH | 0.000000 WETH | 0.000003 WETH | 0.000097 WETH (0.1901 €) | — | 10.00 | 0.129 (n=215) | REJECTED | stale_data(4299ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 55299524 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002727 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1899 €) | — | 10.16 | 0.129 (n=215) | REJECTED | stale_data(4304ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 55299524 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002710 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1837 €) | — | 9.89 | 0.058 (n=130) | REJECTED | stale_data(4318ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55299524 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 206.948004 USDC | 0.206046 USDC | 0.000000 USDC | 0.006406 USDC | 0.199640 USDC (0.1837 €) | — | 9.65 | 0.058 (n=130) | REJECTED | stale_data(4322ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55299524 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.087641 WETH | 0.000094 WETH | 0.000000 WETH | 0.000003 WETH | 0.000091 WETH (0.1769 €) | — | 10.34 | 0.129 (n=215) | REJECTED | stale_data(4309ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 55299524 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002513 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1768 €) | — | 10.27 | 0.129 (n=215) | REJECTED | stale_data(4314ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 55299437 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.090677 WETH | 0.000091 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1702 €) | — | 9.62 | 0.130 (n=213) | REJECTED | stale_data(6476ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 55299437 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002450 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1700 €) | — | 10.12 | 0.130 (n=213) | REJECTED | stale_data(6481ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 55299437 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 869.454596 USDC | 0.189033 USDC | 0.000000 USDC | 0.004788 USDC | 0.184245 USDC (0.1695 €) | — | 2.12 | 0.062 (n=312) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55299437 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.410138 WETH | 0.000089 WETH | 0.000000 WETH | 0.000002 WETH | 0.000087 WETH (0.1693 €) | — | 2.12 | 0.062 (n=312) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |

## Fiabilité et décision
- Observations ghost : 7059 ; taux observé 0.185 ; borne inférieure crédible (0.9) 0.179 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
