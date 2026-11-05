# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T15:23:43+00:00 ; durée 315.23 min ; blocs 53541978 → 53551432 (9363 vus)

## Connexion
- Requêtes RPC : 110098 ; erreurs : 13 ; latence p50/p95 : 108.4/1,560.0 ms
- Rafraîchissements d'état : 9363 ; âge des données au dernier bloc : 8.11 s ; changements de frais LP observés (pools à frais dynamiques) : 17257
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 93820 ; cycles déclenchés par événement : 8198 ; avance médiane sur le rafraîchissement multicall : 1,390 ms
- Gaz : base fee 0.014388 gwei ; prix ETH (pool le plus profond) : 2,304.14 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 288 jetons, 19416 routes
- Par DEX : uniswap_v3 142 (quarantaine 1), aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 310, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2417.172064, 'cbBTC': 80337.642272, 'AERO': 0.664358}
- Pools en quarantaine : 1 — uniswap_v3:VIRTUAL/WETH@0x9c087E: simulation failed ×5 (model/chain mismatch) — until block 53551571

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,022,032 | 2,303.967584 | 53551432 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,797,714 | 0.029869 | 53551432 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,261,841 | 0.029839 | 53551432 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,042,682 | 0.000013 | 53551432 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,047,864 | 2,298.238233 | 53551432 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,471,354 | 111.211610 | 53551432 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,522,453 | 0.001548 | 53551432 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,125,773 | 1.680138 | 53551432 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,125,161 | 0.029883 | 53551432 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,160,004 | 2,297.261894 | 53551432 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,062,838 | 0.998760 | 53551432 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,429,143 | 42,253.252595 | 53551432 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 1384 | 3,340,989 | 2,297.399243 | 53551432 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2590 | 2,625,356 | 0.029828 | 53551432 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,153,617 | 1,160,500.715180 | 53551432 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,798,889 | 0.007013 | 53551432 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,784,844 | 0.000013 | 53551432 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,682,244 | 0.000000 | 53551432 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,658,850 | 0.016671 | 53551432 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,644,564 | 0.000013 | 53551432 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,555,681 | 452.044429 | 53551432 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,549,151 | 1.432376 | 53551432 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,528,762 | 0.000013 | 53551432 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,082 | 0.817048 | 53551432 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,381,680 | 3,852.161616 | 53551432 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,345,359 | 2,304.393061 | 53551432 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,344,946 | 2,304.392822 | 53551432 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,280,007 | 15,108.646235 | 53551432 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,203,055 | 2,298.127010 | 53551432 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,151,099 | 73.335477 | 53551432 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,124,880 | 37,667,688.172912 | 53551432 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,054,693 | 0.000000 | 53551432 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,045,102 | 575,921.659291 | 53551432 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,044,015 | 110.474030 | 53551432 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,014,475 | 23,003,409.905224 | 53551432 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 986,134 | 64.477869 | 53551432 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 970,065 | 20.720661 | 53551432 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 946,027 | 2,320.321287 | 53551432 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 943,665 | 1,082.864801 | 53551432 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 430 | 936,106 | 0.000013 | 53551432 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 903,223 | 99,270.772174 | 53551432 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 877,549 | 0.000546 | 53551432 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 854,287 | 0.048437 | 53551432 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 803,766 | 3,823.750355 | 53551432 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 800,900 | 0.057491 | 53551432 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4630 | 795,823 | 21.033127 | 53551432 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 782,198 | 0.798912 | 53551432 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 714,001 | 0.560718 | 53551432 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 704,989 | 5,053,867.691143 | 53551432 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 693,951 | 0.000246 | 53551432 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 690,742 | 140,600.605119 | 53551432 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 656,493 | 0.546090 | 53551432 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 650,577 | 0.000008 | 53551432 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2198 | 637,416 | 581,373.650878 | 53551432 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 618,400 | 0.914226 | 53551432 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 614,674 | 2.479668 | 53551432 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 579,584 | 0.085371 | 53551432 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | cbBTC/EDGE | 7000 | 554,776 | 821,536.780314 | 53551432 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | FLOCK/USDC | 3000 | 550,043 | 0.036989 | 53551432 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/DRV | 3000 | 539,350 | 6,692.856427 | 53551432 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 17560 ; routes examinées : 340944960 ; candidats optimisés : 1065172 ; net attendu > 0 : 3170 ; dernier cycle 929.2 ms
- Rejets (moteur) : {'spread_below_threshold': 334911914, 'liquidity_below_min': 4859785, 'negative_expected_net': 1062002, 'pool_quarantined': 78040, 'borrow_bound_too_small': 17535, 'cycle_budget_exhausted': 12514}
- Enregistrements de la session : 1065172 ; net attendu > 0 : 3170 ; simulés (eth_call de la vraie tx) : 189 (ok 112, échec 77) ; étiquettes ghost N+1 : 27/168 positives
- Décisions : {'REJECTED': 1065172} ; motifs de rejet : {'below_safety_margin': 2081, 'negative_expected_net': 1062002, 'p_lower_below_threshold': 2839, 'price_impact': 2, 'reliability_not_demonstrated': 331, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 77, 'stale_data': 46}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53551389 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.036868 cbBTC | 0.000025 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000024 cbBTC (1.7452 €) | — | 6.64 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.259493 WETH | 0.000831 WETH | 0.000000 WETH | 0.000010 WETH | 0.000821 WETH (1.7449 €) | — | 6.52 | 0.150 (n=729) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551389 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,893.570456 USDC | 1.915127 USDC | 0.000000 USDC | 0.023090 USDC | 1.892037 USDC (1.7407 €) | — | 6.54 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53545322 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 275.403994 USDC | 1.039397 USDC | 0.000000 USDC | 0.005442 USDC | 1.033955 USDC (0.9512 €) | — | 37.54 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53551389 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.027073 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000010 cbBTC (0.6948 €) | — | 3.60 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.931860 WETH | 0.000336 WETH | 0.000000 WETH | 0.000009 WETH | 0.000327 WETH (0.6946 €) | — | 3.51 | 0.150 (n=729) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551389 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,099.401077 USDC | 0.773419 USDC | 0.000000 USDC | 0.020472 USDC | 0.752947 USDC (0.6927 €) | — | 3.59 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.024956 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6755 €) | — | 3.80 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.854198 WETH | 0.000327 WETH | 0.000000 WETH | 0.000010 WETH | 0.000318 WETH (0.6750 €) | — | 3.72 | 0.150 (n=729) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551389 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,967.336294 USDC | 0.753778 USDC | 0.000000 USDC | 0.022217 USDC | 0.731561 USDC (0.6730 €) | — | 3.72 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.501821 WETH | 0.000323 WETH | 0.000000 WETH | 0.000009 WETH | 0.000314 WETH (0.6671 €) | — | 6.26 | 0.150 (n=729) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551389 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.014823 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6670 €) | — | 6.31 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,164.754684 USDC | 0.743565 USDC | 0.000000 USDC | 0.020472 USDC | 0.723093 USDC (0.6652 €) | — | 6.21 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.800686 WETH | 0.000303 WETH | 0.000000 WETH | 0.000010 WETH | 0.000293 WETH (0.6231 €) | — | 3.66 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.023617 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6228 €) | — | 3.70 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,907.105492 USDC | 0.698049 USDC | 0.000000 USDC | 0.022217 USDC | 0.675832 USDC (0.6218 €) | — | 3.54 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551395 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.039270 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6038 €) | — | 2.16 | 0.171 (n=973) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53551395 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.374661 WETH | 0.000294 WETH | 0.000000 WETH | 0.000010 WETH | 0.000284 WETH (0.6038 €) | — | 2.07 | 0.171 (n=973) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53551395 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 3,011.773235 USDC | 0.676238 USDC | 0.000000 USDC | 0.022966 USDC | 0.653272 USDC (0.6010 €) | — | 2.17 | 0.171 (n=973) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53551389 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.904460 WETH | 0.000266 WETH | 0.000000 WETH | 0.000009 WETH | 0.000257 WETH (0.5462 €) | — | 2.84 | 0.172 (n=972) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53551389 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.026065 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5459 €) | — | 2.94 | 0.172 (n=972) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53551389 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,150.657707 USDC | 0.611675 USDC | 0.000000 USDC | 0.020472 USDC | 0.591203 USDC (0.5439 €) | — | 2.75 | 0.172 (n=972) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53551389 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.824470 WETH | 0.000228 WETH | 0.000000 WETH | 0.000007 WETH | 0.000221 WETH (0.4695 €) | — | 2.68 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53551389 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.024322 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4689 €) | — | 2.71 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53546498 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.562613 WETH | 0.000210 WETH | 0.000000 WETH | 0.000003 WETH | 0.000207 WETH (0.4585 €) | — | 3.68 | 0.029 (n=289) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 5635 ; taux observé 0.157 ; borne inférieure crédible (0.9) 0.151 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
