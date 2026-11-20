# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T15:45:04+00:00 ; durée 330.13 min ; blocs 59896587 → 59995624 (29269 vus)

## Connexion
- Requêtes RPC : 281903 ; erreurs : 95 ; latence p50/p95 : 197.1/986.3 ms
- Rafraîchissements d'état : 29269 ; âge des données au dernier bloc : 5.68 s ; changements de frais LP observés (pools à frais dynamiques) : 19975
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 92351 ; cycles déclenchés par événement : 15895 ; avance médiane sur le rafraîchissement multicall : 151 ms
- Gaz : base fee 0.017705 gwei ; prix ETH (pool le plus profond) : 1,662.36 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 248 jetons, 12740 routes
- Par DEX : uniswap_v3 127, aerodrome_slipstream 86, aerodrome 171, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 255, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1747.036684, 'cbBTC': 61757.075443, 'AERO': 0.420112}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 81,735,137 | 1,662.360214 | 59995623 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 20,165,618 | 0.027771 | 59995623 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,869,518 | 1,661.750114 | 59995626 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,321,413 | 0.027809 | 59995623 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,165,597 | 84.391039 | 59995623 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,703,421 | 0.000017 | 59995627 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,964,310 | 0.027764 | 59995628 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,471,522 | 2.553541 | 59995623 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,152,555 | 0.998604 | 59995623 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,002,160 | 1,661.749493 | 59995628 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,539,878 | 40,089.516970 | 59995623 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 355 | 2,184,934 | 1,661.781952 | 59995628 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,854,047 | 0.000017 | 59995623 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 1,626,610 | 0.027791 | 59995623 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,577,424 | 1,125,769.593627 | 59995623 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,450,780 | 0.843780 | 59995623 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,342,621 | 0.000017 | 59995626 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,251,320 | 0.000000 | 59995623 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,183,265 | 0.000017 | 59995627 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,157,983 | 0.006326 | 59995623 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,063,219 | 16.039813 | 59995624 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,600 | 86.547675 | 59995623 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 985,743 | 461.671591 | 59995623 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 967,189 | 1,663.513903 | 59995623 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 955,305 | 16,582.677460 | 59995623 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 931,728 | 4,253.079678 | 59995623 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 920,281 | 83.828090 | 59995623 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 874,935 | 0.050784 | 59995623 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 874,069 | 1,663.614240 | 59995623 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 867,762 | 31,555,213.790030 | 59995623 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 777,754 | 70.729536 | 59995623 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 772,877 | 533,472.278503 | 59995623 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 749,447 | 22,199,100.983095 | 59995623 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 745,830 | 0.001495 | 59995623 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 736,902 | 0.015206 | 59995629 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | DRB/WETH | 10000 | 734,290 | 0.000000 | 59995623 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| pancakeswap_v3 | QUID/USDC | 100 | 715,848 | 0.045467 | 59995625 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4610 | 696,739 | 25.546891 | 59995623 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | WETH/USDC | 500 | 693,069 | 1,661.678683 | 59995629 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/MORPHO | 3000 | 681,203 | 1,109.221728 | 59995623 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 677,508 | 1,674.814275 | 59995623 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | TIG/USDC | 10000 | 573,256 | 0.413763 | 59995623 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v3 | WETH/USDC | 100 | 569,158 | 1,661.867624 | 59995629 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 564,053 | 0.799406 | 59995623 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 529,466 | 4,691,128.561397 | 59995623 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 510,522 | 4,262.707273 | 59995623 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,939 | 1.386531 | 59995623 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | FLOCK/USDC | 3000 | 480,240 | 0.029970 | 59995623 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 480,139 | 532,535.913373 | 59995623 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| pancakeswap_v3 | ELSA/USDC | 100 | 464,731 | 0.066905 | 59995629 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 456,683 | 1.002443 | 59995626 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v2 | WETH/NPC | 3000 | 427,281 | 192,708.588072 | 59995623 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 418,222 | 0.000007 | 59995623 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | WETH/uSOL | 3000 | 370,654 | 22.897090 | 59995623 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome_slipstream | WETH/MORPHO | 3076 | 369,285 | 1,109.071838 | 59995623 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 368,221 | 848,814.605636 | 59995623 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 362,300 | 0.054581 | 59995623 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/UNI | 10000 | 353,040 | 370.210368 | 59995623 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/DEGEN | 3000 | 341,171 | 2,538,440.632891 | 59995623 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |
| aerodrome_slipstream | WETH/VVV | 2946 | 340,010 | 84.395186 | 59995623 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 45163 ; routes examinées : 575376620 ; candidats optimisés : 789944 ; net attendu > 0 : 1826 ; dernier cycle 1202.3 ms
- Rejets (moteur) : {'spread_below_threshold': 561934722, 'liquidity_below_min': 7286846, 'negative_expected_net': 788118, 'cycle_budget_exhausted': 83175, 'pool_quarantined': 72560, 'borrow_bound_too_small': 65343, 'no_price_reference': 279}
- Enregistrements de la session : 474199 ; net attendu > 0 : 1826 ; simulés (eth_call de la vraie tx) : 151 (ok 47, échec 104) ; étiquettes ghost N+1 : 47/122 positives
- Décisions : {'REJECTED': 474199} ; motifs de rejet : {'below_safety_margin': 1137, 'negative_expected_net': 472373, 'p_lower_below_threshold': 1783, 'price_impact': 149, 'reliability_not_demonstrated': 43, 'sim_below_estimate': 20, 'simulated_net_nonpositive': 15, 'simulation_failed': 104, 'stale_data': 274}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59993481 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.291916 WETH | 0.000282 WETH | 0.000000 WETH | 0.000012 WETH | 0.000270 WETH (0.4156 €) | — | 9.25 | 0.114 (n=164) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 59993481 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.008019 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4151 €) | — | 9.34 | 0.114 (n=164) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 59993481 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 487.466871 USDC | 0.470088 USDC | 0.000000 USDC | 0.020232 USDC | 0.449856 USDC (0.4139 €) | — | 9.23 | 0.114 (n=164) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 59993481 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.276723 WETH | 0.000255 WETH | 0.000000 WETH | 0.000012 WETH | 0.000243 WETH (0.3740 €) | — | 8.78 | 0.153 (n=247) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 59993481 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.007565 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.3735 €) | — | 8.91 | 0.153 (n=247) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 59993481 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 455.937033 USDC | 0.424705 USDC | 0.000000 USDC | 0.020232 USDC | 0.404473 USDC (0.3721 €) | — | 8.87 | 0.153 (n=247) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 59993481 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.164576 WETH | 0.000183 WETH | 0.000000 WETH | 0.000013 WETH | 0.000170 WETH (0.2621 €) | — | 10.35 | 0.114 (n=164) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 59993481 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.162287 WETH | 0.000183 WETH | 0.000000 WETH | 0.000013 WETH | 0.000170 WETH (0.2615 €) | — | 10.47 | 0.114 (n=164) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 59993481 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 274.082901 USDC | 0.304521 USDC | 0.000000 USDC | 0.021099 USDC | 0.283422 USDC (0.2607 €) | — | 10.34 | 0.114 (n=164) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 59993481 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 269.309934 USDC | 0.304730 USDC | 0.000000 USDC | 0.021966 USDC | 0.282764 USDC (0.2601 €) | — | 10.50 | 0.114 (n=164) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 59993481 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.160557 WETH | 0.000175 WETH | 0.000000 WETH | 0.000013 WETH | 0.000162 WETH (0.2500 €) | — | 10.12 | 0.153 (n=247) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 59993481 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 266.787542 USDC | 0.291447 USDC | 0.000000 USDC | 0.021099 USDC | 0.270348 USDC (0.2487 €) | — | 10.13 | 0.153 (n=247) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 59993481 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.164227 WETH | 0.000153 WETH | 0.000000 WETH | 0.000013 WETH | 0.000140 WETH (0.2158 €) | — | 8.53 | 0.153 (n=247) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 59993481 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004403 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2150 €) | — | 8.81 | 0.153 (n=247) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 59993481 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 273.567919 USDC | 0.254461 USDC | 0.000000 USDC | 0.021099 USDC | 0.233362 USDC (0.2147 €) | — | 8.53 | 0.153 (n=247) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 59993481 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.158122 WETH | 0.000138 WETH | 0.000000 WETH | 0.000013 WETH | 0.000125 WETH (0.1931 €) | — | 7.93 | 0.222 (n=1312) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59993481 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004154 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1923 €) | — | 8.35 | 0.153 (n=247) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 59993481 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 263.826362 USDC | 0.229920 USDC | 0.000000 USDC | 0.021099 USDC | 0.208821 USDC (0.1921 €) | — | 7.92 | 0.222 (n=1312) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59986570 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.542832 WETH | 0.000110 WETH | 0.000000 WETH | 0.000005 WETH | 0.000105 WETH (0.1664 €) | — | 1.94 | 0.276 (n=1653) | REJECTED | below_safety_margin(105453345218430<108566410041576), p_lower_below_threshold(0.28<0.75) |
| 59986570 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 929.597658 USDC | 0.188458 USDC | 0.000000 USDC | 0.007950 USDC | 0.180508 USDC (0.1661 €) | — | 1.94 | 0.276 (n=1653) | REJECTED | below_safety_margin(180508<185919), p_lower_below_threshold(0.28<0.75) |
| 59986570 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.014710 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1658 €) | — | 2.01 | 0.276 (n=1653) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59986570 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.009526 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1636 €) | — | 3.07 | 0.076 (n=513) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 59986570 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 581.678195 USDC | 0.183827 USDC | 0.000000 USDC | 0.006347 USDC | 0.177480 USDC (0.1633 €) | — | 3.05 | 0.076 (n=513) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 59994803 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.305290 WETH | 0.000108 WETH | 0.000000 WETH | 0.000008 WETH | 0.000100 WETH (0.1538 €) | — | 3.28 | 0.076 (n=513) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 59994803 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 507.229388 USDC | 0.180210 USDC | 0.000000 USDC | 0.013554 USDC | 0.166656 USDC (0.1533 €) | — | 3.29 | 0.076 (n=513) | REJECTED | p_lower_below_threshold(0.08<0.75) |

## Fiabilité et décision
- Observations ghost : 8712 ; taux observé 0.230 ; borne inférieure crédible (0.9) 0.224 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
