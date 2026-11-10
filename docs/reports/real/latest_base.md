# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T08:50:44+00:00 ; durée 24.3 min ; blocs 55544026 → 55551305 (1694 vus)

## Connexion
- Requêtes RPC : 20820 ; erreurs : 0 ; latence p50/p95 : 146.2/957.4 ms
- Rafraîchissements d'état : 1694 ; âge des données au dernier bloc : 7.9 s ; changements de frais LP observés (pools à frais dynamiques) : 553
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1476 ; cycles déclenchés par événement : 523 ; avance médiane sur le rafraîchissement multicall : 305 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,113.19 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 469 pools, 272 jetons, 17808 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 102, aerodrome 191, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3655 (énumérés 290, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 2 → gardés 469 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2115.286044, 'cbBTC': 74654.762075, 'AERO': 0.563979}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 138,905,033 | 2,113.192195 | 55551330 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,553,802 | 0.028344 | 55551330 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,356,051 | 0.000013 | 55551330 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,797,569 | 0.028336 | 55551330 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,471,959 | 2,112.841390 | 55551330 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,255,980 | 99.035501 | 55551330 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,921,874 | 0.028346 | 55551330 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,397,224 | 1.770071 | 55551330 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,021,491 | 2,113.664029 | 55551330 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,920,159 | 1.000001 | 55551330 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,102,144 | 43,427.942426 | 55551330 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,008,483 | 2,113.536460 | 55551330 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,332,540 | 0.028324 | 55551330 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,015,123 | 1,114,733.552638 | 55551330 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,706,341 | 0.000013 | 55551330 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 1,679,199 | 0.000013 | 55551330 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,603,198 | 0.016109 | 55551330 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,551,554 | 0.000000 | 55551330 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,546,545 | 0.006524 | 55551330 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,499,607 | 0.000013 | 55551330 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,457,856 | 422.400353 | 55551330 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,534 | 0.821103 | 55551330 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,424,441 | 1.429325 | 55551330 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,296,802 | 3,744.026534 | 55551330 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,288,796 | 2,113.486789 | 55551330 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,247,031 | 14,922.287888 | 55551330 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,217,226 | 2,116.275250 | 55551330 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,778 | 79.326458 | 55551330 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,075,500 | 2,112.852178 | 55551330 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,411 | 35,669,903.877610 | 55551330 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 967,861 | 98.537690 | 55551330 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 962,550 | 568,564.690782 | 55551330 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 959,491 | 21.423317 | 55551330 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 958,136 | 0.046975 | 55551330 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 932,009 | 0.001506 | 55551330 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 929,721 | 23,039,733.174810 | 55551330 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 925,770 | 0.000013 | 55551330 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 922,053 | 73.704924 | 55551330 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 903,698 | 1,038.115414 | 55551330 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 898,132 | 0.000000 | 55551330 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 886,366 | 2,127.157333 | 55551330 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 804,300 | 105,241.033389 | 55551330 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 775,150 | 21.867446 | 55551330 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 762,307 | 0.051845 | 55551330 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 738,941 | 3,752.968754 | 55551330 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 717,414 | 0.798536 | 55551330 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 663,253 | 0.543014 | 55551330 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 653,833 | 4,945,173.960633 | 55551330 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,234 | 0.527686 | 55551330 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 613,969 | 0.000008 | 55551330 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 603,601 | 155,108.929046 | 55551330 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 593,817 | 0.000256 | 55551330 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 588,816 | 565,419.771535 | 55551330 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,830 | 0.038466 | 55551330 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 509,756 | 1,037.789697 | 55551330 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 494,575 | 6,694.987206 | 55551330 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| aerodrome | WETH/msETH (stable) | 500 | 494,021 | 2.397327 | 55551330 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 466,450 | 0.067312 | 55551330 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/uSOL | 3000 | 466,162 | 24.739805 | 55551330 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 460,554 | 300.551982 | 55551330 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 2216 ; routes examinées : 39462528 ; candidats optimisés : 134631 ; net attendu > 0 : 306 ; dernier cycle 391.3 ms
- Rejets (moteur) : {'spread_below_threshold': 38872905, 'liquidity_below_min': 451092, 'negative_expected_net': 134325, 'borrow_bound_too_small': 2216, 'pool_quarantined': 1248, 'cycle_budget_exhausted': 436}
- Enregistrements de la session : 134631 ; net attendu > 0 : 306 ; simulés (eth_call de la vraie tx) : 42 (ok 16, échec 26) ; étiquettes ghost N+1 : 10/32 positives
- Décisions : {'REJECTED': 134631} ; motifs de rejet : {'below_safety_margin': 182, 'negative_expected_net': 134325, 'p_lower_below_threshold': 288, 'reliability_not_demonstrated': 18, 'simulation_failed': 26}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.143238 WETH | 0.000377 WETH | 0.000000 WETH | 0.000003 WETH | 0.000374 WETH (0.7285 €) | — | 26.13 | 0.024 (n=60) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 302.705180 USDC | 0.796992 USDC | 0.000000 USDC | 0.006358 USDC | 0.790634 USDC (0.7274 €) | — | 26.12 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.141890 WETH | 0.000376 WETH | 0.000000 WETH | 0.000003 WETH | 0.000372 WETH (0.7249 €) | — | 26.25 | 0.024 (n=60) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.142907 WETH | 0.000375 WETH | 0.000000 WETH | 0.000003 WETH | 0.000372 WETH (0.7239 €) | — | 26.03 | 0.024 (n=60) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 299.512996 USDC | 0.793121 USDC | 0.000000 USDC | 0.006358 USDC | 0.786763 USDC (0.7238 €) | — | 26.27 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 301.719894 USDC | 0.792032 USDC | 0.000000 USDC | 0.006358 USDC | 0.785674 USDC (0.7228 €) | — | 26.04 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.139239 WETH | 0.000362 WETH | 0.000000 WETH | 0.000003 WETH | 0.000359 WETH (0.6982 €) | — | 25.77 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 294.039094 USDC | 0.764215 USDC | 0.000000 USDC | 0.006358 USDC | 0.757857 USDC (0.6972 €) | — | 25.77 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.134225 WETH | 0.000349 WETH | 0.000000 WETH | 0.000003 WETH | 0.000346 WETH (0.6726 €) | — | 25.75 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 283.401363 USDC | 0.737190 USDC | 0.000000 USDC | 0.007000 USDC | 0.730190 USDC (0.6718 €) | — | 25.77 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 199.001047 USDC | 0.528660 USDC | 0.000000 USDC | 0.006358 USDC | 0.522302 USDC (0.4805 €) | — | 26.25 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.094206 WETH | 0.000250 WETH | 0.000000 WETH | 0.000003 WETH | 0.000247 WETH (0.4804 €) | — | 26.20 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.089394 WETH | 0.000084 WETH | 0.000000 WETH | 0.000003 WETH | 0.000081 WETH (0.1582 €) | — | 9.09 | 0.124 (n=223) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55544129 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 188.439373 USDC | 0.178035 USDC | 0.000000 USDC | 0.006358 USDC | 0.171677 USDC (0.1579 €) | — | 9.11 | 0.124 (n=223) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55544129 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.090601 WETH | 0.000084 WETH | 0.000000 WETH | 0.000003 WETH | 0.000081 WETH (0.1579 €) | — | 8.95 | 0.124 (n=223) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55544129 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 190.888727 USDC | 0.177691 USDC | 0.000000 USDC | 0.006358 USDC | 0.171333 USDC (0.1576 €) | — | 8.98 | 0.124 (n=223) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55544129 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.089733 WETH | 0.000083 WETH | 0.000000 WETH | 0.000003 WETH | 0.000080 WETH (0.1548 €) | — | 8.86 | 0.056 (n=133) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55544129 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 189.153229 USDC | 0.174338 USDC | 0.000000 USDC | 0.006358 USDC | 0.167980 USDC (0.1545 €) | — | 8.88 | 0.056 (n=133) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55544129 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.068345 WETH | 0.000078 WETH | 0.000000 WETH | 0.000003 WETH | 0.000075 WETH (0.1458 €) | — | 10.96 | 0.124 (n=223) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55544129 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 144.215400 USDC | 0.164860 USDC | 0.000000 USDC | 0.006679 USDC | 0.158181 USDC (0.1455 €) | — | 10.97 | 0.124 (n=223) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55544129 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.068786 WETH | 0.000078 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1447 €) | — | 10.81 | 0.124 (n=223) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55544129 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 144.878037 USDC | 0.163735 USDC | 0.000000 USDC | 0.006679 USDC | 0.157056 USDC (0.1445 €) | — | 10.84 | 0.124 (n=223) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55544129 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.068228 WETH | 0.000076 WETH | 0.000000 WETH | 0.000003 WETH | 0.000073 WETH (0.1423 €) | — | 10.72 | 0.056 (n=133) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55544129 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 143.771753 USDC | 0.161117 USDC | 0.000000 USDC | 0.006679 USDC | 0.154438 USDC (0.1421 €) | — | 10.74 | 0.056 (n=133) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55544129 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.084858 WETH | 0.000076 WETH | 0.000000 WETH | 0.000003 WETH | 0.000073 WETH (0.1416 €) | — | 8.58 | 0.056 (n=133) | REJECTED | p_lower_below_threshold(0.06<0.75) |

## Fiabilité et décision
- Observations ghost : 7323 ; taux observé 0.188 ; borne inférieure crédible (0.9) 0.182 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
