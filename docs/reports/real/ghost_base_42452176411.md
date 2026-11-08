# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T07:22:54+00:00 ; durée 88.74 min ; blocs 54634334 → 54660941 (3884 vus)

## Connexion
- Requêtes RPC : 50603 ; erreurs : 0 ; latence p50/p95 : 216.6/1,533.3 ms
- Rafraîchissements d'état : 3884 ; âge des données au dernier bloc : 9.43 s ; changements de frais LP observés (pools à frais dynamiques) : 753
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2662 ; cycles déclenchés par événement : 1088 ; avance médiane sur le rafraîchissement multicall : 337 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,231.65 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 470 pools, 276 jetons, 17708 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 96, aerodrome 197, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3668 (énumérés 291, par paires 0), mesurés 473, sous le plancher de 10000.0 $ : 3 → gardés 470 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2231.640985, 'cbBTC': 75743.146723, 'AERO': 0.606566}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,691,955 | 2,231.645885 | 54660970 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,845,316 | 0.029466 | 54660970 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,256,026 | 0.000013 | 54660970 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,145,965 | 0.029508 | 54660970 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,090,386 | 2,232.787831 | 54660970 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,288,489 | 109.537614 | 54660970 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,384,430 | 0.001538 | 54660970 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,142,921 | 0.029471 | 54660970 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,872,887 | 1.649444 | 54660970 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,235,346 | 2,233.135954 | 54660970 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,986,308 | 0.999186 | 54660970 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,301,053 | 42,772.111268 | 54660970 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,179,087 | 2,232.974394 | 54660970 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,542,356 | 0.029493 | 54660970 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,096,788 | 1,148,252.607284 | 54660970 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,737,397 | 0.000013 | 54660970 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,659,409 | 0.000013 | 54660970 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,635,461 | 0.006465 | 54660970 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,615,852 | 0.000000 | 54660970 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,570,989 | 0.015574 | 54660970 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,515,135 | 444.889664 | 54660970 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,503,703 | 0.000013 | 54660970 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,469,419 | 1.434827 | 54660970 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,111 | 0.819634 | 54660970 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,392,175 | 3,679.299705 | 54660970 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,942 | 2,236.514771 | 54660970 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,294,991 | 2,238.907575 | 54660970 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,258,919 | 15,095.282760 | 54660970 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,182,410 | 2,232.754217 | 54660970 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,406 | 76.995559 | 54660970 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,092,861 | 36,897,109.812634 | 54660970 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,032,140 | 109.375224 | 54660970 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,006,273 | 585,765.724206 | 54660970 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 982,281 | 22,999,292.916458 | 54660970 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 973,503 | 20.500518 | 54660970 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 965,046 | 0.000000 | 54660970 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,580 | 2,228.787514 | 54660970 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 931,994 | 1,067.243122 | 54660970 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 930,363 | 72.394168 | 54660970 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 925,111 | 0.000013 | 54660970 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 860,519 | 102,534.635354 | 54660970 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 810,861 | 0.049032 | 54660970 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 788,720 | 3,655.317486 | 54660970 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 784,856 | 0.055082 | 54660970 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 779,381 | 21.683576 | 54660970 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 757,027 | 0.799805 | 54660970 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 713,255 | 0.563097 | 54660970 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 684,808 | 5,026,519.346429 | 54660970 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 681,407 | 0.000253 | 54660970 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 672,231 | 0.570486 | 54660970 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 656,768 | 0.000008 | 54660970 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 637,914 | 154,754.489515 | 54660970 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 612,014 | 589,948.481589 | 54660970 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 578,981 | 0.039766 | 54660970 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 553,908 | 2.471618 | 54660970 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 522,530 | 894,409.486788 | 54660970 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 521,861 | 1,067.125350 | 54660970 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/USDC | 100 | 514,146 | 2,233.146827 | 54660970 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 511,931 | 6,968.880160 | 54660970 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 509,119 | 0.075239 | 54660970 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 4971 ; routes examinées : 88026468 ; candidats optimisés : 253518 ; net attendu > 0 : 65 ; dernier cycle 64.3 ms
- Rejets (moteur) : {'spread_below_threshold': 86464211, 'liquidity_below_min': 1307432, 'negative_expected_net': 253453, 'cycle_budget_exhausted': 1307}
- Enregistrements de la session : 253518 ; net attendu > 0 : 65 ; simulés (eth_call de la vraie tx) : 6 (ok 0, échec 6) ; étiquettes ghost N+1 : 1/6 positives
- Décisions : {'REJECTED': 253518} ; motifs de rejet : {'below_safety_margin': 58, 'negative_expected_net': 253453, 'p_lower_below_threshold': 65, 'simulation_failed': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54648584 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000853 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0188 €) | — | 3.17 | 0.153 (n=840) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 54648584 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 78.274107 USDC | 0.026927 USDC | 0.000000 USDC | 0.006705 USDC | 0.020222 USDC (0.0186 €) | — | 2.58 | 0.182 (n=1069) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 54642625 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 46.249502 USDC | 0.023758 USDC | 0.000000 USDC | 0.005011 USDC | 0.018747 USDC (0.0172 €) | — | 4.05 | 0.028 (n=353) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54648584 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000902 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0160 €) | — | 2.55 | 0.241 (n=418) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54648584 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 68.340174 USDC | 0.024013 USDC | 0.000000 USDC | 0.006705 USDC | 0.017308 USDC (0.0159 €) | — | 2.53 | 0.241 (n=418) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.24<0.75) |
| 54650025 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 22.109994 USDC | 0.013877 USDC | 0.000000 USDC | 0.005010 USDC | 0.008867 USDC (0.0082 €) | — | 4.01 | 0.030 (n=354) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54648584 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 54.363118 USDC | 0.012205 USDC | 0.000000 USDC | 0.006705 USDC | 0.005500 USDC (0.0051 €) | — | 1.01 | 0.241 (n=418) | REJECTED | below_safety_margin(5500<10872), p_lower_below_threshold(0.24<0.75) |
| 54648584 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000493 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0049 €) | — | 1.42 | 0.241 (n=418) | REJECTED | below_safety_margin(7<9), p_lower_below_threshold(0.24<0.75) |
| 54649614 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 13.657340 USDC | 0.008114 USDC | 0.000000 USDC | 0.005010 USDC | 0.003104 USDC (0.0029 €) | — | 2.27 | 0.051 (n=85) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
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

## Fiabilité et décision
- Observations ghost : 6145 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
