# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T20:36:43+00:00 ; durée 107.24 min ; blocs 53471207 → 53474426 (3128 vus)

## Connexion
- Requêtes RPC : 37183 ; erreurs : 343 ; latence p50/p95 : 164.8/1,217.4 ms
- Rafraîchissements d'état : 3129 ; âge des données au dernier bloc : 1.78 s ; changements de frais LP observés (pools à frais dynamiques) : 3321
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 25564 ; cycles déclenchés par événement : 2456 ; avance médiane sur le rafraîchissement multicall : 410 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,285.38 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 493 pools, 285 jetons, 19448 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 496, sous le plancher de 10000.0 $ : 3 → gardés 493 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2294.78828, 'cbBTC': 77607.185431, 'AERO': 0.633493}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,369,858 | 2,285.382007 | 53474426 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,406,791 | 0.029387 | 53474426 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,202,861 | 0.029450 | 53474426 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,068,746 | 0.000013 | 53474426 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,036,397 | 2,283.869136 | 53474426 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,793,145 | 100.799869 | 53474426 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,623,932 | 0.001571 | 53474426 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,396,791 | 1.586499 | 53474426 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,835,125 | 0.029394 | 53474426 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,167,045 | 2,284.289933 | 53474426 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,091,342 | 0.999899 | 53474426 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,877,228 | 2,284.226928 | 53474426 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,423,299 | 41,710.353180 | 53474426 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,709,717 | 0.029436 | 53474426 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,170,837 | 1,123,653.677423 | 53474426 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,140,513 | 100.810607 | 53474426 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,816,515 | 0.000013 | 53474426 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,736,504 | 0.017772 | 53474426 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,680,019 | 0.000000 | 53474426 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,628,580 | 0.000013 | 53474426 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,556,324 | 0.000013 | 53474426 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53474426 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,554,389 | 440.701514 | 53474426 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,507,675 | 2,285.685861 | 53474426 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,495,436 | 0.005887 | 53474426 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,800 | 0.821850 | 53474426 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,422,631 | 3,621.691411 | 53474426 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,340,637 | 2,289.647170 | 53474426 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,337,324 | 2,283.840347 | 53474426 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,294,695 | 14,975.454116 | 53474426 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,197,016 | 0.000013 | 53474426 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,158,637 | 72.384430 | 53474426 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,124,899 | 36,832,100.803973 | 53474426 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,058,519 | 544,327.256219 | 53474426 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,051,133 | 0.000000 | 53474426 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,033,972 | 21,950,664.012046 | 53474426 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 998,052 | 19.056888 | 53474426 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 957,523 | 101.018184 | 53474426 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 949,870 | 88,309.759098 | 53474426 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/MORPHO | 3000 | 948,645 | 1,053.781333 | 53474426 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 942,267 | 70.510063 | 53474426 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 933,524 | 1,250,216.725622 | 53474426 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 928,315 | 2,282.122456 | 53474426 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 903,395 | 0.044152 | 53474426 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 877,744 | 0.000554 | 53474426 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 845,517 | 3,646.232124 | 53474426 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 821,703 | 20.040543 | 53474426 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,560 | 0.056853 | 53474426 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 775,720 | 0.799140 | 53474426 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,671 | 0.590248 | 53474426 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 728,211 | 0.000258 | 53474426 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 716,761 | 4,807,730.281722 | 53474426 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 672,477 | 0.000008 | 53474426 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 667,215 | 148,123.723824 | 53474426 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 665,070 | 0.555673 | 53474426 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 661,421 | 2.343097 | 53474426 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 650,524 | 548,623.648185 | 53474426 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 613,882 | 0.914716 | 53474426 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 585,774 | 0.086846 | 53474426 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 564,833 | 0.038584 | 53474426 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 5584 ; routes examinées : 108597632 ; candidats optimisés : 266606 ; net attendu > 0 : 325 ; dernier cycle 99.8 ms
- Rejets (moteur) : {'spread_below_threshold': 107258016, 'liquidity_below_min': 1056111, 'negative_expected_net': 266281, 'unquotable': 11160, 'borrow_bound_too_small': 5580, 'cycle_budget_exhausted': 159}
- Enregistrements de la session : 266606 ; net attendu > 0 : 325 ; simulés (eth_call de la vraie tx) : 10 (ok 5, échec 5) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 266606} ; motifs de rejet : {'below_safety_margin': 301, 'negative_expected_net': 266281, 'p_lower_below_threshold': 323, 'reliability_not_demonstrated': 2, 'simulation_failed': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53472395 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.026252 WETH | 0.000056 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1137 €) | — | 20.53 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53472362 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.020014 WETH | 0.000033 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0642 €) | — | 15.21 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53474176 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000502 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0243 €) | — | 6.77 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000502 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0243 €) | — | 6.77 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 37.177276 USDC | 0.033271 USDC | 0.000000 USDC | 0.006868 USDC | 0.026403 USDC (0.0243 €) | 0.026403 USDC | 7.10 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 37.177276 USDC | 0.033271 USDC | 0.000000 USDC | 0.006868 USDC | 0.026403 USDC (0.0243 €) | 0.026403 USDC | 7.10 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000396 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0200 €) | — | 7.06 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000396 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0200 €) | — | 7.06 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 34.134904 USDC | 0.028597 USDC | 0.000000 USDC | 0.006868 USDC | 0.021729 USDC (0.0200 €) | 0.021729 USDC | 6.37 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 34.134904 USDC | 0.028597 USDC | 0.000000 USDC | 0.006868 USDC | 0.021729 USDC (0.0200 €) | — | 6.37 | 0.291 (n=315) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 30.181602 USDC | 0.020199 USDC | 0.000000 USDC | 0.006868 USDC | 0.013331 USDC (0.0123 €) | 0.013331 USDC | 4.42 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 30.181602 USDC | 0.020199 USDC | 0.000000 USDC | 0.006868 USDC | 0.013331 USDC (0.0123 €) | — | 4.42 | 0.291 (n=315) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 53474176 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000331 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0122 €) | — | 5.14 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000331 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0122 €) | — | 5.14 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53473234 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000756 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0100 €) | — | 1.85 | 0.185 (n=852) | REJECTED | below_safety_margin(14<15), p_lower_below_threshold(0.18<0.75) |
| 53473234 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000756 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0100 €) | — | 1.85 | 0.185 (n=852) | REJECTED | below_safety_margin(14<15), p_lower_below_threshold(0.18<0.75) |
| 53473234 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.026637 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0097 €) | — | 1.72 | 0.185 (n=852) | REJECTED | below_safety_margin(4588171224948<5327432158996), p_lower_below_threshold(0.18<0.75) |
| 53473234 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.026637 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0097 €) | — | 1.72 | 0.185 (n=852) | REJECTED | below_safety_margin(4588171224948<5327432158996), p_lower_below_threshold(0.18<0.75) |
| 53474015 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000754 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0093 €) | — | 1.72 | 0.185 (n=853) | REJECTED | below_safety_margin(13<15), p_lower_below_threshold(0.18<0.75) |
| 53474176 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000377 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0093 €) | — | 3.45 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000377 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0093 €) | — | 3.45 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474015 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.026613 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0090 €) | — | 1.61 | 0.185 (n=853) | REJECTED | below_safety_margin(4297430450779<5322609667007), p_lower_below_threshold(0.18<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 29.387749 USDC | 0.016344 USDC | 0.000000 USDC | 0.006868 USDC | 0.009476 USDC (0.0087 €) | — | 3.22 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 29.387749 USDC | 0.016344 USDC | 0.000000 USDC | 0.006868 USDC | 0.009476 USDC (0.0087 €) | — | 3.22 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53471700 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.168881 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | — | 0.24 | 0.185 (n=852) | REJECTED | below_safety_margin(4067722060797<33776255979005), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 4911 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
