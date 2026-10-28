# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T10:10:41+00:00 ; durée 279.97 min ; blocs 53188044 → 53196441 (7904 vus)

## Connexion
- Requêtes RPC : 93180 ; erreurs : 160 ; latence p50/p95 : 241.8/1,912.3 ms
- Rafraîchissements d'état : 7904 ; âge des données au dernier bloc : 5.88 s ; changements de frais LP observés (pools à frais dynamiques) : 8245
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 27140 ; cycles déclenchés par événement : 4692 ; avance médiane sur le rafraîchissement multicall : 1,115 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,370.75 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 521 pools, 302 jetons, 18962 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 121, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 184 (rejetés 2) → 589 jetons ; pools candidats 3762 (énumérés 330, par paires 0), mesurés 523, sous le plancher de 10000.0 $ : 2 → gardés 521 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2356.459313, 'cbBTC': 80857.377983, 'AERO': 0.694089}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,543,296 | 2,370.753750 | 53196442 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,803,721 | 0.029089 | 53196442 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,734,803 | 0.000012 | 53196442 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,556,991 | 0.029117 | 53196442 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,511,728 | 2,367.266315 | 53196442 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,351,678 | 97.833653 | 53196442 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 7,235,655 | 1.427301 | 53196442 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,120,518 | 0.001652 | 53196442 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,783,877 | 0.029080 | 53196442 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 639 | 5,056,619 | 2,367.659602 | 53196442 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,481,255 | 2,367.375622 | 53196442 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,291,298 | 0.998874 | 53196442 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,804,701 | 36,342.785963 | 53196442 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,982,839 | 0.029131 | 53196442 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2772 | 2,528,293 | 97.828557 | 53196442 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,471,515 | 0.000012 | 53196442 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,163,435 | 1,217,459.143201 | 53196442 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,928,754 | 2,372.483040 | 53196442 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,840,692 | 0.019015 | 53196442 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,815,900 | 0.000000 | 53196442 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,805,978 | 399.417739 | 53196442 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,729,414 | 0.000012 | 53196442 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,706,251 | 0.000012 | 53196442 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,698,578 | 0.000012 | 53196442 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,526,220 | 0.005795 | 53196442 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,274 | 1.655260 | 53196442 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,467,609 | 3,368.295631 | 53196442 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,119 | 0.826842 | 53196442 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,403,792 | 13,730.900574 | 53196442 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,264,497 | 0.000267 | 53196442 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,241,330 | 2,367.219331 | 53196442 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,211,137 | 3,344.684805 | 53196442 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,195,130 | 0.000267 | 53196442 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/SEND | 3000 | 1,193,954 | 68.165887 | 53196442 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,175,053 | 1,067,390.860061 | 53196442 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,172,947 | 36,233,858.667987 | 53196442 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,170,887 | 0.000000 | 53196442 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,132,729 | 504,704.941580 | 53196442 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,086,504 | 72,745.435799 | 53196442 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,077,884 | 21,201,334.751304 | 53196442 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,051,698 | 56.596540 | 53196442 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,050,618 | 16.532839 | 53196442 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 1,000,179 | 98.522304 | 53196442 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 994,791 | 0.041316 | 53196442 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 943,430 | 2,360.576085 | 53196442 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 938,477 | 1,063.525719 | 53196442 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 915,366 | 0.000559 | 53196442 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 889,703 | 2.334541 | 53196442 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 885,244 | 17.774383 | 53196442 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 856,513 | 17.478933 | 53196442 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 853,555 | 2,370.671511 | 53196442 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 805,863 | 0.058297 | 53196442 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 802,677 | 0.803180 | 53196442 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 761,369 | 0.000009 | 53196442 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 756,141 | 0.632401 | 53196442 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 755,902 | 4,643,971.050801 | 53196442 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 721,975 | 135,768.312517 | 53196442 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 701,559 | 501,181.687622 | 53196442 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 676,972 | 0.577079 | 53196442 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 673,596 | 0.108601 | 53196442 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 12595 ; routes examinées : 238826390 ; candidats optimisés : 757636 ; net attendu > 0 : 608 ; dernier cycle 314.4 ms
- Rejets (moteur) : {'spread_below_threshold': 235149151, 'liquidity_below_min': 2553959, 'negative_expected_net': 757028, 'borrow_bound_too_small': 233514, 'pool_quarantined': 129710, 'cycle_budget_exhausted': 2420}
- Enregistrements de la session : 757636 ; net attendu > 0 : 608 ; simulés (eth_call de la vraie tx) : 44 (ok 20, échec 24) ; étiquettes ghost N+1 : 10/40 positives
- Décisions : {'REJECTED': 757636} ; motifs de rejet : {'below_safety_margin': 334, 'negative_expected_net': 757028, 'p_lower_below_threshold': 515, 'price_impact': 41, 'reliability_not_demonstrated': 93, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 2, 'simulation_failed': 24, 'stale_data': 22}

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
- Observations ghost : 2932 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
