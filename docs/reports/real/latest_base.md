# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T13:35:07+00:00 ; durée 64.38 min ; blocs 56049289 → 56068577 (1658 vus)

## Connexion
- Requêtes RPC : 25486 ; erreurs : 0 ; latence p50/p95 : 548.7/2,613.1 ms
- Rafraîchissements d'état : 1658 ; âge des données au dernier bloc : 15.23 s ; changements de frais LP observés (pools à frais dynamiques) : 1337
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 953 ; cycles déclenchés par événement : 394 ; avance médiane sur le rafraîchissement multicall : 746 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,051.62 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 15580 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 283, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2055.911323, 'cbBTC': 73875.741474, 'AERO': 0.535737}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,930,161 | 2,051.621110 | 56068629 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,345,922 | 0.027822 | 56068629 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,563,502 | 0.027840 | 56068629 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,414,748 | 0.000014 | 56068629 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,080,766 | 2,052.157015 | 56068629 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,831,948 | 105.068888 | 56068629 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,306,788 | 0.027828 | 56068629 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,254,178 | 1.845990 | 56068629 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,030,839 | 2,051.394716 | 56068629 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,874,729 | 1.000003 | 56068629 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,042,204 | 42,562.663648 | 56068629 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 639 | 2,915,199 | 2,051.736562 | 56068629 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,207,390 | 0.027825 | 56068629 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,949,764 | 1,122,344.048062 | 56068629 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,650,302 | 0.000014 | 56068629 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,615,751 | 0.016291 | 56068629 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,586,554 | 0.000014 | 56068629 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,547,839 | 0.000000 | 56068629 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,530,104 | 0.000014 | 56068629 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,512,488 | 0.006541 | 56068629 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,592 | 0.825553 | 56068629 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,000 | 1.373193 | 56068629 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,415,257 | 418.976502 | 56068629 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,270,053 | 2,051.840129 | 56068629 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,262,555 | 3,789.732388 | 56068629 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,228,338 | 15,044.536458 | 56068629 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,156,233 | 2,057.458259 | 56068629 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,103,012 | 2,052.248163 | 56068629 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,862 | 86.341789 | 56068629 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,044,353 | 33,269,703.419382 | 56068629 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 997,580 | 105.787246 | 56068629 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 962,337 | 21.230380 | 56068629 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 940,889 | 556,704.492046 | 56068629 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 918,263 | 0.001494 | 56068629 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 912,234 | 0.000014 | 56068629 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 901,946 | 23,083,926.203551 | 56068629 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 900,380 | 0.051177 | 56068629 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 885,311 | 1,010.205359 | 56068629 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 877,856 | 2,050.503253 | 56068629 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 865,606 | 0.000000 | 56068629 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 771,274 | 79.237918 | 56068629 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 763,113 | 0.051953 | 56068629 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 758,414 | 22.554487 | 56068629 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 743,057 | 116,223.623041 | 56068629 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 706,181 | 3,815.056844 | 56068629 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 694,599 | 0.802938 | 56068629 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 671,364 | 0.535539 | 56068629 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 665,623 | 4,502,047.765505 | 56068629 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 622,945 | 0.488710 | 56068629 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 607,114 | 144,659.638091 | 56068629 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 585,203 | 0.000007 | 56068629 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 579,426 | 0.000259 | 56068629 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 578,097 | 552,676.330977 | 56068629 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 561,799 | 0.037917 | 56068629 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 494,710 | 1,010.602245 | 56068629 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 467,478 | 0.067448 | 56068629 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 458,153 | 0.492814 | 56068629 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,336 | 1.000875 | 56068629 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/uSOL | 3000 | 441,887 | 24.617686 | 56068629 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 436,613 | 915,629.723152 | 56068629 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 2051 ; routes examinées : 31954580 ; candidats optimisés : 149699 ; net attendu > 0 : 150 ; dernier cycle 586.8 ms
- Rejets (moteur) : {'spread_below_threshold': 31210597, 'liquidity_below_min': 589273, 'negative_expected_net': 149549, 'borrow_bound_too_small': 4088, 'cycle_budget_exhausted': 923}
- Enregistrements de la session : 149699 ; net attendu > 0 : 150 ; simulés (eth_call de la vraie tx) : 13 (ok 9, échec 4) ; étiquettes ghost N+1 : 10/10 positives
- Décisions : {'REJECTED': 149699} ; motifs de rejet : {'below_safety_margin': 111, 'negative_expected_net': 149549, 'p_lower_below_threshold': 148, 'reliability_not_demonstrated': 2, 'simulation_failed': 4, 'stale_data': 57}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56049891 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.168890 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0267 €) | — | 0.84 | 0.262 (n=1560) | REJECTED | below_safety_margin(14139452649186<33778000811495), stale_data(5505ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.004526 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0265 €) | — | 0.86 | 0.262 (n=1560) | REJECTED | below_safety_margin(39<90), stale_data(5512ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 359.906777 USDC | 0.034977 USDC | 0.000000 USDC | 0.006210 USDC | 0.028767 USDC (0.0265 €) | — | 0.80 | 0.262 (n=1560) | REJECTED | below_safety_margin(28767<71981), stale_data(5520ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.131279 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0204 €) | — | 0.82 | 0.262 (n=1560) | REJECTED | below_safety_margin(10785261854409<26255881789766), stale_data(5478ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 279.774953 USDC | 0.027730 USDC | 0.000000 USDC | 0.006210 USDC | 0.021520 USDC (0.0198 €) | — | 0.77 | 0.262 (n=1560) | REJECTED | below_safety_margin(21520<55954), stale_data(5492ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003163 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0197 €) | — | 0.92 | 0.262 (n=1560) | REJECTED | below_safety_margin(29<63), stale_data(5485ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049892 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.207595 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0170 €) | — | 0.43 | 0.147 (n=41) | REJECTED | below_safety_margin(9007428594155<41519032483598), p_lower_below_threshold(0.15<0.75) |
| 56049892 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.005846 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0170 €) | — | 0.43 | 0.147 (n=41) | REJECTED | below_safety_margin(25<116), p_lower_below_threshold(0.15<0.75) |
| 56049892 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 464.439648 USDC | 0.024900 USDC | 0.000000 USDC | 0.006532 USDC | 0.018368 USDC (0.0169 €) | — | 0.40 | 0.147 (n=41) | REJECTED | below_safety_margin(18368<92887), p_lower_below_threshold(0.15<0.75) |
| 56049891 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.154060 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0167 €) | — | 0.57 | 0.262 (n=1560) | REJECTED | below_safety_margin(8831772322583<30812080858514), stale_data(5649ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 336.469384 USDC | 0.024170 USDC | 0.000000 USDC | 0.006210 USDC | 0.017960 USDC (0.0165 €) | — | 0.53 | 0.262 (n=1560) | REJECTED | below_safety_margin(17960<67293), stale_data(5641ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003675 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0163 €) | — | 0.65 | 0.262 (n=1560) | REJECTED | below_safety_margin(24<73), stale_data(5656ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56052461 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.110935 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0159 €) | — | 0.76 | 0.100 (n=358) | REJECTED | below_safety_margin(8390983438045<22187061430089), p_lower_below_threshold(0.10<0.75) |
| 56052462 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.110935 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0159 €) | — | 0.76 | 0.100 (n=358) | REJECTED | below_safety_margin(8390983438045<22187061430089), p_lower_below_threshold(0.10<0.75) |
| 56052461 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 226.724097 USDC | 0.021861 USDC | 0.000000 USDC | 0.004621 USDC | 0.017240 USDC (0.0159 €) | — | 0.76 | 0.100 (n=358) | REJECTED | below_safety_margin(17240<45344), p_lower_below_threshold(0.10<0.75) |
| 56052462 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 226.724097 USDC | 0.021861 USDC | 0.000000 USDC | 0.004621 USDC | 0.017240 USDC (0.0159 €) | — | 0.76 | 0.100 (n=358) | REJECTED | below_safety_margin(17240<45344), p_lower_below_threshold(0.10<0.75) |
| 56049891 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002690 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0116 €) | — | 0.63 | 0.262 (n=1560) | REJECTED | below_safety_margin(17<53), stale_data(5600ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 233.640912 USDC | 0.018582 USDC | 0.000000 USDC | 0.006210 USDC | 0.012372 USDC (0.0114 €) | — | 0.53 | 0.262 (n=1560) | REJECTED | below_safety_margin(12372<46728), stale_data(5594ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.113398 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0111 €) | — | 0.52 | 0.262 (n=1560) | REJECTED | below_safety_margin(5881677709497<22679664416215), stale_data(5588ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56056252 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 277.667197 USDC | 0.016300 USDC | 0.000000 USDC | 0.004621 USDC | 0.011679 USDC (0.0107 €) | — | 0.42 | 0.100 (n=358) | REJECTED | below_safety_margin(11679<55533), p_lower_below_threshold(0.10<0.75) |
| 56056251 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 277.667197 USDC | 0.016300 USDC | 0.000000 USDC | 0.004621 USDC | 0.011679 USDC (0.0107 €) | — | 0.42 | 0.100 (n=358) | REJECTED | below_safety_margin(11679<55533), p_lower_below_threshold(0.10<0.75) |
| 56054354 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 37.051083 USDC | 0.016295 USDC | 0.000000 USDC | 0.004620 USDC | 0.011675 USDC (0.0107 €) | — | 3.15 | 0.072 (n=493) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 56056252 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.003010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0102 €) | — | 0.50 | 0.100 (n=358) | REJECTED | below_safety_margin(15<60), p_lower_below_threshold(0.10<0.75) |
| 56056251 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.003010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0102 €) | — | 0.50 | 0.100 (n=358) | REJECTED | below_safety_margin(15<60), p_lower_below_threshold(0.10<0.75) |
| 56065389 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 24.453827 USDC | 0.016530 USDC | 0.000000 USDC | 0.005895 USDC | 0.010635 USDC (0.0098 €) | — | 4.35 | 0.298 (n=216) | REJECTED | stale_data(5288ms>4000.0), p_lower_below_threshold(0.30<0.75) |

## Fiabilité et décision
- Observations ghost : 8067 ; taux observé 0.213 ; borne inférieure crédible (0.9) 0.207 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
