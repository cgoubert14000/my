# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T08:18:02+00:00 ; durée 225.37 min ; blocs 53531902 → 53538665 (5855 vus)

## Connexion
- Requêtes RPC : 68807 ; erreurs : 0 ; latence p50/p95 : 316.3/1,119.4 ms
- Rafraîchissements d'état : 5856 ; âge des données au dernier bloc : 3.25 s ; changements de frais LP observés (pools à frais dynamiques) : 7936
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 39887 ; cycles déclenchés par événement : 4391 ; avance médiane sur le rafraîchissement multicall : 1,323 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,416.91 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 288 jetons, 19590 routes
- Par DEX : uniswap_v3 143 (quarantaine 1), aerodrome_slipstream 108 (quarantaine 1), aerodrome 205, pancakeswap_v3 29 (quarantaine 2), uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 311, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2423.443645, 'cbBTC': 80372.656982, 'AERO': 0.644397}
- Pools en quarantaine : 4 — pancakeswap_v3:USDC/PLAY@0xf1CaCd: simulation failed ×5 (model/chain mismatch) — until block 53538906; aerodrome_slipstream:USDC/PLAY@0xF2c832: simulation failed ×5 (model/chain mismatch) — until block 53538906; uniswap_v3:USDC/ICNT@0x9331F5: simulation failed ×5 (model/chain mismatch) — until block 53538943; pancakeswap_v3:USDC/ICNT@0x175Aa9: simulation failed ×5 (model/chain mismatch) — until block 53538943

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,772,721 | 2,416.906716 | 53538664 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,276,944 | 0.030078 | 53538664 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,658,022 | 0.030091 | 53538664 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,275,786 | 0.000012 | 53538664 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,298,099 | 2,421.286574 | 53538664 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,811,760 | 111.932350 | 53538664 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,827,212 | 0.001564 | 53538664 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,397,104 | 1.517237 | 53538664 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,368,353 | 0.030088 | 53538664 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,436,199 | 2,422.131088 | 53538664 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,229,674 | 0.998998 | 53538664 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,666,099 | 40,674.909861 | 53538664 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,459,810 | 2,421.918561 | 53538664 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,743,906 | 0.030093 | 53538664 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,255,323 | 1,164,309.449368 | 53538664 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,870,182 | 0.006999 | 53538664 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,829,073 | 0.000012 | 53538664 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,756,697 | 0.018040 | 53538664 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,755,801 | 0.000000 | 53538664 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,686,143 | 0.000012 | 53538664 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,635,368 | 448.750605 | 53538664 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,229 | 0.000012 | 53538664 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,524,418 | 1.472046 | 53538664 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,498,907 | 3,679.382508 | 53538664 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,506 | 0.814889 | 53538664 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,418,776 | 2,421.262675 | 53538664 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,378,023 | 2,418.951222 | 53538664 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,377,415 | 2,417.107721 | 53538664 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,341,475 | 14,888.251397 | 53538664 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,181,804 | 37,481,849.466973 | 53538664 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,294 | 73.310640 | 53538664 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,146,276 | 0.000000 | 53538664 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,101,135 | 567,944.691058 | 53538664 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,080,287 | 111.166931 | 53538664 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,063,081 | 23,062,837.377633 | 53538664 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 997,032 | 1,073.033744 | 53538664 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/VELVET | 100 | 991,137 | 19.444601 | 53538664 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 983,592 | 64.810927 | 53538664 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 963,945 | 0.000012 | 53538664 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 956,590 | 2,419.823218 | 53538664 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 955,041 | 97,694.064037 | 53538664 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 917,859 | 0.000539 | 53538664 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 867,096 | 0.046280 | 53538664 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 866,262 | 3,705.417344 | 53538664 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 831,032 | 0.062211 | 53538664 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 829,812 | 19.774263 | 53538664 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 820,481 | 0.798911 | 53538664 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 749,231 | 0.597714 | 53538664 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 738,410 | 5,068,434.829543 | 53538664 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 735,708 | 136,356.772054 | 53538664 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 730,528 | 0.000247 | 53538664 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 702,505 | 0.000008 | 53538664 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2168 | 673,101 | 562,273.206474 | 53538664 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 670,466 | 0.568594 | 53538664 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 648,606 | 0.914396 | 53538664 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 643,832 | 2.484915 | 53538664 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 619,226 | 711,332.511638 | 53538664 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 603,778 | 0.100561 | 53538665 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 602,185 | 0.090445 | 53538664 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/DRV | 3000 | 575,544 | 6,466.929359 | 53538664 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 10246 ; routes examinées : 200719140 ; candidats optimisés : 551275 ; net attendu > 0 : 630 ; dernier cycle 294.6 ms
- Rejets (moteur) : {'spread_below_threshold': 197442318, 'liquidity_below_min': 2713535, 'negative_expected_net': 550645, 'borrow_bound_too_small': 7827, 'pool_quarantined': 3958, 'cycle_budget_exhausted': 227}
- Enregistrements de la session : 551275 ; net attendu > 0 : 630 ; simulés (eth_call de la vraie tx) : 114 (ok 18, échec 96) ; étiquettes ghost N+1 : 0/86 positives
- Décisions : {'REJECTED': 551275} ; motifs de rejet : {'below_safety_margin': 344, 'negative_expected_net': 550645, 'p_lower_below_threshold': 609, 'reliability_not_demonstrated': 21, 'simulation_failed': 96, 'stale_data': 30}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53538081 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001557 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4188 €) | — | 36.34 | 0.046 (n=18) | REJECTED | reliability_not_demonstrated |
| 53538081 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 127.593846 USDC | 0.461318 USDC | 0.000000 USDC | 0.006930 USDC | 0.454388 USDC (0.4180 €) | — | 35.61 | 0.046 (n=18) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53538081 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001380 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3440 €) | — | 33.70 | 0.007 (n=117) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53538081 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 114.820388 USDC | 0.380614 USDC | 0.000000 USDC | 0.006930 USDC | 0.373684 USDC (0.3438 €) | — | 32.55 | 0.007 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53538081 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.001408 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3411 €) | — | 32.75 | 0.007 (n=117) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53538081 | USDC→[uniswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 113.457921 USDC | 0.377000 USDC | 0.000000 USDC | 0.006930 USDC | 0.370070 USDC (0.3405 €) | — | 32.62 | 0.007 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53538081 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001379 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3381 €) | — | 33.14 | 0.046 (n=18) | REJECTED | reliability_not_demonstrated |
| 53538081 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001379 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3381 €) | — | 33.13 | 0.007 (n=117) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53538081 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 113.006029 USDC | 0.374318 USDC | 0.000000 USDC | 0.006930 USDC | 0.367388 USDC (0.3380 €) | — | 32.51 | 0.046 (n=18) | REJECTED | reliability_not_demonstrated |
| 53538081 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 113.459859 USDC | 0.374254 USDC | 0.000000 USDC | 0.006930 USDC | 0.367324 USDC (0.3379 €) | — | 32.37 | 0.007 (n=117) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53538261 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.074142 WETH | 0.000107 WETH | 0.000000 WETH | 0.000003 WETH | 0.000104 WETH (0.2314 €) | — | 14.03 | 0.086 (n=136) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53538261 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 179.233640 USDC | 0.259115 USDC | 0.000000 USDC | 0.007631 USDC | 0.251484 USDC (0.2314 €) | — | 14.03 | 0.086 (n=136) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53538261 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 175.674606 USDC | 0.244501 USDC | 0.000000 USDC | 0.007631 USDC | 0.236870 USDC (0.2179 €) | — | 13.48 | 0.086 (n=136) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53538261 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.072718 WETH | 0.000101 WETH | 0.000000 WETH | 0.000003 WETH | 0.000098 WETH (0.2179 €) | — | 13.48 | 0.086 (n=136) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53538261 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 156.197555 USDC | 0.193242 USDC | 0.000000 USDC | 0.007631 USDC | 0.185611 USDC (0.1708 €) | — | 11.88 | 0.086 (n=136) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53538261 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.064768 WETH | 0.000080 WETH | 0.000000 WETH | 0.000003 WETH | 0.000077 WETH (0.1707 €) | — | 11.85 | 0.086 (n=136) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53538261 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 155.147140 USDC | 0.191839 USDC | 0.000000 USDC | 0.007631 USDC | 0.184208 USDC (0.1695 €) | — | 11.87 | 0.086 (n=136) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53538261 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.064345 WETH | 0.000079 WETH | 0.000000 WETH | 0.000003 WETH | 0.000076 WETH (0.1694 €) | — | 11.84 | 0.086 (n=136) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53538261 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 146.050477 USDC | 0.169406 USDC | 0.000000 USDC | 0.007631 USDC | 0.161775 USDC (0.1488 €) | — | 11.08 | 0.086 (n=136) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53538261 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.060424 WETH | 0.000070 WETH | 0.000000 WETH | 0.000003 WETH | 0.000067 WETH (0.1488 €) | — | 11.07 | 0.086 (n=136) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53538261 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 125.393360 USDC | 0.162092 USDC | 0.000000 USDC | 0.007631 USDC | 0.154461 USDC (0.1421 €) | — | 12.32 | 0.086 (n=136) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53538261 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.051933 WETH | 0.000067 WETH | 0.000000 WETH | 0.000003 WETH | 0.000064 WETH (0.1420 €) | — | 12.30 | 0.086 (n=136) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53537209 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 104.101916 USDC | 0.143089 USDC | 0.000000 USDC | 0.005447 USDC | 0.137642 USDC (0.1266 €) | — | 13.22 | 0.000 (n=85) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53537217 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 97.885260 USDC | 0.127361 USDC | 0.000000 USDC | 0.005448 USDC | 0.121913 USDC (0.1122 €) | — | 12.45 | 0.000 (n=86) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53538011 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.056039 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0719 €) | — | 5.77 | 0.153 (n=659) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |

## Fiabilité et décision
- Observations ghost : 5392 ; taux observé 0.159 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
