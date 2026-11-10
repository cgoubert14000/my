# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T00:51:20+00:00 ; durée 218.59 min ; blocs 55341906 → 55407458 (11721 vus)

## Connexion
- Requêtes RPC : 158950 ; erreurs : 80 ; latence p50/p95 : 333.4/1,164.4 ms
- Rafraîchissements d'état : 11721 ; âge des données au dernier bloc : 9.13 s ; changements de frais LP observés (pools à frais dynamiques) : 5275
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 644 ; cycles déclenchés par événement : 303 ; avance médiane sur le rafraîchissement multicall : 435 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,128.95 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 468 pools, 272 jetons, 17716 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 193, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3654 (énumérés 289, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 3 → gardés 468 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2127.766856, 'cbBTC': 74794.411024, 'AERO': 0.572023}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,182,674 | 2,128.844170 | 55407482 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,670,422 | 0.028339 | 55407482 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,367,007 | 0.000013 | 55407482 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,803,803 | 0.028376 | 55407482 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,486,403 | 2,123.432943 | 55407482 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,312,799 | 98.961600 | 55407482 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,939,317 | 0.028331 | 55407482 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,507,443 | 1.785964 | 55407482 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,042,022 | 2,122.663250 | 55407482 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,911,285 | 1.000030 | 55407482 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,119,209 | 43,596.847440 | 55407482 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,028,097 | 2,122.822088 | 55407482 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,350,139 | 0.028341 | 55407482 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,031,539 | 1,113,203.281853 | 55407482 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,711,985 | 0.000013 | 55407482 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,696,537 | 0.000013 | 55407482 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,568,371 | 0.015595 | 55407482 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,563,192 | 0.000000 | 55407482 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,561,481 | 0.006546 | 55407482 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,497,086 | 0.000013 | 55407482 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,082 | 1.429325 | 55407482 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,464,704 | 426.373651 | 55407482 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,263 | 0.821811 | 55407482 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,303,262 | 3,795.250719 | 55407482 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,293,572 | 2,128.870222 | 55407482 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,251,300 | 15,037.511102 | 55407482 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,754 | 2,129.109546 | 55407482 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,108,541 | 2,123.509073 | 55407482 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,107,061 | 79.285849 | 55407482 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,768 | 36,324,898.503719 | 55407482 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 983,700 | 98.277228 | 55407482 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 969,728 | 568,561.082925 | 55407482 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 958,768 | 0.046599 | 55407482 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 958,102 | 21.518881 | 55407482 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 940,365 | 0.001510 | 55407482 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 936,795 | 23,034,487.350762 | 55407482 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 931,859 | 0.000013 | 55407482 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 921,707 | 73.760228 | 55407482 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 906,394 | 1,040.498170 | 55407482 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 898,958 | 0.000000 | 55407482 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 889,258 | 2,127.924155 | 55407482 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 821,334 | 102,431.107075 | 55407482 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| pancakeswap_v3 | QUID/USDC | 100 | 771,682 | 0.053163 | 55407482 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 771,074 | 22.028534 | 55407482 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 738,389 | 3,769.230103 | 55407482 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 722,762 | 0.798535 | 55407482 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,504 | 0.547093 | 55407482 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 661,834 | 4,898,451.797351 | 55407482 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 649,186 | 0.529168 | 55407482 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 617,625 | 150,341.002223 | 55407482 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 613,849 | 0.000007 | 55407482 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 601,144 | 0.000258 | 55407482 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 593,190 | 571,020.709019 | 55407482 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 569,836 | 0.038772 | 55407482 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 512,753 | 1,040.810955 | 55407482 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 498,344 | 6,692.779746 | 55407482 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | USDC/USDT | 100 | 497,025 | 1.001027 | 55407482 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/msETH (stable) | 500 | 496,633 | 2.404977 | 55407482 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/uSOL | 3000 | 469,953 | 24.705397 | 55407482 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| pancakeswap_v3 | ELSA/USDC | 100 | 466,677 | 0.066999 | 55407482 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 12023 ; routes examinées : 212999468 ; candidats optimisés : 757843 ; net attendu > 0 : 956 ; dernier cycle 269.1 ms
- Rejets (moteur) : {'spread_below_threshold': 209032937, 'liquidity_below_min': 3183181, 'negative_expected_net': 756887, 'borrow_bound_too_small': 24032, 'cycle_budget_exhausted': 1475}
- Enregistrements de la session : 757843 ; net attendu > 0 : 956 ; simulés (eth_call de la vraie tx) : 97 (ok 91, échec 6) ; étiquettes ghost N+1 : 28/87 positives
- Décisions : {'REJECTED': 757843} ; motifs de rejet : {'below_safety_margin': 696, 'negative_expected_net': 756887, 'p_lower_below_threshold': 923, 'reliability_not_demonstrated': 33, 'sim_below_estimate': 3, 'simulation_failed': 6, 'stale_data': 40}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.418819 WETH | 0.000076 WETH | 0.000000 WETH | 0.000002 WETH | 0.000074 WETH (0.1445 €) | — | 1.76 | 0.069 (n=319) | REJECTED | below_safety_margin(73797417742801<83763779130135), stale_data(4362ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55346177 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 889.698067 USDC | 0.162109 USDC | 0.000000 USDC | 0.005113 USDC | 0.156996 USDC (0.1444 €) | — | 1.76 | 0.069 (n=319) | REJECTED | below_safety_margin(156996<177939), stale_data(4365ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 171.149913 USDC | 0.154905 USDC | 0.000000 USDC | 0.006410 USDC | 0.148495 USDC (0.1366 €) | — | 8.68 | 0.058 (n=130) | REJECTED | stale_data(4301ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.080469 WETH | 0.000073 WETH | 0.000000 WETH | 0.000003 WETH | 0.000070 WETH (0.1366 €) | — | 8.67 | 0.058 (n=130) | REJECTED | stale_data(4298ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55392067 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 871.963393 USDC | 0.147684 USDC | 0.000000 USDC | 0.004783 USDC | 0.142901 USDC (0.1315 €) | — | 1.64 | 0.069 (n=319) | REJECTED | below_safety_margin(142901<174392), p_lower_below_threshold(0.07<0.75) |
| 55392067 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.408980 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000067 WETH (0.1312 €) | — | 1.64 | 0.069 (n=319) | REJECTED | below_safety_margin(66975775509652<81795971327634), p_lower_below_threshold(0.07<0.75) |
| 55365017 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.388929 WETH | 0.000065 WETH | 0.000000 WETH | 0.000002 WETH | 0.000063 WETH (0.1226 €) | — | 1.61 | 0.069 (n=319) | REJECTED | below_safety_margin(62680517911025<77785893271738), p_lower_below_threshold(0.07<0.75) |
| 55365017 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 826.225630 USDC | 0.138065 USDC | 0.000000 USDC | 0.004778 USDC | 0.133287 USDC (0.1226 €) | — | 1.61 | 0.069 (n=319) | REJECTED | below_safety_margin(133287<165245), p_lower_below_threshold(0.07<0.75) |
| 55391987 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002448 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1210 €) | — | 7.15 | 0.178 (n=1043) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55391987 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.083369 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1210 €) | 0.000062 WETH | 7.41 | 0.178 (n=1043) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55391987 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 162.239951 USDC | 0.133640 USDC | 0.000000 USDC | 0.006397 USDC | 0.127243 USDC (0.1171 €) | — | 7.84 | 0.297 (n=465) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55391987 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002103 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1168 €) | — | 8.04 | 0.057 (n=131) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55391987 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 162.239951 USDC | 0.131030 USDC | 0.000000 USDC | 0.006721 USDC | 0.124309 USDC (0.1144 €) | — | 7.66 | 0.178 (n=1043) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55391987 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001961 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1141 €) | — | 8.42 | 0.126 (n=220) | REJECTED | p_lower_below_threshold(0.13<0.75) |
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
| 55391987 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001973 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0836 €) | — | 6.13 | 0.178 (n=1043) | REJECTED | p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 7188 ; taux observé 0.186 ; borne inférieure crédible (0.9) 0.180 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
