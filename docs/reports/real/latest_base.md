# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T15:04:42+00:00 ; durée 153.97 min ; blocs 56049289 → 56095398 (3701 vus)

## Connexion
- Requêtes RPC : 58782 ; erreurs : 80 ; latence p50/p95 : 921.8/3,865.0 ms
- Rafraîchissements d'état : 3701 ; âge des données au dernier bloc : 23.93 s ; changements de frais LP observés (pools à frais dynamiques) : 3736
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2738 ; cycles déclenchés par événement : 816 ; avance médiane sur le rafraîchissement multicall : 960 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,052.71 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 15580 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 283, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2055.911323, 'cbBTC': 73875.741474, 'AERO': 0.535737}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,102,632 | 2,052.705111 | 56095484 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,390,185 | 0.027928 | 56095484 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,564,533 | 0.027860 | 56095484 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,397,086 | 0.000014 | 56095484 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,084,268 | 2,053.002185 | 56095484 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,847,842 | 104.692147 | 56095484 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,281,931 | 0.027920 | 56095484 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,260,890 | 1.839299 | 56095484 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,037,194 | 2,052.180902 | 56095484 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,863,381 | 1.000002 | 56095484 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,043,595 | 42,568.715093 | 56095484 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,916,619 | 2,052.614464 | 56095484 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,207,416 | 0.027873 | 56095484 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,951,622 | 1,121,392.886244 | 56095484 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,643,026 | 0.000014 | 56095484 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,630,824 | 0.016522 | 56095484 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,604,267 | 0.000014 | 56095484 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,548,609 | 0.000000 | 56095484 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,526,823 | 0.000014 | 56095484 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,508,573 | 0.006516 | 56095484 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,465,227 | 0.827839 | 56095484 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,000 | 1.373193 | 56095484 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,415,803 | 419.193666 | 56095484 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,270,395 | 2,056.660690 | 56095484 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,262,007 | 3,775.045225 | 56095484 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,226,104 | 15,037.081169 | 56095484 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,156,537 | 2,049.610771 | 56095484 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,126,806 | 2,053.287318 | 56095484 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,862 | 86.341789 | 56095484 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,043,223 | 33,427,198.693464 | 56095484 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,000,181 | 105.260336 | 56095484 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 967,392 | 20.894683 | 56095484 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 941,809 | 555,979.952574 | 56095484 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 915,176 | 0.001494 | 56095484 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 909,497 | 0.000014 | 56095484 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 903,476 | 0.051007 | 56095484 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 902,833 | 23,053,289.280513 | 56095484 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 884,547 | 1,013.219669 | 56095484 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 878,045 | 2,050.503253 | 56095484 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 858,753 | 0.000000 | 56095484 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 775,913 | 78.127853 | 56095484 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 765,745 | 0.052325 | 56095484 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 758,414 | 22.554487 | 56095484 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 740,439 | 117,171.074716 | 56095484 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 707,646 | 3,766.926328 | 56095484 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 694,966 | 0.802938 | 56095484 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 676,624 | 0.540881 | 56095484 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 655,822 | 4,642,423.119045 | 56095484 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 621,745 | 0.486971 | 56095484 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 611,171 | 142,912.974869 | 56095484 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 586,486 | 0.000007 | 56095484 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 582,267 | 0.000261 | 56095484 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 578,795 | 553,482.616140 | 56095484 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,420 | 0.038393 | 56095484 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 494,307 | 1,013.901460 | 56095484 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 462,783 | 0.066633 | 56095484 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 457,356 | 0.492814 | 56095484 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 11 | 454,359 | 1.000929 | 56095484 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/uSOL | 3000 | 441,663 | 24.626018 | 56095484 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 436,146 | 915,629.438825 | 56095484 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 4516 ; routes examinées : 70359280 ; candidats optimisés : 395197 ; net attendu > 0 : 779 ; dernier cycle 282.6 ms
- Rejets (moteur) : {'spread_below_threshold': 68768187, 'liquidity_below_min': 1183443, 'negative_expected_net': 394418, 'borrow_bound_too_small': 7804, 'cycle_budget_exhausted': 3478, 'unquotable': 1171}
- Enregistrements de la session : 395197 ; net attendu > 0 : 779 ; simulés (eth_call de la vraie tx) : 34 (ok 18, échec 16) ; étiquettes ghost N+1 : 22/31 positives
- Décisions : {'REJECTED': 395197} ; motifs de rejet : {'below_safety_margin': 558, 'negative_expected_net': 394418, 'p_lower_below_threshold': 746, 'price_impact': 5, 'reliability_not_demonstrated': 33, 'simulation_failed': 16, 'stale_data': 361}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56078498 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→AERO→[uniswap_v3]→USDC | 283.749829 USDC | 1.665935 USDC | 0.000000 USDC | 0.006212 USDC | 1.659723 USDC (1.5269 €) | — | 58.49 | 0.000 (n=28) | REJECTED | stale_data(6845ms>4000.0), reliability_not_demonstrated |
| 56078498 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 92.297241 USDC | 0.686225 USDC | 0.000000 USDC | 0.005900 USDC | 0.680325 USDC (0.6259 €) | — | 73.71 | 0.001 (n=12) | REJECTED | stale_data(6516ms>4000.0), reliability_not_demonstrated |
| 56079752 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.367955 WETH | 0.000323 WETH | 0.000000 WETH | 0.000003 WETH | 0.000320 WETH (0.6041 €) | — | 2.34 | 0.263 (n=1564) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.26<0.75) |
| 56079752 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.037397 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6040 €) | — | 2.38 | 0.263 (n=1564) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.26<0.75) |
| 56079752 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,851.810954 USDC | 0.662370 USDC | 0.000000 USDC | 0.006809 USDC | 0.655561 USDC (0.6031 €) | — | 2.30 | 0.263 (n=1564) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.26<0.75) |
| 56078498 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 361.819401 USDC | 0.640285 USDC | 0.000000 USDC | 0.006212 USDC | 0.634073 USDC (0.5833 €) | — | 17.52 | 0.132 (n=64) | REJECTED | stale_data(6739ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 56078498 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.176038 WETH | 0.000311 WETH | 0.000000 WETH | 0.000003 WETH | 0.000308 WETH (0.5825 €) | — | 17.52 | 0.132 (n=64) | REJECTED | stale_data(6732ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 56078498 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[aerodrome]→USDC | 250.590938 USDC | 0.637088 USDC | 0.000000 USDC | 0.005909 USDC | 0.631179 USDC (0.5807 €) | — | 25.19 | 0.172 (n=26) | REJECTED | reliability_not_demonstrated |
| 56078498 | cbBTC→[uniswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.003388 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.5794 €) | — | 25.23 | 0.172 (n=26) | REJECTED | reliability_not_demonstrated |
| 56078498 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[aerodrome]→USDC | 250.553857 USDC | 0.630506 USDC | 0.000000 USDC | 0.005909 USDC | 0.624597 USDC (0.5746 €) | — | 24.93 | 0.006 (n=128) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 56078498 | cbBTC→[uniswap_v3]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→cbBTC | 0.003328 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5733 €) | — | 25.42 | 0.006 (n=128) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 56078498 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[aerodrome]→USDC | 242.941149 USDC | 0.585349 USDC | 0.000000 USDC | 0.005909 USDC | 0.579440 USDC (0.5331 €) | — | 23.85 | 0.006 (n=128) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 56078498 | cbBTC→[uniswap_v3]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→cbBTC | 0.003255 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5319 €) | — | 24.12 | 0.006 (n=128) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 56078498 | USDC→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 86.216075 USDC | 0.578432 USDC | 0.000000 USDC | 0.005900 USDC | 0.572532 USDC (0.5267 €) | — | 66.41 | 0.000 (n=28) | REJECTED | stale_data(6587ms>4000.0), reliability_not_demonstrated |
| 56078498 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→AERO→[aerodrome]→USDC | 240.089070 USDC | 0.569965 USDC | 0.000000 USDC | 0.005909 USDC | 0.564056 USDC (0.5189 €) | — | 23.49 | 0.006 (n=128) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 56078498 | cbBTC→[uniswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→cbBTC | 0.003148 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5170 €) | — | 24.24 | 0.006 (n=128) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 56078498 | USDC→[aerodrome]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 76.582313 USDC | 0.553026 USDC | 0.000000 USDC | 0.005617 USDC | 0.547409 USDC (0.5036 €) | — | 71.48 | 0.000 (n=28) | REJECTED | stale_data(6542ms>4000.0), reliability_not_demonstrated |
| 56078498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 341.057962 USDC | 0.548017 USDC | 0.000000 USDC | 0.006212 USDC | 0.541805 USDC (0.4985 €) | — | 15.89 | 0.132 (n=64) | REJECTED | stale_data(6763ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 56078498 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.165921 WETH | 0.000266 WETH | 0.000000 WETH | 0.000003 WETH | 0.000263 WETH (0.4976 €) | — | 15.88 | 0.132 (n=64) | REJECTED | stale_data(6756ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 56078498 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→AERO→[aerodrome]→USDC | 396.199778 USDC | 0.544188 USDC | 0.000000 USDC | 0.005617 USDC | 0.538571 USDC (0.4955 €) | — | 13.59 | 0.073 (n=208) | REJECTED | stale_data(6824ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 56078498 | WETH→[aerodrome]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.192630 WETH | 0.000265 WETH | 0.000000 WETH | 0.000003 WETH | 0.000262 WETH (0.4948 €) | — | 13.60 | 0.073 (n=208) | REJECTED | stale_data(6821ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 56078498 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 331.628561 USDC | 0.519817 USDC | 0.000000 USDC | 0.006212 USDC | 0.513605 USDC (0.4725 €) | — | 15.49 | 0.031 (n=46) | REJECTED | stale_data(6777ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 56078498 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.161513 WETH | 0.000253 WETH | 0.000000 WETH | 0.000003 WETH | 0.000250 WETH (0.4717 €) | — | 15.46 | 0.031 (n=46) | REJECTED | stale_data(6770ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 56078498 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 319.945943 USDC | 0.490633 USDC | 0.000000 USDC | 0.006212 USDC | 0.484421 USDC (0.4457 €) | — | 15.14 | 0.031 (n=46) | REJECTED | stale_data(6790ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 56078498 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.155549 WETH | 0.000239 WETH | 0.000000 WETH | 0.000003 WETH | 0.000235 WETH (0.4448 €) | — | 15.14 | 0.031 (n=46) | REJECTED | stale_data(6784ms>4000.0), p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 8088 ; taux observé 0.214 ; borne inférieure crédible (0.9) 0.208 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
