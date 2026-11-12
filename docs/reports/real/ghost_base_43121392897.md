# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T00:51:39+00:00 ; durée 67.46 min ; blocs 56251356 → 56271586 (3157 vus)

## Connexion
- Requêtes RPC : 45513 ; erreurs : 0 ; latence p50/p95 : 294.8/1,311.8 ms
- Rafraîchissements d'état : 3158 ; âge des données au dernier bloc : 5.17 s ; changements de frais LP observés (pools à frais dynamiques) : 2562
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4545 ; cycles déclenchés par événement : 1575 ; avance médiane sur le rafraîchissement multicall : 523 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,058.09 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 458 pools, 265 jetons, 15592 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 281, par paires 0), mesurés 460, sous le plancher de 10000.0 $ : 2 → gardés 458 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2049.11291, 'cbBTC': 73781.879924, 'AERO': 0.537258}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,601,102 | 2,058.089795 | 56271586 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,469,197 | 0.027849 | 56271586 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,647,670 | 0.027789 | 56271586 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,530,190 | 0.000014 | 56271586 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,116,413 | 2,062.115242 | 56271586 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,892,225 | 103.891217 | 56271586 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,596,752 | 0.027860 | 56271586 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,249,031 | 1.842553 | 56271586 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,025,700 | 2,062.715916 | 56271586 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,894,007 | 0.998581 | 56271586 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,068,200 | 42,108.748328 | 56271586 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 131 | 2,899,605 | 2,062.663633 | 56271586 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 2,209,533 | 0.027797 | 56271586 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,953,438 | 1,125,188.542308 | 56271586 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,650,242 | 0.000014 | 56271586 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,624,295 | 0.016420 | 56271586 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,609,030 | 0.000014 | 56271586 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,573,524 | 0.000000 | 56271586 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,544,882 | 0.006715 | 56271586 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,532,417 | 0.000014 | 56271586 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,921 | 0.830438 | 56271586 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,836 | 1.406597 | 56271586 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,411,501 | 427.694388 | 56271586 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,272,143 | 2,057.823082 | 56271586 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,262,504 | 3,792.849183 | 56271586 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,220,513 | 15,350.624928 | 56271586 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,158,053 | 2,059.870382 | 56271586 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,128,711 | 2,062.107363 | 56271586 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56271586 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,043,485 | 33,642,416.465512 | 56271586 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,027,940 | 104.619557 | 56271586 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 962,729 | 21.204328 | 56271586 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 938,596 | 565,857.464687 | 56271586 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 915,464 | 0.001478 | 56271586 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 904,174 | 0.000014 | 56271586 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 903,925 | 0.050429 | 56271586 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 898,209 | 23,358,136.408828 | 56271586 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 879,389 | 2,054.856011 | 56271586 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 877,225 | 1,029.520126 | 56271586 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 859,519 | 0.000000 | 56271586 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 781,956 | 76.925000 | 56271586 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 761,366 | 0.051707 | 56271586 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 749,193 | 22.944494 | 56271586 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 746,596 | 115,852.041712 | 56271586 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 707,853 | 3,786.866427 | 56271586 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 697,283 | 0.801801 | 56271586 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 668,248 | 0.530675 | 56271586 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 649,409 | 4,761,953.961094 | 56271586 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 616,775 | 0.478801 | 56271586 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 601,151 | 148,537.219488 | 56271586 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 587,561 | 0.000007 | 56271586 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 577,068 | 0.000257 | 56271586 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 575,052 | 561,639.517275 | 56271586 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 559,409 | 0.037662 | 56271586 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 489,666 | 1,029.839291 | 56271586 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 458,888 | 0.065863 | 56271586 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,788 | 1.000934 | 56271586 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,906 | 0.502364 | 56271586 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 441,491 | 24.808159 | 56271586 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 439,714 | 904,519.367544 | 56271586 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 4732 ; routes examinées : 73781344 ; candidats optimisés : 369818 ; net attendu > 0 : 180 ; dernier cycle 323.7 ms
- Rejets (moteur) : {'spread_below_threshold': 72096425, 'liquidity_below_min': 1309851, 'negative_expected_net': 369638, 'borrow_bound_too_small': 4719, 'cycle_budget_exhausted': 531}
- Enregistrements de la session : 369818 ; net attendu > 0 : 180 ; simulés (eth_call de la vraie tx) : 2 (ok 1, échec 1) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 369818} ; motifs de rejet : {'below_safety_margin': 178, 'negative_expected_net': 369638, 'p_lower_below_threshold': 170, 'reliability_not_demonstrated': 10, 'simulation_failed': 1, 'stale_data': 43}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56252219 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 310.545098 USDC | 0.024609 USDC | 0.000000 USDC | 0.004606 USDC | 0.020003 USDC (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(20003<62109), p_lower_below_threshold(0.10<0.75) |
| 56252220 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 310.545098 USDC | 0.024609 USDC | 0.000000 USDC | 0.004606 USDC | 0.020003 USDC (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(20003<62109), p_lower_below_threshold(0.10<0.75) |
| 56252219 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.151840 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(9758427752881<30368070316317), p_lower_below_threshold(0.10<0.75) |
| 56252220 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.151840 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(9758427752881<30368070316317), p_lower_below_threshold(0.10<0.75) |
| 56258818 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→WETH | 0.028626 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0137 €) | — | 2.53 | 0.103 (n=364) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 56266624 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 190.712068 USDC | 0.014891 USDC | 0.000000 USDC | 0.006183 USDC | 0.008708 USDC (0.0080 €) | — | 0.46 | 0.267 (n=1584) | REJECTED | below_safety_margin(8708<38142), p_lower_below_threshold(0.27<0.75) |
| 56266624 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 190.712068 USDC | 0.014891 USDC | 0.000000 USDC | 0.006183 USDC | 0.008708 USDC (0.0080 €) | — | 0.46 | 0.267 (n=1584) | REJECTED | below_safety_margin(8708<38142), p_lower_below_threshold(0.27<0.75) |
| 56266624 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.003009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0075 €) | — | 0.37 | 0.267 (n=1584) | REJECTED | below_safety_margin(11<60), p_lower_below_threshold(0.27<0.75) |
| 56266624 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.003009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0075 €) | — | 0.37 | 0.267 (n=1584) | REJECTED | below_safety_margin(11<60), p_lower_below_threshold(0.27<0.75) |
| 56266624 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.078034 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0075 €) | — | 0.51 | 0.267 (n=1584) | REJECTED | below_safety_margin(3945611638690<15606777291109), p_lower_below_threshold(0.27<0.75) |
| 56266624 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.078034 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0075 €) | — | 0.51 | 0.267 (n=1584) | REJECTED | below_safety_margin(3945611638690<15606777291109), p_lower_below_threshold(0.27<0.75) |
| 56263512 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 92.963658 USDC | 0.014055 USDC | 0.000000 USDC | 0.006177 USDC | 0.007878 USDC (0.0072 €) | — | 0.85 | 0.344 (n=610) | REJECTED | below_safety_margin(7878<18592), p_lower_below_threshold(0.34<0.75) |
| 56263512 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 92.963658 USDC | 0.014055 USDC | 0.000000 USDC | 0.006177 USDC | 0.007878 USDC (0.0072 €) | — | 0.85 | 0.344 (n=610) | REJECTED | below_safety_margin(7878<18592), stale_data(4617ms>4000.0), p_lower_below_threshold(0.34<0.75) |
| 56263512 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.045439 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0072 €) | — | 0.84 | 0.344 (n=610) | REJECTED | below_safety_margin(3816240924519<9087776409896), p_lower_below_threshold(0.34<0.75) |
| 56263512 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.045439 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0072 €) | — | 0.84 | 0.344 (n=610) | REJECTED | below_safety_margin(3816240924519<9087776409896), stale_data(4611ms>4000.0), p_lower_below_threshold(0.34<0.75) |
| 56266624 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 218.234444 USDC | 0.012054 USDC | 0.000000 USDC | 0.004620 USDC | 0.007434 USDC (0.0068 €) | — | 0.34 | 0.103 (n=365) | REJECTED | below_safety_margin(7434<43646), p_lower_below_threshold(0.10<0.75) |
| 56266624 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 218.234444 USDC | 0.012054 USDC | 0.000000 USDC | 0.004620 USDC | 0.007434 USDC (0.0068 €) | — | 0.34 | 0.103 (n=365) | REJECTED | below_safety_margin(7434<43646), p_lower_below_threshold(0.10<0.75) |
| 56266624 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.105938 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0068 €) | — | 0.34 | 0.103 (n=365) | REJECTED | below_safety_margin(3607939099755<21187670830985), p_lower_below_threshold(0.10<0.75) |
| 56266624 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.105938 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0068 €) | — | 0.34 | 0.103 (n=365) | REJECTED | below_safety_margin(3607939099755<21187670830985), p_lower_below_threshold(0.10<0.75) |
| 56252219 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 143.484105 USDC | 0.012065 USDC | 0.000000 USDC | 0.004917 USDC | 0.007148 USDC (0.0066 €) | — | 0.50 | 0.087 (n=116) | REJECTED | below_safety_margin(7148<28696), p_lower_below_threshold(0.09<0.75) |
| 56252220 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 143.484105 USDC | 0.012065 USDC | 0.000000 USDC | 0.004917 USDC | 0.007148 USDC (0.0066 €) | — | 0.50 | 0.087 (n=116) | REJECTED | below_safety_margin(7148<28696), p_lower_below_threshold(0.09<0.75) |
| 56252219 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.070478 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0066 €) | — | 0.49 | 0.087 (n=116) | REJECTED | below_safety_margin(3486419375392<14095681478295), p_lower_below_threshold(0.09<0.75) |
| 56252220 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.070478 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0066 €) | — | 0.49 | 0.087 (n=116) | REJECTED | below_safety_margin(3486419375392<14095681478295), p_lower_below_threshold(0.09<0.75) |
| 56266624 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 179.121564 USDC | 0.011013 USDC | 0.000000 USDC | 0.004620 USDC | 0.006393 USDC (0.0059 €) | — | 0.36 | 0.103 (n=365) | REJECTED | below_safety_margin(6393<35824), p_lower_below_threshold(0.10<0.75) |
| 56266624 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 179.121564 USDC | 0.011013 USDC | 0.000000 USDC | 0.004620 USDC | 0.006393 USDC (0.0059 €) | — | 0.36 | 0.103 (n=365) | REJECTED | below_safety_margin(6393<35824), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 8236 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
