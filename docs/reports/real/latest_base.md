# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T02:40:58+00:00 ; durée 42.69 min ; blocs 53440871 → 53442154 (1264 vus)

## Connexion
- Requêtes RPC : 14859 ; erreurs : 0 ; latence p50/p95 : 391.5/1,342.2 ms
- Rafraîchissements d'état : 1265 ; âge des données au dernier bloc : 2.18 s ; changements de frais LP observés (pools à frais dynamiques) : 1446
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12653 ; cycles déclenchés par événement : 1712 ; avance médiane sur le rafraîchissement multicall : 813 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,255.08 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 285 jetons, 18224 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 108, aerodrome 202, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 308, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2253.967555, 'cbBTC': 77042.637438, 'AERO': 0.602257}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,000,971 | 2,255.081196 | 53442154 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,160,001 | 0.029375 | 53442154 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,084,283 | 0.029314 | 53442154 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,959,364 | 0.000013 | 53442154 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,854,832 | 2,257.362039 | 53442154 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,578,530 | 104.463586 | 53442154 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,534,120 | 0.001568 | 53442154 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,355,175 | 1.660446 | 53442154 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,764,905 | 0.029369 | 53442154 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,112,801 | 2,257.082240 | 53442154 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,038,807 | 0.999897 | 53442154 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,909,796 | 2,256.968533 | 53442154 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,456,237 | 39,841.273500 | 53442154 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,694,030 | 0.029323 | 53442154 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,142,017 | 1,123,693.245522 | 53442154 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 2,029,630 | 0.000013 | 53442154 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2703 | 1,991,854 | 104.417895 | 53442154 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | XDP/USDC | 100 | 1,773,051 | 0.018433 | 53442154 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,667,916 | 0.000000 | 53442154 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,604,279 | 0.000013 | 53442154 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,241 | 1.436173 | 53442154 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,539,783 | 0.000013 | 53442154 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,529,780 | 444.280645 | 53442154 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,497,574 | 2,254.847587 | 53442154 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,608 | 0.822379 | 53442154 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,384,571 | 3,754.408383 | 53442154 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,349,913 | 2,259.714040 | 53442154 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,310,066 | 2,257.502763 | 53442154 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,289,468 | 0.004999 | 53442154 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,273,095 | 15,136.676171 | 53442154 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 1,257,132 | 0.000013 | 53442154 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,168,739 | 71.138543 | 53442154 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,100,984 | 37,707,062.323865 | 53442154 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,045,807 | 542,377.675375 | 53442154 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,007,263 | 0.000000 | 53442154 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,002,236 | 22,617,196.530373 | 53442154 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 979,784 | 20.110164 | 53442154 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 956,181 | 84,852.216548 | 53442154 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 922,981 | 2,257.234891 | 53442154 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 913,769 | 1,270,527.305738 | 53442154 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/VVV | 10000 | 912,426 | 104.430996 | 53442154 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 910,766 | 1,043.662494 | 53442154 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 876,938 | 81.406594 | 53442154 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,004 | 0.000549 | 53442154 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 861,807 | 0.046192 | 53442154 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 825,000 | 3,725.146765 | 53442154 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 814,339 | 20.304054 | 53442154 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,211 | 0.056053 | 53442154 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,527 | 0.798949 | 53442154 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,119 | 0.578214 | 53442154 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 717,667 | 0.000258 | 53442154 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 701,177 | 4,890,670.933261 | 53442154 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 663,316 | 145,901.194426 | 53442154 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 659,974 | 0.547712 | 53442154 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 653,544 | 2.338342 | 53442154 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 652,143 | 0.000008 | 53442154 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 643,061 | 545,898.357520 | 53442154 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 605,699 | 0.914848 | 53442154 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 589,441 | 0.087700 | 53442154 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 549,146 | 0.037010 | 53442154 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 2976 ; routes examinées : 54234624 ; candidats optimisés : 140474 ; net attendu > 0 : 94 ; dernier cycle 403.0 ms
- Rejets (moteur) : {'spread_below_threshold': 53362120, 'liquidity_below_min': 721844, 'negative_expected_net': 140380, 'unquotable': 7042, 'borrow_bound_too_small': 2973, 'cycle_budget_exhausted': 171}
- Enregistrements de la session : 140474 ; net attendu > 0 : 94 ; simulés (eth_call de la vraie tx) : 3 (ok 0, échec 3) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 140474} ; motifs de rejet : {'below_safety_margin': 91, 'negative_expected_net': 140380, 'p_lower_below_threshold': 88, 'reliability_not_demonstrated': 6, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53441531 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.209769 WETH | 0.000036 WETH | 0.000000 WETH | 0.000002 WETH | 0.000033 WETH (0.0690 €) | — | 1.59 | 0.037 (n=181) | REJECTED | below_safety_margin(33265543026060<41953740710885), p_lower_below_threshold(0.04<0.75) |
| 53441531 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 472.119583 USDC | 0.079943 USDC | 0.000000 USDC | 0.005060 USDC | 0.074883 USDC (0.0689 €) | — | 1.59 | 0.037 (n=181) | REJECTED | below_safety_margin(74883<94423), p_lower_below_threshold(0.04<0.75) |
| 53441531 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.171973 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0463 €) | — | 1.30 | 0.026 (n=56) | REJECTED | below_safety_margin(22336456983429<34394668677693), p_lower_below_threshold(0.03<0.75) |
| 53441531 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 387.818691 USDC | 0.055336 USDC | 0.000000 USDC | 0.005060 USDC | 0.050276 USDC (0.0463 €) | — | 1.30 | 0.026 (n=56) | REJECTED | below_safety_margin(50276<77563), p_lower_below_threshold(0.03<0.75) |
| 53441962 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 477.566120 USDC | 0.050033 USDC | 0.000000 USDC | 0.005402 USDC | 0.044631 USDC (0.0411 €) | — | 0.93 | 0.037 (n=181) | REJECTED | below_safety_margin(44631<95513), p_lower_below_threshold(0.04<0.75) |
| 53441962 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006516 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0410 €) | — | 0.89 | 0.037 (n=181) | REJECTED | below_safety_margin(58<130), p_lower_below_threshold(0.04<0.75) |
| 53441531 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004073 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0290 €) | — | 1.01 | 0.186 (n=836) | REJECTED | below_safety_margin(41<81), p_lower_below_threshold(0.19<0.75) |
| 53441531 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 313.655980 USDC | 0.037662 USDC | 0.000000 USDC | 0.006772 USDC | 0.030890 USDC (0.0284 €) | — | 0.98 | 0.186 (n=836) | REJECTED | below_safety_margin(30890<62731), p_lower_below_threshold(0.19<0.75) |
| 53441531 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.125978 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0283 €) | — | 1.08 | 0.186 (n=836) | REJECTED | below_safety_margin(13655291199281<25195668185131), p_lower_below_threshold(0.19<0.75) |
| 53441628 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.104580 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0141 €) | — | 0.65 | 0.026 (n=56) | REJECTED | below_safety_margin(6806094089813<20915932793551), p_lower_below_threshold(0.03<0.75) |
| 53441628 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.104580 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0141 €) | — | 0.65 | 0.026 (n=56) | REJECTED | below_safety_margin(6806094089813<20915932793551), p_lower_below_threshold(0.03<0.75) |
| 53441628 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 233.843885 USDC | 0.020397 USDC | 0.000000 USDC | 0.005060 USDC | 0.015337 USDC (0.0141 €) | — | 0.66 | 0.026 (n=56) | REJECTED | below_safety_margin(15337<46768), p_lower_below_threshold(0.03<0.75) |
| 53441628 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 233.843885 USDC | 0.020397 USDC | 0.000000 USDC | 0.005060 USDC | 0.015337 USDC (0.0141 €) | — | 0.66 | 0.026 (n=56) | REJECTED | below_safety_margin(15337<46768), p_lower_below_threshold(0.03<0.75) |
| 53441628 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.101416 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0124 €) | — | 0.59 | 0.037 (n=181) | REJECTED | below_safety_margin(5965313528361<20283117094792), p_lower_below_threshold(0.04<0.75) |
| 53441628 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.101416 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0124 €) | — | 0.59 | 0.037 (n=181) | REJECTED | below_safety_margin(5965313528361<20283117094792), p_lower_below_threshold(0.04<0.75) |
| 53441628 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 228.327631 USDC | 0.018845 USDC | 0.000000 USDC | 0.005402 USDC | 0.013443 USDC (0.0124 €) | — | 0.59 | 0.037 (n=181) | REJECTED | below_safety_margin(13443<45665), p_lower_below_threshold(0.04<0.75) |
| 53441628 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 228.327631 USDC | 0.018845 USDC | 0.000000 USDC | 0.005402 USDC | 0.013443 USDC (0.0124 €) | — | 0.59 | 0.037 (n=181) | REJECTED | below_safety_margin(13443<45665), p_lower_below_threshold(0.04<0.75) |
| 53441734 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 26.776310 USDC | 0.018347 USDC | 0.000000 USDC | 0.005060 USDC | 0.013287 USDC (0.0122 €) | — | 4.96 | 0.034 (n=220) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53441962 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002269 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.57 | 0.186 (n=836) | REJECTED | below_safety_margin(13<45), p_lower_below_threshold(0.19<0.75) |
| 53441962 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.081190 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0088 €) | — | 0.53 | 0.186 (n=836) | REJECTED | below_safety_margin(4265135207425<16237930542446), p_lower_below_threshold(0.19<0.75) |
| 53441962 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 187.334835 USDC | 0.016123 USDC | 0.000000 USDC | 0.006772 USDC | 0.009351 USDC (0.0086 €) | — | 0.50 | 0.186 (n=836) | REJECTED | below_safety_margin(9351<37466), p_lower_below_threshold(0.19<0.75) |
| 53442037 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 195.746739 USDC | 0.014182 USDC | 0.000000 USDC | 0.005060 USDC | 0.009122 USDC (0.0084 €) | — | 0.47 | 0.037 (n=181) | REJECTED | below_safety_margin(9122<39149), p_lower_below_threshold(0.04<0.75) |
| 53442037 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.086727 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0084 €) | — | 0.46 | 0.037 (n=181) | REJECTED | below_safety_margin(4028713084665<17345431656306), p_lower_below_threshold(0.04<0.75) |
| 53440959 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.017415 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0070 €) | — | 1.93 | 0.186 (n=834) | REJECTED | below_safety_margin(3356158371189<3482936178209), p_lower_below_threshold(0.19<0.75) |
| 53440959 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 39.182298 USDC | 0.014335 USDC | 0.000000 USDC | 0.006772 USDC | 0.007563 USDC (0.0070 €) | — | 1.93 | 0.186 (n=834) | REJECTED | below_safety_margin(7563<7836), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 4780 ; taux observé 0.171 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
