# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T22:32:09+00:00 ; durée 79.42 min ; blocs 55341906 → 55365743 (4182 vus)

## Connexion
- Requêtes RPC : 57149 ; erreurs : 35 ; latence p50/p95 : 342.2/1,149.0 ms
- Rafraîchissements d'état : 4182 ; âge des données au dernier bloc : 4.32 s ; changements de frais LP observés (pools à frais dynamiques) : 2099
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 644 ; cycles déclenchés par événement : 303 ; avance médiane sur le rafraîchissement multicall : 435 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,126.59 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 468 pools, 272 jetons, 17716 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 193, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3654 (énumérés 289, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 3 → gardés 468 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2127.766856, 'cbBTC': 74794.411024, 'AERO': 0.572023}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,049,409 | 2,126.587798 | 55365743 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,649,907 | 0.028354 | 55365743 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,362,503 | 0.000013 | 55365743 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,789,794 | 0.028401 | 55365743 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,475,597 | 2,127.878353 | 55365743 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,398,733 | 96.462138 | 55365743 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,933,224 | 0.028365 | 55365743 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,582,410 | 1.744794 | 55365743 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,024,398 | 2,128.623328 | 55365743 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,900,917 | 1.000033 | 55365743 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,113,751 | 43,652.982349 | 55365743 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,025,168 | 2,128.553129 | 55365743 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,348,341 | 0.028384 | 55365743 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,030,631 | 1,111,732.813378 | 55365743 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,709,028 | 0.000013 | 55365743 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,694,897 | 0.000013 | 55365743 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,578,323 | 0.015717 | 55365743 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,562,405 | 0.006561 | 55365743 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,561,654 | 0.000000 | 55365743 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,495,631 | 0.000013 | 55365743 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,082 | 1.429325 | 55365743 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,463,184 | 426.254946 | 55365743 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,041 | 0.821811 | 55365743 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,321,740 | 3,724.644705 | 55365743 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,292,856 | 2,128.948956 | 55365743 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,249,673 | 15,000.027585 | 55365743 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,079 | 2,131.562689 | 55365743 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,107,496 | 2,128.015580 | 55365743 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,107,263 | 79.257048 | 55365743 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,049,604 | 36,324,898.503719 | 55365743 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 992,390 | 97.144502 | 55365743 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 976,081 | 0.045370 | 55365743 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/BRETT | 10000 | 969,626 | 566,890.828565 | 55365743 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,808 | 21.265326 | 55365743 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 939,347 | 0.001511 | 55365743 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 933,738 | 23,118,623.052805 | 55365743 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 930,466 | 0.000013 | 55365743 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 914,615 | 74.908554 | 55365743 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 908,902 | 1,033.546111 | 55365743 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 895,484 | 0.000000 | 55365743 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 888,506 | 2,127.924155 | 55365743 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 818,375 | 102,944.733273 | 55365743 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 773,599 | 21.927606 | 55365743 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 771,813 | 0.053182 | 55365743 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 746,630 | 3,697.276552 | 55365743 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 721,964 | 0.798531 | 55365743 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 671,987 | 0.550827 | 55365743 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 664,667 | 4,845,817.853124 | 55365743 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,237 | 0.527702 | 55365743 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 623,709 | 0.000008 | 55365743 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 617,051 | 150,285.596066 | 55365743 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 600,752 | 0.000258 | 55365743 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 593,462 | 572,071.300708 | 55365743 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,568 | 0.039269 | 55365743 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 514,319 | 1,033.992038 | 55365743 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 498,740 | 6,667.359914 | 55365743 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| aerodrome | WETH/msETH (stable) | 500 | 497,882 | 2.400596 | 55365743 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | USDC/USDT | 100 | 497,035 | 1.001028 | 55365743 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 470,807 | 0.067809 | 55365743 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/uSOL | 3000 | 469,440 | 24.705397 | 55365743 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 4484 ; routes examinées : 79438544 ; candidats optimisés : 245183 ; net attendu > 0 : 445 ; dernier cycle 340.3 ms
- Rejets (moteur) : {'spread_below_threshold': 77950601, 'liquidity_below_min': 1233334, 'negative_expected_net': 244738, 'borrow_bound_too_small': 8965, 'cycle_budget_exhausted': 461}
- Enregistrements de la session : 245183 ; net attendu > 0 : 445 ; simulés (eth_call de la vraie tx) : 25 (ok 19, échec 6) ; étiquettes ghost N+1 : 8/24 positives
- Décisions : {'REJECTED': 245183} ; motifs de rejet : {'below_safety_margin': 336, 'negative_expected_net': 244738, 'p_lower_below_threshold': 431, 'reliability_not_demonstrated': 14, 'sim_below_estimate': 3, 'simulation_failed': 6, 'stale_data': 30}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.418819 WETH | 0.000076 WETH | 0.000000 WETH | 0.000002 WETH | 0.000074 WETH (0.1445 €) | — | 1.76 | 0.069 (n=319) | REJECTED | below_safety_margin(73797417742801<83763779130135), stale_data(4362ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55346177 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 889.698067 USDC | 0.162109 USDC | 0.000000 USDC | 0.005113 USDC | 0.156996 USDC (0.1444 €) | — | 1.76 | 0.069 (n=319) | REJECTED | below_safety_margin(156996<177939), stale_data(4365ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 171.149913 USDC | 0.154905 USDC | 0.000000 USDC | 0.006410 USDC | 0.148495 USDC (0.1366 €) | — | 8.68 | 0.058 (n=130) | REJECTED | stale_data(4301ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.080469 WETH | 0.000073 WETH | 0.000000 WETH | 0.000003 WETH | 0.000070 WETH (0.1366 €) | — | 8.67 | 0.058 (n=130) | REJECTED | stale_data(4298ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55365017 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.388929 WETH | 0.000065 WETH | 0.000000 WETH | 0.000002 WETH | 0.000063 WETH (0.1226 €) | — | 1.61 | 0.069 (n=319) | REJECTED | below_safety_margin(62680517911025<77785893271738), p_lower_below_threshold(0.07<0.75) |
| 55365017 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 826.225630 USDC | 0.138065 USDC | 0.000000 USDC | 0.004778 USDC | 0.133287 USDC (0.1226 €) | — | 1.61 | 0.069 (n=319) | REJECTED | below_safety_margin(133287<165245), p_lower_below_threshold(0.07<0.75) |
| 55360277 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.069684 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.0987 €) | 0.000050 WETH | 7.24 | 0.177 (n=1027) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55360277 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 147.335806 USDC | 0.113649 USDC | 0.000000 USDC | 0.006397 USDC | 0.107252 USDC (0.0987 €) | — | 7.28 | 0.177 (n=1027) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55360277 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003584 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0987 €) | — | 3.99 | 0.177 (n=1027) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55360277 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH | 0.131076 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.0984 €) | 0.000050 WETH | 3.84 | 0.177 (n=1027) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55360277 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.062711 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0843 €) | 0.000043 WETH | 6.87 | 0.298 (n=458) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55360277 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 133.165503 USDC | 0.097969 USDC | 0.000000 USDC | 0.006397 USDC | 0.091572 USDC (0.0842 €) | — | 6.88 | 0.298 (n=458) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55357897 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.286834 WETH | 0.000043 WETH | 0.000000 WETH | 0.000002 WETH | 0.000041 WETH (0.0804 €) | — | 1.43 | 0.069 (n=319) | REJECTED | below_safety_margin(41111654552322<57366829411307), p_lower_below_threshold(0.07<0.75) |
| 55357897 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 608.448670 USDC | 0.092058 USDC | 0.000000 USDC | 0.004787 USDC | 0.087271 USDC (0.0803 €) | — | 1.43 | 0.069 (n=319) | REJECTED | below_safety_margin(87271<121689), p_lower_below_threshold(0.07<0.75) |
| 55360277 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.061912 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0785 €) | — | 6.48 | 0.298 (n=458) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55360277 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 131.267911 USDC | 0.091666 USDC | 0.000000 USDC | 0.006397 USDC | 0.085269 USDC (0.0784 €) | — | 6.50 | 0.298 (n=458) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55348722 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 654.268100 USDC | 0.087616 USDC | 0.000000 USDC | 0.004787 USDC | 0.082829 USDC (0.0762 €) | — | 1.27 | 0.069 (n=319) | REJECTED | below_safety_margin(82829<130853), p_lower_below_threshold(0.07<0.75) |
| 55348722 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.307237 WETH | 0.000041 WETH | 0.000000 WETH | 0.000002 WETH | 0.000039 WETH (0.0761 €) | — | 1.26 | 0.069 (n=319) | REJECTED | below_safety_margin(38858560354535<61447332248618), p_lower_below_threshold(0.07<0.75) |
| 55360277 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.061224 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0753 €) | — | 6.28 | 0.298 (n=458) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55360277 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 130.063492 USDC | 0.088152 USDC | 0.000000 USDC | 0.006397 USDC | 0.081755 USDC (0.0752 €) | — | 6.29 | 0.298 (n=458) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55346177 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.058706 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0700 €) | — | 6.09 | 0.175 (n=1020) | REJECTED | stale_data(4320ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 124.183498 USDC | 0.082422 USDC | 0.000000 USDC | 0.006410 USDC | 0.076012 USDC (0.0699 €) | — | 6.12 | 0.175 (n=1020) | REJECTED | stale_data(4323ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 55346177 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.055815 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0655 €) | — | 5.99 | 0.299 (n=457) | REJECTED | stale_data(4327ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.30<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 118.767460 USDC | 0.077568 USDC | 0.000000 USDC | 0.006410 USDC | 0.071158 USDC (0.0655 €) | — | 5.99 | 0.299 (n=457) | REJECTED | stale_data(4331ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 55346177 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.057629 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0654 €) | — | 5.80 | 0.299 (n=457) | REJECTED | stale_data(4335ms>4000.0), p_lower_below_threshold(0.30<0.75) |

## Fiabilité et décision
- Observations ghost : 7125 ; taux observé 0.185 ; borne inférieure crédible (0.9) 0.179 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
