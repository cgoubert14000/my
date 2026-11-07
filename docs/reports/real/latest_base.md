# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T03:04:35+00:00 ; durée 73.72 min ; blocs 54129350 → 54151442 (3679 vus)

## Connexion
- Requêtes RPC : 48045 ; erreurs : 140 ; latence p50/p95 : 315.9/1,813.8 ms
- Rafraîchissements d'état : 3679 ; âge des données au dernier bloc : 9.85 s ; changements de frais LP observés (pools à frais dynamiques) : 1480
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 165 ; cycles déclenchés par événement : 65 ; avance médiane sur le rafraîchissement multicall : 543 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,241.24 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 480 pools, 282 jetons, 17844 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 100, aerodrome 199, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 170 (rejetés 2) → 575 jetons ; pools candidats 3720 (énumérés 297, par paires 0), mesurés 483, sous le plancher de 10000.0 $ : 3 → gardés 480 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2239.687391, 'cbBTC': 75912.79678, 'AERO': 0.607077}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,954,124 | 2,241.237864 | 54151472 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,780,623 | 0.029553 | 54151472 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,315,286 | 0.000013 | 54151472 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,168,566 | 0.029485 | 54151472 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,019,536 | 2,245.294985 | 54151472 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,417,636 | 106.705059 | 54151472 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,430,697 | 0.001556 | 54151472 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,883,386 | 1.646352 | 54151472 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,763,347 | 0.029543 | 54151472 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,179,194 | 2,245.821933 | 54151472 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,997,133 | 0.998508 | 54151472 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,326,619 | 42,480.045886 | 54151472 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,204,214 | 2,245.818029 | 54151472 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,561,526 | 0.029498 | 54151472 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,088,980 | 1,166,818.518415 | 54151472 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,741,335 | 0.000013 | 54151472 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,709,809 | 0.006818 | 54151472 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,660,238 | 0.000000 | 54151472 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,631,145 | 0.000013 | 54151472 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,622,513 | 0.016218 | 54151472 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54151472 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,532,999 | 433.941187 | 54151472 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,508,609 | 0.000013 | 54151472 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,379 | 0.819350 | 54151472 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,389,892 | 3,694.213014 | 54151472 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,326,712 | 2,243.130128 | 54151472 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,324,771 | 2,250.761785 | 54151472 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,275,605 | 14,658.686852 | 54151472 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,178,244 | 2,245.182892 | 54151472 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,122,722 | 77.089407 | 54151472 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,109,459 | 36,246,580.475698 | 54151472 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,054,149 | 106.733527 | 54151472 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,029,836 | 553,874.541297 | 54151472 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,008,986 | 0.000000 | 54151472 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 999,027 | 22,508,255.999049 | 54151472 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 981,039 | 20.034924 | 54151472 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 940,866 | 1,064.335735 | 54151472 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,465 | 2,228.788739 | 54151472 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 932,531 | 72.057852 | 54151472 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 926,109 | 0.000013 | 54151472 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 893,475 | 95,986.423939 | 54151472 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 814,109 | 0.047536 | 54151472 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 801,996 | 20.825023 | 54151472 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 800,780 | 3,667.284216 | 54151472 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,683 | 0.056694 | 54151472 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,331 | 0.799699 | 54151472 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 719,326 | 0.567539 | 54151472 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 704,410 | 4,790,631.905800 | 54151472 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 686,940 | 0.000255 | 54151472 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 667,751 | 0.559006 | 54151472 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 661,210 | 145,232.120423 | 54151472 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 656,282 | 0.000008 | 54151472 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 632,844 | 558,542.624639 | 54151472 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 588,944 | 2.473030 | 54151472 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 585,921 | 0.040680 | 54151472 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 526,858 | 1,064.706416 | 54151472 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 522,033 | 897,343.903978 | 54151472 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 517,234 | 2,245.721059 | 54151472 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | ELSA/USDC | 100 | 516,823 | 0.076878 | 54151472 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 516,649 | 6,901.138429 | 54151472 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 3743 ; routes examinées : 66790092 ; candidats optimisés : 242322 ; net attendu > 0 : 37 ; dernier cycle 381.3 ms
- Rejets (moteur) : {'spread_below_threshold': 65781270, 'liquidity_below_min': 753771, 'negative_expected_net': 242285, 'pool_quarantined': 8776, 'borrow_bound_too_small': 3741, 'cycle_budget_exhausted': 212}
- Enregistrements de la session : 242322 ; net attendu > 0 : 37 ; simulés (eth_call de la vraie tx) : 18 (ok 6, échec 12) ; étiquettes ghost N+1 : 1/14 positives
- Décisions : {'REJECTED': 242322} ; motifs de rejet : {'below_safety_margin': 18, 'negative_expected_net': 242285, 'p_lower_below_threshold': 33, 'price_impact': 13, 'reliability_not_demonstrated': 4, 'simulation_failed': 12, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54145094 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 34.995920 USDC | 0.046390 USDC | 0.000000 USDC | 0.005032 USDC | 0.041358 USDC (0.0380 €) | 0.041358 USDC | 11.82 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 54133736 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 25.654596 USDC | 0.027046 USDC | 0.000000 USDC | 0.005029 USDC | 0.022017 USDC (0.0203 €) | 0.022017 USDC | 8.58 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 54148182 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 25.889662 USDC | 0.017681 USDC | 0.000000 USDC | 0.005033 USDC | 0.012648 USDC (0.0116 €) | 0.012648 USDC | 4.89 | 0.026 (n=323) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54149881 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 211.296194 USDC | 0.016940 USDC | 0.000000 USDC | 0.005032 USDC | 0.011908 USDC (0.0110 €) | — | 0.56 | 0.047 (n=250) | REJECTED | below_safety_margin(11908<42259), p_lower_below_threshold(0.05<0.75) |
| 54149881 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.094559 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0109 €) | — | 0.56 | 0.047 (n=250) | REJECTED | below_safety_margin(5302650025869<18911763862340), p_lower_below_threshold(0.05<0.75) |
| 54131500 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 24.545994 USDC | 0.015989 USDC | 0.000000 USDC | 0.005029 USDC | 0.010960 USDC (0.0101 €) | 0.010960 USDC | 4.47 | 0.026 (n=322) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54133628 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 16.785697 USDC | 0.011651 USDC | 0.000000 USDC | 0.005031 USDC | 0.006620 USDC (0.0061 €) | — | 3.94 | 0.065 (n=91) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 54132465 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.625961 USDC | 0.011096 USDC | 0.000000 USDC | 0.005029 USDC | 0.006067 USDC (0.0056 €) | 0.006067 USDC | 2.94 | 0.047 (n=249) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54142205 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0042 €) | — | 45.52 | 0.007 (n=121) | REJECTED | stale_data(4634ms>4000.0), price_impact(209bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |
| 54133929 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 14.185621 USDC | 0.008294 USDC | 0.000000 USDC | 0.005030 USDC | 0.003264 USDC (0.0030 €) | 0.003264 USDC | 2.30 | 0.053 (n=82) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54133049 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.574000 USDC | 0.008255 USDC | 0.000000 USDC | 0.005028 USDC | 0.003227 USDC (0.0030 €) | — | 1.84 | 0.047 (n=250) | REJECTED | below_safety_margin(3227<3514), stale_data(4274ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54137594 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.366000 USDC | 0.007954 USDC | 0.000000 USDC | 0.005032 USDC | 0.002922 USDC (0.0027 €) | — | 1.68 | 0.047 (n=250) | REJECTED | below_safety_margin(2922<3473), p_lower_below_threshold(0.05<0.75) |
| 54132664 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 16.491328 USDC | 0.007156 USDC | 0.000000 USDC | 0.005029 USDC | 0.002127 USDC (0.0020 €) | — | 1.29 | 0.047 (n=250) | REJECTED | below_safety_margin(2127<3298), p_lower_below_threshold(0.05<0.75) |
| 54142205 | WETH→[aerodrome]→fBOMB→[aerodrome]→cbBTC→[aerodrome]→WETH | 0.000446 WETH | 0.000001 WETH | 0.000000 WETH | 0.000000 WETH | 0.000001 WETH (0.0011 €) | — | 11.85 | 0.006 (n=1) | REJECTED | stale_data(4642ms>4000.0), price_impact(224bps>150.0), simulation_failed:revert 0xa932492f, reliability_not_demonstrated |
| 54142802 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.140 (n=262) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54143470 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.139 (n=264) | REJECTED | stale_data(4795ms>4000.0), price_impact(210bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54143111 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.140 (n=263) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54143112 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.139 (n=264) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54143113 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.139 (n=264) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54143114 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.139 (n=264) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54142488 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.141 (n=261) | REJECTED | stale_data(4603ms>4000.0), price_impact(211bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54142489 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.140 (n=262) | REJECTED | price_impact(211bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54142205 | cbBTC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.141 (n=260) | REJECTED | stale_data(4635ms>4000.0), price_impact(235bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54142205 | cbBTC→[aerodrome]→WETH→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.002 (n=3) | REJECTED | stale_data(4642ms>4000.0), price_impact(230bps>150.0), reliability_not_demonstrated |
| 54143367 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 14.719307 USDC | 0.005766 USDC | 0.000000 USDC | 0.005031 USDC | 0.000735 USDC (0.0007 €) | — | 0.50 | 0.047 (n=250) | REJECTED | below_safety_margin(735<2943), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5937 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
