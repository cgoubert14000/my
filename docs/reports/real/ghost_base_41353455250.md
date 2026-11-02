# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T01:25:37+00:00 ; durée 215.38 min ; blocs 53390229 → 53396687 (6236 vus)

## Connexion
- Requêtes RPC : 73000 ; erreurs : 0 ; latence p50/p95 : 236.1/1,561.6 ms
- Rafraîchissements d'état : 6236 ; âge des données au dernier bloc : 6.02 s ; changements de frais LP observés (pools à frais dynamiques) : 9244
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 79172 ; cycles déclenchés par événement : 7978 ; avance médiane sur le rafraîchissement multicall : 636 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,287.14 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 495 pools, 288 jetons, 18180 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 111, aerodrome 203 (quarantaine 2), pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3720 (énumérés 312, par paires 0), mesurés 498, sous le plancher de 10000.0 $ : 3 → gardés 495 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2258.829928, 'cbBTC': 77854.490121, 'AERO': 0.63182}
- Pools en quarantaine : 2 — aerodrome:WETH/OVER@0xB452f8: simulation failed ×5 (model/chain mismatch) — until block 53396843; aerodrome:OVER/USDC@0x889339: simulation failed ×5 (model/chain mismatch) — until block 53396843

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,567,801 | 2,288.614963 | 53396688 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,316,759 | 0.029214 | 53396688 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,359,356 | 0.000013 | 53396688 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,228,827 | 0.029144 | 53396688 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,955,396 | 2,294.366225 | 53396688 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,876,656 | 99.487911 | 53396688 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,703,196 | 0.001586 | 53396688 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,529,503 | 1.588094 | 53396688 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,209,838 | 0.029225 | 53396688 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,123,787 | 0.998855 | 53396688 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 907 | 4,086,034 | 2,294.041406 | 53396688 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,985,256 | 2,294.670399 | 53396688 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,580,487 | 38,188.100749 | 53396688 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 2,719,916 | 0.029158 | 53396688 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,397,398 | 99.469147 | 53396688 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 2,136,254 | 0.000013 | 53396688 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,113,017 | 1,187,813.955255 | 53396688 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,764,350 | 0.018211 | 53396688 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,692,298 | 0.000000 | 53396688 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,633,847 | 0.000013 | 53396688 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,591,161 | 0.000013 | 53396688 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,566,445 | 430.204396 | 53396688 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,514,647 | 2,288.754988 | 53396688 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53396688 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,505 | 0.825116 | 53396688 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,422,655 | 3,626.434012 | 53396688 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,387,821 | 2,287.644305 | 53396688 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,347,566 | 2,294.860335 | 53396688 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,344,823 | 0.005194 | 53396688 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,313,668 | 14,728.739407 | 53396688 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 1,308,612 | 0.000013 | 53396688 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,013 | 71.105164 | 53396688 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,128,047 | 36,445,536.464635 | 53396688 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,075,708 | 521,133.791981 | 53396688 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,061,387 | 0.000000 | 53396688 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,021,006 | 22,413,300.155229 | 53396688 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,000,932 | 98.863484 | 53396688 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 991,459 | 19.423449 | 53396688 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 988,879 | 81,658.700554 | 53396688 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 961,201 | 1,181,106.864815 | 53396688 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 930,572 | 1,020.826590 | 53396688 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 926,597 | 2,272.618031 | 53396688 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 920,565 | 0.043490 | 53396688 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 905,599 | 76.335080 | 53396688 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 871,680 | 0.000544 | 53396688 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 868,529 | 3,609.545818 | 53396688 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 834,085 | 19.582290 | 53396688 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,639 | 0.060575 | 53396688 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 774,994 | 0.801881 | 53396688 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 735,186 | 0.000261 | 53396688 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 732,694 | 0.594033 | 53396688 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 722,516 | 4,736,017.927090 | 53396688 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 698,149 | 135,435.803649 | 53396688 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 687,754 | 0.000008 | 53396688 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 675,175 | 0.572026 | 53396688 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2108 | 665,944 | 522,751.653680 | 53396688 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 665,686 | 2.342041 | 53396688 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 614,057 | 0.915601 | 53396688 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 610,323 | 0.092508 | 53396688 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 568,609 | 0.039088 | 53396688 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 14213 ; routes examinées : 258392340 ; candidats optimisés : 1091906 ; net attendu > 0 : 3039 ; dernier cycle 1203.9 ms
- Rejets (moteur) : {'spread_below_threshold': 253952727, 'liquidity_below_min': 3278167, 'negative_expected_net': 1088867, 'unquotable': 38316, 'borrow_bound_too_small': 14213, 'pool_quarantined': 11032, 'cycle_budget_exhausted': 5979}
- Enregistrements de la session : 1091906 ; net attendu > 0 : 3039 ; simulés (eth_call de la vraie tx) : 147 (ok 82, échec 65) ; étiquettes ghost N+1 : 39/88 positives
- Décisions : {'REJECTED': 1091906} ; motifs de rejet : {'below_safety_margin': 2430, 'negative_expected_net': 1088867, 'p_lower_below_threshold': 2838, 'reliability_not_demonstrated': 201, 'sim_below_estimate': 36, 'simulated_net_nonpositive': 14, 'simulation_failed': 65, 'stale_data': 258}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53395035 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,840.889144 USDC | 0.313870 USDC | 0.000000 USDC | 0.007539 USDC | 0.306331 USDC (0.2818 €) | — | 1.66 | 0.136 (n=720) | REJECTED | below_safety_margin(306331<368177), p_lower_below_threshold(0.14<0.75) |
| 53395035 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.823633 WETH | 0.000138 WETH | 0.000000 WETH | 0.000003 WETH | 0.000135 WETH (0.2818 €) | — | 1.64 | 0.136 (n=720) | REJECTED | below_safety_margin(134731119037051<164726576130861), p_lower_below_threshold(0.14<0.75) |
| 53395035 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.022556 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2816 €) | — | 1.74 | 0.136 (n=720) | REJECTED | below_safety_margin(392<451), p_lower_below_threshold(0.14<0.75) |
| 53395035 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.648371 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1810 €) | — | 1.34 | 0.000 (n=18) | REJECTED | below_safety_margin(86567293990276<129674278175252), reliability_not_demonstrated |
| 53395035 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.018533 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1810 €) | — | 1.36 | 0.000 (n=18) | REJECTED | below_safety_margin(252<370), reliability_not_demonstrated |
| 53395035 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,537.566926 USDC | 0.204336 USDC | 0.000000 USDC | 0.007884 USDC | 0.196452 USDC (0.1807 €) | — | 1.28 | 0.000 (n=18) | REJECTED | below_safety_margin(196452<307513), reliability_not_demonstrated |
| 53395035 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 1,040.238246 USDC | 0.147274 USDC | 0.000000 USDC | 0.007193 USDC | 0.140081 USDC (0.1289 €) | — | 1.35 | 0.136 (n=720) | REJECTED | below_safety_margin(140081<208047), p_lower_below_threshold(0.14<0.75) |
| 53395035 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.012865 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1286 €) | — | 1.39 | 0.136 (n=720) | REJECTED | below_safety_margin(179<257), p_lower_below_threshold(0.14<0.75) |
| 53395035 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.489258 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1284 €) | — | 1.26 | 0.136 (n=720) | REJECTED | below_safety_margin(61413040729236<97851507271082), p_lower_below_threshold(0.14<0.75) |
| 53390954 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 599.027739 USDC | 0.135348 USDC | 0.000000 USDC | 0.005071 USDC | 0.130277 USDC (0.1199 €) | — | 2.17 | 0.042 (n=158) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53390954 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.265345 WETH | 0.000060 WETH | 0.000000 WETH | 0.000002 WETH | 0.000058 WETH (0.1198 €) | — | 2.17 | 0.042 (n=158) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53396379 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.011736 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0942 €) | — | 1.12 | 0.000 (n=18) | REJECTED | below_safety_margin(131<234), reliability_not_demonstrated |
| 53396379 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.011736 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0942 €) | — | 1.12 | 0.000 (n=18) | REJECTED | below_safety_margin(131<234), reliability_not_demonstrated |
| 53396379 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 930.118817 USDC | 0.109283 USDC | 0.000000 USDC | 0.006858 USDC | 0.102425 USDC (0.0942 €) | — | 1.10 | 0.000 (n=18) | REJECTED | below_safety_margin(102425<186023), reliability_not_demonstrated |
| 53396379 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 930.118817 USDC | 0.109283 USDC | 0.000000 USDC | 0.006858 USDC | 0.102425 USDC (0.0942 €) | — | 1.10 | 0.000 (n=18) | REJECTED | below_safety_margin(102425<186023), reliability_not_demonstrated |
| 53396379 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.403704 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0939 €) | — | 1.11 | 0.000 (n=18) | REJECTED | below_safety_margin(44765819386964<80740763926623), reliability_not_demonstrated |
| 53396379 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.403704 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0939 €) | — | 1.11 | 0.000 (n=18) | REJECTED | below_safety_margin(44765819386964<80740763926623), reliability_not_demonstrated |
| 53390786 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.013685 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0937 €) | — | 0.96 | 0.000 (n=18) | REJECTED | below_safety_margin(131<273), reliability_not_demonstrated |
| 53390786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,064.663235 USDC | 0.108835 USDC | 0.000000 USDC | 0.007130 USDC | 0.101705 USDC (0.0936 €) | — | 0.96 | 0.000 (n=18) | REJECTED | below_safety_margin(101705<212932), reliability_not_demonstrated |
| 53390786 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.480798 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0934 €) | — | 0.94 | 0.000 (n=18) | REJECTED | below_safety_margin(44960344685998<96159606306820), reliability_not_demonstrated |
| 53393516 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 967.037137 USDC | 0.104776 USDC | 0.000000 USDC | 0.007161 USDC | 0.097615 USDC (0.0898 €) | — | 1.01 | 0.000 (n=18) | REJECTED | below_safety_margin(97615<193407), reliability_not_demonstrated |
| 53393517 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 967.037137 USDC | 0.104776 USDC | 0.000000 USDC | 0.007161 USDC | 0.097615 USDC (0.0898 €) | — | 1.01 | 0.000 (n=18) | REJECTED | below_safety_margin(97615<193407), reliability_not_demonstrated |
| 53393516 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.449739 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0896 €) | — | 0.96 | 0.000 (n=18) | REJECTED | below_safety_margin(42956745829601<89947709092873), reliability_not_demonstrated |
| 53393517 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.449739 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0896 €) | — | 0.96 | 0.000 (n=18) | REJECTED | below_safety_margin(42956745829601<89947709092873), reliability_not_demonstrated |
| 53393516 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011568 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0891 €) | — | 1.07 | 0.000 (n=18) | REJECTED | below_safety_margin(124<231), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4276 ; taux observé 0.133 ; borne inférieure crédible (0.9) 0.126 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
