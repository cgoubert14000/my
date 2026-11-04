# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T23:05:19+00:00 ; durée 9.13 min ; blocs 53521807 → 53522085 (273 vus)

## Connexion
- Requêtes RPC : 3035 ; erreurs : 0 ; latence p50/p95 : 271.5/1,519.8 ms
- Rafraîchissements d'état : 274 ; âge des données au dernier bloc : 2.41 s ; changements de frais LP observés (pools à frais dynamiques) : 511
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 481 ; cycles déclenchés par événement : 54 ; avance médiane sur le rafraîchissement multicall : 480 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,432.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 503 pools, 289 jetons, 19656 routes
- Par DEX : uniswap_v3 145, aerodrome_slipstream 108, aerodrome 206, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3710 (énumérés 312, par paires 0), mesurés 506, sous le plancher de 10000.0 $ : 3 → gardés 503 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2435.517454, 'cbBTC': 80725.683876, 'AERO': 0.642935}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,942,016 | 2,432.113027 | 53522085 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,361,898 | 0.030182 | 53522085 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,693,277 | 0.030162 | 53522085 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,446,085 | 0.000012 | 53522085 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,395,551 | 2,428.683824 | 53522085 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,939,449 | 109.822272 | 53522085 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,831,339 | 0.001556 | 53522085 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,329,741 | 1.560284 | 53522085 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,030,162 | 0.030190 | 53522085 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,341,556 | 2,428.891331 | 53522085 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,241,432 | 0.999050 | 53522085 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,720,404 | 39,994.707901 | 53522085 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,488,507 | 2,428.566213 | 53522085 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,749,684 | 0.030166 | 53522085 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,274,983 | 1,158,722.007660 | 53522085 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,950,043 | 0.007385 | 53522085 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 1,827,001 | 0.000012 | 53522085 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,783,870 | 0.000000 | 53522085 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,759,910 | 0.018072 | 53522085 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,689,637 | 0.000012 | 53522085 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,648,402 | 446.267554 | 53522085 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,554,624 | 0.000012 | 53522085 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,524,440 | 1.472010 | 53522085 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,476,574 | 3,791.011866 | 53522085 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,448 | 0.816604 | 53522085 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,415,278 | 2,428.803052 | 53522085 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,382,351 | 2,432.743340 | 53522085 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,381,689 | 2,432.278093 | 53522085 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,350,322 | 14,801.631764 | 53522085 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,191,486 | 37,352,757.187842 | 53522085 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,296 | 73.310294 | 53522085 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,145,114 | 0.000000 | 53522085 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,112,758 | 561,007.284716 | 53522085 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,091,054 | 109.451377 | 53522085 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,070,936 | 23,018,510.187006 | 53522085 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 997,099 | 1,076.417856 | 53522085 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,955 | 19.285164 | 53522085 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 980,036 | 65.180500 | 53522085 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 965,573 | 0.000012 | 53522085 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 963,537 | 97,197.025922 | 53522085 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 948,467 | 2,419.823218 | 53522085 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 919,500 | 0.000536 | 53522085 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 887,074 | 0.045225 | 53522085 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 856,921 | 3,790.454216 | 53522085 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 831,349 | 19.716130 | 53522085 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 825,522 | 0.799146 | 53522085 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 807,665 | 0.058540 | 53522085 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 754,391 | 4,916,683.629057 | 53522085 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 750,191 | 0.602537 | 53522085 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 739,864 | 136,498.428768 | 53522085 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 734,248 | 0.000246 | 53522085 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 691,967 | 0.000008 | 53522085 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 681,646 | 556,282.330624 | 53522085 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 678,254 | 0.576246 | 53522085 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 652,773 | 0.914157 | 53522085 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 650,108 | 2.472419 | 53522085 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 609,435 | 0.102661 | 53522085 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 607,013 | 0.091574 | 53522085 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 572,741 | 0.039372 | 53522085 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 559,666 | 1,077.438403 | 53522085 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 327 ; routes examinées : 6427512 ; candidats optimisés : 17151 ; net attendu > 0 : 17 ; dernier cycle 260.4 ms
- Rejets (moteur) : {'spread_below_threshold': 6336758, 'liquidity_below_min': 73603, 'negative_expected_net': 17134}
- Enregistrements de la session : 17151 ; net attendu > 0 : 17 ; simulés (eth_call de la vraie tx) : 4 (ok 3, échec 1) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 17151} ; motifs de rejet : {'below_safety_margin': 2, 'negative_expected_net': 17134, 'p_lower_below_threshold': 17, 'simulation_failed': 1, 'stale_data': 1}

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
| 53521837 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 28.710657 USDC | 0.020882 USDC | 0.000000 USDC | 0.005469 USDC | 0.015413 USDC (0.0142 €) | — | 5.37 | 0.032 (n=263) | REJECTED | stale_data(4495ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53521820 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 44.813379 USDC | 0.007987 USDC | 0.000000 USDC | 0.007319 USDC | 0.000668 USDC (0.0006 €) | — | 0.15 | 0.178 (n=915) | REJECTED | below_safety_margin(668<8962), p_lower_below_threshold(0.18<0.75) |
| 53521820 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.018323 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.14 | 0.178 (n=915) | REJECTED | below_safety_margin(263912968201<3664642927433), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 5272 ; taux observé 0.162 ; borne inférieure crédible (0.9) 0.156 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
