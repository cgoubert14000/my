# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T15:16:38+00:00 ; durée 232.37 min ; blocs 53025852 → 53032821 (6942 vus)

## Connexion
- Requêtes RPC : 86737 ; erreurs : 23 ; latence p50/p95 : 189.4/610.5 ms
- Rafraîchissements d'état : 6943 ; âge des données au dernier bloc : 2.43 s ; changements de frais LP observés (pools à frais dynamiques) : 11553
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 125199 ; cycles déclenchés par événement : 8405 ; avance médiane sur le rafraîchissement multicall : 285 ms
- Gaz : base fee 0.015607 gwei ; prix ETH (pool le plus profond) : 2,297.10 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 536 pools, 308 jetons, 19360 routes
- Par DEX : uniswap_v3 143, aerodrome 216, aerodrome_slipstream 133 (quarantaine 1), pancakeswap_v3 29 (quarantaine 1), uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 348, par paires 0), mesurés 538, sous le plancher de 10000.0 $ : 2 → gardés 536 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2363.674955, 'cbBTC': 80533.217668, 'AERO': 0.705694}
- Pools en quarantaine : 2 — aerodrome_slipstream:WETH/USDT@0x9785eF: simulation failed ×5 (model/chain mismatch) — until block 53032875; pancakeswap_v3:USDC/USDT@0x5f07bb: simulation failed ×5 (model/chain mismatch) — until block 53032875

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 152,006,555 | 2,297.104240 | 53032821 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,695,075 | 0.028902 | 53032821 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 11,917,928 | 97.463962 | 53032821 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,014,197 | 0.028946 | 53032821 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,560,366 | 0.000013 | 53032821 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,827,898 | 1.438427 | 53032821 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,347,480 | 2,291.601112 | 53032821 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2775 | 7,876,624 | 0.028919 | 53032821 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,896,032 | 0.001630 | 53032821 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 438 | 6,266,192 | 0.000013 | 53032821 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 2000 | 5,356,853 | 2,291.778228 | 53032821 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,295,301 | 0.028904 | 53032821 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 4,800,725 | 0.000013 | 53032821 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,415,970 | 2,292.050575 | 53032821 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,184,111 | 0.998962 | 53032821 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,813,780 | 34,352.930079 | 53032821 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,771,572 | 2,293.439857 | 53032821 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 568 | 2,723,791 | 2,317.962499 | 53032821 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2805 | 2,438,505 | 97.458327 | 53032821 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,175,503 | 411.263796 | 53032821 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,066,697 | 1,252,500.827463 | 53032821 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,897,572 | 0.000013 | 53032821 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/AERO | 10000 | 1,885,749 | 3,330.588614 | 53032821 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,866,024 | 0.000000 | 53032821 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,775,721 | 0.017815 | 53032821 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,723,395 | 0.000013 | 53032821 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,551,265 | 0.000264 | 53032821 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,509,855 | 1.653156 | 53032821 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,952 | 0.826796 | 53032821 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,436,490 | 3,307.264292 | 53032821 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,356,010 | 0.005228 | 53032821 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,349,494 | 14,205.977460 | 53032821 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,245,441 | 2,291.936362 | 53032821 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,225,002 | 64.754265 | 53032821 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,219,012 | 0.000265 | 53032821 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,198,856 | 2.301286 | 53032821 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,162,969 | 0.000000 | 53032821 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,143,730 | 35,471,226.642133 | 53032821 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,128,485 | 49.184149 | 53032821 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 1,112,640 | 1,119,387.704851 | 53032821 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,093,129 | 501,975.878905 | 53032821 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,052,082 | 17.084652 | 53032821 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,034,029 | 17.253557 | 53032821 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,024,150 | 77,115.920558 | 53032821 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,002,126 | 21,953,883.097876 | 53032821 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 937,068 | 0.042348 | 53032821 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 931,610 | 23.318710 | 53032821 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 915,945 | 1,086.752404 | 53032821 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4890 | 881,252 | 17.879214 | 53032821 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | uXRP/WETH | 3000 | 876,374 | 0.000546 | 53032821 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 850,025 | 97.927578 | 53032821 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 840,528 | 2,293.085811 | 53032821 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 834,273 | 0.000009 | 53032821 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 831,848 | 0.062394 | 53032821 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 790,593 | 1.105901 | 53032821 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 777,823 | 0.803010 | 53032821 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 776,962 | 2,309.567857 | 53032821 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,269 | 0.608508 | 53032821 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 727,763 | 4,701,771.942739 | 53032821 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 722,008 | 0.654138 | 53032821 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 15347 ; routes examinées : 297117920 ; candidats optimisés : 1175276 ; net attendu > 0 : 2186 ; dernier cycle 664.6 ms
- Rejets (moteur) : {'spread_below_threshold': 292012887, 'liquidity_below_min': 3545275, 'negative_expected_net': 1173090, 'pool_quarantined': 338770, 'borrow_bound_too_small': 27419, 'unquotable': 11639, 'cycle_budget_exhausted': 6654}
- Enregistrements de la session : 1175276 ; net attendu > 0 : 2186 ; simulés (eth_call de la vraie tx) : 137 (ok 61, échec 76) ; étiquettes ghost N+1 : 16/110 positives
- Décisions : {'REJECTED': 1175276} ; motifs de rejet : {'below_safety_margin': 1368, 'negative_expected_net': 1173090, 'p_lower_below_threshold': 1914, 'reliability_not_demonstrated': 272, 'sim_below_estimate': 8, 'simulated_net_nonpositive': 4, 'simulation_failed': 76, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53032626 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.332835 WETH | 0.000923 WETH | 0.000000 WETH | 0.000003 WETH | 0.000919 WETH (1.9605 €) | — | 6.90 | 0.002 (n=123) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 3,086.282102 USDC | 2.136965 USDC | 0.000000 USDC | 0.007231 USDC | 2.129734 USDC (1.9594 €) | — | 6.90 | 0.002 (n=123) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026232 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 451.845630 USDC | 2.035784 USDC | 0.000000 USDC | 0.005666 USDC | 2.030118 USDC (1.8677 €) | — | 44.93 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53032626 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.170560 WETH | 0.000841 WETH | 0.000000 WETH | 0.000004 WETH | 0.000837 WETH (1.7841 €) | — | 7.15 | 0.097 (n=228) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53032626 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.033654 cbBTC | 0.000024 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000024 cbBTC (1.7829 €) | — | 7.22 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,757.298059 USDC | 1.947708 USDC | 0.000000 USDC | 0.009813 USDC | 1.937895 USDC (1.7829 €) | — | 7.03 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.062736 WETH | 0.000765 WETH | 0.000000 WETH | 0.000003 WETH | 0.000762 WETH (1.6241 €) | — | 7.17 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,459.190455 USDC | 1.771885 USDC | 0.000000 USDC | 0.008089 USDC | 1.763796 USDC (1.6227 €) | — | 7.17 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53032626 | WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.160307 WETH | 0.000755 WETH | 0.000000 WETH | 0.000004 WETH | 0.000751 WETH (1.6014 €) | — | 6.47 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.033108 cbBTC | 0.000022 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000022 cbBTC (1.6003 €) | — | 6.59 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,687.066121 USDC | 1.748437 USDC | 0.000000 USDC | 0.009384 USDC | 1.739053 USDC (1.5999 €) | — | 6.47 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.002486 WETH | 0.000652 WETH | 0.000000 WETH | 0.000004 WETH | 0.000648 WETH (1.3825 €) | — | 6.47 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.029053 cbBTC | 0.000019 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000019 cbBTC (1.3825 €) | — | 6.49 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 2,332.393912 USDC | 1.510907 USDC | 0.000000 USDC | 0.009384 USDC | 1.501523 USDC (1.3814 €) | — | 6.44 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.977188 WETH | 0.000572 WETH | 0.000000 WETH | 0.000004 WETH | 0.000568 WETH (1.2118 €) | — | 5.82 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.028024 cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000017 cbBTC (1.2116 €) | — | 5.89 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 2,265.762058 USDC | 1.324881 USDC | 0.000000 USDC | 0.008955 USDC | 1.315926 USDC (1.2107 €) | — | 5.81 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.980915 WETH | 0.000559 WETH | 0.000000 WETH | 0.000003 WETH | 0.000556 WETH (1.1857 €) | — | 5.67 | 0.002 (n=123) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,270.455169 USDC | 1.294786 USDC | 0.000000 USDC | 0.007231 USDC | 1.287555 USDC (1.1846 €) | — | 5.67 | 0.002 (n=123) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53028022 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 291.241849 USDC | 1.237549 USDC | 0.000000 USDC | 0.005307 USDC | 1.232242 USDC (1.1337 €) | — | 42.31 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53032626 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.780902 WETH | 0.000488 WETH | 0.000000 WETH | 0.000004 WETH | 0.000484 WETH (1.0322 €) | — | 6.20 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53032626 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.022442 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0312 €) | — | 6.26 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,871.420995 USDC | 1.130130 USDC | 0.000000 USDC | 0.010241 USDC | 1.119889 USDC (1.0303 €) | — | 5.98 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53032465 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 1.412996 WETH | 0.000431 WETH | 0.000000 WETH | 0.000003 WETH | 0.000428 WETH (0.9176 €) | — | 3.03 | 0.002 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53032465 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,281.379921 USDC | 1.002676 USDC | 0.000000 USDC | 0.007024 USDC | 0.995652 USDC (0.9160 €) | — | 3.03 | 0.002 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2241 ; taux observé 0.099 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
