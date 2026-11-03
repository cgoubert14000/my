# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T20:09:01+00:00 ; durée 79.55 min ; blocs 53471207 → 53473595 (2307 vus)

## Connexion
- Requêtes RPC : 27589 ; erreurs : 278 ; latence p50/p95 : 130.8/1,185.1 ms
- Rafraîchissements d'état : 2307 ; âge des données au dernier bloc : 2.67 s ; changements de frais LP observés (pools à frais dynamiques) : 2350
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 19798 ; cycles déclenchés par événement : 1973 ; avance médiane sur le rafraîchissement multicall : 618 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,289.33 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 493 pools, 285 jetons, 19448 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 496, sous le plancher de 10000.0 $ : 3 → gardés 493 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2294.78828, 'cbBTC': 77607.185431, 'AERO': 0.633493}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,516,838 | 2,289.334673 | 53473596 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,415,640 | 0.029465 | 53473596 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,206,513 | 0.029539 | 53473596 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,066,156 | 0.000013 | 53473596 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,046,561 | 2,286.921171 | 53473596 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,806,325 | 100.807587 | 53473596 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,622,499 | 0.001573 | 53473596 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,396,511 | 1.586664 | 53473596 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,838,594 | 0.029469 | 53473596 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,171,371 | 2,287.580521 | 53473596 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,087,513 | 0.999899 | 53473596 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,887,985 | 2,287.523368 | 53473596 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,428,896 | 41,718.225073 | 53473596 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,712,078 | 0.029526 | 53473596 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,174,591 | 1,123,653.677423 | 53473596 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2757 | 2,144,097 | 100.545758 | 53473596 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,815,452 | 0.000013 | 53473596 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,736,053 | 0.017764 | 53473596 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,684,830 | 0.000000 | 53473596 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,642,351 | 0.000013 | 53473596 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,557,036 | 440.737163 | 53473596 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,555,481 | 0.000013 | 53473596 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53473596 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,936 | 2,289.366011 | 53473596 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,460,793 | 0.005728 | 53473596 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,800 | 0.821850 | 53473596 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,424,960 | 3,623.878483 | 53473596 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,341,796 | 2,289.682214 | 53473596 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,338,930 | 2,287.223948 | 53473596 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,294,925 | 14,937.239635 | 53473596 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,196,159 | 0.000013 | 53473596 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,158,637 | 72.384430 | 53473596 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,127,560 | 36,832,100.803973 | 53473596 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,060,437 | 544,200.570395 | 53473596 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,051,800 | 0.000000 | 53473596 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,035,760 | 21,950,664.012046 | 53473596 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 995,801 | 19.181019 | 53473596 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 959,136 | 101.018332 | 53473596 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 954,274 | 1,047.111849 | 53473596 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 953,405 | 87,959.580743 | 53473596 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 946,190 | 69.926680 | 53473596 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 935,139 | 1,250,216.725622 | 53473596 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 928,866 | 2,282.122456 | 53473596 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 904,445 | 0.044078 | 53473596 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 879,708 | 0.000555 | 53473596 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 846,202 | 3,646.232124 | 53473596 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 821,697 | 20.040742 | 53473596 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,633 | 0.056713 | 53473596 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 777,062 | 0.799140 | 53473596 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,513 | 0.590956 | 53473596 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 727,483 | 0.000257 | 53473596 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 717,990 | 4,807,878.349292 | 53473596 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 672,151 | 0.000008 | 53473596 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 669,050 | 147,819.952585 | 53473596 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 665,227 | 0.555930 | 53473596 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 662,565 | 2.343097 | 53473596 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 651,728 | 548,559.324990 | 53473596 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 614,944 | 0.914716 | 53473596 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 584,543 | 0.086574 | 53473596 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,556 | 0.038871 | 53473596 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 4279 ; routes examinées : 83217992 ; candidats optimisés : 197103 ; net attendu > 0 : 50 ; dernier cycle 160.4 ms
- Rejets (moteur) : {'spread_below_threshold': 82209354, 'liquidity_below_min': 798627, 'negative_expected_net': 197053, 'unquotable': 8554, 'borrow_bound_too_small': 4277, 'cycle_budget_exhausted': 77}
- Enregistrements de la session : 197103 ; net attendu > 0 : 50 ; simulés (eth_call de la vraie tx) : 2 (ok 0, échec 2) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 197103} ; motifs de rejet : {'below_safety_margin': 48, 'negative_expected_net': 197053, 'p_lower_below_threshold': 48, 'reliability_not_demonstrated': 2, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53472395 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.026252 WETH | 0.000056 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1137 €) | — | 20.53 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53472362 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.020014 WETH | 0.000033 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0642 €) | — | 15.21 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53473234 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000756 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0100 €) | — | 1.85 | 0.185 (n=852) | REJECTED | below_safety_margin(14<15), p_lower_below_threshold(0.18<0.75) |
| 53473234 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000756 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0100 €) | — | 1.85 | 0.185 (n=852) | REJECTED | below_safety_margin(14<15), p_lower_below_threshold(0.18<0.75) |
| 53473234 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.026637 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0097 €) | — | 1.72 | 0.185 (n=852) | REJECTED | below_safety_margin(4588171224948<5327432158996), p_lower_below_threshold(0.18<0.75) |
| 53473234 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.026637 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0097 €) | — | 1.72 | 0.185 (n=852) | REJECTED | below_safety_margin(4588171224948<5327432158996), p_lower_below_threshold(0.18<0.75) |
| 53471700 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.168881 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | — | 0.24 | 0.185 (n=852) | REJECTED | below_safety_margin(4067722060797<33776255979005), p_lower_below_threshold(0.18<0.75) |
| 53471700 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.168881 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | — | 0.24 | 0.185 (n=852) | REJECTED | below_safety_margin(4067722060797<33776255979005), p_lower_below_threshold(0.18<0.75) |
| 53471700 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.004337 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0086 €) | — | 0.28 | 0.185 (n=852) | REJECTED | below_safety_margin(12<86), p_lower_below_threshold(0.18<0.75) |
| 53471700 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.004337 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0086 €) | — | 0.28 | 0.185 (n=852) | REJECTED | below_safety_margin(12<86), p_lower_below_threshold(0.18<0.75) |
| 53471700 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 363.859527 USDC | 0.016213 USDC | 0.000000 USDC | 0.006897 USDC | 0.009316 USDC (0.0086 €) | — | 0.26 | 0.185 (n=852) | REJECTED | below_safety_margin(9316<72771), p_lower_below_threshold(0.18<0.75) |
| 53471700 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 363.859527 USDC | 0.016213 USDC | 0.000000 USDC | 0.006897 USDC | 0.009316 USDC (0.0086 €) | — | 0.26 | 0.185 (n=852) | REJECTED | below_safety_margin(9316<72771), p_lower_below_threshold(0.18<0.75) |
| 53473234 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.019104 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0061 €) | — | 1.53 | 0.185 (n=852) | REJECTED | below_safety_margin(2917713397806<3820762798122), p_lower_below_threshold(0.18<0.75) |
| 53473234 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.019104 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0061 €) | — | 1.53 | 0.185 (n=852) | REJECTED | below_safety_margin(2917713397806<3820762798122), p_lower_below_threshold(0.18<0.75) |
| 53473234 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000597 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0057 €) | — | 1.34 | 0.185 (n=852) | REJECTED | below_safety_margin(8<11), p_lower_below_threshold(0.18<0.75) |
| 53473234 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000597 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0057 €) | — | 1.34 | 0.185 (n=852) | REJECTED | below_safety_margin(8<11), p_lower_below_threshold(0.18<0.75) |
| 53471700 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002331 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0043 €) | — | 0.26 | 0.185 (n=852) | REJECTED | below_safety_margin(6<46), p_lower_below_threshold(0.18<0.75) |
| 53471700 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002331 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0043 €) | — | 0.26 | 0.185 (n=852) | REJECTED | below_safety_margin(6<46), p_lower_below_threshold(0.18<0.75) |
| 53471700 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.090141 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.22 | 0.185 (n=852) | REJECTED | below_safety_margin(2021325061000<18028142434123), p_lower_below_threshold(0.18<0.75) |
| 53471700 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.090141 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.22 | 0.185 (n=852) | REJECTED | below_safety_margin(2021325061000<18028142434123), p_lower_below_threshold(0.18<0.75) |
| 53471700 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 224.474377 USDC | 0.011869 USDC | 0.000000 USDC | 0.007245 USDC | 0.004624 USDC (0.0043 €) | — | 0.21 | 0.185 (n=852) | REJECTED | below_safety_margin(4624<44894), p_lower_below_threshold(0.18<0.75) |
| 53471700 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 224.474377 USDC | 0.011869 USDC | 0.000000 USDC | 0.007245 USDC | 0.004624 USDC (0.0043 €) | — | 0.21 | 0.185 (n=852) | REJECTED | below_safety_margin(4624<44894), p_lower_below_threshold(0.18<0.75) |
| 53473429 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH | 0.009356 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.69 | 0.259 (n=342) | REJECTED | below_safety_margin(648186582857<1871155770923), p_lower_below_threshold(0.26<0.75) |
| 53473430 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH | 0.009356 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.69 | 0.259 (n=342) | REJECTED | below_safety_margin(648186582857<1871155770923), p_lower_below_threshold(0.26<0.75) |
| 53473430 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH | 0.009356 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.69 | 0.259 (n=342) | REJECTED | below_safety_margin(648186582857<1871155770923), p_lower_below_threshold(0.26<0.75) |

## Fiabilité et décision
- Observations ghost : 4907 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
