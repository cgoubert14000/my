# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T20:53:53+00:00 ; durée 281.77 min ; blocs 53380086 → 53388538 (6227 vus)

## Connexion
- Requêtes RPC : 81583 ; erreurs : 45 ; latence p50/p95 : 324.6/1,659.4 ms
- Rafraîchissements d'état : 6227 ; âge des données au dernier bloc : 4.82 s ; changements de frais LP observés (pools à frais dynamiques) : 4679
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 64540 ; cycles déclenchés par événement : 10085 ; avance médiane sur le rafraîchissement multicall : 1,369 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,258.83 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 289 jetons, 18734 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 111, aerodrome 206, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3737 (énumérés 315, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2264.227713, 'cbBTC': 77906.671325, 'AERO': 0.64119}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,410,124 | 2,258.831691 | 53388537 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,135,700 | 0.029048 | 53388537 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,324,125 | 0.000013 | 53388537 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,140,018 | 0.029095 | 53388537 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,887,558 | 2,261.204783 | 53388537 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,792,203 | 99.288560 | 53388538 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,649,844 | 0.001583 | 53388537 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,552,139 | 1.584276 | 53388537 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,150,291 | 0.029059 | 53388537 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,094,368 | 0.998850 | 53388537 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,049,404 | 2,261.931380 | 53388537 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,005,717 | 2,262.044451 | 53388538 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,531,449 | 38,290.322035 | 53388537 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,694,828 | 0.029081 | 53388537 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,370,947 | 99.289143 | 53388537 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 2,127,445 | 0.000013 | 53388537 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,086,618 | 1,188,094.920793 | 53388537 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,754,891 | 0.018046 | 53388537 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,752,338 | 0.000000 | 53388537 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,659,131 | 0.000013 | 53388537 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,582,082 | 0.000013 | 53388537 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,548,565 | 428.695780 | 53388538 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,505,220 | 2,261.749613 | 53388537 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53388537 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,248 | 0.825949 | 53388537 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,420,792 | 3,580.791480 | 53388537 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,379,270 | 2,263.241832 | 53388538 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,332,969 | 0.005217 | 53388537 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,321,903 | 2,261.254103 | 53388537 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,303,210 | 14,746.656502 | 53388537 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,301,822 | 0.000013 | 53388537 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,003 | 71.106813 | 53388537 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,118,674 | 36,002,670.776723 | 53388537 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,063,310 | 519,890.970894 | 53388537 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,048,448 | 0.000000 | 53388537 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,012,553 | 22,290,355.296081 | 53388537 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 990,682 | 19.467654 | 53388537 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 989,810 | 98.680866 | 53388537 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 973,686 | 82,154.958013 | 53388537 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 951,698 | 1,175,173.167936 | 53388537 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 947,357 | 69.753678 | 53388537 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 928,744 | 1,002.341897 | 53388537 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 922,286 | 2,252.785626 | 53388537 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 913,558 | 0.043979 | 53388537 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 865,430 | 3,557.688790 | 53388537 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 862,563 | 0.000549 | 53388537 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 834,656 | 19.561327 | 53388537 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,344 | 0.060529 | 53388537 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,402 | 0.801881 | 53388537 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 726,378 | 0.000261 | 53388537 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 726,282 | 0.590952 | 53388537 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 716,697 | 4,694,695.281747 | 53388537 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 689,662 | 135,356.923402 | 53388537 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 687,594 | 0.000008 | 53388537 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 681,445 | 0.582204 | 53388537 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 658,516 | 518,490.042890 | 53388537 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 657,965 | 2.340198 | 53388537 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 608,349 | 0.092059 | 53388537 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 606,458 | 0.915597 | 53388537 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| uniswap_v3 | FLOCK/USDC | 3000 | 568,225 | 0.039002 | 53388537 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 16311 ; routes examinées : 305570274 ; candidats optimisés : 965348 ; net attendu > 0 : 1446 ; dernier cycle 402.1 ms
- Rejets (moteur) : {'spread_below_threshold': 299950130, 'liquidity_below_min': 4033738, 'negative_expected_net': 963902, 'pool_quarantined': 569418, 'unquotable': 34353, 'borrow_bound_too_small': 16547, 'cycle_budget_exhausted': 740}
- Enregistrements de la session : 965348 ; net attendu > 0 : 1446 ; simulés (eth_call de la vraie tx) : 91 (ok 15, échec 76) ; étiquettes ghost N+1 : 1/45 positives
- Décisions : {'REJECTED': 965348} ; motifs de rejet : {'below_safety_margin': 1041, 'negative_expected_net': 963902, 'p_lower_below_threshold': 1245, 'price_impact': 103, 'reliability_not_demonstrated': 201, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 1, 'simulation_failed': 76, 'stale_data': 189}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→cbBTC | 0.021317 cbBTC | 0.000026 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000026 cbBTC (1.8481 €) | — | 12.11 | 0.041 (n=163) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53387669 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,672.936584 USDC | 2.010446 USDC | 0.000000 USDC | 0.006475 USDC | 2.003971 USDC (1.8437 €) | — | 11.98 | 0.041 (n=163) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.018012 cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000018 cbBTC (1.2760 €) | — | 9.89 | 0.087 (n=33) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53387669 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,418.750906 USDC | 1.390081 USDC | 0.000000 USDC | 0.006818 USDC | 1.383263 USDC (1.2726 €) | — | 9.75 | 0.087 (n=33) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→cbBTC | 0.016259 cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1786 €) | — | 10.12 | 0.041 (n=163) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53387669 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,278.861383 USDC | 1.285573 USDC | 0.000000 USDC | 0.006475 USDC | 1.279098 USDC (1.1768 €) | — | 10.00 | 0.041 (n=163) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[uniswap_v3]→cbBTC | 0.015695 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (0.9810 €) | — | 8.73 | 0.041 (n=163) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53387669 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,241.974234 USDC | 1.071751 USDC | 0.000000 USDC | 0.006475 USDC | 1.065276 USDC (0.9801 €) | — | 8.58 | 0.041 (n=163) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.008604 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000010 cbBTC (0.6888 €) | — | 11.18 | 0.087 (n=33) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53387669 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 686.620274 USDC | 0.754740 USDC | 0.000000 USDC | 0.006475 USDC | 0.748265 USDC (0.6884 €) | — | 10.90 | 0.087 (n=33) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.013886 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6373 €) | — | 6.41 | 0.118 (n=522) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53387669 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH | 0.493501 WETH | 0.000310 WETH | 0.000000 WETH | 0.000003 WETH | 0.000307 WETH (0.6372 €) | — | 6.21 | 0.118 (n=522) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004742 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6351 €) | — | 18.71 | 0.016 (n=87) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53387669 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 381.952536 USDC | 0.696451 USDC | 0.000000 USDC | 0.007816 USDC | 0.688635 USDC (0.6335 €) | — | 18.03 | 0.016 (n=87) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53387669 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→WETH | 0.204331 WETH | 0.000252 WETH | 0.000000 WETH | 0.000003 WETH | 0.000250 WETH (0.5186 €) | — | 12.21 | 0.087 (n=33) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→WETH→[pancakeswap_v3]→cbBTC | 0.005859 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5184 €) | — | 12.36 | 0.087 (n=33) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004206 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4962 €) | — | 16.48 | 0.065 (n=104) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53387669 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 340.686222 USDC | 0.546637 USDC | 0.000000 USDC | 0.007816 USDC | 0.538821 USDC (0.4957 €) | — | 15.82 | 0.065 (n=104) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004142 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4941 €) | — | 16.66 | 0.016 (n=87) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53387669 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 324.114599 USDC | 0.543422 USDC | 0.000000 USDC | 0.007473 USDC | 0.535949 USDC (0.4931 €) | — | 16.54 | 0.016 (n=87) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003843 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4783 €) | — | 17.38 | 0.065 (n=104) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53387669 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 298.880236 USDC | 0.526209 USDC | 0.000000 USDC | 0.007473 USDC | 0.518736 USDC (0.4772 €) | — | 17.36 | 0.065 (n=104) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.003900 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4189 €) | — | 15.00 | 0.016 (n=87) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53387669 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 310.715424 USDC | 0.461940 USDC | 0.000000 USDC | 0.007473 USDC | 0.454467 USDC (0.4181 €) | — | 14.63 | 0.016 (n=87) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53387669 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→WETH→[uniswap_v3]→cbBTC | 0.005155 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3924 €) | — | 10.63 | 0.041 (n=163) | REJECTED | p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 4176 ; taux observé 0.126 ; borne inférieure crédible (0.9) 0.120 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
