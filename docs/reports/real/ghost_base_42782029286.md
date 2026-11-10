# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T13:42:20+00:00 ; durée 315.9 min ; blocs 55544026 → 55638751 (16522 vus)

## Connexion
- Requêtes RPC : 232753 ; erreurs : 113 ; latence p50/p95 : 241.3/956.2 ms
- Rafraîchissements d'état : 16522 ; âge des données au dernier bloc : 8.22 s ; changements de frais LP observés (pools à frais dynamiques) : 10040
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 17381 ; cycles déclenchés par événement : 5266 ; avance médiane sur le rafraîchissement multicall : 409 ms
- Gaz : base fee 0.008396 gwei ; prix ETH (pool le plus profond) : 2,065.30 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 469 pools, 272 jetons, 17808 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 102, aerodrome 191, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3655 (énumérés 290, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 2 → gardés 469 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2115.286044, 'cbBTC': 74654.762075, 'AERO': 0.563979}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 136,825,606 | 2,065.304150 | 55638776 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,182,350 | 0.027957 | 55638776 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,217,928 | 0.000014 | 55638776 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,598,039 | 0.027929 | 55638776 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,312,888 | 2,062.088625 | 55638776 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,916,195 | 104.368539 | 55638776 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,682,776 | 0.027962 | 55638776 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,353,567 | 1.799209 | 55638776 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,924,197 | 2,062.059731 | 55638776 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,882,078 | 1.000003 | 55638776 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,049,804 | 42,917.979320 | 55638776 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,943,920 | 2,062.104343 | 55638776 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2525 | 2,281,110 | 0.027951 | 55638776 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,978,315 | 1,104,773.585088 | 55638776 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,684,231 | 0.000014 | 55638776 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,658,618 | 0.000014 | 55638776 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,606,989 | 0.016175 | 55638776 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,540,875 | 0.006676 | 55638776 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,512,074 | 0.000000 | 55638776 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,492,930 | 0.000014 | 55638776 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,034 | 0.821905 | 55638776 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,429,958 | 417.162003 | 55638776 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,424,441 | 1.429325 | 55638776 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,274,184 | 2,065.348515 | 55638776 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,262,409 | 3,710.418156 | 55638776 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,235,081 | 14,950.037275 | 55638776 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,203,260 | 2,065.622050 | 55638776 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,632 | 79.347361 | 55638776 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,059,048 | 2,061.965438 | 55638776 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,032,069 | 35,260,069.635913 | 55638776 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 953,718 | 21.820504 | 55638776 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 943,938 | 562,950.291365 | 55638776 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 930,914 | 103.916224 | 55638776 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 919,325 | 0.001492 | 55638776 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 364 | 918,267 | 0.000014 | 55638776 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 915,021 | 22,771,465.285706 | 55638776 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 907,285 | 0.050565 | 55638776 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 889,398 | 1,024.916355 | 55638776 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 877,266 | 2,070.799405 | 55638776 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 866,435 | 0.000000 | 55638776 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 788,726 | 75.610071 | 55638776 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 784,564 | 105,646.276678 | 55638776 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 770,663 | 22.047314 | 55638776 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 760,091 | 0.051534 | 55638776 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 724,391 | 3,730.442734 | 55638776 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 701,156 | 0.798536 | 55638776 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 653,250 | 0.535038 | 55638776 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 646,162 | 0.524461 | 55638776 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 644,413 | 4,862,868.934265 | 55638776 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 605,535 | 0.000008 | 55638776 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 586,451 | 156,976.582404 | 55638776 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 581,793 | 0.000257 | 55638776 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2123 | 578,487 | 558,408.709831 | 55638776 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 563,611 | 0.038128 | 55638776 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 501,940 | 1,025.263203 | 55638776 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 480,443 | 6,776.732344 | 55638776 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 474,161 | 0.068643 | 55638776 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 11 | 455,492 | 1.001203 | 55638776 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 450,354 | 300.124427 | 55638776 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | WETH/msETH (stable) | 500 | 444,092 | 2.390100 | 55638776 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |

## Recherche d'opportunités
- Cycles : 21787 ; routes examinées : 387982896 ; candidats optimisés : 1332923 ; net attendu > 0 : 5761 ; dernier cycle 590.2 ms
- Rejets (moteur) : {'spread_below_threshold': 380545883, 'liquidity_below_min': 6032461, 'negative_expected_net': 1327162, 'borrow_bound_too_small': 36718, 'pool_quarantined': 23920, 'cycle_budget_exhausted': 9004, 'unquotable': 1984, 'no_price_reference': 3}
- Enregistrements de la session : 1332923 ; net attendu > 0 : 5761 ; simulés (eth_call de la vraie tx) : 237 (ok 119, échec 118) ; étiquettes ghost N+1 : 70/194 positives
- Décisions : {'REJECTED': 1332923} ; motifs de rejet : {'below_safety_margin': 2826, 'negative_expected_net': 1327162, 'p_lower_below_threshold': 5490, 'price_impact': 18, 'reliability_not_demonstrated': 271, 'sim_below_estimate': 8, 'simulated_net_nonpositive': 4, 'simulation_failed': 118, 'stale_data': 1367}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55553397 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 141.602055 USDC | 4.088765 USDC | 0.000000 USDC | 0.004454 USDC | 4.084311 USDC (3.7576 €) | — | 288.44 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55553404 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 141.602055 USDC | 4.088765 USDC | 0.000000 USDC | 0.004454 USDC | 4.084311 USDC (3.7576 €) | — | 288.44 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55553388 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 141.602055 USDC | 4.088765 USDC | 0.000000 USDC | 0.004456 USDC | 4.084309 USDC (3.7576 €) | — | 288.44 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55553408 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 141.602055 USDC | 4.088765 USDC | 0.000000 USDC | 0.004456 USDC | 4.084309 USDC (3.7576 €) | — | 288.44 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55553410 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 141.602055 USDC | 4.088765 USDC | 0.000000 USDC | 0.004456 USDC | 4.084309 USDC (3.7576 €) | — | 288.44 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55635128 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.288579 WETH | 0.000929 WETH | 0.000000 WETH | 0.000004 WETH | 0.000926 WETH (1.7846 €) | — | 32.08 | 0.068 (n=64) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 55635128 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 602.265600 USDC | 1.940530 USDC | 0.000000 USDC | 0.007338 USDC | 1.933192 USDC (1.7785 €) | — | 32.10 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.274730 WETH | 0.000854 WETH | 0.000000 WETH | 0.000003 WETH | 0.000851 WETH (1.6398 €) | — | 30.96 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55635128 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v2]→USDC | 573.161691 USDC | 1.782241 USDC | 0.000000 USDC | 0.006313 USDC | 1.775928 USDC (1.6339 €) | — | 30.98 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 55635128 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.314967 WETH | 0.000844 WETH | 0.000000 WETH | 0.000003 WETH | 0.000841 WETH (1.6213 €) | — | 26.70 | 0.068 (n=64) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 55635128 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 657.313221 USDC | 1.764080 USDC | 0.000000 USDC | 0.007001 USDC | 1.757079 USDC (1.6165 €) | — | 26.73 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.312818 WETH | 0.000788 WETH | 0.000000 WETH | 0.000003 WETH | 0.000785 WETH (1.5124 €) | — | 25.08 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 653.427259 USDC | 1.645981 USDC | 0.000000 USDC | 0.007001 USDC | 1.638980 USDC (1.5079 €) | — | 25.08 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.259104 WETH | 0.000773 WETH | 0.000000 WETH | 0.000003 WETH | 0.000769 WETH (1.4833 €) | — | 29.70 | 0.121 (n=24) | REJECTED | reliability_not_demonstrated |
| 55635128 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 540.741679 USDC | 1.612703 USDC | 0.000000 USDC | 0.006696 USDC | 1.606007 USDC (1.4775 €) | — | 29.70 | 0.121 (n=24) | REJECTED | reliability_not_demonstrated |
| 55635128 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.264113 WETH | 0.000630 WETH | 0.000000 WETH | 0.000004 WETH | 0.000626 WETH (1.2071 €) | — | 23.71 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 550.945904 USDC | 1.314762 USDC | 0.000000 USDC | 0.007674 USDC | 1.307088 USDC (1.2025 €) | — | 23.72 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.269380 WETH | 0.000616 WETH | 0.000000 WETH | 0.000003 WETH | 0.000613 WETH (1.1815 €) | — | 22.75 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 562.035412 USDC | 1.286502 USDC | 0.000000 USDC | 0.007001 USDC | 1.279501 USDC (1.1771 €) | — | 22.77 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.265118 WETH | 0.000576 WETH | 0.000000 WETH | 0.000003 WETH | 0.000572 WETH (1.1031 €) | — | 21.58 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 553.467511 USDC | 1.201473 USDC | 0.000000 USDC | 0.007001 USDC | 1.194472 USDC (1.0989 €) | — | 21.58 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.260491 WETH | 0.000552 WETH | 0.000000 WETH | 0.000003 WETH | 0.000549 WETH (1.0583 €) | — | 21.07 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 543.571684 USDC | 1.152882 USDC | 0.000000 USDC | 0.007001 USDC | 1.145881 USDC (1.0542 €) | — | 21.08 | 0.068 (n=64) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55635128 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.437929 WETH | 0.000512 WETH | 0.000000 WETH | 0.000003 WETH | 0.000510 WETH (0.9825 €) | — | 11.64 | 0.023 (n=36) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55635203 | WETH→[uniswap_v3]→LINK→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.080530 WETH | 0.000460 WETH | 0.000000 WETH | 0.000004 WETH | 0.000456 WETH (0.8720 €) | — | 56.60 | 0.000 (n=42) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 7485 ; taux observé 0.192 ; borne inférieure crédible (0.9) 0.186 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
