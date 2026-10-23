# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T08:33:08+00:00 ; durée 70.53 min ; blocs 52975401 → 52977519 (2114 vus)

## Connexion
- Requêtes RPC : 23560 ; erreurs : 0 ; latence p50/p95 : 226.2/1,221.6 ms
- Rafraîchissements d'état : 2115 ; âge des données au dernier bloc : 1.9 s ; changements de frais LP observés (pools à frais dynamiques) : 2537
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 66 ; cycles déclenchés par événement : 17 ; avance médiane sur le rafraîchissement multicall : 442 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,403.58 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19290 routes
- Par DEX : uniswap_v3 137, aerodrome 221, aerodrome_slipstream 136, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 199 (rejetés 2) → 604 jetons ; pools candidats 3831 (énumérés 359, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2402.292282, 'AERO': 0.794098, 'cbBTC': 81667.512713}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,765,916 | 2,403.578227 | 52977519 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,441,442 | 0.029453 | 52977519 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,419,312 | 91.924996 | 52977519 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 11,624,357 | 1.259791 | 52977519 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,313,104 | 0.029405 | 52977519 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,861,023 | 0.000012 | 52977519 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,945,742 | 0.029402 | 52977519 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,695,502 | 2,406.386939 | 52977519 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,171,407 | 0.001672 | 52977519 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,353,248 | 0.000012 | 52977519 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,627,571 | 2,406.744120 | 52977519 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,446,181 | 0.029453 | 52977519 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 5,259,974 | 0.000012 | 52977519 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,575,194 | 2,406.432766 | 52977519 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,294,836 | 0.999609 | 52977519 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,291,195 | 2,405.153726 | 52977519 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 4,004,136 | 34,148.615599 | 52977519 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,410,143 | 0.000274 | 52977519 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 409 | 2,906,107 | 2,410.335478 | 52977519 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,565,189 | 91.908000 | 52977519 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,318,530 | 390.741078 | 52977519 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,232,662 | 1,175,004.675833 | 52977519 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,156,764 | 3,025.077109 | 52977519 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,003,099 | 0.000000 | 52977519 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,923,814 | 0.000012 | 52977519 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,774,141 | 0.018048 | 52977519 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,760,380 | 0.000012 | 52977519 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,634,634 | 1.527886 | 52977519 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,618,142 | 3,028.748461 | 52977519 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,772 | 0.823512 | 52977519 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,422,255 | 13,272.866322 | 52977519 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,356,900 | 0.004929 | 52977519 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,301,114 | 2.318302 | 52977519 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,298,520 | 0.000276 | 52977519 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,286,697 | 2,406.390833 | 52977519 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,269,099 | 0.000000 | 52977519 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,408 | 64.291011 | 52977519 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,189,660 | 36,006,236.921269 | 52977519 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,179,498 | 16.102505 | 52977519 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,169,697 | 1,113,351.136600 | 52977519 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,160,360 | 46.531887 | 52977519 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,154,206 | 496,846.403137 | 52977519 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 1,089,511 | 0.038162 | 52977519 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 1,088,006 | 75,183.645772 | 52977519 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | weETH_04c0/WETH | 500 | 1,075,253 | 1.105789 | 52977519 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,066,542 | 21,313,449.073659 | 52977519 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,052,137 | 16.462365 | 52977519 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,032,985 | 0.000010 | 52977519 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,015,547 | 23.055597 | 52977519 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 962,743 | 1,051.225232 | 52977519 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 949,478 | 2,390.321401 | 52977519 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 919,065 | 0.000548 | 52977519 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 885,651 | 17.704089 | 52977519 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 866,691 | 2,403.572522 | 52977519 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 814,244 | 0.803225 | 52977519 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 789,906 | 0.663572 | 52977519 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| pancakeswap_v3 | QUID/USDC | 100 | 788,383 | 0.055698 | 52977519 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | fBOMB/USDC | 10000 | 773,700 | 0.018516 | 52977519 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 773,091 | 4,560,756.401536 | 52977519 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 738,783 | 133,112.644629 | 52977519 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |

## Recherche d'opportunités
- Cycles : 2131 ; routes examinées : 41106990 ; candidats optimisés : 241192 ; net attendu > 0 : 31 ; dernier cycle 262.2 ms
- Rejets (moteur) : {'spread_below_threshold': 40566305, 'liquidity_below_min': 297299, 'negative_expected_net': 241161, 'borrow_bound_too_small': 2131, 'cycle_budget_exhausted': 63}
- Enregistrements de la session : 241192 ; net attendu > 0 : 31 ; simulés (eth_call de la vraie tx) : 5 (ok 5, échec 0) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 241192} ; motifs de rejet : {'below_safety_margin': 12, 'negative_expected_net': 241161, 'p_lower_below_threshold': 24, 'reliability_not_demonstrated': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52975572 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.029140 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0701 €) | 0.000032 WETH | 10.89 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[uniswap_v3]→USDC | 69.929959 USDC | 0.083061 USDC | 0.000000 USDC | 0.006893 USDC | 0.076168 USDC (0.0701 €) | — | 10.89 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.028214 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0640 €) | 0.000029 WETH | 10.27 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 67.426150 USDC | 0.076476 USDC | 0.000000 USDC | 0.006893 USDC | 0.069583 USDC (0.0640 €) | — | 10.32 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.027874 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0625 €) | 0.000028 WETH | 10.15 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 66.755766 USDC | 0.074809 USDC | 0.000000 USDC | 0.006893 USDC | 0.067916 USDC (0.0625 €) | — | 10.17 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 52975572 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.022727 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0454 €) | — | 9.04 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[sushiswap_v3]→USDC | 54.395945 USDC | 0.056563 USDC | 0.000000 USDC | 0.007258 USDC | 0.049305 USDC (0.0454 €) | — | 9.06 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.024158 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0453 €) | — | 8.48 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 57.724561 USDC | 0.056052 USDC | 0.000000 USDC | 0.006893 USDC | 0.049159 USDC (0.0452 €) | — | 8.52 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 52975572 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.022972 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0401 €) | — | 7.89 | 0.032 (n=135) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[uniswap_v3]→USDC | 54.819032 USDC | 0.050399 USDC | 0.000000 USDC | 0.006893 USDC | 0.043506 USDC (0.0400 €) | — | 7.94 | 0.032 (n=135) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52975572 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.016322 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0366 €) | — | 10.15 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 39.043187 USDC | 0.046973 USDC | 0.000000 USDC | 0.007258 USDC | 0.039715 USDC (0.0365 €) | — | 10.17 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | WETH→[uniswap_v3]→USDbC→[aerodrome]→WETH | 0.011585 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0153 €) | — | 5.99 | 0.086 (n=25) | REJECTED | reliability_not_demonstrated |
| 52977122 | WETH→[aerodrome_slipstream]→BID→[aerodrome]→WETH | 0.004528 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0046 €) | 0.000002 WETH | 4.63 | 0.086 (n=25) | REJECTED | reliability_not_demonstrated |
| 52975572 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.003183 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 2.93 | 0.120 (n=91) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[aerodrome]→USDC | 7.636700 USDC | 0.008781 USDC | 0.000000 USDC | 0.006562 USDC | 0.002219 USDC (0.0020 €) | — | 2.91 | 0.120 (n=91) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52977107 | WETH→[aerodrome_slipstream]→BID→[aerodrome]→WETH | 0.003842 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0020 €) | 0.000001 WETH | 2.39 | 0.151 (n=10) | REJECTED | reliability_not_demonstrated |
| 52975667 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.110321 USDC | 0.009207 USDC | 0.000000 USDC | 0.007223 USDC | 0.001984 USDC (0.0018 €) | — | 1.96 | 0.116 (n=238) | REJECTED | below_safety_margin(1984<2022), p_lower_below_threshold(0.12<0.75) |
| 52975667 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004246 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 1.94 | 0.116 (n=238) | REJECTED | below_safety_margin(824547019587<849211132160), p_lower_below_threshold(0.12<0.75) |
| 52975665 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.711333 USDC | 0.008570 USDC | 0.000000 USDC | 0.007223 USDC | 0.001347 USDC (0.0012 €) | — | 1.39 | 0.238 (n=118) | REJECTED | below_safety_margin(1347<1942), p_lower_below_threshold(0.24<0.75) |
| 52975666 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.711333 USDC | 0.008570 USDC | 0.000000 USDC | 0.007223 USDC | 0.001347 USDC (0.0012 €) | — | 1.39 | 0.238 (n=118) | REJECTED | below_safety_margin(1347<1942), p_lower_below_threshold(0.24<0.75) |
| 52975667 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.711333 USDC | 0.008570 USDC | 0.000000 USDC | 0.007223 USDC | 0.001347 USDC (0.0012 €) | — | 1.39 | 0.238 (n=118) | REJECTED | below_safety_margin(1347<1942), p_lower_below_threshold(0.24<0.75) |
| 52975665 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004070 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.38 | 0.238 (n=118) | REJECTED | below_safety_margin(559739321322<814028048062), p_lower_below_threshold(0.24<0.75) |

## Fiabilité et décision
- Observations ghost : 1984 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
