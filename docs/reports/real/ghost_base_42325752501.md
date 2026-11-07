# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T05:31:15+00:00 ; durée 220.38 min ; blocs 54129350 → 54195430 (11388 vus)

## Connexion
- Requêtes RPC : 145279 ; erreurs : 450 ; latence p50/p95 : 281.7/1,814.2 ms
- Rafraîchissements d'état : 11388 ; âge des données au dernier bloc : 9.07 s ; changements de frais LP observés (pools à frais dynamiques) : 4287
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
| uniswap_v3 | WETH/USDC | 3000 | 145,980,868 | 2,241.228568 | 54195456 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,769,793 | 0.029588 | 54195456 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,318,747 | 0.000013 | 54195456 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,164,445 | 0.029513 | 54195456 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,021,604 | 2,246.526267 | 54195456 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,377,279 | 107.857204 | 54195456 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,415,633 | 0.001553 | 54195456 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,886,612 | 1.644179 | 54195456 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,761,249 | 0.029577 | 54195456 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,229,206 | 2,245.966846 | 54195456 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,992,347 | 0.998508 | 54195456 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,324,723 | 42,528.152304 | 54195456 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,204,243 | 2,246.135969 | 54195456 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,560,538 | 0.029528 | 54195456 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,095,550 | 1,159,503.991138 | 54195456 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,740,794 | 0.006969 | 54195456 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,739,858 | 0.000013 | 54195456 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,660,214 | 0.000000 | 54195456 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,629,680 | 0.000013 | 54195456 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,619,789 | 0.016140 | 54195456 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54195456 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,533,077 | 433.883049 | 54195456 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,507,427 | 0.000013 | 54195456 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,378 | 0.819350 | 54195456 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,391,124 | 3,692.634899 | 54195456 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,326,724 | 2,245.657106 | 54195456 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,325,171 | 2,247.847477 | 54195456 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,274,805 | 14,655.431427 | 54195456 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,195,249 | 2,246.339726 | 54195456 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,702 | 76.955062 | 54195456 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,109,818 | 36,211,011.540682 | 54195456 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,046,587 | 107.127187 | 54195456 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,027,473 | 557,565.003975 | 54195456 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,000,912 | 0.000000 | 54195456 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 998,664 | 22,522,087.949012 | 54195456 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 989,490 | 19.537275 | 54195456 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 938,935 | 1,066.769466 | 54195456 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,474 | 2,228.788739 | 54195456 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 925,178 | 0.000013 | 54195456 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 923,697 | 73.442759 | 54195456 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 889,631 | 96,816.816987 | 54195456 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 807,342 | 0.048078 | 54195456 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 801,303 | 3,680.501020 | 54195456 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 799,848 | 20.896985 | 54195456 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 792,426 | 0.056207 | 54195456 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,328 | 0.799699 | 54195456 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 716,648 | 0.565131 | 54195456 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 699,638 | 4,856,265.197346 | 54195456 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 685,333 | 0.000253 | 54195456 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 668,389 | 0.560019 | 54195456 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 661,207 | 145,232.120423 | 54195456 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 656,514 | 0.000008 | 54195456 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 630,647 | 559,370.678107 | 54195456 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 588,963 | 2.472900 | 54195456 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 581,829 | 0.040239 | 54195456 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 527,659 | 0.079189 | 54195456 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 525,900 | 1,067.072916 | 54195456 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 521,575 | 896,430.388148 | 54195456 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 517,246 | 2,245.765678 | 54195456 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 514,204 | 6,966.852916 | 54195456 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 11452 ; routes examinées : 204349488 ; candidats optimisés : 637183 ; net attendu > 0 : 131 ; dernier cycle 308.7 ms
- Rejets (moteur) : {'spread_below_threshold': 201565947, 'liquidity_below_min': 2125817, 'negative_expected_net': 637052, 'borrow_bound_too_small': 11448, 'pool_quarantined': 8776, 'cycle_budget_exhausted': 317}
- Enregistrements de la session : 637183 ; net attendu > 0 : 131 ; simulés (eth_call de la vraie tx) : 29 (ok 17, échec 12) ; étiquettes ghost N+1 : 1/25 positives
- Décisions : {'REJECTED': 637183} ; motifs de rejet : {'below_safety_margin': 49, 'negative_expected_net': 637052, 'p_lower_below_threshold': 119, 'price_impact': 23, 'reliability_not_demonstrated': 12, 'simulation_failed': 12, 'stale_data': 23}

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
