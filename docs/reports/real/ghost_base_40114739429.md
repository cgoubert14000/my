# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T17:16:56+00:00 ; durée 3.02 min ; blocs 53036340 → 53036433 (91 vus)

## Connexion
- Requêtes RPC : 1217 ; erreurs : 0 ; latence p50/p95 : 243.8/1,169.5 ms
- Rafraîchissements d'état : 91 ; âge des données au dernier bloc : 2.95 s ; changements de frais LP observés (pools à frais dynamiques) : 140
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1215 ; cycles déclenchés par événement : 154 ; avance médiane sur le rafraîchissement multicall : 554 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,311.37 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 306 jetons, 19348 routes
- Par DEX : uniswap_v3 139, aerodrome 216, aerodrome_slipstream 130, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3808 (énumérés 345, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 2 → gardés 530 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2311.365621, 'cbBTC': 80049.166907, 'AERO': 0.688082}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 152,840,418 | 2,311.365628 | 53036433 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,066,403 | 0.028920 | 53036433 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 11,945,081 | 97.259334 | 53036433 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,070,008 | 0.028893 | 53036433 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,488,971 | 0.000012 | 53036433 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,711,876 | 1.453316 | 53036433 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,365,955 | 2,315.575973 | 53036433 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 7,591,801 | 0.028886 | 53036433 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,948,876 | 0.001637 | 53036433 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 6,279,351 | 0.000012 | 53036433 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,385,446 | 2,315.599741 | 53036433 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,352,365 | 0.028932 | 53036433 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 4,493,770 | 0.000012 | 53036433 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,425,334 | 2,315.862380 | 53036434 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,205,474 | 0.999835 | 53036433 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,827,859 | 34,525.415598 | 53036433 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,776,109 | 2,309.130119 | 53036433 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 406 | 2,740,399 | 2,324.635009 | 53036433 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,456,494 | 97.250824 | 53036433 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,191,041 | 410.327958 | 53036433 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,087,403 | 1,243,064.919347 | 53036433 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,894,921 | 0.000013 | 53036433 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/AERO | 10000 | 1,881,276 | 3,341.127574 | 53036433 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,879,164 | 0.000000 | 53036433 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,782,528 | 0.017921 | 53036433 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,729,432 | 0.000012 | 53036433 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,560,896 | 0.000264 | 53036433 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,509,869 | 1.653132 | 53036433 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,852 | 0.826899 | 53036433 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,433,172 | 3,358.738746 | 53036433 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,385,614 | 0.005325 | 53036433 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,358,680 | 14,206.291356 | 53036433 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,227,828 | 2,315.680918 | 53036433 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,226,593 | 0.000266 | 53036433 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,224,787 | 64.777090 | 53036433 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/msETH (stable) | 500 | 1,204,622 | 2.306063 | 53036433 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,153,359 | 0.000000 | 53036433 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,145,771 | 35,511,971.060590 | 53036433 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,121,665 | 49.784062 | 53036433 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 1,118,140 | 1,122,207.256227 | 53036433 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,100,663 | 501,073.386748 | 53036433 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,033,245 | 76,707.788125 | 53036433 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,020,291 | 17.899066 | 53036433 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,011,876 | 21,823,007.868303 | 53036433 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 942,669 | 17.067591 | 53036433 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 940,376 | 23.203055 | 53036433 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 939,876 | 0.042094 | 53036433 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 921,046 | 1,089.174795 | 53036433 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 883,669 | 0.000548 | 53036433 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 878,722 | 17.965017 | 53036433 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 856,468 | 97.275921 | 53036433 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 843,081 | 2,310.782516 | 53036433 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 828,601 | 0.061888 | 53036433 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 815,900 | 0.000009 | 53036433 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 790,936 | 1.105883 | 53036433 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 782,610 | 0.803098 | 53036433 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 779,867 | 2,304.780586 | 53036433 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,569 | 0.615522 | 53036433 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 736,878 | 4,643,458.546654 | 53036433 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 731,174 | 0.669797 | 53036433 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 244 ; routes examinées : 4720912 ; candidats optimisés : 19991 ; net attendu > 0 : 20 ; dernier cycle 117.1 ms
- Rejets (moteur) : {'spread_below_threshold': 4638581, 'liquidity_below_min': 61531, 'negative_expected_net': 19971, 'unquotable': 486, 'borrow_bound_too_small': 243}
- Enregistrements de la session : 19988 ; net attendu > 0 : 20 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 19988} ; motifs de rejet : {'below_safety_margin': 20, 'negative_expected_net': 19968, 'p_lower_below_threshold': 14, 'reliability_not_demonstrated': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53036409 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 128.847810 USDC | 0.009566 USDC | 0.000000 USDC | 0.005900 USDC | 0.003666 USDC (0.0034 €) | — | 0.28 | 0.017 (n=84) | REJECTED | below_safety_margin(3666<25769), p_lower_below_threshold(0.02<0.75) |
| 53036409 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.055731 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0034 €) | — | 0.28 | 0.017 (n=84) | REJECTED | below_safety_margin(1578166331557<11146113775505), p_lower_below_threshold(0.02<0.75) |
| 53036429 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003318 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0029 €) | — | 0.12 | 0.141 (n=287) | REJECTED | below_safety_margin(4<66), p_lower_below_threshold(0.14<0.75) |
| 53036429 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003318 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0029 €) | — | 0.12 | 0.141 (n=287) | REJECTED | below_safety_margin(4<66), p_lower_below_threshold(0.14<0.75) |
| 53036429 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.131809 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0027 €) | — | 0.10 | 0.141 (n=287) | REJECTED | below_safety_margin(1278851017125<26361792562592), p_lower_below_threshold(0.14<0.75) |
| 53036429 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.131809 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0027 €) | — | 0.10 | 0.141 (n=287) | REJECTED | below_safety_margin(1278851017125<26361792562592), p_lower_below_threshold(0.14<0.75) |
| 53036429 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 350.391803 USDC | 0.010066 USDC | 0.000000 USDC | 0.007305 USDC | 0.002761 USDC (0.0025 €) | — | 0.08 | 0.141 (n=287) | REJECTED | below_safety_margin(2761<70078), p_lower_below_threshold(0.14<0.75) |
| 53036429 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 350.391803 USDC | 0.010066 USDC | 0.000000 USDC | 0.007305 USDC | 0.002761 USDC (0.0025 €) | — | 0.08 | 0.141 (n=287) | REJECTED | below_safety_margin(2761<70078), p_lower_below_threshold(0.14<0.75) |
| 53036429 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.102825 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 0.08 | 0.001 (n=7) | REJECTED | below_safety_margin(864846979120<20565053369324), reliability_not_demonstrated |
| 53036429 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.102825 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 0.08 | 0.001 (n=7) | REJECTED | below_safety_margin(864846979120<20565053369324), reliability_not_demonstrated |
| 53036429 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 287.060681 USDC | 0.009278 USDC | 0.000000 USDC | 0.007305 USDC | 0.001973 USDC (0.0018 €) | — | 0.07 | 0.001 (n=7) | REJECTED | below_safety_margin(1973<57412), reliability_not_demonstrated |
| 53036429 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 287.060681 USDC | 0.009278 USDC | 0.000000 USDC | 0.007305 USDC | 0.001973 USDC (0.0018 €) | — | 0.07 | 0.001 (n=7) | REJECTED | below_safety_margin(1973<57412), reliability_not_demonstrated |
| 53036429 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002642 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0015 €) | — | 0.08 | 0.001 (n=7) | REJECTED | below_safety_margin(2<52), reliability_not_demonstrated |
| 53036429 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002642 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0015 €) | — | 0.08 | 0.001 (n=7) | REJECTED | below_safety_margin(2<52), reliability_not_demonstrated |
| 53036382 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.001121 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.09 | 0.017 (n=84) | REJECTED | below_safety_margin(1<22), p_lower_below_threshold(0.02<0.75) |
| 53036383 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.001121 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.09 | 0.017 (n=84) | REJECTED | below_safety_margin(1<22), p_lower_below_threshold(0.02<0.75) |
| 53036382 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.038652 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0006 €) | — | 0.08 | 0.017 (n=84) | REJECTED | below_safety_margin(297592250342<7730340463961), p_lower_below_threshold(0.02<0.75) |
| 53036383 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.038652 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0006 €) | — | 0.08 | 0.017 (n=84) | REJECTED | below_safety_margin(297592250342<7730340463961), p_lower_below_threshold(0.02<0.75) |
| 53036385 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 93.664094 USDC | 0.007183 USDC | 0.000000 USDC | 0.006957 USDC | 0.000226 USDC (0.0002 €) | — | 0.02 | 0.141 (n=287) | REJECTED | below_safety_margin(226<18732), p_lower_below_threshold(0.14<0.75) |
| 53036385 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.039639 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.02 | 0.141 (n=287) | REJECTED | below_safety_margin(76167444960<7927891206701), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 2255 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
