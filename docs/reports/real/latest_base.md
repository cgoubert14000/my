# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T17:11:46+00:00 ; durée 36.63 min ; blocs 56554640 → 56565601 (2142 vus)

## Connexion
- Requêtes RPC : 24910 ; erreurs : 32 ; latence p50/p95 : 143.7/1,487.4 ms
- Rafraîchissements d'état : 2142 ; âge des données au dernier bloc : 10.05 s ; changements de frais LP observés (pools à frais dynamiques) : 1426
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1271 ; cycles déclenchés par événement : 354 ; avance médiane sur le rafraîchissement multicall : 593 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,003.07 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 454 pools, 266 jetons, 14202 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 96, aerodrome 187, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 160 (rejetés 2) → 565 jetons ; pools candidats 3627 (énumérés 281, par paires 0), mesurés 456, sous le plancher de 10000.0 $ : 2 → gardés 454 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2012.424484, 'cbBTC': 71768.389273, 'AERO': 0.523178}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,158,939 | 2,003.072343 | 56565634 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,249,753 | 0.027987 | 56565634 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,608,481 | 0.000014 | 56565634 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,495,018 | 0.028017 | 56565634 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 6,954,380 | 2,005.889045 | 56565634 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,648,937 | 105.774486 | 56565634 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,180,184 | 0.027981 | 56565634 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,157,570 | 1.913367 | 56565634 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,064,411 | 2,005.104337 | 56565634 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,771,212 | 0.998585 | 56565634 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,973,372 | 42,472.303947 | 56565634 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 138 | 2,800,152 | 2,005.261729 | 56565634 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,145,998 | 0.028010 | 56565634 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,871,039 | 1,161,779.506815 | 56565634 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,648,148 | 0.016796 | 56565634 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,604,322 | 0.000014 | 56565634 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,571,235 | 0.000014 | 56565634 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,517,113 | 0.000000 | 56565634 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,489,184 | 0.006633 | 56565634 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,471,413 | 0.000014 | 56565634 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,486 | 0.831291 | 56565634 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,371,606 | 429.694797 | 56565634 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,255,098 | 2,003.936701 | 56565634 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,221,957 | 3,840.691485 | 56565634 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,182,230 | 15,325.218071 | 56565634 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,140,803 | 2,007.166460 | 56565634 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,088,673 | 2,005.728205 | 56565634 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,177 | 86.290648 | 56565634 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,047,058 | 1.389298 | 56565634 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,009,632 | 34,378,325.114166 | 56565634 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 973,257 | 105.929015 | 56565634 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 973,043 | 20.532063 | 56565634 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 916,722 | 560,046.417721 | 56565634 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 888,465 | 0.001484 | 56565634 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 877,148 | 23,229,511.263151 | 56565634 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 872,347 | 0.052753 | 56565634 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 868,569 | 0.000014 | 56565634 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 867,386 | 2,005.358242 | 56565634 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 864,203 | 1,007.703953 | 56565634 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 823,051 | 0.000000 | 56565634 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 767,473 | 79.855691 | 56565634 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 743,882 | 0.049291 | 56565634 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 737,020 | 23.475862 | 56565634 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 685,010 | 3,867.479175 | 56565634 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 678,643 | 0.801801 | 56565634 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 648,903 | 0.512889 | 56565634 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/EDEL | 7000 | 647,551 | 145,793.847197 | 56565634 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 628,472 | 4,816,905.786342 | 56565634 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 595,464 | 0.447136 | 56565634 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 580,602 | 150,896.250762 | 56565634 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2144 | 562,803 | 560,893.994614 | 56565634 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | VIRTUAL/WETH | 10000 | 559,693 | 0.000255 | 56565634 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 556,300 | 0.000007 | 56565634 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 553,531 | 0.037265 | 56565634 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 482,268 | 1,007.489906 | 56565634 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 455,527 | 0.065236 | 56565634 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 450,249 | 1.000985 | 56565634 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 445,501 | 0.502823 | 56565634 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 427,755 | 24.791120 | 56565634 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 422,396 | 928,011.021398 | 56565634 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 2495 ; routes examinées : 35433990 ; candidats optimisés : 150021 ; net attendu > 0 : 113 ; dernier cycle 362.6 ms
- Rejets (moteur) : {'spread_below_threshold': 34730979, 'liquidity_below_min': 552206, 'negative_expected_net': 149908, 'cycle_budget_exhausted': 784}
- Enregistrements de la session : 150021 ; net attendu > 0 : 113 ; simulés (eth_call de la vraie tx) : 7 (ok 6, échec 1) ; étiquettes ghost N+1 : 1/6 positives
- Décisions : {'REJECTED': 150021} ; motifs de rejet : {'below_safety_margin': 95, 'negative_expected_net': 149908, 'p_lower_below_threshold': 94, 'reliability_not_demonstrated': 19, 'simulation_failed': 1, 'stale_data': 20}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56564036 | WETH→[aerodrome]→NPC→[uniswap_v2]→WETH | 0.011966 WETH | 0.000080 WETH | 0.000000 WETH | 0.000002 WETH | 0.000079 WETH (0.1449 €) | 0.000079 WETH | 65.72 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 56559823 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 12.458759 USDC | 0.017572 USDC | 0.000000 USDC | 0.006123 USDC | 0.011449 USDC (0.0105 €) | — | 9.19 | 0.144 (n=242) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 56559823 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 12.459670 USDC | 0.017547 USDC | 0.000000 USDC | 0.006123 USDC | 0.011424 USDC (0.0105 €) | — | 9.17 | 0.092 (n=155) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56559823 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.006243 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0105 €) | 0.000006 WETH | 9.13 | 0.144 (n=242) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 56559823 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.006235 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0105 €) | 0.000006 WETH | 9.12 | 0.092 (n=155) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56561451 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 217.507912 USDC | 0.015583 USDC | 0.000000 USDC | 0.004565 USDC | 0.011018 USDC (0.0101 €) | — | 0.51 | 0.104 (n=370) | REJECTED | below_safety_margin(11018<43501), p_lower_below_threshold(0.10<0.75) |
| 56561474 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 217.507912 USDC | 0.015583 USDC | 0.000000 USDC | 0.004569 USDC | 0.011014 USDC (0.0101 €) | — | 0.51 | 0.104 (n=370) | REJECTED | below_safety_margin(11014<43501), stale_data(4107ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56561451 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.108186 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0101 €) | — | 0.51 | 0.104 (n=370) | REJECTED | below_safety_margin(5486822804668<21637100879107), p_lower_below_threshold(0.10<0.75) |
| 56561474 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.108186 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0101 €) | — | 0.51 | 0.104 (n=370) | REJECTED | below_safety_margin(5485032354154<21637100879107), stale_data(4099ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56559823 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 11.743599 USDC | 0.016508 USDC | 0.000000 USDC | 0.006123 USDC | 0.010385 USDC (0.0096 €) | — | 8.84 | 0.092 (n=155) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56559823 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 12.087530 USDC | 0.016479 USDC | 0.000000 USDC | 0.006123 USDC | 0.010356 USDC (0.0095 €) | — | 8.57 | 0.092 (n=155) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56559823 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.005838 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0095 €) | 0.000005 WETH | 8.85 | 0.092 (n=155) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56559823 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.006082 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0095 €) | — | 8.47 | 0.092 (n=155) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56559823 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 12.061064 USDC | 0.016402 USDC | 0.000000 USDC | 0.006123 USDC | 0.010279 USDC (0.0095 €) | — | 8.52 | 0.092 (n=155) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56559823 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.006068 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0094 €) | — | 8.43 | 0.092 (n=155) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56556875 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.055027 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0092 €) | — | 0.91 | 0.268 (n=1617) | REJECTED | below_safety_margin(4989908289805<11005499079417), p_lower_below_threshold(0.27<0.75) |
| 56556875 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.055027 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0092 €) | — | 0.91 | 0.268 (n=1617) | REJECTED | below_safety_margin(4989908289805<11005499079417), stale_data(4616ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56556875 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 109.404960 USDC | 0.016420 USDC | 0.000000 USDC | 0.006455 USDC | 0.009965 USDC (0.0092 €) | — | 0.91 | 0.268 (n=1617) | REJECTED | below_safety_margin(9965<21880), p_lower_below_threshold(0.27<0.75) |
| 56556875 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 109.404960 USDC | 0.016420 USDC | 0.000000 USDC | 0.006455 USDC | 0.009965 USDC (0.0092 €) | — | 0.91 | 0.268 (n=1617) | REJECTED | below_safety_margin(9965<21880), stale_data(4623ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56559823 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 11.885167 USDC | 0.015958 USDC | 0.000000 USDC | 0.006123 USDC | 0.009835 USDC (0.0090 €) | — | 8.28 | 0.144 (n=242) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 56559823 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.005962 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0090 €) | — | 8.21 | 0.144 (n=242) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 56559823 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.582685 USDC | 0.014506 USDC | 0.000000 USDC | 0.006123 USDC | 0.008383 USDC (0.0077 €) | — | 8.75 | 0.092 (n=155) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56559823 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004806 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0077 €) | — | 8.67 | 0.092 (n=155) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56557458 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 156.322850 USDC | 0.014155 USDC | 0.000000 USDC | 0.006129 USDC | 0.008026 USDC (0.0074 €) | — | 0.51 | 0.268 (n=1617) | REJECTED | below_safety_margin(8026<31264), p_lower_below_threshold(0.27<0.75) |
| 56557459 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 156.322850 USDC | 0.014155 USDC | 0.000000 USDC | 0.006129 USDC | 0.008026 USDC (0.0074 €) | — | 0.51 | 0.268 (n=1617) | REJECTED | below_safety_margin(8026<31264), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8421 ; taux observé 0.222 ; borne inférieure crédible (0.9) 0.216 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
