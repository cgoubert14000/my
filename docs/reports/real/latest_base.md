# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T04:16:27+00:00 ; durée 138.17 min ; blocs 53440871 → 53445017 (4080 vus)

## Connexion
- Requêtes RPC : 47865 ; erreurs : 33 ; latence p50/p95 : 246.9/1,362.9 ms
- Rafraîchissements d'état : 4081 ; âge des données au dernier bloc : 1.89 s ; changements de frais LP observés (pools à frais dynamiques) : 4910
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 42600 ; cycles déclenchés par événement : 5560 ; avance médiane sur le rafraîchissement multicall : 539 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,249.05 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 285 jetons, 18224 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 108, aerodrome 202, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 308, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2253.967555, 'cbBTC': 77042.637438, 'AERO': 0.602257}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,744,863 | 2,249.054625 | 53445017 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,134,800 | 0.029295 | 53445017 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,073,863 | 0.029314 | 53445017 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,959,911 | 0.000013 | 53445017 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,838,202 | 2,251.251694 | 53445017 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,552,577 | 104.621319 | 53445017 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,535,675 | 0.001569 | 53445017 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,343,951 | 1.666386 | 53445017 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,779,423 | 0.029307 | 53445017 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,081,686 | 2,252.031299 | 53445017 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,039,169 | 0.999884 | 53445017 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,900,624 | 2,252.043090 | 53445017 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,458,022 | 39,587.712636 | 53445017 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,683,322 | 0.029323 | 53445017 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,147,577 | 1,111,915.152196 | 53445017 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 2,029,780 | 0.000013 | 53445017 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2712 | 1,984,806 | 104.590955 | 53445017 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | XDP/USDC | 100 | 1,770,426 | 0.018386 | 53445017 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,663,357 | 0.000000 | 53445017 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,604,688 | 0.000013 | 53445017 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,241 | 1.436173 | 53445017 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,540,196 | 0.000013 | 53445017 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,527,151 | 442.907577 | 53445017 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,495,512 | 2,250.077775 | 53445017 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,608 | 0.822379 | 53445017 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,378,829 | 3,749.265815 | 53445017 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,348,107 | 2,252.715745 | 53445017 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,306,924 | 2,251.272299 | 53445017 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,276,781 | 0.004956 | 53445017 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,273,380 | 15,138.347915 | 53445017 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 1,257,270 | 0.000013 | 53445017 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,168,728 | 71.139858 | 53445017 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,098,359 | 37,672,885.672023 | 53445017 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,043,024 | 542,352.996735 | 53445017 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,007,117 | 0.000000 | 53445017 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 999,547 | 22,617,196.530373 | 53445017 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 978,537 | 20.186210 | 53445017 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 955,099 | 84,590.728183 | 53445017 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 921,997 | 2,257.234778 | 53445017 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 913,085 | 1,265,639.720811 | 53445017 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/VVV | 10000 | 911,082 | 104.470342 | 53445017 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 907,412 | 1,048.514751 | 53445017 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 877,252 | 81.348437 | 53445017 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 862,579 | 0.000551 | 53445017 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 856,500 | 0.046493 | 53445017 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 822,120 | 3,725.146765 | 53445017 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 813,309 | 20.342032 | 53445017 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 784,300 | 0.055029 | 53445017 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 763,481 | 0.798949 | 53445017 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 722,450 | 0.576298 | 53445017 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 715,749 | 0.000258 | 53445017 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 701,603 | 4,858,701.002076 | 53445017 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 661,432 | 145,950.492952 | 53445017 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 659,972 | 0.547712 | 53445017 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 651,798 | 2.338342 | 53445017 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 650,699 | 0.000008 | 53445017 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 641,359 | 544,522.815276 | 53445017 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 604,080 | 0.914848 | 53445017 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 586,302 | 0.086997 | 53445017 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 548,115 | 0.036903 | 53445017 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 9640 ; routes examinées : 175679360 ; candidats optimisés : 475553 ; net attendu > 0 : 348 ; dernier cycle 255.4 ms
- Rejets (moteur) : {'spread_below_threshold': 173016337, 'liquidity_below_min': 2148417, 'negative_expected_net': 475205, 'unquotable': 24716, 'borrow_bound_too_small': 9633, 'pool_quarantined': 4194, 'cycle_budget_exhausted': 510}
- Enregistrements de la session : 475553 ; net attendu > 0 : 348 ; simulés (eth_call de la vraie tx) : 13 (ok 0, échec 13) ; étiquettes ghost N+1 : 0/12 positives
- Décisions : {'REJECTED': 475553} ; motifs de rejet : {'below_safety_margin': 331, 'negative_expected_net': 475205, 'p_lower_below_threshold': 330, 'reliability_not_demonstrated': 18, 'simulation_failed': 13}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53444910 | WETH→[aerodrome]→MOR→[uniswap_v3]→WETH | 0.027022 WETH | 0.000160 WETH | 0.000000 WETH | 0.000002 WETH | 0.000158 WETH (0.3261 €) | — | 58.33 | 0.001 (n=15) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53443297 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,433.036354 USDC | 0.166334 USDC | 0.000000 USDC | 0.005390 USDC | 0.160944 USDC (0.1481 €) | — | 1.12 | 0.037 (n=182) | REJECTED | below_safety_margin(160944<286607), p_lower_below_threshold(0.04<0.75) |
| 53443297 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.637943 WETH | 0.000074 WETH | 0.000000 WETH | 0.000002 WETH | 0.000071 WETH (0.1479 €) | — | 1.12 | 0.037 (n=182) | REJECTED | below_safety_margin(71467813412258<127588534649033), p_lower_below_threshold(0.04<0.75) |
| 53442750 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 45.296202 USDC | 0.104960 USDC | 0.000000 USDC | 0.005062 USDC | 0.099898 USDC (0.0919 €) | — | 22.05 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53442864 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.011029 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0790 €) | — | 1.02 | 0.185 (n=839) | REJECTED | below_safety_margin(112<220), p_lower_below_threshold(0.19<0.75) |
| 53442864 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.401701 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0789 €) | — | 0.95 | 0.185 (n=839) | REJECTED | below_safety_margin(38094113610882<80340255564833), p_lower_below_threshold(0.19<0.75) |
| 53442864 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 920.782602 USDC | 0.092212 USDC | 0.000000 USDC | 0.006768 USDC | 0.085444 USDC (0.0786 €) | — | 0.93 | 0.185 (n=839) | REJECTED | below_safety_margin(85444<184156), p_lower_below_threshold(0.19<0.75) |
| 53442864 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.010076 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0748 €) | — | 1.05 | 0.185 (n=839) | REJECTED | below_safety_margin(106<201), p_lower_below_threshold(0.19<0.75) |
| 53442864 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.370100 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0745 €) | — | 0.97 | 0.185 (n=839) | REJECTED | below_safety_margin(35977094181516<74019905616955), p_lower_below_threshold(0.19<0.75) |
| 53442864 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 846.379396 USDC | 0.087446 USDC | 0.000000 USDC | 0.006768 USDC | 0.080678 USDC (0.0742 €) | — | 0.95 | 0.185 (n=839) | REJECTED | below_safety_margin(80678<169275), p_lower_below_threshold(0.19<0.75) |
| 53442864 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.008895 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0699 €) | — | 1.11 | 0.037 (n=181) | REJECTED | below_safety_margin(99<177), p_lower_below_threshold(0.04<0.75) |
| 53442864 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 702.804983 USDC | 0.080699 USDC | 0.000000 USDC | 0.005057 USDC | 0.075642 USDC (0.0696 €) | — | 1.08 | 0.037 (n=181) | REJECTED | below_safety_margin(75642<140560), p_lower_below_threshold(0.04<0.75) |
| 53441531 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.209769 WETH | 0.000036 WETH | 0.000000 WETH | 0.000002 WETH | 0.000033 WETH (0.0690 €) | — | 1.59 | 0.037 (n=181) | REJECTED | below_safety_margin(33265543026060<41953740710885), p_lower_below_threshold(0.04<0.75) |
| 53441531 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 472.119583 USDC | 0.079943 USDC | 0.000000 USDC | 0.005060 USDC | 0.074883 USDC (0.0689 €) | — | 1.59 | 0.037 (n=181) | REJECTED | below_safety_margin(74883<94423), p_lower_below_threshold(0.04<0.75) |
| 53441531 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.171973 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0463 €) | — | 1.30 | 0.026 (n=56) | REJECTED | below_safety_margin(22336456983429<34394668677693), p_lower_below_threshold(0.03<0.75) |
| 53441531 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 387.818691 USDC | 0.055336 USDC | 0.000000 USDC | 0.005060 USDC | 0.050276 USDC (0.0463 €) | — | 1.30 | 0.026 (n=56) | REJECTED | below_safety_margin(50276<77563), p_lower_below_threshold(0.03<0.75) |
| 53442864 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006417 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0423 €) | — | 0.93 | 0.037 (n=181) | REJECTED | below_safety_margin(60<128), p_lower_below_threshold(0.04<0.75) |
| 53442864 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 530.820876 USDC | 0.050816 USDC | 0.000000 USDC | 0.005057 USDC | 0.045759 USDC (0.0421 €) | — | 0.86 | 0.037 (n=181) | REJECTED | below_safety_margin(45759<106164), p_lower_below_threshold(0.04<0.75) |
| 53443064 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 788.452279 USDC | 0.050415 USDC | 0.000000 USDC | 0.005391 USDC | 0.045024 USDC (0.0414 €) | — | 0.57 | 0.037 (n=181) | REJECTED | below_safety_margin(45024<157690), p_lower_below_threshold(0.04<0.75) |
| 53443065 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 788.452279 USDC | 0.050415 USDC | 0.000000 USDC | 0.005391 USDC | 0.045024 USDC (0.0414 €) | — | 0.57 | 0.037 (n=181) | REJECTED | below_safety_margin(45024<157690), p_lower_below_threshold(0.04<0.75) |
| 53443064 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.350606 WETH | 0.000022 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0414 €) | — | 0.57 | 0.037 (n=181) | REJECTED | below_safety_margin(19996530617578<70121240411614), p_lower_below_threshold(0.04<0.75) |
| 53443065 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.350606 WETH | 0.000022 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0414 €) | — | 0.57 | 0.037 (n=181) | REJECTED | below_safety_margin(19996530617578<70121240411614), p_lower_below_threshold(0.04<0.75) |
| 53441962 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 477.566120 USDC | 0.050033 USDC | 0.000000 USDC | 0.005402 USDC | 0.044631 USDC (0.0411 €) | — | 0.93 | 0.037 (n=181) | REJECTED | below_safety_margin(44631<95513), p_lower_below_threshold(0.04<0.75) |
| 53441962 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006516 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0410 €) | — | 0.89 | 0.037 (n=181) | REJECTED | below_safety_margin(58<130), p_lower_below_threshold(0.04<0.75) |
| 53441531 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004073 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0290 €) | — | 1.01 | 0.186 (n=836) | REJECTED | below_safety_margin(41<81), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 4789 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
