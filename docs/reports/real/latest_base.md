# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T15:49:11+00:00 ; durée 290.47 min ; blocs 56453704 → 56540800 (8800 vus)

## Connexion
- Requêtes RPC : 162658 ; erreurs : 20 ; latence p50/p95 : 286.0/1,352.8 ms
- Rafraîchissements d'état : 8800 ; âge des données au dernier bloc : 8.34 s ; changements de frais LP observés (pools à frais dynamiques) : 13606
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11548 ; cycles déclenchés par événement : 2720 ; avance médiane sur le rafraîchissement multicall : 566 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,998.44 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 456 pools, 265 jetons, 15214 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 458, sous le plancher de 10000.0 $ : 2 → gardés 456 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2045.271447, 'cbBTC': 73394.102525, 'AERO': 0.529681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 131,967,831 | 1,998.440956 | 56540820 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,169,247 | 0.028024 | 56540820 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,626,349 | 0.000014 | 56540820 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,471,707 | 0.027991 | 56540820 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 6,936,801 | 1,998.989323 | 56540820 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,632,795 | 105.769081 | 56540820 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,169,129 | 0.028032 | 56540820 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,115,549 | 1.952867 | 56540820 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,096,144 | 1,998.392036 | 56540820 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,757,809 | 0.998540 | 56540820 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,964,430 | 42,531.560113 | 56540820 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 100 | 2,788,420 | 1,998.557540 | 56540820 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,140,492 | 0.028003 | 56540820 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,872,807 | 1,154,230.850464 | 56540820 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,643,018 | 0.016716 | 56540820 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,599,650 | 0.000014 | 56540820 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,555,592 | 0.000014 | 56540820 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,520,364 | 0.000000 | 56540820 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,467,051 | 0.000014 | 56540820 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,959 | 0.831291 | 56540820 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,463,122 | 0.006482 | 56540820 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,366,503 | 431.747991 | 56540820 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,253,630 | 1,999.108601 | 56540820 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,203,810 | 3,905.830942 | 56540820 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,176,117 | 15,422.368494 | 56540820 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,140,175 | 1,998.448666 | 56540820 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,084,956 | 1,998.846436 | 56540820 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,177 | 86.290648 | 56540820 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,047,058 | 1.389298 | 56540820 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,008,229 | 34,284,591.641183 | 56540820 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 978,098 | 106.369932 | 56540820 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,132 | 21.312775 | 56540820 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 912,065 | 564,591.945075 | 56540820 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 887,131 | 0.001491 | 56540820 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 875,120 | 23,229,511.263151 | 56540820 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 871,264 | 0.000014 | 56540820 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 870,324 | 0.052886 | 56540820 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 866,591 | 2,001.746817 | 56540820 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 859,397 | 1,014.554436 | 56540820 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 832,224 | 0.000000 | 56540820 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 766,524 | 80.053667 | 56540820 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 741,105 | 0.048915 | 56540820 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 732,915 | 23.656178 | 56540820 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 677,257 | 3,918.532711 | 56540820 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 677,074 | 0.801801 | 56540820 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 646,876 | 0.508007 | 56540820 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 629,354 | 4,781,170.221462 | 56540820 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 589,232 | 0.438208 | 56540820 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/EDEL | 7000 | 571,661 | 186,300.008634 | 56540820 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/NPC | 3000 | 570,596 | 155,496.245667 | 56540820 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2150 | 559,094 | 566,234.083859 | 56540820 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | VIRTUAL/WETH | 10000 | 558,399 | 0.000255 | 56540820 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 549,169 | 0.000007 | 56540820 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 546,888 | 0.036587 | 56540820 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 479,370 | 1,014.439195 | 56540820 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 464,361 | 0.066835 | 56540820 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 11 | 450,216 | 1.001151 | 56540820 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 442,503 | 0.505910 | 56540820 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 425,998 | 24.864112 | 56540820 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 421,734 | 923,590.709229 | 56540820 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 11519 ; routes examinées : 175250066 ; candidats optimisés : 956301 ; net attendu > 0 : 2806 ; dernier cycle 120.2 ms
- Rejets (moteur) : {'spread_below_threshold': 171177504, 'liquidity_below_min': 3090306, 'negative_expected_net': 953495, 'pool_quarantined': 10990, 'borrow_bound_too_small': 7941, 'cycle_budget_exhausted': 7024}
- Enregistrements de la session : 956301 ; net attendu > 0 : 2806 ; simulés (eth_call de la vraie tx) : 141 (ok 93, échec 48) ; étiquettes ghost N+1 : 55/117 positives
- Décisions : {'REJECTED': 956301} ; motifs de rejet : {'below_safety_margin': 1885, 'negative_expected_net': 953495, 'p_lower_below_threshold': 2743, 'price_impact': 27, 'reliability_not_demonstrated': 63, 'sim_below_estimate': 16, 'simulated_net_nonpositive': 15, 'simulation_failed': 48, 'stale_data': 1339}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56493120 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.469193 WETH | 0.000388 WETH | 0.000000 WETH | 0.000004 WETH | 0.000385 WETH (0.7073 €) | 0.000385 WETH | 8.20 | 0.007 (n=116) | REJECTED | stale_data(5394ms>4000.0), p_lower_below_threshold(0.01<0.75) |
| 56493120 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 934.056366 USDC | 0.773536 USDC | 0.000000 USDC | 0.007430 USDC | 0.766106 USDC (0.7048 €) | — | 8.20 | 0.007 (n=116) | REJECTED | stale_data(5399ms>4000.0), p_lower_below_threshold(0.01<0.75) |
| 56493120 | WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.358780 WETH | 0.000278 WETH | 0.000000 WETH | 0.000004 WETH | 0.000274 WETH (0.5031 €) | 0.000274 WETH | 7.62 | 0.207 (n=1253) | REJECTED | stale_data(5334ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 56493120 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.009565 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5019 €) | — | 7.86 | 0.207 (n=1253) | REJECTED | stale_data(5338ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 56493120 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 730.183805 USDC | 0.552978 USDC | 0.000000 USDC | 0.008224 USDC | 0.544754 USDC (0.5012 €) | — | 7.46 | 0.207 (n=1253) | REJECTED | stale_data(5330ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 56493120 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.359236 WETH | 0.000269 WETH | 0.000000 WETH | 0.000004 WETH | 0.000265 WETH (0.4878 €) | 0.000265 WETH | 7.38 | 0.207 (n=1253) | REJECTED | stale_data(5403ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 56493120 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.009455 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4872 €) | — | 7.72 | 0.207 (n=1253) | REJECTED | stale_data(5407ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 56493120 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 700.522877 USDC | 0.536783 USDC | 0.000000 USDC | 0.008224 USDC | 0.528559 USDC (0.4863 €) | — | 7.55 | 0.207 (n=1253) | REJECTED | stale_data(5411ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 56486832 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 77.387925 USDC | 0.517155 USDC | 0.000000 USDC | 0.004270 USDC | 0.512885 USDC (0.4719 €) | — | 66.27 | 0.000 (n=22) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 56493120 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.327291 WETH | 0.000257 WETH | 0.000000 WETH | 0.000004 WETH | 0.000253 WETH (0.4660 €) | — | 7.74 | 0.207 (n=1253) | REJECTED | stale_data(5364ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 56493120 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.009073 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4659 €) | — | 7.69 | 0.207 (n=1253) | REJECTED | stale_data(5368ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 56493120 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 677.351314 USDC | 0.512648 USDC | 0.000000 USDC | 0.008224 USDC | 0.504424 USDC (0.4641 €) | — | 7.45 | 0.207 (n=1253) | REJECTED | stale_data(5372ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 56534916 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,416.958531 USDC | 0.448629 USDC | 0.000000 USDC | 0.004931 USDC | 0.443698 USDC (0.4082 €) | — | 3.13 | 0.077 (n=498) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 56534916 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.707589 WETH | 0.000224 WETH | 0.000000 WETH | 0.000002 WETH | 0.000221 WETH (0.4076 €) | — | 3.13 | 0.077 (n=498) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 56493120 | WETH→[uniswap_v3]→VVV→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.110035 WETH | 0.000136 WETH | 0.000000 WETH | 0.000004 WETH | 0.000132 WETH (0.2428 €) | — | 11.99 | 0.146 (n=240) | REJECTED | stale_data(5009ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 56493120 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→VVV→[uniswap_v3]→USDC | 219.388625 USDC | 0.270719 USDC | 0.000000 USDC | 0.007829 USDC | 0.262890 USDC (0.2419 €) | — | 11.98 | 0.146 (n=240) | REJECTED | stale_data(5013ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 56493285 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,298.381230 USDC | 0.231055 USDC | 0.000000 USDC | 0.007740 USDC | 0.223315 USDC (0.2054 €) | — | 1.72 | 0.104 (n=368) | REJECTED | below_safety_margin(223315<259676), stale_data(4594ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56493285 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.653008 WETH | 0.000116 WETH | 0.000000 WETH | 0.000004 WETH | 0.000112 WETH (0.2053 €) | — | 1.72 | 0.104 (n=368) | REJECTED | below_safety_margin(112009790710837<130601557229976), stale_data(4588ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56493120 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.097651 WETH | 0.000106 WETH | 0.000000 WETH | 0.000004 WETH | 0.000102 WETH (0.1871 €) | — | 10.42 | 0.146 (n=240) | REJECTED | stale_data(5085ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 56493120 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 194.228897 USDC | 0.210844 USDC | 0.000000 USDC | 0.008224 USDC | 0.202620 USDC (0.1864 €) | — | 10.43 | 0.146 (n=240) | REJECTED | stale_data(5089ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 56493076 | WETH→[uniswap_v3]→USDbC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.048268 WETH | 0.000100 WETH | 0.000000 WETH | 0.000004 WETH | 0.000096 WETH (0.1760 €) | 0.000096 WETH | 19.82 | 0.083 (n=152) | REJECTED | stale_data(4788ms>4000.0), p_lower_below_threshold(0.08<0.75) |
| 56493076 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDbC→[uniswap_v3]→USDC | 96.143377 USDC | 0.199447 USDC | 0.000000 USDC | 0.008327 USDC | 0.191120 USDC (0.1758 €) | — | 19.88 | 0.083 (n=152) | REJECTED | stale_data(4794ms>4000.0), p_lower_below_threshold(0.08<0.75) |
| 56493076 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.047642 WETH | 0.000097 WETH | 0.000000 WETH | 0.000004 WETH | 0.000093 WETH (0.1717 €) | 0.000093 WETH | 19.58 | 0.083 (n=152) | REJECTED | stale_data(4805ms>4000.0), p_lower_below_threshold(0.08<0.75) |
| 56493076 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 94.927839 USDC | 0.194759 USDC | 0.000000 USDC | 0.008327 USDC | 0.186432 USDC (0.1715 €) | — | 19.64 | 0.083 (n=152) | REJECTED | stale_data(4811ms>4000.0), p_lower_below_threshold(0.08<0.75) |
| 56493120 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.003359 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1709 €) | — | 7.62 | 0.207 (n=1253) | REJECTED | stale_data(5315ms>4000.0), p_lower_below_threshold(0.21<0.75) |

## Fiabilité et décision
- Observations ghost : 8384 ; taux observé 0.221 ; borne inférieure crédible (0.9) 0.215 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
