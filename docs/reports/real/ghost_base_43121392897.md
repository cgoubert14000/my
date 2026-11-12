# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T02:15:05+00:00 ; durée 150.89 min ; blocs 56251356 → 56296607 (4152 vus)

## Connexion
- Requêtes RPC : 91371 ; erreurs : 70 ; latence p50/p95 : 277.3/1,299.5 ms
- Rafraîchissements d'état : 4152 ; âge des données au dernier bloc : 5.39 s ; changements de frais LP observés (pools à frais dynamiques) : 5143
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4545 ; cycles déclenchés par événement : 1575 ; avance médiane sur le rafraîchissement multicall : 523 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,051.90 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 458 pools, 265 jetons, 15592 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 281, par paires 0), mesurés 460, sous le plancher de 10000.0 $ : 2 → gardés 458 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2049.11291, 'cbBTC': 73781.879924, 'AERO': 0.537258}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,186,943 | 2,051.901545 | 56296630 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,421,072 | 0.027869 | 56296630 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,703,051 | 0.027797 | 56296630 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,504,843 | 0.000014 | 56296630 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,098,349 | 2,056.495030 | 56296630 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,881,177 | 103.599267 | 56296630 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,582,235 | 0.027877 | 56296630 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,242,672 | 1.847993 | 56296630 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,017,387 | 2,055.779654 | 56296630 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,879,511 | 0.998581 | 56296630 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,057,078 | 42,161.015722 | 56296630 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 131 | 2,892,096 | 2,055.930108 | 56296630 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,202,678 | 0.027814 | 56296630 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,947,565 | 1,125,188.542308 | 56296630 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,645,475 | 0.000014 | 56296630 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,626,977 | 0.016460 | 56296630 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,590,057 | 0.000014 | 56296630 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,568,890 | 0.000000 | 56296630 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,528,761 | 0.000014 | 56296630 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,525,355 | 0.006635 | 56296630 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,989 | 0.830405 | 56296630 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,871 | 1.406539 | 56296630 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,407,235 | 427.728432 | 56296630 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,270,238 | 2,051.627980 | 56296630 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,258,752 | 3,792.865964 | 56296630 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,216,314 | 15,366.957521 | 56296630 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,155,933 | 2,053.138489 | 56296630 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,126,367 | 2,056.496373 | 56296630 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,558 | 86.391364 | 56296630 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,040,685 | 33,610,271.580078 | 56296630 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,021,564 | 104.321547 | 56296630 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 962,867 | 21.195111 | 56296630 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 935,749 | 565,901.396155 | 56296630 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 913,219 | 0.001482 | 56296630 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | USDC/VVV | 3000 | 904,514 | 0.050343 | 56296630 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 901,015 | 0.000014 | 56296630 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 896,271 | 23,323,045.662687 | 56296630 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 877,948 | 2,054.853960 | 56296630 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 875,436 | 1,027.901615 | 56296630 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 858,448 | 0.000000 | 56296630 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 784,750 | 76.378220 | 56296630 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 749,111 | 0.049948 | 56296630 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 745,458 | 23.103570 | 56296630 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 741,884 | 116,623.726011 | 56296630 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 705,747 | 3,786.866427 | 56296630 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 695,187 | 0.801801 | 56296630 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 666,654 | 0.527629 | 56296630 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 646,421 | 4,777,351.006875 | 56296630 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 616,834 | 0.478875 | 56296630 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 593,831 | 151,338.276090 | 56296630 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 585,651 | 0.000007 | 56296630 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 575,333 | 0.000257 | 56296630 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 573,300 | 563,703.377607 | 56296630 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 555,635 | 0.037273 | 56296630 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 488,727 | 1,026.740757 | 56296630 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 468,885 | 0.067710 | 56296630 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,780 | 1.000973 | 56296630 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,440 | 0.502364 | 56296630 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 440,350 | 24.793746 | 56296630 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 435,987 | 920,540.066198 | 56296630 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 5726 ; routes examinées : 89279792 ; candidats optimisés : 447479 ; net attendu > 0 : 304 ; dernier cycle 210.0 ms
- Rejets (moteur) : {'spread_below_threshold': 87276230, 'liquidity_below_min': 1549773, 'negative_expected_net': 447175, 'borrow_bound_too_small': 5712, 'cycle_budget_exhausted': 598}
- Enregistrements de la session : 447479 ; net attendu > 0 : 304 ; simulés (eth_call de la vraie tx) : 5 (ok 4, échec 1) ; étiquettes ghost N+1 : 3/5 positives
- Décisions : {'REJECTED': 447479} ; motifs de rejet : {'below_safety_margin': 284, 'negative_expected_net': 447175, 'p_lower_below_threshold': 291, 'reliability_not_demonstrated': 13, 'simulation_failed': 1, 'stale_data': 60}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56275611 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.125642 WETH | 0.000019 WETH | 0.000000 WETH | 0.000002 WETH | 0.000016 WETH (0.0309 €) | — | 1.30 | 0.087 (n=116) | REJECTED | below_safety_margin(16317017251291<25128348512387), p_lower_below_threshold(0.09<0.75) |
| 56275611 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 256.896018 USDC | 0.038127 USDC | 0.000000 USDC | 0.004641 USDC | 0.033486 USDC (0.0308 €) | — | 1.30 | 0.087 (n=116) | REJECTED | below_safety_margin(33486<51379), p_lower_below_threshold(0.09<0.75) |
| 56275611 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.160189 WETH | 0.000018 WETH | 0.000000 WETH | 0.000002 WETH | 0.000016 WETH (0.0300 €) | — | 0.99 | 0.103 (n=365) | REJECTED | below_safety_margin(15862162118235<32037872399716), p_lower_below_threshold(0.10<0.75) |
| 56275611 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 328.189417 USDC | 0.037194 USDC | 0.000000 USDC | 0.004641 USDC | 0.032553 USDC (0.0299 €) | — | 0.99 | 0.103 (n=365) | REJECTED | below_safety_margin(32553<65637), p_lower_below_threshold(0.10<0.75) |
| 56279864 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.146786 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0218 €) | — | 0.79 | 0.267 (n=1584) | REJECTED | below_safety_margin(11545129051888<29357284918098), p_lower_below_threshold(0.27<0.75) |
| 56279864 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 338.772944 USDC | 0.030143 USDC | 0.000000 USDC | 0.006497 USDC | 0.023646 USDC (0.0218 €) | — | 0.70 | 0.267 (n=1584) | REJECTED | below_safety_margin(23646<67754), p_lower_below_threshold(0.27<0.75) |
| 56279864 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003914 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0217 €) | — | 0.82 | 0.267 (n=1584) | REJECTED | below_safety_margin(32<78), p_lower_below_threshold(0.27<0.75) |
| 56252219 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 310.545098 USDC | 0.024609 USDC | 0.000000 USDC | 0.004606 USDC | 0.020003 USDC (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(20003<62109), p_lower_below_threshold(0.10<0.75) |
| 56252220 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 310.545098 USDC | 0.024609 USDC | 0.000000 USDC | 0.004606 USDC | 0.020003 USDC (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(20003<62109), p_lower_below_threshold(0.10<0.75) |
| 56252219 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.151840 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(9758427752881<30368070316317), p_lower_below_threshold(0.10<0.75) |
| 56252220 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.151840 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(9758427752881<30368070316317), p_lower_below_threshold(0.10<0.75) |
| 56295284 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 50.819962 USDC | 0.026105 USDC | 0.000000 USDC | 0.006211 USDC | 0.019894 USDC (0.0183 €) | — | 3.91 | 0.202 (n=1236) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56295284 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.024957 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0183 €) | 0.000010 WETH | 3.88 | 0.202 (n=1236) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56295284 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 48.545964 USDC | 0.024557 USDC | 0.000000 USDC | 0.006211 USDC | 0.018346 USDC (0.0169 €) | — | 3.78 | 0.202 (n=1236) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56295284 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.023802 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0168 €) | 0.000009 WETH | 3.75 | 0.202 (n=1236) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56275611 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.051409 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0159 €) | — | 1.63 | 0.233 (n=30) | REJECTED | below_safety_margin(8391564273252<10281899127144), p_lower_below_threshold(0.23<0.75) |
| 56275611 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 105.234204 USDC | 0.021571 USDC | 0.000000 USDC | 0.004356 USDC | 0.017215 USDC (0.0158 €) | — | 1.64 | 0.233 (n=30) | REJECTED | below_safety_margin(17215<21046), p_lower_below_threshold(0.23<0.75) |
| 56258818 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→WETH | 0.028626 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0137 €) | — | 2.53 | 0.103 (n=364) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 56295309 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 94.921722 USDC | 0.016756 USDC | 0.000000 USDC | 0.004691 USDC | 0.012065 USDC (0.0111 €) | — | 1.27 | 0.055 (n=15) | REJECTED | below_safety_margin(12065<18984), stale_data(4117ms>4000.0), reliability_not_demonstrated |
| 56295309 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001160 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0108 €) | — | 1.38 | 0.055 (n=15) | REJECTED | below_safety_margin(16<23), stale_data(4121ms>4000.0), reliability_not_demonstrated |
| 56295284 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 38.195053 USDC | 0.017548 USDC | 0.000000 USDC | 0.006211 USDC | 0.011337 USDC (0.0104 €) | — | 2.97 | 0.267 (n=1584) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56295284 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.018684 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0104 €) | 0.000006 WETH | 2.95 | 0.267 (n=1584) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56295284 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 36.303023 USDC | 0.016544 USDC | 0.000000 USDC | 0.006211 USDC | 0.010333 USDC (0.0095 €) | — | 2.85 | 0.267 (n=1584) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56295284 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.017693 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0095 €) | — | 2.84 | 0.267 (n=1584) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56295284 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 36.493921 USDC | 0.016241 USDC | 0.000000 USDC | 0.006211 USDC | 0.010030 USDC (0.0092 €) | — | 2.75 | 0.267 (n=1584) | REJECTED | p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8239 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
