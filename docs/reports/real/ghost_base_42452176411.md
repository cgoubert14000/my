# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T06:43:01+00:00 ; durée 48.85 min ; blocs 54634334 → 54648961 (2233 vus)

## Connexion
- Requêtes RPC : 29232 ; erreurs : 0 ; latence p50/p95 : 315.0/2,093.1 ms
- Rafraîchissements d'état : 2233 ; âge des données au dernier bloc : 12.99 s ; changements de frais LP observés (pools à frais dynamiques) : 373
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1336 ; cycles déclenchés par événement : 595 ; avance médiane sur le rafraîchissement multicall : 447 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,231.65 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 470 pools, 276 jetons, 17708 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 96, aerodrome 197, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3668 (énumérés 291, par paires 0), mesurés 473, sous le plancher de 10000.0 $ : 3 → gardés 470 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2231.640985, 'cbBTC': 75743.146723, 'AERO': 0.606566}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,581,678 | 2,231.646842 | 54648997 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,843,860 | 0.029473 | 54648997 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,255,262 | 0.000013 | 54648997 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,152,604 | 0.029508 | 54648997 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,085,378 | 2,231.017883 | 54648997 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,272,535 | 110.018832 | 54648997 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,382,822 | 0.001538 | 54648997 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,142,433 | 0.029461 | 54648997 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,874,096 | 1.648626 | 54648997 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,185,276 | 2,230.047286 | 54648997 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,985,329 | 0.999186 | 54648997 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,301,693 | 42,755.564539 | 54648997 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,179,086 | 2,230.266122 | 54648997 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,542,160 | 0.029493 | 54648997 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,096,789 | 1,148,252.607284 | 54648997 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,737,092 | 0.000013 | 54648997 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,659,096 | 0.000013 | 54648997 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,635,470 | 0.006465 | 54648997 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,615,852 | 0.000000 | 54648997 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,568,132 | 0.015534 | 54648997 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,515,657 | 444.391211 | 54648997 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,503,459 | 0.000013 | 54648997 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,469,420 | 1.434825 | 54648997 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,111 | 0.819634 | 54648997 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,392,591 | 3,679.299705 | 54648997 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,943 | 2,236.842160 | 54648997 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,294,991 | 2,236.928659 | 54648997 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,259,365 | 15,095.282760 | 54648997 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,182,408 | 2,230.984909 | 54648997 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,406 | 76.995559 | 54648997 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,096,907 | 36,897,109.812634 | 54648997 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,032,324 | 109.375213 | 54648997 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,007,464 | 583,706.493145 | 54648997 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 983,211 | 22,962,402.940198 | 54648997 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 973,535 | 20.498526 | 54648997 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 959,051 | 0.000000 | 54648997 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,580 | 2,228.787514 | 54648997 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 931,763 | 1,067.597849 | 54648997 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 930,331 | 72.399026 | 54648997 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 924,916 | 0.000013 | 54648997 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 862,492 | 102,066.314044 | 54648997 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 807,923 | 0.049271 | 54648997 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 788,916 | 3,655.317486 | 54648997 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 783,682 | 0.054909 | 54648997 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 779,381 | 21.683576 | 54648997 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 757,028 | 0.799805 | 54648997 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 713,255 | 0.563097 | 54648997 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 685,274 | 5,019,668.013903 | 54648997 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 681,407 | 0.000253 | 54648997 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 672,233 | 0.570490 | 54648997 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 656,883 | 0.000008 | 54648997 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 638,313 | 154,560.936201 | 54648997 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 613,145 | 589,131.464060 | 54648997 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 579,157 | 0.039785 | 54648997 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 553,876 | 2.471830 | 54648997 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 522,491 | 894,410.224564 | 54648997 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 521,714 | 1,067.652616 | 54648997 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/USDC | 100 | 514,118 | 2,230.289662 | 54648997 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 512,214 | 6,961.189379 | 54648997 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 510,465 | 0.075509 | 54648997 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 2827 ; routes examinées : 50060516 ; candidats optimisés : 148795 ; net attendu > 0 : 63 ; dernier cycle 134.7 ms
- Rejets (moteur) : {'spread_below_threshold': 49186414, 'liquidity_below_min': 724452, 'negative_expected_net': 148732, 'cycle_budget_exhausted': 855}
- Enregistrements de la session : 148795 ; net attendu > 0 : 63 ; simulés (eth_call de la vraie tx) : 4 (ok 0, échec 4) ; étiquettes ghost N+1 : 1/4 positives
- Décisions : {'REJECTED': 148795} ; motifs de rejet : {'below_safety_margin': 58, 'negative_expected_net': 148732, 'p_lower_below_threshold': 63, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54648584 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000853 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0188 €) | — | 3.17 | 0.153 (n=840) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 54648584 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 78.274107 USDC | 0.026927 USDC | 0.000000 USDC | 0.006705 USDC | 0.020222 USDC (0.0186 €) | — | 2.58 | 0.182 (n=1069) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 54642625 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 46.249502 USDC | 0.023758 USDC | 0.000000 USDC | 0.005011 USDC | 0.018747 USDC (0.0172 €) | — | 4.05 | 0.028 (n=353) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54648584 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000902 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0160 €) | — | 2.55 | 0.241 (n=418) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54648584 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 68.340174 USDC | 0.024013 USDC | 0.000000 USDC | 0.006705 USDC | 0.017308 USDC (0.0159 €) | — | 2.53 | 0.241 (n=418) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.24<0.75) |
| 54648584 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 54.363118 USDC | 0.012205 USDC | 0.000000 USDC | 0.006705 USDC | 0.005500 USDC (0.0051 €) | — | 1.01 | 0.241 (n=418) | REJECTED | below_safety_margin(5500<10872), p_lower_below_threshold(0.24<0.75) |
| 54648584 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000493 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0049 €) | — | 1.42 | 0.241 (n=418) | REJECTED | below_safety_margin(7<9), p_lower_below_threshold(0.24<0.75) |
| 54648584 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000493 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.41 | 0.241 (n=418) | REJECTED | below_safety_margin(2<9), p_lower_below_threshold(0.24<0.75) |
| 54648532 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.241 (n=418) | REJECTED | below_safety_margin(527299026272<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648531 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.241 (n=418) | REJECTED | below_safety_margin(527299026272<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648532 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.241 (n=418) | REJECTED | below_safety_margin(527299026272<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648582 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.241 (n=418) | REJECTED | below_safety_margin(527299026272<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648584 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.241 (n=418) | REJECTED | below_safety_margin(527299026272<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648583 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.241 (n=418) | REJECTED | below_safety_margin(527226560374<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648584 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.241 (n=418) | REJECTED | below_safety_margin(527226560374<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648620 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.240 (n=419) | REJECTED | below_safety_margin(527226560374<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648621 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.240 (n=419) | REJECTED | below_safety_margin(527226560374<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648621 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.240 (n=419) | REJECTED | below_safety_margin(527226560374<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648622 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.240 (n=419) | REJECTED | below_safety_margin(527226560374<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648623 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003962 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.33 | 0.240 (n=419) | REJECTED | below_safety_margin(527226560374<792325961252), p_lower_below_threshold(0.24<0.75) |
| 54648532 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.795229 USDC | 0.007880 USDC | 0.000000 USDC | 0.006705 USDC | 0.001175 USDC (0.0011 €) | — | 1.34 | 0.241 (n=418) | REJECTED | below_safety_margin(1175<1759), p_lower_below_threshold(0.24<0.75) |
| 54648531 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.795229 USDC | 0.007880 USDC | 0.000000 USDC | 0.006705 USDC | 0.001175 USDC (0.0011 €) | — | 1.34 | 0.241 (n=418) | REJECTED | below_safety_margin(1175<1759), p_lower_below_threshold(0.24<0.75) |
| 54648532 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.795229 USDC | 0.007880 USDC | 0.000000 USDC | 0.006705 USDC | 0.001175 USDC (0.0011 €) | — | 1.34 | 0.241 (n=418) | REJECTED | below_safety_margin(1175<1759), p_lower_below_threshold(0.24<0.75) |
| 54648582 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.795229 USDC | 0.007880 USDC | 0.000000 USDC | 0.006705 USDC | 0.001175 USDC (0.0011 €) | — | 1.34 | 0.241 (n=418) | REJECTED | below_safety_margin(1175<1759), p_lower_below_threshold(0.24<0.75) |
| 54648584 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.795229 USDC | 0.007880 USDC | 0.000000 USDC | 0.006705 USDC | 0.001175 USDC (0.0011 €) | — | 1.34 | 0.241 (n=418) | REJECTED | below_safety_margin(1175<1759), p_lower_below_threshold(0.24<0.75) |

## Fiabilité et décision
- Observations ghost : 6143 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
