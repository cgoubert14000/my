# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T17:22:31+00:00 ; durée 3.03 min ; blocs 53511708 → 53511802 (91 vus)

## Connexion
- Requêtes RPC : 1240 ; erreurs : 0 ; latence p50/p95 : 214.7/986.2 ms
- Rafraîchissements d'état : 91 ; âge des données au dernier bloc : 2.39 s ; changements de frais LP observés (pools à frais dynamiques) : 256
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2268 ; cycles déclenchés par événement : 197 ; avance médiane sur le rafraîchissement multicall : 446 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,427.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 502 pools, 289 jetons, 19560 routes
- Par DEX : uniswap_v3 145, aerodrome_slipstream 107, aerodrome 206, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3710 (énumérés 311, par paires 0), mesurés 505, sous le plancher de 10000.0 $ : 3 → gardés 502 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2427.762313, 'cbBTC': 80310.699989, 'AERO': 0.65591}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,518,194 | 2,427.770784 | 53511801 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,317,908 | 0.030207 | 53511801 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,681,449 | 0.030231 | 53511801 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,456,436 | 0.000012 | 53511801 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,354,611 | 2,426.266136 | 53511801 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,073,172 | 105.862650 | 53511801 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,821,404 | 0.001559 | 53511801 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,437,211 | 1.524600 | 53511801 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,976,482 | 0.030215 | 53511802 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,293,303 | 2,426.326125 | 53511802 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,229,757 | 0.999550 | 53511801 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,691,842 | 40,471.025799 | 53511801 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,484,487 | 2,426.117716 | 53511801 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,775,766 | 0.030225 | 53511801 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,304,147 | 1,125,545.377394 | 53511801 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 2,068,690 | 0.008088 | 53511801 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,849,949 | 0.000012 | 53511801 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,753,044 | 0.017984 | 53511801 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,748,006 | 0.000000 | 53511801 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,639,823 | 451.163432 | 53511801 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,628,376 | 0.000012 | 53511801 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,561,789 | 0.000012 | 53511801 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,522,741 | 1.474784 | 53511801 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,501,763 | 3,701.541859 | 53511801 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,440 | 0.816276 | 53511801 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,395,544 | 2,426.216840 | 53511801 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,380,927 | 2,429.298605 | 53511801 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,380,420 | 2,427.232318 | 53511801 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,340,906 | 14,950.769977 | 53511801 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,190,639 | 37,228,249.593390 | 53511801 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,157,988 | 72.465398 | 53511801 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,144,175 | 0.000000 | 53511801 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,112,886 | 557,919.552600 | 53511801 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,069,058 | 23,018,538.652786 | 53511801 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,043,445 | 105.101183 | 53511801 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 989,865 | 19.516825 | 53511801 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/WELL | 10000 | 986,421 | 1,263,599.891658 | 53511801 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 981,884 | 1,104.998365 | 53511801 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 978,299 | 65.412183 | 53511801 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 969,170 | 95,727.768182 | 53511801 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 966,926 | 0.000012 | 53511801 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 943,953 | 2,419.737204 | 53511801 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 913,806 | 0.000535 | 53511801 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 911,350 | 0.043628 | 53511801 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 870,284 | 3,679.007074 | 53511801 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 831,573 | 19.705532 | 53511801 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 824,051 | 0.799140 | 53511801 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 800,221 | 0.057402 | 53511802 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 755,527 | 4,884,018.689129 | 53511801 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 751,759 | 0.600184 | 53511801 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 736,412 | 0.000248 | 53511801 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 731,807 | 138,994.164393 | 53511801 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 699,595 | 0.000008 | 53511801 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 682,369 | 562,761.448154 | 53511801 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 679,038 | 0.577551 | 53511801 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 652,638 | 0.913292 | 53511801 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 644,104 | 2.613933 | 53511801 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 609,777 | 0.092228 | 53511801 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 570,350 | 0.039122 | 53511801 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/DRV | 3000 | 557,705 | 6,950.926145 | 53511801 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 287 ; routes examinées : 5613720 ; candidats optimisés : 17455 ; net attendu > 0 : 19 ; dernier cycle 53.5 ms
- Rejets (moteur) : {'spread_below_threshold': 5535705, 'liquidity_below_min': 60560, 'negative_expected_net': 17436}
- Enregistrements de la session : 17455 ; net attendu > 0 : 19 ; simulés (eth_call de la vraie tx) : 2 (ok 0, échec 2) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 17455} ; motifs de rejet : {'below_safety_margin': 17, 'negative_expected_net': 17436, 'p_lower_below_threshold': 16, 'reliability_not_demonstrated': 3, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53511734 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.721090 WETH | 0.000150 WETH | 0.000000 WETH | 0.000002 WETH | 0.000147 WETH (0.3292 €) | — | 2.04 | 0.044 (n=208) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53511734 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,748.991565 USDC | 0.363408 USDC | 0.000000 USDC | 0.005881 USDC | 0.357527 USDC (0.3289 €) | — | 2.04 | 0.044 (n=208) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53511734 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.502422 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1992 €) | — | 1.78 | 0.034 (n=24) | REJECTED | below_safety_margin(89184135546903<100484401015770), reliability_not_demonstrated |
| 53511734 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,220.153928 USDC | 0.224568 USDC | 0.000000 USDC | 0.008108 USDC | 0.216460 USDC (0.1991 €) | — | 1.77 | 0.034 (n=24) | REJECTED | below_safety_margin(216460<244030), reliability_not_demonstrated |
| 53511734 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.014562 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1990 €) | — | 1.85 | 0.034 (n=24) | REJECTED | below_safety_margin(269<291), reliability_not_demonstrated |
| 53511734 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.161036 WETH | 0.000021 WETH | 0.000000 WETH | 0.000002 WETH | 0.000019 WETH (0.0424 €) | — | 1.18 | 0.044 (n=208) | REJECTED | below_safety_margin(18967213709547<32207245541463), p_lower_below_threshold(0.04<0.75) |
| 53511734 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 389.739350 USDC | 0.051527 USDC | 0.000000 USDC | 0.005513 USDC | 0.046014 USDC (0.0423 €) | — | 1.18 | 0.044 (n=208) | REJECTED | below_safety_margin(46014<77947), p_lower_below_threshold(0.04<0.75) |
| 53511734 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006565 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0325 €) | — | 0.67 | 0.180 (n=907) | REJECTED | below_safety_margin(44<131), p_lower_below_threshold(0.18<0.75) |
| 53511734 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.249518 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0324 €) | — | 0.58 | 0.180 (n=907) | REJECTED | below_safety_margin(14518190717593<49903521877096), p_lower_below_threshold(0.18<0.75) |
| 53511734 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 584.148359 USDC | 0.042969 USDC | 0.000000 USDC | 0.007740 USDC | 0.035229 USDC (0.0324 €) | — | 0.60 | 0.180 (n=907) | REJECTED | below_safety_margin(35229<116829), p_lower_below_threshold(0.18<0.75) |
| 53511783 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.027132 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0049 €) | — | 0.80 | 0.043 (n=210) | REJECTED | below_safety_margin(2180687693690<5426333722050), p_lower_below_threshold(0.04<0.75) |
| 53511783 | USDC→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 65.185538 USDC | 0.010792 USDC | 0.000000 USDC | 0.005507 USDC | 0.005285 USDC (0.0049 €) | — | 0.81 | 0.043 (n=210) | REJECTED | below_safety_margin(5285<13037), p_lower_below_threshold(0.04<0.75) |
| 53511734 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.019318 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.11 | 0.180 (n=907) | REJECTED | below_safety_margin(202978014120<3863501180544), p_lower_below_threshold(0.18<0.75) |
| 53511734 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 63.029498 USDC | 0.007808 USDC | 0.000000 USDC | 0.007371 USDC | 0.000437 USDC (0.0004 €) | — | 0.07 | 0.180 (n=907) | REJECTED | below_safety_margin(437<12605), p_lower_below_threshold(0.18<0.75) |
| 53511750 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 37.977969 USDC | 0.007699 USDC | 0.000000 USDC | 0.007363 USDC | 0.000336 USDC (0.0003 €) | — | 0.09 | 0.180 (n=907) | REJECTED | below_safety_margin(336<7595), p_lower_below_threshold(0.18<0.75) |
| 53511782 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.056261 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0003 €) | — | 0.02 | 0.034 (n=62) | REJECTED | below_safety_margin(116188810669<11252162024963), p_lower_below_threshold(0.03<0.75) |
| 53511782 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.056261 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0003 €) | — | 0.02 | 0.034 (n=62) | REJECTED | below_safety_margin(116188810669<11252162024963), p_lower_below_threshold(0.03<0.75) |
| 53511782 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 135.337173 USDC | 0.005785 USDC | 0.000000 USDC | 0.005507 USDC | 0.000278 USDC (0.0003 €) | — | 0.02 | 0.034 (n=62) | REJECTED | below_safety_margin(278<27067), p_lower_below_threshold(0.03<0.75) |
| 53511782 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 135.337173 USDC | 0.005785 USDC | 0.000000 USDC | 0.005507 USDC | 0.000278 USDC (0.0003 €) | — | 0.02 | 0.034 (n=62) | REJECTED | below_safety_margin(278<27067), p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 5200 ; taux observé 0.164 ; borne inférieure crédible (0.9) 0.158 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
