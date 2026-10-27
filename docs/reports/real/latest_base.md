# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T02:07:31+00:00 ; durée 39.76 min ; blocs 53137556 → 53138751 (1165 vus)

## Connexion
- Requêtes RPC : 14638 ; erreurs : 0 ; latence p50/p95 : 327.0/1,375.7 ms
- Rafraîchissements d'état : 1166 ; âge des données au dernier bloc : 1.94 s ; changements de frais LP observés (pools à frais dynamiques) : 2196
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16762 ; cycles déclenchés par événement : 1015 ; avance médiane sur le rafraîchissement multicall : 723 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,322.24 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 305 jetons, 19446 routes
- Par DEX : uniswap_v3 143, aerodrome 212, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 3 → gardés 530 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2322.398057, 'cbBTC': 80000.770706, 'AERO': 0.673032}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,333,838 | 2,322.239953 | 53138751 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,109,469 | 0.028999 | 53138751 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,124,950 | 0.028948 | 53138751 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,462,821 | 0.000013 | 53138751 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,668,989 | 92.498817 | 53138751 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,341,761 | 2,316.419403 | 53138751 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,017,770 | 1.484270 | 53138751 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,973,965 | 0.001642 | 53138751 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,381,403 | 0.028995 | 53138751 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,253,896 | 2,317.085233 | 53138751 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,551,369 | 2,317.094543 | 53138751 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,214,707 | 0.999452 | 53138751 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,778,584 | 35,354.315773 | 53138751 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,363,836 | 2,322.503242 | 53138751 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,187,179 | 0.028965 | 53138751 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,509,668 | 92.466728 | 53138751 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,450,514 | 0.000013 | 53138751 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,120,102 | 1,216,380.983500 | 53138751 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,835,022 | 0.018780 | 53138751 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,834,689 | 0.000000 | 53138751 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,762,082 | 404.038276 | 53138751 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,689,351 | 0.000013 | 53138751 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,678,303 | 0.000013 | 53138751 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,665,270 | 0.000012 | 53138751 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,554,953 | 0.000266 | 53138751 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,511,636 | 0.005874 | 53138751 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,925 | 0.826518 | 53138751 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53138751 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,429,153 | 3,442.907857 | 53138751 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,371,439 | 13,940.617583 | 53138751 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,251,919 | 2,316.446036 | 53138751 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,237,170 | 0.000266 | 53138751 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53138751 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,207,071 | 3,444.389703 | 53138751 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | DRB/WETH | 10000 | 1,147,423 | 0.000000 | 53138751 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,141,415 | 36,863,515.097092 | 53138751 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,138,813 | 1,090,994.362113 | 53138751 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,108,398 | 497,959.542305 | 53138751 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,086,586 | 19,563,583.169593 | 53138751 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,071,313 | 72,001.065495 | 53138751 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,039,518 | 57.930569 | 53138751 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,032,557 | 17.323722 | 53138751 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,004,283 | 0.039892 | 53138751 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 952,222 | 2,317.651257 | 53138751 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 919,728 | 1,081.380675 | 53138751 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 907,752 | 2.309154 | 53138751 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 895,760 | 0.000558 | 53138751 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4570 | 877,941 | 18.009622 | 53138751 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 873,795 | 92.391211 | 53138751 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 859,462 | 17.193154 | 53138751 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 845,272 | 2,322.278861 | 53138751 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,572 | 0.057192 | 53138751 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 796,421 | 0.000008 | 53138751 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 786,252 | 0.803179 | 53138751 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,215 | 0.616933 | 53138751 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 736,087 | 4,698,998.951314 | 53138751 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 700,254 | 138,415.538833 | 53138751 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 699,989 | 0.616103 | 53138751 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 692,808 | 501,922.981369 | 53138751 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 673,469 | 0.108671 | 53138751 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 2180 ; routes examinées : 42392280 ; candidats optimisés : 116233 ; net attendu > 0 : 35 ; dernier cycle 188.5 ms
- Rejets (moteur) : {'spread_below_threshold': 41666684, 'liquidity_below_min': 563536, 'negative_expected_net': 116198, 'unquotable': 43580, 'borrow_bound_too_small': 2179}
- Enregistrements de la session : 116230 ; net attendu > 0 : 35 ; simulés (eth_call de la vraie tx) : 7 (ok 3, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 116230} ; motifs de rejet : {'below_safety_margin': 6, 'negative_expected_net': 116195, 'p_lower_below_threshold': 33, 'reliability_not_demonstrated': 2, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53138225 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015175 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0441 €) | 0.000021 WETH | 13.59 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015175 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0441 €) | — | 13.59 | 0.000 (n=58) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 35.137177 USDC | 0.055236 USDC | 0.000000 USDC | 0.007338 USDC | 0.047898 USDC (0.0441 €) | — | 13.63 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 35.137177 USDC | 0.055236 USDC | 0.000000 USDC | 0.007338 USDC | 0.047898 USDC (0.0441 €) | — | 13.63 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015350 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0433 €) | 0.000020 WETH | 13.19 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015350 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0433 €) | — | 13.19 | 0.000 (n=58) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.470699 USDC | 0.054007 USDC | 0.000000 USDC | 0.006985 USDC | 0.047022 USDC (0.0433 €) | — | 13.26 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.470699 USDC | 0.054007 USDC | 0.000000 USDC | 0.006985 USDC | 0.047022 USDC (0.0433 €) | — | 13.26 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.014411 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0418 €) | 0.000020 WETH | 13.58 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.014411 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0418 €) | — | 13.58 | 0.000 (n=58) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 33.276894 USDC | 0.052434 USDC | 0.000000 USDC | 0.006985 USDC | 0.045449 USDC (0.0418 €) | — | 13.66 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 33.276894 USDC | 0.052434 USDC | 0.000000 USDC | 0.006985 USDC | 0.045449 USDC (0.0418 €) | — | 13.66 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015201 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0418 €) | — | 12.86 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.137177 USDC | 0.052383 USDC | 0.000000 USDC | 0.006985 USDC | 0.045398 USDC (0.0418 €) | — | 12.92 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015225 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0417 €) | — | 12.82 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.090479 USDC | 0.052318 USDC | 0.000000 USDC | 0.006985 USDC | 0.045333 USDC (0.0417 €) | — | 12.92 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015161 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0416 €) | — | 12.84 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015161 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0416 €) | — | 12.84 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.098791 USDC | 0.052179 USDC | 0.000000 USDC | 0.006985 USDC | 0.045194 USDC (0.0416 €) | — | 12.88 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.098791 USDC | 0.052179 USDC | 0.000000 USDC | 0.006985 USDC | 0.045194 USDC (0.0416 €) | — | 12.88 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.014645 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0387 €) | — | 12.37 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.014645 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0387 €) | — | 12.37 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 33.965697 USDC | 0.049043 USDC | 0.000000 USDC | 0.006985 USDC | 0.042058 USDC (0.0387 €) | — | 12.38 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 33.965697 USDC | 0.049043 USDC | 0.000000 USDC | 0.006985 USDC | 0.042058 USDC (0.0387 €) | — | 12.38 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.011848 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0228 €) | — | 8.99 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2779 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
