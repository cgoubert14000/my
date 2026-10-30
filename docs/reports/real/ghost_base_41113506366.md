# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T23:54:18+00:00 ; durée 274.25 min ; blocs 53299323 → 53307548 (8029 vus)

## Connexion
- Requêtes RPC : 91170 ; erreurs : 75 ; latence p50/p95 : 318.2/1,340.4 ms
- Rafraîchissements d'état : 8029 ; âge des données au dernier bloc : 5.5 s ; changements de frais LP observés (pools à frais dynamiques) : 11537
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 50750 ; cycles déclenchés par événement : 4316 ; avance médiane sur le rafraîchissement multicall : 1,091 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,238.00 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18532 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 112, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3774 (énumérés 315, par paires 0), mesurés 500, sous le plancher de 10000.0 $ : 3 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.87299, 'cbBTC': 76304.747909, 'AERO': 0.609807}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,217,875 | 2,237.997175 | 53307549 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,953,890 | 0.029047 | 53307549 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,234,807 | 0.000013 | 53307549 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,003,863 | 0.029120 | 53307549 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,182,778 | 2,241.636675 | 53307549 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,738,531 | 99.187439 | 53307549 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,679,396 | 0.001627 | 53307549 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,870,079 | 1.615907 | 53307549 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,551,839 | 0.029046 | 53307549 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,136,401 | 2,241.453864 | 53307549 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,117,724 | 2,241.557734 | 53307549 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,052,340 | 1.000000 | 53307549 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,537,506 | 37,458.759048 | 53307549 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,745,755 | 0.029106 | 53307549 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,335,314 | 99.097437 | 53307549 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,051,675 | 1,206,344.208581 | 53307549 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,983,971 | 0.000013 | 53307549 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,763,319 | 0.000000 | 53307549 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,734,524 | 0.017658 | 53307549 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,687,767 | 414.815667 | 53307549 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,613,544 | 0.000013 | 53307549 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,567,537 | 0.000013 | 53307549 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,522,166 | 2,244.130636 | 53307549 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,512,933 | 1.548785 | 53307549 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,461,844 | 0.000013 | 53307549 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,512 | 0.825661 | 53307549 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,401,547 | 3,624.719100 | 53307549 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,311,599 | 2,242.179067 | 53307549 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,308,549 | 14,301.501729 | 53307549 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,301,574 | 0.005104 | 53307549 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,176,931 | 70.152090 | 53307549 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,107,869 | 36,184,127.467798 | 53307549 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,056,837 | 514,158.753461 | 53307549 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,032,250 | 21,143,075.977215 | 53307549 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,011,578 | 0.000000 | 53307549 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | WETH/USDC | 3000 | 1,008,672 | 2,237.318790 | 53307549 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,008,171 | 18.515702 | 53307549 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,008,075 | 75,273.818666 | 53307549 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 973,417 | 100.221059 | 53307549 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 964,600 | 67.280926 | 53307549 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 956,707 | 0.044395 | 53307549 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 925,747 | 1,221,922.009998 | 53307549 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 919,959 | 2,235.963227 | 53307549 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 891,385 | 1,077.796912 | 53307549 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,268 | 0.000557 | 53307549 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 859,452 | 3,612.674591 | 53307549 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 842,958 | 19.257279 | 53307549 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,034 | 0.060468 | 53307549 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 757,563 | 0.803531 | 53307549 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 737,999 | 0.000266 | 53307549 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 727,872 | 4,466,352.577490 | 53307549 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 727,662 | 0.600156 | 53307549 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 679,198 | 2.331396 | 53307549 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 677,450 | 0.000008 | 53307549 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 659,276 | 145,302.625157 | 53307549 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 656,349 | 509,859.878417 | 53307549 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 631,696 | 0.504492 | 53307549 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 618,855 | 0.094581 | 53307549 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 601,875 | 0.914729 | 53307549 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 539,401 | 1,078.146735 | 53307549 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 12344 ; routes examinées : 228759008 ; candidats optimisés : 1063233 ; net attendu > 0 : 484 ; dernier cycle 374.1 ms
- Rejets (moteur) : {'spread_below_threshold': 224124832, 'liquidity_below_min': 3519627, 'negative_expected_net': 1062749, 'unquotable': 35130, 'borrow_bound_too_small': 12331, 'pool_quarantined': 2340, 'cycle_budget_exhausted': 1515}
- Enregistrements de la session : 1063233 ; net attendu > 0 : 484 ; simulés (eth_call de la vraie tx) : 27 (ok 13, échec 14) ; étiquettes ghost N+1 : 0/23 positives
- Décisions : {'REJECTED': 1063233} ; motifs de rejet : {'below_safety_margin': 330, 'negative_expected_net': 1062749, 'p_lower_below_threshold': 453, 'reliability_not_demonstrated': 31, 'simulation_failed': 14, 'stale_data': 19}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53304483 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 194.189460 USDC | 0.881802 USDC | 0.000000 USDC | 0.005026 USDC | 0.876776 USDC (0.8066 €) | — | 45.15 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 628.636240 USDC | 0.523468 USDC | 0.000000 USDC | 0.006416 USDC | 0.517052 USDC (0.4757 €) | — | 8.22 | 0.096 (n=30) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 628.636240 USDC | 0.523468 USDC | 0.000000 USDC | 0.006416 USDC | 0.517052 USDC (0.4757 €) | — | 8.22 | 0.096 (n=30) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53307356 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.280829 WETH | 0.000234 WETH | 0.000000 WETH | 0.000003 WETH | 0.000231 WETH (0.4751 €) | — | 8.22 | 0.096 (n=30) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53307356 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.280829 WETH | 0.000234 WETH | 0.000000 WETH | 0.000003 WETH | 0.000231 WETH (0.4751 €) | 0.000231 WETH | 8.22 | 0.096 (n=30) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 642.908521 USDC | 0.517904 USDC | 0.000000 USDC | 0.006416 USDC | 0.511488 USDC (0.4706 €) | — | 7.96 | 0.254 (n=93) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 642.908521 USDC | 0.517904 USDC | 0.000000 USDC | 0.006416 USDC | 0.511488 USDC (0.4706 €) | — | 7.96 | 0.254 (n=93) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 53307356 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.286774 WETH | 0.000231 WETH | 0.000000 WETH | 0.000003 WETH | 0.000228 WETH (0.4699 €) | — | 7.96 | 0.254 (n=93) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.25<0.75) |
| 53307356 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.286774 WETH | 0.000231 WETH | 0.000000 WETH | 0.000003 WETH | 0.000228 WETH (0.4699 €) | 0.000228 WETH | 7.96 | 0.254 (n=93) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 53302962 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.002481 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3587 €) | — | 20.52 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53302962 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 191.105100 USDC | 0.396516 USDC | 0.000000 USDC | 0.006734 USDC | 0.389782 USDC (0.3586 €) | — | 20.40 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 463.693528 USDC | 0.363565 USDC | 0.000000 USDC | 0.006416 USDC | 0.357149 USDC (0.3286 €) | — | 7.70 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 463.693528 USDC | 0.363565 USDC | 0.000000 USDC | 0.006416 USDC | 0.357149 USDC (0.3286 €) | — | 7.70 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.207042 WETH | 0.000162 WETH | 0.000000 WETH | 0.000003 WETH | 0.000159 WETH (0.3283 €) | — | 7.70 | 0.114 (n=187) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.207042 WETH | 0.000162 WETH | 0.000000 WETH | 0.000003 WETH | 0.000159 WETH (0.3283 €) | 0.000159 WETH | 7.70 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53302962 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 172.900069 USDC | 0.342781 USDC | 0.000000 USDC | 0.006734 USDC | 0.336047 USDC (0.3092 €) | — | 19.44 | 0.017 (n=82) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53302962 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.002223 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3086 €) | — | 19.70 | 0.017 (n=82) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 484.598311 USDC | 0.291789 USDC | 0.000000 USDC | 0.006416 USDC | 0.285373 USDC (0.2625 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 484.598311 USDC | 0.291789 USDC | 0.000000 USDC | 0.006416 USDC | 0.285373 USDC (0.2625 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.216284 WETH | 0.000130 WETH | 0.000000 WETH | 0.000003 WETH | 0.000127 WETH (0.2623 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.216284 WETH | 0.000130 WETH | 0.000000 WETH | 0.000003 WETH | 0.000127 WETH (0.2623 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 477.797871 USDC | 0.287690 USDC | 0.000000 USDC | 0.006416 USDC | 0.281274 USDC (0.2588 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 477.797871 USDC | 0.287690 USDC | 0.000000 USDC | 0.006416 USDC | 0.281274 USDC (0.2588 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.213235 WETH | 0.000128 WETH | 0.000000 WETH | 0.000003 WETH | 0.000126 WETH (0.2585 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.213235 WETH | 0.000128 WETH | 0.000000 WETH | 0.000003 WETH | 0.000126 WETH (0.2585 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 3895 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
