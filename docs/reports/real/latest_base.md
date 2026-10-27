# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T23:29:03+00:00 ; durée 310.71 min ; blocs 53167873 → 53177194 (9247 vus)

## Connexion
- Requêtes RPC : 109674 ; erreurs : 471 ; latence p50/p95 : 87.5/445.3 ms
- Rafraîchissements d'état : 9247 ; âge des données au dernier bloc : 2.37 s ; changements de frais LP observés (pools à frais dynamiques) : 10224
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 42666 ; cycles déclenchés par événement : 6121 ; avance médiane sur le rafraîchissement multicall : 223 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,351.40 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 519 pools, 301 jetons, 18846 routes
- Par DEX : uniswap_v3 145, aerodrome 211, aerodrome_slipstream 120, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 185 (rejetés 2) → 590 jetons ; pools candidats 3771 (énumérés 330, par paires 0), mesurés 521, sous le plancher de 10000.0 $ : 2 → gardés 519 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2347.170972, 'cbBTC': 80539.356341, 'AERO': 0.69796}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,664,958 | 2,351.399987 | 53177195 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,661,084 | 0.029047 | 53177195 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,219,758 | 0.029025 | 53177195 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,648,510 | 0.000012 | 53177195 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,641,371 | 90.040839 | 53177195 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,438,566 | 2,348.050580 | 53177195 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,040,656 | 0.001638 | 53177195 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,957,514 | 1.431286 | 53177195 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,759,404 | 0.029058 | 53177195 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,085,715 | 2,348.807806 | 53177195 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,494,118 | 2,348.925623 | 53177195 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,263,965 | 0.998745 | 53177195 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,734,763 | 37,103.378490 | 53177195 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,973,095 | 0.029022 | 53177195 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,588,479 | 90.046990 | 53177195 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,367,560 | 2,351.476919 | 53177195 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 2,194,154 | 0.000012 | 53177195 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,139,482 | 1,224,630.551123 | 53177195 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,831,515 | 0.000000 | 53177195 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,822,929 | 0.018580 | 53177195 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,792,500 | 398.154038 | 53177195 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 1,699,832 | 0.000012 | 53177195 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,692,255 | 0.000012 | 53177195 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,688,491 | 0.000012 | 53177195 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,536,576 | 0.005901 | 53177195 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,280 | 1.658893 | 53177195 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,579 | 0.826489 | 53177195 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,459,234 | 3,360.542851 | 53177195 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,395,341 | 13,704.199515 | 53177195 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,255,213 | 0.000267 | 53177195 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,242,072 | 2,348.053068 | 53177195 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,207,061 | 3,358.072677 | 53177195 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,204,133 | 67.018286 | 53177195 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,186,655 | 0.000266 | 53177195 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,169,262 | 35,677,363.058060 | 53177195 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,166,777 | 1,065,010.438058 | 53177195 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,130,748 | 0.000000 | 53177195 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,118,320 | 505,799.605428 | 53177195 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,091,630 | 70,899.391910 | 53177195 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,065,592 | 55.130243 | 53177195 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,059,399 | 16.169997 | 53177195 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,049,710 | 21,236,902.374132 | 53177195 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,041,205 | 0.038316 | 53177195 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 944,891 | 2,338.016459 | 53177195 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 926,960 | 1,074.195922 | 53177195 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 911,105 | 0.000563 | 53177195 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 903,298 | 90.276491 | 53177195 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/msETH (stable) | 500 | 888,142 | 2.312268 | 53177195 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 885,572 | 17.762433 | 53177195 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 850,016 | 2,350.658767 | 53177195 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 841,595 | 17.641017 | 53177195 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 811,882 | 0.000009 | 53177195 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 803,879 | 0.057996 | 53177195 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 796,125 | 0.803180 | 53177195 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 756,245 | 4,564,114.618119 | 53177195 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 752,489 | 0.628226 | 53177195 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 711,863 | 137,372.112677 | 53177195 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 695,952 | 503,302.662646 | 53177195 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 684,970 | 0.590617 | 53177195 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 675,454 | 0.109109 | 53177195 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 15367 ; routes examinées : 289606482 ; candidats optimisés : 902365 ; net attendu > 0 : 586 ; dernier cycle 257.0 ms
- Rejets (moteur) : {'spread_below_threshold': 284746332, 'liquidity_below_min': 3712242, 'negative_expected_net': 901779, 'borrow_bound_too_small': 244402, 'cycle_budget_exhausted': 1141}
- Enregistrements de la session : 902365 ; net attendu > 0 : 586 ; simulés (eth_call de la vraie tx) : 27 (ok 8, échec 19) ; étiquettes ghost N+1 : 3/22 positives
- Décisions : {'REJECTED': 902365} ; motifs de rejet : {'below_safety_margin': 286, 'negative_expected_net': 901779, 'p_lower_below_threshold': 513, 'price_impact': 4, 'reliability_not_demonstrated': 73, 'simulation_failed': 19}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53173674 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.860012 WETH | 0.000987 WETH | 0.000000 WETH | 0.000003 WETH | 0.000984 WETH (2.1216 €) | — | 5.29 | 0.094 (n=303) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53173674 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 4,359.237608 USDC | 2.313517 USDC | 0.000000 USDC | 0.008126 USDC | 2.305391 USDC (2.1210 €) | — | 5.29 | 0.094 (n=303) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53173674 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.053073 cbBTC | 0.000029 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000029 cbBTC (2.1201 €) | — | 5.37 | 0.094 (n=303) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53177043 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.060889 cbBTC | 0.000024 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000024 cbBTC (1.7667 €) | — | 3.90 | 0.002 (n=148) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53177043 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 4,978.060856 USDC | 1.921200 USDC | 0.000000 USDC | 0.005997 USDC | 1.915203 USDC (1.7620 €) | — | 3.85 | 0.002 (n=148) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53173674 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 1.724012 WETH | 0.000770 WETH | 0.000000 WETH | 0.000003 WETH | 0.000767 WETH (1.6552 €) | — | 4.45 | 0.124 (n=165) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53173674 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 4,014.698590 USDC | 1.805936 USDC | 0.000000 USDC | 0.007058 USDC | 1.798878 USDC (1.6550 €) | — | 4.48 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53173674 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.049114 cbBTC | 0.000022 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000022 cbBTC (1.6540 €) | — | 4.53 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53173674 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 3,131.730995 USDC | 1.512105 USDC | 0.000000 USDC | 0.005631 USDC | 1.506474 USDC (1.3860 €) | — | 4.81 | 0.002 (n=148) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53173674 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.038861 cbBTC | 0.000019 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000019 cbBTC (1.3857 €) | — | 4.80 | 0.002 (n=148) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53173674 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 2,825.202856 USDC | 1.236134 USDC | 0.000000 USDC | 0.007058 USDC | 1.229076 USDC (1.1307 €) | — | 4.35 | 0.094 (n=303) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53173674 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.215260 WETH | 0.000527 WETH | 0.000000 WETH | 0.000003 WETH | 0.000524 WETH (1.1303 €) | — | 4.31 | 0.094 (n=303) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53173674 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.034548 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.1299 €) | — | 4.40 | 0.094 (n=303) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53173674 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 1.375748 WETH | 0.000490 WETH | 0.000000 WETH | 0.000003 WETH | 0.000487 WETH (1.0514 €) | — | 3.54 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53173674 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 3,206.338997 USDC | 1.149748 USDC | 0.000000 USDC | 0.007058 USDC | 1.142690 USDC (1.0513 €) | — | 3.56 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53173674 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.039503 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0511 €) | — | 3.58 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53173674 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.218714 WETH | 0.000437 WETH | 0.000000 WETH | 0.000003 WETH | 0.000434 WETH (0.9361 €) | — | 3.56 | 0.094 (n=303) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53173674 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 2,831.716030 USDC | 1.025188 USDC | 0.000000 USDC | 0.007770 USDC | 1.017418 USDC (0.9360 €) | — | 3.59 | 0.094 (n=303) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53173674 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.034547 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.9352 €) | — | 3.64 | 0.094 (n=303) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53177043 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.306003 WETH | 0.000369 WETH | 0.000000 WETH | 0.000003 WETH | 0.000365 WETH (0.7907 €) | — | 2.80 | 0.127 (n=391) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 53177043 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.036904 cbBTC | 0.000011 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000011 cbBTC (0.7902 €) | — | 2.88 | 0.127 (n=391) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53177043 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.450799 WETH | 0.000368 WETH | 0.000000 WETH | 0.000003 WETH | 0.000364 WETH (0.7881 €) | — | 2.51 | 0.127 (n=391) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 53177043 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 3,035.223693 USDC | 0.864758 USDC | 0.000000 USDC | 0.008141 USDC | 0.856617 USDC (0.7881 €) | — | 2.82 | 0.127 (n=391) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53177043 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.041335 cbBTC | 0.000011 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000011 cbBTC (0.7873 €) | — | 2.56 | 0.127 (n=391) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53177043 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 3,415.228360 USDC | 0.862106 USDC | 0.000000 USDC | 0.008141 USDC | 0.853965 USDC (0.7856 €) | — | 2.50 | 0.127 (n=391) | REJECTED | p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2878 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
