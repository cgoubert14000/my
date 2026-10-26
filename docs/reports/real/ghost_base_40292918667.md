# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T14:02:43+00:00 ; durée 325.21 min ; blocs 53107248 → 53117003 (9438 vus)

## Connexion
- Requêtes RPC : 110380 ; erreurs : 90 ; latence p50/p95 : 291.7/1,367.5 ms
- Rafraîchissements d'état : 9438 ; âge des données au dernier bloc : 4.81 s ; changements de frais LP observés (pools à frais dynamiques) : 18359
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 23094 ; cycles déclenchés par événement : 1480 ; avance médiane sur le rafraîchissement multicall : 827 ms
- Gaz : base fee 0.005035 gwei ; prix ETH (pool le plus profond) : 2,299.66 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 527 pools, 302 jetons, 19574 routes
- Par DEX : uniswap_v3 142, aerodrome 213, aerodrome_slipstream 127, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 188 (rejetés 2) → 593 jetons ; pools candidats 3779 (énumérés 339, par paires 0), mesurés 529, sous le plancher de 10000.0 $ : 2 → gardés 527 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2317.899718, 'cbBTC': 80102.759686, 'AERO': 0.672129}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,892,070 | 2,299.662663 | 53117004 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,602,937 | 0.028900 | 53117004 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,087,510 | 0.028968 | 53117004 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,443,850 | 0.000013 | 53117004 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,732,693 | 93.928623 | 53117004 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,255,621 | 2,297.236817 | 53117004 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,141,182 | 1.490717 | 53117004 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,955,881 | 0.001654 | 53117004 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 639 | 5,311,944 | 2,296.697995 | 53117004 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,311,772 | 0.028891 | 53117004 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,426,923 | 2,296.747821 | 53117004 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,187,845 | 0.999591 | 53117004 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,770,933 | 34,811.038340 | 53117004 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,729,949 | 2,299.914622 | 53117004 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 3,181,496 | 0.028955 | 53117004 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,470,323 | 93.825538 | 53117004 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,465,674 | 0.000013 | 53117004 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,185,660 | 405.250388 | 53117004 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,104,815 | 1,210,234.968788 | 53117004 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,881,986 | 0.000013 | 53117004 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,871,405 | 0.000000 | 53117004 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,813,957 | 0.018407 | 53117004 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,706,888 | 0.000013 | 53117004 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,691,494 | 0.000013 | 53117004 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,540,612 | 0.000265 | 53117004 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,491,582 | 0.005850 | 53117004 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,944 | 0.826461 | 53117004 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53117004 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,412,966 | 3,433.032819 | 53117004 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,359,244 | 14,013.681043 | 53117004 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,221,876 | 0.000267 | 53117004 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,560 | 65.119740 | 53117004 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,212,519 | 3,440.523125 | 53117004 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,204,527 | 2,297.251510 | 53117004 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,158,352 | 0.000000 | 53117004 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,127,080 | 1,092,273.529269 | 53117004 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,123,728 | 37,447,732.306301 | 53117004 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,096,583 | 499,327.370307 | 53117004 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,060,163 | 20,057,666.453620 | 53117004 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,059,911 | 72,139.825087 | 53117004 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,055,456 | 56.226276 | 53117004 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,026,540 | 17.602485 | 53117004 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 963,134 | 0.040758 | 53117004 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 919,088 | 2,311.179744 | 53117004 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 899,093 | 2.308512 | 53117004 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 884,292 | 0.000554 | 53117004 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4555 | 877,478 | 18.022108 | 53117004 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 873,369 | 17.063383 | 53117004 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/MORPHO | 3000 | 872,838 | 1,142.044301 | 53117004 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 859,122 | 93.744772 | 53117004 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 841,105 | 2,299.725704 | 53117004 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 793,880 | 0.000008 | 53117004 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 792,377 | 0.056262 | 53117004 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 778,626 | 0.803142 | 53117004 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,262 | 0.612313 | 53117004 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 725,054 | 4,749,028.534212 | 53117004 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 695,691 | 137,535.922570 | 53117004 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 693,178 | 0.605012 | 53117004 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 685,113 | 497,521.639070 | 53117004 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,313 | 0.108931 | 53117004 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 10917 ; routes examinées : 213689358 ; candidats optimisés : 643568 ; net attendu > 0 : 459 ; dernier cycle 313.1 ms
- Rejets (moteur) : {'spread_below_threshold': 210060603, 'liquidity_below_min': 2753093, 'negative_expected_net': 643109, 'unquotable': 219900, 'borrow_bound_too_small': 10905, 'cycle_budget_exhausted': 1289}
- Enregistrements de la session : 643568 ; net attendu > 0 : 459 ; simulés (eth_call de la vraie tx) : 22 (ok 16, échec 6) ; étiquettes ghost N+1 : 2/17 positives
- Décisions : {'REJECTED': 643568} ; motifs de rejet : {'below_safety_margin': 357, 'negative_expected_net': 643109, 'p_lower_below_threshold': 423, 'price_impact': 1, 'reliability_not_demonstrated': 36, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 6, 'stale_data': 32}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53116285 | WETH→[uniswap_v3]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.145963 WETH | 0.000374 WETH | 0.000000 WETH | 0.000004 WETH | 0.000370 WETH (0.7870 €) | 0.000370 WETH | 25.38 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53116285 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.137659 WETH | 0.000351 WETH | 0.000000 WETH | 0.000004 WETH | 0.000347 WETH (0.7379 €) | 0.000347 WETH | 25.23 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53116285 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 238.211126 USDC | 0.451470 USDC | 0.000000 USDC | 0.008291 USDC | 0.443179 USDC (0.4077 €) | — | 18.60 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.002951 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4063 €) | — | 18.77 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 246.127642 USDC | 0.444785 USDC | 0.000000 USDC | 0.008291 USDC | 0.436494 USDC (0.4016 €) | — | 17.73 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.002938 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.4004 €) | — | 18.59 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 238.193084 USDC | 0.442249 USDC | 0.000000 USDC | 0.008291 USDC | 0.433958 USDC (0.3992 €) | — | 18.22 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 245.086905 USDC | 0.441624 USDC | 0.000000 USDC | 0.008291 USDC | 0.433333 USDC (0.3987 €) | — | 17.68 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002894 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3975 €) | — | 18.73 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.002951 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3975 €) | — | 18.37 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 227.845023 USDC | 0.408657 USDC | 0.000000 USDC | 0.008291 USDC | 0.400366 USDC (0.3683 €) | — | 17.57 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.002749 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3667 €) | — | 18.19 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 213.999081 USDC | 0.404490 USDC | 0.000000 USDC | 0.008707 USDC | 0.395783 USDC (0.3641 €) | — | 18.49 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002618 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3630 €) | — | 18.91 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | WETH→[aerodrome]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.064503 WETH | 0.000132 WETH | 0.000000 WETH | 0.000003 WETH | 0.000129 WETH (0.2737 €) | 0.000129 WETH | 19.97 | 0.039 (n=21) | REJECTED | reliability_not_demonstrated |
| 53116285 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.053301 WETH | 0.000123 WETH | 0.000000 WETH | 0.000003 WETH | 0.000120 WETH (0.2544 €) | — | 22.47 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53116285 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.051721 WETH | 0.000117 WETH | 0.000000 WETH | 0.000003 WETH | 0.000114 WETH (0.2420 €) | — | 22.02 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53116285 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.082709 WETH | 0.000112 WETH | 0.000000 WETH | 0.000004 WETH | 0.000108 WETH (0.2304 €) | — | 13.12 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002424 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2303 €) | — | 12.95 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.073288 WETH | 0.000096 WETH | 0.000000 WETH | 0.000004 WETH | 0.000092 WETH (0.1960 €) | — | 12.59 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002115 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1958 €) | — | 12.63 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002045 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1767 €) | — | 11.79 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.073175 WETH | 0.000087 WETH | 0.000000 WETH | 0.000004 WETH | 0.000083 WETH (0.1767 €) | — | 11.36 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.070000 WETH | 0.000082 WETH | 0.000000 WETH | 0.000004 WETH | 0.000078 WETH (0.1667 €) | — | 11.21 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.001989 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1665 €) | — | 11.41 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2624 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
