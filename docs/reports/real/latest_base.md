# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T06:56:29+00:00 ; durée 235.14 min ; blocs 53097164 → 53104218 (7042 vus)

## Connexion
- Requêtes RPC : 85015 ; erreurs : 10 ; latence p50/p95 : 70.9/868.9 ms
- Rafraîchissements d'état : 7043 ; âge des données au dernier bloc : 2.07 s ; changements de frais LP observés (pools à frais dynamiques) : 10411
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16418 ; cycles déclenchés par événement : 1008 ; avance médiane sur le rafraîchissement multicall : 349 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,316.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 302 jetons, 19436 routes
- Par DEX : uniswap_v3 140, aerodrome 213, aerodrome_slipstream 125, pancakeswap_v3 31, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 337, par paires 0), mesurés 526, sous le plancher de 10000.0 $ : 2 → gardés 524 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2299.668664, 'cbBTC': 79491.484, 'AERO': 0.669155}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,240,619 | 2,316.819747 | 53104218 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,410,064 | 0.028952 | 53104218 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,157,746 | 0.028978 | 53104218 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,471,495 | 0.000013 | 53104218 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,794,511 | 94.042433 | 53104218 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,298,973 | 2,314.688959 | 53104218 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,151,814 | 1.499570 | 53104218 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,979,949 | 0.001647 | 53104218 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 549 | 5,437,898 | 2,315.275208 | 53104218 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,344,495 | 0.028959 | 53104218 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,447,867 | 2,315.390888 | 53104218 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,212,517 | 0.998980 | 53104218 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,802,911 | 34,740.707179 | 53104218 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,757,126 | 2,312.761109 | 53104218 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,188,072 | 0.028970 | 53104218 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,510,210 | 0.000013 | 53104218 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,480,595 | 94.127162 | 53104218 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,189,221 | 411.571444 | 53104218 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,120,453 | 1,210,308.594714 | 53104218 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,891,688 | 0.000013 | 53104218 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,886,128 | 0.000000 | 53104218 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,811,564 | 0.018334 | 53104218 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,712,813 | 0.000013 | 53104218 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,696,999 | 0.000013 | 53104218 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,554,357 | 0.000265 | 53104218 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,242 | 0.826241 | 53104218 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53104218 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,443,276 | 0.005574 | 53104218 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,411,211 | 3,471.586732 | 53104218 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,359,430 | 14,196.727894 | 53104218 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,230,966 | 0.000265 | 53104218 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/AERO | 10000 | 1,228,912 | 3,469.603693 | 53104218 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,228,076 | 2,314.783668 | 53104218 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,220,854 | 65.195116 | 53104218 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,157,188 | 0.000000 | 53104218 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,155,206 | 35,355,544.640689 | 53104218 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,127,666 | 1,107,480.567830 | 53104218 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,112,410 | 496,190.019054 | 53104218 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,077,502 | 19,718,037.189327 | 53104218 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,060,287 | 73,168.356862 | 53104218 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,059,596 | 55.787799 | 53104218 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,032,990 | 17.303228 | 53104218 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 965,018 | 0.040670 | 53104218 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 921,665 | 2,314.067319 | 53104218 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 908,352 | 2.308115 | 53104218 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 890,071 | 0.000553 | 53104218 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 875,036 | 17.185754 | 53104218 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 871,841 | 18.207841 | 53104218 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/MORPHO | 3000 | 871,814 | 1,154.146119 | 53104218 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 866,643 | 94.004998 | 53104218 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 844,215 | 2,314.518124 | 53104218 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 792,958 | 0.000008 | 53104218 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,934 | 0.056199 | 53104218 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 784,435 | 0.803142 | 53104218 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 774,573 | 1.105941 | 53104218 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 743,153 | 0.614213 | 53104218 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 730,984 | 4,742,071.176955 | 53104218 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 710,187 | 0.633640 | 53104218 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 704,106 | 136,269.637021 | 53104218 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 692,489 | 498,859.873566 | 53104218 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 8050 ; routes examinées : 156459800 ; candidats optimisés : 515600 ; net attendu > 0 : 310 ; dernier cycle 209.1 ms
- Rejets (moteur) : {'spread_below_threshold': 153383255, 'liquidity_below_min': 2378186, 'negative_expected_net': 515290, 'unquotable': 174494, 'borrow_bound_too_small': 8050, 'cycle_budget_exhausted': 215}
- Enregistrements de la session : 515600 ; net attendu > 0 : 310 ; simulés (eth_call de la vraie tx) : 14 (ok 12, échec 2) ; étiquettes ghost N+1 : 8/9 positives
- Décisions : {'REJECTED': 515600} ; motifs de rejet : {'below_safety_margin': 287, 'negative_expected_net': 515290, 'p_lower_below_threshold': 286, 'reliability_not_demonstrated': 24, 'sim_below_estimate': 3, 'simulation_failed': 2, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53098029 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.142261 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000024 WETH (0.0501 €) | — | 1.66 | 0.022 (n=94) | REJECTED | below_safety_margin(23566127176808<28452265992404), p_lower_below_threshold(0.02<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 327.219771 USDC | 0.059835 USDC | 0.000000 USDC | 0.005543 USDC | 0.054292 USDC (0.0499 €) | — | 1.66 | 0.022 (n=94) | REJECTED | below_safety_margin(54292<65443), p_lower_below_threshold(0.02<0.75) |
| 53098029 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.098833 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0198 €) | — | 0.94 | 0.129 (n=342) | REJECTED | below_safety_margin(9338811363951<19766565681607), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002899 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0198 €) | — | 0.93 | 0.129 (n=342) | REJECTED | below_safety_margin(27<57), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 192.423773 USDC | 0.028144 USDC | 0.000000 USDC | 0.006948 USDC | 0.021196 USDC (0.0195 €) | — | 1.10 | 0.129 (n=342) | REJECTED | below_safety_margin(21196<38484), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002446 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0191 €) | — | 1.06 | 0.129 (n=342) | REJECTED | below_safety_margin(26<48), p_lower_below_threshold(0.13<0.75) |
| 53098029 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.093531 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0189 €) | — | 0.95 | 0.129 (n=342) | REJECTED | below_safety_margin(8880679294217<18706197028796), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 208.572973 USDC | 0.027344 USDC | 0.000000 USDC | 0.006948 USDC | 0.020396 USDC (0.0188 €) | — | 0.98 | 0.129 (n=342) | REJECTED | below_safety_margin(20396<41714), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002900 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0183 €) | — | 0.86 | 0.129 (n=342) | REJECTED | below_safety_margin(25<57), p_lower_below_threshold(0.13<0.75) |
| 53098029 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.098785 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0182 €) | — | 0.87 | 0.129 (n=342) | REJECTED | below_safety_margin(8567298155534<19757042730904), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 195.851277 USDC | 0.026645 USDC | 0.000000 USDC | 0.006948 USDC | 0.019697 USDC (0.0181 €) | — | 1.01 | 0.129 (n=342) | REJECTED | below_safety_margin(19697<39170), p_lower_below_threshold(0.13<0.75) |
| 53098029 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.055574 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0162 €) | — | 1.37 | 0.129 (n=342) | REJECTED | below_safety_margin(7610299035162<11114801967723), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 128.153521 USDC | 0.024481 USDC | 0.000000 USDC | 0.006948 USDC | 0.017533 USDC (0.0161 €) | — | 1.37 | 0.129 (n=342) | REJECTED | below_safety_margin(17533<25630), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001395 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0147 €) | — | 1.43 | 0.180 (n=175) | REJECTED | below_safety_margin(20<27), p_lower_below_threshold(0.18<0.75) |
| 53098029 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001492 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0147 €) | — | 1.34 | 0.180 (n=175) | REJECTED | below_safety_margin(20<29), p_lower_below_threshold(0.18<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 138.355232 USDC | 0.022683 USDC | 0.000000 USDC | 0.006948 USDC | 0.015735 USDC (0.0145 €) | — | 1.14 | 0.180 (n=175) | REJECTED | below_safety_margin(15735<27671), p_lower_below_threshold(0.18<0.75) |
| 53098029 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.066994 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0142 €) | — | 1.00 | 0.180 (n=175) | REJECTED | below_safety_margin(6686863175120<13398720985300), p_lower_below_threshold(0.18<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 118.828226 USDC | 0.022342 USDC | 0.000000 USDC | 0.006948 USDC | 0.015394 USDC (0.0142 €) | — | 1.30 | 0.180 (n=175) | REJECTED | below_safety_margin(15394<23765), p_lower_below_threshold(0.18<0.75) |
| 53098029 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.050495 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0140 €) | — | 1.31 | 0.180 (n=175) | REJECTED | below_safety_margin(6603141486837<10099080547927), p_lower_below_threshold(0.18<0.75) |
| 53098029 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001438 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0139 €) | — | 1.32 | 0.129 (n=342) | REJECTED | below_safety_margin(19<28), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 118.828226 USDC | 0.022043 USDC | 0.000000 USDC | 0.006948 USDC | 0.015095 USDC (0.0139 €) | — | 1.27 | 0.129 (n=342) | REJECTED | below_safety_margin(15095<23765), p_lower_below_threshold(0.13<0.75) |
| 53098029 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.051267 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0138 €) | — | 1.27 | 0.129 (n=342) | REJECTED | below_safety_margin(6509871033140<10253483185164), p_lower_below_threshold(0.13<0.75) |
| 53099408 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001734 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0132 €) | — | 1.04 | 0.129 (n=342) | REJECTED | below_safety_margin(18<34), p_lower_below_threshold(0.13<0.75) |
| 53099408 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 142.144379 USDC | 0.021683 USDC | 0.000000 USDC | 0.007394 USDC | 0.014289 USDC (0.0131 €) | — | 1.01 | 0.129 (n=342) | REJECTED | below_safety_margin(14289<28428), p_lower_below_threshold(0.13<0.75) |
| 53099408 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.066210 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | — | 0.93 | 0.129 (n=342) | REJECTED | below_safety_margin(6133012101569<13241987517452), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2597 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
