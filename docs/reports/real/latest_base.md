# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T11:31:05+00:00 ; durée 295.7 min ; blocs 53319584 → 53328453 (8795 vus)

## Connexion
- Requêtes RPC : 103948 ; erreurs : 75 ; latence p50/p95 : 220.9/1,518.4 ms
- Rafraîchissements d'état : 8795 ; âge des données au dernier bloc : 5.25 s ; changements de frais LP observés (pools à frais dynamiques) : 6298
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 68525 ; cycles déclenchés par événement : 7911 ; avance médiane sur le rafraîchissement multicall : 464 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,240.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 503 pools, 290 jetons, 18766 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 115, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3730 (énumérés 320, par paires 0), mesurés 506, sous le plancher de 10000.0 $ : 3 → gardés 503 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2240.565044, 'cbBTC': 77162.459811, 'AERO': 0.625673}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,205,071 | 2,240.570806 | 53328454 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,994,036 | 0.029004 | 53328454 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,284,958 | 0.000013 | 53328454 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,014,746 | 0.029060 | 53328454 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,854,923 | 2,243.237410 | 53328454 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,721,298 | 99.859074 | 53328454 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,673,933 | 0.001615 | 53328454 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,823,990 | 1.611141 | 53328454 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,282,913 | 0.029003 | 53328454 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,136,663 | 2,243.057747 | 53328454 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,120,702 | 2,243.211640 | 53328454 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,062,340 | 1.000001 | 53328454 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,529,158 | 37,722.797016 | 53328454 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,747,321 | 0.029040 | 53328454 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,345,183 | 99.839657 | 53328454 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,056,202 | 1,203,801.785954 | 53328454 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,976,197 | 0.000013 | 53328454 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,751,362 | 0.000000 | 53328454 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,723,591 | 0.017498 | 53328454 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,680,227 | 421.847583 | 53328454 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,640,125 | 0.000013 | 53328454 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,590,830 | 2,242.865205 | 53328454 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,579,003 | 0.000013 | 53328454 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,542,998 | 1.498770 | 53328454 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/USDC | 3000 | 1,522,877 | 2,249.552126 | 53328454 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,812 | 0.826388 | 53328454 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,425,809 | 0.000013 | 53328454 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,402,933 | 3,614.265288 | 53328454 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,358,169 | 2,243.141447 | 53328454 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,325,589 | 0.005209 | 53328454 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,302,345 | 14,553.860161 | 53328454 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,176,798 | 70.167929 | 53328454 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,844 | 35,684,096.582832 | 53328454 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,057,450 | 514,970.441257 | 53328454 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,029,849 | 21,273,057.667850 | 53328454 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,022,187 | 0.000000 | 53328454 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,015,778 | 74,307.183138 | 53328454 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,046 | 19.276745 | 53328454 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 964,538 | 100.539018 | 53328454 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 957,207 | 0.044510 | 53328454 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 949,590 | 69.425179 | 53328454 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 930,092 | 1,213,316.923184 | 53328454 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,025 | 2,235.963257 | 53328454 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 906,970 | 1,050.616809 | 53328454 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 860,193 | 3,588.493993 | 53328454 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 860,009 | 0.000552 | 53328454 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4590 | 847,118 | 19.115922 | 53328454 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 830,202 | 0.062083 | 53328454 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,760 | 0.802842 | 53328454 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 724,106 | 0.000257 | 53328454 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 722,180 | 4,547,737.643344 | 53328454 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 709,290 | 0.577359 | 53328454 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 679,709 | 0.000008 | 53328454 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 661,280 | 144,774.244799 | 53328454 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 659,457 | 2.334749 | 53328454 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 656,584 | 517,309.279385 | 53328454 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 626,340 | 0.496279 | 53328454 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 614,937 | 0.093637 | 53328454 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 602,058 | 0.916277 | 53328454 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 548,546 | 1,050.916024 | 53328454 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 16705 ; routes examinées : 313486030 ; candidats optimisés : 818581 ; net attendu > 0 : 772 ; dernier cycle 213.2 ms
- Rejets (moteur) : {'spread_below_threshold': 307044800, 'liquidity_below_min': 5118385, 'negative_expected_net': 817809, 'pool_quarantined': 453450, 'unquotable': 33394, 'borrow_bound_too_small': 16701, 'cycle_budget_exhausted': 719}
- Enregistrements de la session : 818581 ; net attendu > 0 : 772 ; simulés (eth_call de la vraie tx) : 49 (ok 24, échec 25) ; étiquettes ghost N+1 : 6/34 positives
- Décisions : {'REJECTED': 818581} ; motifs de rejet : {'below_safety_margin': 241, 'negative_expected_net': 817809, 'p_lower_below_threshold': 578, 'price_impact': 14, 'reliability_not_demonstrated': 194, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 25, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53324104 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 3.817698 WETH | 0.071890 WETH | 0.000000 WETH | 0.000002 WETH | 0.071888 WETH (148.1834 €) | — | 188.30 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53324104 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 5.248679 WETH | 0.062852 WETH | 0.000000 WETH | 0.000003 WETH | 0.062849 WETH (129.5514 €) | — | 119.74 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53324104 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 1.089365 WETH | 0.010528 WETH | 0.000000 WETH | 0.000004 WETH | 0.010524 WETH (21.6939 €) | — | 96.61 | 0.000 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53324104 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,439.739245 USDC | 23.583335 USDC | 0.000000 USDC | 0.008435 USDC | 23.574900 USDC (21.6889 €) | — | 96.63 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 1.082016 WETH | 0.010414 WETH | 0.000000 WETH | 0.000003 WETH | 0.010410 WETH (21.4589 €) | — | 96.21 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 2,422.871204 USDC | 23.324238 USDC | 0.000000 USDC | 0.007755 USDC | 23.316483 USDC (21.4512 €) | — | 96.23 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.995732 WETH | 0.009811 WETH | 0.000000 WETH | 0.000005 WETH | 0.009806 WETH (20.2133 €) | — | 98.48 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 2,226.266499 USDC | 21.940137 USDC | 0.000000 USDC | 0.010476 USDC | 21.929661 USDC (20.1753 €) | — | 98.50 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 1.037266 WETH | 0.009699 WETH | 0.000000 WETH | 0.000004 WETH | 0.009695 WETH (19.9842 €) | — | 93.47 | 0.000 (n=32) | REJECTED | stale_data(4008ms>4000.0), p_lower_below_threshold(0.00<0.75) |
| 53324104 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,320.615737 USDC | 21.704974 USDC | 0.000000 USDC | 0.008095 USDC | 21.696879 USDC (19.9611 €) | — | 93.50 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 2,316.317036 USDC | 21.208234 USDC | 0.000000 USDC | 0.007755 USDC | 21.200479 USDC (19.5044 €) | — | 91.53 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.545795 WETH | 0.005120 WETH | 0.000000 WETH | 0.000004 WETH | 0.005116 WETH (10.5454 €) | — | 93.73 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 1,210.383412 USDC | 11.359412 USDC | 0.000000 USDC | 0.008775 USDC | 11.350637 USDC (10.4426 €) | — | 93.78 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→WETH | 0.272298 WETH | 0.003771 WETH | 0.000000 WETH | 0.000002 WETH | 0.003769 WETH (7.7686 €) | — | 138.41 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53324104 | WETH→[uniswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.458692 WETH | 0.003637 WETH | 0.000000 WETH | 0.000002 WETH | 0.003635 WETH (7.4936 €) | — | 79.25 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53324104 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.216771 WETH | 0.002927 WETH | 0.000000 WETH | 0.000003 WETH | 0.002924 WETH (6.0264 €) | — | 134.87 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 477.747777 USDC | 6.457178 USDC | 0.000000 USDC | 0.007755 USDC | 6.449423 USDC (5.9335 €) | — | 135.00 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53324104 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.260437 WETH | 0.002669 WETH | 0.000000 WETH | 0.000002 WETH | 0.002667 WETH (5.4967 €) | — | 102.39 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53324104 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.161081 WETH | 0.002223 WETH | 0.000000 WETH | 0.000002 WETH | 0.002220 WETH (4.5771 €) | — | 137.85 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53324104 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.209942 WETH | 0.001712 WETH | 0.000000 WETH | 0.000003 WETH | 0.001709 WETH (3.5229 €) | — | 81.41 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 53324104 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→USDC | 470.191877 USDC | 3.835436 USDC | 0.000000 USDC | 0.006425 USDC | 3.829011 USDC (3.5227 €) | — | 81.44 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 53324104 | WETH→[uniswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.123722 WETH | 0.001682 WETH | 0.000000 WETH | 0.000002 WETH | 0.001680 WETH (3.4629 €) | — | 135.78 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53324104 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→USDC | 463.979756 USDC | 3.734604 USDC | 0.000000 USDC | 0.006425 USDC | 3.728179 USDC (3.4299 €) | — | 80.35 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 53324104 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.207012 WETH | 0.001667 WETH | 0.000000 WETH | 0.000003 WETH | 0.001664 WETH (3.4293 €) | — | 80.37 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 53324104 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→USDC | 463.146437 USDC | 3.722987 USDC | 0.000000 USDC | 0.006425 USDC | 3.716562 USDC (3.4192 €) | — | 80.25 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3941 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
