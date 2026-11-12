# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T05:36:35+00:00 ; durée 15.28 min ; blocs 56352481 → 56357055 (664 vus)

## Connexion
- Requêtes RPC : 9568 ; erreurs : 0 ; latence p50/p95 : 413.3/1,458.0 ms
- Rafraîchissements d'état : 664 ; âge des données au dernier bloc : 9.42 s ; changements de frais LP observés (pools à frais dynamiques) : 397
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 693 ; cycles déclenchés par événement : 309 ; avance médiane sur le rafraîchissement multicall : 518 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,045.22 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 265 jetons, 15538 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2045.219297, 'cbBTC': 73500.635487, 'AERO': 0.536237}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,917,773 | 2,045.219388 | 56357083 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,383,017 | 0.027787 | 56357083 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,685,503 | 0.027806 | 56357083 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,468,527 | 0.000014 | 56357083 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,089,361 | 2,043.275995 | 56357083 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,843,864 | 104.050560 | 56357083 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,570,629 | 0.027798 | 56357083 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,221,787 | 1.866369 | 56357083 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,133,234 | 2,043.760360 | 56357083 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,878,291 | 0.998581 | 56357083 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,042,896 | 42,278.213119 | 56357083 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 131 | 2,883,688 | 2,043.816807 | 56357083 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,195,082 | 0.027823 | 56357083 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,941,222 | 1,125,188.542308 | 56357083 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,645,145 | 0.000014 | 56357083 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,617,574 | 0.016316 | 56357083 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,589,819 | 0.000014 | 56357083 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,560,077 | 0.000000 | 56357083 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,528,497 | 0.000014 | 56357083 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,501,779 | 0.006537 | 56357083 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,228 | 0.830323 | 56357083 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,851 | 1.406571 | 56357083 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,401,138 | 429.328878 | 56357083 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,268,177 | 2,045.436111 | 56357083 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,249,450 | 3,811.690154 | 56357083 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,212,337 | 15,445.445330 | 56357083 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,153,917 | 2,046.873553 | 56357083 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,118,051 | 2,043.375590 | 56357083 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,558 | 86.391364 | 56357083 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,035,435 | 33,787,417.907718 | 56357083 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,015,611 | 104.123283 | 56357083 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,735 | 21.339384 | 56357083 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 933,081 | 565,229.971074 | 56357083 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 911,465 | 0.001477 | 56357083 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 900,787 | 0.000014 | 56357083 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 899,057 | 0.050939 | 56357083 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 893,966 | 23,297,417.836114 | 56357083 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 879,357 | 1,026.390348 | 56357083 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 876,553 | 2,054.853960 | 56357083 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 852,939 | 0.000000 | 56357083 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 779,823 | 77.346459 | 56357083 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 748,596 | 0.049934 | 56357083 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 745,966 | 23.082007 | 56357083 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 737,920 | 117,113.700323 | 56357083 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 701,125 | 3,786.866427 | 56357083 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 692,923 | 0.801801 | 56357083 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 666,035 | 0.525873 | 56357083 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 644,184 | 4,779,375.498766 | 56357083 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 616,818 | 0.478825 | 56357083 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 583,612 | 155,678.198371 | 56357083 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 574,173 | 0.000258 | 56357083 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 572,216 | 0.000007 | 56357083 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 571,800 | 560,727.867269 | 56357083 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,130 | 0.037323 | 56357083 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 486,807 | 1,025.632375 | 56357083 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 468,775 | 0.067687 | 56357083 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,541 | 1.001036 | 56357083 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 445,866 | 0.501968 | 56357083 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 438,802 | 24.807640 | 56357083 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 431,970 | 927,647.757410 | 56357083 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 972 ; routes examinées : 15102936 ; candidats optimisés : 67142 ; net attendu > 0 : 29 ; dernier cycle 192.0 ms
- Rejets (moteur) : {'spread_below_threshold': 14858028, 'liquidity_below_min': 176779, 'negative_expected_net': 67113, 'borrow_bound_too_small': 972, 'cycle_budget_exhausted': 15}
- Enregistrements de la session : 67142 ; net attendu > 0 : 29 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 67142} ; motifs de rejet : {'below_safety_margin': 29, 'negative_expected_net': 67113, 'p_lower_below_threshold': 29}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56352545 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003784 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.54 | 0.344 (n=610) | REJECTED | below_safety_margin(204108972654<756812506909), p_lower_below_threshold(0.34<0.75) |
| 56352546 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003784 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.54 | 0.344 (n=610) | REJECTED | below_safety_margin(204108972654<756812506909), p_lower_below_threshold(0.34<0.75) |
| 56352547 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003784 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.54 | 0.344 (n=610) | REJECTED | below_safety_margin(204108972654<756812506909), p_lower_below_threshold(0.34<0.75) |
| 56352548 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003784 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.54 | 0.344 (n=610) | REJECTED | below_safety_margin(204108972654<756812506909), p_lower_below_threshold(0.34<0.75) |
| 56352548 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003784 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.54 | 0.344 (n=610) | REJECTED | below_safety_margin(204108972654<756812506909), p_lower_below_threshold(0.34<0.75) |
| 56352545 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.684145 USDC | 0.006546 USDC | 0.000000 USDC | 0.006146 USDC | 0.000400 USDC (0.0004 €) | — | 0.52 | 0.344 (n=610) | REJECTED | below_safety_margin(400<1536), p_lower_below_threshold(0.34<0.75) |
| 56352546 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.684145 USDC | 0.006546 USDC | 0.000000 USDC | 0.006146 USDC | 0.000400 USDC (0.0004 €) | — | 0.52 | 0.344 (n=610) | REJECTED | below_safety_margin(400<1536), p_lower_below_threshold(0.34<0.75) |
| 56352547 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.684145 USDC | 0.006546 USDC | 0.000000 USDC | 0.006146 USDC | 0.000400 USDC (0.0004 €) | — | 0.52 | 0.344 (n=610) | REJECTED | below_safety_margin(400<1536), p_lower_below_threshold(0.34<0.75) |
| 56352548 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.684145 USDC | 0.006546 USDC | 0.000000 USDC | 0.006146 USDC | 0.000400 USDC (0.0004 €) | — | 0.52 | 0.344 (n=610) | REJECTED | below_safety_margin(400<1536), p_lower_below_threshold(0.34<0.75) |
| 56352548 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.684145 USDC | 0.006546 USDC | 0.000000 USDC | 0.006146 USDC | 0.000400 USDC (0.0004 €) | — | 0.52 | 0.344 (n=610) | REJECTED | below_safety_margin(400<1536), p_lower_below_threshold(0.34<0.75) |
| 56352545 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003761 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.36 | 0.267 (n=1585) | REJECTED | below_safety_margin(136978468898<752279609749), p_lower_below_threshold(0.27<0.75) |
| 56352546 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003761 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.36 | 0.267 (n=1585) | REJECTED | below_safety_margin(136978468898<752279609749), p_lower_below_threshold(0.27<0.75) |
| 56352547 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003761 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.36 | 0.267 (n=1585) | REJECTED | below_safety_margin(136978468898<752279609749), p_lower_below_threshold(0.27<0.75) |
| 56352548 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003761 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.36 | 0.267 (n=1585) | REJECTED | below_safety_margin(136978468898<752279609749), p_lower_below_threshold(0.27<0.75) |
| 56352548 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003761 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.36 | 0.267 (n=1585) | REJECTED | below_safety_margin(136978468898<752279609749), p_lower_below_threshold(0.27<0.75) |
| 56352545 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.595327 USDC | 0.006409 USDC | 0.000000 USDC | 0.006146 USDC | 0.000263 USDC (0.0002 €) | — | 0.35 | 0.267 (n=1585) | REJECTED | below_safety_margin(263<1519), p_lower_below_threshold(0.27<0.75) |
| 56352546 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.595327 USDC | 0.006409 USDC | 0.000000 USDC | 0.006146 USDC | 0.000263 USDC (0.0002 €) | — | 0.35 | 0.267 (n=1585) | REJECTED | below_safety_margin(263<1519), p_lower_below_threshold(0.27<0.75) |
| 56352547 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.595327 USDC | 0.006409 USDC | 0.000000 USDC | 0.006146 USDC | 0.000263 USDC (0.0002 €) | — | 0.35 | 0.267 (n=1585) | REJECTED | below_safety_margin(263<1519), p_lower_below_threshold(0.27<0.75) |
| 56352548 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.595327 USDC | 0.006409 USDC | 0.000000 USDC | 0.006146 USDC | 0.000263 USDC (0.0002 €) | — | 0.35 | 0.267 (n=1585) | REJECTED | below_safety_margin(263<1519), p_lower_below_threshold(0.27<0.75) |
| 56352548 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.595327 USDC | 0.006409 USDC | 0.000000 USDC | 0.006146 USDC | 0.000263 USDC (0.0002 €) | — | 0.35 | 0.267 (n=1585) | REJECTED | below_safety_margin(263<1519), p_lower_below_threshold(0.27<0.75) |
| 56352518 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003673 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.09 | 0.267 (n=1585) | REJECTED | below_safety_margin(33311596084<734691644414), p_lower_below_threshold(0.27<0.75) |
| 56352520 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003673 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.09 | 0.267 (n=1585) | REJECTED | below_safety_margin(33311596084<734691644414), p_lower_below_threshold(0.27<0.75) |
| 56352521 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003673 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.09 | 0.267 (n=1585) | REJECTED | below_safety_margin(33311596084<734691644414), p_lower_below_threshold(0.27<0.75) |
| 56352518 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.442754 USDC | 0.006197 USDC | 0.000000 USDC | 0.006146 USDC | 0.000051 USDC (0.0000 €) | — | 0.07 | 0.267 (n=1585) | REJECTED | below_safety_margin(51<1488), p_lower_below_threshold(0.27<0.75) |
| 56352520 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.442754 USDC | 0.006197 USDC | 0.000000 USDC | 0.006146 USDC | 0.000051 USDC (0.0000 €) | — | 0.07 | 0.267 (n=1585) | REJECTED | below_safety_margin(51<1488), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8240 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
