# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T06:12:37+00:00 ; durée 314.61 min ; blocs 53309463 → 53318897 (9155 vus)

## Connexion
- Requêtes RPC : 107540 ; erreurs : 8 ; latence p50/p95 : 200.6/1,707.5 ms
- Rafraîchissements d'état : 9155 ; âge des données au dernier bloc : 6.45 s ; changements de frais LP observés (pools à frais dynamiques) : 8650
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 81479 ; cycles déclenchés par événement : 8291 ; avance médiane sur le rafraîchissement multicall : 586 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,240.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 506 pools, 291 jetons, 18872 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 117, aerodrome 207, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 179 (rejetés 2) → 584 jetons ; pools candidats 3782 (énumérés 322, par paires 0), mesurés 509, sous le plancher de 10000.0 $ : 3 → gardés 506 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2241.465194, 'cbBTC': 77391.917525, 'AERO': 0.626719}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,178,581 | 2,240.571457 | 53318898 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,990,501 | 0.029026 | 53318898 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,259,939 | 0.000013 | 53318898 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,013,638 | 0.029063 | 53318898 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,188,941 | 2,240.751155 | 53318898 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,668,777 | 101.231609 | 53318898 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,682,506 | 0.001622 | 53318898 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,895,823 | 1.601511 | 53318898 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,478,644 | 0.029031 | 53318898 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,126,977 | 2,239.963544 | 53318898 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,075,521 | 2,239.940158 | 53318898 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,059,290 | 1.000001 | 53318898 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,540,179 | 37,488.300127 | 53318898 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,746,956 | 0.029045 | 53318898 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,324,185 | 101.251500 | 53318898 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,054,311 | 1,206,019.233111 | 53318898 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,972,688 | 0.000013 | 53318898 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,751,298 | 0.000000 | 53318898 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,718,820 | 0.017398 | 53318898 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,679,796 | 422.128132 | 53318898 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,638,784 | 0.000013 | 53318898 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,590,829 | 2,240.957111 | 53318898 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,579,130 | 0.000013 | 53318898 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,540,980 | 1.502063 | 53318898 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/USDC | 3000 | 1,523,041 | 2,246.575456 | 53318898 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,570 | 0.825600 | 53318898 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 1,424,972 | 0.000013 | 53318898 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,419,142 | 3,590.996114 | 53318898 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,333,723 | 0.005248 | 53318898 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,301,373 | 14,539.096569 | 53318898 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,280,760 | 2,240.705737 | 53318898 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,176,817 | 70.165644 | 53318898 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,726 | 35,677,478.940151 | 53318898 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,058,702 | 513,290.543553 | 53318898 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,036,337 | 21,041,997.297808 | 53318898 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,024,001 | 73,118.513067 | 53318898 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | DRB/WETH | 10000 | 994,226 | 0.000000 | 53318898 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 992,580 | 19.359177 | 53318898 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 977,065 | 65.575212 | 53318898 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 961,979 | 100.509504 | 53318898 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 947,403 | 0.045202 | 53318898 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 930,094 | 1,213,314.424026 | 53318898 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,025 | 2,235.963227 | 53318898 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 899,459 | 1,065.008818 | 53318898 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 862,851 | 3,585.793582 | 53318898 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,950 | 0.000554 | 53318898 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 843,684 | 19.235208 | 53318898 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 824,354 | 0.061149 | 53318898 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,760 | 0.802842 | 53318898 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 737,144 | 0.000265 | 53318898 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 725,403 | 0.589602 | 53318898 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 724,225 | 4,521,937.892111 | 53318898 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 681,924 | 0.000008 | 53318898 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 660,021 | 2.331780 | 53318898 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 658,876 | 145,829.340819 | 53318898 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2123 | 657,703 | 517,561.995621 | 53318898 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 626,805 | 0.496993 | 53318898 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 614,067 | 0.093433 | 53318898 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 602,418 | 0.915183 | 53318898 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 544,630 | 1,065.405159 | 53318898 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 17445 ; routes examinées : 329222040 ; candidats optimisés : 1104527 ; net attendu > 0 : 123 ; dernier cycle 121.8 ms
- Rejets (moteur) : {'spread_below_threshold': 322389993, 'liquidity_below_min': 5597781, 'negative_expected_net': 1104404, 'pool_quarantined': 74714, 'unquotable': 35926, 'borrow_bound_too_small': 17424, 'cycle_budget_exhausted': 1675}
- Enregistrements de la session : 1104527 ; net attendu > 0 : 123 ; simulés (eth_call de la vraie tx) : 15 (ok 2, échec 13) ; étiquettes ghost N+1 : 0/9 positives
- Décisions : {'REJECTED': 1104527} ; motifs de rejet : {'below_safety_margin': 108, 'negative_expected_net': 1104404, 'p_lower_below_threshold': 110, 'price_impact': 5, 'reliability_not_demonstrated': 13, 'simulation_failed': 13, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53311518 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 156.809559 USDC | 0.574020 USDC | 0.000000 USDC | 0.005037 USDC | 0.568983 USDC (0.5235 €) | — | 36.28 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53311518 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 36.083248 USDC | 0.132511 USDC | 0.000000 USDC | 0.004728 USDC | 0.127783 USDC (0.1176 €) | — | 35.41 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53311962 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.132647 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0417 €) | — | 1.52 | 0.007 (n=40) | REJECTED | below_safety_margin(20200336303825<26529307582136), p_lower_below_threshold(0.01<0.75) |
| 53311962 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 297.246067 USDC | 0.051017 USDC | 0.000000 USDC | 0.005716 USDC | 0.045301 USDC (0.0417 €) | — | 1.52 | 0.007 (n=40) | REJECTED | below_safety_margin(45301<59449), p_lower_below_threshold(0.01<0.75) |
| 53312554 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.120908 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0318 €) | — | 1.28 | 0.007 (n=40) | REJECTED | below_safety_margin(15433686526591<24181676425436), p_lower_below_threshold(0.01<0.75) |
| 53312554 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 270.693097 USDC | 0.040326 USDC | 0.000000 USDC | 0.005718 USDC | 0.034608 USDC (0.0318 €) | — | 1.28 | 0.007 (n=40) | REJECTED | below_safety_margin(34608<54138), p_lower_below_threshold(0.01<0.75) |
| 53312554 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.120034 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0311 €) | — | 1.26 | 0.039 (n=152) | REJECTED | below_safety_margin(15070938891017<24006807585150), p_lower_below_threshold(0.04<0.75) |
| 53312554 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 269.084436 USDC | 0.039513 USDC | 0.000000 USDC | 0.005718 USDC | 0.033795 USDC (0.0311 €) | — | 1.26 | 0.039 (n=152) | REJECTED | below_safety_margin(33795<53816), p_lower_below_threshold(0.04<0.75) |
| 53312554 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002177 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0128 €) | — | 0.83 | 0.144 (n=648) | REJECTED | below_safety_margin(18<43), p_lower_below_threshold(0.14<0.75) |
| 53312554 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.092680 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0127 €) | — | 0.66 | 0.144 (n=648) | REJECTED | below_safety_margin(6132891148761<18536092021884), p_lower_below_threshold(0.14<0.75) |
| 53312554 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 205.265425 USDC | 0.020967 USDC | 0.000000 USDC | 0.007422 USDC | 0.013545 USDC (0.0125 €) | — | 0.66 | 0.144 (n=648) | REJECTED | below_safety_margin(13545<41053), p_lower_below_threshold(0.14<0.75) |
| 53311962 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.070188 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0098 €) | — | 0.68 | 0.039 (n=152) | REJECTED | below_safety_margin(4744697771754<14037556274620), p_lower_below_threshold(0.04<0.75) |
| 53311962 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 156.039900 USDC | 0.015676 USDC | 0.000000 USDC | 0.005035 USDC | 0.010641 USDC (0.0098 €) | — | 0.68 | 0.039 (n=152) | REJECTED | below_safety_margin(10641<31207), p_lower_below_threshold(0.04<0.75) |
| 53311962 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.060825 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | — | 0.68 | 0.144 (n=648) | REJECTED | below_safety_margin(4151995149371<12164987351071), p_lower_below_threshold(0.14<0.75) |
| 53312403 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 11.690860 USDC | 0.013894 USDC | 0.000000 USDC | 0.004726 USDC | 0.009168 USDC (0.0084 €) | — | 7.84 | 0.034 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53311962 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 134.368857 USDC | 0.016096 USDC | 0.000000 USDC | 0.007080 USDC | 0.009016 USDC (0.0083 €) | — | 0.67 | 0.144 (n=648) | REJECTED | below_safety_margin(9016<26873), p_lower_below_threshold(0.14<0.75) |
| 53312554 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.021929 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0083 €) | — | 1.82 | 0.007 (n=40) | REJECTED | below_safety_margin(4001287781270<4385899572285), p_lower_below_threshold(0.01<0.75) |
| 53312554 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 48.783390 USDC | 0.014005 USDC | 0.000000 USDC | 0.005037 USDC | 0.008968 USDC (0.0083 €) | — | 1.84 | 0.007 (n=40) | REJECTED | below_safety_margin(8968<9756), p_lower_below_threshold(0.01<0.75) |
| 53311962 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001611 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0078 €) | — | 0.68 | 0.144 (n=648) | REJECTED | below_safety_margin(11<32), p_lower_below_threshold(0.14<0.75) |
| 53309650 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000493 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0050 €) | — | 1.42 | 0.144 (n=648) | REJECTED | below_safety_margin(7<9), p_lower_below_threshold(0.14<0.75) |
| 53309651 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000493 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0050 €) | — | 1.42 | 0.144 (n=648) | REJECTED | below_safety_margin(7<9), p_lower_below_threshold(0.14<0.75) |
| 53309650 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.008857 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0047 €) | 0.000002 WETH | 2.58 | 0.285 (n=80) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 53309651 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.008857 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0047 €) | — | 2.58 | 0.285 (n=80) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.28<0.75) |
| 53309650 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 30.718101 USDC | 0.011829 USDC | 0.000000 USDC | 0.006741 USDC | 0.005088 USDC (0.0047 €) | — | 1.66 | 0.144 (n=648) | REJECTED | below_safety_margin(5088<6143), p_lower_below_threshold(0.14<0.75) |
| 53309651 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 30.718101 USDC | 0.011829 USDC | 0.000000 USDC | 0.006741 USDC | 0.005088 USDC (0.0047 €) | — | 1.66 | 0.144 (n=648) | REJECTED | below_safety_margin(5088<6143), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3907 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
