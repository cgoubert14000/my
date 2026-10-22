# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T16:35:42+00:00 ; durée 124.02 min ; blocs 52945073 → 52948793 (3506 vus)

## Connexion
- Requêtes RPC : 43324 ; erreurs : 8 ; latence p50/p95 : 359.6/1,484.4 ms
- Rafraîchissements d'état : 3507 ; âge des données au dernier bloc : 2.09 s ; changements de frais LP observés (pools à frais dynamiques) : 9410
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 78993 ; cycles déclenchés par événement : 2907 ; avance médiane sur le rafraîchissement multicall : 777 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,392.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 318 jetons, 19398 routes
- Par DEX : uniswap_v3 137, aerodrome 226, aerodrome_slipstream 137, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3827 (énumérés 366, par paires 0), mesurés 549, sous le plancher de 10000.0 $ : 3 → gardés 546 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2404.811718, 'AERO': 0.81356, 'cbBTC': 81633.413427}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,934,558 | 2,392.567605 | 52948793 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 18,203,632 | 1.251633 | 52948793 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,246,136 | 0.029328 | 52948793 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,414,798 | 93.170586 | 52948793 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,271,945 | 0.029402 | 52948793 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,413,304 | 0.000012 | 52948793 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 9,326,574 | 0.029387 | 52948793 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,704,889 | 2,387.877885 | 52948793 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,164,436 | 0.001670 | 52948793 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 6,809,207 | 0.000012 | 52948793 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,795,557 | 2,387.436283 | 52948793 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 5,440,417 | 0.000012 | 52948793 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,390,757 | 0.029332 | 52948793 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,490,596 | 2,387.631156 | 52948793 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/USDC | 3000 | 4,307,585 | 2,389.196088 | 52948793 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,289,837 | 1.000001 | 52948793 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,958,694 | 34,634.177491 | 52948793 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,461,761 | 0.000274 | 52948793 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 433 | 2,907,228 | 2,391.770880 | 52948793 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,551,503 | 93.147739 | 52948793 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,329,091 | 2,987.026051 | 52948793 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,294,306 | 398.514664 | 52948793 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,216,866 | 0.000012 | 52948793 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,197,621 | 1,202,482.873335 | 52948793 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,045,636 | 0.000012 | 52948793 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,894,782 | 0.000000 | 52948793 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,803,846 | 0.018550 | 52948793 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,661,386 | 1.521320 | 52948793 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,622,315 | 2,988.135705 | 52948793 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,240 | 0.823520 | 52948793 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,409,022 | 13,569.759697 | 52948793 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,371,638 | 0.004999 | 52948793 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,320,268 | 2,387.925961 | 52948793 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/msETH (stable) | 500 | 1,297,512 | 2.367671 | 52948793 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,293,063 | 0.000273 | 52948793 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,278,388 | 0.000000 | 52948793 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,679 | 64.262670 | 52948793 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,023 | 35,205,930.437768 | 52948793 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,179,174 | 1,093,450.290012 | 52948793 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,178,229 | 16.282278 | 52948793 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/NOCK | 3000 | 1,145,677 | 47.811624 | 52948793 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,145,242 | 500,017.713432 | 52948793 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,099,678 | 74,471.318272 | 52948793 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,093,405 | 0.000010 | 52948793 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 1,092,283 | 1.105751 | 52948793 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,058,920 | 21,408,920.470197 | 52948793 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,041,013 | 16.946507 | 52948793 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,016,019 | 22.984821 | 52948793 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,012,558 | 0.029398 | 52948793 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | USDC/VVV | 3000 | 980,218 | 0.038999 | 52948793 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 955,762 | 1,060.583297 | 52948793 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,704 | 2,409.501940 | 52948793 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 915,296 | 0.000552 | 52948793 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 891,201 | 0.916099 | 52948793 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 885,722 | 17.699622 | 52948793 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 875,319 | 2,392.094597 | 52948793 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 810,600 | 0.803225 | 52948793 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 800,518 | 1.106136 | 52948793 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | fBOMB/USDC | 10000 | 799,932 | 0.018485 | 52948793 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 787,745 | 0.653135 | 52948793 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |

## Recherche d'opportunités
- Cycles : 6413 ; routes examinées : 124399374 ; candidats optimisés : 799427 ; net attendu > 0 : 221 ; dernier cycle 176.3 ms
- Rejets (moteur) : {'spread_below_threshold': 122599502, 'liquidity_below_min': 993088, 'negative_expected_net': 799206, 'borrow_bound_too_small': 6410, 'cycle_budget_exhausted': 947}
- Enregistrements de la session : 799427 ; net attendu > 0 : 221 ; simulés (eth_call de la vraie tx) : 17 (ok 5, échec 12) ; étiquettes ghost N+1 : 3/17 positives
- Décisions : {'REJECTED': 799427} ; motifs de rejet : {'below_safety_margin': 108, 'negative_expected_net': 799206, 'p_lower_below_threshold': 190, 'reliability_not_demonstrated': 31, 'simulation_failed': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52946299 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.017489 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2258 €) | — | 1.72 | 0.001 (n=6) | REJECTED | below_safety_margin(301<349), reliability_not_demonstrated |
| 52946299 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.595274 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000102 WETH (0.2257 €) | — | 1.72 | 0.001 (n=6) | REJECTED | below_safety_margin(102399355594060<119054820899875), reliability_not_demonstrated |
| 52946299 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,478.363420 USDC | 0.252661 USDC | 0.000000 USDC | 0.008652 USDC | 0.244009 USDC (0.2245 €) | — | 1.65 | 0.001 (n=6) | REJECTED | below_safety_margin(244009<295672), reliability_not_demonstrated |
| 52946299 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.316550 WETH | 0.000099 WETH | 0.000000 WETH | 0.000003 WETH | 0.000096 WETH (0.2116 €) | — | 3.03 | 0.094 (n=190) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 52946299 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009285 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2116 €) | — | 3.04 | 0.094 (n=190) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52946299 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 764.368596 USDC | 0.237843 USDC | 0.000000 USDC | 0.008282 USDC | 0.229561 USDC (0.2112 €) | — | 3.00 | 0.094 (n=190) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52948349 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 491.552280 USDC | 0.231479 USDC | 0.000000 USDC | 0.007367 USDC | 0.224112 USDC (0.2062 €) | — | 4.56 | 0.120 (n=98) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.005630 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2055 €) | — | 4.87 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 490.246119 USDC | 0.229508 USDC | 0.000000 USDC | 0.007367 USDC | 0.222141 USDC (0.2044 €) | — | 4.53 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.005630 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2040 €) | — | 4.83 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.005247 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1883 €) | — | 4.78 | 0.093 (n=191) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52948349 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 452.628167 USDC | 0.212258 USDC | 0.000000 USDC | 0.007731 USDC | 0.204527 USDC (0.1882 €) | — | 4.52 | 0.093 (n=191) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52948349 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 413.910120 USDC | 0.184965 USDC | 0.000000 USDC | 0.007367 USDC | 0.177598 USDC (0.1634 €) | — | 4.29 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.004931 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1628 €) | — | 4.40 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52946299 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.269461 WETH | 0.000074 WETH | 0.000000 WETH | 0.000003 WETH | 0.000071 WETH (0.1573 €) | — | 2.65 | 0.022 (n=64) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52946299 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 644.411865 USDC | 0.176635 USDC | 0.000000 USDC | 0.006021 USDC | 0.170614 USDC (0.1570 €) | — | 2.65 | 0.022 (n=64) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52948349 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 241.331339 USDC | 0.139162 USDC | 0.000000 USDC | 0.007367 USDC | 0.131795 USDC (0.1213 €) | — | 5.46 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 242.243688 USDC | 0.138949 USDC | 0.000000 USDC | 0.007367 USDC | 0.131582 USDC (0.1211 €) | — | 5.43 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002809 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1208 €) | — | 5.73 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002809 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1208 €) | — | 5.73 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52945116 | USDC→[aerodrome]→msUSD→[aerodrome_slipstream]→USDC | 158.467777 USDC | 0.135546 USDC | 0.000000 USDC | 0.005350 USDC | 0.130196 USDC (0.1198 €) | 0.130196 USDC | 8.22 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 52946299 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.390994 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1189 €) | — | 1.38 | 0.003 (n=2) | REJECTED | below_safety_margin(53933268041385<78198898589374), reliability_not_demonstrated |
| 52946299 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 936.046966 USDC | 0.134941 USDC | 0.000000 USDC | 0.006021 USDC | 0.128920 USDC (0.1186 €) | — | 1.38 | 0.003 (n=2) | REJECTED | below_safety_margin(128920<187209), reliability_not_demonstrated |
| 52948349 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002809 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1133 €) | — | 5.38 | 0.093 (n=191) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52948349 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 229.097001 USDC | 0.130666 USDC | 0.000000 USDC | 0.007731 USDC | 0.122935 USDC (0.1131 €) | — | 5.37 | 0.093 (n=191) | REJECTED | p_lower_below_threshold(0.09<0.75) |

## Fiabilité et décision
- Observations ghost : 1902 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.086 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
