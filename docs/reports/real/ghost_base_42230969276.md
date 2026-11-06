# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T14:38:37+00:00 ; durée 27.53 min ; blocs 53919422 → 53927658 (1050 vus)

## Connexion
- Requêtes RPC : 16063 ; erreurs : 0 ; latence p50/p95 : 354.6/1,753.2 ms
- Rafraîchissements d'état : 1050 ; âge des données au dernier bloc : 9.6 s ; changements de frais LP observés (pools à frais dynamiques) : 1201
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1011 ; cycles déclenchés par événement : 405 ; avance médiane sur le rafraîchissement multicall : 707 ms
- Gaz : base fee 0.005641 gwei ; prix ETH (pool le plus profond) : 2,232.31 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 484 pools, 280 jetons, 17898 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 103, aerodrome 200, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3743 (énumérés 302, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 3 → gardés 484 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2229.592504, 'cbBTC': 75521.601442, 'AERO': 0.600396}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,727,256 | 2,233.367523 | 53927689 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,699,264 | 0.029537 | 53927689 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,343,649 | 0.000013 | 53927689 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,127,942 | 0.029461 | 53927689 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,982,402 | 2,238.857550 | 53927689 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,371,495 | 107.005209 | 53927689 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,428,637 | 0.001566 | 53927689 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,883,533 | 1.652507 | 53927689 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,720,238 | 0.029545 | 53927689 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,151,686 | 2,238.864436 | 53927689 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,983,436 | 0.998492 | 53927689 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,300,484 | 42,812.471838 | 53927689 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 1399 | 3,199,632 | 2,238.843579 | 53927689 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2520 | 2,551,555 | 0.029478 | 53927689 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,077,286 | 1,170,614.944842 | 53927689 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,797,987 | 0.007346 | 53927689 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,732,653 | 0.000013 | 53927689 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,654,233 | 0.000013 | 53927689 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,645,315 | 0.016581 | 53927689 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,640,281 | 0.000000 | 53927689 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,161 | 1.444757 | 53927689 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,529,035 | 430.763564 | 53927689 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,525,804 | 0.000013 | 53927689 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,125 | 0.818407 | 53927689 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,381,142 | 3,703.839957 | 53927689 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,324,006 | 2,232.456009 | 53927689 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,322,172 | 2,233.031808 | 53927689 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,273,427 | 14,604.073318 | 53927689 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,169,950 | 2,238.786732 | 53927689 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,886 | 76.929838 | 53927689 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,094,251 | 37,146,336.463410 | 53927689 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,047,506 | 107.061298 | 53927689 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,022,378 | 559,380.869257 | 53927689 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,021,481 | 0.000000 | 53927689 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 997,750 | 22,433,261.257503 | 53927689 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 984,357 | 19.815448 | 53927689 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 935,007 | 2,225.576719 | 53927689 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 934,190 | 1,068.719043 | 53927689 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 921,988 | 0.000013 | 53927689 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 903,268 | 76.802295 | 53927689 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 859,257 | 102,958.418091 | 53927689 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 838,325 | 0.000529 | 53927689 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4665 | 814,416 | 20.343113 | 53927689 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | USDC/VVV | 3000 | 808,700 | 0.047794 | 53927689 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 796,766 | 3,681.640183 | 53927689 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 790,672 | 0.055947 | 53927689 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 757,304 | 0.799699 | 53927689 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 725,935 | 0.580842 | 53927689 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,404 | 4,890,083.098241 | 53927689 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 688,495 | 0.000258 | 53927689 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 659,460 | 144,843.140821 | 53927689 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 655,745 | 0.540158 | 53927689 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 652,688 | 0.000008 | 53927689 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2186 | 627,036 | 555,540.481849 | 53927689 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 598,544 | 0.913997 | 53927689 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 586,717 | 2.472301 | 53927689 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 561,737 | 0.038217 | 53927689 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 530,317 | 862,520.062338 | 53927689 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 527,984 | 0.079279 | 53927689 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 522,516 | 1,068.326975 | 53927689 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 1454 ; routes examinées : 26023692 ; candidats optimisés : 108445 ; net attendu > 0 : 80 ; dernier cycle 266.5 ms
- Rejets (moteur) : {'spread_below_threshold': 25550608, 'liquidity_below_min': 362918, 'negative_expected_net': 108365, 'borrow_bound_too_small': 1453, 'cycle_budget_exhausted': 268}
- Enregistrements de la session : 108445 ; net attendu > 0 : 80 ; simulés (eth_call de la vraie tx) : 3 (ok 3, échec 0) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 108445} ; motifs de rejet : {'below_safety_margin': 77, 'negative_expected_net': 108365, 'p_lower_below_threshold': 79, 'reliability_not_demonstrated': 1, 'stale_data': 33}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53927539 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 62.319997 USDC | 0.016706 USDC | 0.000000 USDC | 0.007595 USDC | 0.009111 USDC (0.0084 €) | — | 1.46 | 0.169 (n=1026) | REJECTED | below_safety_margin(9111<12463), stale_data(5017ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53927539 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.027835 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0083 €) | — | 1.46 | 0.169 (n=1026) | REJECTED | below_safety_margin(4065668304859<5566941738758), stale_data(5010ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53926197 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 30.409808 USDC | 0.011342 USDC | 0.000000 USDC | 0.005141 USDC | 0.006201 USDC (0.0057 €) | 0.006201 USDC | 2.04 | 0.048 (n=242) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 53921994 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 164.696992 USDC | 0.011222 USDC | 0.000000 USDC | 0.005035 USDC | 0.006187 USDC (0.0057 €) | — | 0.38 | 0.048 (n=242) | REJECTED | below_safety_margin(6187<32939), p_lower_below_threshold(0.05<0.75) |
| 53921994 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 164.696992 USDC | 0.011222 USDC | 0.000000 USDC | 0.005035 USDC | 0.006187 USDC (0.0057 €) | — | 0.38 | 0.048 (n=242) | REJECTED | below_safety_margin(6187<32939), p_lower_below_threshold(0.05<0.75) |
| 53921994 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.074266 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0057 €) | — | 0.37 | 0.048 (n=242) | REJECTED | below_safety_margin(2772403998773<14853259609927), p_lower_below_threshold(0.05<0.75) |
| 53921994 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.074266 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0057 €) | — | 0.37 | 0.048 (n=242) | REJECTED | below_safety_margin(2772403998773<14853259609927), p_lower_below_threshold(0.05<0.75) |
| 53927539 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 54.545633 USDC | 0.012895 USDC | 0.000000 USDC | 0.007595 USDC | 0.005300 USDC (0.0049 €) | — | 0.97 | 0.169 (n=1026) | REJECTED | below_safety_margin(5300<10909), stale_data(5131ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53927539 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.024413 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0048 €) | — | 0.97 | 0.169 (n=1026) | REJECTED | below_safety_margin(2361562323000<4882632775584), stale_data(5124ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53927539 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 52.896241 USDC | 0.012104 USDC | 0.000000 USDC | 0.007595 USDC | 0.004509 USDC (0.0041 €) | — | 0.85 | 0.169 (n=1026) | REJECTED | below_safety_margin(4509<10579), stale_data(5175ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53927539 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.023842 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0041 €) | — | 0.84 | 0.169 (n=1026) | REJECTED | below_safety_margin(2007579166666<4768340883255), stale_data(5168ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53927539 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 35.220252 USDC | 0.012018 USDC | 0.000000 USDC | 0.007595 USDC | 0.004423 USDC (0.0041 €) | — | 1.26 | 0.236 (n=403) | REJECTED | below_safety_margin(4423<7044), stale_data(4908ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 53927539 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.015860 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0040 €) | — | 1.24 | 0.236 (n=403) | REJECTED | below_safety_margin(1970796398355<3172005933325), stale_data(4901ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 53927539 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 48.562830 USDC | 0.010947 USDC | 0.000000 USDC | 0.007595 USDC | 0.003352 USDC (0.0031 €) | — | 0.69 | 0.236 (n=403) | REJECTED | below_safety_margin(3352<9712), stale_data(5190ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 53927539 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.021846 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0031 €) | — | 0.68 | 0.236 (n=403) | REJECTED | below_safety_margin(1490950275762<4369161796510), stale_data(5183ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 53926910 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 112.195826 USDC | 0.007563 USDC | 0.000000 USDC | 0.005006 USDC | 0.002557 USDC (0.0024 €) | — | 0.23 | 0.053 (n=82) | REJECTED | below_safety_margin(2557<22439), p_lower_below_threshold(0.05<0.75) |
| 53923061 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 26.329986 USDC | 0.003625 USDC | 0.000000 USDC | 0.001134 USDC | 0.002491 USDC (0.0023 €) | — | 0.95 | 0.169 (n=1026) | REJECTED | below_safety_margin(2491<5265), stale_data(4225ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53923061 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.011872 WETH | 0.000002 WETH | 0.000000 WETH | 0.000001 WETH | 0.000001 WETH (0.0023 €) | — | 0.94 | 0.169 (n=1026) | REJECTED | below_safety_margin(1116903815319<2374312355251), stale_data(4231ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53927540 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 11.367468 USDC | 0.009287 USDC | 0.000000 USDC | 0.006910 USDC | 0.002377 USDC (0.0022 €) | 0.002377 USDC | 2.09 | 0.218 (n=187) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 53927540 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.005089 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0022 €) | 0.000001 WETH | 2.07 | 0.218 (n=187) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 53927539 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 31.798125 USDC | 0.009824 USDC | 0.000000 USDC | 0.007595 USDC | 0.002229 USDC (0.0021 €) | — | 0.70 | 0.236 (n=403) | REJECTED | below_safety_margin(2229<6359), stale_data(4937ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 53927539 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.014295 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0020 €) | — | 0.69 | 0.236 (n=403) | REJECTED | below_safety_margin(989326917602<2859015192102), stale_data(4931ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 53927539 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 31.308381 USDC | 0.009373 USDC | 0.000000 USDC | 0.007595 USDC | 0.001778 USDC (0.0016 €) | — | 0.57 | 0.169 (n=1026) | REJECTED | below_safety_margin(1778<6261), stale_data(4951ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53927539 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.013815 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 0.57 | 0.169 (n=1026) | REJECTED | below_safety_margin(786713084761<2762991563488), stale_data(4944ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53927540 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→cbBTC | 0.000486 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.41 | 0.169 (n=1026) | REJECTED | below_safety_margin(2<9), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 5849 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
