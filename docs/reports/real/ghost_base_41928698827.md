# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T02:19:07+00:00 ; durée 202.93 min ; blocs 53521807 → 53527896 (6029 vus)

## Connexion
- Requêtes RPC : 65623 ; erreurs : 0 ; latence p50/p95 : 286.4/1,516.7 ms
- Rafraîchissements d'état : 6029 ; âge des données au dernier bloc : 5.75 s ; changements de frais LP observés (pools à frais dynamiques) : 9481
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 481 ; cycles déclenchés par événement : 54 ; avance médiane sur le rafraîchissement multicall : 480 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,426.63 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 503 pools, 289 jetons, 19656 routes
- Par DEX : uniswap_v3 145, aerodrome_slipstream 108, aerodrome 206, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3710 (énumérés 312, par paires 0), mesurés 506, sous le plancher de 10000.0 $ : 3 → gardés 503 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2435.517454, 'cbBTC': 80725.683876, 'AERO': 0.642935}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,796,877 | 2,426.629242 | 53527897 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,358,876 | 0.030117 | 53527897 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,681,704 | 0.030091 | 53527897 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,282,622 | 0.000012 | 53527897 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,380,884 | 2,428.819099 | 53527897 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,796,177 | 113.288390 | 53527897 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,838,938 | 0.001560 | 53527897 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,346,693 | 1.547582 | 53527897 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,023,437 | 0.030107 | 53527897 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,339,660 | 2,427.946701 | 53527897 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,241,092 | 0.999062 | 53527897 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,711,138 | 40,013.625941 | 53527897 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,483,523 | 2,428.121465 | 53527897 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,756,269 | 0.030079 | 53527897 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,264,396 | 1,164,309.449368 | 53527897 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,844,250 | 0.006896 | 53527897 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,827,022 | 0.000012 | 53527897 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,778,185 | 0.000000 | 53527897 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,760,804 | 0.018065 | 53527897 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,690,604 | 0.000012 | 53527897 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,645,632 | 445.465250 | 53527897 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,554,693 | 0.000012 | 53527897 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,524,440 | 1.472010 | 53527897 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,482,842 | 3,763.815781 | 53527897 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,875 | 0.816604 | 53527897 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,413,663 | 2,428.988389 | 53527897 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,380,792 | 2,428.558116 | 53527897 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,380,174 | 2,433.467922 | 53527897 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,350,044 | 14,813.055732 | 53527897 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,188,748 | 37,357,857.488394 | 53527897 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,296 | 73.310294 | 53527897 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,142,659 | 0.000000 | 53527897 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,110,679 | 560,345.864985 | 53527897 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,070,402 | 114.046473 | 53527897 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,068,565 | 23,018,393.135731 | 53527897 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 995,864 | 1,078.657534 | 53527897 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/VELVET | 100 | 988,721 | 19.582994 | 53527897 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 982,835 | 64.910841 | 53527897 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 965,597 | 0.000012 | 53527897 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 957,356 | 2,419.823218 | 53527897 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 956,970 | 98,085.027862 | 53527897 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 915,776 | 0.000534 | 53527897 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 865,039 | 0.046573 | 53527897 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 859,461 | 3,767.676117 | 53527897 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 831,010 | 19.729407 | 53527897 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 823,660 | 0.799146 | 53527897 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 807,192 | 0.058465 | 53527897 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 749,104 | 0.599994 | 53527897 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 742,165 | 5,057,628.334499 | 53527897 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 739,763 | 135,942.541848 | 53527897 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 732,622 | 0.000246 | 53527897 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 695,451 | 0.000008 | 53527897 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 680,546 | 560,450.081314 | 53527897 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 675,262 | 0.576412 | 53527897 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 651,184 | 0.914485 | 53527897 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 642,410 | 2.507744 | 53527897 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 610,502 | 0.092373 | 53527897 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | cbBTC/EDGE | 7000 | 609,362 | 718,134.253842 | 53527897 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 580,212 | 0.093593 | 53527897 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 580,117 | 6,416.691546 | 53527897 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 6082 ; routes examinées : 119547792 ; candidats optimisés : 341489 ; net attendu > 0 : 121 ; dernier cycle 264.4 ms
- Rejets (moteur) : {'spread_below_threshold': 117713165, 'liquidity_below_min': 1492227, 'negative_expected_net': 341368, 'cycle_budget_exhausted': 911}
- Enregistrements de la session : 341489 ; net attendu > 0 : 121 ; simulés (eth_call de la vraie tx) : 29 (ok 28, échec 1) ; étiquettes ghost N+1 : 0/29 positives
- Décisions : {'REJECTED': 341489} ; motifs de rejet : {'below_safety_margin': 43, 'negative_expected_net': 341368, 'p_lower_below_threshold': 112, 'reliability_not_demonstrated': 9, 'simulation_failed': 1, 'stale_data': 37}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53521849 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.093750 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000103 WETH (0.2310 €) | 0.000103 WETH | 11.00 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 228.057798 USDC | 0.258391 USDC | 0.000000 USDC | 0.007320 USDC | 0.251071 USDC (0.2310 €) | — | 11.01 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.095513 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000103 WETH (0.2303 €) | 0.000103 WETH | 10.76 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 232.330795 USDC | 0.257687 USDC | 0.000000 USDC | 0.007320 USDC | 0.250367 USDC (0.2303 €) | — | 10.78 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.095575 WETH | 0.000105 WETH | 0.000000 WETH | 0.000003 WETH | 0.000102 WETH (0.2292 €) | 0.000102 WETH | 10.70 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 232.397471 USDC | 0.256437 USDC | 0.000000 USDC | 0.007320 USDC | 0.249117 USDC (0.2292 €) | — | 10.72 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.095305 WETH | 0.000105 WETH | 0.000000 WETH | 0.000003 WETH | 0.000102 WETH (0.2275 €) | — | 10.66 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 232.330795 USDC | 0.254631 USDC | 0.000000 USDC | 0.007320 USDC | 0.247311 USDC (0.2275 €) | — | 10.64 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.091928 WETH | 0.000098 WETH | 0.000000 WETH | 0.000003 WETH | 0.000095 WETH (0.2135 €) | — | 10.37 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 224.164697 USDC | 0.239385 USDC | 0.000000 USDC | 0.007320 USDC | 0.232065 USDC (0.2135 €) | — | 10.35 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.069904 WETH | 0.000081 WETH | 0.000000 WETH | 0.000003 WETH | 0.000077 WETH (0.1736 €) | — | 11.09 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 170.112430 USDC | 0.196308 USDC | 0.000000 USDC | 0.007689 USDC | 0.188619 USDC (0.1735 €) | — | 11.09 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.021917 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0598 €) | — | 12.17 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 52.842361 USDC | 0.072162 USDC | 0.000000 USDC | 0.007320 USDC | 0.064842 USDC (0.0597 €) | — | 12.27 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53524429 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 40.816538 USDC | 0.071648 USDC | 0.000000 USDC | 0.006954 USDC | 0.064694 USDC (0.0595 €) | — | 15.85 | 0.118 (n=44) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53524429 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.016849 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0595 €) | 0.000027 WETH | 15.81 | 0.118 (n=44) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53526787 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 102.828197 USDC | 0.071226 USDC | 0.000000 USDC | 0.007265 USDC | 0.063961 USDC (0.0588 €) | — | 6.22 | 0.155 (n=654) | REJECTED | stale_data(6678ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53526787 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.042480 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0587 €) | 0.000026 WETH | 6.21 | 0.155 (n=654) | REJECTED | stale_data(6673ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53524429 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 40.680304 USDC | 0.070634 USDC | 0.000000 USDC | 0.006954 USDC | 0.063680 USDC (0.0586 €) | — | 15.65 | 0.039 (n=37) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53524429 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.016786 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0585 €) | 0.000026 WETH | 15.62 | 0.039 (n=37) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53526787 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 100.436448 USDC | 0.069160 USDC | 0.000000 USDC | 0.007265 USDC | 0.061895 USDC (0.0569 €) | — | 6.16 | 0.155 (n=654) | REJECTED | stale_data(6683ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53526787 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.041527 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0568 €) | 0.000026 WETH | 6.15 | 0.155 (n=654) | REJECTED | stale_data(6688ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53524578 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 77.925601 USDC | 0.068464 USDC | 0.000000 USDC | 0.007322 USDC | 0.061142 USDC (0.0563 €) | 0.061142 USDC | 7.85 | 0.288 (n=152) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53527777 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 514.101477 USDC | 0.066044 USDC | 0.000000 USDC | 0.005448 USDC | 0.060596 USDC (0.0557 €) | — | 1.18 | 0.043 (n=214) | REJECTED | below_safety_margin(60596<102820), stale_data(4764ms>4000.0), p_lower_below_threshold(0.04<0.75) |
| 53524578 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000936 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0556 €) | — | 8.01 | 0.113 (n=46) | REJECTED | p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 5297 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
