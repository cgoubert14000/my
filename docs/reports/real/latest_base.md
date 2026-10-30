# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T22:53:41+00:00 ; durée 213.64 min ; blocs 53299323 → 53305733 (6317 vus)

## Connexion
- Requêtes RPC : 71627 ; erreurs : 71 ; latence p50/p95 : 131.0/901.8 ms
- Rafraîchissements d'état : 6317 ; âge des données au dernier bloc : 2.23 s ; changements de frais LP observés (pools à frais dynamiques) : 9193
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 35385 ; cycles déclenchés par événement : 2911 ; avance médiane sur le rafraîchissement multicall : 808 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,236.49 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18532 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 112, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3774 (énumérés 315, par paires 0), mesurés 500, sous le plancher de 10000.0 $ : 3 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.87299, 'cbBTC': 76304.747909, 'AERO': 0.609807}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,110,923 | 2,236.493596 | 53305733 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,936,568 | 0.029079 | 53305733 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,221,567 | 0.000013 | 53305733 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,992,410 | 0.029127 | 53305733 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,167,597 | 2,234.007880 | 53305733 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,684,617 | 100.467375 | 53305733 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,666,715 | 0.001627 | 53305733 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,885,799 | 1.607287 | 53305733 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,545,977 | 0.029071 | 53305733 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,134,032 | 2,234.038440 | 53305733 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,064,424 | 2,234.118262 | 53305733 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,045,272 | 1.000000 | 53305733 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,536,626 | 37,427.060712 | 53305733 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,743,157 | 0.029138 | 53305733 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,316,768 | 100.442345 | 53305733 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,050,296 | 1,206,344.208581 | 53305733 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,990,847 | 0.000013 | 53305733 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,762,178 | 0.000000 | 53305733 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,728,288 | 0.017555 | 53305733 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,682,969 | 417.490387 | 53305733 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,611,208 | 0.000013 | 53305733 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,565,804 | 0.000013 | 53305733 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,521,654 | 2,239.196881 | 53305733 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,512,933 | 1.548785 | 53305733 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,460,007 | 0.000013 | 53305733 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,296 | 0.825661 | 53305733 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,405,280 | 3,591.175520 | 53305733 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,310,894 | 2,233.775154 | 53305733 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,303,425 | 14,378.582436 | 53305733 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,278,829 | 0.005001 | 53305733 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,176,971 | 70.147259 | 53305733 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,107,096 | 36,186,923.289493 | 53305733 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,056,041 | 514,273.609833 | 53305733 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,030,705 | 21,173,050.588630 | 53305733 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,020,254 | 0.000000 | 53305733 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,013,930 | 74,307.075401 | 53305733 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,008,332 | 2,237.049289 | 53305733 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,004,002 | 18.734296 | 53305733 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 964,912 | 101.175480 | 53305733 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 963,066 | 67.495460 | 53305733 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 947,116 | 0.044970 | 53305733 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 923,026 | 1,227,489.491195 | 53305733 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 919,798 | 2,235.963227 | 53305733 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 891,096 | 1,076.441891 | 53305733 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,029 | 0.000557 | 53305733 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 861,466 | 3,612.674591 | 53305733 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 835,249 | 19.527948 | 53305733 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 818,030 | 0.060153 | 53305733 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 757,054 | 0.803531 | 53305733 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 737,592 | 0.000267 | 53305733 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 727,435 | 0.599721 | 53305733 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 726,000 | 4,483,351.007886 | 53305733 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 678,978 | 0.000008 | 53305733 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 678,741 | 2.331396 | 53305733 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 655,826 | 510,270.922388 | 53305733 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 653,314 | 147,761.685326 | 53305733 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 631,696 | 0.504492 | 53305733 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 613,480 | 0.093324 | 53305733 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 601,394 | 0.914964 | 53305733 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 540,309 | 1,075.798012 | 53305733 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 9227 ; routes examinées : 170994764 ; candidats optimisés : 700880 ; net attendu > 0 : 350 ; dernier cycle 261.7 ms
- Rejets (moteur) : {'spread_below_threshold': 167777825, 'liquidity_below_min': 2474852, 'negative_expected_net': 700530, 'unquotable': 28912, 'borrow_bound_too_small': 9217, 'pool_quarantined': 2340, 'cycle_budget_exhausted': 738}
- Enregistrements de la session : 700880 ; net attendu > 0 : 350 ; simulés (eth_call de la vraie tx) : 19 (ok 9, échec 10) ; étiquettes ghost N+1 : 0/19 positives
- Décisions : {'REJECTED': 700880} ; motifs de rejet : {'below_safety_margin': 274, 'negative_expected_net': 700530, 'p_lower_below_threshold': 325, 'reliability_not_demonstrated': 25, 'simulation_failed': 10, 'stale_data': 17}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53304483 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 194.189460 USDC | 0.881802 USDC | 0.000000 USDC | 0.005026 USDC | 0.876776 USDC (0.8066 €) | — | 45.15 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53302962 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.002481 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3587 €) | — | 20.52 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53302962 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 191.105100 USDC | 0.396516 USDC | 0.000000 USDC | 0.006734 USDC | 0.389782 USDC (0.3586 €) | — | 20.40 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53302962 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 172.900069 USDC | 0.342781 USDC | 0.000000 USDC | 0.006734 USDC | 0.336047 USDC (0.3092 €) | — | 19.44 | 0.017 (n=82) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53302962 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.002223 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3086 €) | — | 19.70 | 0.017 (n=82) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53302962 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 158.414428 USDC | 0.284367 USDC | 0.000000 USDC | 0.006734 USDC | 0.277633 USDC (0.2554 €) | — | 17.53 | 0.017 (n=82) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53302962 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.001978 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2551 €) | — | 18.30 | 0.017 (n=82) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53302962 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.002061 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2523 €) | — | 17.37 | 0.017 (n=82) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53302962 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 157.940864 USDC | 0.280575 USDC | 0.000000 USDC | 0.006734 USDC | 0.273841 USDC (0.2519 €) | — | 17.34 | 0.017 (n=82) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53302962 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.001808 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2135 €) | — | 16.76 | 0.058 (n=88) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53302962 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 143.643991 USDC | 0.238317 USDC | 0.000000 USDC | 0.006734 USDC | 0.231583 USDC (0.2131 €) | — | 16.12 | 0.058 (n=88) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53302962 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDC | 145.581723 USDC | 0.118473 USDC | 0.000000 USDC | 0.004724 USDC | 0.113749 USDC (0.1046 €) | — | 7.81 | 0.105 (n=42) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53299663 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 852.704355 USDC | 0.105755 USDC | 0.000000 USDC | 0.007061 USDC | 0.098694 USDC (0.0908 €) | — | 1.16 | 0.001 (n=15) | REJECTED | below_safety_margin(98694<170540), reliability_not_demonstrated |
| 53299663 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.378616 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0907 €) | — | 1.17 | 0.001 (n=15) | REJECTED | below_safety_margin(44325697852444<75723270317330), reliability_not_demonstrated |
| 53299663 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.011165 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0906 €) | — | 1.16 | 0.001 (n=15) | REJECTED | below_safety_margin(129<223), reliability_not_demonstrated |
| 53299663 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.009073 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0653 €) | — | 1.03 | 0.145 (n=645) | REJECTED | below_safety_margin(93<181), p_lower_below_threshold(0.14<0.75) |
| 53299663 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 763.278000 USDC | 0.077483 USDC | 0.000000 USDC | 0.006723 USDC | 0.070760 USDC (0.0651 €) | — | 0.93 | 0.145 (n=645) | REJECTED | below_safety_margin(70760<152655), p_lower_below_threshold(0.14<0.75) |
| 53299663 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.342793 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0651 €) | — | 0.93 | 0.145 (n=645) | REJECTED | below_safety_margin(31776587749514<68558667203723), p_lower_below_threshold(0.14<0.75) |
| 53304483 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 26.187326 USDC | 0.070007 USDC | 0.000000 USDC | 0.004717 USDC | 0.065290 USDC (0.0601 €) | — | 24.93 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53302962 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.039551 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0559 €) | 0.000027 WETH | 6.87 | 0.120 (n=482) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53302962 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.001046 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0557 €) | — | 7.55 | 0.120 (n=482) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53302962 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 88.436807 USDC | 0.063960 USDC | 0.000000 USDC | 0.006734 USDC | 0.057226 USDC (0.0526 €) | — | 6.47 | 0.120 (n=482) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53302962 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.039609 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0526 €) | 0.000026 WETH | 6.45 | 0.120 (n=482) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53303136 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 222.899039 USDC | 0.062779 USDC | 0.000000 USDC | 0.006425 USDC | 0.056354 USDC (0.0518 €) | 0.056354 USDC | 2.53 | 0.292 (n=78) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53303136 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.099579 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0517 €) | 0.000025 WETH | 2.53 | 0.292 (n=78) | REJECTED | p_lower_below_threshold(0.29<0.75) |

## Fiabilité et décision
- Observations ghost : 3891 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
