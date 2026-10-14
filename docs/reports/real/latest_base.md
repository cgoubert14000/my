# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T15:22:14+00:00 ; durée 18.3 min ; blocs 52600436 → 52600993 (197 vus)

## Connexion
- Requêtes RPC : 3902 ; erreurs : 0 ; latence p50/p95 : 757.8/4,530.6 ms
- Rafraîchissements d'état : 197 ; âge des données au dernier bloc : 14.59 s ; changements de frais LP observés (pools à frais dynamiques) : 1257
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12806 ; cycles déclenchés par événement : 563 ; avance médiane sur le rafraîchissement multicall : 1,322 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,437.41 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 140 (quarantaine 2), aerodrome 235 (quarantaine 1), aerodrome_slipstream 153, pancakeswap_v3 30 (quarantaine 1), uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3920 (énumérés 391, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 5 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2425.371992, 'AERO': 0.862121, 'cbBTC': 81739.3593}
- Pools en quarantaine : 4 — pancakeswap_v3:WETH/AUKI@0xF9d4C7: simulation failed ×5 (model/chain mismatch) — until block 52601197; aerodrome:USDC/AUKI@0x437846: simulation failed ×5 (model/chain mismatch) — until block 52601197; uniswap_v3:USDC/SUP@0xF39B8a: simulation failed ×5 (model/chain mismatch) — until block 52601195; uniswap_v3:WETH/SUP@0xc4838F: simulation failed ×5 (model/chain mismatch) — until block 52601195

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,601,848 | 2,437.408841 | 52600991 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,398,122 | 1.160059 | 52600991 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,919,975 | 0.029764 | 52600991 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,905,848 | 107.967547 | 52600991 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2560 | 12,467,795 | 0.029730 | 52600991 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,499,308 | 0.029718 | 52600991 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,232,384 | 0.000012 | 52600993 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,199,809 | 2,436.182248 | 52600993 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,981,786 | 2,437.345055 | 52600991 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,111,964 | 0.000012 | 52600993 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 579 | 7,916,201 | 2,435.425173 | 52600991 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,174,414 | 0.001661 | 52600991 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 6,561,136 | 0.000012 | 52600993 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,442,293 | 0.029758 | 52600992 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,383,458 | 1.000859 | 52600991 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,216,549 | 0.026581 | 52600991 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,063,522 | 1.157179 | 52600991 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,632,830 | 0.000278 | 52600991 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,584,157 | 0.802388 | 52600991 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,417,273 | 2,435.218725 | 52600992 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 4,348,364 | 0.998900 | 52600991 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,012,966 | 34,990.015219 | 52600991 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,587,900 | 2,804.631894 | 52600991 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,948,944 | 1.141639 | 52600991 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,842,013 | 0.000012 | 52600991 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2751 | 2,565,069 | 107.932937 | 52600991 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,476,808 | 0.000011 | 52600991 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,377,648 | 1,066,812.609594 | 52600991 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,338,762 | 403.586368 | 52600991 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,182,793 | 2,439.442167 | 52600993 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,115,951 | 1.190950 | 52600991 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,100,831 | 0.000000 | 52600991 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,012,968 | 0.023437 | 52600991 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,909,330 | 0.916707 | 52600991 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,900,766 | 15.595019 | 52600991 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/MORPHO | 2754 | 1,848,468 | 1,043.099638 | 52600991 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,840,035 | 1.397535 | 52600991 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,769,586 | 0.018920 | 52600991 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,750,757 | 0.000012 | 52600993 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,635,145 | 2.304293 | 52600991 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,632,149 | 13,556.895023 | 52600991 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,516,749 | 2,824.266484 | 52600991 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,506,971 | 1.105776 | 52600991 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,858 | 0.836331 | 52600991 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,424,918 | 0.000000 | 52600991 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,360,804 | 0.000278 | 52600991 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,345,440 | 0.004806 | 52600991 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3036 | 1,341,983 | 2,824.244538 | 52600991 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,276,746 | 23.401964 | 52600991 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,253,028 | 2,436.243106 | 52600991 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,247,308 | 62.459029 | 52600991 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,237,961 | 33,248,568.751527 | 52600991 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,215,752 | 1.105594 | 52600991 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,204,174 | 1.131080 | 52600991 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/EDEL | 7000 | 1,187,608 | 72,662.798203 | 52600991 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,176,591 | 45.523715 | 52600991 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,166,017 | 493,173.304965 | 52600991 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,161,657 | 1,193,822.414145 | 52600991 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,133,227 | 13.653789 | 52600991 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,035,431 | 0.885315 | 52600991 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |

## Recherche d'opportunités
- Cycles : 759 ; routes examinées : 15942036 ; candidats optimisés : 120374 ; net attendu > 0 : 832 ; dernier cycle 188.6 ms
- Rejets (moteur) : {'spread_below_threshold': 15555808, 'liquidity_below_min': 147254, 'negative_expected_net': 119542, 'pool_quarantined': 94542, 'unquotable': 15894, 'borrow_bound_too_small': 4599, 'cycle_budget_exhausted': 3565}
- Enregistrements de la session : 120374 ; net attendu > 0 : 832 ; simulés (eth_call de la vraie tx) : 24 (ok 5, échec 19) ; étiquettes ghost N+1 : 0/14 positives
- Décisions : {'REJECTED': 120374} ; motifs de rejet : {'below_safety_margin': 804, 'negative_expected_net': 119542, 'price_impact': 6, 'reliability_not_demonstrated': 832, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 5, 'simulation_failed': 19, 'stale_data': 497}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52600862 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.236021 WETH | 0.000083 WETH | 0.000000 WETH | 0.000002 WETH | 0.000081 WETH (0.1803 €) | — | 0.65 | 0.003 (n=2) | REJECTED | below_safety_margin(80572873655235<247204155501096), reliability_not_demonstrated |
| 52600862 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.035155 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1798 €) | — | 0.68 | 0.003 (n=2) | REJECTED | below_safety_margin(239<703), reliability_not_demonstrated |
| 52600862 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.040788 WETH | 0.000068 WETH | 0.000000 WETH | 0.000002 WETH | 0.000065 WETH (0.1465 €) | — | 0.63 | 0.003 (n=2) | REJECTED | below_safety_margin(65460329991419<208157582204409), reliability_not_demonstrated |
| 52600862 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.028712 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1459 €) | — | 0.68 | 0.003 (n=2) | REJECTED | below_safety_margin(194<574), reliability_not_demonstrated |
| 52600862 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.028837 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1354 €) | — | 0.62 | 0.003 (n=2) | REJECTED | below_safety_margin(180<576), reliability_not_demonstrated |
| 52600862 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.892238 WETH | 0.000063 WETH | 0.000000 WETH | 0.000002 WETH | 0.000060 WETH (0.1353 €) | — | 0.68 | 0.003 (n=2) | REJECTED | below_safety_margin(60439176157500<178447505802959), reliability_not_demonstrated |
| 52600818 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,187.620992 USDC | 0.150904 USDC | 0.000000 USDC | 0.007995 USDC | 0.142909 USDC (0.1315 €) | — | 1.20 | 0.001 (n=14) | REJECTED | below_safety_margin(142909<237524), reliability_not_demonstrated |
| 52600818 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.489501 WETH | 0.000062 WETH | 0.000000 WETH | 0.000003 WETH | 0.000059 WETH (0.1310 €) | — | 1.20 | 0.001 (n=14) | REJECTED | below_safety_margin(58717639295016<97900106940413), reliability_not_demonstrated |
| 52600864 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,290.524278 USDC | 0.136890 USDC | 0.000000 USDC | 0.008380 USDC | 0.128510 USDC (0.1182 €) | — | 1.00 | 0.000 (n=16) | REJECTED | below_safety_margin(128510<258104), stale_data(5226ms>4000.0), reliability_not_demonstrated |
| 52600864 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.531096 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1179 €) | — | 0.99 | 0.000 (n=16) | REJECTED | below_safety_margin(52663053278228<106219260097614), stale_data(5219ms>4000.0), reliability_not_demonstrated |
| 52600789 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,120.342147 USDC | 0.135269 USDC | 0.000000 USDC | 0.007990 USDC | 0.127279 USDC (0.1171 €) | — | 1.14 | 0.001 (n=14) | REJECTED | below_safety_margin(127279<224068), reliability_not_demonstrated |
| 52600789 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.461665 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1169 €) | — | 1.13 | 0.001 (n=14) | REJECTED | below_safety_margin(52380512945299<92333025975433), reliability_not_demonstrated |
| 52600864 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,131.836208 USDC | 0.134275 USDC | 0.000000 USDC | 0.008008 USDC | 0.126267 USDC (0.1162 €) | — | 1.12 | 0.000 (n=16) | REJECTED | below_safety_margin(126267<226367), stale_data(5096ms>4000.0), reliability_not_demonstrated |
| 52600864 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.465027 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1158 €) | — | 1.11 | 0.000 (n=16) | REJECTED | below_safety_margin(51723970702919<93005482134803), stale_data(5090ms>4000.0), reliability_not_demonstrated |
| 52600865 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,129.216008 USDC | 0.133335 USDC | 0.000000 USDC | 0.008008 USDC | 0.125327 USDC (0.1153 €) | — | 1.11 | 0.000 (n=16) | REJECTED | below_safety_margin(125327<225843), stale_data(5992ms>4000.0), reliability_not_demonstrated |
| 52600866 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,129.216008 USDC | 0.133335 USDC | 0.000000 USDC | 0.008008 USDC | 0.125327 USDC (0.1153 €) | — | 1.11 | 0.000 (n=16) | REJECTED | below_safety_margin(125327<225843), stale_data(8003ms>4000.0), reliability_not_demonstrated |
| 52600865 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.463551 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000051 WETH (0.1149 €) | — | 1.11 | 0.000 (n=16) | REJECTED | below_safety_margin(51338598726463<92710238940151), stale_data(5985ms>4000.0), reliability_not_demonstrated |
| 52600866 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.463551 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000051 WETH (0.1149 €) | — | 1.11 | 0.000 (n=16) | REJECTED | below_safety_margin(51338598726463<92710238940151), stale_data(7996ms>4000.0), reliability_not_demonstrated |
| 52600862 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.916203 WETH | 0.000041 WETH | 0.000000 WETH | 0.000002 WETH | 0.000039 WETH (0.0868 €) | — | 0.42 | 0.003 (n=2) | REJECTED | below_safety_margin(38793785507145<183240659786817), reliability_not_demonstrated |
| 52600862 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.024812 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0865 €) | — | 0.46 | 0.003 (n=2) | REJECTED | below_safety_margin(115<496), reliability_not_demonstrated |
| 52600985 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.012082 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0761 €) | — | 0.84 | 0.000 (n=16) | REJECTED | below_safety_margin(101<241), reliability_not_demonstrated |
| 52600985 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,087.562962 USDC | 0.090147 USDC | 0.000000 USDC | 0.007943 USDC | 0.082204 USDC (0.0756 €) | — | 0.76 | 0.000 (n=16) | REJECTED | below_safety_margin(82204<217512), reliability_not_demonstrated |
| 52600985 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.382299 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0751 €) | — | 0.88 | 0.000 (n=16) | REJECTED | below_safety_margin(33507957130234<76459818655941), reliability_not_demonstrated |
| 52600818 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 753.890747 USDC | 0.085800 USDC | 0.000000 USDC | 0.007995 USDC | 0.077805 USDC (0.0716 €) | — | 1.03 | 0.001 (n=14) | REJECTED | below_safety_margin(77805<150778), reliability_not_demonstrated |
| 52600818 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.310476 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0713 €) | — | 1.03 | 0.001 (n=14) | REJECTED | below_safety_margin(31962114767247<62095251028885), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 151 ; taux observé 0.192 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
