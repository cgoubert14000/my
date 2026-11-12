# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T00:26:58+00:00 ; durée 42.77 min ; blocs 56251356 → 56264155 (2148 vus)

## Connexion
- Requêtes RPC : 29415 ; erreurs : 0 ; latence p50/p95 : 210.7/1,308.3 ms
- Rafraîchissements d'état : 2148 ; âge des données au dernier bloc : 10.51 s ; changements de frais LP observés (pools à frais dynamiques) : 1785
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3496 ; cycles déclenchés par événement : 1156 ; avance médiane sur le rafraîchissement multicall : 499 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,056.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 458 pools, 265 jetons, 15592 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 281, par paires 0), mesurés 460, sous le plancher de 10000.0 $ : 2 → gardés 458 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2049.11291, 'cbBTC': 73781.879924, 'AERO': 0.537258}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,540,514 | 2,056.759097 | 56264184 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,459,784 | 0.027839 | 56264184 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,634,111 | 0.027789 | 56264184 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,528,554 | 0.000014 | 56264184 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,104,667 | 2,061.818499 | 56264184 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,880,140 | 104.121747 | 56264184 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,593,980 | 0.027841 | 56264184 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,244,563 | 1.846522 | 56264184 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,023,567 | 2,062.109605 | 56264184 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,892,823 | 0.998581 | 56264184 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,035,200 | 42,973.758515 | 56264184 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 247 | 2,897,963 | 2,062.336939 | 56264184 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,208,204 | 0.027783 | 56264184 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,952,175 | 1,125,188.542308 | 56264184 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 1,649,935 | 0.000014 | 56264184 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,624,146 | 0.016418 | 56264184 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,608,657 | 0.000013 | 56264184 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,572,884 | 0.000000 | 56264184 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,543,115 | 0.006710 | 56264184 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,532,107 | 0.000014 | 56264184 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,921 | 0.830438 | 56264184 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,836 | 1.406597 | 56264184 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,410,697 | 427.574333 | 56264184 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,271,732 | 2,057.022513 | 56264184 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,260,476 | 3,802.260962 | 56264184 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,220,108 | 15,383.995636 | 56264184 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,157,678 | 2,056.281974 | 56264184 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,128,115 | 2,061.771019 | 56264184 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56264184 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,043,394 | 33,587,420.847465 | 56264184 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,025,553 | 104.619565 | 56264184 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 964,720 | 21.071180 | 56264184 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 937,585 | 566,570.738843 | 56264184 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 915,816 | 0.001480 | 56264184 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 903,933 | 0.000014 | 56264184 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 901,847 | 0.050554 | 56264184 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 897,628 | 23,358,136.408828 | 56264184 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 879,142 | 2,054.856011 | 56264184 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 876,626 | 1,029.586062 | 56264184 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 859,338 | 0.000000 | 56264184 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 782,470 | 76.823928 | 56264184 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 761,547 | 0.051732 | 56264184 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4530 | 749,052 | 22.950471 | 56264184 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 745,360 | 116,086.409769 | 56264184 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 706,863 | 3,786.866427 | 56264184 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 696,832 | 0.801801 | 56264184 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 667,873 | 0.529800 | 56264184 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 649,390 | 4,756,067.281123 | 56264184 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 616,777 | 0.478805 | 56264184 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 602,244 | 147,804.599882 | 56264184 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 586,643 | 0.000007 | 56264184 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 576,695 | 0.000257 | 56264184 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 574,301 | 562,163.639062 | 56264184 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 559,749 | 0.037710 | 56264184 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 489,326 | 1,029.564825 | 56264184 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 463,379 | 0.066689 | 56264184 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 11 | 453,798 | 1.000923 | 56264184 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,675 | 0.502364 | 56264184 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 441,206 | 24.808159 | 56264184 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 439,622 | 904,519.367544 | 56264184 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 3303 ; routes examinées : 51500376 ; candidats optimisés : 260642 ; net attendu > 0 : 150 ; dernier cycle 583.9 ms
- Rejets (moteur) : {'spread_below_threshold': 50358226, 'liquidity_below_min': 877756, 'negative_expected_net': 260492, 'borrow_bound_too_small': 3291, 'cycle_budget_exhausted': 461}
- Enregistrements de la session : 260642 ; net attendu > 0 : 150 ; simulés (eth_call de la vraie tx) : 2 (ok 1, échec 1) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 260642} ; motifs de rejet : {'below_safety_margin': 148, 'negative_expected_net': 260492, 'p_lower_below_threshold': 140, 'reliability_not_demonstrated': 10, 'simulation_failed': 1, 'stale_data': 41}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56252219 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 310.545098 USDC | 0.024609 USDC | 0.000000 USDC | 0.004606 USDC | 0.020003 USDC (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(20003<62109), p_lower_below_threshold(0.10<0.75) |
| 56252220 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 310.545098 USDC | 0.024609 USDC | 0.000000 USDC | 0.004606 USDC | 0.020003 USDC (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(20003<62109), p_lower_below_threshold(0.10<0.75) |
| 56252219 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.151840 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(9758427752881<30368070316317), p_lower_below_threshold(0.10<0.75) |
| 56252220 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.151840 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(9758427752881<30368070316317), p_lower_below_threshold(0.10<0.75) |
| 56258818 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→WETH | 0.028626 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0137 €) | — | 2.53 | 0.103 (n=364) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 56263512 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 92.963658 USDC | 0.014055 USDC | 0.000000 USDC | 0.006177 USDC | 0.007878 USDC (0.0072 €) | — | 0.85 | 0.344 (n=610) | REJECTED | below_safety_margin(7878<18592), p_lower_below_threshold(0.34<0.75) |
| 56263512 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 92.963658 USDC | 0.014055 USDC | 0.000000 USDC | 0.006177 USDC | 0.007878 USDC (0.0072 €) | — | 0.85 | 0.344 (n=610) | REJECTED | below_safety_margin(7878<18592), stale_data(4617ms>4000.0), p_lower_below_threshold(0.34<0.75) |
| 56263512 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.045439 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0072 €) | — | 0.84 | 0.344 (n=610) | REJECTED | below_safety_margin(3816240924519<9087776409896), p_lower_below_threshold(0.34<0.75) |
| 56263512 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.045439 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0072 €) | — | 0.84 | 0.344 (n=610) | REJECTED | below_safety_margin(3816240924519<9087776409896), stale_data(4611ms>4000.0), p_lower_below_threshold(0.34<0.75) |
| 56252219 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 143.484105 USDC | 0.012065 USDC | 0.000000 USDC | 0.004917 USDC | 0.007148 USDC (0.0066 €) | — | 0.50 | 0.087 (n=116) | REJECTED | below_safety_margin(7148<28696), p_lower_below_threshold(0.09<0.75) |
| 56252220 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 143.484105 USDC | 0.012065 USDC | 0.000000 USDC | 0.004917 USDC | 0.007148 USDC (0.0066 €) | — | 0.50 | 0.087 (n=116) | REJECTED | below_safety_margin(7148<28696), p_lower_below_threshold(0.09<0.75) |
| 56252219 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.070478 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0066 €) | — | 0.49 | 0.087 (n=116) | REJECTED | below_safety_margin(3486419375392<14095681478295), p_lower_below_threshold(0.09<0.75) |
| 56252220 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.070478 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0066 €) | — | 0.49 | 0.087 (n=116) | REJECTED | below_safety_margin(3486419375392<14095681478295), p_lower_below_threshold(0.09<0.75) |
| 56263512 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 88.453922 USDC | 0.012725 USDC | 0.000000 USDC | 0.006488 USDC | 0.006237 USDC (0.0057 €) | — | 0.71 | 0.267 (n=1584) | REJECTED | below_safety_margin(6237<17690), p_lower_below_threshold(0.27<0.75) |
| 56263512 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 88.453922 USDC | 0.012725 USDC | 0.000000 USDC | 0.006488 USDC | 0.006237 USDC (0.0057 €) | — | 0.71 | 0.267 (n=1584) | REJECTED | below_safety_margin(6237<17690), stale_data(4657ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56263512 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.042626 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0057 €) | — | 0.71 | 0.267 (n=1584) | REJECTED | below_safety_margin(3018083671569<8525108947529), p_lower_below_threshold(0.27<0.75) |
| 56263512 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.042626 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0057 €) | — | 0.71 | 0.267 (n=1584) | REJECTED | below_safety_margin(3018083671569<8525108947529), stale_data(4651ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56263512 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.034300 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0051 €) | — | 0.79 | 0.267 (n=1584) | REJECTED | below_safety_margin(2714357232445<6859945367304), p_lower_below_threshold(0.27<0.75) |
| 56263512 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.034300 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0051 €) | — | 0.79 | 0.267 (n=1584) | REJECTED | below_safety_margin(2714357232445<6859945367304), stale_data(4561ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56263512 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 44.443974 USDC | 0.011478 USDC | 0.000000 USDC | 0.006177 USDC | 0.005301 USDC (0.0049 €) | — | 1.19 | 0.344 (n=610) | REJECTED | below_safety_margin(5301<8888), p_lower_below_threshold(0.34<0.75) |
| 56263512 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 44.443974 USDC | 0.011478 USDC | 0.000000 USDC | 0.006177 USDC | 0.005301 USDC (0.0049 €) | — | 1.19 | 0.344 (n=610) | REJECTED | below_safety_margin(5301<8888), stale_data(4361ms>4000.0), p_lower_below_threshold(0.34<0.75) |
| 56263512 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.021576 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0048 €) | — | 1.19 | 0.344 (n=610) | REJECTED | below_safety_margin(2564535373720<4315163862633), p_lower_below_threshold(0.34<0.75) |
| 56263512 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.021576 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0048 €) | — | 1.19 | 0.344 (n=610) | REJECTED | below_safety_margin(2564535373720<4315163862633), stale_data(4367ms>4000.0), p_lower_below_threshold(0.34<0.75) |
| 56263512 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000792 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0048 €) | — | 0.88 | 0.267 (n=1584) | REJECTED | below_safety_margin(7<15), p_lower_below_threshold(0.27<0.75) |
| 56263512 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000792 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0048 €) | — | 0.88 | 0.267 (n=1584) | REJECTED | below_safety_margin(7<15), stale_data(4554ms>4000.0), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8236 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
