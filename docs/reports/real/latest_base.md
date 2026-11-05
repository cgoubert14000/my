# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T08:55:36+00:00 ; durée 262.93 min ; blocs 53531902 → 53539791 (6583 vus)

## Connexion
- Requêtes RPC : 79215 ; erreurs : 0 ; latence p50/p95 : 260.2/1,291.1 ms
- Rafraîchissements d'état : 6583 ; âge des données au dernier bloc : 5.93 s ; changements de frais LP observés (pools à frais dynamiques) : 9113
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 59562 ; cycles déclenchés par événement : 6402 ; avance médiane sur le rafraîchissement multicall : 1,238 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,417.91 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 288 jetons, 19590 routes
- Par DEX : uniswap_v3 143 (quarantaine 1), aerodrome_slipstream 108, aerodrome 205, pancakeswap_v3 29 (quarantaine 1), uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 311, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2423.443645, 'cbBTC': 80372.656982, 'AERO': 0.644397}
- Pools en quarantaine : 2 — pancakeswap_v3:ELSA/USDC@0x83f3AC: simulation failed ×5 (model/chain mismatch) — until block 53540057; uniswap_v3:ELSA/USDC@0xdc8F36: simulation failed ×5 (model/chain mismatch) — until block 53540057

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,803,789 | 2,417.912999 | 53539790 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,286,122 | 0.030071 | 53539790 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,663,229 | 0.030091 | 53539790 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,278,588 | 0.000012 | 53539790 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,300,319 | 2,418.329013 | 53539790 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,832,694 | 111.426893 | 53539791 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,850,261 | 0.001572 | 53539791 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,427,032 | 1.500549 | 53539790 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,371,239 | 0.030065 | 53539790 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,489,957 | 2,418.454574 | 53539790 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,232,372 | 0.998999 | 53539790 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,664,637 | 40,741.279988 | 53539790 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,460,754 | 2,418.265289 | 53539790 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,744,904 | 0.030093 | 53539790 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,256,262 | 1,164,309.449368 | 53539790 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,878,749 | 0.007035 | 53539790 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,829,543 | 0.000012 | 53539790 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,756,531 | 0.000000 | 53539790 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,756,166 | 0.018034 | 53539790 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,686,754 | 0.000012 | 53539790 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,641,827 | 443.670966 | 53539790 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,641 | 0.000012 | 53539790 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,524,416 | 1.472048 | 53539790 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,509,149 | 3,628.221940 | 53539790 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,704 | 0.815752 | 53539790 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | WETH/USDC | 3000 | 1,378,311 | 2,424.394969 | 53539791 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,377,702 | 2,418.027889 | 53539790 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,348,774 | 14,776.211001 | 53539790 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,259,873 | 2,418.637483 | 53539790 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,182,294 | 37,481,849.466973 | 53539790 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,294 | 73.310638 | 53539790 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,145,180 | 0.000000 | 53539790 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,103,777 | 564,670.329827 | 53539790 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,084,645 | 111.166939 | 53539790 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,063,021 | 23,062,837.377633 | 53539790 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 999,465 | 1,073.075196 | 53539790 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,462 | 19.245619 | 53539790 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 983,964 | 64.761977 | 53539790 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 964,364 | 0.000012 | 53539790 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 956,668 | 2,419.823218 | 53539790 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 954,735 | 97,838.000173 | 53539790 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 917,554 | 0.000542 | 53539790 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 871,241 | 3,654.624090 | 53539790 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/VVV | 3000 | 870,461 | 0.046030 | 53539790 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4560 | 831,780 | 19.704137 | 53539790 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 825,391 | 0.061306 | 53539790 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 820,822 | 0.798912 | 53539790 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 750,669 | 0.602547 | 53539790 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 738,525 | 5,071,085.047138 | 53539790 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 734,617 | 136,877.100996 | 53539790 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 731,517 | 0.000247 | 53539790 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 706,897 | 0.000008 | 53539790 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2108 | 675,430 | 559,355.305000 | 53539790 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 670,466 | 0.568594 | 53539790 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 648,962 | 0.914155 | 53539790 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 644,100 | 2.484915 | 53539790 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 607,526 | 744,589.227620 | 53539790 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 604,637 | 0.091004 | 53539790 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/DRV | 3000 | 576,243 | 6,456.623600 | 53539790 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | FLOCK/USDC | 3000 | 573,192 | 0.039410 | 53539790 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 12984 ; routes examinées : 254356560 ; candidats optimisés : 690499 ; net attendu > 0 : 1258 ; dernier cycle 75.4 ms
- Rejets (moteur) : {'spread_below_threshold': 250069143, 'liquidity_below_min': 3576984, 'negative_expected_net': 689241, 'borrow_bound_too_small': 10565, 'pool_quarantined': 9008, 'cycle_budget_exhausted': 361}
- Enregistrements de la session : 690499 ; net attendu > 0 : 1258 ; simulés (eth_call de la vraie tx) : 147 (ok 20, échec 127) ; étiquettes ghost N+1 : 3/112 positives
- Décisions : {'REJECTED': 690499} ; motifs de rejet : {'below_safety_margin': 449, 'negative_expected_net': 689241, 'p_lower_below_threshold': 1194, 'price_impact': 6, 'reliability_not_demonstrated': 64, 'simulation_failed': 127, 'stale_data': 34}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53538780 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.034833 cbBTC | 0.000097 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000097 cbBTC (7.1431 €) | — | 27.75 | 0.000 (n=45) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53538780 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.178909 WETH | 0.003214 WETH | 0.000000 WETH | 0.000003 WETH | 0.003211 WETH (7.1411 €) | — | 27.24 | 0.000 (n=45) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53538780 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.034098 cbBTC | 0.000091 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000091 cbBTC (6.7544 €) | — | 26.80 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53538780 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 1.143579 WETH | 0.003039 WETH | 0.000000 WETH | 0.000003 WETH | 0.003036 WETH (6.7509 €) | — | 26.55 | 0.000 (n=58) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53538780 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.030354 cbBTC | 0.000081 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000081 cbBTC (5.9569 €) | — | 26.55 | 0.000 (n=45) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53538780 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.012732 WETH | 0.002679 WETH | 0.000000 WETH | 0.000003 WETH | 0.002676 WETH (5.9505 €) | — | 26.42 | 0.000 (n=45) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53538780 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.014018 cbBTC | 0.000041 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000041 cbBTC (3.0590 €) | — | 29.53 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 53538780 | WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.466816 WETH | 0.001378 WETH | 0.000000 WETH | 0.000003 WETH | 0.001375 WETH (3.0581 €) | — | 29.46 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 53538780 | cbBTC→[uniswap_v3]→WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.013587 cbBTC | 0.000039 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000039 cbBTC (2.8949 €) | — | 28.83 | 0.007 (n=119) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53538780 | WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.449555 WETH | 0.001304 WETH | 0.000000 WETH | 0.000003 WETH | 0.001301 WETH (2.8929 €) | — | 28.94 | 0.007 (n=119) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53539222 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.329123 WETH | 0.001286 WETH | 0.000000 WETH | 0.000003 WETH | 0.001283 WETH (2.8532 €) | — | 38.97 | 0.000 (n=47) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53539222 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.009874 cbBTC | 0.000039 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000039 cbBTC (2.8530 €) | — | 39.08 | 0.000 (n=47) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53539222 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 2,044.258401 USDC | 3.076430 USDC | 0.000000 USDC | 0.007686 USDC | 3.068744 USDC (2.8232 €) | — | 15.01 | 0.113 (n=46) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53539222 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 2,160.225849 USDC | 3.073992 USDC | 0.000000 USDC | 0.006952 USDC | 3.067040 USDC (2.8217 €) | — | 14.20 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53539222 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.025221 cbBTC | 0.000038 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000038 cbBTC (2.8153 €) | — | 15.10 | 0.113 (n=46) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53539222 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[uniswap_v3]→cbBTC | 0.026179 cbBTC | 0.000038 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000038 cbBTC (2.8138 €) | — | 14.54 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53539222 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH | 0.985047 WETH | 0.001255 WETH | 0.000000 WETH | 0.000003 WETH | 0.001252 WETH (2.7843 €) | — | 12.71 | 0.086 (n=137) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53539222 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.029309 cbBTC | 0.000038 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000038 cbBTC (2.7835 €) | — | 12.85 | 0.086 (n=137) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53538780 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.013084 cbBTC | 0.000037 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000037 cbBTC (2.7368 €) | — | 28.30 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 53538780 | WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.435838 WETH | 0.001233 WETH | 0.000000 WETH | 0.000003 WETH | 0.001230 WETH (2.7347 €) | — | 28.22 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 53538780 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 5,626.681975 USDC | 2.800200 USDC | 0.000000 USDC | 0.008368 USDC | 2.791832 USDC (2.5685 €) | — | 4.96 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53538780 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.069357 cbBTC | 0.000035 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000035 cbBTC (2.5646 €) | — | 5.00 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53538780 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 2.324259 WETH | 0.001156 WETH | 0.000000 WETH | 0.000003 WETH | 0.001153 WETH (2.5635 €) | — | 4.96 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53539222 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.308846 WETH | 0.001123 WETH | 0.000000 WETH | 0.000003 WETH | 0.001120 WETH (2.4913 €) | — | 36.26 | 0.000 (n=47) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53539222 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.009286 cbBTC | 0.000034 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000034 cbBTC (2.4900 €) | — | 36.27 | 0.000 (n=47) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 5418 ; taux observé 0.159 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
