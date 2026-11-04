# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T22:31:57+00:00 ; durée 312.47 min ; blocs 53511708 → 53521082 (9068 vus)

## Connexion
- Requêtes RPC : 109556 ; erreurs : 908 ; latence p50/p95 : 90.7/850.1 ms
- Rafraîchissements d'état : 9069 ; âge des données au dernier bloc : 2.2 s ; changements de frais LP observés (pools à frais dynamiques) : 14716
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 55241 ; cycles déclenchés par événement : 5455 ; avance médiane sur le rafraîchissement multicall : 256 ms
- Gaz : base fee 0.005014 gwei ; prix ETH (pool le plus profond) : 2,428.41 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 502 pools, 289 jetons, 19560 routes
- Par DEX : uniswap_v3 145, aerodrome_slipstream 107, aerodrome 206, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3710 (énumérés 311, par paires 0), mesurés 505, sous le plancher de 10000.0 $ : 3 → gardés 502 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2427.762313, 'cbBTC': 80310.699989, 'AERO': 0.65591}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,939,527 | 2,428.409729 | 53521082 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,327,896 | 0.030188 | 53521082 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,677,550 | 0.030149 | 53521082 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,255,558 | 0.000012 | 53521082 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,387,964 | 2,434.681856 | 53521082 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,898,439 | 110.641025 | 53521082 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,805,539 | 0.001550 | 53521082 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,316,009 | 1.569353 | 53521082 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,021,923 | 0.030200 | 53521082 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,338,645 | 2,435.197015 | 53521082 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,234,185 | 0.999050 | 53521082 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,716,950 | 39,947.141861 | 53521082 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,485,329 | 2,434.997692 | 53521082 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,745,292 | 0.030163 | 53521082 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,271,519 | 1,158,722.007660 | 53521082 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 2,200,094 | 0.008517 | 53521082 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,825,141 | 0.000012 | 53521082 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,781,788 | 0.000000 | 53521082 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,757,053 | 0.018053 | 53521082 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,688,038 | 0.000012 | 53521082 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,643,188 | 448.630686 | 53521082 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,087 | 0.000012 | 53521082 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,524,440 | 1.472010 | 53521082 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,470,377 | 3,816.601094 | 53521082 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,448 | 0.816604 | 53521082 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,415,138 | 2,434.560857 | 53521082 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,381,370 | 2,428.152567 | 53521082 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,380,631 | 2,427.912322 | 53521082 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,345,071 | 14,878.811051 | 53521082 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,189,730 | 37,347,281.982865 | 53521082 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,415 | 73.295109 | 53521082 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,143,434 | 0.000000 | 53521082 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,120,395 | 561,902.271198 | 53521082 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,082,824 | 110.910381 | 53521082 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,069,307 | 23,018,485.661554 | 53521082 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 1,001,166 | 1,075.388947 | 53521082 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/VELVET | 100 | 997,094 | 19.110691 | 53521082 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 979,785 | 65.213839 | 53521082 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 964,555 | 0.000012 | 53521082 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 962,731 | 97,063.635669 | 53521082 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 948,190 | 2,419.823218 | 53521082 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 918,240 | 0.000536 | 53521082 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 881,068 | 0.045429 | 53521082 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 857,897 | 3,790.454216 | 53521082 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4540 | 830,266 | 19.754699 | 53521082 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 824,265 | 0.799146 | 53521082 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 807,657 | 0.058538 | 53521082 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 753,465 | 4,913,774.965787 | 53521082 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 749,784 | 0.601635 | 53521082 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 735,602 | 137,661.490608 | 53521082 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 733,485 | 0.000246 | 53521082 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 689,066 | 0.000008 | 53521082 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 680,030 | 560,275.908912 | 53521082 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 678,253 | 0.576246 | 53521082 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 651,779 | 0.914157 | 53521082 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 649,120 | 2.472419 | 53521082 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 626,771 | 0.108440 | 53521082 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 606,648 | 0.091491 | 53521082 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 573,552 | 0.039457 | 53521082 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 562,306 | 1,075.386449 | 53521082 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 14523 ; routes examinées : 284069880 ; candidats optimisés : 808909 ; net attendu > 0 : 655 ; dernier cycle 418.1 ms
- Rejets (moteur) : {'spread_below_threshold': 279195130, 'liquidity_below_min': 4009318, 'negative_expected_net': 808254, 'unquotable': 51422, 'pool_quarantined': 3932, 'cycle_budget_exhausted': 1169}
- Enregistrements de la session : 808909 ; net attendu > 0 : 655 ; simulés (eth_call de la vraie tx) : 83 (ok 30, échec 53) ; étiquettes ghost N+1 : 0/70 positives
- Décisions : {'REJECTED': 808909} ; motifs de rejet : {'below_safety_margin': 419, 'negative_expected_net': 808254, 'p_lower_below_threshold': 577, 'price_impact': 2, 'reliability_not_demonstrated': 78, 'simulation_failed': 53, 'stale_data': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53516727 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.005236 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0184 €) | — | 26.40 | 0.046 (n=18) | REJECTED | reliability_not_demonstrated |
| 53516727 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.005236 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0184 €) | — | 26.40 | 0.046 (n=18) | REJECTED | reliability_not_demonstrated |
| 53516727 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.164899 WETH | 0.000462 WETH | 0.000000 WETH | 0.000003 WETH | 0.000458 WETH (1.0168 €) | 0.000458 WETH | 27.80 | 0.000 (n=43) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53516727 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.164899 WETH | 0.000462 WETH | 0.000000 WETH | 0.000003 WETH | 0.000458 WETH (1.0168 €) | — | 27.80 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53516727 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→cbBTC | 0.004867 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0162 €) | — | 28.33 | 0.000 (n=43) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53516727 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→cbBTC | 0.004867 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0162 €) | — | 28.33 | 0.000 (n=43) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53516727 | USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 419.719745 USDC | 1.110716 USDC | 0.000000 USDC | 0.006931 USDC | 1.103785 USDC (1.0155 €) | — | 26.30 | 0.046 (n=18) | REJECTED | reliability_not_demonstrated |
| 53516727 | USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 419.719745 USDC | 1.110716 USDC | 0.000000 USDC | 0.006931 USDC | 1.103785 USDC (1.0155 €) | — | 26.30 | 0.046 (n=18) | REJECTED | reliability_not_demonstrated |
| 53516727 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.005075 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (0.9985 €) | — | 26.70 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.005075 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (0.9985 €) | — | 26.70 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 407.883005 USDC | 1.089368 USDC | 0.000000 USDC | 0.006931 USDC | 1.082437 USDC (0.9958 €) | — | 26.54 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 407.883005 USDC | 1.089368 USDC | 0.000000 USDC | 0.006931 USDC | 1.082437 USDC (0.9958 €) | — | 26.54 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53517261 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 206.580723 USDC | 1.061041 USDC | 0.000000 USDC | 0.005423 USDC | 1.055618 USDC (0.9712 €) | — | 51.10 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53516727 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.005049 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.9624 €) | — | 25.86 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.005049 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.9624 €) | — | 25.86 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 412.174838 USDC | 1.049795 USDC | 0.000000 USDC | 0.006931 USDC | 1.042864 USDC (0.9594 €) | — | 25.30 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 412.174838 USDC | 1.049795 USDC | 0.000000 USDC | 0.006931 USDC | 1.042864 USDC (0.9594 €) | — | 25.30 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.004950 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.9300 €) | — | 25.50 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.004950 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.9300 €) | — | 25.50 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 401.422935 USDC | 1.015157 USDC | 0.000000 USDC | 0.006931 USDC | 1.008226 USDC (0.9276 €) | — | 25.12 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 401.422935 USDC | 1.015157 USDC | 0.000000 USDC | 0.006931 USDC | 1.008226 USDC (0.9276 €) | — | 25.12 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.004597 cbBTC | 0.000011 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000011 cbBTC (0.7973 €) | — | 23.54 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.004597 cbBTC | 0.000011 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000011 cbBTC (0.7973 €) | — | 23.54 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 369.411480 USDC | 0.870282 USDC | 0.000000 USDC | 0.006931 USDC | 0.863351 USDC (0.7943 €) | — | 23.37 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53516727 | USDC→[aerodrome]→AERO→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 369.411480 USDC | 0.870282 USDC | 0.000000 USDC | 0.006931 USDC | 0.863351 USDC (0.7943 €) | — | 23.37 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |

## Fiabilité et décision
- Observations ghost : 5268 ; taux observé 0.162 ; borne inférieure crédible (0.9) 0.156 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
