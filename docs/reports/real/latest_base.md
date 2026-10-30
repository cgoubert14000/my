# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T21:01:16+00:00 ; durée 101.21 min ; blocs 53299323 → 53302362 (3004 vus)

## Connexion
- Requêtes RPC : 34699 ; erreurs : 15 ; latence p50/p95 : 228.9/1,541.7 ms
- Rafraîchissements d'état : 3005 ; âge des données au dernier bloc : 1.74 s ; changements de frais LP observés (pools à frais dynamiques) : 4620
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 20123 ; cycles déclenchés par événement : 1437 ; avance médiane sur le rafraîchissement multicall : 927 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,236.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18532 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 112, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3774 (énumérés 315, par paires 0), mesurés 500, sous le plancher de 10000.0 $ : 3 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.87299, 'cbBTC': 76304.747909, 'AERO': 0.609807}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,044,400 | 2,236.542615 | 53302362 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,927,393 | 0.029109 | 53302362 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,196,927 | 0.000013 | 53302362 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,990,166 | 0.029112 | 53302362 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,168,516 | 2,236.391155 | 53302362 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,659,536 | 101.130831 | 53302362 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,640,495 | 0.001617 | 53302362 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,844,708 | 1.631771 | 53302362 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,541,189 | 0.029118 | 53302362 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,134,533 | 2,237.063970 | 53302362 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,060,996 | 2,237.146606 | 53302362 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,044,618 | 0.998959 | 53302362 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,526,429 | 37,645.469783 | 53302362 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,742,455 | 0.029113 | 53302362 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,308,184 | 101.185594 | 53302362 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,050,341 | 1,206,344.208581 | 53302362 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,939,900 | 0.000013 | 53302362 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,760,736 | 0.000000 | 53302362 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,716,137 | 0.017355 | 53302362 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,676,175 | 422.460001 | 53302362 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,624,990 | 0.000013 | 53302362 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,565,408 | 0.000013 | 53302362 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,521,631 | 2,242.337528 | 53302362 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,512,933 | 1.548785 | 53302362 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,458,749 | 0.000013 | 53302362 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,912 | 0.825659 | 53302362 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,392,620 | 3,650.211722 | 53302362 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,310,845 | 2,236.298415 | 53302362 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,296,326 | 14,512.937691 | 53302362 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,270,223 | 0.004960 | 53302362 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,176,991 | 70.144871 | 53302362 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,104,871 | 36,408,839.921413 | 53302362 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,053,772 | 517,368.937121 | 53302362 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,035,141 | 21,015,971.546121 | 53302362 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,018,946 | 0.000000 | 53302362 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,013,666 | 74,349.024537 | 53302362 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,008,342 | 2,235.637213 | 53302362 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,078 | 19.331177 | 53302362 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 977,692 | 65.491125 | 53302362 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 960,859 | 101.211583 | 53302362 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 941,345 | 0.045195 | 53302362 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 920,949 | 1,233,081.833906 | 53302362 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 919,806 | 2,235.963227 | 53302362 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 884,413 | 1,087.920178 | 53302362 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,273 | 0.000555 | 53302362 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 854,989 | 3,628.639242 | 53302362 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 831,040 | 19.676783 | 53302362 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 812,061 | 0.059221 | 53302362 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 757,071 | 0.803531 | 53302362 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 734,490 | 0.000264 | 53302362 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 722,815 | 4,522,982.500072 | 53302362 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 722,764 | 0.591571 | 53302362 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 678,756 | 2.331396 | 53302362 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 672,526 | 0.000008 | 53302362 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2132 | 653,765 | 516,602.613571 | 53302362 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 653,091 | 147,869.087577 | 53302362 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 629,569 | 0.501273 | 53302362 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 606,833 | 0.091787 | 53302362 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 601,372 | 0.915071 | 53302362 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2724 | 537,140 | 1,087.469402 | 53302362 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 4441 ; routes examinées : 82300612 ; candidats optimisés : 363568 ; net attendu > 0 : 231 ; dernier cycle 432.2 ms
- Rejets (moteur) : {'spread_below_threshold': 80783361, 'liquidity_below_min': 1134890, 'negative_expected_net': 363337, 'unquotable': 14156, 'borrow_bound_too_small': 4438, 'cycle_budget_exhausted': 199}
- Enregistrements de la session : 363568 ; net attendu > 0 : 231 ; simulés (eth_call de la vraie tx) : 8 (ok 3, échec 5) ; étiquettes ghost N+1 : 0/8 positives
- Décisions : {'REJECTED': 363568} ; motifs de rejet : {'below_safety_margin': 217, 'negative_expected_net': 363337, 'p_lower_below_threshold': 216, 'reliability_not_demonstrated': 15, 'simulation_failed': 5, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53299663 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 852.704355 USDC | 0.105755 USDC | 0.000000 USDC | 0.007061 USDC | 0.098694 USDC (0.0908 €) | — | 1.16 | 0.001 (n=15) | REJECTED | below_safety_margin(98694<170540), reliability_not_demonstrated |
| 53299663 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.378616 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0907 €) | — | 1.17 | 0.001 (n=15) | REJECTED | below_safety_margin(44325697852444<75723270317330), reliability_not_demonstrated |
| 53299663 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.011165 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0906 €) | — | 1.16 | 0.001 (n=15) | REJECTED | below_safety_margin(129<223), reliability_not_demonstrated |
| 53299663 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.009073 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0653 €) | — | 1.03 | 0.145 (n=645) | REJECTED | below_safety_margin(93<181), p_lower_below_threshold(0.14<0.75) |
| 53299663 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 763.278000 USDC | 0.077483 USDC | 0.000000 USDC | 0.006723 USDC | 0.070760 USDC (0.0651 €) | — | 0.93 | 0.145 (n=645) | REJECTED | below_safety_margin(70760<152655), p_lower_below_threshold(0.14<0.75) |
| 53299663 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.342793 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0651 €) | — | 0.93 | 0.145 (n=645) | REJECTED | below_safety_margin(31776587749514<68558667203723), p_lower_below_threshold(0.14<0.75) |
| 53299923 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000781 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0148 €) | — | 2.69 | 0.145 (n=645) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53299923 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 60.638004 USDC | 0.022255 USDC | 0.000000 USDC | 0.006713 USDC | 0.015542 USDC (0.0143 €) | — | 2.56 | 0.145 (n=645) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53299663 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 166.887928 USDC | 0.019728 USDC | 0.000000 USDC | 0.006723 USDC | 0.013005 USDC (0.0120 €) | — | 0.78 | 0.145 (n=645) | REJECTED | below_safety_margin(13005<33377), p_lower_below_threshold(0.14<0.75) |
| 53299663 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001844 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0119 €) | — | 0.92 | 0.145 (n=645) | REJECTED | below_safety_margin(17<36), p_lower_below_threshold(0.14<0.75) |
| 53299663 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.081701 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0117 €) | — | 0.70 | 0.145 (n=645) | REJECTED | below_safety_margin(5702577909032<16340267270861), p_lower_below_threshold(0.14<0.75) |
| 53299923 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000623 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0105 €) | — | 2.41 | 0.145 (n=645) | REJECTED | stale_data(4272ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 53299923 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.023706 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0105 €) | — | 2.17 | 0.145 (n=645) | REJECTED | stale_data(4265ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53301213 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.046057 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0098 €) | — | 1.03 | 0.144 (n=648) | REJECTED | below_safety_margin(4758278363656<9211405688239), stale_data(4239ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 53301214 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.046083 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0098 €) | — | 1.03 | 0.144 (n=648) | REJECTED | below_safety_margin(4758180758158<9216585585063), p_lower_below_threshold(0.14<0.75) |
| 53301214 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 101.687668 USDC | 0.017356 USDC | 0.000000 USDC | 0.006736 USDC | 0.010620 USDC (0.0098 €) | — | 1.04 | 0.144 (n=648) | REJECTED | below_safety_margin(10620<20337), p_lower_below_threshold(0.14<0.75) |
| 53301213 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 102.096753 USDC | 0.017356 USDC | 0.000000 USDC | 0.006736 USDC | 0.010620 USDC (0.0098 €) | — | 1.04 | 0.144 (n=648) | REJECTED | below_safety_margin(10620<20419), stale_data(4247ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 53300577 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 75.260200 USDC | 0.016845 USDC | 0.000000 USDC | 0.006733 USDC | 0.010112 USDC (0.0093 €) | — | 1.34 | 0.144 (n=648) | REJECTED | below_safety_margin(10112<15052), p_lower_below_threshold(0.14<0.75) |
| 53300577 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.033908 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0093 €) | — | 1.33 | 0.144 (n=648) | REJECTED | below_safety_margin(4505248457028<6781502356572), p_lower_below_threshold(0.14<0.75) |
| 53300577 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 81.295563 USDC | 0.016330 USDC | 0.000000 USDC | 0.006733 USDC | 0.009597 USDC (0.0088 €) | — | 1.18 | 0.144 (n=648) | REJECTED | below_safety_margin(9597<16259), p_lower_below_threshold(0.14<0.75) |
| 53300577 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.036567 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0088 €) | — | 1.17 | 0.144 (n=648) | REJECTED | below_safety_margin(4274490304938<7313335920581), p_lower_below_threshold(0.14<0.75) |
| 53300577 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 74.498972 USDC | 0.016186 USDC | 0.000000 USDC | 0.006733 USDC | 0.009453 USDC (0.0087 €) | — | 1.27 | 0.144 (n=648) | REJECTED | below_safety_margin(9453<14899), p_lower_below_threshold(0.14<0.75) |
| 53300577 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.033308 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0087 €) | — | 1.26 | 0.144 (n=648) | REJECTED | below_safety_margin(4210533599417<6661575634718), p_lower_below_threshold(0.14<0.75) |
| 53300579 | USDC→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 99.528716 USDC | 0.016085 USDC | 0.000000 USDC | 0.006741 USDC | 0.009344 USDC (0.0086 €) | — | 0.94 | 0.144 (n=648) | REJECTED | below_safety_margin(9344<19905), p_lower_below_threshold(0.14<0.75) |
| 53299923 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000767 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0084 €) | — | 1.56 | 0.145 (n=645) | REJECTED | below_safety_margin(12<15), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3880 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
