# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T03:55:00+00:00 ; durée 54.88 min ; blocs 53718130 → 53734598 (2023 vus)

## Connexion
- Requêtes RPC : 35290 ; erreurs : 10 ; latence p50/p95 : 351.8/1,161.6 ms
- Rafraîchissements d'état : 2023 ; âge des données au dernier bloc : 5.04 s ; changements de frais LP observés (pools à frais dynamiques) : 1509
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 510 ; cycles déclenchés par événement : 193 ; avance médiane sur le rafraîchissement multicall : 344 ms
- Gaz : base fee 0.005005 gwei ; prix ETH (pool le plus profond) : 2,231.22 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 488 pools, 283 jetons, 18176 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 104, aerodrome 201, pancakeswap_v3 31, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3755 (énumérés 304, par paires 0), mesurés 491, sous le plancher de 10000.0 $ : 3 → gardés 488 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2237.238829, 'cbBTC': 76116.143211, 'AERO': 0.590143}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,016,914 | 2,231.217665 | 53734598 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,501,437 | 0.029450 | 53734598 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,057,303 | 0.029375 | 53734598 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,862,824 | 0.000013 | 53734598 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,948,501 | 2,232.672577 | 53734598 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,301,811 | 109.183505 | 53734598 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,407,760 | 0.001548 | 53734598 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,025,667 | 1.697569 | 53734598 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,692,106 | 0.029451 | 53734598 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,121,299 | 2,232.013197 | 53734598 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,991,684 | 0.998657 | 53734598 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,277,647 | 43,368.522984 | 53734598 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,206,463 | 2,231.991599 | 53734598 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,554,853 | 0.029395 | 53734598 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,077,258 | 1,169,496.608639 | 53734598 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,829,073 | 0.007487 | 53734598 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,747,056 | 0.000013 | 53734598 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,641,790 | 0.000000 | 53734598 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,641,167 | 0.016502 | 53734598 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,637,815 | 0.000013 | 53734598 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,535,089 | 1.448073 | 53734598 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,523,440 | 0.000013 | 53734598 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,519,390 | 439.985759 | 53734598 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,000 | 0.816940 | 53734598 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,359,467 | 3,785.557015 | 53734598 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,640 | 2,231.629284 | 53734598 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,322,249 | 2,233.502149 | 53734598 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,264,456 | 14,965.926977 | 53734598 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,161,980 | 2,232.677110 | 53734598 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,791 | 76.942850 | 53734598 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,091,642 | 37,415,085.623295 | 53734598 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,032,509 | 108.463560 | 53734598 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,017,079 | 568,968.629839 | 53734598 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,005,411 | 0.000000 | 53734598 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 993,066 | 22,588,921.913143 | 53734598 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 974,222 | 20.453850 | 53734598 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 943,481 | 1,051.418785 | 53734598 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 933,729 | 2,225.341209 | 53734598 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 927,836 | 72.835674 | 53734598 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 923,657 | 0.000013 | 53734598 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 870,633 | 100,186.893023 | 53734598 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 842,585 | 0.000538 | 53734598 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 830,181 | 0.048910 | 53734598 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 793,465 | 21.134394 | 53734598 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 786,860 | 3,808.350080 | 53734598 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,509 | 0.055333 | 53734598 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 756,932 | 0.799699 | 53734598 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 714,701 | 0.570083 | 53734598 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 692,971 | 4,905,226.486955 | 53734598 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 682,371 | 0.000254 | 53734598 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 663,674 | 142,851.996348 | 53734598 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 653,926 | 0.537331 | 53734598 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 643,363 | 0.000008 | 53734598 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 621,064 | 566,835.989651 | 53734598 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 598,032 | 0.914663 | 53734598 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 595,271 | 2.479369 | 53734598 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,758 | 0.037457 | 53734598 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 541,250 | 833,779.030008 | 53734598 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2724 | 528,772 | 1,051.650739 | 53734598 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/USDC | 100 | 524,855 | 2,231.779543 | 53734598 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 2215 ; routes examinées : 40259840 ; candidats optimisés : 116844 ; net attendu > 0 : 29 ; dernier cycle 259.9 ms
- Rejets (moteur) : {'spread_below_threshold': 39585217, 'liquidity_below_min': 555392, 'negative_expected_net': 116815, 'borrow_bound_too_small': 2211, 'cycle_budget_exhausted': 111}
- Enregistrements de la session : 116842 ; net attendu > 0 : 29 ; simulés (eth_call de la vraie tx) : 3 (ok 3, échec 0) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 116842} ; motifs de rejet : {'below_safety_margin': 23, 'negative_expected_net': 116813, 'p_lower_below_threshold': 26, 'reliability_not_demonstrated': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53725304 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.156652 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0218 €) | — | 0.67 | 0.046 (n=234) | REJECTED | below_safety_margin(10572709808215<31330346245869), p_lower_below_threshold(0.05<0.75) |
| 53725304 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 347.087299 USDC | 0.028661 USDC | 0.000000 USDC | 0.005056 USDC | 0.023605 USDC (0.0217 €) | — | 0.68 | 0.046 (n=234) | REJECTED | below_safety_margin(23605<69417), p_lower_below_threshold(0.05<0.75) |
| 53725304 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.005171 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0168 €) | — | 0.46 | 0.029 (n=28) | REJECTED | below_safety_margin(24<103), reliability_not_demonstrated |
| 53725304 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 362.277498 USDC | 0.024862 USDC | 0.000000 USDC | 0.007108 USDC | 0.017754 USDC (0.0163 €) | — | 0.49 | 0.029 (n=28) | REJECTED | below_safety_margin(17754<72455), reliability_not_demonstrated |
| 53725304 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.182958 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0162 €) | — | 0.43 | 0.029 (n=28) | REJECTED | below_safety_margin(7872478763124<36591648302483), reliability_not_demonstrated |
| 53732366 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 10.621985 USDC | 0.011366 USDC | 0.000000 USDC | 0.006706 USDC | 0.004660 USDC (0.0043 €) | — | 4.39 | 0.275 (n=354) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 53732366 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004782 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | 0.000002 WETH | 4.36 | 0.275 (n=354) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 53725304 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.054607 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0035 €) | — | 0.31 | 0.054 (n=80) | REJECTED | below_safety_margin(1716234941059<10921392512990), p_lower_below_threshold(0.05<0.75) |
| 53725304 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 122.519288 USDC | 0.008882 USDC | 0.000000 USDC | 0.005056 USDC | 0.003826 USDC (0.0035 €) | — | 0.31 | 0.054 (n=80) | REJECTED | below_safety_margin(3826<24503), p_lower_below_threshold(0.05<0.75) |
| 53732366 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 10.189995 USDC | 0.010391 USDC | 0.000000 USDC | 0.006706 USDC | 0.003685 USDC (0.0034 €) | — | 3.62 | 0.275 (n=354) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 53732366 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004606 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0034 €) | 0.000002 WETH | 3.58 | 0.275 (n=354) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 53732366 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.189995 USDC | 0.010275 USDC | 0.000000 USDC | 0.006706 USDC | 0.003569 USDC (0.0033 €) | — | 3.50 | 0.150 (n=775) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53732366 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004579 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0033 €) | 0.000002 WETH | 3.49 | 0.150 (n=775) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53719627 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.36 | 0.168 (n=1023) | REJECTED | below_safety_margin(3<16), p_lower_below_threshold(0.17<0.75) |
| 53719627 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.36 | 0.168 (n=1023) | REJECTED | below_safety_margin(3<16), p_lower_below_threshold(0.17<0.75) |
| 53719627 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.030204 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 0.33 | 0.168 (n=1023) | REJECTED | below_safety_margin(998400457097<6040730406466), p_lower_below_threshold(0.17<0.75) |
| 53719627 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.030204 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 0.33 | 0.168 (n=1023) | REJECTED | below_safety_margin(998400457097<6040730406466), p_lower_below_threshold(0.17<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 73.774811 USDC | 0.008830 USDC | 0.000000 USDC | 0.006735 USDC | 0.002095 USDC (0.0019 €) | — | 0.28 | 0.168 (n=1023) | REJECTED | below_safety_margin(2095<14754), p_lower_below_threshold(0.17<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 73.774811 USDC | 0.008830 USDC | 0.000000 USDC | 0.006735 USDC | 0.002095 USDC (0.0019 €) | — | 0.28 | 0.168 (n=1023) | REJECTED | below_safety_margin(2095<14754), p_lower_below_threshold(0.17<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 42.144036 USDC | 0.008506 USDC | 0.000000 USDC | 0.006735 USDC | 0.001771 USDC (0.0016 €) | — | 0.42 | 0.237 (n=401) | REJECTED | below_safety_margin(1771<8428), p_lower_below_threshold(0.24<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 42.144036 USDC | 0.008506 USDC | 0.000000 USDC | 0.006735 USDC | 0.001771 USDC (0.0016 €) | — | 0.42 | 0.237 (n=401) | REJECTED | below_safety_margin(1771<8428), p_lower_below_threshold(0.24<0.75) |
| 53719627 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018871 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 0.42 | 0.237 (n=401) | REJECTED | below_safety_margin(786924803159<3774194771479), p_lower_below_threshold(0.24<0.75) |
| 53719627 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018871 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 0.42 | 0.237 (n=401) | REJECTED | below_safety_margin(786924803159<3774194771479), p_lower_below_threshold(0.24<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 99.256286 USDC | 0.006073 USDC | 0.000000 USDC | 0.005032 USDC | 0.001041 USDC (0.0010 €) | — | 0.10 | 0.054 (n=80) | REJECTED | below_safety_margin(1041<19851), p_lower_below_threshold(0.05<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 99.256286 USDC | 0.006073 USDC | 0.000000 USDC | 0.005032 USDC | 0.001041 USDC (0.0010 €) | — | 0.10 | 0.054 (n=80) | REJECTED | below_safety_margin(1041<19851), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5793 ; taux observé 0.159 ; borne inférieure crédible (0.9) 0.153 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
