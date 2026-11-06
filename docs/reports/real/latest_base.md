# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T13:58:22+00:00 ; durée 322.97 min ; blocs 53818717 → 53915568 (18404 vus)

## Connexion
- Requêtes RPC : 250244 ; erreurs : 43 ; latence p50/p95 : 232.7/960.1 ms
- Rafraîchissements d'état : 18404 ; âge des données au dernier bloc : 6.49 s ; changements de frais LP observés (pools à frais dynamiques) : 10831
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 14830 ; cycles déclenchés par événement : 6771 ; avance médiane sur le rafraîchissement multicall : 332 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,233.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 484 pools, 281 jetons, 17914 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 103, aerodrome 201, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3751 (énumérés 303, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 3 → gardés 484 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.035754, 'cbBTC': 75513.528915, 'AERO': 0.590274}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,737,307 | 2,233.106878 | 53915587 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,701,890 | 0.029478 | 53915587 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,390,862 | 0.000013 | 53915587 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,139,617 | 0.029445 | 53915587 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,986,405 | 2,233.443413 | 53915587 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,363,793 | 107.469457 | 53915587 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,430,043 | 0.001560 | 53915587 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,881,502 | 1.657803 | 53915587 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,725,083 | 0.029476 | 53915587 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,105,643 | 2,233.454340 | 53915587 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,992,824 | 0.998492 | 53915587 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,297,859 | 42,911.132712 | 53915587 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,200,217 | 2,233.432710 | 53915587 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,554,034 | 0.029463 | 53915587 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,078,024 | 1,170,614.944842 | 53915587 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,795,918 | 0.007333 | 53915587 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,735,536 | 0.000013 | 53915587 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,657,079 | 0.000013 | 53915587 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,645,401 | 0.016570 | 53915587 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,638,044 | 0.000000 | 53915587 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,161 | 1.444757 | 53915587 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,528,249 | 0.000013 | 53915587 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,526,926 | 434.220520 | 53915587 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,679 | 0.818509 | 53915587 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,380,646 | 3,704.529709 | 53915587 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,324,232 | 2,234.729575 | 53915587 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,322,407 | 2,234.820617 | 53915587 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,272,209 | 14,729.097883 | 53915587 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,170,273 | 2,233.373875 | 53915587 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,886 | 76.929838 | 53915587 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,093,458 | 37,269,526.397501 | 53915587 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,046,164 | 107.061342 | 53915587 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,022,742 | 559,380.608527 | 53915587 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,021,145 | 0.000000 | 53915587 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 998,112 | 22,433,261.257503 | 53915587 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 983,584 | 19.882190 | 53915587 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 937,738 | 1,063.718708 | 53915587 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 935,145 | 2,225.576719 | 53915587 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 923,801 | 0.000013 | 53915587 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 900,749 | 77.232523 | 53915587 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 862,634 | 102,226.567997 | 53915587 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 837,990 | 0.000530 | 53915587 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 812,856 | 20.415122 | 53915587 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | USDC/VVV | 3000 | 807,363 | 0.048156 | 53915587 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 796,578 | 3,681.640183 | 53915587 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 794,027 | 0.056448 | 53915587 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 757,573 | 0.799699 | 53915587 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 725,045 | 0.579161 | 53915587 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,316 | 4,894,790.151861 | 53915587 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 688,093 | 0.000257 | 53915587 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 659,620 | 144,875.925403 | 53915587 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 656,770 | 0.541771 | 53915587 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 652,966 | 0.000008 | 53915587 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 627,254 | 555,999.131816 | 53915587 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 598,756 | 0.913997 | 53915587 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 586,925 | 2.472301 | 53915587 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 561,047 | 0.038104 | 53915587 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 531,363 | 0.080067 | 53915587 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 529,593 | 869,633.805833 | 53915587 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 524,654 | 1,062.787079 | 53915587 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 25174 ; routes examinées : 450967036 ; candidats optimisés : 1244932 ; net attendu > 0 : 487 ; dernier cycle 202.3 ms
- Rejets (moteur) : {'spread_below_threshold': 443830469, 'liquidity_below_min': 5865849, 'negative_expected_net': 1244445, 'borrow_bound_too_small': 25165, 'cycle_budget_exhausted': 621}
- Enregistrements de la session : 1244932 ; net attendu > 0 : 487 ; simulés (eth_call de la vraie tx) : 49 (ok 34, échec 15) ; étiquettes ghost N+1 : 6/41 positives
- Décisions : {'REJECTED': 1244932} ; motifs de rejet : {'below_safety_margin': 356, 'negative_expected_net': 1244445, 'p_lower_below_threshold': 460, 'reliability_not_demonstrated': 27, 'simulation_failed': 15, 'stale_data': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53867531 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 270.605872 USDC | 0.904345 USDC | 0.000000 USDC | 0.005034 USDC | 0.899311 USDC (0.8274 €) | 0.899311 USDC | 33.23 | 0.000 (n=18) | REJECTED | stale_data(6459ms>4000.0), reliability_not_demonstrated |
| 53867531 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 270.605872 USDC | 0.904345 USDC | 0.000000 USDC | 0.005034 USDC | 0.899311 USDC (0.8274 €) | — | 33.23 | 0.000 (n=18) | REJECTED | stale_data(6593ms>4000.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53907146 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.355649 WETH | 0.000046 WETH | 0.000000 WETH | 0.000004 WETH | 0.000043 WETH (0.0873 €) | — | 1.20 | 0.029 (n=28) | REJECTED | below_safety_margin(42515202857603<71129857263593), reliability_not_demonstrated |
| 53907146 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 793.055544 USDC | 0.102602 USDC | 0.000000 USDC | 0.007838 USDC | 0.094764 USDC (0.0872 €) | — | 1.19 | 0.029 (n=28) | REJECTED | below_safety_margin(94764<158611), reliability_not_demonstrated |
| 53907146 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010418 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0871 €) | — | 1.20 | 0.029 (n=28) | REJECTED | below_safety_margin(125<208), reliability_not_demonstrated |
| 53904293 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 87.573900 USDC | 0.093676 USDC | 0.000000 USDC | 0.005035 USDC | 0.088641 USDC (0.0815 €) | 0.088641 USDC | 10.12 | 0.000 (n=99) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53907146 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.098132 WETH | 0.000040 WETH | 0.000000 WETH | 0.000004 WETH | 0.000037 WETH (0.0758 €) | 0.000037 WETH | 3.76 | 0.149 (n=779) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53907146 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 226.218833 USDC | 0.090064 USDC | 0.000000 USDC | 0.007838 USDC | 0.082226 USDC (0.0756 €) | — | 3.63 | 0.149 (n=779) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53907146 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003102 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0753 €) | — | 3.48 | 0.149 (n=779) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53907146 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005663 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0732 €) | — | 1.85 | 0.168 (n=1025) | REJECTED | below_safety_margin(105<113), p_lower_below_threshold(0.17<0.75) |
| 53907146 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 437.030495 USDC | 0.087054 USDC | 0.000000 USDC | 0.007838 USDC | 0.079216 USDC (0.0729 €) | — | 1.81 | 0.168 (n=1025) | REJECTED | below_safety_margin(79216<87406), p_lower_below_threshold(0.17<0.75) |
| 53907146 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.175666 WETH | 0.000039 WETH | 0.000000 WETH | 0.000004 WETH | 0.000035 WETH (0.0723 €) | 0.000035 WETH | 2.01 | 0.168 (n=1025) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53907146 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 226.218833 USDC | 0.072566 USDC | 0.000000 USDC | 0.007479 USDC | 0.065087 USDC (0.0599 €) | — | 2.88 | 0.168 (n=1025) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53907146 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.093753 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0598 €) | 0.000029 WETH | 3.11 | 0.149 (n=779) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53907146 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003102 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0592 €) | — | 2.74 | 0.168 (n=1025) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53907207 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.245787 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0564 €) | — | 1.12 | 0.045 (n=239) | REJECTED | below_safety_margin(27476743313157<49157472386663), p_lower_below_threshold(0.05<0.75) |
| 53907207 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 548.604829 USDC | 0.067499 USDC | 0.000000 USDC | 0.006238 USDC | 0.061261 USDC (0.0564 €) | — | 1.12 | 0.045 (n=239) | REJECTED | below_safety_margin(61261<109720), p_lower_below_threshold(0.05<0.75) |
| 53907146 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.059894 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0558 €) | — | 4.54 | 0.149 (n=779) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53907146 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 133.117667 USDC | 0.067693 USDC | 0.000000 USDC | 0.007119 USDC | 0.060574 USDC (0.0557 €) | — | 4.55 | 0.149 (n=779) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53907146 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001082 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0488 €) | — | 6.47 | 0.149 (n=779) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53907146 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 81.869066 USDC | 0.059837 USDC | 0.000000 USDC | 0.007119 USDC | 0.052718 USDC (0.0485 €) | — | 6.44 | 0.149 (n=779) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53848955 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 384.664259 USDC | 0.052147 USDC | 0.000000 USDC | 0.005375 USDC | 0.046772 USDC (0.0430 €) | — | 1.22 | 0.054 (n=80) | REJECTED | below_safety_margin(46772<76932), p_lower_below_threshold(0.05<0.75) |
| 53848955 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 384.664259 USDC | 0.052147 USDC | 0.000000 USDC | 0.005375 USDC | 0.046772 USDC (0.0430 €) | — | 1.22 | 0.054 (n=80) | REJECTED | below_safety_margin(46772<76932), p_lower_below_threshold(0.05<0.75) |
| 53848955 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 343.755764 USDC | 0.045380 USDC | 0.000000 USDC | 0.005715 USDC | 0.039665 USDC (0.0365 €) | — | 1.15 | 0.054 (n=80) | REJECTED | below_safety_margin(39665<68751), p_lower_below_threshold(0.05<0.75) |
| 53848955 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 343.755764 USDC | 0.045380 USDC | 0.000000 USDC | 0.005715 USDC | 0.039665 USDC (0.0365 €) | — | 1.15 | 0.054 (n=80) | REJECTED | below_safety_margin(39665<68751), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5842 ; taux observé 0.159 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
