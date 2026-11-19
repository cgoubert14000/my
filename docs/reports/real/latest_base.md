# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-19T18:28:23+00:00 ; durée 70.24 min ; blocs 59591500 → 59612599 (2058 vus)

## Connexion
- Requêtes RPC : 27362 ; erreurs : 385 ; latence p50/p95 : 382.0/1,830.3 ms
- Rafraîchissements d'état : 2058 ; âge des données au dernier bloc : 8.38 s ; changements de frais LP observés (pools à frais dynamiques) : 2936
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4681 ; cycles déclenchés par événement : 1186 ; avance médiane sur le rafraîchissement multicall : 490 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,779.43 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 428 pools, 248 jetons, 13064 routes
- Par DEX : uniswap_v3 129, aerodrome 172, aerodrome_slipstream 87, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 257, par paires 0), mesurés 430, sous le plancher de 10000.0 $ : 2 → gardés 428 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1755.680432, 'cbBTC': 62293.409251, 'AERO': 0.417081}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 86,466,916 | 1,779.437198 | 59612623 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/USDC | 500 | 25,729,427 | 1,783.611504 | 59612623 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,446,978 | 0.028259 | 59612623 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,796,808 | 0.028195 | 59612623 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,827,804 | 78.874789 | 59612623 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,960,288 | 0.000016 | 59612623 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,216,077 | 0.028250 | 59612623 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,611,332 | 2.360588 | 59612623 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,311,751 | 1.000000 | 59612623 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,299,740 | 1,783.644319 | 59612623 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,777,195 | 38,425.079779 | 59612623 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 239 | 2,330,033 | 1,783.429507 | 59612623 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,092,967 | 0.000016 | 59612623 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 1,736,294 | 0.028209 | 59612623 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,678,049 | 1,139,858.229140 | 59612623 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,006 | 0.844383 | 59612623 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,452,492 | 0.000016 | 59612623 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,334,540 | 0.000000 | 59612623 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,287,174 | 0.006529 | 59612623 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,262,843 | 0.000016 | 59612623 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,145,026 | 13.286509 | 59612623 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,062,090 | 448.043208 | 59612623 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/SEND | 3000 | 1,060,088 | 86.467991 | 59612623 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/VVV | 10000 | 1,032,423 | 78.585887 | 59612623 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/USDC | 3000 | 1,027,772 | 1,779.089891 | 59612623 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,026,891 | 15,875.129160 | 59612623 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,004,374 | 4,208.095044 | 59612623 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 992,794 | 1,779.234382 | 59612623 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/doginme | 10000 | 961,952 | 28,639,197.268741 | 59612623 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 930,781 | 0.044216 | 59612623 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 856,889 | 58.268836 | 59612623 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 832,626 | 523,906.753383 | 59612623 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 819,892 | 0.000000 | 59612623 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 801,660 | 22,203,974.752029 | 59612623 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 797,613 | 0.001545 | 59612623 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 742,235 | 1,087.665656 | 59612623 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | WETH/USDC | 500 | 737,604 | 1,783.659863 | 59612623 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | XDP/USDC | 100 | 732,630 | 0.014935 | 59612623 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/SAPIEN | 4970 | 723,313 | 24.182020 | 59612623 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 721,469 | 0.046260 | 59612623 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/USDC | 10000 | 698,599 | 1,769.013158 | 59612623 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 604,092 | 1,783.625523 | 59612623 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 603,990 | 0.798842 | 59612623 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 593,190 | 0.442055 | 59612623 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 561,468 | 4,778,411.393135 | 59612623 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 549,349 | 4,190.759325 | 59612623 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 518,640 | 524,679.817435 | 59612623 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 509,175 | 1.386543 | 59612623 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | FLOCK/USDC | 3000 | 501,783 | 0.031997 | 59612623 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 488,845 | 168,482.179333 | 59612623 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 8 | 461,380 | 1.001295 | 59612623 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 448,651 | 0.000007 | 59612623 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 433,126 | 0.000239 | 59612623 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | ELSA/USDC | 100 | 412,696 | 0.057730 | 59612623 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 404,143 | 1,087.634054 | 59612623 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/UNI | 10000 | 389,259 | 357.692790 | 59612623 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 388,984 | 24.103082 | 59612623 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 387,911 | 847,850.208800 | 59612623 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/VVV | 2799 | 374,782 | 78.832574 | 59612623 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | AWE/USDC | 3000 | 373,047 | 0.057867 | 59612623 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |

## Recherche d'opportunités
- Cycles : 3243 ; routes examinées : 42366552 ; candidats optimisés : 80039 ; net attendu > 0 : 51 ; dernier cycle 122.2 ms
- Rejets (moteur) : {'spread_below_threshold': 41528243, 'liquidity_below_min': 541978, 'negative_expected_net': 79988, 'borrow_bound_too_small': 4556, 'cycle_budget_exhausted': 2327}
- Enregistrements de la session : 52938 ; net attendu > 0 : 51 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 52938} ; motifs de rejet : {'below_safety_margin': 51, 'negative_expected_net': 52887, 'p_lower_below_threshold': 51, 'stale_data': 29}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59591958 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.126331 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0177 €) | — | 0.87 | 0.109 (n=377) | REJECTED | below_safety_margin(10948928198956<25266204118772), p_lower_below_threshold(0.11<0.75) |
| 59591958 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.126331 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0177 €) | — | 0.87 | 0.109 (n=377) | REJECTED | below_safety_margin(10948928198956<25266204118772), p_lower_below_threshold(0.11<0.75) |
| 59591958 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 218.769810 USDC | 0.023215 USDC | 0.000000 USDC | 0.004050 USDC | 0.019165 USDC (0.0176 €) | — | 0.88 | 0.109 (n=377) | REJECTED | below_safety_margin(19165<43753), p_lower_below_threshold(0.11<0.75) |
| 59591958 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 218.769810 USDC | 0.023215 USDC | 0.000000 USDC | 0.004050 USDC | 0.019165 USDC (0.0176 €) | — | 0.88 | 0.109 (n=377) | REJECTED | below_safety_margin(19165<43753), p_lower_below_threshold(0.11<0.75) |
| 59591958 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 47.588538 USDC | 0.009311 USDC | 0.000000 USDC | 0.005408 USDC | 0.003903 USDC (0.0036 €) | — | 0.82 | 0.272 (n=1639) | REJECTED | below_safety_margin(3903<9517), p_lower_below_threshold(0.27<0.75) |
| 59591958 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 47.588538 USDC | 0.009311 USDC | 0.000000 USDC | 0.005408 USDC | 0.003903 USDC (0.0036 €) | — | 0.82 | 0.272 (n=1639) | REJECTED | below_safety_margin(3903<9517), p_lower_below_threshold(0.27<0.75) |
| 59591958 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.026982 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 0.80 | 0.272 (n=1639) | REJECTED | below_safety_margin(2148914236807<5396318220261), p_lower_below_threshold(0.27<0.75) |
| 59591958 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.026982 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 0.80 | 0.272 (n=1639) | REJECTED | below_safety_margin(2148914236807<5396318220261), p_lower_below_threshold(0.27<0.75) |
| 59591958 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000624 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0034 €) | — | 0.96 | 0.272 (n=1639) | REJECTED | below_safety_margin(6<12), p_lower_below_threshold(0.27<0.75) |
| 59591958 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000624 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0034 €) | — | 0.96 | 0.272 (n=1639) | REJECTED | below_safety_margin(6<12), p_lower_below_threshold(0.27<0.75) |
| 59592754 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 52.540659 USDC | 0.006096 USDC | 0.000000 USDC | 0.003827 USDC | 0.002269 USDC (0.0021 €) | — | 0.43 | 0.253 (n=31) | REJECTED | below_safety_margin(2269<10508), stale_data(33749ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 59592754 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.030242 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0021 €) | — | 0.42 | 0.253 (n=31) | REJECTED | below_safety_margin(1280472426852<6048444384827), stale_data(33746ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 59592754 | USDC→[uniswap_v3]→SLC→[aerodrome]→WETH→[uniswap_v3]→USDC | 15.016684 USDC | 0.006500 USDC | 0.000000 USDC | 0.005190 USDC | 0.001310 USDC (0.0012 €) | — | 0.87 | 0.276 (n=243) | REJECTED | below_safety_margin(1310<3003), stale_data(33446ms>4000.0), p_lower_below_threshold(0.28<0.75) |
| 59592754 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SLC→[aerodrome]→WETH | 0.008724 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 0.84 | 0.276 (n=243) | REJECTED | below_safety_margin(734416735291<1744840239615), stale_data(33442ms>4000.0), p_lower_below_threshold(0.28<0.75) |
| 59593875 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 7.721666 USDC | 0.006654 USDC | 0.000000 USDC | 0.005601 USDC | 0.001053 USDC (0.0010 €) | — | 1.36 | 0.353 (n=641) | REJECTED | below_safety_margin(1053<1544), p_lower_below_threshold(0.35<0.75) |
| 59593876 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 7.811663 USDC | 0.006644 USDC | 0.000000 USDC | 0.005602 USDC | 0.001042 USDC (0.0010 €) | — | 1.33 | 0.353 (n=641) | REJECTED | below_safety_margin(1042<1562), p_lower_below_threshold(0.35<0.75) |
| 59593877 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 7.710664 USDC | 0.006638 USDC | 0.000000 USDC | 0.005603 USDC | 0.001035 USDC (0.0010 €) | — | 1.34 | 0.353 (n=641) | REJECTED | below_safety_margin(1035<1542), p_lower_below_threshold(0.35<0.75) |
| 59593875 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004412 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0010 €) | — | 1.32 | 0.353 (n=641) | REJECTED | below_safety_margin(584482381186<882329081164), p_lower_below_threshold(0.35<0.75) |
| 59593876 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004392 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0009 €) | — | 1.32 | 0.353 (n=641) | REJECTED | below_safety_margin(578113540988<878312182130), p_lower_below_threshold(0.35<0.75) |
| 59593877 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004392 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0009 €) | — | 1.31 | 0.353 (n=641) | REJECTED | below_safety_margin(574567064919<878312352930), p_lower_below_threshold(0.35<0.75) |
| 59592754 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 16.253466 USDC | 0.006388 USDC | 0.000000 USDC | 0.005433 USDC | 0.000955 USDC (0.0009 €) | — | 0.59 | 0.272 (n=1639) | REJECTED | below_safety_margin(955<3250), stale_data(33469ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 59592754 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.009233 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0009 €) | — | 0.58 | 0.272 (n=1639) | REJECTED | below_safety_margin(532603464847<1846647301195), stale_data(33462ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 59593875 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 7.531660 USDC | 0.006373 USDC | 0.000000 USDC | 0.005601 USDC | 0.000772 USDC (0.0007 €) | — | 1.03 | 0.272 (n=1639) | REJECTED | below_safety_margin(772<1506), p_lower_below_threshold(0.27<0.75) |
| 59593876 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 7.531660 USDC | 0.006373 USDC | 0.000000 USDC | 0.005602 USDC | 0.000771 USDC (0.0007 €) | — | 1.02 | 0.272 (n=1639) | REJECTED | below_safety_margin(771<1506), p_lower_below_threshold(0.27<0.75) |
| 59593877 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 7.531660 USDC | 0.006372 USDC | 0.000000 USDC | 0.005603 USDC | 0.000769 USDC (0.0007 €) | — | 1.02 | 0.272 (n=1639) | REJECTED | below_safety_margin(769<1506), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8576 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
