# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T23:55:21+00:00 ; durée 162.61 min ; blocs 55341906 → 55390677 (8794 vus)

## Connexion
- Requêtes RPC : 119019 ; erreurs : 60 ; latence p50/p95 : 309.5/1,167.6 ms
- Rafraîchissements d'état : 8794 ; âge des données au dernier bloc : 7.29 s ; changements de frais LP observés (pools à frais dynamiques) : 4212
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 644 ; cycles déclenchés par événement : 303 ; avance médiane sur le rafraîchissement multicall : 435 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,128.94 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 468 pools, 272 jetons, 17716 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 193, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3654 (énumérés 289, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 3 → gardés 468 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2127.766856, 'cbBTC': 74794.411024, 'AERO': 0.572023}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,179,378 | 2,128.937498 | 55390703 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,673,884 | 0.028330 | 55390703 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,366,989 | 0.000013 | 55390703 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,804,851 | 0.028401 | 55390703 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,486,219 | 2,132.261339 | 55390703 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,337,328 | 98.300329 | 55390703 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,939,482 | 0.028330 | 55390703 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,530,605 | 1.767751 | 55390703 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,091,532 | 2,131.552259 | 55390703 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,908,525 | 1.000033 | 55390703 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,118,411 | 43,618.859692 | 55390703 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,028,059 | 2,131.324891 | 55390703 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,350,249 | 0.028384 | 55390703 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,031,532 | 1,113,203.281853 | 55390703 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,711,947 | 0.000013 | 55390703 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,697,295 | 0.000013 | 55390703 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,576,664 | 0.015693 | 55390703 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,563,187 | 0.000000 | 55390703 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,548,218 | 0.006480 | 55390703 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,497,416 | 0.000013 | 55390703 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,082 | 1.429325 | 55390703 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,462,344 | 428.725930 | 55390703 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,041 | 0.821811 | 55390703 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,311,704 | 3,769.246836 | 55390703 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,293,570 | 2,129.004557 | 55390703 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,248,501 | 15,084.808562 | 55390703 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,754 | 2,136.922661 | 55390703 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,108,362 | 2,132.338458 | 55390703 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,107,061 | 79.285849 | 55390703 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,764 | 36,324,898.503719 | 55390703 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 986,390 | 97.785970 | 55390703 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 970,024 | 568,045.343127 | 55390703 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 963,220 | 0.046140 | 55390703 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 958,442 | 21.495398 | 55390703 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 943,972 | 23,034,487.350762 | 55390703 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 939,728 | 0.001507 | 55390703 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 932,091 | 0.000013 | 55390703 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 921,865 | 73.734997 | 55390703 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 907,090 | 1,039.322540 | 55390703 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 898,561 | 0.000000 | 55390703 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 889,008 | 2,127.924155 | 55390703 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 819,669 | 102,846.791149 | 55390703 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 771,075 | 22.028456 | 55390703 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 770,437 | 0.052985 | 55390703 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 742,177 | 3,743.541317 | 55390703 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 722,760 | 0.798535 | 55390703 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,601 | 0.548996 | 55390703 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 661,530 | 4,902,896.311899 | 55390703 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,836 | 0.528627 | 55390703 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 618,205 | 150,056.957508 | 55390703 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 618,100 | 0.000008 | 55390703 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 601,142 | 0.000258 | 55390703 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 593,471 | 571,739.005569 | 55390703 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 571,953 | 0.038994 | 55390703 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 513,120 | 1,039.607260 | 55390703 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 497,380 | 6,718.691489 | 55390703 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | USDC/USDT | 100 | 497,025 | 1.001027 | 55390703 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/msETH (stable) | 500 | 497,014 | 2.409292 | 55390703 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/uSOL | 3000 | 469,959 | 24.705397 | 55390703 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| pancakeswap_v3 | ELSA/USDC | 100 | 466,710 | 0.067053 | 55390703 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 9096 ; routes examinées : 161144736 ; candidats optimisés : 552203 ; net attendu > 0 : 699 ; dernier cycle 301.5 ms
- Rejets (moteur) : {'spread_below_threshold': 158349764, 'liquidity_below_min': 2223594, 'negative_expected_net': 551504, 'borrow_bound_too_small': 18184, 'cycle_budget_exhausted': 991}
- Enregistrements de la session : 552203 ; net attendu > 0 : 699 ; simulés (eth_call de la vraie tx) : 74 (ok 68, échec 6) ; étiquettes ghost N+1 : 27/64 positives
- Décisions : {'REJECTED': 552203} ; motifs de rejet : {'below_safety_margin': 495, 'negative_expected_net': 551504, 'p_lower_below_threshold': 678, 'reliability_not_demonstrated': 21, 'sim_below_estimate': 3, 'simulation_failed': 6, 'stale_data': 32}

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
| 55372397 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001813 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0877 €) | — | 7.01 | 0.296 (n=461) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55372397 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 129.290561 USDC | 0.100812 USDC | 0.000000 USDC | 0.006398 USDC | 0.094414 USDC (0.0869 €) | — | 7.30 | 0.296 (n=461) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55372397 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 141.590397 USDC | 0.099770 USDC | 0.000000 USDC | 0.006398 USDC | 0.093372 USDC (0.0859 €) | — | 6.59 | 0.177 (n=1031) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55372397 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001823 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0856 €) | — | 6.80 | 0.177 (n=1031) | REJECTED | p_lower_below_threshold(0.18<0.75) |
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
| 55378927 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001671 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0711 €) | — | 6.16 | 0.296 (n=461) | REJECTED | p_lower_below_threshold(0.30<0.75) |

## Fiabilité et décision
- Observations ghost : 7165 ; taux observé 0.187 ; borne inférieure crédible (0.9) 0.181 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
