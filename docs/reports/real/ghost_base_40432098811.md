# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T06:54:54+00:00 ; durée 327.13 min ; blocs 53137556 → 53147369 (9649 vus)

## Connexion
- Requêtes RPC : 115229 ; erreurs : 43 ; latence p50/p95 : 270.7/1,534.5 ms
- Rafraîchissements d'état : 9650 ; âge des données au dernier bloc : 2.03 s ; changements de frais LP observés (pools à frais dynamiques) : 12751
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 68883 ; cycles déclenchés par événement : 6858 ; avance médiane sur le rafraîchissement multicall : 660 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,306.24 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 305 jetons, 19446 routes
- Par DEX : uniswap_v3 143, aerodrome 212, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 3 → gardés 530 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2322.398057, 'cbBTC': 80000.770706, 'AERO': 0.673032}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,455,447 | 2,306.241182 | 53147369 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,076,741 | 0.028943 | 53147369 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,057,380 | 0.028948 | 53147369 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,481,603 | 0.000013 | 53147369 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,367,441 | 93.898464 | 53147369 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,302,095 | 2,301.471152 | 53147369 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 6,942,124 | 1.502331 | 53147369 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,924,626 | 0.001635 | 53147369 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,323,437 | 0.028931 | 53147369 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,211,776 | 2,301.304041 | 53147369 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,448,738 | 2,301.419973 | 53147369 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,197,073 | 0.998750 | 53147369 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,644,388 | 37,484.068293 | 53147369 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,164,347 | 0.028975 | 53147369 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,477,884 | 94.007141 | 53147369 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,434,947 | 0.000013 | 53147369 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 2,352,014 | 2,305.473632 | 53147369 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/FAI | 10000 | 2,104,479 | 1,217,557.512867 | 53147369 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,839,540 | 0.018862 | 53147369 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,824,564 | 0.000000 | 53147369 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,747,454 | 406.020024 | 53147369 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,686,539 | 0.000013 | 53147369 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,684,432 | 0.000013 | 53147369 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,659,899 | 0.000013 | 53147369 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,496,954 | 0.005854 | 53147369 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,181 | 0.826254 | 53147369 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53147369 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,416,584 | 3,460.225421 | 53147369 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,361,079 | 14,012.114164 | 53147369 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,244,394 | 2,301.359790 | 53147369 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,226,529 | 0.000265 | 53147369 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53147369 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,195,553 | 3,447.248911 | 53147369 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,165,677 | 0.000266 | 53147369 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,135,246 | 0.000000 | 53147369 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,130,865 | 1,091,191.188509 | 53147369 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,129,348 | 37,286,274.837589 | 53147369 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,098,028 | 501,544.213942 | 53147369 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,065,488 | 71,790.977957 | 53147369 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,053,523 | 20,512,964.965661 | 53147369 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,034,760 | 17.223560 | 53147369 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,028,927 | 59.129273 | 53147369 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 1,001,473 | 0.040803 | 53147369 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 949,321 | 2,317.651257 | 53147369 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 906,941 | 1,061.268105 | 53147369 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 901,595 | 2.308782 | 53147369 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 891,411 | 0.000560 | 53147369 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 874,737 | 18.117301 | 53147369 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 867,213 | 93.245174 | 53147369 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 842,370 | 2,306.128495 | 53147369 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 841,218 | 17.458614 | 53147369 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 802,704 | 0.057819 | 53147369 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 789,401 | 0.000008 | 53147369 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 780,835 | 0.803179 | 53147369 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,074 | 0.612483 | 53147369 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 736,299 | 4,631,924.400756 | 53147369 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 696,656 | 0.610492 | 53147369 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 695,003 | 138,586.395113 | 53147369 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 685,464 | 501,342.860765 | 53147369 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,519 | 0.108933 | 53147369 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 16507 ; routes examinées : 320995122 ; candidats optimisés : 828038 ; net attendu > 0 : 497 ; dernier cycle 368.9 ms
- Rejets (moteur) : {'spread_below_threshold': 315571128, 'liquidity_below_min': 4182021, 'negative_expected_net': 827541, 'unquotable': 356210, 'pool_quarantined': 40112, 'borrow_bound_too_small': 16492, 'cycle_budget_exhausted': 1121}
- Enregistrements de la session : 828038 ; net attendu > 0 : 497 ; simulés (eth_call de la vraie tx) : 36 (ok 5, échec 31) ; étiquettes ghost N+1 : 0/33 positives
- Décisions : {'REJECTED': 828038} ; motifs de rejet : {'below_safety_margin': 214, 'negative_expected_net': 827541, 'p_lower_below_threshold': 362, 'price_impact': 3, 'reliability_not_demonstrated': 135, 'simulation_failed': 31, 'stale_data': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53143351 | WETH→[uniswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.054583 WETH | 0.000952 WETH | 0.000000 WETH | 0.000003 WETH | 0.000950 WETH (2.0209 €) | — | 173.98 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143351 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.054910 WETH | 0.000951 WETH | 0.000000 WETH | 0.000003 WETH | 0.000948 WETH (2.0177 €) | — | 172.67 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 125.935794 USDC | 2.196972 USDC | 0.000000 USDC | 0.005914 USDC | 2.191058 USDC (2.0158 €) | — | 173.98 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 126.695173 USDC | 2.193525 USDC | 0.000000 USDC | 0.005914 USDC | 2.187611 USDC (2.0126 €) | — | 172.67 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.054616 WETH | 0.000943 WETH | 0.000000 WETH | 0.000003 WETH | 0.000940 WETH (2.0009 €) | — | 172.16 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[aerodrome_slipstream]→USDC | 126.003261 USDC | 2.175157 USDC | 0.000000 USDC | 0.005914 USDC | 2.169243 USDC (1.9957 €) | — | 172.16 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.052424 WETH | 0.000919 WETH | 0.000000 WETH | 0.000003 WETH | 0.000916 WETH (1.9497 €) | — | 174.76 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 120.934634 USDC | 2.119371 USDC | 0.000000 USDC | 0.005914 USDC | 2.113457 USDC (1.9444 €) | — | 174.76 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[uniswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.052451 WETH | 0.000916 WETH | 0.000000 WETH | 0.000003 WETH | 0.000913 WETH (1.9428 €) | — | 174.06 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 120.990801 USDC | 2.111837 USDC | 0.000000 USDC | 0.005914 USDC | 2.105923 USDC (1.9374 €) | — | 174.06 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[sushiswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.050692 WETH | 0.000890 WETH | 0.000000 WETH | 0.000003 WETH | 0.000888 WETH (1.8887 €) | — | 175.08 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[sushiswap_v3]→USDC | 116.842036 USDC | 2.051957 USDC | 0.000000 USDC | 0.006265 USDC | 2.045692 USDC (1.8820 €) | — | 175.08 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.051526 WETH | 0.000883 WETH | 0.000000 WETH | 0.000003 WETH | 0.000880 WETH (1.8737 €) | — | 170.88 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[aerodrome_slipstream]→USDC | 118.668551 USDC | 2.033663 USDC | 0.000000 USDC | 0.005914 USDC | 2.027749 USDC (1.8655 €) | — | 170.88 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.062844 WETH | 0.000743 WETH | 0.000000 WETH | 0.000003 WETH | 0.000741 WETH (1.5767 €) | — | 117.90 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.062754 WETH | 0.000742 WETH | 0.000000 WETH | 0.000003 WETH | 0.000740 WETH (1.5746 €) | — | 117.91 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.063188 WETH | 0.000742 WETH | 0.000000 WETH | 0.000003 WETH | 0.000740 WETH (1.5741 €) | — | 117.06 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143242 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 145.055042 USDC | 1.716050 USDC | 0.000000 USDC | 0.005912 USDC | 1.710138 USDC (1.5733 €) | — | 117.90 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 144.861660 USDC | 1.713938 USDC | 0.000000 USDC | 0.005912 USDC | 1.708026 USDC (1.5714 €) | — | 117.91 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 145.855037 USDC | 1.713297 USDC | 0.000000 USDC | 0.005912 USDC | 1.707385 USDC (1.5708 €) | — | 117.06 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.060312 WETH | 0.000692 WETH | 0.000000 WETH | 0.000003 WETH | 0.000689 WETH (1.4665 €) | — | 114.26 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 139.311377 USDC | 1.597670 USDC | 0.000000 USDC | 0.005912 USDC | 1.591758 USDC (1.4644 €) | — | 114.26 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.058628 WETH | 0.000691 WETH | 0.000000 WETH | 0.000003 WETH | 0.000688 WETH (1.4643 €) | — | 117.37 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 135.528430 USDC | 1.596572 USDC | 0.000000 USDC | 0.005912 USDC | 1.590660 USDC (1.4634 €) | — | 117.37 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.060344 WETH | 0.000688 WETH | 0.000000 WETH | 0.000003 WETH | 0.000685 WETH (1.4577 €) | — | 113.51 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2808 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
