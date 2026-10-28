# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T08:36:05+00:00 ; durée 185.37 min ; blocs 53188044 → 53193606 (5407 vus)

## Connexion
- Requêtes RPC : 63618 ; erreurs : 100 ; latence p50/p95 : 205.0/1,456.0 ms
- Rafraîchissements d'état : 5408 ; âge des données au dernier bloc : 1.52 s ; changements de frais LP observés (pools à frais dynamiques) : 4877
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 22306 ; cycles déclenchés par événement : 3885 ; avance médiane sur le rafraîchissement multicall : 657 ms
- Gaz : base fee 0.005165 gwei ; prix ETH (pool le plus profond) : 2,372.93 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 521 pools, 302 jetons, 18962 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 121 (quarantaine 1), aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 184 (rejetés 2) → 589 jetons ; pools candidats 3762 (énumérés 330, par paires 0), mesurés 523, sous le plancher de 10000.0 $ : 2 → gardés 521 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2356.459313, 'cbBTC': 80857.377983, 'AERO': 0.694089}
- Pools en quarantaine : 1 — aerodrome_slipstream:VIRTUAL/WETH@0x3f0296: simulation failed ×5 (model/chain mismatch) — until block 53193610

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,565,728 | 2,372.926435 | 53193606 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,829,859 | 0.029151 | 53193606 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,669,549 | 0.000012 | 53193606 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,571,203 | 0.029117 | 53193606 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,461,529 | 2,379.041661 | 53193606 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,299,575 | 99.247759 | 53193606 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,111,533 | 0.001652 | 53193606 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,872,542 | 1.408871 | 53193606 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,783,477 | 0.029152 | 53193606 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 1041 | 5,074,350 | 2,379.767552 | 53193606 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,496,882 | 2,379.697540 | 53193606 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,286,129 | 0.998869 | 53193606 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,806,759 | 36,370.084904 | 53193606 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,984,540 | 0.029132 | 53193606 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,511,553 | 99.264166 | 53193606 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 2,466,236 | 0.000012 | 53193606 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,165,598 | 1,217,256.969031 | 53193606 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,929,638 | 2,372.906987 | 53193606 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,855,933 | 0.019298 | 53193606 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,838,601 | 0.000000 | 53193606 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,807,574 | 399.453461 | 53193606 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 390 | 1,705,101 | 0.000012 | 53193606 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,697,850 | 0.000012 | 53193606 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,697,593 | 0.000012 | 53193606 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,520,298 | 0.005761 | 53193606 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,478,299 | 3,341.662638 | 53193606 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,274 | 1.655260 | 53193606 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,231 | 0.826726 | 53193606 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,403,157 | 13,700.065396 | 53193606 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,266,470 | 0.000267 | 53193606 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,249,269 | 2,379.125468 | 53193606 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,220,029 | 3,335.124151 | 53193606 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,197,122 | 0.000267 | 53193606 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/SEND | 3000 | 1,193,954 | 68.165924 | 53193606 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,176,271 | 1,067,162.416955 | 53193606 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,174,890 | 0.000000 | 53193606 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,174,026 | 36,233,794.182936 | 53193606 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,130,418 | 500,875.017220 | 53193606 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,087,632 | 72,727.688663 | 53193606 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,060,744 | 21,194,429.691772 | 53193606 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,058,814 | 55.838292 | 53193606 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,056,270 | 16.297877 | 53193606 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 991,641 | 98.564500 | 53193606 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 985,626 | 0.041860 | 53193606 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 943,813 | 2,356.415187 | 53193606 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 936,775 | 1,066.710464 | 53193606 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 916,428 | 0.000559 | 53193606 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 891,920 | 2.329952 | 53193606 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 882,672 | 17.858921 | 53193606 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 858,174 | 17.446284 | 53193606 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 853,918 | 2,372.390934 | 53193606 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 808,756 | 0.058742 | 53193606 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 803,413 | 0.803180 | 53193606 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 766,598 | 0.000009 | 53193606 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 757,315 | 0.632727 | 53193606 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 756,475 | 4,645,440.884917 | 53193606 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 718,487 | 137,337.234798 | 53193606 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 704,968 | 499,128.306935 | 53193606 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,194 | 0.108760 | 53193606 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 671,948 | 0.569016 | 53193606 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 9292 ; routes examinées : 176194904 ; candidats optimisés : 567452 ; net attendu > 0 : 356 ; dernier cycle 527.5 ms
- Rejets (moteur) : {'spread_below_threshold': 173476240, 'liquidity_below_min': 1863000, 'negative_expected_net': 567096, 'borrow_bound_too_small': 157775, 'pool_quarantined': 129032, 'cycle_budget_exhausted': 1224}
- Enregistrements de la session : 567452 ; net attendu > 0 : 356 ; simulés (eth_call de la vraie tx) : 36 (ok 13, échec 23) ; étiquettes ghost N+1 : 4/32 positives
- Décisions : {'REJECTED': 567452} ; motifs de rejet : {'below_safety_margin': 121, 'negative_expected_net': 567096, 'p_lower_below_threshold': 269, 'price_impact': 41, 'reliability_not_demonstrated': 87, 'simulation_failed': 23}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53188413 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 139.105675 USDC | 6.970905 USDC | 0.000000 USDC | 0.004965 USDC | 6.965940 USDC (6.4087 €) | — | 500.77 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53190872 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→WETH | 0.030970 WETH | 0.001205 WETH | 0.000000 WETH | 0.000002 WETH | 0.001203 WETH (2.6071 €) | — | 388.47 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53190872 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.035468 WETH | 0.000712 WETH | 0.000000 WETH | 0.000003 WETH | 0.000709 WETH (1.5369 €) | — | 199.97 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 83.365828 USDC | 1.674102 USDC | 0.000000 USDC | 0.007083 USDC | 1.667019 USDC (1.5337 €) | — | 199.96 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53190872 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.034928 WETH | 0.000707 WETH | 0.000000 WETH | 0.000003 WETH | 0.000704 WETH (1.5248 €) | — | 201.46 | 0.000 (n=36) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 82.080099 USDC | 1.660987 USDC | 0.000000 USDC | 0.007441 USDC | 1.653546 USDC (1.5213 €) | — | 201.46 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.034548 WETH | 0.000694 WETH | 0.000000 WETH | 0.000003 WETH | 0.000691 WETH (1.4974 €) | — | 200.01 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 81.200053 USDC | 1.631135 USDC | 0.000000 USDC | 0.007083 USDC | 1.624052 USDC (1.4941 €) | — | 200.01 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.028014 WETH | 0.000560 WETH | 0.000000 WETH | 0.000003 WETH | 0.000557 WETH (1.2070 €) | — | 198.82 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 65.812975 USDC | 1.315568 USDC | 0.000000 USDC | 0.007083 USDC | 1.308485 USDC (1.2038 €) | — | 198.82 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.027940 WETH | 0.000558 WETH | 0.000000 WETH | 0.000003 WETH | 0.000555 WETH (1.2035 €) | — | 198.77 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 65.636014 USDC | 1.311744 USDC | 0.000000 USDC | 0.007083 USDC | 1.304661 USDC (1.2003 €) | — | 198.77 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53193326 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 7,184.757275 USDC | 1.228025 USDC | 0.000000 USDC | 0.005494 USDC | 1.222531 USDC (1.1247 €) | — | 1.70 | 0.013 (n=23) | REJECTED | below_safety_margin(1222531<1436951), reliability_not_demonstrated |
| 53193326 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 3.032690 WETH | 0.000518 WETH | 0.000000 WETH | 0.000002 WETH | 0.000516 WETH (1.1213 €) | — | 1.70 | 0.013 (n=23) | REJECTED | below_safety_margin(515773344303832<606538084833004), reliability_not_demonstrated |
| 53190872 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.025335 WETH | 0.000501 WETH | 0.000000 WETH | 0.000003 WETH | 0.000498 WETH (1.0798 €) | — | 196.68 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 59.386962 USDC | 1.175437 USDC | 0.000000 USDC | 0.007441 USDC | 1.167996 USDC (1.0746 €) | — | 196.68 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53193281 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.254233 WETH | 0.000492 WETH | 0.000000 WETH | 0.000002 WETH | 0.000489 WETH (1.0615 €) | 0.000489 WETH | 19.24 | 0.000 (n=57) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.022567 WETH | 0.000453 WETH | 0.000000 WETH | 0.000003 WETH | 0.000450 WETH (0.9750 €) | — | 199.38 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53190872 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 52.612578 USDC | 1.056021 USDC | 0.000000 USDC | 0.007083 USDC | 1.048938 USDC (0.9650 €) | — | 199.37 | 0.000 (n=36) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53193281 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.239613 WETH | 0.000392 WETH | 0.000000 WETH | 0.000003 WETH | 0.000389 WETH (0.8437 €) | 0.000389 WETH | 16.23 | 0.000 (n=63) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53193281 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.006949 cbBTC | 0.000011 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000011 cbBTC (0.8435 €) | — | 16.31 | 0.000 (n=63) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53193281 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.006272 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6894 €) | — | 14.76 | 0.000 (n=63) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53193281 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.214906 WETH | 0.000321 WETH | 0.000000 WETH | 0.000003 WETH | 0.000318 WETH (0.6890 €) | 0.000318 WETH | 14.78 | 0.000 (n=63) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53193281 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.005216 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6648 €) | — | 17.12 | 0.000 (n=63) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53193281 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.179655 WETH | 0.000309 WETH | 0.000000 WETH | 0.000003 WETH | 0.000306 WETH (0.6642 €) | — | 17.04 | 0.000 (n=63) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2924 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
