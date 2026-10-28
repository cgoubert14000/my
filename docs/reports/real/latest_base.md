# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T06:50:31+00:00 ; durée 79.8 min ; blocs 53188044 → 53190440 (2381 vus)

## Connexion
- Requêtes RPC : 28541 ; erreurs : 20 ; latence p50/p95 : 214.0/1,201.2 ms
- Rafraîchissements d'état : 2382 ; âge des données au dernier bloc : 1.88 s ; changements de frais LP observés (pools à frais dynamiques) : 1580
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 15426 ; cycles déclenchés par événement : 2734 ; avance médiane sur le rafraîchissement multicall : 514 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,355.91 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 521 pools, 302 jetons, 18962 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 121, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 184 (rejetés 2) → 589 jetons ; pools candidats 3762 (énumérés 330, par paires 0), mesurés 523, sous le plancher de 10000.0 $ : 2 → gardés 521 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2356.459313, 'cbBTC': 80857.377983, 'AERO': 0.694089}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,352,594 | 2,355.910468 | 53190440 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,708,796 | 0.029088 | 53190440 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,647,961 | 0.000012 | 53190440 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,495,278 | 0.029105 | 53190440 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,445,710 | 2,351.525499 | 53190440 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,378,067 | 96.004993 | 53190440 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,067,707 | 0.001649 | 53190440 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,866,989 | 1.441952 | 53190440 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,746,125 | 0.029097 | 53190440 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,047,580 | 2,351.017852 | 53190440 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,483,843 | 2,351.059912 | 53190440 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,264,585 | 0.998869 | 53190440 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,777,393 | 36,409.904525 | 53190440 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,964,311 | 0.029116 | 53190440 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,531,915 | 95.967992 | 53190440 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,458,708 | 0.000012 | 53190440 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,150,546 | 1,216,715.810354 | 53190440 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,922,706 | 2,356.728402 | 53190440 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,843,282 | 0.019046 | 53190440 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,829,468 | 0.000000 | 53190440 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,799,079 | 395.703012 | 53190440 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,700,416 | 0.000012 | 53190440 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,693,634 | 0.000012 | 53190440 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,693,516 | 0.000012 | 53190440 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,517,326 | 0.005798 | 53190440 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,280 | 1.658893 | 53190440 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,878 | 0.826757 | 53190440 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,454,947 | 3,393.525972 | 53190440 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,399,871 | 13,592.804557 | 53190440 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,259,758 | 0.000268 | 53190440 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,242,492 | 2,351.585305 | 53190440 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,201,630 | 3,369.352247 | 53190440 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,194,235 | 68.133836 | 53190440 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,190,785 | 0.000267 | 53190440 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,167,849 | 1,067,137.705684 | 53190440 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,165,639 | 36,230,754.358062 | 53190440 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,143,597 | 0.000000 | 53190440 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,129,838 | 498,236.979071 | 53190440 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,083,567 | 72,227.288837 | 53190440 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,057,913 | 55.933504 | 53190440 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,054,661 | 21,141,464.036905 | 53190440 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,046,228 | 16.719242 | 53190440 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,002,845 | 0.040811 | 53190440 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 1,001,343 | 95.958364 | 53190440 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 945,544 | 2,342.370626 | 53190440 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 933,112 | 1,062.945040 | 53190440 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 910,567 | 0.000560 | 53190440 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 889,475 | 2.313703 | 53190440 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 883,054 | 17.846184 | 53190440 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 852,021 | 17.446284 | 53190440 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 850,847 | 2,356.292291 | 53190440 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 812,144 | 0.059269 | 53190440 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 797,652 | 0.803180 | 53190440 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 755,772 | 0.000009 | 53190440 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 755,449 | 0.630601 | 53190440 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 753,069 | 4,620,519.624771 | 53190440 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 713,946 | 137,102.136989 | 53190440 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 701,850 | 501,369.566106 | 53190440 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 681,427 | 0.584770 | 53190440 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 672,124 | 0.108220 | 53190440 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 5115 ; routes examinées : 96990630 ; candidats optimisés : 281435 ; net attendu > 0 : 79 ; dernier cycle 146.5 ms
- Rejets (moteur) : {'spread_below_threshold': 95669073, 'liquidity_below_min': 963202, 'negative_expected_net': 281356, 'borrow_bound_too_small': 76665, 'cycle_budget_exhausted': 255}
- Enregistrements de la session : 281435 ; net attendu > 0 : 79 ; simulés (eth_call de la vraie tx) : 14 (ok 0, échec 14) ; étiquettes ghost N+1 : 0/14 positives
- Décisions : {'REJECTED': 281435} ; motifs de rejet : {'below_safety_margin': 13, 'negative_expected_net': 281356, 'p_lower_below_threshold': 55, 'price_impact': 2, 'reliability_not_demonstrated': 24, 'simulation_failed': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53188413 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 139.105675 USDC | 6.970905 USDC | 0.000000 USDC | 0.004965 USDC | 6.965940 USDC (6.4087 €) | — | 500.77 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.029300 WETH | 0.000161 WETH | 0.000000 WETH | 0.000003 WETH | 0.000158 WETH (0.3435 €) | — | 54.09 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.029241 WETH | 0.000161 WETH | 0.000000 WETH | 0.000003 WETH | 0.000158 WETH (0.3430 €) | — | 54.13 | 0.000 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53190406 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 68.839715 USDC | 0.379669 USDC | 0.000000 USDC | 0.007081 USDC | 0.372588 USDC (0.3428 €) | — | 54.12 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53190406 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 68.639366 USDC | 0.379194 USDC | 0.000000 USDC | 0.007081 USDC | 0.372113 USDC (0.3423 €) | — | 54.21 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.029027 WETH | 0.000158 WETH | 0.000000 WETH | 0.000003 WETH | 0.000155 WETH (0.3369 €) | — | 53.55 | 0.000 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53190406 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 68.252205 USDC | 0.372548 USDC | 0.000000 USDC | 0.007081 USDC | 0.365467 USDC (0.3362 €) | — | 53.55 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.027508 WETH | 0.000143 WETH | 0.000000 WETH | 0.000003 WETH | 0.000140 WETH (0.3024 €) | — | 50.71 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 64.762850 USDC | 0.335283 USDC | 0.000000 USDC | 0.007081 USDC | 0.328202 USDC (0.3019 €) | — | 50.68 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.027467 WETH | 0.000142 WETH | 0.000000 WETH | 0.000003 WETH | 0.000139 WETH (0.3006 €) | — | 50.49 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53190406 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 64.477794 USDC | 0.333362 USDC | 0.000000 USDC | 0.007081 USDC | 0.326281 USDC (0.3002 €) | — | 50.60 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.026639 WETH | 0.000137 WETH | 0.000000 WETH | 0.000003 WETH | 0.000134 WETH (0.2908 €) | — | 50.37 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 62.571533 USDC | 0.323209 USDC | 0.000000 USDC | 0.007439 USDC | 0.315770 USDC (0.2905 €) | — | 50.47 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.024855 WETH | 0.000136 WETH | 0.000000 WETH | 0.000003 WETH | 0.000133 WETH (0.2881 €) | — | 53.48 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190406 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 58.576565 USDC | 0.320121 USDC | 0.000000 USDC | 0.007081 USDC | 0.313040 USDC (0.2880 €) | — | 53.44 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.003143 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1141 €) | — | 167.43 | 0.000 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.383964 USDC | 0.131180 USDC | 0.000000 USDC | 0.007438 USDC | 0.123742 USDC (0.1138 €) | — | 167.58 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.003145 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1135 €) | — | 166.40 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.003145 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1134 €) | — | 166.34 | 0.000 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.386026 USDC | 0.130499 USDC | 0.000000 USDC | 0.007438 USDC | 0.123061 USDC (0.1132 €) | — | 166.61 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53188189 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.386509 USDC | 0.130461 USDC | 0.000000 USDC | 0.007438 USDC | 0.123023 USDC (0.1132 €) | — | 166.55 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.003142 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1128 €) | — | 165.64 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.384617 USDC | 0.129822 USDC | 0.000000 USDC | 0.007438 USDC | 0.122384 USDC (0.1126 €) | — | 165.73 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.003131 WETH | 0.000054 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1092 €) | — | 160.87 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.357162 USDC | 0.126296 USDC | 0.000000 USDC | 0.007796 USDC | 0.118500 USDC (0.1090 €) | — | 161.07 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2906 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
