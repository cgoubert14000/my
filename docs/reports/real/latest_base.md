# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T18:31:30+00:00 ; durée 175.71 min ; blocs 55240823 → 55293547 (7032 vus)

## Connexion
- Requêtes RPC : 103682 ; erreurs : 0 ; latence p50/p95 : 566.8/1,638.8 ms
- Rafraîchissements d'état : 7032 ; âge des données au dernier bloc : 10.1 s ; changements de frais LP observés (pools à frais dynamiques) : 5415
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6175 ; cycles déclenchés par événement : 1931 ; avance médiane sur le rafraîchissement multicall : 534 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,121.50 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 274 jetons, 17868 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 102, aerodrome 193, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3663 (énumérés 293, par paires 0), mesurés 475, sous le plancher de 10000.0 $ : 2 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2131.426069, 'cbBTC': 75169.710892, 'AERO': 0.579676}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,553,969 | 2,121.495957 | 55293534 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,604,785 | 0.028460 | 55293534 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,270,048 | 0.000013 | 55293534 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,745,361 | 0.028437 | 55293534 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,314,584 | 2,122.982608 | 55293534 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,280,559 | 99.141967 | 55293544 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,932,905 | 0.028465 | 55293534 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,577,253 | 1.748990 | 55293544 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,997,132 | 2,123.224868 | 55293544 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,927,578 | 0.998591 | 55293534 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,109,508 | 43,562.829386 | 55293534 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,020,766 | 2,123.342883 | 55293547 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,357,131 | 0.028431 | 55293534 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,993,033 | 1,148,554.063045 | 55293534 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,716,884 | 0.000013 | 55293534 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 592 | 1,700,172 | 0.000013 | 55293534 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,577,244 | 0.015703 | 55293534 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,574,940 | 0.006649 | 55293534 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,557,652 | 0.000000 | 55293534 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,507,932 | 0.000013 | 55293534 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,481,281 | 1.407587 | 55293534 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,464,082 | 421.800285 | 55293534 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,000 | 0.821800 | 55293534 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,318,207 | 3,709.869430 | 55293534 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,291,292 | 2,121.632133 | 55293534 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,249,627 | 14,831.718956 | 55293534 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,219,616 | 2,122.234674 | 55293544 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,252 | 79.258498 | 55293534 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,093,889 | 2,122.980665 | 55293534 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,045,232 | 36,659,074.914461 | 55293534 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 980,849 | 99.767949 | 55293534 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 968,248 | 565,272.246609 | 55293534 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,634 | 21.344927 | 55293534 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 955,406 | 0.046794 | 55293534 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 935,712 | 0.001518 | 55293534 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 368 | 925,250 | 0.000013 | 55293534 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 924,584 | 23,537,564.740435 | 55293534 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 919,598 | 74.098888 | 55293534 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 907,271 | 1,032.214305 | 55293534 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 896,713 | 0.000000 | 55293534 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 886,420 | 2,127.924155 | 55293534 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 816,419 | 102,943.960977 | 55293534 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 774,308 | 21.898542 | 55293534 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 771,972 | 0.053205 | 55293534 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 744,780 | 3,692.738593 | 55293534 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 720,211 | 0.798586 | 55293534 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 670,253 | 0.549422 | 55293534 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 660,620 | 4,880,735.898534 | 55293534 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,271 | 0.527774 | 55293534 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 621,224 | 0.000008 | 55293534 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 612,167 | 151,952.984556 | 55293534 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 597,941 | 0.000257 | 55293534 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 592,909 | 569,786.800041 | 55293534 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 571,631 | 0.038964 | 55293534 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 530,526 | 2.393307 | 55293534 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 515,288 | 1,032.800892 | 55293534 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 509,963 | 906,054.195506 | 55293534 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 493,511 | 1.001029 | 55293534 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 487,435 | 6,946.834492 | 55293534 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | WETH/uSOL | 3000 | 468,673 | 24.661502 | 55293534 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 8962 ; routes examinées : 160133016 ; candidats optimisés : 574650 ; net attendu > 0 : 1474 ; dernier cycle 52.1 ms
- Rejets (moteur) : {'spread_below_threshold': 157054238, 'liquidity_below_min': 2464316, 'negative_expected_net': 573176, 'borrow_bound_too_small': 37659, 'pool_quarantined': 1512, 'cycle_budget_exhausted': 641}
- Enregistrements de la session : 574650 ; net attendu > 0 : 1474 ; simulés (eth_call de la vraie tx) : 96 (ok 64, échec 32) ; étiquettes ghost N+1 : 24/59 positives
- Décisions : {'REJECTED': 574650} ; motifs de rejet : {'below_safety_margin': 1248, 'negative_expected_net': 573176, 'p_lower_below_threshold': 1393, 'reliability_not_demonstrated': 81, 'sim_below_estimate': 7, 'simulated_net_nonpositive': 3, 'simulation_failed': 32, 'stale_data': 523}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55292046 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.628604 WETH | 0.000161 WETH | 0.000000 WETH | 0.000002 WETH | 0.000159 WETH (0.3108 €) | — | 2.53 | 0.048 (n=91) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,328.473302 USDC | 0.341590 USDC | 0.000000 USDC | 0.004798 USDC | 0.336792 USDC (0.3098 €) | — | 2.54 | 0.048 (n=91) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55292046 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.489407 WETH | 0.000128 WETH | 0.000000 WETH | 0.000002 WETH | 0.000126 WETH (0.2460 €) | — | 2.58 | 0.063 (n=309) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,032.952111 USDC | 0.271387 USDC | 0.000000 USDC | 0.004798 USDC | 0.266589 USDC (0.2453 €) | — | 2.58 | 0.063 (n=309) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55292068 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.486339 WETH | 0.000127 WETH | 0.000000 WETH | 0.000002 WETH | 0.000125 WETH (0.2438 €) | — | 2.57 | 0.063 (n=309) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55292068 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,028.744064 USDC | 0.268963 USDC | 0.000000 USDC | 0.004798 USDC | 0.264165 USDC (0.2430 €) | — | 2.57 | 0.063 (n=309) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55292046 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.011792 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2107 €) | — | 2.60 | 0.219 (n=1279) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 55292046 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.435109 WETH | 0.000111 WETH | 0.000000 WETH | 0.000003 WETH | 0.000108 WETH (0.2101 €) | — | 2.47 | 0.219 (n=1279) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 927.984639 USDC | 0.233918 USDC | 0.000000 USDC | 0.006417 USDC | 0.227501 USDC (0.2093 €) | — | 2.45 | 0.219 (n=1279) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 55292046 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.461965 WETH | 0.000106 WETH | 0.000000 WETH | 0.000002 WETH | 0.000104 WETH (0.2032 €) | — | 2.25 | 0.048 (n=91) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 976.657356 USDC | 0.224972 USDC | 0.000000 USDC | 0.004798 USDC | 0.220174 USDC (0.2026 €) | — | 2.25 | 0.048 (n=91) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55292068 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.368931 WETH | 0.000089 WETH | 0.000000 WETH | 0.000003 WETH | 0.000086 WETH (0.1682 €) | — | 2.34 | 0.219 (n=1279) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |
| 55292068 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.010266 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1682 €) | — | 2.39 | 0.219 (n=1279) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 55292068 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 808.296799 USDC | 0.188656 USDC | 0.000000 USDC | 0.006417 USDC | 0.182239 USDC (0.1677 €) | — | 2.25 | 0.219 (n=1279) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 55292308 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.502346 WETH | 0.000081 WETH | 0.000000 WETH | 0.000003 WETH | 0.000077 WETH (0.1513 €) | — | 1.54 | 0.048 (n=30) | REJECTED | below_safety_margin(77496584625021<100469129525430), p_lower_below_threshold(0.05<0.75) |
| 55292308 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.014128 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1510 €) | — | 1.56 | 0.048 (n=30) | REJECTED | below_safety_margin(220<282), p_lower_below_threshold(0.05<0.75) |
| 55292308 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,048.256806 USDC | 0.170840 USDC | 0.000000 USDC | 0.006741 USDC | 0.164099 USDC (0.1510 €) | — | 1.57 | 0.048 (n=30) | REJECTED | below_safety_margin(164099<209651), p_lower_below_threshold(0.05<0.75) |
| 55292068 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.441191 WETH | 0.000079 WETH | 0.000000 WETH | 0.000002 WETH | 0.000077 WETH (0.1507 €) | — | 1.75 | 0.048 (n=91) | REJECTED | below_safety_margin(77205434641210<88238142028159), p_lower_below_threshold(0.05<0.75) |
| 55292068 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 932.179925 USDC | 0.168094 USDC | 0.000000 USDC | 0.004798 USDC | 0.163296 USDC (0.1502 €) | — | 1.75 | 0.048 (n=91) | REJECTED | below_safety_margin(163296<186435), p_lower_below_threshold(0.05<0.75) |
| 55292096 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.348371 WETH | 0.000065 WETH | 0.000000 WETH | 0.000002 WETH | 0.000063 WETH (0.1227 €) | — | 1.80 | 0.063 (n=309) | REJECTED | below_safety_margin(62877414844093<69674239312979), p_lower_below_threshold(0.06<0.75) |
| 55292046 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.290513 WETH | 0.000065 WETH | 0.000000 WETH | 0.000002 WETH | 0.000063 WETH (0.1224 €) | — | 2.16 | 0.063 (n=309) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55292096 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 736.378566 USDC | 0.137780 USDC | 0.000000 USDC | 0.004797 USDC | 0.132983 USDC (0.1223 €) | — | 1.81 | 0.063 (n=309) | REJECTED | below_safety_margin(132983<147275), p_lower_below_threshold(0.06<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 611.970534 USDC | 0.137364 USDC | 0.000000 USDC | 0.004798 USDC | 0.132566 USDC (0.1220 €) | — | 2.17 | 0.063 (n=309) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55292096 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.392973 WETH | 0.000063 WETH | 0.000000 WETH | 0.000002 WETH | 0.000061 WETH (0.1187 €) | — | 1.55 | 0.048 (n=91) | REJECTED | below_safety_margin(60795483372735<78594652099520), p_lower_below_threshold(0.05<0.75) |
| 55292096 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 828.298730 USDC | 0.133380 USDC | 0.000000 USDC | 0.004797 USDC | 0.128583 USDC (0.1183 €) | — | 1.55 | 0.048 (n=91) | REJECTED | below_safety_margin(128583<165659), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 6971 ; taux observé 0.185 ; borne inférieure crédible (0.9) 0.179 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
