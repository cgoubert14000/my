# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T14:55:48+00:00 ; durée 280.87 min ; blocs 59896587 → 59980853 (26804 vus)

## Connexion
- Requêtes RPC : 247761 ; erreurs : 0 ; latence p50/p95 : 94.0/916.6 ms
- Rafraîchissements d'état : 26804 ; âge des données au dernier bloc : 5.91 s ; changements de frais LP observés (pools à frais dynamiques) : 15579
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 52348 ; cycles déclenchés par événement : 10048 ; avance médiane sur le rafraîchissement multicall : 142 ms
- Gaz : base fee 0.010242 gwei ; prix ETH (pool le plus profond) : 1,735.02 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 248 jetons, 12740 routes
- Par DEX : uniswap_v3 127, aerodrome_slipstream 86, aerodrome 171, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 255, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1747.036684, 'cbBTC': 61757.075443, 'AERO': 0.420112}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 85,055,696 | 1,735.016936 | 59980843 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,048,436 | 0.028178 | 59980829 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 11,628,658 | 1,737.926908 | 59980830 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,608,884 | 0.028171 | 59980829 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,451,882 | 83.979086 | 59980829 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,990,918 | 0.000016 | 59980840 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,124,484 | 0.028187 | 59980853 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,550,321 | 2.441448 | 59980829 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,369,977 | 1,738.202662 | 59980853 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,242,595 | 0.998726 | 59980829 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,664,373 | 39,684.748328 | 59980829 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 394 | 2,271,614 | 1,737.753937 | 59980833 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,908,377 | 0.000016 | 59980829 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2565 | 1,693,578 | 0.028155 | 59980829 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,633,978 | 1,142,907.098486 | 59980829 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,501 | 0.843780 | 59980829 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,376,590 | 0.000016 | 59980829 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,312,565 | 0.000000 | 59980829 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,235,990 | 0.000016 | 59980852 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,211,115 | 0.006326 | 59980829 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,074,019 | 15.618675 | 59980851 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,687 | 86.533479 | 59980829 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,028,812 | 461.656513 | 59980829 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 989,383 | 16,389.875055 | 59980829 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | WETH/USDC | 3000 | 988,051 | 1,734.605563 | 59980829 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 973,874 | 4,241.780765 | 59980829 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 966,055 | 84.268086 | 59980829 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 905,095 | 0.048383 | 59980829 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/doginme | 10000 | 897,246 | 32,392,401.732076 | 59980829 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/USDC | 3000 | 892,966 | 1,734.643793 | 59980829 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/BRETT | 10000 | 806,727 | 533,355.047421 | 59980843 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 790,506 | 68.466056 | 59980832 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 774,686 | 22,553,299.775880 | 59980829 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 770,319 | 0.001508 | 59980829 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | DRB/WETH | 10000 | 767,436 | 0.000000 | 59980829 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | XDP/USDC | 100 | 744,484 | 0.015500 | 59980829 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 722,511 | 0.046393 | 59980829 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| pancakeswap_v3 | WETH/USDC | 500 | 719,847 | 1,737.772407 | 59980830 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/SAPIEN | 4615 | 716,011 | 24.611087 | 59980829 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/MORPHO | 3000 | 712,108 | 1,107.130501 | 59980829 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 692,254 | 1,740.788311 | 59980829 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 614,893 | 1,738.182396 | 59980853 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 589,062 | 0.798440 | 59980829 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 583,831 | 0.428649 | 59980829 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 551,509 | 4,709,625.330327 | 59980829 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 533,400 | 4,262.693180 | 59980829 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,939 | 1.386531 | 59980829 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 501,158 | 536,406.245313 | 59980829 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 491,227 | 0.030997 | 59980829 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | USDC/USDT | 8 | 456,488 | 1.001622 | 59980832 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 450,707 | 0.064225 | 59980844 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v2 | WETH/NPC | 3000 | 450,009 | 189,269.428926 | 59980829 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 435,570 | 0.000007 | 59980829 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3058 | 386,073 | 1,107.284350 | 59980829 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 381,129 | 23.783111 | 59980829 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 375,826 | 860,235.149070 | 59980829 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 370,053 | 368.176484 | 59980829 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | AWE/USDC | 3000 | 366,592 | 0.055882 | 59980829 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome_slipstream | WETH/VVV | 2721 | 355,554 | 83.958971 | 59980829 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | VIRTUAL/WETH | 10000 | 355,473 | 0.000230 | 59980829 | `0x21594b992F68495dD28d605834b58889d0a727c7` |

## Recherche d'opportunités
- Cycles : 36851 ; routes examinées : 469481740 ; candidats optimisés : 573617 ; net attendu > 0 : 831 ; dernier cycle 170.6 ms
- Rejets (moteur) : {'spread_below_threshold': 460054061, 'liquidity_below_min': 5349674, 'negative_expected_net': 572786, 'cycle_budget_exhausted': 59472, 'pool_quarantined': 54560, 'borrow_bound_too_small': 51278, 'no_price_reference': 279}
- Enregistrements de la session : 322191 ; net attendu > 0 : 831 ; simulés (eth_call de la vraie tx) : 74 (ok 18, échec 56) ; étiquettes ghost N+1 : 25/54 positives
- Décisions : {'REJECTED': 322191} ; motifs de rejet : {'below_safety_margin': 590, 'negative_expected_net': 321360, 'p_lower_below_threshold': 823, 'price_impact': 145, 'reliability_not_demonstrated': 8, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 1, 'simulation_failed': 56, 'stale_data': 103}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59931575 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 686.457140 USDC | 0.119872 USDC | 0.000000 USDC | 0.004198 USDC | 0.115674 USDC (0.1064 €) | — | 1.69 | 0.111 (n=380) | REJECTED | below_safety_margin(115674<137291), p_lower_below_threshold(0.11<0.75) |
| 59931589 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 686.457140 USDC | 0.119872 USDC | 0.000000 USDC | 0.004198 USDC | 0.115674 USDC (0.1064 €) | — | 1.69 | 0.111 (n=380) | REJECTED | below_safety_margin(115674<137291), p_lower_below_threshold(0.11<0.75) |
| 59931575 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.397053 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000067 WETH (0.1063 €) | — | 1.68 | 0.111 (n=380) | REJECTED | below_safety_margin(66717612332529<79410520469949), p_lower_below_threshold(0.11<0.75) |
| 59931589 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.397053 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000067 WETH (0.1063 €) | — | 1.68 | 0.111 (n=380) | REJECTED | below_safety_margin(66717612332529<79410520469949), p_lower_below_threshold(0.11<0.75) |
| 59975591 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 363.997118 USDC | 0.107146 USDC | 0.000000 USDC | 0.008095 USDC | 0.099051 USDC (0.0911 €) | — | 2.72 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.005606 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.0910 €) | — | 2.85 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.216239 WETH | 0.000061 WETH | 0.000000 WETH | 0.000005 WETH | 0.000057 WETH (0.0909 €) | -0.000001 WETH | 2.61 | 0.273 (n=1646) | REJECTED | sim_below_estimate(3842308596892<61157677787177), simulated_net_nonpositive, p_lower_below_threshold(0.27<0.75) |
| 59975591 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.269412 WETH | 0.000060 WETH | 0.000000 WETH | 0.000005 WETH | 0.000056 WETH (0.0894 €) | — | 2.06 | 0.273 (n=1646) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.27<0.75) |
| 59975591 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.007429 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.0893 €) | — | 2.11 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 497.623320 USDC | 0.105172 USDC | 0.000000 USDC | 0.008095 USDC | 0.097077 USDC (0.0893 €) | — | 1.95 | 0.273 (n=1646) | REJECTED | below_safety_margin(97077<99524), p_lower_below_threshold(0.27<0.75) |
| 59975591 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.268883 WETH | 0.000060 WETH | 0.000000 WETH | 0.000005 WETH | 0.000055 WETH (0.0886 €) | — | 2.05 | 0.273 (n=1646) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.27<0.75) |
| 59975591 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.007423 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.0882 €) | — | 2.09 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 480.766129 USDC | 0.103900 USDC | 0.000000 USDC | 0.008095 USDC | 0.095805 USDC (0.0881 €) | — | 1.99 | 0.273 (n=1646) | REJECTED | below_safety_margin(95805<96153), p_lower_below_threshold(0.27<0.75) |
| 59975591 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.179246 WETH | 0.000049 WETH | 0.000000 WETH | 0.000005 WETH | 0.000045 WETH (0.0720 €) | — | 2.50 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 311.356022 USDC | 0.086123 USDC | 0.000000 USDC | 0.008095 USDC | 0.078028 USDC (0.0718 €) | — | 2.51 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004843 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0717 €) | — | 2.60 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 400.951842 USDC | 0.075627 USDC | 0.000000 USDC | 0.008095 USDC | 0.067532 USDC (0.0621 €) | — | 1.68 | 0.273 (n=1646) | REJECTED | below_safety_margin(67532<80190), p_lower_below_threshold(0.27<0.75) |
| 59975591 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.164226 WETH | 0.000036 WETH | 0.000000 WETH | 0.000005 WETH | 0.000032 WETH (0.0507 €) | — | 1.92 | 0.175 (n=44) | REJECTED | below_safety_margin(31512223146885<32845151877118), p_lower_below_threshold(0.18<0.75) |
| 59975591 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004567 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0506 €) | — | 1.95 | 0.175 (n=44) | REJECTED | below_safety_margin(89<91), p_lower_below_threshold(0.18<0.75) |
| 59975591 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 272.153238 USDC | 0.062966 USDC | 0.000000 USDC | 0.008499 USDC | 0.054467 USDC (0.0501 €) | — | 2.00 | 0.175 (n=44) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 59931575 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 283.558757 USDC | 0.042818 USDC | 0.000000 USDC | 0.003935 USDC | 0.038883 USDC (0.0358 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(38883<56711), p_lower_below_threshold(0.10<0.75) |
| 59931589 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 283.558757 USDC | 0.042818 USDC | 0.000000 USDC | 0.003935 USDC | 0.038883 USDC (0.0358 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(38883<56711), p_lower_below_threshold(0.10<0.75) |
| 59931575 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.163619 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0357 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(22426759358077<32723734311580), p_lower_below_threshold(0.10<0.75) |
| 59931589 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.163619 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0357 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(22426759358077<32723734311580), p_lower_below_threshold(0.10<0.75) |
| 59945018 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 404.546288 USDC | 0.038086 USDC | 0.000000 USDC | 0.003925 USDC | 0.034161 USDC (0.0314 €) | — | 0.84 | 0.110 (n=381) | REJECTED | below_safety_margin(34161<80909), p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 8644 ; taux observé 0.229 ; borne inférieure crédible (0.9) 0.224 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
