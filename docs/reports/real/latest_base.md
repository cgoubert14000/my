# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T21:29:33+00:00 ; durée 160.09 min ; blocs 53471207 → 53476010 (4666 vus)

## Connexion
- Requêtes RPC : 55637 ; erreurs : 580 ; latence p50/p95 : 168.6/1,132.6 ms
- Rafraîchissements d'état : 4666 ; âge des données au dernier bloc : 4.49 s ; changements de frais LP observés (pools à frais dynamiques) : 4804
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 43048 ; cycles déclenchés par événement : 4117 ; avance médiane sur le rafraîchissement multicall : 418 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,289.39 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 493 pools, 285 jetons, 19448 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 496, sous le plancher de 10000.0 $ : 3 → gardés 493 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2294.78828, 'cbBTC': 77607.185431, 'AERO': 0.633493}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,558,085 | 2,289.391832 | 53476010 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,400,872 | 0.029473 | 53476010 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,207,028 | 0.029450 | 53476010 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,070,742 | 0.000013 | 53476010 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,046,311 | 2,293.949707 | 53476010 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,810,197 | 100.712665 | 53476010 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,624,727 | 0.001575 | 53476010 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,405,628 | 1.581305 | 53476010 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,838,501 | 0.029470 | 53476010 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,172,608 | 2,293.261327 | 53476010 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,086,452 | 0.999913 | 53476010 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,877,491 | 2,293.421056 | 53476010 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,435,198 | 41,567.364071 | 53476010 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,689,185 | 0.029438 | 53476010 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,174,325 | 1,123,985.241900 | 53476010 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,145,462 | 100.707924 | 53476010 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,815,139 | 0.000013 | 53476010 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,738,451 | 0.017804 | 53476010 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,681,568 | 0.000000 | 53476010 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,627,360 | 0.000013 | 53476010 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,559,537 | 438.452813 | 53476010 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,555,270 | 0.000013 | 53476010 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53476010 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,999 | 2,289.313875 | 53476010 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,495,869 | 0.005878 | 53476010 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,800 | 0.821850 | 53476010 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,426,408 | 3,621.813069 | 53476010 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,341,813 | 2,293.264081 | 53476010 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,338,992 | 2,293.968759 | 53476010 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,297,698 | 14,892.096077 | 53476010 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,195,982 | 0.000013 | 53476010 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,158,637 | 72.384430 | 53476010 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,126,904 | 36,829,006.003004 | 53476010 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,059,482 | 545,637.503178 | 53476010 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,054,034 | 0.000000 | 53476010 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,035,786 | 21,950,664.012046 | 53476010 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,003,049 | 18.786828 | 53476010 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 959,621 | 101.018655 | 53476010 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 949,612 | 1,055.357614 | 53476010 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 949,035 | 88,776.020521 | 53476010 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 940,247 | 70.813424 | 53476010 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 931,832 | 1,259,166.927151 | 53476010 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 928,874 | 2,282.122456 | 53476010 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 893,953 | 0.043906 | 53476010 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 878,065 | 0.000556 | 53476010 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 847,650 | 3,646.232124 | 53476010 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 823,920 | 19.960661 | 53476010 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,727 | 0.056727 | 53476010 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 777,081 | 0.799140 | 53476010 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,574 | 0.594242 | 53476010 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 727,548 | 0.000257 | 53476010 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 718,948 | 4,795,328.862598 | 53476010 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 673,345 | 0.000008 | 53476010 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 670,385 | 147,242.844978 | 53476010 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 665,070 | 0.555673 | 53476010 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 657,763 | 2.368619 | 53476010 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2153 | 650,846 | 549,208.318066 | 53476010 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 614,959 | 0.914716 | 53476010 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 589,761 | 0.087731 | 53476010 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 565,701 | 0.038675 | 53476010 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 8782 ; routes examinées : 170792336 ; candidats optimisés : 493287 ; net attendu > 0 : 536 ; dernier cycle 175.5 ms
- Rejets (moteur) : {'spread_below_threshold': 168273634, 'liquidity_below_min': 1998805, 'negative_expected_net': 492751, 'unquotable': 17554, 'borrow_bound_too_small': 8777, 'cycle_budget_exhausted': 279}
- Enregistrements de la session : 493287 ; net attendu > 0 : 536 ; simulés (eth_call de la vraie tx) : 19 (ok 10, échec 9) ; étiquettes ghost N+1 : 0/15 positives
- Décisions : {'REJECTED': 493287} ; motifs de rejet : {'below_safety_margin': 491, 'negative_expected_net': 492751, 'p_lower_below_threshold': 531, 'reliability_not_demonstrated': 5, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 9, 'stale_data': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53472395 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.026252 WETH | 0.000056 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1137 €) | — | 20.53 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53472362 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.020014 WETH | 0.000033 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0642 €) | — | 15.21 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53475795 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 19.939998 USDC | 0.035428 USDC | 0.000000 USDC | 0.004826 USDC | 0.030602 USDC (0.0282 €) | — | 15.35 | 0.010 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53474176 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000502 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0243 €) | — | 6.77 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000502 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0243 €) | — | 6.77 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 37.177276 USDC | 0.033271 USDC | 0.000000 USDC | 0.006868 USDC | 0.026403 USDC (0.0243 €) | 0.026403 USDC | 7.10 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 37.177276 USDC | 0.033271 USDC | 0.000000 USDC | 0.006868 USDC | 0.026403 USDC (0.0243 €) | 0.026403 USDC | 7.10 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474568 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 61.786427 USDC | 0.031613 USDC | 0.000000 USDC | 0.007215 USDC | 0.024398 USDC (0.0224 €) | — | 3.95 | 0.159 (n=607) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474568 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.027157 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0224 €) | — | 3.92 | 0.159 (n=607) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53475911 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001166 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0207 €) | 0.000000 cbBTC | 2.49 | 0.259 (n=342) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 53475911 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 90.505089 USDC | 0.029717 USDC | 0.000000 USDC | 0.007227 USDC | 0.022490 USDC (0.0207 €) | 0.022490 USDC | 2.48 | 0.259 (n=342) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 53474176 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000396 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0200 €) | — | 7.06 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000396 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0200 €) | — | 7.06 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 34.134904 USDC | 0.028597 USDC | 0.000000 USDC | 0.006868 USDC | 0.021729 USDC (0.0200 €) | 0.021729 USDC | 6.37 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 34.134904 USDC | 0.028597 USDC | 0.000000 USDC | 0.006868 USDC | 0.021729 USDC (0.0200 €) | — | 6.37 | 0.291 (n=315) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 53474568 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 48.971145 USDC | 0.026206 USDC | 0.000000 USDC | 0.007215 USDC | 0.018991 USDC (0.0175 €) | — | 3.88 | 0.159 (n=607) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474568 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.021535 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0174 €) | -0.000002 WETH | 3.85 | 0.159 (n=607) | REJECTED | sim_below_estimate(901946496553<11449691792594), simulated_net_nonpositive, p_lower_below_threshold(0.16<0.75) |
| 53475911 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000911 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0157 €) | — | 2.42 | 0.185 (n=853) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53475911 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 74.605229 USDC | 0.024220 USDC | 0.000000 USDC | 0.007227 USDC | 0.016993 USDC (0.0156 €) | 0.016993 USDC | 2.28 | 0.185 (n=853) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53474568 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 52.765461 USDC | 0.023825 USDC | 0.000000 USDC | 0.007215 USDC | 0.016610 USDC (0.0153 €) | — | 3.15 | 0.159 (n=607) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474568 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.023089 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0152 €) | -0.000002 WETH | 3.14 | 0.159 (n=607) | REJECTED | sim_below_estimate(1442662554566<10409709912743), simulated_net_nonpositive, p_lower_below_threshold(0.16<0.75) |
| 53474568 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 50.883379 USDC | 0.021579 USDC | 0.000000 USDC | 0.007215 USDC | 0.014364 USDC (0.0132 €) | — | 2.82 | 0.185 (n=853) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53474568 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.022415 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0132 €) | — | 2.80 | 0.185 (n=853) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53474568 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 50.685261 USDC | 0.021449 USDC | 0.000000 USDC | 0.007215 USDC | 0.014234 USDC (0.0131 €) | — | 2.81 | 0.185 (n=853) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53474568 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.022205 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0131 €) | — | 2.80 | 0.185 (n=853) | REJECTED | p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 4920 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
