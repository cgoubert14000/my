# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T15:47:34+00:00 ; durée 244.64 min ; blocs 53501612 → 53508950 (6971 vus)

## Connexion
- Requêtes RPC : 83425 ; erreurs : 45 ; latence p50/p95 : 166.3/1,618.5 ms
- Rafraîchissements d'état : 6972 ; âge des données au dernier bloc : 2.55 s ; changements de frais LP observés (pools à frais dynamiques) : 16727
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 25566 ; cycles déclenchés par événement : 2919 ; avance médiane sur le rafraîchissement multicall : 433 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,423.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 495 pools, 284 jetons, 19384 routes
- Par DEX : uniswap_v3 142, aerodrome_slipstream 106, aerodrome 204, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 308, par paires 0), mesurés 498, sous le plancher de 10000.0 $ : 3 → gardés 495 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2327.57512, 'cbBTC': 78571.031441, 'AERO': 0.644724}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,747,760 | 2,423.063797 | 53508950 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,359,133 | 0.030153 | 53508950 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,699,503 | 0.030198 | 53508950 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,223,800 | 0.000012 | 53508950 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,333,518 | 2,416.948562 | 53508950 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,071,075 | 105.507519 | 53508950 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,845,042 | 0.001571 | 53508950 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,490,674 | 1.498789 | 53508950 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,986,005 | 0.030165 | 53508950 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,235,593 | 2,417.960303 | 53508950 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,229,332 | 0.999357 | 53508950 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 1190 | 3,970,268 | 2,417.603823 | 53508950 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,678,969 | 40,596.921639 | 53508950 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,776,369 | 0.030212 | 53508950 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,278,051 | 1,147,022.325397 | 53508950 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,956,847 | 0.007573 | 53508950 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,849,928 | 0.000012 | 53508950 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,763,851 | 0.018175 | 53508950 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,736,691 | 0.000000 | 53508950 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,650,276 | 0.000012 | 53508950 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,640,921 | 447.356468 | 53508950 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,561,330 | 0.000012 | 53508950 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,522,741 | 1.474784 | 53508950 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,512,549 | 3,637.783746 | 53508950 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,757 | 0.815936 | 53508950 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,396,028 | 2,417.151754 | 53508950 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,379,588 | 2,423.538315 | 53508950 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,379,068 | 2,422.940246 | 53508950 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,344,496 | 14,806.392174 | 53508950 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,188,341 | 37,227,540.814579 | 53508950 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,158,071 | 72.455067 | 53508950 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,137,090 | 0.000000 | 53508950 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,113,558 | 553,830.627443 | 53508950 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,074,428 | 22,748,628.209637 | 53508950 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,020,514 | 104.776370 | 53508950 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,000,743 | 18.911320 | 53508950 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 993,286 | 63.452878 | 53508950 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 992,632 | 1,086.393553 | 53508950 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/WELL | 10000 | 981,883 | 1,270,367.154412 | 53508950 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 976,740 | 0.043513 | 53508950 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 974,477 | 94,321.700621 | 53508950 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/cbBTC | 392 | 966,730 | 0.000012 | 53508950 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 945,250 | 2,416.694727 | 53508950 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 917,206 | 0.000541 | 53508950 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 893,297 | 3,624.045530 | 53508950 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 844,774 | 19.232588 | 53508950 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 822,453 | 0.799140 | 53508950 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,898 | 0.057202 | 53508950 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 756,802 | 0.604173 | 53508950 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 752,285 | 4,907,069.265492 | 53508950 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 746,795 | 0.000252 | 53508950 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 726,385 | 140,541.904958 | 53508950 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 705,341 | 0.000008 | 53508950 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2168 | 683,628 | 556,216.673102 | 53508950 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 682,188 | 0.582739 | 53508950 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 651,164 | 0.913877 | 53508950 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 643,979 | 2.607047 | 53508950 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 616,411 | 0.093784 | 53508950 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,484 | 0.039551 | 53508950 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/DRV | 3000 | 556,481 | 6,954.652667 | 53508950 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 9890 ; routes examinées : 191707760 ; candidats optimisés : 711323 ; net attendu > 0 : 2065 ; dernier cycle 226.8 ms
- Rejets (moteur) : {'spread_below_threshold': 187873598, 'liquidity_below_min': 3103015, 'negative_expected_net': 709258, 'cycle_budget_exhausted': 10459, 'borrow_bound_too_small': 8749, 'unquotable': 616}
- Enregistrements de la session : 711323 ; net attendu > 0 : 2065 ; simulés (eth_call de la vraie tx) : 100 (ok 80, échec 20) ; étiquettes ghost N+1 : 3/89 positives
- Décisions : {'REJECTED': 711323} ; motifs de rejet : {'below_safety_margin': 1135, 'negative_expected_net': 709258, 'p_lower_below_threshold': 1860, 'reliability_not_demonstrated': 205, 'simulation_failed': 20, 'stale_data': 9}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53507787 | WETH→[uniswap_v3]→BRETT→[aerodrome_slipstream]→WETH | 0.169364 WETH | 0.001475 WETH | 0.000000 WETH | 0.000009 WETH | 0.001466 WETH (3.2357 €) | 0.001466 WETH | 86.58 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 53501798 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 2,034.593747 USDC | 3.018894 USDC | 0.000000 USDC | 0.007392 USDC | 3.011502 USDC (2.7706 €) | — | 14.80 | 0.130 (n=40) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.025981 cbBTC | 0.000038 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000038 cbBTC (2.7669 €) | — | 14.76 | 0.130 (n=40) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53501798 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,767.921875 USDC | 2.407901 USDC | 0.000000 USDC | 0.006685 USDC | 2.401216 USDC (2.2091 €) | — | 13.58 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→cbBTC | 0.022432 cbBTC | 0.000031 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000031 cbBTC (2.2055 €) | — | 13.62 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,514.082298 USDC | 1.845325 USDC | 0.000000 USDC | 0.006685 USDC | 1.838640 USDC (1.6915 €) | — | 12.14 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→cbBTC | 0.019018 cbBTC | 0.000023 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000023 cbBTC (1.6880 €) | — | 12.30 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,642.926197 USDC | 1.835277 USDC | 0.000000 USDC | 0.006685 USDC | 1.828592 USDC (1.6823 €) | — | 11.13 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[uniswap_v3]→cbBTC | 0.020773 cbBTC | 0.000023 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000023 cbBTC (1.6793 €) | — | 11.20 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH | 0.510340 WETH | 0.000611 WETH | 0.000000 WETH | 0.000003 WETH | 0.000608 WETH (1.3035 €) | — | 11.92 | 0.097 (n=121) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.015101 cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000018 cbBTC (1.3034 €) | — | 11.96 | 0.097 (n=121) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.014794 cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000017 cbBTC (1.2536 €) | — | 11.74 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53501798 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH | 0.496341 WETH | 0.000588 WETH | 0.000000 WETH | 0.000003 WETH | 0.000585 WETH (1.2535 €) | — | 11.79 | 0.030 (n=93) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53505938 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.008228 cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000017 cbBTC (1.2266 €) | — | 20.71 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53505938 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 654.383126 USDC | 1.339804 USDC | 0.000000 USDC | 0.006964 USDC | 1.332840 USDC (1.2262 €) | — | 20.37 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53507661 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 394.085204 USDC | 1.346452 USDC | 0.000000 USDC | 0.023917 USDC | 1.322535 USDC (1.2167 €) | — | 33.56 | 0.000 (n=53) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53507661 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.163628 WETH | 0.000559 WETH | 0.000000 WETH | 0.000010 WETH | 0.000549 WETH (1.2130 €) | 0.000549 WETH | 33.54 | 0.000 (n=53) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53507787 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.224876 WETH | 0.000546 WETH | 0.000000 WETH | 0.000010 WETH | 0.000536 WETH (1.1817 €) | 0.000536 WETH | 23.81 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53507787 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 538.293823 USDC | 1.307355 USDC | 0.000000 USDC | 0.024893 USDC | 1.282462 USDC (1.1799 €) | — | 23.82 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53507661 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 386.019903 USDC | 1.300382 USDC | 0.000000 USDC | 0.023917 USDC | 1.276465 USDC (1.1743 €) | — | 33.07 | 0.000 (n=53) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53507661 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.160430 WETH | 0.000540 WETH | 0.000000 WETH | 0.000010 WETH | 0.000530 WETH (1.1706 €) | 0.000530 WETH | 33.02 | 0.000 (n=53) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53507661 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 384.257173 USDC | 1.293368 USDC | 0.000000 USDC | 0.023917 USDC | 1.269451 USDC (1.1679 €) | — | 33.04 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53507788 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 598.519257 USDC | 1.300700 USDC | 0.000000 USDC | 0.032155 USDC | 1.268545 USDC (1.1671 €) | — | 21.19 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53507788 | cbBTC→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.007324 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1668 €) | — | 21.64 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53507788 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.248255 WETH | 0.000540 WETH | 0.000000 WETH | 0.000013 WETH | 0.000526 WETH (1.1649 €) | 0.000526 WETH | 21.20 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 5161 ; taux observé 0.166 ; borne inférieure crédible (0.9) 0.159 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
