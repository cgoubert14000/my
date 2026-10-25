# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T09:05:14+00:00 ; durée 265.81 min ; blocs 53056902 → 53064880 (7884 vus)

## Connexion
- Requêtes RPC : 98023 ; erreurs : 5 ; latence p50/p95 : 266.9/934.6 ms
- Rafraîchissements d'état : 7884 ; âge des données au dernier bloc : 2.61 s ; changements de frais LP observés (pools à frais dynamiques) : 8791
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 78115 ; cycles déclenchés par événement : 8722 ; avance médiane sur le rafraîchissement multicall : 461 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,336.90 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 309 jetons, 19696 routes
- Par DEX : uniswap_v3 144, aerodrome 216, aerodrome_slipstream 134, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 349, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2361.63016, 'cbBTC': 80803.612106, 'AERO': 0.690594}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,238,492 | 2,336.904356 | 53064880 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,251,011 | 0.029040 | 53064880 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,229,677 | 0.029106 | 53064880 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,524,285 | 0.000012 | 53064880 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,886,433 | 96.120531 | 53064880 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,423,195 | 2,332.722143 | 53064880 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,588,636 | 1.480610 | 53064880 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,001,919 | 0.001639 | 53064880 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,629,031 | 2,332.730193 | 53064880 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,441,849 | 0.029040 | 53064880 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,428,325 | 2,332.622528 | 53064880 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,234,957 | 0.999704 | 53064880 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,874,398 | 34,448.972655 | 53064880 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,788,405 | 2,337.457585 | 53064880 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,243,666 | 0.029092 | 53064880 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,852,889 | 0.000012 | 53064880 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,498,849 | 96.152198 | 53064880 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,206,801 | 414.549594 | 53064880 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,121,273 | 1,230,433.085261 | 53064880 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,901,301 | 0.000012 | 53064880 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,893,194 | 0.000000 | 53064880 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,781,320 | 0.017886 | 53064880 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,730,484 | 0.000012 | 53064880 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,719,542 | 0.000012 | 53064880 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,568,724 | 0.000265 | 53064880 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53064880 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,722 | 0.827034 | 53064880 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,457,666 | 0.005583 | 53064880 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,424,660 | 3,454.365684 | 53064880 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,364,546 | 14,270.077021 | 53064880 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,288,336 | 2,332.739980 | 53064880 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,256,980 | 3,445.976476 | 53064880 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,240,807 | 0.000263 | 53064880 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,222,545 | 65.014830 | 53064880 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,164,783 | 0.000000 | 53064880 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,164,543 | 35,412,295.627789 | 53064880 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,127,835 | 1,126,428.556634 | 53064880 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,120,938 | 497,334.315182 | 53064880 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,069,864 | 54.721849 | 53064880 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,033,236 | 17.290654 | 53064880 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,032,609 | 21,489,605.354605 | 53064880 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,030,815 | 78,768.634886 | 53064880 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 958,064 | 0.041222 | 53064880 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 925,265 | 2,344.953048 | 53064880 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 920,867 | 2.308722 | 53064880 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 912,227 | 17.186808 | 53064880 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/MORPHO | 3000 | 899,535 | 1,127.153066 | 53064880 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 898,105 | 0.000554 | 53064880 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 875,582 | 18.073433 | 53064880 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 864,501 | 95.781959 | 53064880 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 847,777 | 2,337.115069 | 53064880 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 809,350 | 0.000008 | 53064880 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 791,241 | 0.803130 | 53064880 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 788,453 | 0.055684 | 53064880 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 781,257 | 1.105854 | 53064880 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,353 | 0.612493 | 53064880 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 742,044 | 4,681,308.200067 | 53064880 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 732,739 | 0.672454 | 53064880 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 714,998 | 134,421.963696 | 53064880 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 697,908 | 500,644.426652 | 53064880 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 16605 ; routes examinées : 327052080 ; candidats optimisés : 920934 ; net attendu > 0 : 651 ; dernier cycle 123.0 ms
- Rejets (moteur) : {'spread_below_threshold': 321494233, 'liquidity_below_min': 4380587, 'negative_expected_net': 920283, 'borrow_bound_too_small': 115037, 'pool_quarantined': 80376, 'unquotable': 59068, 'cycle_budget_exhausted': 1845}
- Enregistrements de la session : 920934 ; net attendu > 0 : 651 ; simulés (eth_call de la vraie tx) : 55 (ok 10, échec 45) ; étiquettes ghost N+1 : 0/49 positives
- Décisions : {'REJECTED': 920934} ; motifs de rejet : {'below_safety_margin': 471, 'negative_expected_net': 920283, 'p_lower_below_threshold': 488, 'price_impact': 2, 'reliability_not_demonstrated': 163, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 45, 'stale_data': 12}

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
| 53064382 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 140.249528 USDC | 6.323402 USDC | 0.000000 USDC | 0.004925 USDC | 6.318477 USDC (5.8130 €) | — | 450.52 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53060725 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC | 0.010275 cbBTC | 0.000076 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000076 cbBTC (5.6352 €) | — | 73.96 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 823.781781 USDC | 6.098433 USDC | 0.000000 USDC | 0.007084 USDC | 6.091349 USDC (5.6040 €) | — | 73.94 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53060725 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC | 0.005690 cbBTC | 0.000059 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000059 cbBTC (4.3938 €) | — | 104.14 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53060725 | USDC→[uniswap_v3]→EDGE→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 457.177588 USDC | 4.767503 USDC | 0.000000 USDC | 0.006728 USDC | 4.760775 USDC (4.3799 €) | — | 104.13 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2403 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
