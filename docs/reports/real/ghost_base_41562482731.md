# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T02:56:17+00:00 ; durée 58.0 min ; blocs 53440871 → 53442613 (1718 vus)

## Connexion
- Requêtes RPC : 20055 ; erreurs : 0 ; latence p50/p95 : 336.9/1,240.4 ms
- Rafraîchissements d'état : 1718 ; âge des données au dernier bloc : 4.66 s ; changements de frais LP observés (pools à frais dynamiques) : 1954
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16637 ; cycles déclenchés par événement : 2298 ; avance médiane sur le rafraîchissement multicall : 529 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,255.08 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 285 jetons, 18224 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 108, aerodrome 202, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 308, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2253.967555, 'cbBTC': 77042.637438, 'AERO': 0.602257}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,984,618 | 2,255.081329 | 53442612 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,165,167 | 0.029347 | 53442612 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,088,053 | 0.029314 | 53442612 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,963,863 | 0.000013 | 53442612 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,854,333 | 2,252.818950 | 53442612 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,553,083 | 105.168666 | 53442612 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,537,310 | 0.001567 | 53442612 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,355,175 | 1.660446 | 53442612 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,734,041 | 0.029349 | 53442612 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,112,832 | 2,251.956804 | 53442612 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,042,641 | 0.999897 | 53442612 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,909,826 | 2,252.145720 | 53442612 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,455,701 | 39,853.639210 | 53442612 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,689,128 | 0.029323 | 53442612 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,142,413 | 1,123,278.025912 | 53442612 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 2,031,025 | 0.000013 | 53442612 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2841 | 1,983,679 | 105.174833 | 53442612 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | XDP/USDC | 100 | 1,765,756 | 0.018304 | 53442613 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,667,842 | 0.000000 | 53442612 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,605,406 | 0.000013 | 53442612 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,241 | 1.436173 | 53442612 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,540,646 | 0.000013 | 53442612 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,529,055 | 444.970443 | 53442612 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,497,511 | 2,254.848624 | 53442612 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,608 | 0.822379 | 53442612 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,384,556 | 3,748.251143 | 53442612 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,349,912 | 2,258.574486 | 53442612 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,310,072 | 2,252.658770 | 53442612 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,289,467 | 0.004999 | 53442612 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,272,903 | 15,144.633438 | 53442612 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 1,258,059 | 0.000013 | 53442612 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,168,739 | 71.138543 | 53442612 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,100,977 | 37,707,062.323865 | 53442612 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,045,809 | 542,366.666581 | 53442613 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,007,834 | 0.000000 | 53442612 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,002,229 | 22,617,196.530373 | 53442612 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 976,873 | 20.288563 | 53442612 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 956,338 | 84,824.462991 | 53442612 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 922,928 | 2,257.234891 | 53442612 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 914,914 | 1,267,349.544148 | 53442612 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 912,496 | 1,044.538333 | 53442612 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 908,115 | 104.431021 | 53442612 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 875,401 | 81.692678 | 53442612 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,001 | 0.000549 | 53442612 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 857,163 | 0.046703 | 53442612 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 825,000 | 3,725.146765 | 53442612 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 814,339 | 20.304054 | 53442612 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,203 | 0.056052 | 53442612 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,527 | 0.798949 | 53442612 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,123 | 0.577134 | 53442612 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 717,667 | 0.000258 | 53442612 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 702,165 | 4,876,932.615891 | 53442612 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 663,316 | 145,901.194426 | 53442612 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 659,972 | 0.547712 | 53442612 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 653,544 | 2.338342 | 53442612 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 652,376 | 0.000008 | 53442612 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 643,068 | 545,898.357520 | 53442612 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 605,699 | 0.914848 | 53442612 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 587,892 | 0.087354 | 53442612 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 547,207 | 0.036811 | 53442612 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 4015 ; routes examinées : 73169360 ; candidats optimisés : 194210 ; net attendu > 0 : 123 ; dernier cycle 404.1 ms
- Rejets (moteur) : {'spread_below_threshold': 72037551, 'liquidity_below_min': 923632, 'negative_expected_net': 194087, 'unquotable': 9784, 'borrow_bound_too_small': 4012, 'cycle_budget_exhausted': 171}
- Enregistrements de la session : 194210 ; net attendu > 0 : 123 ; simulés (eth_call de la vraie tx) : 3 (ok 0, échec 3) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 194210} ; motifs de rejet : {'below_safety_margin': 120, 'negative_expected_net': 194087, 'p_lower_below_threshold': 117, 'reliability_not_demonstrated': 6, 'simulation_failed': 3}

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
| 53442597 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.125424 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0226 €) | — | 0.87 | 0.026 (n=56) | REJECTED | below_safety_margin(10907254575686<25084764188851), p_lower_below_threshold(0.03<0.75) |
| 53442597 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 282.085552 USDC | 0.029630 USDC | 0.000000 USDC | 0.005063 USDC | 0.024567 USDC (0.0226 €) | — | 0.87 | 0.026 (n=56) | REJECTED | below_safety_margin(24567<56417), p_lower_below_threshold(0.03<0.75) |
| 53441628 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.104580 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0141 €) | — | 0.65 | 0.026 (n=56) | REJECTED | below_safety_margin(6806094089813<20915932793551), p_lower_below_threshold(0.03<0.75) |
| 53441628 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.104580 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0141 €) | — | 0.65 | 0.026 (n=56) | REJECTED | below_safety_margin(6806094089813<20915932793551), p_lower_below_threshold(0.03<0.75) |
| 53441628 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 233.843885 USDC | 0.020397 USDC | 0.000000 USDC | 0.005060 USDC | 0.015337 USDC (0.0141 €) | — | 0.66 | 0.026 (n=56) | REJECTED | below_safety_margin(15337<46768), p_lower_below_threshold(0.03<0.75) |
| 53441628 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 233.843885 USDC | 0.020397 USDC | 0.000000 USDC | 0.005060 USDC | 0.015337 USDC (0.0141 €) | — | 0.66 | 0.026 (n=56) | REJECTED | below_safety_margin(15337<46768), p_lower_below_threshold(0.03<0.75) |
| 53441628 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.101416 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0124 €) | — | 0.59 | 0.037 (n=181) | REJECTED | below_safety_margin(5965313528361<20283117094792), p_lower_below_threshold(0.04<0.75) |
| 53441628 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.101416 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0124 €) | — | 0.59 | 0.037 (n=181) | REJECTED | below_safety_margin(5965313528361<20283117094792), p_lower_below_threshold(0.04<0.75) |
| 53441628 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 228.327631 USDC | 0.018845 USDC | 0.000000 USDC | 0.005402 USDC | 0.013443 USDC (0.0124 €) | — | 0.59 | 0.037 (n=181) | REJECTED | below_safety_margin(13443<45665), p_lower_below_threshold(0.04<0.75) |
| 53441628 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 228.327631 USDC | 0.018845 USDC | 0.000000 USDC | 0.005402 USDC | 0.013443 USDC (0.0124 €) | — | 0.59 | 0.037 (n=181) | REJECTED | below_safety_margin(13443<45665), p_lower_below_threshold(0.04<0.75) |
| 53441734 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 26.776310 USDC | 0.018347 USDC | 0.000000 USDC | 0.005060 USDC | 0.013287 USDC (0.0122 €) | — | 4.96 | 0.034 (n=220) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53442343 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.043538 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0110 €) | — | 1.21 | 0.260 (n=341) | REJECTED | below_safety_margin(5288901754384<8707638240010), p_lower_below_threshold(0.26<0.75) |
| 53442344 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.043538 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0110 €) | — | 1.21 | 0.260 (n=341) | REJECTED | below_safety_margin(5288901754384<8707638240010), p_lower_below_threshold(0.26<0.75) |
| 53442343 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 97.776827 USDC | 0.018690 USDC | 0.000000 USDC | 0.006777 USDC | 0.011913 USDC (0.0110 €) | — | 1.22 | 0.260 (n=341) | REJECTED | below_safety_margin(11913<19555), p_lower_below_threshold(0.26<0.75) |
| 53442344 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 97.776827 USDC | 0.018690 USDC | 0.000000 USDC | 0.006777 USDC | 0.011913 USDC (0.0110 €) | — | 1.22 | 0.260 (n=341) | REJECTED | below_safety_margin(11913<19555), p_lower_below_threshold(0.26<0.75) |
| 53441962 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002269 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.57 | 0.186 (n=836) | REJECTED | below_safety_margin(13<45), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 4780 ; taux observé 0.171 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
