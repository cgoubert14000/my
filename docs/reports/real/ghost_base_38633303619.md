# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T21:34:30+00:00 ; durée 55.15 min ; blocs 52610504 → 52612160 (1616 vus)

## Connexion
- Requêtes RPC : 18459 ; erreurs : 0 ; latence p50/p95 : 79.4/1,826.0 ms
- Rafraîchissements d'état : 1617 ; âge des données au dernier bloc : 1.79 s ; changements de frais LP observés (pools à frais dynamiques) : 2899
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1 ; cycles déclenchés par événement : 1 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,420.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 327 jetons, 21784 routes
- Par DEX : uniswap_v3 139, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 33, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3920 (énumérés 394, par paires 0), mesurés 583, sous le plancher de 10000.0 $ : 3 → gardés 580 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2422.373052, 'AERO': 0.888199, 'cbBTC': 81793.071591}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,035,485 | 2,420.113659 | 52612160 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,148,849 | 1.122345 | 52612160 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,812,075 | 0.029637 | 52612160 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,126,790 | 103.551310 | 52612160 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2555 | 13,743,830 | 0.029578 | 52612160 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,430,265 | 0.029564 | 52612160 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,219,852 | 0.000012 | 52612160 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,189,147 | 2,426.085420 | 52612160 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,951,621 | 2,420.186211 | 52612160 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 8,156,677 | 0.000012 | 52612160 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 788 | 7,683,450 | 2,425.820244 | 52612160 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,171,638 | 0.001670 | 52612160 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 6,590,420 | 0.000012 | 52612160 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,393,110 | 0.029637 | 52612160 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,345,287 | 1.000855 | 52612160 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,344,836 | 0.026706 | 52612160 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,605,664 | 0.000279 | 52612160 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,551,634 | 0.802388 | 52612160 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,385,595 | 2,425.623828 | 52612160 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,108,740 | 1.000134 | 52612160 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,993,475 | 34,833.175576 | 52612160 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,634,812 | 2,738.445137 | 52612160 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,591,236 | 1.130595 | 52612160 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,839,029 | 0.000012 | 52612160 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,680,003 | 0.000011 | 52612160 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,610,342 | 103.512911 | 52612160 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,576,218 | 1.141642 | 52612160 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,446,676 | 403.903992 | 52612160 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,359,188 | 1,068,249.628419 | 52612160 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 460 | 2,325,959 | 2,429.821597 | 52612160 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,286,329 | 1,026.320283 | 52612160 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,113,918 | 1.193280 | 52612160 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,064,225 | 0.000000 | 52612160 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 1,926,384 | 0.023410 | 52612160 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,895,784 | 0.916706 | 52612160 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,854,353 | 15.718794 | 52612160 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,836,402 | 1.402356 | 52612160 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,789,224 | 0.019099 | 52612160 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,290 | 0.000012 | 52612160 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,718,650 | 13,620.694076 | 52612160 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,623,806 | 2.304462 | 52612160 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,524,017 | 2,719.526721 | 52612160 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,496,278 | 1.105776 | 52612160 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,484 | 0.835124 | 52612160 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,376,563 | 0.000000 | 52612160 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,362,314 | 2,719.113949 | 52612160 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,355,581 | 0.004892 | 52612160 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,328,229 | 1.115073 | 52612160 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,317,312 | 0.000280 | 52612160 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,293,431 | 1.131106 | 52612160 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,279,804 | 23.295890 | 52612160 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,246,980 | 62.491890 | 52612160 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,244,703 | 2,426.404078 | 52612160 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,223,160 | 33,453,518.990405 | 52612160 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,207,126 | 1.105594 | 52612160 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,179,589 | 72,823.120493 | 52612160 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,161,683 | 488,691.317475 | 52612160 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,153,343 | 1,193,984.411649 | 52612160 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,137,442 | 48.709522 | 52612160 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,135,649 | 13.582642 | 52612160 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 1617 ; routes examinées : 35224728 ; candidats optimisés : 196801 ; net attendu > 0 : 201 ; dernier cycle 226.9 ms
- Rejets (moteur) : {'spread_below_threshold': 34607572, 'liquidity_below_min': 376132, 'negative_expected_net': 196600, 'borrow_bound_too_small': 40425, 'unquotable': 3234, 'cycle_budget_exhausted': 564}
- Enregistrements de la session : 196801 ; net attendu > 0 : 201 ; simulés (eth_call de la vraie tx) : 15 (ok 15, échec 0) ; étiquettes ghost N+1 : 3/12 positives
- Décisions : {'REJECTED': 196801} ; motifs de rejet : {'below_safety_margin': 68, 'negative_expected_net': 196600, 'reliability_not_demonstrated': 201, 'stale_data': 145}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52610694 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.207976 WETH | 0.000122 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2638 €) | 0.000118 WETH | 5.70 | 0.141 (n=26) | REJECTED | stale_data(4588ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006085 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2638 €) | — | 5.75 | 0.141 (n=26) | REJECTED | stale_data(4604ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 508.108618 USDC | 0.293288 USDC | 0.000000 USDC | 0.007687 USDC | 0.285601 USDC (0.2628 €) | — | 5.62 | 0.141 (n=26) | REJECTED | stale_data(4596ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.184295 WETH | 0.000095 WETH | 0.000000 WETH | 0.000002 WETH | 0.000092 WETH (0.2055 €) | 0.000092 WETH | 5.01 | 0.002 (n=3) | REJECTED | stale_data(4718ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.005276 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2050 €) | — | 5.16 | 0.002 (n=3) | REJECTED | stale_data(4723ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.178692 WETH | 0.000089 WETH | 0.000000 WETH | 0.000003 WETH | 0.000086 WETH (0.1920 €) | 0.000086 WETH | 4.83 | 0.439 (n=13) | REJECTED | stale_data(4730ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 444.021441 USDC | 0.216079 USDC | 0.000000 USDC | 0.007687 USDC | 0.208392 USDC (0.1917 €) | — | 4.69 | 0.439 (n=13) | REJECTED | stale_data(4738ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.005024 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1914 €) | — | 5.06 | 0.439 (n=13) | REJECTED | stale_data(4745ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.172133 WETH | 0.000074 WETH | 0.000000 WETH | 0.000002 WETH | 0.000072 WETH (0.1603 €) | — | 4.18 | 0.264 (n=6) | REJECTED | stale_data(4814ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.004772 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1598 €) | — | 4.44 | 0.264 (n=6) | REJECTED | stale_data(4819ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.128075 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1366 €) | — | 4.79 | 0.439 (n=13) | REJECTED | stale_data(4674ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC | 0.003507 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1364 €) | — | 5.16 | 0.439 (n=13) | REJECTED | stale_data(4681ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[aerodrome_slipstream]→tBTC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.122579 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1360 €) | — | 4.98 | 0.439 (n=13) | REJECTED | stale_data(4688ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→tBTC→[uniswap_v3]→cbBTC | 0.003399 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1357 €) | — | 5.30 | 0.439 (n=13) | REJECTED | stale_data(4695ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC | 0.003491 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1341 €) | — | 5.10 | 0.141 (n=26) | REJECTED | stale_data(4712ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.119080 WETH | 0.000063 WETH | 0.000000 WETH | 0.000003 WETH | 0.000060 WETH (0.1341 €) | — | 5.06 | 0.141 (n=26) | REJECTED | stale_data(4706ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.140146 WETH | 0.000060 WETH | 0.000000 WETH | 0.000003 WETH | 0.000057 WETH (0.1266 €) | — | 4.06 | 0.141 (n=26) | REJECTED | stale_data(4827ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003764 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1266 €) | — | 4.46 | 0.141 (n=26) | REJECTED | stale_data(4842ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 317.781783 USDC | 0.144866 USDC | 0.000000 USDC | 0.007687 USDC | 0.137179 USDC (0.1262 €) | — | 4.32 | 0.141 (n=26) | REJECTED | stale_data(4834ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[aerodrome_slipstream]→ZORA→[uniswap_v3]→USDC | 147.954389 USDC | 0.140518 USDC | 0.000000 USDC | 0.005840 USDC | 0.134678 USDC (0.1239 €) | — | 9.10 | 0.006 (n=1) | REJECTED | stale_data(4433ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003408 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0852 €) | — | 3.32 | 0.141 (n=26) | REJECTED | stale_data(5009ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.120186 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0850 €) | — | 3.18 | 0.141 (n=26) | REJECTED | stale_data(4991ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 280.870647 USDC | 0.100121 USDC | 0.000000 USDC | 0.008055 USDC | 0.092066 USDC (0.0847 €) | — | 3.28 | 0.141 (n=26) | REJECTED | stale_data(5000ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 261.831522 USDC | 0.095056 USDC | 0.000000 USDC | 0.007687 USDC | 0.087369 USDC (0.0804 €) | — | 3.34 | 0.439 (n=13) | REJECTED | stale_data(4974ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.110496 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0803 €) | — | 3.26 | 0.439 (n=13) | REJECTED | stale_data(4967ms>4000.0), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 193 ; taux observé 0.166 ; borne inférieure crédible (0.9) 0.134 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 13.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
