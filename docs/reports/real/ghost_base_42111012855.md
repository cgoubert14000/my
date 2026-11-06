# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T00:18:31+00:00 ; durée 174.54 min ; blocs 53617273 → 53669596 (1937 vus)

## Connexion
- Requêtes RPC : 69506 ; erreurs : 220 ; latence p50/p95 : 714.1/2,130.0 ms
- Rafraîchissements d'état : 1937 ; âge des données au dernier bloc : 15.9 s ; changements de frais LP observés (pools à frais dynamiques) : 6068
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3578 ; cycles déclenchés par événement : 893 ; avance médiane sur le rafraîchissement multicall : 779 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,236.26 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 482 pools, 280 jetons, 18100 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 101, aerodrome 201, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3707 (énumérés 302, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 5 → gardés 482 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2231.121633, 'cbBTC': 75799.40241, 'AERO': 0.604242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,174,940 | 2,236.259478 | 53669643 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,547,949 | 0.029405 | 53669643 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,227,447 | 0.000013 | 53669643 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,112,557 | 0.029375 | 53669643 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,961,418 | 2,239.156281 | 53669643 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,399,864 | 106.789810 | 53669643 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,421,983 | 0.001544 | 53669643 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,079,643 | 1.670315 | 53669643 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,673,491 | 0.029413 | 53669643 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,113,507 | 2,238.507182 | 53669643 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,006,894 | 0.998652 | 53669643 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,324,529 | 42,344.718848 | 53669643 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 609 | 3,212,839 | 2,238.607196 | 53669643 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,563,473 | 0.029384 | 53669643 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,081,240 | 1,170,297.440977 | 53669643 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 2,016,524 | 0.008459 | 53669643 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,752,314 | 0.000013 | 53669643 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,641,767 | 0.000000 | 53669643 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,636,803 | 0.016433 | 53669643 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,629,308 | 0.000013 | 53669643 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,529,107 | 1.457700 | 53669643 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,516,435 | 0.000013 | 53669643 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,513,851 | 448.491625 | 53669643 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,387 | 0.816940 | 53669643 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,373,594 | 3,734.060454 | 53669643 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,325,124 | 2,235.984238 | 53669643 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,323,742 | 2,237.440698 | 53669643 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,257,736 | 15,248.296953 | 53669643 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,164,382 | 2,239.224789 | 53669643 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,791 | 76.942850 | 53669643 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,095,796 | 37,238,257.815967 | 53669643 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,050,595 | 106.298109 | 53669643 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,019,654 | 575,392.857296 | 53669643 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,005,931 | 0.000000 | 53669643 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 995,310 | 22,588,921.913143 | 53669643 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 958,801 | 21.467888 | 53669643 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 949,215 | 69.591480 | 53669643 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 935,066 | 2,225.465428 | 53669643 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 931,953 | 1,072.671567 | 53669643 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 926,529 | 0.000013 | 53669643 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 880,361 | 98,438.308690 | 53669643 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 846,211 | 0.047661 | 53669643 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 845,274 | 0.000539 | 53669643 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 794,147 | 3,730.662252 | 53669643 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 793,784 | 0.056415 | 53669643 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4560 | 785,380 | 21.441031 | 53669643 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 758,782 | 0.799698 | 53669643 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 712,529 | 0.562387 | 53669643 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 689,418 | 4,978,219.770198 | 53669643 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 681,954 | 0.000252 | 53669643 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 665,777 | 142,590.699381 | 53669643 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 650,620 | 0.000008 | 53669643 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 649,636 | 0.530666 | 53669643 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2144 | 618,804 | 573,113.221476 | 53669643 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 599,371 | 0.914700 | 53669643 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 597,259 | 2.475446 | 53669643 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 555,047 | 0.085702 | 53669643 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 550,366 | 807,583.317562 | 53669643 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | FLOCK/USDC | 3000 | 544,695 | 0.036428 | 53669643 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2730 | 521,331 | 1,072.412605 | 53669643 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 2829 ; routes examinées : 51204900 ; candidats optimisés : 176171 ; net attendu > 0 : 161 ; dernier cycle 295.1 ms
- Rejets (moteur) : {'spread_below_threshold': 50185249, 'liquidity_below_min': 836022, 'negative_expected_net': 176010, 'cycle_budget_exhausted': 4690, 'borrow_bound_too_small': 2768}
- Enregistrements de la session : 176171 ; net attendu > 0 : 161 ; simulés (eth_call de la vraie tx) : 14 (ok 13, échec 1) ; étiquettes ghost N+1 : 1/14 positives
- Décisions : {'REJECTED': 176171} ; motifs de rejet : {'below_safety_margin': 130, 'negative_expected_net': 176010, 'p_lower_below_threshold': 145, 'reliability_not_demonstrated': 16, 'simulation_failed': 1, 'stale_data': 143}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53617917 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.338587 WETH | 0.000069 WETH | 0.000000 WETH | 0.000003 WETH | 0.000066 WETH (0.1350 €) | — | 1.95 | 0.046 (n=233) | REJECTED | below_safety_margin(66042364924503<67717351541604), stale_data(6295ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53617917 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 748.880467 USDC | 0.152184 USDC | 0.000000 USDC | 0.005683 USDC | 0.146501 USDC (0.1348 €) | — | 1.96 | 0.046 (n=233) | REJECTED | below_safety_margin(146501<149776), stale_data(6303ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53617917 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.152255 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0908 €) | 0.000044 WETH | 2.92 | 0.057 (n=76) | REJECTED | stale_data(6191ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 336.649658 USDC | 0.104612 USDC | 0.000000 USDC | 0.006041 USDC | 0.098571 USDC (0.0907 €) | 0.098571 USDC | 2.93 | 0.057 (n=76) | REJECTED | stale_data(6198ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 53649132 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 345.694814 USDC | 0.098995 USDC | 0.000000 USDC | 0.005847 USDC | 0.093148 USDC (0.0857 €) | 0.093148 USDC | 2.69 | 0.056 (n=78) | REJECTED | stale_data(5536ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 53649132 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.156617 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0856 €) | 0.000042 WETH | 2.69 | 0.056 (n=78) | REJECTED | stale_data(5529ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 53649132 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 559.146380 USDC | 0.086896 USDC | 0.000000 USDC | 0.005499 USDC | 0.081397 USDC (0.0749 €) | — | 1.46 | 0.046 (n=233) | REJECTED | below_safety_margin(81397<111829), stale_data(5610ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53649132 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.253280 WETH | 0.000039 WETH | 0.000000 WETH | 0.000002 WETH | 0.000037 WETH (0.0748 €) | — | 1.45 | 0.046 (n=233) | REJECTED | below_safety_margin(36761086370394<50656040952722), stale_data(5603ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53649132 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 451.754794 USDC | 0.073504 USDC | 0.000000 USDC | 0.006894 USDC | 0.066610 USDC (0.0613 €) | — | 1.47 | 0.168 (n=1020) | REJECTED | below_safety_margin(66610<90350), stale_data(5582ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53649132 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.210558 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0612 €) | — | 1.43 | 0.168 (n=1020) | REJECTED | below_safety_margin(30045423179333<42111650811301), stale_data(5596ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53649132 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005940 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0610 €) | — | 1.48 | 0.168 (n=1020) | REJECTED | below_safety_margin(88<118), stale_data(5589ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53655384 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001056 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0306 €) | — | 4.17 | 0.149 (n=773) | REJECTED | stale_data(5341ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53655384 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 82.797701 USDC | 0.039879 USDC | 0.000000 USDC | 0.006722 USDC | 0.033157 USDC (0.0305 €) | 0.033157 USDC | 4.00 | 0.149 (n=773) | REJECTED | stale_data(5334ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53655384 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000989 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0237 €) | — | 3.44 | 0.276 (n=352) | REJECTED | stale_data(5367ms>4000.0), p_lower_below_threshold(0.28<0.75) |
| 53655384 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 76.859199 USDC | 0.031886 USDC | 0.000000 USDC | 0.006722 USDC | 0.025164 USDC (0.0232 €) | 0.025164 USDC | 3.27 | 0.276 (n=352) | REJECTED | stale_data(5360ms>4000.0), p_lower_below_threshold(0.28<0.75) |
| 53618187 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 333.527485 USDC | 0.029762 USDC | 0.000000 USDC | 0.005283 USDC | 0.024479 USDC (0.0225 €) | — | 0.73 | 0.046 (n=233) | REJECTED | below_safety_margin(24479<66705), p_lower_below_threshold(0.05<0.75) |
| 53618187 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.149601 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0225 €) | — | 0.74 | 0.046 (n=233) | REJECTED | below_safety_margin(11000756189724<29920206520439), p_lower_below_threshold(0.05<0.75) |
| 53655384 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000894 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0216 €) | — | 3.47 | 0.276 (n=352) | REJECTED | stale_data(5373ms>4000.0), p_lower_below_threshold(0.28<0.75) |
| 53655384 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 70.203000 USDC | 0.029794 USDC | 0.000000 USDC | 0.006722 USDC | 0.023072 USDC (0.0212 €) | 0.023072 USDC | 3.29 | 0.276 (n=352) | REJECTED | stale_data(5379ms>4000.0), p_lower_below_threshold(0.28<0.75) |
| 53655384 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000977 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0195 €) | — | 2.87 | 0.168 (n=1020) | REJECTED | stale_data(5353ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53655384 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 63.547196 USDC | 0.027780 USDC | 0.000000 USDC | 0.006722 USDC | 0.021058 USDC (0.0194 €) | — | 3.31 | 0.149 (n=773) | REJECTED | stale_data(5347ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53626056 | WETH→[uniswap_v3]→MEY→[aerodrome]→WETH | 0.010874 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0170 €) | — | 7.60 | 0.234 (n=59) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.23<0.75) |
| 53617917 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.064521 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | — | 0.99 | 0.168 (n=1020) | REJECTED | below_safety_margin(6373757605358<12904292848390), stale_data(6350ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 142.645611 USDC | 0.021504 USDC | 0.000000 USDC | 0.007481 USDC | 0.014023 USDC (0.0129 €) | — | 0.98 | 0.168 (n=1020) | REJECTED | below_safety_margin(14023<28529), stale_data(6368ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001637 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0126 €) | — | 1.10 | 0.168 (n=1020) | REJECTED | below_safety_margin(18<32), stale_data(6359ms>4000.0), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 5785 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
