# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T03:24:27+00:00 ; durée 33.92 min ; blocs 55443239 → 55453399 (1593 vus)

## Connexion
- Requêtes RPC : 20041 ; erreurs : 60 ; latence p50/p95 : 309.7/1,845.6 ms
- Rafraîchissements d'état : 1593 ; âge des données au dernier bloc : 11.22 s ; changements de frais LP observés (pools à frais dynamiques) : 520
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 283 ; cycles déclenchés par événement : 102 ; avance médiane sur le rafraîchissement multicall : 318 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,121.50 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 465 pools, 270 jetons, 17662 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 99, aerodrome 191, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3655 (énumérés 287, par paires 0), mesurés 467, sous le plancher de 10000.0 $ : 2 → gardés 465 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2121.500856, 'cbBTC': 74826.515907, 'AERO': 0.554783}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,888,733 | 2,121.500788 | 55453429 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,626,868 | 0.028356 | 55453429 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,378,908 | 0.000013 | 55453429 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,771,686 | 0.028376 | 55453429 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,491,039 | 2,117.872312 | 55453429 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,291,842 | 98.836404 | 55453429 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,921,726 | 0.028350 | 55453429 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,478,046 | 1.802508 | 55453429 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,030,817 | 2,117.073733 | 55453429 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,932,711 | 1.000002 | 55453429 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,117,685 | 43,334.824185 | 55453429 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,019,084 | 2,117.085074 | 55453429 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,341,687 | 0.028342 | 55453429 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,023,046 | 1,114,733.552638 | 55453429 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,706,660 | 0.000013 | 55453429 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,683,411 | 0.000013 | 55453429 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,569,186 | 0.015620 | 55453429 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,560,665 | 0.006565 | 55453429 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,557,659 | 0.000000 | 55453429 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,493,207 | 0.000013 | 55453429 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,460,435 | 425.530250 | 55453429 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,267 | 0.821811 | 55453429 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,424,441 | 1.429325 | 55453429 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,293,996 | 3,820.960064 | 55453429 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,291,312 | 2,122.106535 | 55453429 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,247,604 | 15,019.479119 | 55453429 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,219,617 | 2,123.371165 | 55453429 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,979 | 79.297593 | 55453429 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,105,719 | 2,117.826939 | 55453429 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,052,786 | 35,848,271.329511 | 55453429 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 984,413 | 98.537448 | 55453429 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 966,330 | 568,573.773153 | 55453429 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 958,443 | 0.046596 | 55453429 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 955,138 | 21.725895 | 55453429 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 934,992 | 0.001505 | 55453429 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 933,391 | 23,039,733.174810 | 55453429 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 928,609 | 0.000013 | 55453429 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 917,550 | 74.430029 | 55453429 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 903,195 | 1,040.796348 | 55453429 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 896,491 | 0.000000 | 55453429 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 887,781 | 2,127.924155 | 55453429 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 809,102 | 104,796.766775 | 55453429 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 769,462 | 22.093399 | 55453429 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 762,098 | 0.051802 | 55453429 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 733,705 | 3,794.578430 | 55453429 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 720,235 | 0.798536 | 55453429 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 669,565 | 0.542633 | 55453429 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 659,478 | 4,899,074.427570 | 55453429 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,678 | 0.528376 | 55453429 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 614,692 | 150,720.195397 | 55453429 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 607,779 | 0.000007 | 55453429 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 598,420 | 0.000258 | 55453429 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 591,112 | 572,295.136829 | 55453429 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,209 | 0.038497 | 55453429 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 510,871 | 1,040.505501 | 55453429 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/USDT | 100 | 497,025 | 1.001027 | 55453429 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 495,889 | 6,712.037745 | 55453429 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| aerodrome | WETH/msETH (stable) | 500 | 494,852 | 2.405291 | 55453429 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/uSOL | 3000 | 468,097 | 24.728645 | 55453429 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| pancakeswap_v3 | ELSA/USDC | 100 | 462,894 | 0.066332 | 55453429 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 1694 ; routes examinées : 29919428 ; candidats optimisés : 92266 ; net attendu > 0 : 106 ; dernier cycle 221.9 ms
- Rejets (moteur) : {'spread_below_threshold': 29316977, 'liquidity_below_min': 506290, 'negative_expected_net': 92160, 'borrow_bound_too_small': 3388, 'cycle_budget_exhausted': 507}
- Enregistrements de la session : 92266 ; net attendu > 0 : 106 ; simulés (eth_call de la vraie tx) : 7 (ok 5, échec 2) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 92266} ; motifs de rejet : {'below_safety_margin': 88, 'negative_expected_net': 92160, 'p_lower_below_threshold': 106, 'simulation_failed': 2, 'stale_data': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55444678 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 399.069046 USDC | 0.038627 USDC | 0.000000 USDC | 0.004765 USDC | 0.033862 USDC (0.0312 €) | — | 0.85 | 0.069 (n=319) | REJECTED | below_safety_margin(33862<79813), p_lower_below_threshold(0.07<0.75) |
| 55444679 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 399.069046 USDC | 0.038627 USDC | 0.000000 USDC | 0.004765 USDC | 0.033862 USDC (0.0312 €) | — | 0.85 | 0.069 (n=319) | REJECTED | below_safety_margin(33862<79813), p_lower_below_threshold(0.07<0.75) |
| 55444678 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.188631 WETH | 0.000018 WETH | 0.000000 WETH | 0.000002 WETH | 0.000016 WETH (0.0311 €) | — | 0.85 | 0.069 (n=319) | REJECTED | below_safety_margin(15952296321365<37726101222205), p_lower_below_threshold(0.07<0.75) |
| 55444679 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.188631 WETH | 0.000018 WETH | 0.000000 WETH | 0.000002 WETH | 0.000016 WETH (0.0311 €) | — | 0.85 | 0.069 (n=319) | REJECTED | below_safety_margin(15952296321365<37726101222205), p_lower_below_threshold(0.07<0.75) |
| 55445948 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 55.517859 USDC | 0.036125 USDC | 0.000000 USDC | 0.004767 USDC | 0.031358 USDC (0.0288 €) | 0.031358 USDC | 5.65 | 0.049 (n=435) | REJECTED | stale_data(4357ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55444678 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 280.388628 USDC | 0.029064 USDC | 0.000000 USDC | 0.004765 USDC | 0.024299 USDC (0.0224 €) | — | 0.87 | 0.069 (n=319) | REJECTED | below_safety_margin(24299<56077), p_lower_below_threshold(0.07<0.75) |
| 55444679 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 280.388628 USDC | 0.029064 USDC | 0.000000 USDC | 0.004765 USDC | 0.024299 USDC (0.0224 €) | — | 0.87 | 0.069 (n=319) | REJECTED | below_safety_margin(24299<56077), p_lower_below_threshold(0.07<0.75) |
| 55444678 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.132698 WETH | 0.000014 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0223 €) | — | 0.86 | 0.069 (n=319) | REJECTED | below_safety_margin(11447151199638<26539590820553), p_lower_below_threshold(0.07<0.75) |
| 55444679 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.132698 WETH | 0.000014 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0223 €) | — | 0.86 | 0.069 (n=319) | REJECTED | below_safety_margin(11447151199638<26539590820553), p_lower_below_threshold(0.07<0.75) |
| 55445395 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003247 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0207 €) | — | 0.92 | 0.223 (n=1336) | REJECTED | below_safety_margin(30<64), p_lower_below_threshold(0.22<0.75) |
| 55445395 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003247 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0207 €) | — | 0.92 | 0.223 (n=1336) | REJECTED | below_safety_margin(30<64), p_lower_below_threshold(0.22<0.75) |
| 55445395 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.132537 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0203 €) | — | 0.78 | 0.223 (n=1336) | REJECTED | below_safety_margin(10399926788623<26507466908703), p_lower_below_threshold(0.22<0.75) |
| 55445395 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.132537 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0203 €) | — | 0.78 | 0.223 (n=1336) | REJECTED | below_safety_margin(10399926788623<26507466908703), p_lower_below_threshold(0.22<0.75) |
| 55445395 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 298.655026 USDC | 0.028738 USDC | 0.000000 USDC | 0.006700 USDC | 0.022038 USDC (0.0203 €) | — | 0.74 | 0.223 (n=1336) | REJECTED | below_safety_margin(22038<59731), p_lower_below_threshold(0.22<0.75) |
| 55445395 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 298.655026 USDC | 0.028738 USDC | 0.000000 USDC | 0.006700 USDC | 0.022038 USDC (0.0203 €) | — | 0.74 | 0.223 (n=1336) | REJECTED | below_safety_margin(22038<59731), p_lower_below_threshold(0.22<0.75) |
| 55447167 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 47.899372 USDC | 0.026741 USDC | 0.000000 USDC | 0.004768 USDC | 0.021973 USDC (0.0202 €) | 0.021973 USDC | 4.59 | 0.049 (n=436) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55448170 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.125177 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0192 €) | — | 0.78 | 0.069 (n=319) | REJECTED | below_safety_margin(9825110377080<25035491299217), p_lower_below_threshold(0.07<0.75) |
| 55448170 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 264.136813 USDC | 0.025904 USDC | 0.000000 USDC | 0.005091 USDC | 0.020813 USDC (0.0191 €) | — | 0.79 | 0.069 (n=319) | REJECTED | below_safety_margin(20813<52827), p_lower_below_threshold(0.07<0.75) |
| 55445816 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002585 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0124 €) | — | 0.70 | 0.223 (n=1336) | REJECTED | below_safety_margin(18<51), stale_data(4990ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55445817 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002585 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0124 €) | — | 0.70 | 0.223 (n=1336) | REJECTED | below_safety_margin(18<51), p_lower_below_threshold(0.22<0.75) |
| 55447886 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000658 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0124 €) | — | 2.74 | 0.223 (n=1336) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |
| 55445816 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.091252 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0120 €) | — | 0.68 | 0.223 (n=1336) | REJECTED | below_safety_margin(6163095705995<18250460471642), stale_data(4975ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55445817 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.091252 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0120 €) | — | 0.68 | 0.223 (n=1336) | REJECTED | below_safety_margin(6163095705995<18250460471642), p_lower_below_threshold(0.22<0.75) |
| 55445816 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 193.911378 USDC | 0.019434 USDC | 0.000000 USDC | 0.006379 USDC | 0.013055 USDC (0.0120 €) | — | 0.67 | 0.223 (n=1336) | REJECTED | below_safety_margin(13055<38782), stale_data(4983ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55445817 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 193.911378 USDC | 0.019434 USDC | 0.000000 USDC | 0.006379 USDC | 0.013055 USDC (0.0120 €) | — | 0.67 | 0.223 (n=1336) | REJECTED | below_safety_margin(13055<38782), p_lower_below_threshold(0.22<0.75) |

## Fiabilité et décision
- Observations ghost : 7210 ; taux observé 0.186 ; borne inférieure crédible (0.9) 0.181 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
