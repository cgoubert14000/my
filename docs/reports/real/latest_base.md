# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T22:16:40+00:00 ; durée 238.33 min ; blocs 53167873 → 53175023 (7100 vus)

## Connexion
- Requêtes RPC : 84889 ; erreurs : 451 ; latence p50/p95 : 95.2/541.9 ms
- Rafraîchissements d'état : 7100 ; âge des données au dernier bloc : 2.22 s ; changements de frais LP observés (pools à frais dynamiques) : 8436
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 39269 ; cycles déclenchés par événement : 5464 ; avance médiane sur le rafraîchissement multicall : 304 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,352.39 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 519 pools, 301 jetons, 18846 routes
- Par DEX : uniswap_v3 145, aerodrome 211, aerodrome_slipstream 120, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 185 (rejetés 2) → 590 jetons ; pools candidats 3771 (énumérés 330, par paires 0), mesurés 521, sous le plancher de 10000.0 $ : 2 → gardés 519 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2347.170972, 'cbBTC': 80539.356341, 'AERO': 0.69796}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,192,534 | 2,352.389480 | 53175023 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,668,868 | 0.029046 | 53175023 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,224,288 | 0.029025 | 53175023 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,649,997 | 0.000012 | 53175023 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,644,068 | 90.550569 | 53175023 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,444,786 | 2,349.855815 | 53175023 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,041,989 | 0.001637 | 53175023 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,951,751 | 1.441450 | 53175023 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,761,810 | 0.029058 | 53175023 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,093,767 | 2,350.604399 | 53175023 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,500,641 | 2,350.714053 | 53175023 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,265,883 | 0.998746 | 53175023 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,736,941 | 37,091.330577 | 53175023 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,974,576 | 0.029023 | 53175023 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,583,753 | 90.565358 | 53175023 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,368,035 | 2,353.068613 | 53175023 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 2,194,661 | 0.000012 | 53175023 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,143,795 | 1,220,734.716423 | 53175023 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,829,281 | 0.018686 | 53175023 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,819,494 | 0.000000 | 53175023 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,793,662 | 397.814067 | 53175023 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 1,700,238 | 0.000012 | 53175023 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,692,611 | 0.000012 | 53175023 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,688,843 | 0.000012 | 53175023 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,532,551 | 0.005880 | 53175023 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,472,286 | 1.662536 | 53175023 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,608 | 0.826459 | 53175023 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,454,311 | 3,382.173688 | 53175023 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,396,403 | 13,694.398015 | 53175023 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,255,774 | 0.000267 | 53175023 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,240,091 | 2,349.745640 | 53175023 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,203,136 | 3,358.103728 | 53175023 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,201,196 | 67.346385 | 53175023 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,188,321 | 0.000266 | 53175023 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,169,858 | 35,679,419.037098 | 53175023 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,165,530 | 1,068,188.632366 | 53175023 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,129,431 | 0.000000 | 53175023 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,118,797 | 505,792.662100 | 53175023 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,084,846 | 71,849.228086 | 53175023 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,062,788 | 55.421537 | 53175023 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,050,683 | 16.529391 | 53175023 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,050,163 | 21,236,715.146711 | 53175023 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,038,041 | 0.038544 | 53175023 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 945,068 | 2,338.016459 | 53175023 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 921,177 | 1,075.336839 | 53175023 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 909,604 | 0.000560 | 53175023 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 902,143 | 90.276442 | 53175023 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/msETH (stable) | 500 | 888,515 | 2.312268 | 53175023 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 885,269 | 17.772397 | 53175023 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 850,193 | 2,352.810424 | 53175023 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 839,661 | 17.693118 | 53175023 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 809,286 | 0.000009 | 53175023 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 803,038 | 0.057868 | 53175023 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 796,460 | 0.803179 | 53175023 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 757,288 | 4,555,352.139123 | 53175023 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 752,738 | 0.627759 | 53175023 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 712,345 | 137,301.720757 | 53175023 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 696,246 | 503,081.984985 | 53175023 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 685,066 | 0.590617 | 53175023 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,348 | 0.108819 | 53175023 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 12563 ; routes examinées : 236762298 ; candidats optimisés : 724446 ; net attendu > 0 : 484 ; dernier cycle 167.2 ms
- Rejets (moteur) : {'spread_below_threshold': 232844585, 'liquidity_below_min': 2986431, 'negative_expected_net': 723962, 'borrow_bound_too_small': 205937, 'cycle_budget_exhausted': 899}
- Enregistrements de la session : 724446 ; net attendu > 0 : 484 ; simulés (eth_call de la vraie tx) : 24 (ok 8, échec 16) ; étiquettes ghost N+1 : 3/19 positives
- Décisions : {'REJECTED': 724446} ; motifs de rejet : {'below_safety_margin': 248, 'negative_expected_net': 723962, 'p_lower_below_threshold': 432, 'price_impact': 4, 'reliability_not_demonstrated': 52, 'simulation_failed': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53173674 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.860012 WETH | 0.000987 WETH | 0.000000 WETH | 0.000003 WETH | 0.000984 WETH (2.1216 €) | — | 5.29 | 0.094 (n=303) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53173674 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 4,359.237608 USDC | 2.313517 USDC | 0.000000 USDC | 0.008126 USDC | 2.305391 USDC (2.1210 €) | — | 5.29 | 0.094 (n=303) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53173674 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.053073 cbBTC | 0.000029 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000029 cbBTC (2.1201 €) | — | 5.37 | 0.094 (n=303) | REJECTED | p_lower_below_threshold(0.09<0.75) |
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
| 53173674 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,178.638376 USDC | 0.668488 USDC | 0.000000 USDC | 0.007770 USDC | 0.660718 USDC (0.6079 €) | — | 5.61 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53173674 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.502604 WETH | 0.000285 WETH | 0.000000 WETH | 0.000003 WETH | 0.000282 WETH (0.6075 €) | — | 5.60 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53173674 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.014211 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6073 €) | — | 5.75 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53170773 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001644 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4731 €) | — | 38.81 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 134.135900 USDC | 0.521005 USDC | 0.000000 USDC | 0.007060 USDC | 0.513945 USDC (0.4728 €) | — | 38.32 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53170773 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001631 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4694 €) | — | 38.80 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 133.067463 USDC | 0.517115 USDC | 0.000000 USDC | 0.007060 USDC | 0.510055 USDC (0.4693 €) | — | 38.33 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53170773 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001648 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4679 €) | — | 38.28 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2875 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
