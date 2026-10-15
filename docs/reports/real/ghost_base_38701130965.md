# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T12:14:09+00:00 ; durée 262.08 min ; blocs 52630686 → 52638546 (7329 vus)

## Connexion
- Requêtes RPC : 84786 ; erreurs : 560 ; latence p50/p95 : 176.3/1,965.3 ms
- Rafraîchissements d'état : 7329 ; âge des données au dernier bloc : 2.18 s ; changements de frais LP observés (pools à frais dynamiques) : 17438
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1 ; cycles déclenchés par événement : 1 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,364.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 567 pools, 324 jetons, 20918 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 152, pancakeswap_v3 29, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 204 (rejetés 2) → 609 jetons ; pools candidats 3862 (énumérés 388, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 2 → gardés 567 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2370.057693, 'AERO': 0.841029, 'cbBTC': 81234.761422}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 143,369,220 | 2,364.461077 | 52638546 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,845,842 | 1.196939 | 52638546 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,759,997 | 0.029199 | 52638546 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,605,253 | 105.380443 | 52638546 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,762,679 | 0.029166 | 52638546 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,330,857 | 0.029158 | 52638546 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,597,182 | 0.000012 | 52638546 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,914,593 | 2,362.191711 | 52638546 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,845,574 | 2,364.752394 | 52638546 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 7,934,467 | 0.000012 | 52638546 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 7,281,261 | 2,362.949933 | 52638546 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,058,935 | 0.001646 | 52638546 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 7,029,496 | 0.000012 | 52638546 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,221,620 | 0.029209 | 52638546 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,147,007 | 0.026791 | 52638546 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,446,682 | 0.802389 | 52638546 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,355,696 | 0.000274 | 52638546 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,259,958 | 0.999940 | 52638546 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,253,046 | 2,363.110714 | 52638546 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,126,269 | 1.192761 | 52638546 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 3,887,449 | 35,087.975758 | 52638546 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,397,317 | 2,809.917633 | 52638546 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,817,802 | 0.000012 | 52638546 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,534,116 | 105.397348 | 52638546 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,498,086 | 0.000010 | 52638546 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,469,320 | 1.141649 | 52638546 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,456,838 | 407.064502 | 52638546 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,312,227 | 1,061,524.978419 | 52638546 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 430 | 2,130,106 | 2,366.943900 | 52638546 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,476 | 1.194801 | 52638546 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 2,097,042 | 1,027.096910 | 52638546 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52638546 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,955,279 | 0.000000 | 52638546 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,913,143 | 0.022584 | 52638546 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,871,619 | 15.868825 | 52638546 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,782,864 | 0.916541 | 52638546 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,765,668 | 0.000012 | 52638546 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,760,729 | 0.018663 | 52638546 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,759,460 | 13,918.567579 | 52638546 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,675,418 | 2.302225 | 52638546 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,467,809 | 2,825.262922 | 52638546 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,461,923 | 1.105502 | 52638546 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,083 | 0.831340 | 52638546 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,334,061 | 0.000000 | 52638546 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,330,986 | 1.130672 | 52638546 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/AERO | 3032 | 1,312,384 | 2,824.266908 | 52638546 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,289,561 | 0.004737 | 52638546 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,275,022 | 0.000273 | 52638546 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,273,513 | 23.219772 | 52638546 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,246,875 | 1.120652 | 52638546 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,245,648 | 62.625657 | 52638546 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,196,257 | 2,362.153913 | 52638546 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,176,134 | 1.105590 | 52638546 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,171,004 | 35,588,809.396719 | 52638546 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,139,432 | 0.029217 | 52638546 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,133,260 | 1,180,454.433459 | 52638546 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,120,386 | 506,111.363810 | 52638546 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,119,207 | 77,663.362212 | 52638546 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,117,447 | 50.470654 | 52638546 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,106,520 | 14.495392 | 52638546 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 7329 ; routes examinées : 153308022 ; candidats optimisés : 967470 ; net attendu > 0 : 300 ; dernier cycle 633.0 ms
- Rejets (moteur) : {'spread_below_threshold': 151090609, 'liquidity_below_min': 1226319, 'negative_expected_net': 967170, 'unquotable': 15531, 'borrow_bound_too_small': 7329, 'cycle_budget_exhausted': 764}
- Enregistrements de la session : 967470 ; net attendu > 0 : 300 ; simulés (eth_call de la vraie tx) : 13 (ok 13, échec 0) ; étiquettes ghost N+1 : 3/10 positives
- Décisions : {'REJECTED': 967470} ; motifs de rejet : {'below_safety_margin': 254, 'negative_expected_net': 967170, 'p_lower_below_threshold': 110, 'reliability_not_demonstrated': 190, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52635174 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.011261 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0642 €) | 0.000029 WETH | 26.14 | 0.315 (n=3) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.010459 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0250 €) | 0.000011 WETH | 10.97 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 24.566653 USDC | 0.033911 USDC | 0.000000 USDC | 0.006805 USDC | 0.027106 USDC (0.0249 €) | — | 11.03 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[uniswap_v2]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.010315 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0223 €) | 0.000010 WETH | 9.91 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52635174 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 24.294626 USDC | 0.030208 USDC | 0.000000 USDC | 0.006068 USDC | 0.024140 USDC (0.0222 €) | — | 9.94 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.010622 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0221 €) | — | 9.52 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 25.012209 USDC | 0.030685 USDC | 0.000000 USDC | 0.006805 USDC | 0.023880 USDC (0.0220 €) | — | 9.55 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[aerodrome]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.010424 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0215 €) | — | 9.44 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 24.519547 USDC | 0.029720 USDC | 0.000000 USDC | 0.006477 USDC | 0.023243 USDC (0.0214 €) | — | 9.48 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.010490 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0212 €) | — | 9.26 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 24.545553 USDC | 0.029743 USDC | 0.000000 USDC | 0.006805 USDC | 0.022938 USDC (0.0211 €) | — | 9.35 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.010435 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0209 €) | — | 9.20 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[sushiswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.010166 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0209 €) | — | 9.41 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 24.465838 USDC | 0.029462 USDC | 0.000000 USDC | 0.006805 USDC | 0.022657 USDC (0.0208 €) | — | 9.26 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 23.844197 USDC | 0.029394 USDC | 0.000000 USDC | 0.006805 USDC | 0.022589 USDC (0.0208 €) | — | 9.47 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.010273 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0204 €) | — | 9.12 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 24.210623 USDC | 0.028928 USDC | 0.000000 USDC | 0.006805 USDC | 0.022123 USDC (0.0204 €) | — | 9.14 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[uniswap_v3]→AERO→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.006924 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0203 €) | — | 13.44 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.010237 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0201 €) | — | 9.00 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635174 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 24.178325 USDC | 0.028565 USDC | 0.000000 USDC | 0.006805 USDC | 0.021760 USDC (0.0200 €) | — | 9.00 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52635092 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.006427 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0123 €) | 0.000006 WETH | 8.76 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52635092 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 15.182028 USDC | 0.020454 USDC | 0.000000 USDC | 0.007129 USDC | 0.013325 USDC (0.0123 €) | — | 8.78 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52635092 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.006352 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0119 €) | 0.000005 WETH | 8.57 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52635092 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 15.038896 USDC | 0.020011 USDC | 0.000000 USDC | 0.007129 USDC | 0.012882 USDC (0.0119 €) | — | 8.57 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.007985 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0098 €) | — | 5.64 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 268 ; taux observé 0.194 ; borne inférieure crédible (0.9) 0.165 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
