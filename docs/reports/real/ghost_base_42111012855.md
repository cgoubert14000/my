# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T23:29:17+00:00 ; durée 125.32 min ; blocs 53617273 → 53654854 (1569 vus)

## Connexion
- Requêtes RPC : 51056 ; erreurs : 220 ; latence p50/p95 : 680.2/1,981.6 ms
- Rafraîchissements d'état : 1569 ; âge des données au dernier bloc : 10.58 s ; changements de frais LP observés (pools à frais dynamiques) : 4556
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3578 ; cycles déclenchés par événement : 893 ; avance médiane sur le rafraîchissement multicall : 779 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,226.61 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 482 pools, 280 jetons, 18100 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 101, aerodrome 201, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3707 (énumérés 302, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 5 → gardés 482 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2231.121633, 'cbBTC': 75799.40241, 'AERO': 0.604242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,661,463 | 2,226.612119 | 53654887 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,482,069 | 0.029412 | 53654887 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,199,216 | 0.000013 | 53654887 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,073,072 | 0.029375 | 53654887 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,934,508 | 2,231.008133 | 53654887 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,384,973 | 106.298034 | 53654887 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,385,153 | 0.001540 | 53654887 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,066,010 | 1.679317 | 53654887 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,652,929 | 0.029420 | 53654887 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,081,904 | 2,230.700460 | 53654887 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,988,567 | 0.998654 | 53654887 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,289,833 | 42,870.310619 | 53654887 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,201,424 | 2,230.795670 | 53654887 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,552,321 | 0.029384 | 53654887 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,072,261 | 1,170,297.440977 | 53654887 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,952,665 | 0.008218 | 53654887 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 1,746,551 | 0.000013 | 53654887 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,634,507 | 0.000000 | 53654887 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,629,319 | 0.016326 | 53654887 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,622,458 | 0.000013 | 53654887 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,529,107 | 1.457700 | 53654887 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,512,043 | 0.000013 | 53654887 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,506,137 | 449.613091 | 53654887 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,340 | 0.816940 | 53654887 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,366,758 | 3,750.137834 | 53654887 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,322,262 | 2,234.263804 | 53654887 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,320,884 | 2,226.464236 | 53654887 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,250,740 | 15,287.009886 | 53654887 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,160,455 | 2,231.084738 | 53654887 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,791 | 76.942850 | 53654887 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,091,782 | 37,163,661.328170 | 53654887 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,049,558 | 106.065167 | 53654887 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,015,258 | 575,388.912613 | 53654887 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,003,237 | 0.000000 | 53654887 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 991,538 | 22,568,618.897092 | 53654887 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 954,881 | 21.741174 | 53654887 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 949,119 | 69.605667 | 53654887 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 933,346 | 2,225.465428 | 53654887 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 925,775 | 1,073.995064 | 53654887 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 922,901 | 0.000013 | 53654887 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 876,538 | 98,423.905905 | 53654887 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 846,288 | 0.047650 | 53654887 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 841,697 | 0.000539 | 53654887 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 790,306 | 3,730.662252 | 53654887 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 788,138 | 0.055576 | 53654887 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4565 | 780,737 | 21.619881 | 53654887 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 755,508 | 0.799698 | 53654887 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 710,989 | 0.557520 | 53654887 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 686,466 | 4,977,901.639601 | 53654887 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 679,151 | 0.000252 | 53654887 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 664,924 | 141,724.609328 | 53654887 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 649,616 | 0.530635 | 53654887 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 647,302 | 0.000008 | 53654887 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2210 | 616,130 | 574,887.371773 | 53654887 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 596,785 | 0.914700 | 53654887 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 594,786 | 2.474811 | 53654887 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 544,588 | 0.083316 | 53654887 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | FLOCK/USDC | 3000 | 541,150 | 0.036069 | 53654887 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 537,265 | 839,362.502719 | 53654887 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 518,607 | 1,074.248380 | 53654887 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 2461 ; routes examinées : 44544100 ; candidats optimisés : 149101 ; net attendu > 0 : 78 ; dernier cycle 1123.9 ms
- Rejets (moteur) : {'spread_below_threshold': 43648618, 'liquidity_below_min': 740976, 'negative_expected_net': 149023, 'cycle_budget_exhausted': 2986, 'borrow_bound_too_small': 2419}
- Enregistrements de la session : 149101 ; net attendu > 0 : 78 ; simulés (eth_call de la vraie tx) : 8 (ok 7, échec 1) ; étiquettes ghost N+1 : 1/8 positives
- Décisions : {'REJECTED': 149101} ; motifs de rejet : {'below_safety_margin': 59, 'negative_expected_net': 149023, 'p_lower_below_threshold': 70, 'reliability_not_demonstrated': 8, 'simulation_failed': 1, 'stale_data': 60}

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
| 53618187 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 333.527485 USDC | 0.029762 USDC | 0.000000 USDC | 0.005283 USDC | 0.024479 USDC (0.0225 €) | — | 0.73 | 0.046 (n=233) | REJECTED | below_safety_margin(24479<66705), p_lower_below_threshold(0.05<0.75) |
| 53618187 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.149601 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0225 €) | — | 0.74 | 0.046 (n=233) | REJECTED | below_safety_margin(11000756189724<29920206520439), p_lower_below_threshold(0.05<0.75) |
| 53626056 | WETH→[uniswap_v3]→MEY→[aerodrome]→WETH | 0.010874 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0170 €) | — | 7.60 | 0.234 (n=59) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.23<0.75) |
| 53617917 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.064521 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | — | 0.99 | 0.168 (n=1020) | REJECTED | below_safety_margin(6373757605358<12904292848390), stale_data(6350ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 142.645611 USDC | 0.021504 USDC | 0.000000 USDC | 0.007481 USDC | 0.014023 USDC (0.0129 €) | — | 0.98 | 0.168 (n=1020) | REJECTED | below_safety_margin(14023<28529), stale_data(6368ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001637 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0126 €) | — | 1.10 | 0.168 (n=1020) | REJECTED | below_safety_margin(18<32), stale_data(6359ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53632809 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 179.344034 USDC | 0.018208 USDC | 0.000000 USDC | 0.005365 USDC | 0.012843 USDC (0.0118 €) | — | 0.72 | 0.046 (n=233) | REJECTED | below_safety_margin(12843<35868), stale_data(7275ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53632809 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.080433 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0118 €) | — | 0.71 | 0.046 (n=233) | REJECTED | below_safety_margin(5732207256396<16086674229864), stale_data(7270ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53617917 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.043508 WETH | 0.000009 WETH | 0.000000 WETH | 0.000004 WETH | 0.000005 WETH (0.0111 €) | — | 1.24 | 0.168 (n=1020) | REJECTED | below_safety_margin(5405219764860<8701692752134), stale_data(6259ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 101.697045 USDC | 0.019489 USDC | 0.000000 USDC | 0.007838 USDC | 0.011651 USDC (0.0107 €) | — | 1.15 | 0.168 (n=1020) | REJECTED | below_safety_margin(11651<20339), stale_data(6272ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53649132 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.076779 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0106 €) | — | 0.68 | 0.168 (n=1020) | REJECTED | below_safety_margin(5197637816906<15355815469641), stale_data(5624ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001342 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0105 €) | — | 1.12 | 0.168 (n=1020) | REJECTED | below_safety_margin(15<26), stale_data(6266ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53649132 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002634 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0104 €) | — | 0.57 | 0.168 (n=1020) | REJECTED | below_safety_margin(15<52), stale_data(5617ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53649132 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 204.820487 USDC | 0.018112 USDC | 0.000000 USDC | 0.006894 USDC | 0.011218 USDC (0.0103 €) | — | 0.55 | 0.168 (n=1020) | REJECTED | below_safety_margin(11218<40964), stale_data(5630ms>4000.0), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 5779 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
