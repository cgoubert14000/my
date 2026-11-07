# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T12:40:15+00:00 ; durée 311.72 min ; blocs 54230643 → 54324123 (15564 vus)

## Connexion
- Requêtes RPC : 198651 ; erreurs : 300 ; latence p50/p95 : 236.2/1,789.9 ms
- Rafraîchissements d'état : 15564 ; âge des données au dernier bloc : 8.87 s ; changements de frais LP observés (pools à frais dynamiques) : 4998
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4588 ; cycles déclenchés par événement : 2012 ; avance médiane sur le rafraîchissement multicall : 437 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,242.47 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 476 pools, 279 jetons, 17784 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 99, aerodrome 198, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 170 (rejetés 2) → 575 jetons ; pools candidats 3720 (énumérés 295, par paires 0), mesurés 479, sous le plancher de 10000.0 $ : 3 → gardés 476 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2241.234025, 'cbBTC': 75952.6335, 'AERO': 0.608777}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,085,052 | 2,242.465699 | 54324147 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,820,497 | 0.029527 | 54324147 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,348,680 | 0.000013 | 54324147 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,193,920 | 0.029513 | 54324147 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,087,343 | 2,241.122310 | 54324147 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,396,161 | 107.425695 | 54324147 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,427,060 | 0.001550 | 54324147 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,836,888 | 1.676985 | 54324147 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,773,501 | 0.029532 | 54324147 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,229,842 | 2,240.407653 | 54324147 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,996,115 | 0.999829 | 54324147 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,322,834 | 42,623.541659 | 54324147 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,204,253 | 2,240.027870 | 54324147 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,559,341 | 0.029529 | 54324147 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,101,174 | 1,154,578.522736 | 54324147 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,743,001 | 0.000013 | 54324147 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,670,318 | 0.000000 | 54324147 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,663,994 | 0.006573 | 54324147 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,636,605 | 0.000013 | 54324147 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,605,424 | 0.015969 | 54324147 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,527,694 | 439.845682 | 54324147 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,509,957 | 0.000013 | 54324147 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,481,374 | 1.493422 | 54324147 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,301 | 0.819432 | 54324147 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,374,937 | 3,756.836046 | 54324147 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,327,092 | 2,246.897446 | 54324147 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,325,364 | 2,243.389452 | 54324147 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,269,684 | 14,865.017060 | 54324147 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,205,676 | 2,241.320852 | 54324147 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,702 | 76.955062 | 54324147 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,111,222 | 36,023,806.755343 | 54324147 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,052,065 | 107.611816 | 54324147 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,024,720 | 562,580.563580 | 54324147 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,003,047 | 0.000000 | 54324147 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 998,821 | 22,537,302.896047 | 54324147 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 992,812 | 19.348297 | 54324147 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 944,492 | 1,055.662242 | 54324147 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,072 | 2,228.788739 | 54324147 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 927,231 | 0.000013 | 54324147 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 917,202 | 74.486558 | 54324147 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 876,345 | 99,884.968619 | 54324147 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 811,990 | 0.047965 | 54324147 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 795,639 | 21.056579 | 54324147 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 793,652 | 3,730.217456 | 54324147 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,481 | 0.056065 | 54324147 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,748 | 0.799699 | 54324147 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 721,205 | 0.565894 | 54324147 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,056 | 4,940,366.767476 | 54324147 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 685,711 | 0.000253 | 54324147 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 683,014 | 0.583423 | 54324147 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 658,950 | 146,401.360874 | 54324147 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 649,902 | 0.000008 | 54324147 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 628,057 | 567,110.723780 | 54324147 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 589,114 | 2.473976 | 54324147 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 576,540 | 0.039669 | 54324147 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 530,731 | 1,055.404746 | 54324147 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 525,493 | 0.078676 | 54324147 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 515,268 | 923,023.227143 | 54324147 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 513,431 | 2,240.493609 | 54324147 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 513,281 | 6,999.666069 | 54324147 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 17575 ; routes examinées : 312553800 ; candidats optimisés : 750647 ; net attendu > 0 : 176 ; dernier cycle 131.3 ms
- Rejets (moteur) : {'spread_below_threshold': 308745253, 'liquidity_below_min': 3039005, 'negative_expected_net': 750471, 'borrow_bound_too_small': 17553, 'cycle_budget_exhausted': 1342}
- Enregistrements de la session : 750647 ; net attendu > 0 : 176 ; simulés (eth_call de la vraie tx) : 26 (ok 19, échec 7) ; étiquettes ghost N+1 : 2/21 positives
- Décisions : {'REJECTED': 750647} ; motifs de rejet : {'below_safety_margin': 150, 'negative_expected_net': 750471, 'p_lower_below_threshold': 176, 'simulation_failed': 7, 'stale_data': 43}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54246318 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 27.735293 USDC | 0.020597 USDC | 0.000000 USDC | 0.005033 USDC | 0.015564 USDC (0.0143 €) | 0.015564 USDC | 5.61 | 0.025 (n=329) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54315763 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 21.134228 USDC | 0.019157 USDC | 0.000000 USDC | 0.005035 USDC | 0.014122 USDC (0.0130 €) | 0.014122 USDC | 6.68 | 0.072 (n=94) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54279992 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 222.859116 USDC | 0.018633 USDC | 0.000000 USDC | 0.005082 USDC | 0.013551 USDC (0.0125 €) | — | 0.61 | 0.045 (n=256) | REJECTED | below_safety_margin(13551<44571), p_lower_below_threshold(0.05<0.75) |
| 54279992 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.099719 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0124 €) | — | 0.61 | 0.045 (n=256) | REJECTED | below_safety_margin(6033296570905<19943787764438), p_lower_below_threshold(0.05<0.75) |
| 54323456 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 25.934652 USDC | 0.018127 USDC | 0.000000 USDC | 0.005037 USDC | 0.013090 USDC (0.0120 €) | 0.013090 USDC | 5.05 | 0.025 (n=336) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 54299518 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 38.165777 USDC | 0.017147 USDC | 0.000000 USDC | 0.005037 USDC | 0.012110 USDC (0.0111 €) | 0.012110 USDC | 3.17 | 0.025 (n=333) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 54266291 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 24.463190 USDC | 0.016058 USDC | 0.000000 USDC | 0.005035 USDC | 0.011023 USDC (0.0101 €) | — | 4.51 | 0.025 (n=331) | REJECTED | stale_data(4867ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54308391 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 37.212887 USDC | 0.015713 USDC | 0.000000 USDC | 0.005035 USDC | 0.010678 USDC (0.0098 €) | 0.010678 USDC | 2.87 | 0.045 (n=256) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54290256 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.906654 USDC | 0.015688 USDC | 0.000000 USDC | 0.005035 USDC | 0.010653 USDC (0.0098 €) | 0.010653 USDC | 4.46 | 0.025 (n=332) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 54322641 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 238.511721 USDC | 0.014871 USDC | 0.000000 USDC | 0.005037 USDC | 0.009834 USDC (0.0090 €) | — | 0.41 | 0.052 (n=84) | REJECTED | below_safety_margin(9834<47702), p_lower_below_threshold(0.05<0.75) |
| 54322642 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 238.511721 USDC | 0.014871 USDC | 0.000000 USDC | 0.005037 USDC | 0.009834 USDC (0.0090 €) | — | 0.41 | 0.052 (n=84) | REJECTED | below_safety_margin(9834<47702), p_lower_below_threshold(0.05<0.75) |
| 54231076 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.543309 USDC | 0.014681 USDC | 0.000000 USDC | 0.005032 USDC | 0.009649 USDC (0.0089 €) | 0.009649 USDC | 4.10 | 0.025 (n=328) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54231076 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.543309 USDC | 0.014681 USDC | 0.000000 USDC | 0.005032 USDC | 0.009649 USDC (0.0089 €) | — | 4.10 | 0.025 (n=328) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54274531 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDbC→[aerodrome_slipstream]→USDC | 32.331815 USDC | 0.015477 USDC | 0.000000 USDC | 0.006429 USDC | 0.009048 USDC (0.0083 €) | 0.009048 USDC | 2.80 | 0.212 (n=192) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 54270937 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→wstETH→[uniswap_v3]→WETH | 0.009427 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0077 €) | 0.000004 WETH | 3.94 | 0.279 (n=167) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54322641 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 154.078497 USDC | 0.012497 USDC | 0.000000 USDC | 0.005037 USDC | 0.007460 USDC (0.0069 €) | — | 0.48 | 0.052 (n=84) | REJECTED | below_safety_margin(7460<30815), p_lower_below_threshold(0.05<0.75) |
| 54322642 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 154.078497 USDC | 0.012497 USDC | 0.000000 USDC | 0.005037 USDC | 0.007460 USDC (0.0069 €) | — | 0.48 | 0.052 (n=84) | REJECTED | below_safety_margin(7460<30815), p_lower_below_threshold(0.05<0.75) |
| 54270937 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→wstETH→[aerodrome_slipstream]→WETH | 0.008987 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0065 €) | 0.000003 WETH | 3.49 | 0.279 (n=167) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54301558 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 21.031316 USDC | 0.011999 USDC | 0.000000 USDC | 0.005036 USDC | 0.006963 USDC (0.0064 €) | 0.006963 USDC | 3.31 | 0.025 (n=334) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 54310372 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 31.603954 USDC | 0.011463 USDC | 0.000000 USDC | 0.005035 USDC | 0.006428 USDC (0.0059 €) | — | 2.03 | 0.045 (n=258) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54310373 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 31.603954 USDC | 0.011463 USDC | 0.000000 USDC | 0.005035 USDC | 0.006428 USDC (0.0059 €) | 0.006428 USDC | 2.03 | 0.048 (n=259) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54249134 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.515326 USDC | 0.011356 USDC | 0.000000 USDC | 0.005036 USDC | 0.006320 USDC (0.0058 €) | 0.006320 USDC | 3.08 | 0.025 (n=330) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54249134 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.515326 USDC | 0.011356 USDC | 0.000000 USDC | 0.005036 USDC | 0.006320 USDC (0.0058 €) | — | 3.08 | 0.025 (n=330) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54314368 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.356316 USDC | 0.011323 USDC | 0.000000 USDC | 0.005035 USDC | 0.006288 USDC (0.0058 €) | — | 3.09 | 0.025 (n=335) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 54314369 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.356316 USDC | 0.011323 USDC | 0.000000 USDC | 0.005035 USDC | 0.006288 USDC (0.0058 €) | — | 3.09 | 0.025 (n=336) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 5976 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
