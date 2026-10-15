# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T10:20:08+00:00 ; durée 148.06 min ; blocs 52630686 → 52635125 (4159 vus)

## Connexion
- Requêtes RPC : 48144 ; erreurs : 258 ; latence p50/p95 : 218.3/1,917.1 ms
- Rafraîchissements d'état : 4159 ; âge des données au dernier bloc : 6.27 s ; changements de frais LP observés (pools à frais dynamiques) : 9282
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1 ; cycles déclenchés par événement : 1 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,370.56 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 567 pools, 324 jetons, 20918 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 152, pancakeswap_v3 29, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 204 (rejetés 2) → 609 jetons ; pools candidats 3862 (énumérés 388, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 2 → gardés 567 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2370.057693, 'AERO': 0.841029, 'cbBTC': 81234.761422}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 143,702,860 | 2,370.556883 | 52635126 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,922,645 | 1.191322 | 52635126 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,839,555 | 0.029193 | 52635126 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,624,624 | 105.661997 | 52635126 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,808,519 | 0.029166 | 52635126 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,334,707 | 0.029158 | 52635126 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,607,840 | 0.000012 | 52635126 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,943,303 | 2,366.944848 | 52635126 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,856,857 | 2,370.964176 | 52635126 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 7,968,367 | 0.000012 | 52635126 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,082,101 | 0.001645 | 52635126 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 549 | 6,838,583 | 2,366.175968 | 52635126 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 6,574,516 | 0.000012 | 52635126 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,244,293 | 0.029183 | 52635126 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,152,260 | 0.026642 | 52635126 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,458,146 | 0.802389 | 52635126 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,366,868 | 0.000274 | 52635126 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,251,649 | 2,365.986758 | 52635126 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,166,502 | 1.000078 | 52635126 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,080,654 | 1.192760 | 52635126 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 3,880,721 | 35,391.529011 | 52635126 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,409,797 | 2,803.381663 | 52635126 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,823,122 | 0.000012 | 52635126 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,717,702 | 407.886645 | 52635126 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,536,883 | 105.700614 | 52635126 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,495,199 | 0.000010 | 52635126 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,475,685 | 1.141650 | 52635126 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome | WETH/FAI | 10000 | 2,330,532 | 1,050,309.238891 | 52635126 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,120,700 | 2,370.824288 | 52635126 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,489 | 1.194788 | 52635126 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52635126 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,964,266 | 0.000000 | 52635126 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,869,518 | 0.022623 | 52635126 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,809,361 | 15.774830 | 52635126 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,787,460 | 0.916541 | 52635126 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,773,492 | 0.000012 | 52635126 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,770,260 | 0.018860 | 52635126 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,680,091 | 2.301503 | 52635126 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,667,827 | 13,961.425042 | 52635126 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,472,575 | 2,819.038234 | 52635126 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,465,695 | 1.105502 | 52635126 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,410 | 0.831299 | 52635126 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,330,358 | 0.000000 | 52635126 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,305,945 | 2,816.596167 | 52635126 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,305,431 | 0.004793 | 52635126 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,301,860 | 23.181278 | 52635126 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,286,843 | 1.130555 | 52635126 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,278,293 | 0.000273 | 52635126 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 79 | 1,248,501 | 1.120828 | 52635126 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,246,459 | 62.544172 | 52635126 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,202,691 | 2,366.933626 | 52635126 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,179,163 | 1.105595 | 52635126 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,173,951 | 35,591,418.210733 | 52635126 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,142,477 | 0.029217 | 52635126 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/MORPHO | 2721 | 1,140,522 | 1,022.803551 | 52635126 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/WELL | 10000 | 1,136,333 | 1,180,140.375456 | 52635126 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,124,058 | 505,145.788086 | 52635126 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,123,204 | 77,509.744495 | 52635126 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,117,191 | 50.493801 | 52635126 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,114,284 | 14.228652 | 52635126 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 4159 ; routes examinées : 86997962 ; candidats optimisés : 602438 ; net attendu > 0 : 163 ; dernier cycle 389.8 ms
- Rejets (moteur) : {'spread_below_threshold': 85671762, 'liquidity_below_min': 710135, 'negative_expected_net': 602275, 'unquotable': 9057, 'borrow_bound_too_small': 4159, 'cycle_budget_exhausted': 411}
- Enregistrements de la session : 602438 ; net attendu > 0 : 163 ; simulés (eth_call de la vraie tx) : 3 (ok 3, échec 0) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 602438} ; motifs de rejet : {'below_safety_margin': 151, 'negative_expected_net': 602275, 'p_lower_below_threshold': 52, 'reliability_not_demonstrated': 111, 'stale_data': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52635092 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.006427 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0123 €) | 0.000006 WETH | 8.76 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52635092 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 15.182028 USDC | 0.020454 USDC | 0.000000 USDC | 0.007129 USDC | 0.013325 USDC (0.0123 €) | — | 8.78 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52635092 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.006352 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0119 €) | 0.000005 WETH | 8.57 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52635092 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 15.038896 USDC | 0.020011 USDC | 0.000000 USDC | 0.007129 USDC | 0.012882 USDC (0.0119 €) | — | 8.57 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52635092 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.005681 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0094 €) | 0.000004 WETH | 7.57 | 0.403 (n=14) | REJECTED | reliability_not_demonstrated |
| 52635092 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 13.459128 USDC | 0.017307 USDC | 0.000000 USDC | 0.007129 USDC | 0.010178 USDC (0.0094 €) | — | 7.56 | 0.403 (n=14) | REJECTED | reliability_not_demonstrated |
| 52635092 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004991 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0047 €) | — | 4.35 | 0.403 (n=14) | REJECTED | reliability_not_demonstrated |
| 52635092 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 11.821367 USDC | 0.012268 USDC | 0.000000 USDC | 0.007129 USDC | 0.005139 USDC (0.0047 €) | — | 4.35 | 0.403 (n=14) | REJECTED | reliability_not_demonstrated |
| 52633002 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.001862 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.21 | 0.071 (n=30) | REJECTED | below_safety_margin(4<37), p_lower_below_threshold(0.07<0.75) |
| 52633002 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 194.176044 USDC | 0.010260 USDC | 0.000000 USDC | 0.007128 USDC | 0.003132 USDC (0.0029 €) | — | 0.16 | 0.071 (n=30) | REJECTED | below_safety_margin(3132<38835), p_lower_below_threshold(0.07<0.75) |
| 52635092 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004534 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0028 €) | — | 2.79 | 0.071 (n=30) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 52635092 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.642764 USDC | 0.010125 USDC | 0.000000 USDC | 0.007129 USDC | 0.002996 USDC (0.0028 €) | — | 2.82 | 0.071 (n=30) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 52635092 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004534 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0028 €) | — | 2.78 | 0.299 (n=21) | REJECTED | reliability_not_demonstrated |
| 52635092 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.662783 USDC | 0.010115 USDC | 0.000000 USDC | 0.007129 USDC | 0.002986 USDC (0.0027 €) | — | 2.80 | 0.299 (n=21) | REJECTED | reliability_not_demonstrated |
| 52635092 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.004159 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.63 | 0.299 (n=21) | REJECTED | below_safety_margin(677314632994<831853076582), reliability_not_demonstrated |
| 52635092 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.750962 USDC | 0.008732 USDC | 0.000000 USDC | 0.007129 USDC | 0.001603 USDC (0.0015 €) | — | 1.64 | 0.299 (n=21) | REJECTED | below_safety_margin(1603<1950), reliability_not_demonstrated |
| 52633002 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 161.706871 USDC | 0.008627 USDC | 0.000000 USDC | 0.007128 USDC | 0.001499 USDC (0.0014 €) | — | 0.09 | 0.071 (n=30) | REJECTED | below_safety_margin(1499<32341), p_lower_below_threshold(0.07<0.75) |
| 52633965 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.726653 USDC | 0.008608 USDC | 0.000000 USDC | 0.007131 USDC | 0.001477 USDC (0.0014 €) | — | 1.52 | 0.299 (n=21) | REJECTED | below_safety_margin(1477<1945), reliability_not_demonstrated |
| 52633965 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004176 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 1.49 | 0.299 (n=21) | REJECTED | below_safety_margin(621265028040<835205070426), reliability_not_demonstrated |
| 52633965 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008564 USDC | 0.000000 USDC | 0.007131 USDC | 0.001433 USDC (0.0013 €) | — | 1.47 | 0.071 (n=30) | REJECTED | below_safety_margin(1433<1945), p_lower_below_threshold(0.07<0.75) |
| 52633965 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004178 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.44 | 0.071 (n=30) | REJECTED | below_safety_margin(602801913733<835657501441), p_lower_below_threshold(0.07<0.75) |
| 52633957 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633958 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633959 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633960 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |

## Fiabilité et décision
- Observations ghost : 261 ; taux observé 0.188 ; borne inférieure crédible (0.9) 0.159 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
