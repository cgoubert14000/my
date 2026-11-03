# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T13:29:57+00:00 ; durée 18.33 min ; blocs 53461072 → 53461621 (541 vus)

## Connexion
- Requêtes RPC : 6426 ; erreurs : 0 ; latence p50/p95 : 234.0/1,452.8 ms
- Rafraîchissements d'état : 541 ; âge des données au dernier bloc : 7.81 s ; changements de frais LP observés (pools à frais dynamiques) : 895
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8602 ; cycles déclenchés par événement : 510 ; avance médiane sur le rafraîchissement multicall : 1,561 ms
- Gaz : base fee 0.005228 gwei ; prix ETH (pool le plus profond) : 2,285.40 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 286 jetons, 19214 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204 (quarantaine 1), pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 495, sous le plancher de 10000.0 $ : 3 → gardés 492 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2276.593928, 'cbBTC': 77247.513172, 'AERO': 0.617437}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 53461859

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,297,271 | 2,285.403407 | 53461621 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,475,546 | 0.029534 | 53461621 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,163,322 | 0.029459 | 53461621 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,006,036 | 0.000013 | 53461621 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,934,115 | 2,291.703093 | 53461621 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,698,610 | 103.970952 | 53461621 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,583,095 | 0.001568 | 53461621 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,417,328 | 1.587584 | 53461621 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,806,549 | 0.029545 | 53461621 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,206,507 | 2,291.942556 | 53461621 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,071,853 | 0.999818 | 53461621 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 1250 | 3,911,581 | 2,290.340180 | 53461621 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,512,510 | 39,619.269171 | 53461621 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2565 | 2,711,127 | 0.029481 | 53461621 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,166,088 | 1,128,607.075173 | 53461621 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2754 | 2,093,166 | 103.966834 | 53461621 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,811,416 | 0.000013 | 53461621 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,740,508 | 0.017842 | 53461621 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,679,380 | 0.000000 | 53461621 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,637,549 | 0.000013 | 53461621 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,397 | 0.000013 | 53461621 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,552,334 | 442.552623 | 53461621 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,546,556 | 1.442896 | 53461621 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,507,572 | 2,285.264896 | 53461621 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,645 | 0.821369 | 53461621 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,429,554 | 3,630.286898 | 53461621 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,343,182 | 2,284.747962 | 53461621 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,321,267 | 2,291.644396 | 53461621 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,317,937 | 0.005074 | 53461621 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,288,624 | 15,000.506929 | 53461621 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 396 | 1,235,600 | 0.000013 | 53461621 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,164,322 | 71.679251 | 53461621 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,123,789 | 36,906,634.524476 | 53461621 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,059,703 | 542,613.811813 | 53461621 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,486 | 22,327,199.391956 | 53461621 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,018,383 | 0.000000 | 53461621 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,001,046 | 18.893604 | 53461621 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 959,718 | 86,508.410967 | 53461621 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 936,146 | 104.707174 | 53461621 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/WELL | 10000 | 932,614 | 1,252,721.609265 | 53461621 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 928,934 | 2,269.320166 | 53461621 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 919,411 | 1,083.041896 | 53461621 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 911,918 | 75.281212 | 53461621 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 882,067 | 0.000558 | 53461621 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 880,143 | 0.045379 | 53461621 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 848,763 | 3,658.275507 | 53461621 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 821,154 | 20.059249 | 53461621 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,060 | 0.056628 | 53461621 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 775,735 | 0.799125 | 53461621 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 729,248 | 0.587121 | 53461621 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 725,602 | 0.000257 | 53461621 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 717,201 | 4,801,658.325979 | 53461621 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 672,174 | 0.000008 | 53461621 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 668,681 | 147,467.920574 | 53461621 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 661,666 | 2.341840 | 53461621 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 655,607 | 0.540798 | 53461621 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 651,580 | 542,649.794804 | 53461621 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 613,922 | 0.914615 | 53461621 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 591,368 | 0.088107 | 53461621 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 571,590 | 0.039296 | 53461621 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 1050 ; routes examinées : 20174700 ; candidats optimisés : 61139 ; net attendu > 0 : 61 ; dernier cycle 1201.8 ms
- Rejets (moteur) : {'spread_below_threshold': 19821173, 'liquidity_below_min': 284631, 'negative_expected_net': 61078, 'pool_quarantined': 2730, 'unquotable': 2221, 'cycle_budget_exhausted': 1756, 'borrow_bound_too_small': 1050}
- Enregistrements de la session : 61139 ; net attendu > 0 : 61 ; simulés (eth_call de la vraie tx) : 8 (ok 0, échec 8) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 61139} ; motifs de rejet : {'below_safety_margin': 53, 'negative_expected_net': 61078, 'p_lower_below_threshold': 61, 'price_impact': 5, 'simulation_failed': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53461592 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 863.053285 USDC | 0.058737 USDC | 0.000000 USDC | 0.005490 USDC | 0.053247 USDC (0.0490 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(53247<172610), p_lower_below_threshold(0.03<0.75) |
| 53461593 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 863.053285 USDC | 0.058737 USDC | 0.000000 USDC | 0.005490 USDC | 0.053247 USDC (0.0490 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(53247<172610), p_lower_below_threshold(0.03<0.75) |
| 53461592 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.378818 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0488 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(23308414488570<75763685316246), p_lower_below_threshold(0.03<0.75) |
| 53461593 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.378818 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0488 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(23308414488570<75763685316246), p_lower_below_threshold(0.03<0.75) |
| 53461592 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 264.521146 USDC | 0.024946 USDC | 0.000000 USDC | 0.005143 USDC | 0.019803 USDC (0.0182 €) | — | 0.75 | 0.025 (n=58) | REJECTED | below_safety_margin(19803<52904), p_lower_below_threshold(0.02<0.75) |
| 53461593 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 264.521146 USDC | 0.024946 USDC | 0.000000 USDC | 0.005143 USDC | 0.019803 USDC (0.0182 €) | — | 0.75 | 0.025 (n=58) | REJECTED | below_safety_margin(19803<52904), p_lower_below_threshold(0.02<0.75) |
| 53461592 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.115652 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0181 €) | — | 0.75 | 0.025 (n=58) | REJECTED | below_safety_margin(8664892176091<23130374141157), p_lower_below_threshold(0.02<0.75) |
| 53461593 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.115652 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0181 €) | — | 0.75 | 0.025 (n=58) | REJECTED | below_safety_margin(8664892176091<23130374141157), p_lower_below_threshold(0.02<0.75) |
| 53461200 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.115048 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0108 €) | — | 0.45 | 0.187 (n=842) | REJECTED | below_safety_margin(5146246836645<23009588869935), p_lower_below_threshold(0.19<0.75) |
| 53461200 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002834 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0107 €) | — | 0.53 | 0.187 (n=842) | REJECTED | below_safety_margin(15<56), p_lower_below_threshold(0.19<0.75) |
| 53461200 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 259.955727 USDC | 0.018769 USDC | 0.000000 USDC | 0.007203 USDC | 0.011566 USDC (0.0106 €) | — | 0.44 | 0.187 (n=842) | REJECTED | below_safety_margin(11566<51991), p_lower_below_threshold(0.19<0.75) |
| 53461516 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 53.941949 USDC | 0.016424 USDC | 0.000000 USDC | 0.005130 USDC | 0.011294 USDC (0.0104 €) | — | 2.09 | 0.026 (n=56) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53461516 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.023898 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0104 €) | — | 2.07 | 0.026 (n=56) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53461516 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 51.910745 USDC | 0.014555 USDC | 0.000000 USDC | 0.005130 USDC | 0.009425 USDC (0.0087 €) | — | 1.82 | 0.026 (n=56) | REJECTED | below_safety_margin(9425<10382), p_lower_below_threshold(0.03<0.75) |
| 53461516 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.022968 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0087 €) | — | 1.80 | 0.026 (n=56) | REJECTED | below_safety_margin(4134729814390<4593529188301), p_lower_below_threshold(0.03<0.75) |
| 53461516 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.023676 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0081 €) | — | 1.63 | 0.187 (n=842) | REJECTED | below_safety_margin(3856343035207<4735199363378), p_lower_below_threshold(0.19<0.75) |
| 53461516 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 50.298820 USDC | 0.013730 USDC | 0.000000 USDC | 0.005130 USDC | 0.008600 USDC (0.0079 €) | — | 1.71 | 0.035 (n=190) | REJECTED | below_safety_margin(8600<10059), p_lower_below_threshold(0.04<0.75) |
| 53461516 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.022331 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0079 €) | — | 1.69 | 0.035 (n=190) | REJECTED | below_safety_margin(3772350983885<4466188153712), p_lower_below_threshold(0.04<0.75) |
| 53461516 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 51.985672 USDC | 0.015433 USDC | 0.000000 USDC | 0.006864 USDC | 0.008569 USDC (0.0079 €) | — | 1.65 | 0.187 (n=842) | REJECTED | below_safety_margin(8569<10397), p_lower_below_threshold(0.19<0.75) |
| 53461516 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000618 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0078 €) | — | 1.78 | 0.187 (n=842) | REJECTED | below_safety_margin(11<12), p_lower_below_threshold(0.19<0.75) |
| 53461516 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.000651 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0078 €) | — | 1.69 | 0.187 (n=842) | REJECTED | below_safety_margin(11<13), p_lower_below_threshold(0.19<0.75) |
| 53461516 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 49.487948 USDC | 0.013352 USDC | 0.000000 USDC | 0.005130 USDC | 0.008222 USDC (0.0076 €) | — | 1.66 | 0.035 (n=190) | REJECTED | below_safety_margin(8222<9897), p_lower_below_threshold(0.04<0.75) |
| 53461516 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.021640 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0076 €) | — | 1.67 | 0.035 (n=190) | REJECTED | below_safety_margin(3605834800145<4327980806728), p_lower_below_threshold(0.04<0.75) |
| 53461516 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.023096 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0074 €) | — | 1.53 | 0.187 (n=842) | REJECTED | below_safety_margin(3544515659324<4619100132081), p_lower_below_threshold(0.19<0.75) |
| 53461516 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 57.304011 USDC | 0.014510 USDC | 0.000000 USDC | 0.006864 USDC | 0.007646 USDC (0.0070 €) | — | 1.33 | 0.187 (n=842) | REJECTED | below_safety_margin(7646<11460), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 4841 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.163 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
