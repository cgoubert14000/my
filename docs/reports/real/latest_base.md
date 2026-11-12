# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T08:52:23+00:00 ; durée 211.08 min ; blocs 56352481 → 56415756 (9529 vus)

## Connexion
- Requêtes RPC : 130406 ; erreurs : 5 ; latence p50/p95 : 439.3/1,514.3 ms
- Rafraîchissements d'état : 9529 ; âge des données au dernier bloc : 11.52 s ; changements de frais LP observés (pools à frais dynamiques) : 4251
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1475 ; cycles déclenchés par événement : 699 ; avance médiane sur le rafraîchissement multicall : 504 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,044.78 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 265 jetons, 15538 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2045.219297, 'cbBTC': 73500.635487, 'AERO': 0.536237}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,721,316 | 2,044.775509 | 56415783 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,384,348 | 0.027863 | 56415783 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,684,117 | 0.027806 | 56415783 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,450,380 | 0.000014 | 56415783 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,069,150 | 2,048.066307 | 56415783 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,808,759 | 105.081055 | 56415783 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,253,347 | 0.027873 | 56415783 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,190,040 | 1.894004 | 56415783 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,185,552 | 2,048.548514 | 56415783 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,866,071 | 0.998657 | 56415783 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,034,283 | 42,500.099224 | 56415783 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 146 | 2,861,353 | 2,048.797439 | 56415783 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,193,744 | 0.027823 | 56415783 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,938,764 | 1,127,553.662132 | 56415783 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,641,469 | 0.000014 | 56415783 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,638,605 | 0.016637 | 56415783 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,586,934 | 0.000014 | 56415783 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,558,900 | 0.000000 | 56415783 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,525,210 | 0.000014 | 56415783 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,497,417 | 0.006515 | 56415783 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,872 | 0.830193 | 56415783 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,399,363 | 430.879302 | 56415783 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,268,040 | 2,044.941257 | 56415783 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,237,537 | 3,873.601298 | 56415783 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,208,288 | 15,467.147541 | 56415783 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,153,506 | 2,052.316781 | 56415783 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,127,325 | 2,048.033071 | 56415783 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,555 | 86.229165 | 56415783 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,046,779 | 1.389936 | 56415783 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,035,041 | 33,803,543.346035 | 56415783 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,009,283 | 104.382842 | 56415783 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 963,781 | 21.133929 | 56415783 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 934,096 | 563,081.900646 | 56415783 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 908,789 | 0.001477 | 56415783 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 898,257 | 0.000014 | 56415783 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 893,772 | 23,297,416.943306 | 56415783 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 891,805 | 0.051322 | 56415783 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 876,392 | 2,054.853960 | 56415783 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 874,836 | 1,024.994056 | 56415783 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 851,843 | 0.000000 | 56415783 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 778,652 | 77.579207 | 56415783 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 745,970 | 23.082376 | 56415783 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 745,774 | 0.049549 | 56415783 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 735,128 | 117,953.632722 | 56415783 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 695,914 | 3,846.107766 | 56415783 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 692,772 | 0.801801 | 56415783 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 664,117 | 0.521924 | 56415783 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 642,383 | 4,804,175.648628 | 56415783 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 615,797 | 0.477280 | 56415783 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 580,672 | 157,194.595163 | 56415783 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 573,168 | 0.000257 | 56415783 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2234 | 572,820 | 561,762.064130 | 56415783 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 565,891 | 0.000007 | 56415783 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 559,181 | 0.037636 | 56415783 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 487,104 | 1,024.976306 | 56415783 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 462,010 | 0.066422 | 56415783 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,543 | 1.001030 | 56415783 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,250 | 0.501968 | 56415783 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 438,707 | 24.807641 | 56415783 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 432,495 | 930,029.609200 | 56415783 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 10227 ; routes examinées : 158907126 ; candidats optimisés : 762201 ; net attendu > 0 : 71 ; dernier cycle 396.9 ms
- Rejets (moteur) : {'spread_below_threshold': 156195248, 'liquidity_below_min': 1938671, 'negative_expected_net': 762130, 'borrow_bound_too_small': 10218, 'cycle_budget_exhausted': 788}
- Enregistrements de la session : 762201 ; net attendu > 0 : 71 ; simulés (eth_call de la vraie tx) : 3 (ok 3, échec 0) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 762201} ; motifs de rejet : {'below_safety_margin': 56, 'negative_expected_net': 762130, 'p_lower_below_threshold': 71, 'stale_data': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.218273 USDC | 0.032458 USDC | 0.000000 USDC | 0.006143 USDC | 0.026315 USDC (0.0242 €) | — | 7.47 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017342 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0242 €) | 0.000013 WETH | 7.41 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.404259 USDC | 0.032255 USDC | 0.000000 USDC | 0.006143 USDC | 0.026112 USDC (0.0240 €) | — | 7.38 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017304 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0240 €) | 0.000013 WETH | 7.37 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 34.633173 USDC | 0.031152 USDC | 0.000000 USDC | 0.006143 USDC | 0.025009 USDC (0.0230 €) | — | 7.22 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017066 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0230 €) | 0.000012 WETH | 7.16 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.013924 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0160 €) | — | 6.09 | 0.077 (n=120) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 56380462 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004048 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 0.42 | 0.102 (n=366) | REJECTED | below_safety_margin(17<80), p_lower_below_threshold(0.10<0.75) |
| 56380462 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 349.650476 USDC | 0.017156 USDC | 0.000000 USDC | 0.004913 USDC | 0.012243 USDC (0.0113 €) | — | 0.35 | 0.102 (n=366) | REJECTED | below_safety_margin(12243<69930), p_lower_below_threshold(0.10<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 26.577874 USDC | 0.018129 USDC | 0.000000 USDC | 0.006143 USDC | 0.011986 USDC (0.0110 €) | — | 4.51 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.012985 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0110 €) | — | 4.51 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 25.295059 USDC | 0.016679 USDC | 0.000000 USDC | 0.006143 USDC | 0.010536 USDC (0.0097 €) | — | 4.17 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.012479 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0097 €) | — | 4.13 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 18.973789 USDC | 0.012147 USDC | 0.000000 USDC | 0.006143 USDC | 0.006004 USDC (0.0055 €) | — | 3.16 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.009378 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0055 €) | — | 3.13 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56358036 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 127.764441 USDC | 0.010716 USDC | 0.000000 USDC | 0.004903 USDC | 0.005813 USDC (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(5813<25552), p_lower_below_threshold(0.09<0.75) |
| 56358037 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 127.764441 USDC | 0.010716 USDC | 0.000000 USDC | 0.004903 USDC | 0.005813 USDC (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(5813<25552), p_lower_below_threshold(0.09<0.75) |
| 56358036 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.062941 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(2840846607235<12588174234970), p_lower_below_threshold(0.09<0.75) |
| 56358037 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.062941 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(2840846607235<12588174234970), p_lower_below_threshold(0.09<0.75) |
| 56388390 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.005953 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0040 €) | — | 3.59 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 12.189597 USDC | 0.010513 USDC | 0.000000 USDC | 0.006143 USDC | 0.004370 USDC (0.0040 €) | — | 3.59 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56366735 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.012368 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0024 €) | — | 1.02 | 0.087 (n=116) | REJECTED | below_safety_margin(1265918134090<2473627526013), p_lower_below_threshold(0.09<0.75) |
| 56403427 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 179.339160 USDC | 0.006581 USDC | 0.000000 USDC | 0.004606 USDC | 0.001975 USDC (0.0018 €) | — | 0.11 | 0.102 (n=366) | REJECTED | below_safety_margin(1975<35867), p_lower_below_threshold(0.10<0.75) |
| 56403428 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 179.339160 USDC | 0.006581 USDC | 0.000000 USDC | 0.004616 USDC | 0.001965 USDC (0.0018 €) | — | 0.11 | 0.102 (n=366) | REJECTED | below_safety_margin(1965<35867), p_lower_below_threshold(0.10<0.75) |
| 56366735 | WETH→[uniswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.014136 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0014 €) | — | 0.53 | 0.087 (n=116) | REJECTED | below_safety_margin(745305964134<2827232825153), p_lower_below_threshold(0.09<0.75) |

## Fiabilité et décision
- Observations ghost : 8243 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
