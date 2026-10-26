# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T12:19:21+00:00 ; durée 221.84 min ; blocs 53107248 → 53113904 (6428 vus)

## Connexion
- Requêtes RPC : 75681 ; erreurs : 63 ; latence p50/p95 : 225.4/1,183.1 ms
- Rafraîchissements d'état : 6428 ; âge des données au dernier bloc : 2.91 s ; changements de frais LP observés (pools à frais dynamiques) : 11118
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11567 ; cycles déclenchés par événement : 845 ; avance médiane sur le rafraîchissement multicall : 492 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,328.36 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 527 pools, 302 jetons, 19574 routes
- Par DEX : uniswap_v3 142, aerodrome 213, aerodrome_slipstream 127, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 188 (rejetés 2) → 593 jetons ; pools candidats 3779 (énumérés 339, par paires 0), mesurés 529, sous le plancher de 10000.0 $ : 2 → gardés 527 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2317.899718, 'cbBTC': 80102.759686, 'AERO': 0.672129}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,238,990 | 2,328.362598 | 53113905 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,784,833 | 0.029016 | 53113905 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,201,488 | 0.028978 | 53113905 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,485,340 | 0.000012 | 53113905 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,805,256 | 94.702657 | 53113905 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,333,303 | 2,328.204157 | 53113905 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,161,021 | 1.484936 | 53113905 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,013,854 | 0.001654 | 53113905 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,404,355 | 2,327.164149 | 53113905 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,376,401 | 0.029020 | 53113905 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,469,520 | 2,327.247420 | 53113905 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,224,220 | 0.998980 | 53113905 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,818,074 | 34,809.602346 | 53113905 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,756,889 | 2,328.997052 | 53113905 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,224,338 | 0.028971 | 53113905 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,491,700 | 94.742942 | 53113905 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,483,639 | 0.000012 | 53113905 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,204,092 | 409.664140 | 53113905 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,131,083 | 1,210,234.968788 | 53113905 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,895,383 | 0.000000 | 53113905 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,888,875 | 0.000012 | 53113905 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,823,637 | 0.018581 | 53113905 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,716,118 | 0.000012 | 53113905 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,699,795 | 0.000012 | 53113905 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,559,840 | 0.000265 | 53113905 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,484 | 0.825901 | 53113905 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53113905 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,445,942 | 0.005553 | 53113905 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,423,167 | 3,456.575630 | 53113905 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,366,979 | 14,123.233346 | 53113905 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,237,112 | 0.000265 | 53113905 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/AERO | 10000 | 1,237,111 | 3,480.912872 | 53113905 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,220,638 | 65.218151 | 53113905 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,215,690 | 2,328.202050 | 53113905 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,167,141 | 0.000000 | 53113905 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,140,900 | 1,092,745.921457 | 53113905 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,133,975 | 37,837,648.056064 | 53113905 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,109,923 | 499,749.695717 | 53113905 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,071,314 | 72,385.753447 | 53113905 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,055,622 | 20,650,683.672308 | 53113905 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,052,563 | 56.535805 | 53113905 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,030,542 | 17.415551 | 53113905 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 965,913 | 0.040684 | 53113905 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 924,031 | 2,312.265191 | 53113905 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 909,591 | 2.311243 | 53113905 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,594 | 0.000551 | 53113905 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/MORPHO | 3000 | 879,121 | 1,148.502932 | 53113905 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 878,496 | 17.185816 | 53113905 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4570 | 875,379 | 18.091039 | 53113905 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 868,357 | 94.690981 | 53113905 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 846,325 | 2,328.449958 | 53113905 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 798,365 | 0.000008 | 53113905 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 792,830 | 0.056329 | 53113905 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 788,343 | 0.803142 | 53113905 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 778,432 | 1.105941 | 53113905 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 746,032 | 0.618239 | 53113905 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 732,384 | 4,771,292.594891 | 53113905 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 704,897 | 137,328.031425 | 53113905 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 697,940 | 0.612970 | 53113905 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 693,348 | 501,684.780147 | 53113905 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 7272 ; routes examinées : 142342128 ; candidats optimisés : 412192 ; net attendu > 0 : 117 ; dernier cycle 245.7 ms
- Rejets (moteur) : {'spread_below_threshold': 140112562, 'liquidity_below_min': 1662925, 'negative_expected_net': 412075, 'unquotable': 146658, 'borrow_bound_too_small': 7267, 'cycle_budget_exhausted': 524}
- Enregistrements de la session : 412192 ; net attendu > 0 : 117 ; simulés (eth_call de la vraie tx) : 8 (ok 5, échec 3) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 412192} ; motifs de rejet : {'below_safety_margin': 109, 'negative_expected_net': 412075, 'p_lower_below_threshold': 110, 'price_impact': 1, 'reliability_not_demonstrated': 7, 'simulation_failed': 3, 'stale_data': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53113838 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 57.394422 USDC | 0.073073 USDC | 0.000000 USDC | 0.005230 USDC | 0.067843 USDC (0.0624 €) | — | 11.82 | 0.000 (n=51) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53113383 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 35.563030 USDC | 0.027254 USDC | 0.000000 USDC | 0.005232 USDC | 0.022022 USDC (0.0203 €) | 0.022022 USDC | 6.19 | 0.002 (n=134) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53113383 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 35.563030 USDC | 0.027254 USDC | 0.000000 USDC | 0.005232 USDC | 0.022022 USDC (0.0203 €) | 0.022022 USDC | 6.19 | 0.002 (n=134) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53113418 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.184010 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0054 €) | — | 0.14 | 0.022 (n=95) | REJECTED | below_safety_margin(2497999458590<36802053422786), p_lower_below_threshold(0.02<0.75) |
| 53113419 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.184010 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0054 €) | — | 0.14 | 0.022 (n=95) | REJECTED | below_safety_margin(2497999458590<36802053422786), p_lower_below_threshold(0.02<0.75) |
| 53113418 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 430.913300 USDC | 0.011045 USDC | 0.000000 USDC | 0.005230 USDC | 0.005815 USDC (0.0053 €) | — | 0.13 | 0.022 (n=95) | REJECTED | below_safety_margin(5815<86182), p_lower_below_threshold(0.02<0.75) |
| 53113419 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 430.913300 USDC | 0.011045 USDC | 0.000000 USDC | 0.005230 USDC | 0.005815 USDC (0.0053 €) | — | 0.13 | 0.022 (n=95) | REJECTED | below_safety_margin(5815<86182), p_lower_below_threshold(0.02<0.75) |
| 53107366 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 63.193801 USDC | 0.009983 USDC | 0.000000 USDC | 0.005224 USDC | 0.004759 USDC (0.0044 €) | — | 0.75 | 0.022 (n=95) | REJECTED | below_safety_margin(4759<12638), p_lower_below_threshold(0.02<0.75) |
| 53107366 | WETH→[pancakeswap_v3]→USDC→[sushiswap_v3]→WETH | 0.027089 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0044 €) | — | 0.75 | 0.022 (n=95) | REJECTED | below_safety_margin(2036524520673<5417835819103), p_lower_below_threshold(0.02<0.75) |
| 53113890 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.016247 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 1.22 | 0.133 (n=344) | REJECTED | below_safety_margin(1986842600651<3249449387170), p_lower_below_threshold(0.13<0.75) |
| 53113890 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.016247 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 1.22 | 0.133 (n=344) | REJECTED | below_safety_margin(1986842600651<3249449387170), p_lower_below_threshold(0.13<0.75) |
| 53113890 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 37.532616 USDC | 0.011977 USDC | 0.000000 USDC | 0.007355 USDC | 0.004622 USDC (0.0043 €) | — | 1.23 | 0.133 (n=344) | REJECTED | below_safety_margin(4622<7506), p_lower_below_threshold(0.13<0.75) |
| 53113890 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 37.532616 USDC | 0.011977 USDC | 0.000000 USDC | 0.007355 USDC | 0.004622 USDC (0.0043 €) | — | 1.23 | 0.133 (n=344) | REJECTED | below_safety_margin(4622<7506), p_lower_below_threshold(0.13<0.75) |
| 53108445 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.494862 USDC | 0.008361 USDC | 0.000000 USDC | 0.005220 USDC | 0.003141 USDC (0.0029 €) | — | 1.61 | 0.022 (n=95) | REJECTED | below_safety_margin(3141<3898), p_lower_below_threshold(0.02<0.75) |
| 53108189 | WETH→[aerodrome]→doginme→[uniswap_v3]→WETH | 0.000430 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0028 €) | 0.000001 WETH | 30.08 | 0.000 (n=22) | REJECTED | price_impact(200bps>150.0), reliability_not_demonstrated |
| 53111495 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.030554 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0025 €) | — | 0.39 | 0.184 (n=176) | REJECTED | below_safety_margin(1188648585199<6110749115033), p_lower_below_threshold(0.18<0.75) |
| 53111495 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 71.077813 USDC | 0.009753 USDC | 0.000000 USDC | 0.006997 USDC | 0.002756 USDC (0.0025 €) | — | 0.39 | 0.184 (n=176) | REJECTED | below_safety_margin(2756<14215), p_lower_below_threshold(0.18<0.75) |
| 53113655 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004782 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0022 €) | 0.000001 WETH | 2.17 | 0.184 (n=176) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53113655 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004782 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0022 €) | — | 2.17 | 0.184 (n=176) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 53113655 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 11.114795 USDC | 0.009417 USDC | 0.000000 USDC | 0.007001 USDC | 0.002416 USDC (0.0022 €) | 0.002416 USDC | 2.17 | 0.184 (n=176) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53113655 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 11.114795 USDC | 0.009417 USDC | 0.000000 USDC | 0.007001 USDC | 0.002416 USDC (0.0022 €) | — | 2.17 | 0.184 (n=176) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 53113655 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004718 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 1.83 | 0.133 (n=344) | REJECTED | below_safety_margin(861117352160<943539983062), p_lower_below_threshold(0.13<0.75) |
| 53113655 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004718 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 1.83 | 0.133 (n=344) | REJECTED | below_safety_margin(861117352160<943539983062), p_lower_below_threshold(0.13<0.75) |
| 53113655 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.890832 USDC | 0.009001 USDC | 0.000000 USDC | 0.007001 USDC | 0.002000 USDC (0.0018 €) | — | 1.84 | 0.133 (n=344) | REJECTED | below_safety_margin(2000<2178), p_lower_below_threshold(0.13<0.75) |
| 53113655 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.890832 USDC | 0.009001 USDC | 0.000000 USDC | 0.007001 USDC | 0.002000 USDC (0.0018 €) | — | 1.84 | 0.133 (n=344) | REJECTED | below_safety_margin(2000<2178), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2612 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
