# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T06:48:24+00:00 ; durée 128.98 min ; blocs 53056902 → 53060776 (3807 vus)

## Connexion
- Requêtes RPC : 47162 ; erreurs : 0 ; latence p50/p95 : 256.9/873.3 ms
- Rafraîchissements d'état : 3807 ; âge des données au dernier bloc : 3.24 s ; changements de frais LP observés (pools à frais dynamiques) : 3887
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 36559 ; cycles déclenchés par événement : 4490 ; avance médiane sur le rafraîchissement multicall : 297 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,347.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 309 jetons, 19696 routes
- Par DEX : uniswap_v3 144, aerodrome 216, aerodrome_slipstream 134, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 349, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2361.63016, 'cbBTC': 80803.612106, 'AERO': 0.690594}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,820,227 | 2,347.459547 | 53060777 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,316,641 | 0.029127 | 53060777 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,259,711 | 0.029192 | 53060777 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,524,867 | 0.000012 | 53060777 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,965,780 | 95.425523 | 53060777 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,417,657 | 2,343.869977 | 53060777 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,619,588 | 1.469703 | 53060777 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,030,689 | 0.001648 | 53060777 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,649,850 | 2,343.647626 | 53060777 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,453,066 | 0.029124 | 53060777 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,440,710 | 2,343.766454 | 53060777 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,240,734 | 0.999832 | 53060777 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,893,312 | 34,423.946326 | 53060777 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,796,810 | 2,347.767717 | 53060777 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2525 | 3,257,798 | 0.029180 | 53060777 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,855,669 | 0.000012 | 53060777 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,518,225 | 95.451078 | 53060777 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,223,776 | 411.163581 | 53060777 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,131,510 | 1,229,675.520279 | 53060777 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,904,423 | 0.000012 | 53060777 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,901,751 | 0.000000 | 53060777 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,789,194 | 0.018017 | 53060777 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,732,077 | 0.000012 | 53060777 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,720,986 | 0.000012 | 53060777 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,577,938 | 0.000265 | 53060777 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53060777 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,464,085 | 0.005582 | 53060777 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,859 | 0.826892 | 53060777 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,436,237 | 3,443.951015 | 53060777 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,372,953 | 14,100.759645 | 53060777 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,294,860 | 2,343.758923 | 53060777 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,265,303 | 3,445.976476 | 53060777 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,247,475 | 0.000264 | 53060777 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,222,545 | 65.014830 | 53060777 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,173,674 | 0.000000 | 53060777 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,169,425 | 35,446,293.114047 | 53060777 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,132,682 | 1,126,920.900813 | 53060777 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,127,929 | 491,864.954002 | 53060777 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,065,920 | 55.127535 | 53060777 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,038,437 | 78,319.715505 | 53060777 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,514 | 17.096209 | 53060777 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,037,283 | 21,489,605.354605 | 53060777 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 965,257 | 0.040724 | 53060777 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 950,174 | 17.165105 | 53060777 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/USDC | 10000 | 927,144 | 2,344.953414 | 53060777 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 924,817 | 2.309502 | 53060777 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 907,308 | 1,120.791591 | 53060777 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 900,225 | 0.000551 | 53060777 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 882,149 | 17.853711 | 53060777 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 871,179 | 95.781970 | 53060777 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 849,685 | 2,347.856152 | 53060777 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 813,211 | 0.000008 | 53060777 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 801,675 | 1.105854 | 53060777 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 794,815 | 0.803130 | 53060777 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,431 | 0.055237 | 53060777 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 745,992 | 0.618984 | 53060777 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 744,694 | 4,690,124.288701 | 53060777 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 734,109 | 0.674837 | 53060777 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 719,694 | 133,874.037105 | 53060777 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2111 | 705,130 | 495,044.559836 | 53060777 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 8296 ; routes examinées : 163398016 ; candidats optimisés : 444891 ; net attendu > 0 : 446 ; dernier cycle 87.3 ms
- Rejets (moteur) : {'spread_below_threshold': 160955588, 'liquidity_below_min': 1926606, 'negative_expected_net': 444445, 'pool_quarantined': 43624, 'borrow_bound_too_small': 24166, 'unquotable': 2508, 'cycle_budget_exhausted': 633}
- Enregistrements de la session : 444891 ; net attendu > 0 : 446 ; simulés (eth_call de la vraie tx) : 31 (ok 5, échec 26) ; étiquettes ghost N+1 : 0/30 positives
- Décisions : {'REJECTED': 444891} ; motifs de rejet : {'below_safety_margin': 322, 'negative_expected_net': 444445, 'p_lower_below_threshold': 328, 'price_impact': 2, 'reliability_not_demonstrated': 118, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 26, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53060725 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC | 0.011916 cbBTC | 0.000125 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000125 cbBTC (9.2452 €) | — | 104.62 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 958.596974 USDC | 10.034586 USDC | 0.000000 USDC | 0.007052 USDC | 10.027534 USDC (9.2253 €) | — | 104.61 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53060725 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC | 0.011915 cbBTC | 0.000122 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000122 cbBTC (9.0487 €) | — | 102.41 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC | 0.011915 cbBTC | 0.000122 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000122 cbBTC (9.0368 €) | — | 102.27 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 958.406303 USDC | 9.820367 USDC | 0.000000 USDC | 0.007052 USDC | 9.813315 USDC (9.0282 €) | — | 102.39 | 0.000 (n=18) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 958.596974 USDC | 9.807750 USDC | 0.000000 USDC | 0.007052 USDC | 9.800698 USDC (9.0166 €) | — | 102.24 | 0.000 (n=18) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53060725 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC | 0.011917 cbBTC | 0.000121 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000121 cbBTC (8.9641 €) | — | 101.43 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 958.596974 USDC | 9.727597 USDC | 0.000000 USDC | 0.007052 USDC | 9.720545 USDC (8.9429 €) | — | 101.40 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC | 0.013965 cbBTC | 0.000109 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000109 cbBTC (8.1024 €) | — | 78.24 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 1,123.069202 USDC | 8.793215 USDC | 0.000000 USDC | 0.006728 USDC | 8.786487 USDC (8.0836 €) | — | 78.24 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC | 0.009892 cbBTC | 0.000108 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000108 cbBTC (8.0275 €) | — | 109.43 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 795.426995 USDC | 8.709758 USDC | 0.000000 USDC | 0.007052 USDC | 8.702706 USDC (8.0065 €) | — | 109.41 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC | 0.013107 cbBTC | 0.000104 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000104 cbBTC (7.6879 €) | — | 79.09 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 1,053.859737 USDC | 8.342476 USDC | 0.000000 USDC | 0.006728 USDC | 8.335748 USDC (7.6689 €) | — | 79.10 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC | 0.012973 cbBTC | 0.000103 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000103 cbBTC (7.6434 €) | — | 79.45 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 1,043.466857 USDC | 8.295615 USDC | 0.000000 USDC | 0.006728 USDC | 8.288887 USDC (7.6258 €) | — | 79.44 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC | 0.013229 cbBTC | 0.000103 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000103 cbBTC (7.6174 €) | — | 77.65 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 1,063.750293 USDC | 8.265389 USDC | 0.000000 USDC | 0.006728 USDC | 8.258661 USDC (7.5980 €) | — | 77.64 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC | 0.011922 cbBTC | 0.000102 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000102 cbBTC (7.5781 €) | — | 85.72 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 958.397536 USDC | 8.205027 USDC | 0.000000 USDC | 0.007408 USDC | 8.197619 USDC (7.5418 €) | — | 85.53 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC | 0.010275 cbBTC | 0.000076 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000076 cbBTC (5.6352 €) | — | 73.96 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 823.781781 USDC | 6.098433 USDC | 0.000000 USDC | 0.007084 USDC | 6.091349 USDC (5.6040 €) | — | 73.94 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC | 0.005690 cbBTC | 0.000059 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000059 cbBTC (4.3938 €) | — | 104.14 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 457.177588 USDC | 4.767503 USDC | 0.000000 USDC | 0.006728 USDC | 4.760775 USDC (4.3799 €) | — | 104.13 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[aerodrome]→USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC | 0.003863 cbBTC | 0.000042 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000042 cbBTC (3.1324 €) | — | 109.35 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2384 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
