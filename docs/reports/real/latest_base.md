# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T17:03:20+00:00 ; durée 180.62 min ; blocs 55644907 → 55699046 (8787 vus)

## Connexion
- Requêtes RPC : 121091 ; erreurs : 270 ; latence p50/p95 : 280.3/1,251.6 ms
- Rafraîchissements d'état : 8787 ; âge des données au dernier bloc : 9.22 s ; changements de frais LP observés (pools à frais dynamiques) : 11179
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5086 ; cycles déclenchés par événement : 932 ; avance médiane sur le rafraîchissement multicall : 569 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,017.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 270 jetons, 16362 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 99, aerodrome 190, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 164 (rejetés 2) → 569 jetons ; pools candidats 3648 (énumérés 286, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2067.744894, 'cbBTC': 73787.664735, 'AERO': 0.555242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,135,967 | 2,017.574114 | 55699072 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,105,157 | 0.027697 | 55699072 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,918,107 | 0.000014 | 55699072 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,409,587 | 0.027710 | 55699072 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,170,887 | 2,018.971883 | 55699072 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,684,869 | 106.357063 | 55699072 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 4,255,582 | 1.883012 | 55699072 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,239,064 | 0.027688 | 55699072 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,832,808 | 0.999599 | 55699072 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,781,340 | 2,018.381414 | 55699072 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,971,737 | 43,137.340981 | 55699072 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,883,586 | 2,018.830596 | 55699072 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,225,891 | 0.027697 | 55699072 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,921,139 | 1,117,988.291112 | 55699072 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,662,878 | 0.000014 | 55699072 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 1,641,225 | 0.000014 | 55699072 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,612,726 | 0.016249 | 55699072 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,532,901 | 0.006826 | 55699072 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,482,297 | 0.000000 | 55699072 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,743 | 0.822038 | 55699072 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,454,698 | 1.378597 | 55699072 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,408,567 | 0.000014 | 55699072 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,391,612 | 418.784166 | 55699072 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,259,398 | 2,017.494144 | 55699072 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,216,683 | 3,803.937534 | 55699072 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,210,827 | 15,082.055630 | 55699072 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,188,976 | 2,017.729468 | 55699072 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,083,094 | 82.833636 | 55699072 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,038,801 | 2,019.431302 | 55699072 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,008,526 | 34,806,405.299412 | 55699072 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 952,822 | 21.890735 | 55699072 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 926,929 | 554,520.270549 | 55699072 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/cbBTC | 364 | 906,442 | 0.000014 | 55699072 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 900,653 | 0.001473 | 55699072 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/VVV | 10000 | 899,050 | 105.582690 | 55699072 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 898,051 | 22,594,168.260306 | 55699072 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 869,350 | 1,008.147469 | 55699072 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 868,411 | 2,025.243169 | 55699072 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 867,654 | 0.052701 | 55699072 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | DRB/WETH | 10000 | 850,930 | 0.000000 | 55699072 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 785,476 | 76.237122 | 55699072 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 763,482 | 0.052009 | 55699072 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4550 | 759,137 | 22.520193 | 55699072 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 752,179 | 109,688.489841 | 55699072 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 699,856 | 3,775.859859 | 55699072 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 682,996 | 0.803116 | 55699072 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 643,764 | 0.520170 | 55699072 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 638,403 | 0.512456 | 55699072 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 636,698 | 4,754,149.062420 | 55699072 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 577,682 | 0.000007 | 55699072 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 569,742 | 0.000259 | 55699072 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 569,603 | 556,654.884658 | 55699072 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 563,801 | 162,109.256292 | 55699072 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | FLOCK/USDC | 3000 | 555,870 | 0.037321 | 55699072 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 489,018 | 1,010.539104 | 55699072 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 480,856 | 0.069997 | 55699072 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 475,078 | 6,614.031352 | 55699072 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | USDC/MORPHO | 10000 | 460,338 | 0.501375 | 55699072 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,961 | 1.001383 | 55699072 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 439,842 | 299.180925 | 55699072 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 9718 ; routes examinées : 159005916 ; candidats optimisés : 897318 ; net attendu > 0 : 5894 ; dernier cycle 536.3 ms
- Rejets (moteur) : {'spread_below_threshold': 155344878, 'liquidity_below_min': 2696930, 'negative_expected_net': 891424, 'pool_quarantined': 38112, 'borrow_bound_too_small': 17928, 'cycle_budget_exhausted': 10750}
- Enregistrements de la session : 897318 ; net attendu > 0 : 5894 ; simulés (eth_call de la vraie tx) : 328 (ok 239, échec 89) ; étiquettes ghost N+1 : 149/282 positives
- Décisions : {'REJECTED': 897318} ; motifs de rejet : {'below_safety_margin': 4781, 'negative_expected_net': 891424, 'p_lower_below_threshold': 5701, 'price_impact': 7, 'reliability_not_demonstrated': 193, 'sim_below_estimate': 38, 'simulated_net_nonpositive': 26, 'simulation_failed': 89, 'stale_data': 543}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55689884 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.012577 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.8596 €) | — | 10.15 | 0.123 (n=62) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55689884 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 948.622129 USDC | 0.939139 USDC | 0.000000 USDC | 0.005944 USDC | 0.933195 USDC (0.8585 €) | 0.933195 USDC | 9.84 | 0.123 (n=62) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55670011 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.066963 WETH | 0.000440 WETH | 0.000000 WETH | 0.000003 WETH | 0.000438 WETH (0.8349 €) | — | 65.34 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 138.463970 USDC | 0.912685 USDC | 0.000000 USDC | 0.006029 USDC | 0.906656 USDC (0.8341 €) | — | 65.48 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.066851 WETH | 0.000438 WETH | 0.000000 WETH | 0.000003 WETH | 0.000435 WETH (0.8303 €) | — | 65.10 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 138.459955 USDC | 0.907719 USDC | 0.000000 USDC | 0.006029 USDC | 0.901690 USDC (0.8296 €) | — | 65.12 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.066134 WETH | 0.000434 WETH | 0.000000 WETH | 0.000003 WETH | 0.000432 WETH (0.8233 €) | — | 65.25 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 136.946975 USDC | 0.899995 USDC | 0.000000 USDC | 0.006029 USDC | 0.893966 USDC (0.8224 €) | — | 65.28 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.064805 WETH | 0.000411 WETH | 0.000000 WETH | 0.000003 WETH | 0.000408 WETH (0.7789 €) | — | 62.99 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 134.087851 USDC | 0.851510 USDC | 0.000000 USDC | 0.006029 USDC | 0.845481 USDC (0.7778 €) | — | 63.05 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.064117 WETH | 0.000405 WETH | 0.000000 WETH | 0.000003 WETH | 0.000402 WETH (0.7671 €) | — | 62.71 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 132.821327 USDC | 0.838622 USDC | 0.000000 USDC | 0.006029 USDC | 0.832593 USDC (0.7660 €) | — | 62.69 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→AUKI→[pancakeswap_v3]→WETH | 0.071959 WETH | 0.000375 WETH | 0.000000 WETH | 0.000002 WETH | 0.000373 WETH (0.7119 €) | — | 51.85 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[sushiswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.055050 WETH | 0.000345 WETH | 0.000000 WETH | 0.000003 WETH | 0.000342 WETH (0.6532 €) | — | 62.19 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 113.877973 USDC | 0.714076 USDC | 0.000000 USDC | 0.006344 USDC | 0.707732 USDC (0.6511 €) | — | 62.15 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.056208 WETH | 0.000309 WETH | 0.000000 WETH | 0.000003 WETH | 0.000306 WETH (0.5834 €) | — | 54.40 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 116.152836 USDC | 0.638193 USDC | 0.000000 USDC | 0.006029 USDC | 0.632164 USDC (0.5816 €) | — | 54.43 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v2]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.055179 WETH | 0.000307 WETH | 0.000000 WETH | 0.000003 WETH | 0.000305 WETH (0.5811 €) | — | 55.20 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 114.010951 USDC | 0.634991 USDC | 0.000000 USDC | 0.005385 USDC | 0.629606 USDC (0.5792 €) | — | 55.22 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[aerodrome]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.051894 WETH | 0.000272 WETH | 0.000000 WETH | 0.000003 WETH | 0.000269 WETH (0.5136 €) | — | 51.87 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 107.024642 USDC | 0.561837 USDC | 0.000000 USDC | 0.005743 USDC | 0.556094 USDC (0.5116 €) | — | 51.96 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.045931 WETH | 0.000268 WETH | 0.000000 WETH | 0.000004 WETH | 0.000264 WETH (0.5046 €) | — | 57.58 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 94.751963 USDC | 0.553346 USDC | 0.000000 USDC | 0.007603 USDC | 0.545743 USDC (0.5021 €) | — | 57.60 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55689884 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.009507 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4042 €) | — | 6.31 | 0.156 (n=294) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 55689884 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 703.705096 USDC | 0.444803 USDC | 0.000000 USDC | 0.005944 USDC | 0.438859 USDC (0.4038 €) | — | 6.24 | 0.156 (n=294) | REJECTED | p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 7787 ; taux observé 0.205 ; borne inférieure crédible (0.9) 0.199 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 19.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
