# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T14:27:32+00:00 ; durée 116.79 min ; blocs 56049289 → 56084288 (2724 vus)

## Connexion
- Requêtes RPC : 43800 ; erreurs : 80 ; latence p50/p95 : 823.4/2,126.8 ms
- Rafraîchissements d'état : 2724 ; âge des données au dernier bloc : 16.47 s ; changements de frais LP observés (pools à frais dynamiques) : 2574
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2556 ; cycles déclenchés par événement : 748 ; avance médiane sur le rafraîchissement multicall : 935 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,052.24 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 15580 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 283, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2055.911323, 'cbBTC': 73875.741474, 'AERO': 0.535737}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,181,404 | 2,052.236008 | 56084335 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,395,048 | 0.027826 | 56084335 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,569,791 | 0.027840 | 56084335 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,415,266 | 0.000014 | 56084335 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,082,954 | 2,047.263173 | 56084335 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,849,531 | 104.592832 | 56084335 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,274,984 | 0.027831 | 56084335 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,255,726 | 1.843820 | 56084335 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,036,739 | 2,046.786754 | 56084335 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,876,642 | 1.000002 | 56084335 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,041,552 | 42,606.454411 | 56084335 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,915,988 | 2,046.944864 | 56084335 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,208,012 | 0.027826 | 56084335 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,950,176 | 1,122,542.542992 | 56084335 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,647,178 | 0.000014 | 56084335 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,620,457 | 0.016363 | 56084335 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,608,409 | 0.000014 | 56084335 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,548,306 | 0.000000 | 56084335 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,530,431 | 0.000014 | 56084335 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,513,854 | 0.006546 | 56084335 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,465,227 | 0.827839 | 56084335 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,000 | 1.373193 | 56084335 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,415,257 | 419.425451 | 56084335 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,270,244 | 2,052.297356 | 56084335 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,264,185 | 3,771.141467 | 56084335 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,228,052 | 15,052.657325 | 56084335 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,156,405 | 2,052.717164 | 56084335 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,126,546 | 2,047.355589 | 56084335 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,862 | 86.341789 | 56084335 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,043,991 | 33,332,866.804384 | 56084335 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,000,812 | 105.258771 | 56084335 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 962,675 | 21.207579 | 56084335 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 941,595 | 555,979.661887 | 56084335 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 917,920 | 0.001492 | 56084335 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 912,407 | 0.000014 | 56084335 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 904,054 | 0.051065 | 56084335 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 902,477 | 23,072,783.026731 | 56084335 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 885,114 | 1,011.390297 | 56084335 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 877,971 | 2,050.503253 | 56084335 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 866,256 | 0.000000 | 56084335 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 774,585 | 78.396128 | 56084335 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 766,816 | 0.052477 | 56084335 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 758,414 | 22.554487 | 56084335 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 737,446 | 118,069.969523 | 56084335 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 706,699 | 3,766.926328 | 56084335 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 694,808 | 0.802938 | 56084335 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 674,827 | 0.538216 | 56084335 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 657,253 | 4,621,202.569414 | 56084335 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 622,771 | 0.488440 | 56084335 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 613,905 | 141,572.105797 | 56084335 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 586,172 | 0.000007 | 56084335 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 581,291 | 0.000260 | 56084335 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 578,663 | 552,688.153874 | 56084335 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 562,505 | 0.037989 | 56084335 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 494,605 | 1,011.149061 | 56084335 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 463,443 | 0.066705 | 56084335 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 457,872 | 0.492814 | 56084335 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,344 | 1.000916 | 56084335 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/uSOL | 3000 | 442,223 | 24.553039 | 56084335 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 436,604 | 915,629.438825 | 56084335 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 3471 ; routes examinées : 54078180 ; candidats optimisés : 287319 ; net attendu > 0 : 551 ; dernier cycle 313.4 ms
- Rejets (moteur) : {'spread_below_threshold': 52867600, 'liquidity_below_min': 913931, 'negative_expected_net': 286768, 'borrow_bound_too_small': 6767, 'cycle_budget_exhausted': 2430, 'unquotable': 133}
- Enregistrements de la session : 287319 ; net attendu > 0 : 551 ; simulés (eth_call de la vraie tx) : 28 (ok 12, échec 16) ; étiquettes ghost N+1 : 19/25 positives
- Décisions : {'REJECTED': 287319} ; motifs de rejet : {'below_safety_margin': 347, 'negative_expected_net': 286768, 'p_lower_below_threshold': 520, 'price_impact': 5, 'reliability_not_demonstrated': 31, 'simulation_failed': 16, 'stale_data': 246}

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
- Observations ghost : 8082 ; taux observé 0.214 ; borne inférieure crédible (0.9) 0.208 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
