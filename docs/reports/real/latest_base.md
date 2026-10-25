# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T21:41:20+00:00 ; durée 15.22 min ; blocs 53087107 → 53087566 (457 vus)

## Connexion
- Requêtes RPC : 5611 ; erreurs : 0 ; latence p50/p95 : 111.2/1,350.2 ms
- Rafraîchissements d'état : 457 ; âge des données au dernier bloc : 2.45 s ; changements de frais LP observés (pools à frais dynamiques) : 405
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4229 ; cycles déclenchés par événement : 654 ; avance médiane sur le rafraîchissement multicall : 427 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,341.93 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 533 pools, 308 jetons, 19442 routes
- Par DEX : uniswap_v3 143, aerodrome 214, aerodrome_slipstream 129, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 192 (rejetés 2) → 597 jetons ; pools candidats 3802 (énumérés 342, par paires 0), mesurés 535, sous le plancher de 10000.0 $ : 2 → gardés 533 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2341.931042, 'cbBTC': 80341.676682, 'AERO': 0.683871}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,452,294 | 2,341.931981 | 53087565 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,506,870 | 0.029091 | 53087565 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,240,740 | 0.029142 | 53087565 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,599,696 | 0.000012 | 53087565 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,957,371 | 92.650332 | 53087565 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,437,970 | 2,336.561107 | 53087565 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,477,378 | 1.465892 | 53087565 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,023,886 | 0.001648 | 53087565 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 654 | 5,496,628 | 2,336.185482 | 53087566 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,362,589 | 0.029083 | 53087566 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,459,466 | 2,336.316044 | 53087566 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,232,080 | 1.000002 | 53087565 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,833,757 | 34,928.981632 | 53087565 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,785,312 | 2,341.665857 | 53087565 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,232,097 | 0.029147 | 53087565 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,526,032 | 0.000012 | 53087565 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,523,382 | 92.665329 | 53087565 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,217,194 | 410.309330 | 53087565 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,137,192 | 1,217,392.988104 | 53087565 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,898,751 | 0.000000 | 53087565 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,898,506 | 0.000012 | 53087565 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,802,795 | 0.018047 | 53087565 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,720,339 | 0.000012 | 53087565 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,720,162 | 0.000012 | 53087565 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,572,129 | 0.000265 | 53087565 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,135 | 0.825585 | 53087565 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53087565 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,438,079 | 0.005542 | 53087565 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,434,163 | 3,424.468882 | 53087565 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,371,783 | 14,095.859200 | 53087565 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,288,832 | 2,336.520574 | 53087565 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,256,225 | 3,400.687041 | 53087565 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,244,434 | 0.000267 | 53087565 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,956 | 65.077583 | 53087565 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,166,669 | 35,446,952.567842 | 53087565 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,163,642 | 0.000000 | 53087565 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,138,531 | 1,110,125.497084 | 53087565 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,125,594 | 495,965.952575 | 53087565 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,092,866 | 52.442722 | 53087565 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,069,628 | 73,462.980009 | 53087565 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,036,832 | 17.128720 | 53087565 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,022,346 | 21,969,859.621726 | 53087565 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 972,889 | 0.039649 | 53087565 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 925,857 | 2,339.202029 | 53087565 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 917,369 | 2.311225 | 53087565 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 912,365 | 1,133.385667 | 53087565 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 898,213 | 0.000551 | 53087565 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 890,593 | 17.088102 | 53087565 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/VVV | 10000 | 880,304 | 91.982332 | 53087565 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 876,215 | 18.056487 | 53087565 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 848,712 | 2,341.993575 | 53087565 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 805,286 | 0.000008 | 53087565 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 792,943 | 0.803130 | 53087565 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 790,014 | 0.055914 | 53087565 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 782,938 | 1.105853 | 53087565 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 746,924 | 0.623650 | 53087565 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 736,034 | 4,778,980.419635 | 53087565 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 719,682 | 0.649982 | 53087565 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 717,335 | 134,137.490291 | 53087565 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 700,414 | 496,007.629302 | 53087565 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 1110 ; routes examinées : 21580620 ; candidats optimisés : 61780 ; net attendu > 0 : 32 ; dernier cycle 247.7 ms
- Rejets (moteur) : {'spread_below_threshold': 21086377, 'liquidity_below_min': 406933, 'negative_expected_net': 61748, 'unquotable': 24420, 'borrow_bound_too_small': 1110}
- Enregistrements de la session : 61780 ; net attendu > 0 : 32 ; simulés (eth_call de la vraie tx) : 6 (ok 2, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 61780} ; motifs de rejet : {'below_safety_margin': 26, 'negative_expected_net': 61748, 'p_lower_below_threshold': 30, 'reliability_not_demonstrated': 2, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53087522 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.016486 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1666 €) | — | 1.36 | 0.129 (n=327) | REJECTED | below_safety_margin(225<329), p_lower_below_threshold(0.13<0.75) |
| 53087522 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.577121 WETH | 0.000080 WETH | 0.000000 WETH | 0.000003 WETH | 0.000077 WETH (0.1663 €) | — | 1.34 | 0.129 (n=327) | REJECTED | below_safety_margin(77178992824150<115424216900843), p_lower_below_threshold(0.13<0.75) |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,348.818293 USDC | 0.188160 USDC | 0.000000 USDC | 0.007747 USDC | 0.180413 USDC (0.1660 €) | — | 1.34 | 0.129 (n=327) | REJECTED | below_safety_margin(180413<269763), p_lower_below_threshold(0.13<0.75) |
| 53087522 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.292631 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0222 €) | — | 0.35 | 0.022 (n=94) | REJECTED | below_safety_margin(10323917283576<58526124130582), p_lower_below_threshold(0.02<0.75) |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 683.278827 USDC | 0.029382 USDC | 0.000000 USDC | 0.005257 USDC | 0.024125 USDC (0.0222 €) | — | 0.35 | 0.022 (n=94) | REJECTED | below_safety_margin(24125<136655), p_lower_below_threshold(0.02<0.75) |
| 53087522 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.099667 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0193 €) | — | 0.90 | 0.018 (n=16) | REJECTED | below_safety_margin(8977677215883<19933430314713), reliability_not_demonstrated |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 230.551841 USDC | 0.026234 USDC | 0.000000 USDC | 0.005257 USDC | 0.020977 USDC (0.0193 €) | — | 0.91 | 0.018 (n=16) | REJECTED | below_safety_margin(20977<46110), reliability_not_demonstrated |
| 53087522 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.001314 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0074 €) | — | 0.76 | 0.129 (n=327) | REJECTED | below_safety_margin(10<26), p_lower_below_threshold(0.13<0.75) |
| 53087522 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.051452 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0074 €) | — | 0.66 | 0.129 (n=327) | REJECTED | below_safety_margin(3418979276331<10290429459934), p_lower_below_threshold(0.13<0.75) |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 117.133329 USDC | 0.014869 USDC | 0.000000 USDC | 0.007036 USDC | 0.007833 USDC (0.0072 €) | — | 0.67 | 0.129 (n=327) | REJECTED | below_safety_margin(7833<23426), p_lower_below_threshold(0.13<0.75) |
| 53087553 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004312 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 2.58 | 0.199 (n=158) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 53087553 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.019246 USDC | 0.009622 USDC | 0.000000 USDC | 0.007037 USDC | 0.002585 USDC (0.0024 €) | — | 2.58 | 0.199 (n=158) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 53087552 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004262 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | -0.000003 WETH | 2.50 | 0.199 (n=158) | REJECTED | sim_below_estimate(240799736155<4071100489212), simulated_net_nonpositive, p_lower_below_threshold(0.20<0.75) |
| 53087552 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.919670 USDC | 0.009514 USDC | 0.000000 USDC | 0.007037 USDC | 0.002477 USDC (0.0023 €) | -0.006439 USDC | 2.50 | 0.199 (n=158) | REJECTED | sim_below_estimate(598<9514), simulated_net_nonpositive, p_lower_below_threshold(0.20<0.75) |
| 53087556 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004584 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0022 €) | — | 2.21 | 0.197 (n=160) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 53087556 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.564839 USDC | 0.009381 USDC | 0.000000 USDC | 0.007036 USDC | 0.002345 USDC (0.0022 €) | — | 2.22 | 0.197 (n=160) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 53087553 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004515 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 1.90 | 0.129 (n=327) | REJECTED | below_safety_margin(859481066685<902906530470), p_lower_below_threshold(0.13<0.75) |
| 53087553 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004458 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 1.92 | 0.199 (n=158) | REJECTED | below_safety_margin(856545294788<891543210658), p_lower_below_threshold(0.20<0.75) |
| 53087553 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.452609 USDC | 0.009030 USDC | 0.000000 USDC | 0.007037 USDC | 0.001993 USDC (0.0018 €) | — | 1.91 | 0.129 (n=327) | REJECTED | below_safety_margin(1993<2090), p_lower_below_threshold(0.13<0.75) |
| 53087553 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.432528 USDC | 0.009024 USDC | 0.000000 USDC | 0.007037 USDC | 0.001987 USDC (0.0018 €) | — | 1.90 | 0.199 (n=158) | REJECTED | below_safety_margin(1987<2086), p_lower_below_threshold(0.20<0.75) |
| 53087552 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004445 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 1.83 | 0.129 (n=327) | REJECTED | below_safety_margin(811408878912<889016593317), p_lower_below_threshold(0.13<0.75) |
| 53087552 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.393780 USDC | 0.008918 USDC | 0.000000 USDC | 0.007037 USDC | 0.001881 USDC (0.0017 €) | — | 1.81 | 0.129 (n=327) | REJECTED | below_safety_margin(1881<2078), p_lower_below_threshold(0.13<0.75) |
| 53087553 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004437 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 1.76 | 0.199 (n=158) | REJECTED | below_safety_margin(781713098282<887381202757), p_lower_below_threshold(0.20<0.75) |
| 53087553 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.318488 USDC | 0.008849 USDC | 0.000000 USDC | 0.007037 USDC | 0.001812 USDC (0.0017 €) | — | 1.76 | 0.199 (n=158) | REJECTED | below_safety_margin(1812<2063), p_lower_below_threshold(0.20<0.75) |
| 53087552 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.66 | 0.199 (n=158) | REJECTED | below_safety_margin(734215437870<882019180932), p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 2542 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
