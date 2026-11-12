# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T11:10:54+00:00 ; durée 12.19 min ; blocs 56453704 → 56457355 (583 vus)

## Connexion
- Requêtes RPC : 8144 ; erreurs : 0 ; latence p50/p95 : 305.5/1,392.2 ms
- Rafraîchissements d'état : 583 ; âge des données au dernier bloc : 8.02 s ; changements de frais LP observés (pools à frais dynamiques) : 276
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 638 ; cycles déclenchés par événement : 242 ; avance médiane sur le rafraîchissement multicall : 491 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,045.27 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 456 pools, 265 jetons, 15214 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 458, sous le plancher de 10000.0 $ : 2 → gardés 456 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2045.271447, 'cbBTC': 73394.102525, 'AERO': 0.529681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,727,056 | 2,045.271502 | 56457379 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,407,779 | 0.027843 | 56457379 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,675,280 | 0.027806 | 56457379 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,397,742 | 0.000014 | 56457379 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,069,904 | 2,043.078772 | 56457379 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,836,559 | 104.278767 | 56457379 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,251,070 | 0.027849 | 56457379 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,204,642 | 1.880871 | 56457379 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,186,803 | 2,042.984223 | 56457379 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,869,825 | 0.998657 | 56457379 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,040,438 | 42,348.757888 | 56457379 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 107 | 2,869,889 | 2,042.981966 | 56457379 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,194,458 | 0.027825 | 56457379 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,939,016 | 1,127,807.662643 | 56457379 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,649,868 | 0.016816 | 56457379 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,642,840 | 0.000014 | 56457379 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,588,537 | 0.000014 | 56457379 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,558,015 | 0.000000 | 56457379 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,521,785 | 0.000014 | 56457379 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,513,056 | 0.006595 | 56457379 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,872 | 0.830193 | 56457379 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,397,851 | 432.404093 | 56457379 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,268,195 | 2,045.409436 | 56457379 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,243,312 | 3,842.553127 | 56457379 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,207,185 | 15,526.883713 | 56457379 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,153,644 | 2,048.455703 | 56457379 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,124,697 | 2,042.682981 | 56457379 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,623 | 86.218152 | 56457379 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,046,779 | 1.389936 | 56457379 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,034,835 | 33,847,318.837345 | 56457379 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,014,293 | 104.215896 | 56457379 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 957,491 | 21.562641 | 56457379 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 934,410 | 562,928.380412 | 56457379 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 910,838 | 0.001481 | 56457379 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | USDC/VVV | 3000 | 897,894 | 0.051012 | 56457379 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 896,350 | 0.000014 | 56457379 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 894,476 | 23,276,178.771400 | 56457379 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 876,485 | 2,054.853960 | 56457379 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 876,042 | 1,022.953583 | 56457379 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 860,176 | 0.000000 | 56457379 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 775,665 | 78.158329 | 56457379 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 747,843 | 0.049831 | 56457379 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 745,874 | 23.086546 | 56457379 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 738,763 | 116,840.564985 | 56457379 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 698,420 | 3,849.674049 | 56457379 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 692,940 | 0.801801 | 56457379 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 664,243 | 0.523967 | 56457379 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 640,147 | 4,840,213.419928 | 56457379 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 616,271 | 0.477958 | 56457379 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 584,801 | 155,064.775177 | 56457379 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 573,303 | 0.000257 | 56457379 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 573,047 | 565,371.630247 | 56457379 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 568,791 | 0.000007 | 56457379 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 558,796 | 0.037595 | 56457379 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2724 | 487,816 | 1,022.400178 | 56457379 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 463,650 | 0.066738 | 56457379 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,298 | 1.001029 | 56457379 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,958 | 0.501968 | 56457379 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 439,004 | 24.794769 | 56457379 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 432,669 | 332.166569 | 56457379 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 824 ; routes examinées : 12536336 ; candidats optimisés : 59581 ; net attendu > 0 : 50 ; dernier cycle 326.9 ms
- Rejets (moteur) : {'spread_below_threshold': 12376862, 'liquidity_below_min': 99069, 'negative_expected_net': 59531, 'borrow_bound_too_small': 824}
- Enregistrements de la session : 59581 ; net attendu > 0 : 50 ; simulés (eth_call de la vraie tx) : 6 (ok 6, échec 0) ; étiquettes ghost N+1 : 6/6 positives
- Décisions : {'REJECTED': 59581} ; motifs de rejet : {'below_safety_margin': 38, 'negative_expected_net': 59531, 'p_lower_below_threshold': 50, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56454376 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004616 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0032 €) | 0.000000 WETH | 3.71 | 0.203 (n=1242) | REJECTED | sim_below_estimate(3104886127760<4719147461324), p_lower_below_threshold(0.20<0.75) |
| 56454376 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.317322 USDC | 0.009640 USDC | 0.000000 USDC | 0.006148 USDC | 0.003492 USDC (0.0032 €) | — | 3.75 | 0.203 (n=1242) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56454376 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004516 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0028 €) | -0.000000 WETH | 3.34 | 0.309 (n=575) | REJECTED | sim_below_estimate(2933358450431<4512467379983), simulated_net_nonpositive, p_lower_below_threshold(0.31<0.75) |
| 56454376 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 9.228954 USDC | 0.009218 USDC | 0.000000 USDC | 0.006148 USDC | 0.003070 USDC (0.0028 €) | — | 3.33 | 0.309 (n=575) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56454376 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004489 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0027 €) | -0.000000 WETH | 3.22 | 0.309 (n=575) | REJECTED | sim_below_estimate(2882332297405<4452143773794), simulated_net_nonpositive, p_lower_below_threshold(0.31<0.75) |
| 56454376 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.131977 USDC | 0.009095 USDC | 0.000000 USDC | 0.006148 USDC | 0.002947 USDC (0.0027 €) | — | 3.23 | 0.309 (n=575) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56453893 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004438 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0025 €) | -0.000000 WETH | 3.03 | 0.308 (n=574) | REJECTED | sim_below_estimate(2569212350310<4349841384000), simulated_net_nonpositive, p_lower_below_threshold(0.31<0.75) |
| 56453893 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.964530 USDC | 0.008886 USDC | 0.000000 USDC | 0.006149 USDC | 0.002737 USDC (0.0025 €) | — | 3.05 | 0.308 (n=574) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56453893 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004367 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | -0.000001 WETH | 2.84 | 0.344 (n=610) | REJECTED | sim_below_estimate(2495838582483<4247947250688), simulated_net_nonpositive, p_lower_below_threshold(0.34<0.75) |
| 56453893 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.927777 USDC | 0.008678 USDC | 0.000000 USDC | 0.006149 USDC | 0.002529 USDC (0.0023 €) | — | 2.83 | 0.344 (n=610) | REJECTED | p_lower_below_threshold(0.34<0.75) |
| 56453893 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004332 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0022 €) | -0.000001 WETH | 2.69 | 0.268 (n=1593) | REJECTED | sim_below_estimate(2433077665355<4170964948589), simulated_net_nonpositive, p_lower_below_threshold(0.27<0.75) |
| 56453893 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.737838 USDC | 0.008520 USDC | 0.000000 USDC | 0.006149 USDC | 0.002371 USDC (0.0022 €) | — | 2.71 | 0.268 (n=1593) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56454376 | WETH→[aerodrome]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003993 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.75 | 0.254 (n=234) | REJECTED | below_safety_margin(699596359840<798595016250), p_lower_below_threshold(0.25<0.75) |
| 56454376 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome]→USDC | 8.096967 USDC | 0.007287 USDC | 0.000000 USDC | 0.005866 USDC | 0.001421 USDC (0.0013 €) | — | 1.75 | 0.254 (n=234) | REJECTED | below_safety_margin(1421<1619), p_lower_below_threshold(0.25<0.75) |
| 56454693 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.014149 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 0.43 | 0.269 (n=1594) | REJECTED | below_safety_margin(610079413538<2829709182099), p_lower_below_threshold(0.27<0.75) |
| 56454694 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.014149 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 0.43 | 0.269 (n=1594) | REJECTED | below_safety_margin(610079413538<2829709182099), p_lower_below_threshold(0.27<0.75) |
| 56454693 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 28.828287 USDC | 0.007392 USDC | 0.000000 USDC | 0.006150 USDC | 0.001242 USDC (0.0011 €) | — | 0.43 | 0.269 (n=1594) | REJECTED | below_safety_margin(1242<5765), p_lower_below_threshold(0.27<0.75) |
| 56454694 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 28.828287 USDC | 0.007392 USDC | 0.000000 USDC | 0.006150 USDC | 0.001242 USDC (0.0011 €) | — | 0.43 | 0.269 (n=1594) | REJECTED | below_safety_margin(1242<5765), p_lower_below_threshold(0.27<0.75) |
| 56454376 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003314 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 1.34 | 0.345 (n=611) | REJECTED | below_safety_margin(444390496880<662888347950), p_lower_below_threshold(0.35<0.75) |
| 56454376 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 6.697829 USDC | 0.007045 USDC | 0.000000 USDC | 0.006148 USDC | 0.000897 USDC (0.0008 €) | — | 1.34 | 0.345 (n=611) | REJECTED | below_safety_margin(897<1339), p_lower_below_threshold(0.35<0.75) |
| 56454445 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003884 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.88 | 0.269 (n=1594) | REJECTED | below_safety_margin(340145882418<776804531222), p_lower_below_threshold(0.27<0.75) |
| 56454447 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003884 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.88 | 0.269 (n=1594) | REJECTED | below_safety_margin(340145882418<776804531222), p_lower_below_threshold(0.27<0.75) |
| 56454446 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003884 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.88 | 0.269 (n=1594) | REJECTED | below_safety_margin(340145882418<776804531222), p_lower_below_threshold(0.27<0.75) |
| 56454447 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003884 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.88 | 0.269 (n=1594) | REJECTED | below_safety_margin(340145882418<776804531222), p_lower_below_threshold(0.27<0.75) |
| 56454447 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003884 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.88 | 0.269 (n=1594) | REJECTED | below_safety_margin(340145882418<776804531222), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8273 ; taux observé 0.218 ; borne inférieure crédible (0.9) 0.212 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
