# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T01:35:03+00:00 ; durée 283.46 min ; blocs 53258868 → 53267369 (7797 vus)

## Connexion
- Requêtes RPC : 90625 ; erreurs : 290 ; latence p50/p95 : 388.6/1,796.5 ms
- Rafraîchissements d'état : 7797 ; âge des données au dernier bloc : 4.92 s ; changements de frais LP observés (pools à frais dynamiques) : 27903
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 182532 ; cycles déclenchés par événement : 5362 ; avance médiane sur le rafraîchissement multicall : 1,648 ms
- Gaz : base fee 0.009668 gwei ; prix ETH (pool le plus profond) : 2,199.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 499 pools, 290 jetons, 18414 routes
- Par DEX : uniswap_v3 138 (quarantaine 1), aerodrome_slipstream 113, aerodrome 207, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 319, par paires 0), mesurés 502, sous le plancher de 10000.0 $ : 3 → gardés 499 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2268.963647, 'cbBTC': 79202.631326, 'AERO': 0.656707}
- Pools en quarantaine : 1 — uniswap_v3:WBTC/cbBTC@0xd960B7: simulation failed ×5 (model/chain mismatch) — until block 53267556

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,650,272 | 2,199.472397 | 53267369 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,772,877 | 0.028672 | 53267368 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,472,043 | 0.000013 | 53267368 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,925,252 | 0.028594 | 53267368 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,955,398 | 2,204.674698 | 53267368 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,651,649 | 100.099027 | 53267368 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,590,013 | 0.001599 | 53267368 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,040,512 | 1.631502 | 53267368 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,488,057 | 0.028673 | 53267369 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 1071 | 4,192,012 | 2,205.619775 | 53267369 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,108,991 | 2,205.795126 | 53267369 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,514,984 | 1.000384 | 53267368 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,464,417 | 37,714.680937 | 53267368 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2540 | 2,736,061 | 0.028617 | 53267368 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2841 | 2,268,984 | 100.069524 | 53267368 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,010,205 | 1,213,474.723704 | 53267368 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 1,973,123 | 0.000013 | 53267368 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,760,313 | 0.018092 | 53267369 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 1,681,959 | 2,198.817057 | 53267368 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,650,113 | 420.770107 | 53267368 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,640,414 | 0.000000 | 53267368 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,628,236 | 0.000013 | 53267368 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,602,804 | 0.000013 | 53267369 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,116 | 1.588220 | 53267368 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 1,456,367 | 0.000013 | 53267369 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,257 | 0.826798 | 53267368 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,328,220 | 3,591.405823 | 53267368 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,287,735 | 14,712.895516 | 53267369 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,278,979 | 0.005130 | 53267368 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,278,097 | 2,204.903737 | 53267368 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,178,295 | 69.989676 | 53267368 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,142,103 | 0.000253 | 53267368 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | WETH/doginme | 10000 | 1,084,390 | 36,519,405.774328 | 53267368 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,025,245 | 531,939.287073 | 53267368 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,006,214 | 18.617092 | 53267368 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 1,005,029 | 0.000000 | 53267368 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | WETH/USDC | 3000 | 999,811 | 2,198.539144 | 53267368 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/EDEL | 7000 | 997,892 | 74,186.464546 | 53267368 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 984,845 | 22,215,934.040448 | 53267368 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | VIRTUAL/WETH | 10000 | 958,837 | 0.000251 | 53267368 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/NOCK | 3000 | 949,389 | 69.453478 | 53267368 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 948,742 | 0.045381 | 53267369 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 936,052 | 100.235945 | 53267368 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/AERO | 10000 | 932,785 | 3,587.362329 | 53267368 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/WELL | 10000 | 927,917 | 1,174,446.380117 | 53267368 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 911,102 | 2,203.131359 | 53267368 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 853,705 | 1,094.598964 | 53267368 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 840,741 | 0.000547 | 53267368 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4565 | 832,751 | 19.607319 | 53267368 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 814,041 | 0.059532 | 53267368 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 754,691 | 18.486843 | 53267368 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 744,402 | 0.803616 | 53267368 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 696,093 | 4,714,531.184079 | 53267368 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 685,039 | 0.557755 | 53267368 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 683,681 | 0.000008 | 53267368 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 670,211 | 2.329802 | 53267369 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 636,441 | 0.512114 | 53267368 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2141 | 633,448 | 527,020.791942 | 53267368 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 630,119 | 153,511.044658 | 53267368 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 600,448 | 0.090386 | 53267368 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 13158 ; routes examinées : 242291412 ; candidats optimisés : 1651751 ; net attendu > 0 : 4577 ; dernier cycle 738.8 ms
- Rejets (moteur) : {'spread_below_threshold': 236040399, 'liquidity_below_min': 4198626, 'negative_expected_net': 1647174, 'pool_quarantined': 304372, 'cycle_budget_exhausted': 53775, 'unquotable': 29347, 'borrow_bound_too_small': 13142}
- Enregistrements de la session : 1651751 ; net attendu > 0 : 4577 ; simulés (eth_call de la vraie tx) : 220 (ok 131, échec 89) ; étiquettes ghost N+1 : 48/208 positives
- Décisions : {'REJECTED': 1651751} ; motifs de rejet : {'below_safety_margin': 3082, 'negative_expected_net': 1647174, 'p_lower_below_threshold': 3952, 'price_impact': 10, 'reliability_not_demonstrated': 625, 'sim_below_estimate': 14, 'simulated_net_nonpositive': 8, 'simulation_failed': 89, 'stale_data': 197}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.087669 WETH | 0.007300 WETH | 0.000000 WETH | 0.000018 WETH | 0.007282 WETH (15.2342 €) | — | 830.57 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53265454 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.386452 WETH | 0.007251 WETH | 0.000000 WETH | 0.000022 WETH | 0.007229 WETH (14.7805 €) | 0.007229 WETH | 187.06 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53265454 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 855.686437 USDC | 16.055412 USDC | 0.000000 USDC | 0.048929 USDC | 16.006483 USDC (14.7260 €) | — | 187.06 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.083895 WETH | 0.006985 WETH | 0.000000 WETH | 0.000018 WETH | 0.006967 WETH (14.5760 €) | — | 830.43 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53259987 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 194.516486 USDC | 15.588983 USDC | 0.000000 USDC | 0.042064 USDC | 15.546919 USDC (14.3032 €) | — | 799.26 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53265454 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.356215 WETH | 0.006796 WETH | 0.000000 WETH | 0.000021 WETH | 0.006775 WETH (13.8513 €) | 0.006775 WETH | 190.18 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53265454 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 788.901271 USDC | 15.050257 USDC | 0.000000 USDC | 0.046879 USDC | 15.003378 USDC (13.8031 €) | — | 190.18 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53265454 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.339136 WETH | 0.006674 WETH | 0.000000 WETH | 0.000022 WETH | 0.006652 WETH (13.6001 €) | 0.006652 WETH | 196.14 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53265454 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 750.677187 USDC | 14.772297 USDC | 0.000000 USDC | 0.048929 USDC | 14.723368 USDC (13.5455 €) | — | 196.13 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.074170 WETH | 0.006048 WETH | 0.000000 WETH | 0.000018 WETH | 0.006030 WETH (12.6155 €) | — | 812.97 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.073121 WETH | 0.005996 WETH | 0.000000 WETH | 0.000018 WETH | 0.005978 WETH (12.5070 €) | — | 817.55 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.071054 WETH | 0.005909 WETH | 0.000000 WETH | 0.000018 WETH | 0.005891 WETH (12.3250 €) | — | 829.09 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53265454 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.319788 WETH | 0.006020 WETH | 0.000000 WETH | 0.000024 WETH | 0.005996 WETH (12.2592 €) | — | 187.50 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53265454 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 705.309446 USDC | 13.276990 USDC | 0.000000 USDC | 0.053030 USDC | 13.223960 USDC (12.1660 €) | — | 187.49 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.070554 WETH | 0.005753 WETH | 0.000000 WETH | 0.000018 WETH | 0.005735 WETH (11.9978 €) | — | 812.79 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.069593 WETH | 0.005707 WETH | 0.000000 WETH | 0.000018 WETH | 0.005688 WETH (11.9009 €) | — | 817.36 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | USDC→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 158.488819 USDC | 12.466653 USDC | 0.000000 USDC | 0.041719 USDC | 12.424934 USDC (11.4309 €) | — | 783.96 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v2]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.066843 WETH | 0.005450 WETH | 0.000000 WETH | 0.000018 WETH | 0.005432 WETH (11.3656 €) | — | 812.72 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53259987 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome]→USDC | 160.275220 USDC | 12.199157 USDC | 0.000000 USDC | 0.041750 USDC | 12.157407 USDC (11.1848 €) | — | 758.53 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 53259987 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.001836 cbBTC | 0.000141 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC | 0.000141 cbBTC (10.2641 €) | — | 767.17 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.059219 WETH | 0.004823 WETH | 0.000000 WETH | 0.000018 WETH | 0.004804 WETH (10.0519 €) | — | 811.30 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.058561 WETH | 0.004796 WETH | 0.000000 WETH | 0.000018 WETH | 0.004778 WETH (9.9962 €) | — | 815.87 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.057714 WETH | 0.004686 WETH | 0.000000 WETH | 0.000018 WETH | 0.004667 WETH (9.7649 €) | — | 808.70 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53265454 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.279131 WETH | 0.004765 WETH | 0.000000 WETH | 0.000021 WETH | 0.004744 WETH (9.6988 €) | — | 169.94 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53265454 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 616.208228 USDC | 10.518570 USDC | 0.000000 USDC | 0.046879 USDC | 10.471691 USDC (9.6340 €) | — | 169.94 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3460 ; taux observé 0.114 ; borne inférieure crédible (0.9) 0.107 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
