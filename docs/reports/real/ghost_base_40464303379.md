# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T07:13:59+00:00 ; durée 9.18 min ; blocs 53147666 → 53147945 (272 vus)

## Connexion
- Requêtes RPC : 3325 ; erreurs : 0 ; latence p50/p95 : 347.7/1,463.2 ms
- Rafraîchissements d'état : 272 ; âge des données au dernier bloc : 2.24 s ; changements de frais LP observés (pools à frais dynamiques) : 342
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2986 ; cycles déclenchés par événement : 252 ; avance médiane sur le rafraîchissement multicall : 561 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,304.41 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 526 pools, 304 jetons, 19350 routes
- Par DEX : uniswap_v3 143, aerodrome_slipstream 127, aerodrome 212 (quarantaine 1), pancakeswap_v3 28, uniswap_v2 13 (quarantaine 1), sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 338, par paires 0), mesurés 528, sous le plancher de 10000.0 $ : 2 → gardés 526 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2304.525597, 'cbBTC': 79510.140598, 'AERO': 0.665632}
- Pools en quarantaine : 2 — aerodrome:wIRON/USDC@0x9941df: simulation failed ×5 (model/chain mismatch) — until block 53148226; uniswap_v2:wIRON/WETH@0x378C0D: simulation failed ×5 (model/chain mismatch) — until block 53148226

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,378,364 | 2,304.406515 | 53147945 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,064,490 | 0.028939 | 53147945 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,046,778 | 0.028948 | 53147945 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,478,702 | 0.000013 | 53147945 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,351,322 | 94.111361 | 53147945 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,297,060 | 2,301.632684 | 53147945 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 6,940,122 | 1.502331 | 53147945 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,921,494 | 0.001636 | 53147945 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,319,397 | 0.028940 | 53147945 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 594 | 5,208,636 | 2,300.896662 | 53147945 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,445,165 | 2,300.694855 | 53147945 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,194,300 | 0.998749 | 53147945 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,631,855 | 37,683.180146 | 53147945 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,161,907 | 0.028975 | 53147945 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,473,422 | 94.371719 | 53147945 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,433,894 | 0.000013 | 53147945 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 2,351,078 | 2,307.614539 | 53147945 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/FAI | 10000 | 2,102,805 | 1,217,557.512867 | 53147945 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,849,383 | 0.019051 | 53147945 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,823,112 | 0.000000 | 53147945 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,746,537 | 405.665225 | 53147945 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,685,521 | 0.000013 | 53147945 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,683,756 | 0.000013 | 53147945 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,659,293 | 0.000013 | 53147945 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,493,450 | 0.005843 | 53147945 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,048 | 0.826392 | 53147945 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53147945 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,416,095 | 3,460.221769 | 53147945 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,360,570 | 14,012.114164 | 53147945 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,253,379 | 2,301.654624 | 53147945 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,225,609 | 0.000265 | 53147945 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53147945 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,195,076 | 3,447.248911 | 53147945 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,164,802 | 0.000266 | 53147945 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,133,984 | 0.000000 | 53147945 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,129,965 | 1,091,191.188509 | 53147945 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,128,450 | 37,286,282.345016 | 53147945 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,097,161 | 501,536.071952 | 53147945 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,063,528 | 71,941.184981 | 53147945 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,052,685 | 20,512,964.965661 | 53147945 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,034,339 | 17.242673 | 53147945 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,029,096 | 59.109836 | 53147945 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 999,473 | 0.040894 | 53147945 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 948,990 | 2,317.651257 | 53147945 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 907,020 | 1,059.542714 | 53147945 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 900,878 | 2.308782 | 53147945 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 890,701 | 0.000560 | 53147945 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 874,737 | 18.117301 | 53147945 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 865,804 | 93.452950 | 53147945 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 842,036 | 2,304.490200 | 53147945 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 838,179 | 17.512176 | 53147945 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 802,187 | 0.057740 | 53147945 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 789,179 | 0.000008 | 53147945 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 780,214 | 0.803179 | 53147945 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 736,676 | 0.612383 | 53147945 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 735,713 | 4,631,924.400756 | 53147945 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 696,656 | 0.610492 | 53147945 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 694,450 | 138,586.394314 | 53147945 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2123 | 684,927 | 503,073.951267 | 53147945 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 677,683 | 0.109765 | 53147945 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 523 ; routes examinées : 10120050 ; candidats optimisés : 23982 ; net attendu > 0 : 48 ; dernier cycle 117.9 ms
- Rejets (moteur) : {'spread_below_threshold': 9868787, 'liquidity_below_min': 213253, 'negative_expected_net': 23934, 'unquotable': 11484, 'pool_quarantined': 1960, 'borrow_bound_too_small': 522, 'cycle_budget_exhausted': 62}
- Enregistrements de la session : 23982 ; net attendu > 0 : 48 ; simulés (eth_call de la vraie tx) : 9 (ok 3, échec 6) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 23982} ; motifs de rejet : {'below_safety_margin': 6, 'negative_expected_net': 23934, 'p_lower_below_threshold': 2, 'reliability_not_demonstrated': 46, 'simulation_failed': 6, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53147926 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.016252 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0892 €) | — | 25.89 | 0.006 (n=1) | REJECTED | stale_data(4665ms>4000.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53147926 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 37.334929 USDC | 0.102767 USDC | 0.000000 USDC | 0.005891 USDC | 0.096876 USDC (0.0891 €) | — | 25.95 | 0.006 (n=1) | REJECTED | stale_data(4662ms>4000.0), reliability_not_demonstrated |
| 53147926 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.016147 WETH | 0.000044 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0882 €) | — | 25.77 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53147926 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.016145 WETH | 0.000044 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0882 €) | — | 25.77 | 0.003 (n=2) | REJECTED | stale_data(4676ms>4000.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53147926 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 37.075324 USDC | 0.102040 USDC | 0.000000 USDC | 0.006241 USDC | 0.095799 USDC (0.0881 €) | — | 25.84 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53147926 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 37.178792 USDC | 0.101684 USDC | 0.000000 USDC | 0.005891 USDC | 0.095793 USDC (0.0881 €) | — | 25.77 | 0.003 (n=2) | REJECTED | stale_data(4674ms>4000.0), reliability_not_demonstrated |
| 53147926 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.015451 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0859 €) | — | 26.21 | 0.003 (n=2) | REJECTED | stale_data(4659ms>4000.0), reliability_not_demonstrated |
| 53147926 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 35.535016 USDC | 0.099138 USDC | 0.000000 USDC | 0.005891 USDC | 0.093247 USDC (0.0858 €) | — | 26.24 | 0.003 (n=2) | REJECTED | stale_data(4656ms>4000.0), reliability_not_demonstrated |
| 53147926 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.015111 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0762 €) | — | 23.79 | 0.003 (n=2) | REJECTED | stale_data(4682ms>4000.0), reliability_not_demonstrated |
| 53147926 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 34.669772 USDC | 0.088672 USDC | 0.000000 USDC | 0.005891 USDC | 0.082781 USDC (0.0762 €) | — | 23.88 | 0.003 (n=2) | REJECTED | stale_data(4679ms>4000.0), reliability_not_demonstrated |
| 53147926 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.015034 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0754 €) | — | 23.67 | 0.006 (n=1) | REJECTED | stale_data(4687ms>4000.0), reliability_not_demonstrated |
| 53147926 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 34.491514 USDC | 0.087847 USDC | 0.000000 USDC | 0.005891 USDC | 0.081956 USDC (0.0754 €) | — | 23.76 | 0.006 (n=1) | REJECTED | stale_data(4684ms>4000.0), reliability_not_demonstrated |
| 53147926 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[sushiswap_v3]→WETH | 0.014405 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0715 €) | — | 23.41 | 0.003 (n=2) | REJECTED | stale_data(4693ms>4000.0), reliability_not_demonstrated |
| 53147926 | USDC→[sushiswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 33.115564 USDC | 0.083580 USDC | 0.000000 USDC | 0.005891 USDC | 0.077689 USDC (0.0715 €) | — | 23.46 | 0.003 (n=2) | REJECTED | stale_data(4690ms>4000.0), reliability_not_demonstrated |
| 53147874 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.014579 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0641 €) | 0.000030 WETH | 20.74 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53147874 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.014579 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0641 €) | — | 20.74 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53147874 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 33.484642 USDC | 0.075489 USDC | 0.000000 USDC | 0.005891 USDC | 0.069598 USDC (0.0640 €) | — | 20.79 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53147874 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 33.484642 USDC | 0.075489 USDC | 0.000000 USDC | 0.005891 USDC | 0.069598 USDC (0.0640 €) | — | 20.79 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53147874 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.014157 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0602 €) | 0.000028 WETH | 20.06 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53147874 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.014157 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0602 €) | — | 20.06 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53147874 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 32.445638 USDC | 0.071629 USDC | 0.000000 USDC | 0.006241 USDC | 0.065388 USDC (0.0602 €) | — | 20.15 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53147874 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 32.445638 USDC | 0.071629 USDC | 0.000000 USDC | 0.006241 USDC | 0.065388 USDC (0.0602 €) | — | 20.15 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53147874 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.014127 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0599 €) | 0.000028 WETH | 20.01 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53147874 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.014127 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0599 €) | — | 20.01 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53147874 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 32.439275 USDC | 0.070970 USDC | 0.000000 USDC | 0.005891 USDC | 0.065079 USDC (0.0599 €) | — | 20.06 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2814 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
