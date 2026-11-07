# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T05:53:28+00:00 ; durée 242.6 min ; blocs 54129350 → 54202091 (12670 vus)

## Connexion
- Requêtes RPC : 160825 ; erreurs : 468 ; latence p50/p95 : 283.7/1,801.2 ms
- Rafraîchissements d'état : 12670 ; âge des données au dernier bloc : 9.73 s ; changements de frais LP observés (pools à frais dynamiques) : 4598
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 165 ; cycles déclenchés par événement : 65 ; avance médiane sur le rafraîchissement multicall : 543 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,241.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 480 pools, 282 jetons, 17844 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 100, aerodrome 199, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 170 (rejetés 2) → 575 jetons ; pools candidats 3720 (énumérés 297, par paires 0), mesurés 483, sous le plancher de 10000.0 $ : 3 → gardés 480 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2239.687391, 'cbBTC': 75912.79678, 'AERO': 0.607077}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,988,625 | 2,241.227750 | 54202118 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,728,501 | 0.029582 | 54202118 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,319,465 | 0.000013 | 54202118 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,165,195 | 0.029513 | 54202118 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,021,598 | 2,246.303937 | 54202118 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,377,990 | 107.836337 | 54202118 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,418,660 | 0.001554 | 54202118 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,888,838 | 1.642682 | 54202118 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,761,642 | 0.029581 | 54202118 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,229,256 | 2,247.088083 | 54202118 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,993,239 | 0.998503 | 54202118 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,323,673 | 42,554.999720 | 54202118 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,204,249 | 2,246.997657 | 54202118 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,560,702 | 0.029528 | 54202118 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,095,549 | 1,159,503.991138 | 54202118 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,741,684 | 0.006973 | 54202118 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,740,121 | 0.000013 | 54202118 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,660,205 | 0.000000 | 54202118 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,630,154 | 0.000013 | 54202118 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,616,148 | 0.016124 | 54202118 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54202118 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,532,925 | 434.028053 | 54202118 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,507,635 | 0.000013 | 54202118 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,378 | 0.819350 | 54202118 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,391,902 | 3,689.155097 | 54202118 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,326,724 | 2,245.008705 | 54202118 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,325,172 | 2,250.281624 | 54202118 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,274,784 | 14,662.102976 | 54202118 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,195,295 | 2,246.339726 | 54202118 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,702 | 76.955062 | 54202118 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,109,816 | 36,211,122.992199 | 54202118 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,046,723 | 107.127187 | 54202118 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,027,473 | 557,565.003975 | 54202118 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,000,911 | 0.000000 | 54202118 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 998,652 | 22,522,526.287595 | 54202118 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 986,318 | 19.721279 | 54202118 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 938,776 | 1,067.021896 | 54202118 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 937,463 | 2,228.788739 | 54202118 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 925,345 | 0.000013 | 54202118 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 924,061 | 73.384856 | 54202118 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 886,573 | 97,485.907876 | 54202118 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 807,467 | 0.048078 | 54202118 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 801,668 | 3,680.501020 | 54202118 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 799,848 | 20.896985 | 54202118 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 793,873 | 0.056423 | 54202118 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,328 | 0.799699 | 54202118 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 716,646 | 0.565914 | 54202118 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 699,237 | 4,861,843.396116 | 54202118 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 685,333 | 0.000253 | 54202118 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 668,913 | 0.560849 | 54202118 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 659,265 | 146,090.414622 | 54202118 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 656,908 | 0.000008 | 54202118 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 630,647 | 559,334.724274 | 54202118 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 588,962 | 2.472900 | 54202118 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 579,504 | 0.039990 | 54202118 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 526,321 | 0.078881 | 54202118 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 525,803 | 1,067.082496 | 54202118 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 520,888 | 898,254.942830 | 54202118 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 517,249 | 2,247.180186 | 54202118 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 514,204 | 6,966.851546 | 54202118 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 12734 ; routes examinées : 227225496 ; candidats optimisés : 688860 ; net attendu > 0 : 133 ; dernier cycle 302.1 ms
- Rejets (moteur) : {'spread_below_threshold': 224035646, 'liquidity_below_min': 2479167, 'negative_expected_net': 688727, 'borrow_bound_too_small': 12730, 'pool_quarantined': 8776, 'cycle_budget_exhausted': 317}
- Enregistrements de la session : 688860 ; net attendu > 0 : 133 ; simulés (eth_call de la vraie tx) : 29 (ok 17, échec 12) ; étiquettes ghost N+1 : 1/25 positives
- Décisions : {'REJECTED': 688860} ; motifs de rejet : {'below_safety_margin': 51, 'negative_expected_net': 688727, 'p_lower_below_threshold': 121, 'price_impact': 23, 'reliability_not_demonstrated': 12, 'simulation_failed': 12, 'stale_data': 24}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54155415 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 169.469178 USDC | 12.894019 USDC | 0.000000 USDC | 0.006742 USDC | 12.887277 USDC (11.8563 €) | — | 760.45 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.075545 WETH | 0.005748 WETH | 0.000000 WETH | 0.000003 WETH | 0.005745 WETH (11.8455 €) | 0.005745 WETH | 760.45 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.074633 WETH | 0.005676 WETH | 0.000000 WETH | 0.000003 WETH | 0.005673 WETH (11.6971 €) | 0.005673 WETH | 760.10 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 167.251780 USDC | 12.719616 USDC | 0.000000 USDC | 0.006742 USDC | 12.712874 USDC (11.6958 €) | — | 760.10 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 153.424791 USDC | 11.717144 USDC | 0.000000 USDC | 0.006742 USDC | 11.710402 USDC (10.7736 €) | — | 763.27 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.068422 WETH | 0.005225 WETH | 0.000000 WETH | 0.000003 WETH | 0.005222 WETH (10.7684 €) | 0.005222 WETH | 763.27 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 154.017547 USDC | 11.644573 USDC | 0.000000 USDC | 0.006742 USDC | 11.637831 USDC (10.7068 €) | — | 755.62 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.068716 WETH | 0.005195 WETH | 0.000000 WETH | 0.000003 WETH | 0.005192 WETH (10.7062 €) | — | 755.62 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.063002 WETH | 0.004807 WETH | 0.000000 WETH | 0.000003 WETH | 0.004804 WETH (9.9052 €) | — | 762.49 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 139.444678 USDC | 10.639227 USDC | 0.000000 USDC | 0.006742 USDC | 10.632485 USDC (9.7819 €) | — | 762.49 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.060834 WETH | 0.004521 WETH | 0.000000 WETH | 0.000003 WETH | 0.004518 WETH (9.3168 €) | — | 742.76 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 136.092658 USDC | 10.115126 USDC | 0.000000 USDC | 0.006742 USDC | 10.108384 USDC (9.2997 €) | — | 742.76 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.058585 WETH | 0.004483 WETH | 0.000000 WETH | 0.000003 WETH | 0.004480 WETH (9.2378 €) | — | 764.73 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 129.884350 USDC | 9.939684 USDC | 0.000000 USDC | 0.007083 USDC | 9.932601 USDC (9.1380 €) | — | 764.73 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 93.273704 USDC | 7.671126 USDC | 0.000000 USDC | 0.006742 USDC | 7.664384 USDC (7.0512 €) | — | 821.71 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH | 0.041580 WETH | 0.003420 WETH | 0.000000 WETH | 0.000003 WETH | 0.003417 WETH (7.0449 €) | — | 821.71 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH | 0.041072 WETH | 0.003377 WETH | 0.000000 WETH | 0.000003 WETH | 0.003373 WETH (6.9559 €) | — | 821.35 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 92.037099 USDC | 7.566255 USDC | 0.000000 USDC | 0.006742 USDC | 7.559513 USDC (6.9548 €) | — | 821.35 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH | 0.034748 WETH | 0.002865 WETH | 0.000000 WETH | 0.000003 WETH | 0.002862 WETH (5.9015 €) | — | 823.67 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 77.401820 USDC | 6.388020 USDC | 0.000000 USDC | 0.006742 USDC | 6.381278 USDC (5.8708 €) | — | 824.44 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH | 0.034520 WETH | 0.002849 WETH | 0.000000 WETH | 0.000003 WETH | 0.002846 WETH (5.8681 €) | — | 824.43 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 77.704476 USDC | 6.353211 USDC | 0.000000 USDC | 0.006742 USDC | 6.346469 USDC (5.8388 €) | — | 816.74 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH | 0.034669 WETH | 0.002835 WETH | 0.000000 WETH | 0.000003 WETH | 0.002832 WETH (5.8385 €) | — | 816.74 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 76.848831 USDC | 6.336508 USDC | 0.000000 USDC | 0.006742 USDC | 6.329766 USDC (5.8234 €) | — | 823.66 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54155415 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→cbXRP→[aerodrome_slipstream]→WETH | 0.029515 WETH | 0.002440 WETH | 0.000000 WETH | 0.000003 WETH | 0.002437 WETH (5.0256 €) | — | 825.79 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 5948 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
