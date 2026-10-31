# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T21:12:39+00:00 ; durée 203.62 min ; blocs 53339794 → 53345902 (5982 vus)

## Connexion
- Requêtes RPC : 70476 ; erreurs : 0 ; latence p50/p95 : 110.6/1,058.3 ms
- Rafraîchissements d'état : 5983 ; âge des données au dernier bloc : 1.05 s ; changements de frais LP observés (pools à frais dynamiques) : 5171
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 37765 ; cycles déclenchés par événement : 6018 ; avance médiane sur le rafraîchissement multicall : 366 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,249.72 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 506 pools, 291 jetons, 18722 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 115, aerodrome 206, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 179 (rejetés 2) → 584 jetons ; pools candidats 3790 (énumérés 319, par paires 0), mesurés 509, sous le plancher de 10000.0 $ : 3 → gardés 506 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2248.577307, 'cbBTC': 77558.902259, 'AERO': 0.633591}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,236,939 | 2,249.715851 | 53345902 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,057,668 | 0.029082 | 53345902 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,294,540 | 0.000013 | 53345902 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,043,758 | 0.029054 | 53345902 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,852,126 | 2,250.462570 | 53345902 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,827,506 | 97.885211 | 53345902 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,675,065 | 0.001612 | 53345902 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,731,096 | 1.569062 | 53345902 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,242,129 | 0.029089 | 53345902 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,073,049 | 0.998849 | 53345902 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,052,606 | 2,249.973403 | 53345902 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,944,095 | 2,250.076579 | 53345902 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,537,353 | 37,855.222382 | 53345902 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,684,193 | 0.029042 | 53345902 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,394,023 | 97.887244 | 53345902 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,067,547 | 1,200,366.119818 | 53345902 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,966,139 | 0.000013 | 53345902 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,757,017 | 0.000000 | 53345902 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,719,336 | 0.017431 | 53345902 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,654,561 | 0.000013 | 53345902 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,594,107 | 2,251.717747 | 53345902 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,581,315 | 0.000013 | 53345902 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,547,077 | 424.044902 | 53345902 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,546,920 | 1.490152 | 53345902 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,362 | 0.825821 | 53345902 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,425,034 | 3,528.914635 | 53345902 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,407,142 | 2,256.217679 | 53345902 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,344,303 | 2,250.516012 | 53345902 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,325,137 | 0.005206 | 53345902 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,303,390 | 0.000013 | 53345902 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,302,867 | 14,593.455587 | 53345902 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,174,224 | 70.475891 | 53345902 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,164,330 | 31,627,538.921171 | 53345902 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,062,040 | 515,516.073656 | 53345902 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,041,607 | 0.000000 | 53345902 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,024,639 | 21,643,590.881841 | 53345902 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,003,510 | 76,720.421691 | 53345902 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 991,435 | 19.424339 | 53345902 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 990,867 | 97.190095 | 53345902 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 975,215 | 0.043533 | 53345902 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 964,239 | 67.332088 | 53345902 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 949,696 | 941.542265 | 53345902 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/WELL | 10000 | 944,979 | 1,184,992.028350 | 53345902 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 922,994 | 2,236.005346 | 53345902 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 872,915 | 3,505.733206 | 53345902 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,090 | 0.000552 | 53345902 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 840,128 | 19.363711 | 53345902 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 834,172 | 0.062745 | 53345902 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 761,751 | 0.803065 | 53345902 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 733,577 | 0.000262 | 53345902 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,532 | 0.590422 | 53345902 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 721,385 | 4,595,375.433790 | 53345902 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 689,918 | 0.000008 | 53345902 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 671,434 | 141,586.134358 | 53345902 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 658,619 | 518,450.321938 | 53345902 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 656,655 | 2.335254 | 53345902 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 646,005 | 0.526413 | 53345902 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 615,398 | 0.093728 | 53345902 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 603,606 | 0.916826 | 53345902 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 555,821 | 941.757390 | 53345902 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 12000 ; routes examinées : 224664000 ; candidats optimisés : 822724 ; net attendu > 0 : 445 ; dernier cycle 77.1 ms
- Rejets (moteur) : {'spread_below_threshold': 221076238, 'liquidity_below_min': 2547522, 'negative_expected_net': 822279, 'pool_quarantined': 181440, 'unquotable': 23998, 'borrow_bound_too_small': 11999, 'cycle_budget_exhausted': 79}
- Enregistrements de la session : 822724 ; net attendu > 0 : 445 ; simulés (eth_call de la vraie tx) : 65 (ok 6, échec 59) ; étiquettes ghost N+1 : 0/44 positives
- Décisions : {'REJECTED': 822724} ; motifs de rejet : {'below_safety_margin': 190, 'negative_expected_net': 822279, 'p_lower_below_threshold': 438, 'price_impact': 12, 'reliability_not_demonstrated': 7, 'simulation_failed': 59}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53341420 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 435.572012 USDC | 0.677533 USDC | 0.000000 USDC | 0.007105 USDC | 0.670428 USDC (0.6168 €) | — | 15.39 | 0.069 (n=97) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341420 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005357 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6154 €) | — | 16.13 | 0.069 (n=97) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341420 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 370.493614 USDC | 0.511152 USDC | 0.000000 USDC | 0.006764 USDC | 0.504388 USDC (0.4640 €) | — | 13.61 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53341420 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004550 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4623 €) | — | 14.26 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53341422 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 279.859953 USDC | 0.484356 USDC | 0.000000 USDC | 0.007447 USDC | 0.476909 USDC (0.4388 €) | — | 17.04 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341422 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.124368 WETH | 0.000215 WETH | 0.000000 WETH | 0.000003 WETH | 0.000211 WETH (0.4377 €) | — | 17.00 | 0.067 (n=100) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53341422 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 279.868114 USDC | 0.482925 USDC | 0.000000 USDC | 0.007447 USDC | 0.475478 USDC (0.4374 €) | — | 16.99 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341422 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.124316 WETH | 0.000214 WETH | 0.000000 WETH | 0.000003 WETH | 0.000211 WETH (0.4364 €) | — | 16.96 | 0.067 (n=100) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53341420 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 276.446817 USDC | 0.470563 USDC | 0.000000 USDC | 0.007105 USDC | 0.463458 USDC (0.4264 €) | — | 16.76 | 0.069 (n=97) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341420 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.122776 WETH | 0.000209 WETH | 0.000000 WETH | 0.000003 WETH | 0.000205 WETH (0.4252 €) | — | 16.73 | 0.069 (n=97) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53341420 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 363.045231 USDC | 0.459632 USDC | 0.000000 USDC | 0.006764 USDC | 0.452868 USDC (0.4166 €) | — | 12.47 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53341420 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004325 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4160 €) | — | 13.50 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53341420 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 261.579763 USDC | 0.456485 USDC | 0.000000 USDC | 0.007105 USDC | 0.449380 USDC (0.4134 €) | — | 17.18 | 0.069 (n=97) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341420 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.116197 WETH | 0.000202 WETH | 0.000000 WETH | 0.000003 WETH | 0.000199 WETH (0.4122 €) | — | 17.14 | 0.069 (n=97) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53341420 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 270.343549 USDC | 0.450823 USDC | 0.000000 USDC | 0.007105 USDC | 0.443718 USDC (0.4082 €) | — | 16.41 | 0.069 (n=97) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341420 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.119920 WETH | 0.000200 WETH | 0.000000 WETH | 0.000003 WETH | 0.000197 WETH (0.4071 €) | — | 16.40 | 0.069 (n=97) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53341420 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 343.529594 USDC | 0.436126 USDC | 0.000000 USDC | 0.006764 USDC | 0.429362 USDC (0.3950 €) | — | 12.50 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53341420 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.004312 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.3939 €) | — | 12.83 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53341422 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 252.270714 USDC | 0.424966 USDC | 0.000000 USDC | 0.007788 USDC | 0.417178 USDC (0.3838 €) | — | 16.54 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341422 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.112101 WETH | 0.000189 WETH | 0.000000 WETH | 0.000003 WETH | 0.000185 WETH (0.3830 €) | — | 16.51 | 0.067 (n=100) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53341420 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 255.713627 USDC | 0.402255 USDC | 0.000000 USDC | 0.007105 USDC | 0.395150 USDC (0.3635 €) | — | 15.45 | 0.069 (n=97) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341420 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.113542 WETH | 0.000178 WETH | 0.000000 WETH | 0.000003 WETH | 0.000175 WETH (0.3625 €) | — | 15.42 | 0.069 (n=97) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341420 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 247.825595 USDC | 0.376971 USDC | 0.000000 USDC | 0.006764 USDC | 0.370207 USDC (0.3406 €) | — | 14.94 | 0.069 (n=97) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341420 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.110057 WETH | 0.000167 WETH | 0.000000 WETH | 0.000003 WETH | 0.000164 WETH (0.3396 €) | — | 14.91 | 0.069 (n=97) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53341422 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 308.565124 USDC | 0.373619 USDC | 0.000000 USDC | 0.007447 USDC | 0.366172 USDC (0.3369 €) | — | 11.87 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |

## Fiabilité et décision
- Observations ghost : 4014 ; taux observé 0.128 ; borne inférieure crédible (0.9) 0.121 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
