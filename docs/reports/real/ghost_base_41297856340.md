# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T14:20:44+00:00 ; durée 224.78 min ; blocs 53370003 → 53376746 (6725 vus)

## Connexion
- Requêtes RPC : 79491 ; erreurs : 3 ; latence p50/p95 : 105.6/580.8 ms
- Rafraîchissements d'état : 6726 ; âge des données au dernier bloc : 1.78 s ; changements de frais LP observés (pools à frais dynamiques) : 5626
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 45607 ; cycles déclenchés par événement : 5408 ; avance médiane sur le rafraîchissement multicall : 280 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,264.22 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 501 pools, 289 jetons, 18668 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 112, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 317, par paires 0), mesurés 504, sous le plancher de 10000.0 $ : 3 → gardés 501 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2268.223075, 'cbBTC': 77979.526152, 'AERO': 0.640175}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,796,228 | 2,264.224509 | 53376746 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,165,137 | 0.029087 | 53376746 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,295,313 | 0.000013 | 53376746 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,156,756 | 0.029102 | 53376746 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,889,598 | 2,269.276119 | 53376746 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,883,653 | 97.554107 | 53376746 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,681,883 | 0.001595 | 53376746 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,733,236 | 1.543412 | 53376746 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,193,720 | 0.029086 | 53376746 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,099,001 | 0.998824 | 53376746 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,061,307 | 2,268.602603 | 53376746 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,963,073 | 2,268.425884 | 53376746 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,557,675 | 37,908.232705 | 53376746 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,701,396 | 0.029087 | 53376746 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,416,095 | 97.580775 | 53376746 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 2,186,504 | 0.000013 | 53376746 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,083,858 | 1,196,938.977038 | 53376746 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,776,993 | 0.018439 | 53376746 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,761,486 | 0.000000 | 53376746 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,638,207 | 0.000013 | 53376746 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,585,991 | 0.000013 | 53376746 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,558,789 | 422.531148 | 53376746 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,008 | 1.499750 | 53376746 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,507,266 | 2,263.951936 | 53376746 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,453 | 0.826767 | 53376746 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,442,818 | 3,500.796650 | 53376746 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,408,476 | 2,268.463105 | 53376746 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,328,623 | 2,269.394072 | 53376746 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,325,555 | 0.005168 | 53376746 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,313,255 | 14,526.843198 | 53376746 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 1,307,829 | 0.000013 | 53376746 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,691 | 71.023144 | 53376746 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,119,502 | 36,154,909.052645 | 53376746 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,080,243 | 508,539.884698 | 53376746 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,060,188 | 0.000000 | 53376746 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,022,337 | 21,961,631.233214 | 53376746 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,002,328 | 96.866330 | 53376746 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 995,044 | 19.221591 | 53376746 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 972,640 | 82,725.162258 | 53376746 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 959,762 | 67.962016 | 53376746 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 958,975 | 1,162,938.015813 | 53376746 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 950,200 | 0.043095 | 53376746 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 949,458 | 992.889927 | 53376746 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 923,209 | 2,252.785569 | 53376746 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 878,538 | 3,507.716727 | 53376746 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 865,254 | 0.000547 | 53376746 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 843,375 | 19.251378 | 53376746 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 822,122 | 0.060810 | 53376746 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 767,230 | 0.801881 | 53376746 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 736,703 | 0.000261 | 53376746 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 728,017 | 0.596390 | 53376746 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 718,286 | 4,695,299.105900 | 53376746 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 698,127 | 0.000008 | 53376746 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 680,391 | 139,687.988173 | 53376746 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 667,747 | 511,132.784806 | 53376746 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 665,121 | 0.556226 | 53376746 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 659,536 | 2.340198 | 53376746 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 615,994 | 0.093845 | 53376746 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 607,757 | 0.916046 | 53376746 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2769 | 554,930 | 993.829286 | 53376746 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 12133 ; routes examinées : 226498844 ; candidats optimisés : 737783 ; net attendu > 0 : 1878 ; dernier cycle 84.6 ms
- Rejets (moteur) : {'spread_below_threshold': 222612471, 'liquidity_below_min': 3101535, 'negative_expected_net': 735905, 'unquotable': 24254, 'borrow_bound_too_small': 22075, 'cycle_budget_exhausted': 726}
- Enregistrements de la session : 737783 ; net attendu > 0 : 1878 ; simulés (eth_call de la vraie tx) : 83 (ok 51, échec 32) ; étiquettes ghost N+1 : 0/62 positives
- Décisions : {'REJECTED': 737783} ; motifs de rejet : {'below_safety_margin': 1576, 'negative_expected_net': 735905, 'p_lower_below_threshold': 1621, 'price_impact': 14, 'reliability_not_demonstrated': 257, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 1, 'simulation_failed': 32, 'stale_data': 17}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.036307 WETH | 0.000885 WETH | 0.000000 WETH | 0.000003 WETH | 0.000882 WETH (1.8341 €) | — | 242.94 | 0.000 (n=33) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 81.979625 USDC | 1.998439 USDC | 0.000000 USDC | 0.006792 USDC | 1.991647 USDC (1.8323 €) | — | 242.94 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.035802 WETH | 0.000874 WETH | 0.000000 WETH | 0.000003 WETH | 0.000871 WETH (1.8108 €) | — | 243.24 | 0.000 (n=37) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 80.865987 USDC | 1.973757 USDC | 0.000000 USDC | 0.006792 USDC | 1.966965 USDC (1.8096 €) | — | 243.24 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.035327 WETH | 0.000863 WETH | 0.000000 WETH | 0.000003 WETH | 0.000860 WETH (1.7879 €) | — | 243.39 | 0.000 (n=37) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 79.770095 USDC | 1.948323 USDC | 0.000000 USDC | 0.006792 USDC | 1.941531 USDC (1.7862 €) | — | 243.39 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→WETH | 0.035595 WETH | 0.000759 WETH | 0.000000 WETH | 0.000002 WETH | 0.000756 WETH (1.5730 €) | — | 212.52 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53373620 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 67.437266 USDC | 1.643882 USDC | 0.000000 USDC | 0.006792 USDC | 1.637090 USDC (1.5061 €) | — | 242.76 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.029721 WETH | 0.000725 WETH | 0.000000 WETH | 0.000003 WETH | 0.000721 WETH (1.5003 €) | — | 242.75 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.028659 WETH | 0.000705 WETH | 0.000000 WETH | 0.000003 WETH | 0.000702 WETH (1.4593 €) | — | 244.88 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 64.723995 USDC | 1.591766 USDC | 0.000000 USDC | 0.006792 USDC | 1.584974 USDC (1.4582 €) | — | 244.88 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.028560 WETH | 0.000703 WETH | 0.000000 WETH | 0.000003 WETH | 0.000700 WETH (1.4558 €) | — | 245.14 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 64.504232 USDC | 1.588066 USDC | 0.000000 USDC | 0.006792 USDC | 1.581274 USDC (1.4548 €) | — | 245.14 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 56.215788 USDC | 1.381799 USDC | 0.000000 USDC | 0.006792 USDC | 1.375007 USDC (1.2650 €) | — | 244.59 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.024806 WETH | 0.000610 WETH | 0.000000 WETH | 0.000003 WETH | 0.000607 WETH (1.2616 €) | — | 244.59 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.018515 WETH | 0.000588 WETH | 0.000000 WETH | 0.000003 WETH | 0.000584 WETH (1.2152 €) | — | 315.62 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018487 WETH | 0.000587 WETH | 0.000000 WETH | 0.000003 WETH | 0.000584 WETH (1.2145 €) | — | 315.93 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 41.805418 USDC | 1.326609 USDC | 0.000000 USDC | 0.007135 USDC | 1.319474 USDC (1.2139 €) | — | 315.62 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 41.743933 USDC | 1.325938 USDC | 0.000000 USDC | 0.007135 USDC | 1.318803 USDC (1.2133 €) | — | 315.93 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.018413 WETH | 0.000585 WETH | 0.000000 WETH | 0.000003 WETH | 0.000582 WETH (1.2102 €) | — | 316.09 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 41.573764 USDC | 1.321235 USDC | 0.000000 USDC | 0.007135 USDC | 1.314100 USDC (1.2090 €) | — | 316.09 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.018103 WETH | 0.000574 WETH | 0.000000 WETH | 0.000003 WETH | 0.000571 WETH (1.1879 €) | — | 315.58 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 40.912689 USDC | 1.298257 USDC | 0.000000 USDC | 0.007135 USDC | 1.291122 USDC (1.1878 €) | — | 315.58 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.017698 WETH | 0.000566 WETH | 0.000000 WETH | 0.000003 WETH | 0.000563 WETH (1.1703 €) | — | 318.01 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.017704 WETH | 0.000566 WETH | 0.000000 WETH | 0.000003 WETH | 0.000563 WETH (1.1697 €) | — | 317.74 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 4117 ; taux observé 0.128 ; borne inférieure crédible (0.9) 0.121 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
