# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T01:52:18+00:00 ; durée 24.53 min ; blocs 53137556 → 53138294 (722 vus)

## Connexion
- Requêtes RPC : 9081 ; erreurs : 0 ; latence p50/p95 : 289.8/1,481.3 ms
- Rafraîchissements d'état : 722 ; âge des données au dernier bloc : 2.77 s ; changements de frais LP observés (pools à frais dynamiques) : 1375
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 10631 ; cycles déclenchés par événement : 637 ; avance médiane sur le rafraîchissement multicall : 699 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,323.63 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 305 jetons, 19446 routes
- Par DEX : uniswap_v3 143, aerodrome 212, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 3 → gardés 530 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2322.398057, 'cbBTC': 80000.770706, 'AERO': 0.673032}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,423,967 | 2,323.630469 | 53138295 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,118,473 | 0.029005 | 53138295 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,130,482 | 0.028948 | 53138295 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,464,662 | 0.000013 | 53138295 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,662,094 | 92.757121 | 53138295 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,345,387 | 2,319.064083 | 53138295 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,019,961 | 1.483414 | 53138295 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,976,709 | 0.001642 | 53138295 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,384,363 | 0.028997 | 53138295 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 922 | 5,256,611 | 2,318.408869 | 53138295 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,553,361 | 2,318.493376 | 53138295 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,216,432 | 0.999452 | 53138295 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,779,962 | 35,370.868022 | 53138295 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,364,843 | 2,323.908860 | 53138295 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,191,109 | 0.028965 | 53138295 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,508,401 | 92.741108 | 53138295 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 2,451,100 | 0.000013 | 53138295 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,121,372 | 1,216,380.983500 | 53138295 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,835,788 | 0.000000 | 53138295 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,833,081 | 0.018743 | 53138295 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,763,093 | 404.070301 | 53138295 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 370 | 1,689,739 | 0.000013 | 53138295 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,678,723 | 0.000013 | 53138295 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,665,646 | 0.000012 | 53138295 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,555,881 | 0.000266 | 53138295 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,513,923 | 0.005881 | 53138295 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,925 | 0.826518 | 53138295 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53138295 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,429,991 | 3,442.911918 | 53138295 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,372,059 | 13,942.913046 | 53138295 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,242,807 | 2,319.076911 | 53138295 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,237,910 | 0.000266 | 53138295 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53138295 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,207,778 | 3,444.389703 | 53138295 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | DRB/WETH | 10000 | 1,148,110 | 0.000000 | 53138295 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,142,098 | 36,863,515.097092 | 53138295 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,139,495 | 1,090,993.540534 | 53138295 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,109,045 | 497,980.334198 | 53138295 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,073,100 | 20,008,548.418872 | 53138295 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,071,874 | 72,011.867890 | 53138295 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,040,560 | 57.814540 | 53138295 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,031,541 | 17.373419 | 53138295 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,002,885 | 0.039968 | 53138295 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 952,473 | 2,317.651257 | 53138295 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 920,616 | 1,080.706290 | 53138295 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 908,295 | 2.309154 | 53138295 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 896,295 | 0.000558 | 53138295 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 879,695 | 17.950891 | 53138295 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 873,468 | 92.391195 | 53138295 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 859,977 | 17.193154 | 53138295 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 845,525 | 2,322.150404 | 53138295 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 796,818 | 0.000008 | 53138295 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,802 | 0.056901 | 53138295 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 786,723 | 0.803179 | 53138295 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,537 | 0.618070 | 53138295 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 735,451 | 4,712,749.408622 | 53138295 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 700,673 | 138,415.538833 | 53138295 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 699,631 | 0.615511 | 53138295 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 693,207 | 502,013.800513 | 53138295 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,884 | 0.109043 | 53138295 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 1358 ; routes examinées : 26407668 ; candidats optimisés : 72230 ; net attendu > 0 : 35 ; dernier cycle 280.5 ms
- Rejets (moteur) : {'spread_below_threshold': 25971353, 'liquidity_below_min': 335567, 'negative_expected_net': 72195, 'unquotable': 27160, 'borrow_bound_too_small': 1358}
- Enregistrements de la session : 72230 ; net attendu > 0 : 35 ; simulés (eth_call de la vraie tx) : 7 (ok 3, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 72230} ; motifs de rejet : {'below_safety_margin': 6, 'negative_expected_net': 72195, 'p_lower_below_threshold': 33, 'reliability_not_demonstrated': 2, 'simulation_failed': 4}

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
