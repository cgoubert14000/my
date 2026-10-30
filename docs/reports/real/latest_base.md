# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T18:52:09+00:00 ; durée 310.24 min ; blocs 53289181 → 53298482 (9023 vus)

## Connexion
- Requêtes RPC : 108168 ; erreurs : 45 ; latence p50/p95 : 67.7/601.9 ms
- Rafraîchissements d'état : 9023 ; âge des données au dernier bloc : 2.45 s ; changements de frais LP observés (pools à frais dynamiques) : 23645
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 192464 ; cycles déclenchés par événement : 10528 ; avance médiane sur le rafraîchissement multicall : 719 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,227.71 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 287 jetons, 18738 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 206, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2224.464255, 'cbBTC': 77004.393698, 'AERO': 0.620215}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,005,936 | 2,227.707705 | 53298483 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,852,205 | 0.029052 | 53298483 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,567,801 | 0.000013 | 53298483 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,997,826 | 0.029029 | 53298483 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,137,753 | 2,222.455663 | 53298483 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,620,992 | 101.351200 | 53298483 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,592,055 | 0.001600 | 53298483 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,856,809 | 1.625035 | 53298483 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,521,263 | 0.029048 | 53298483 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,133,764 | 2,221.812440 | 53298483 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,038,163 | 2,221.705831 | 53298483 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,036,598 | 0.998958 | 53298483 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,526,058 | 37,356.498056 | 53298483 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,732,871 | 0.029043 | 53298483 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2841 | 2,296,036 | 101.317677 | 53298483 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,042,242 | 1,206,344.208581 | 53298483 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,907,728 | 0.000013 | 53298483 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,751,188 | 0.000000 | 53298483 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,706,666 | 0.017202 | 53298483 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,668,337 | 423.324584 | 53298483 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,622,344 | 0.000013 | 53298483 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,537,349 | 0.000013 | 53298483 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,519,222 | 2,228.310112 | 53298483 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,512,933 | 1.548785 | 53298483 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 1,457,095 | 0.000013 | 53298483 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,542 | 0.825809 | 53298483 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,394,187 | 3,617.497924 | 53298483 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,307,216 | 2,222.307310 | 53298483 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,291,569 | 14,521.854962 | 53298483 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,265,205 | 0.004960 | 53298483 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,176,477 | 70.206134 | 53298483 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,096,538 | 36,539,184.753919 | 53298483 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,049,743 | 517,186.035209 | 53298483 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,031,052 | 21,015,971.546121 | 53298483 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,014,367 | 0.000000 | 53298483 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,008,682 | 74,493.390611 | 53298483 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,006,343 | 2,226.489489 | 53298483 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 992,492 | 63.552541 | 53298483 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 984,763 | 19.810598 | 53298483 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 955,766 | 101.212026 | 53298483 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 936,835 | 0.045601 | 53298483 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 923,703 | 1,216,075.930632 | 53298483 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 918,358 | 2,235.963227 | 53298483 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 880,142 | 1,089.395003 | 53298483 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 855,069 | 3,591.290607 | 53298483 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 854,652 | 0.000551 | 53298483 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4540 | 830,590 | 19.692539 | 53298483 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 814,005 | 0.059524 | 53298483 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 776,616 | 17.789772 | 53298483 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 754,041 | 0.803616 | 53298483 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 732,607 | 0.000264 | 53298483 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 721,935 | 4,498,151.037220 | 53298483 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 720,455 | 0.587359 | 53298483 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 678,560 | 2.330944 | 53298483 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 673,629 | 0.000008 | 53298483 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 655,061 | 145,804.704618 | 53298483 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 651,302 | 521,195.543803 | 53298483 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 633,127 | 0.506568 | 53298483 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 598,984 | 0.915108 | 53298483 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 598,823 | 0.089959 | 53298483 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 19550 ; routes examinées : 366327900 ; candidats optimisés : 2004338 ; net attendu > 0 : 6505 ; dernier cycle 319.8 ms
- Rejets (moteur) : {'spread_below_threshold': 357924165, 'liquidity_below_min': 5897108, 'negative_expected_net': 1997833, 'pool_quarantined': 338566, 'unquotable': 140123, 'borrow_bound_too_small': 19544, 'cycle_budget_exhausted': 4056}
- Enregistrements de la session : 2004338 ; net attendu > 0 : 6505 ; simulés (eth_call de la vraie tx) : 335 (ok 236, échec 99) ; étiquettes ghost N+1 : 74/209 positives
- Décisions : {'REJECTED': 2004338} ; motifs de rejet : {'below_safety_margin': 5580, 'negative_expected_net': 1997833, 'p_lower_below_threshold': 6010, 'reliability_not_demonstrated': 495, 'sim_below_estimate': 33, 'simulated_net_nonpositive': 6, 'simulation_failed': 99, 'stale_data': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53294291 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→USDC | 6,312.671201 USDC | 3.315700 USDC | 0.000000 USDC | 0.007816 USDC | 3.307884 USDC (3.0433 €) | — | 5.24 | 0.020 (n=177) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53295119 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,048.326394 USDC | 0.412676 USDC | 0.000000 USDC | 0.005855 USDC | 0.406821 USDC (0.3743 €) | — | 1.99 | 0.040 (n=147) | REJECTED | below_safety_margin(406821<409665), p_lower_below_threshold(0.04<0.75) |
| 53295119 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.918920 WETH | 0.000185 WETH | 0.000000 WETH | 0.000003 WETH | 0.000182 WETH (0.3733 €) | — | 1.98 | 0.040 (n=147) | REJECTED | below_safety_margin(182165546497490<183783964067372), p_lower_below_threshold(0.04<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.117062 WETH | 0.000177 WETH | 0.000000 WETH | 0.000003 WETH | 0.000174 WETH (0.3554 €) | 0.000174 WETH | 14.86 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.117062 WETH | 0.000177 WETH | 0.000000 WETH | 0.000003 WETH | 0.000174 WETH (0.3554 €) | — | 14.86 | 0.059 (n=87) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 259.464116 USDC | 0.393348 USDC | 0.000000 USDC | 0.007214 USDC | 0.386134 USDC (0.3552 €) | — | 14.88 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 259.464116 USDC | 0.393348 USDC | 0.000000 USDC | 0.007214 USDC | 0.386134 USDC (0.3552 €) | — | 14.88 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.109757 WETH | 0.000172 WETH | 0.000000 WETH | 0.000003 WETH | 0.000169 WETH (0.3456 €) | 0.000169 WETH | 15.41 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.109757 WETH | 0.000172 WETH | 0.000000 WETH | 0.000003 WETH | 0.000169 WETH (0.3456 €) | — | 15.41 | 0.018 (n=80) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53293514 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 243.507113 USDC | 0.382725 USDC | 0.000000 USDC | 0.007214 USDC | 0.375511 USDC (0.3455 €) | — | 15.42 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 243.507113 USDC | 0.382725 USDC | 0.000000 USDC | 0.007214 USDC | 0.375511 USDC (0.3455 €) | — | 15.42 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.112422 WETH | 0.000162 WETH | 0.000000 WETH | 0.000003 WETH | 0.000159 WETH (0.3254 €) | 0.000159 WETH | 14.16 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.112422 WETH | 0.000162 WETH | 0.000000 WETH | 0.000003 WETH | 0.000159 WETH (0.3254 €) | — | 14.16 | 0.018 (n=80) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53293514 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 249.147534 USDC | 0.360718 USDC | 0.000000 USDC | 0.007214 USDC | 0.353504 USDC (0.3252 €) | — | 14.19 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 249.147534 USDC | 0.360718 USDC | 0.000000 USDC | 0.007214 USDC | 0.353504 USDC (0.3252 €) | — | 14.19 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.108803 WETH | 0.000155 WETH | 0.000000 WETH | 0.000003 WETH | 0.000152 WETH (0.3103 €) | — | 13.96 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.108803 WETH | 0.000155 WETH | 0.000000 WETH | 0.000003 WETH | 0.000152 WETH (0.3103 €) | — | 13.96 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 241.443620 USDC | 0.344393 USDC | 0.000000 USDC | 0.007214 USDC | 0.337179 USDC (0.3102 €) | — | 13.97 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 241.443620 USDC | 0.344393 USDC | 0.000000 USDC | 0.007214 USDC | 0.337179 USDC (0.3102 €) | — | 13.97 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.225957 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.2794 €) | — | 6.05 | 0.202 (n=85) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.225957 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.2794 €) | — | 6.05 | 0.202 (n=85) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 501.049732 USDC | 0.310117 USDC | 0.000000 USDC | 0.006570 USDC | 0.303547 USDC (0.2793 €) | — | 6.06 | 0.202 (n=85) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 501.049732 USDC | 0.310117 USDC | 0.000000 USDC | 0.006570 USDC | 0.303547 USDC (0.2793 €) | — | 6.06 | 0.202 (n=85) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53289560 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 140.927016 USDC | 0.310023 USDC | 0.000000 USDC | 0.006770 USDC | 0.303253 USDC (0.2790 €) | — | 21.52 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.063562 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.2783 €) | 0.000137 WETH | 21.52 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3859 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
