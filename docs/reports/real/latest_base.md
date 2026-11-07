# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T14:51:55+00:00 ; durée 107.05 min ; blocs 54331551 → 54363652 (6964 vus)

## Connexion
- Requêtes RPC : 88317 ; erreurs : 3 ; latence p50/p95 : 448.9/1,140.5 ms
- Rafraîchissements d'état : 6964 ; âge des données au dernier bloc : 8.42 s ; changements de frais LP observés (pools à frais dynamiques) : 1208
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 7414 ; cycles déclenchés par événement : 2785 ; avance médiane sur le rafraîchissement multicall : 436 ms
- Gaz : base fee 0.005010 gwei ; prix ETH (pool le plus profond) : 2,242.47 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 477 pools, 279 jetons, 17784 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 97, aerodrome 199, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 170 (rejetés 2) → 575 jetons ; pools candidats 3720 (énumérés 294, par paires 0), mesurés 480, sous le plancher de 10000.0 $ : 3 → gardés 477 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2242.465806, 'cbBTC': 75805.716976, 'AERO': 0.595957}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,088,599 | 2,242.466572 | 54363678 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,815,756 | 0.029570 | 54363678 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,343,217 | 0.000013 | 54363678 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,185,097 | 0.029513 | 54363678 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,080,559 | 2,244.653510 | 54363678 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,391,661 | 107.536407 | 54363678 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,422,923 | 0.001553 | 54363678 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,838,795 | 1.674445 | 54363678 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,787,447 | 0.029582 | 54363678 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,229,594 | 2,245.559671 | 54363678 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,991,430 | 0.999394 | 54363678 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,321,488 | 42,658.132009 | 54363678 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,199,808 | 2,245.373317 | 54363678 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,554,063 | 0.029529 | 54363678 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,101,175 | 1,154,578.522736 | 54363678 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,737,940 | 0.000013 | 54363678 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,698,243 | 0.006735 | 54363678 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,670,314 | 0.000000 | 54363678 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,647,587 | 0.000013 | 54363678 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,606,629 | 0.015987 | 54363678 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,526,857 | 440.647254 | 54363678 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,508,585 | 0.000013 | 54363678 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,501,313 | 1.460115 | 54363678 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,012 | 0.819738 | 54363678 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,376,248 | 3,754.908358 | 54363678 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,327,094 | 2,243.653810 | 54363678 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,324,961 | 2,248.912795 | 54363678 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,267,677 | 14,862.974791 | 54363678 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,205,662 | 2,244.635317 | 54363678 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,702 | 76.955062 | 54363678 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,113,619 | 35,790,511.592113 | 54363678 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,051,321 | 107.611783 | 54363678 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,023,845 | 563,984.997550 | 54363678 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 998,821 | 22,537,302.896047 | 54363678 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 988,832 | 0.000000 | 54363678 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 984,981 | 19.800231 | 54363678 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 942,328 | 1,059.065166 | 54363678 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,072 | 2,228.787514 | 54363678 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 926,133 | 0.000013 | 54363678 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 918,305 | 74.307782 | 54363678 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 879,913 | 99,076.511261 | 54363678 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 811,628 | 0.047909 | 54363678 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 795,175 | 3,730.217456 | 54363678 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 794,369 | 21.104959 | 54363678 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,475 | 0.055175 | 54363678 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,748 | 0.799699 | 54363678 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 721,207 | 0.566311 | 54363678 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,421 | 4,935,263.087908 | 54363678 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 685,712 | 0.000253 | 54363678 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 684,104 | 0.585221 | 54363678 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 658,950 | 146,402.044332 | 54363678 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 650,216 | 0.000008 | 54363678 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 627,241 | 568,312.527021 | 54363678 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 589,114 | 2.473976 | 54363678 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 584,943 | 0.040563 | 54363678 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 529,469 | 1,059.291526 | 54363678 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 516,591 | 921,154.365212 | 54363678 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 511,552 | 2,245.448383 | 54363678 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 509,874 | 7,093.532613 | 54363678 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 509,026 | 0.075328 | 54363678 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 9748 ; routes examinées : 173358432 ; candidats optimisés : 202394 ; net attendu > 0 : 33 ; dernier cycle 183.8 ms
- Rejets (moteur) : {'spread_below_threshold': 171641702, 'liquidity_below_min': 1504372, 'negative_expected_net': 202361, 'borrow_bound_too_small': 9748, 'pool_quarantined': 154, 'cycle_budget_exhausted': 62}
- Enregistrements de la session : 202394 ; net attendu > 0 : 33 ; simulés (eth_call de la vraie tx) : 19 (ok 4, échec 15) ; étiquettes ghost N+1 : 2/11 positives
- Décisions : {'REJECTED': 202394} ; motifs de rejet : {'below_safety_margin': 14, 'negative_expected_net': 202361, 'p_lower_below_threshold': 30, 'reliability_not_demonstrated': 3, 'simulation_failed': 15}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54348528 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 44.816547 USDC | 0.055181 USDC | 0.000000 USDC | 0.005038 USDC | 0.050143 USDC (0.0461 €) | — | 11.19 | 0.000 (n=100) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54355159 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.009080 WETH | 0.000019 WETH | 0.000000 WETH | 0.000002 WETH | 0.000017 WETH (0.0341 €) | 0.000017 WETH | 18.18 | 0.023 (n=35) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 54358910 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 56.345718 USDC | 0.036120 USDC | 0.000000 USDC | 0.005035 USDC | 0.031085 USDC (0.0286 €) | — | 5.52 | 0.027 (n=339) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54358911 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 56.345718 USDC | 0.036120 USDC | 0.000000 USDC | 0.005035 USDC | 0.031085 USDC (0.0286 €) | — | 5.52 | 0.027 (n=339) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54361963 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 55.149680 USDC | 0.033617 USDC | 0.000000 USDC | 0.005035 USDC | 0.028582 USDC (0.0263 €) | — | 5.18 | 0.027 (n=341) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54361964 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 55.149680 USDC | 0.033617 USDC | 0.000000 USDC | 0.005035 USDC | 0.028582 USDC (0.0263 €) | — | 5.18 | 0.027 (n=341) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54347132 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 38.265766 USDC | 0.016470 USDC | 0.000000 USDC | 0.005037 USDC | 0.011433 USDC (0.0105 €) | — | 2.99 | 0.048 (n=259) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54349219 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.654316 USDC | 0.015378 USDC | 0.000000 USDC | 0.005037 USDC | 0.010341 USDC (0.0095 €) | — | 4.37 | 0.024 (n=338) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 54360249 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 22.473839 USDC | 0.014003 USDC | 0.000000 USDC | 0.005036 USDC | 0.008967 USDC (0.0082 €) | 0.008967 USDC | 3.99 | 0.027 (n=340) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54360249 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 22.473839 USDC | 0.014003 USDC | 0.000000 USDC | 0.005036 USDC | 0.008967 USDC (0.0082 €) | — | 3.99 | 0.027 (n=340) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54337664 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→WETH | 0.014203 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0062 €) | — | 2.12 | 0.052 (n=84) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54337662 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→WETH | 0.014203 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0062 €) | — | 2.12 | 0.052 (n=84) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54337666 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→WETH | 0.014203 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0062 €) | — | 2.12 | 0.052 (n=84) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54346444 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.163332 USDC | 0.011212 USDC | 0.000000 USDC | 0.005038 USDC | 0.006174 USDC (0.0057 €) | 0.006174 USDC | 3.06 | 0.025 (n=337) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 54349377 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 31.693115 USDC | 0.011175 USDC | 0.000000 USDC | 0.005037 USDC | 0.006138 USDC (0.0056 €) | — | 1.94 | 0.048 (n=260) | REJECTED | below_safety_margin(6138<6338), p_lower_below_threshold(0.05<0.75) |
| 54361663 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.107999 USDC | 0.010044 USDC | 0.000000 USDC | 0.005036 USDC | 0.005008 USDC (0.0046 €) | 0.005008 USDC | 2.62 | 0.048 (n=260) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54361663 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.107999 USDC | 0.010044 USDC | 0.000000 USDC | 0.005036 USDC | 0.005008 USDC (0.0046 €) | — | 2.62 | 0.048 (n=260) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54361664 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.648979 USDC | 0.008661 USDC | 0.000000 USDC | 0.005036 USDC | 0.003625 USDC (0.0033 €) | — | 2.05 | 0.048 (n=261) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54346632 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 150.183250 USDC | 0.008481 USDC | 0.000000 USDC | 0.005378 USDC | 0.003103 USDC (0.0029 €) | — | 0.21 | 0.048 (n=259) | REJECTED | below_safety_margin(3103<30036), p_lower_below_threshold(0.05<0.75) |
| 54346632 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 150.183250 USDC | 0.008481 USDC | 0.000000 USDC | 0.005378 USDC | 0.003103 USDC (0.0029 €) | — | 0.21 | 0.048 (n=259) | REJECTED | below_safety_margin(3103<30036), p_lower_below_threshold(0.05<0.75) |
| 54346632 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.067495 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0029 €) | — | 0.20 | 0.048 (n=259) | REJECTED | below_safety_margin(1383108914410<13499089765070), p_lower_below_threshold(0.05<0.75) |
| 54346632 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.067495 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0029 €) | — | 0.20 | 0.048 (n=259) | REJECTED | below_safety_margin(1383108914410<13499089765070), p_lower_below_threshold(0.05<0.75) |
| 54344609 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.003648 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0019 €) | — | 2.56 | 0.223 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54344610 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.003648 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0019 €) | — | 2.56 | 0.223 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54343178 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 15.348285 USDC | 0.006472 USDC | 0.000000 USDC | 0.005038 USDC | 0.001434 USDC (0.0013 €) | — | 0.93 | 0.048 (n=259) | REJECTED | below_safety_margin(1434<3069), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5987 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
