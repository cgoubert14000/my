# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T21:45:14+00:00 ; durée 184.95 min ; blocs 54432179 → 54487627 (14400 vus)

## Connexion
- Requêtes RPC : 145648 ; erreurs : 25 ; latence p50/p95 : 114.2/1,715.0 ms
- Rafraîchissements d'état : 14400 ; âge des données au dernier bloc : 8.68 s ; changements de frais LP observés (pools à frais dynamiques) : 4095
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2880 ; cycles déclenchés par événement : 828 ; avance médiane sur le rafraîchissement multicall : 205 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,227.64 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 277 jetons, 17824 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 96, aerodrome 198, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 169 (rejetés 2) → 574 jetons ; pools candidats 3672 (énumérés 292, par paires 0), mesurés 476, sous le plancher de 10000.0 $ : 3 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2234.638115, 'cbBTC': 75748.316454, 'AERO': 0.612979}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,411,663 | 2,227.638595 | 54487650 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,806,954 | 0.029444 | 54487650 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,311,220 | 0.000013 | 54487650 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,137,348 | 0.029508 | 54487650 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,055,362 | 2,226.602174 | 54487650 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,250,369 | 110.295273 | 54487650 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,384,208 | 0.001541 | 54487650 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,151,097 | 0.029456 | 54487650 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,919,679 | 1.618727 | 54487650 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,153,762 | 2,227.449187 | 54487650 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,982,133 | 0.999135 | 54487650 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,315,023 | 42,260.197322 | 54487650 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,175,821 | 2,227.359487 | 54487650 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,538,378 | 0.029493 | 54487650 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,093,778 | 1,147,424.274597 | 54487650 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,736,332 | 0.000013 | 54487650 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,654,804 | 0.006573 | 54487650 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,650,192 | 0.000013 | 54487650 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,625,948 | 0.000000 | 54487650 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,597,253 | 0.015951 | 54487650 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,514,623 | 442.738005 | 54487650 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,502,847 | 0.000013 | 54487650 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,477,525 | 1.432959 | 54487650 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,111 | 0.819634 | 54487650 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,402,106 | 3,602.991502 | 54487650 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,322,721 | 2,227.322883 | 54487650 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,320,542 | 2,228.979759 | 54487650 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,259,787 | 15,027.492757 | 54487650 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,183,008 | 2,226.544290 | 54487650 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,406 | 76.995559 | 54487650 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,101,379 | 36,242,853.596227 | 54487650 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,028,637 | 109.537725 | 54487650 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,007,972 | 579,120.951747 | 54487650 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 988,051 | 22,701,799.773459 | 54487650 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 979,481 | 20.130031 | 54487650 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 972,565 | 0.000000 | 54487650 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,159 | 2,228.787514 | 54487650 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 933,868 | 1,062.918894 | 54487650 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 924,330 | 0.000013 | 54487650 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 919,096 | 74.179968 | 54487650 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 874,190 | 99,054.926969 | 54487650 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 805,150 | 0.049582 | 54487650 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 795,453 | 3,629.675939 | 54487650 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,797 | 0.055222 | 54487650 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 782,975 | 21.543387 | 54487650 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 755,718 | 0.799699 | 54487650 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 715,114 | 0.560250 | 54487650 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 691,879 | 4,906,256.880580 | 54487650 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 680,186 | 0.000253 | 54487650 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 674,710 | 0.574524 | 54487650 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 663,125 | 0.000008 | 54487650 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 636,108 | 155,070.156814 | 54487650 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 614,613 | 582,554.301005 | 54487650 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 586,490 | 0.040723 | 54487650 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 585,482 | 2.472336 | 54487650 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 523,064 | 1,063.237370 | 54487650 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 521,508 | 895,703.923620 | 54487650 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 513,366 | 2,227.346397 | 54487650 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | ELSA/USDC | 100 | 506,408 | 0.074782 | 54487650 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 503,105 | 7,189.668850 | 54487650 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 15227 ; routes examinées : 271406048 ; candidats optimisés : 522997 ; net attendu > 0 : 472 ; dernier cycle 178.2 ms
- Rejets (moteur) : {'spread_below_threshold': 267072041, 'liquidity_below_min': 3780653, 'negative_expected_net': 522525, 'cycle_budget_exhausted': 15247, 'borrow_bound_too_small': 14894, 'pool_quarantined': 216}
- Enregistrements de la session : 522997 ; net attendu > 0 : 472 ; simulés (eth_call de la vraie tx) : 47 (ok 23, échec 24) ; étiquettes ghost N+1 : 10/37 positives
- Décisions : {'REJECTED': 522997} ; motifs de rejet : {'below_safety_margin': 308, 'negative_expected_net': 522525, 'p_lower_below_threshold': 463, 'price_impact': 1, 'reliability_not_demonstrated': 9, 'simulation_failed': 24, 'stale_data': 42}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54441177 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.912476 WETH | 0.000347 WETH | 0.000000 WETH | 0.000002 WETH | 0.000345 WETH (0.7087 €) | — | 3.78 | 0.079 (n=96) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 2,035.652673 USDC | 0.774170 USDC | 0.000000 USDC | 0.005018 USDC | 0.769152 USDC (0.7076 €) | — | 3.78 | 0.079 (n=96) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.900158 WETH | 0.000342 WETH | 0.000000 WETH | 0.000003 WETH | 0.000340 WETH (0.6982 €) | — | 3.77 | 0.026 (n=348) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,007.352772 USDC | 0.763436 USDC | 0.000000 USDC | 0.005696 USDC | 0.757740 USDC (0.6971 €) | — | 3.77 | 0.026 (n=348) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54441177 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.022473 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5041 €) | — | 3.22 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.771353 WETH | 0.000248 WETH | 0.000000 WETH | 0.000003 WETH | 0.000245 WETH (0.5040 €) | — | 3.18 | 0.154 (n=828) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,770.502825 USDC | 0.553561 USDC | 0.000000 USDC | 0.006716 USDC | 0.546845 USDC (0.5031 €) | — | 3.09 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.022769 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4880 €) | — | 3.07 | 0.277 (n=382) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54441177 | WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.789801 WETH | 0.000240 WETH | 0.000000 WETH | 0.000003 WETH | 0.000237 WETH (0.4878 €) | — | 3.00 | 0.277 (n=382) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,770.767158 USDC | 0.536128 USDC | 0.000000 USDC | 0.006716 USDC | 0.529412 USDC (0.4871 €) | — | 2.99 | 0.240 (n=408) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.606885 WETH | 0.000191 WETH | 0.000000 WETH | 0.000003 WETH | 0.000187 WETH (0.3854 €) | — | 3.09 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.017548 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.3849 €) | — | 3.15 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,360.687868 USDC | 0.425206 USDC | 0.000000 USDC | 0.007055 USDC | 0.418151 USDC (0.3847 €) | — | 3.07 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.607163 WETH | 0.000183 WETH | 0.000000 WETH | 0.000003 WETH | 0.000180 WETH (0.3707 €) | — | 2.97 | 0.182 (n=1058) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54441177 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.017275 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3702 €) | — | 3.07 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,358.336950 USDC | 0.409090 USDC | 0.000000 USDC | 0.007055 USDC | 0.402035 USDC (0.3699 €) | — | 2.96 | 0.182 (n=1058) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.549665 WETH | 0.000180 WETH | 0.000000 WETH | 0.000002 WETH | 0.000178 WETH (0.3651 €) | — | 3.23 | 0.026 (n=348) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,225.808314 USDC | 0.401126 USDC | 0.000000 USDC | 0.005018 USDC | 0.396108 USDC (0.3644 €) | — | 3.23 | 0.026 (n=348) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54441177 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.358952 WETH | 0.000147 WETH | 0.000000 WETH | 0.000003 WETH | 0.000145 WETH (0.2974 €) | — | 4.03 | 0.079 (n=96) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 799.471843 USDC | 0.328288 USDC | 0.000000 USDC | 0.005696 USDC | 0.322592 USDC (0.2968 €) | — | 4.04 | 0.079 (n=96) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54441177 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.012502 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2775 €) | — | 3.18 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.439939 WETH | 0.000138 WETH | 0.000000 WETH | 0.000003 WETH | 0.000135 WETH (0.2774 €) | — | 3.07 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 983.462996 USDC | 0.307673 USDC | 0.000000 USDC | 0.006716 USDC | 0.300957 USDC (0.2769 €) | — | 3.06 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.011149 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2705 €) | — | 3.48 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.367728 WETH | 0.000134 WETH | 0.000000 WETH | 0.000003 WETH | 0.000131 WETH (0.2699 €) | — | 3.57 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |

## Fiabilité et décision
- Observations ghost : 6108 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
