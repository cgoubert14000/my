# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T17:28:46+00:00 ; durée 164.58 min ; blocs 53420649 → 53425585 (4885 vus)

## Connexion
- Requêtes RPC : 58769 ; erreurs : 10 ; latence p50/p95 : 90.2/1,042.4 ms
- Rafraîchissements d'état : 4885 ; âge des données au dernier bloc : 2.21 s ; changements de frais LP observés (pools à frais dynamiques) : 8353
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 71187 ; cycles déclenchés par événement : 6033 ; avance médiane sur le rafraîchissement multicall : 1,586 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,260.10 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 286 jetons, 18656 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 310, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2287.70349, 'cbBTC': 77760.832568, 'AERO': 0.623017}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,272,652 | 2,260.101963 | 53425585 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,221,631 | 0.029257 | 53425585 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,122,366 | 0.029328 | 53425585 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,032,678 | 0.000013 | 53425585 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,892,142 | 2,255.468577 | 53425585 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,528,034 | 106.341659 | 53425585 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,583,894 | 0.001574 | 53425585 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,418,968 | 1.635619 | 53425585 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,776,041 | 0.029269 | 53425585 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,079,664 | 2,255.996318 | 53425586 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,063,844 | 0.999919 | 53425585 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 833 | 3,980,170 | 2,255.894935 | 53425586 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,513,418 | 38,726.868053 | 53425585 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 2,643,469 | 0.029313 | 53425585 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,264,475 | 106.369615 | 53425585 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,147,758 | 1,122,676.503855 | 53425585 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 592 | 2,086,394 | 0.000013 | 53425585 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,735,475 | 0.017738 | 53425585 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,682,767 | 0.000000 | 53425585 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,610,714 | 0.000013 | 53425585 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,568,552 | 0.000013 | 53425585 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,533,289 | 444.126930 | 53425585 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,499,181 | 2,260.118415 | 53425585 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53425585 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,556 | 0.822512 | 53425585 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,401,954 | 3,691.307845 | 53425585 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,351,877 | 2,260.079044 | 53425585 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,314,502 | 0.005103 | 53425585 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,311,620 | 2,255.455784 | 53425585 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,278,920 | 15,154.192136 | 53425585 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 366 | 1,263,299 | 0.000013 | 53425585 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,168,911 | 71.117634 | 53425585 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,098,805 | 38,177,182.906255 | 53425585 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,052,498 | 535,824.181213 | 53425585 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,011,713 | 22,796,281.878603 | 53425585 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 997,444 | 0.000000 | 53425585 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 983,400 | 19.892492 | 53425585 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 976,181 | 81,791.379131 | 53425585 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 938,358 | 1,210,184.797128 | 53425585 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 922,878 | 2,276.064229 | 53425585 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 918,465 | 1,032.661616 | 53425585 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 892,058 | 106.172670 | 53425585 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 889,226 | 79.172112 | 53425585 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 868,269 | 0.047176 | 53425585 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,283 | 0.000548 | 53425585 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 835,085 | 3,664.068737 | 53425585 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4590 | 824,345 | 19.936579 | 53425585 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,336 | 0.056824 | 53425585 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,827 | 0.801881 | 53425585 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 720,132 | 0.000258 | 53425585 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 715,499 | 0.577943 | 53425585 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 696,817 | 4,973,585.060488 | 53425585 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 677,827 | 140,330.627983 | 53425585 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 672,018 | 0.000008 | 53425585 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 671,540 | 0.571558 | 53425585 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 655,459 | 2.337527 | 53425585 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 648,597 | 540,071.514031 | 53425585 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 606,950 | 0.915143 | 53425585 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 592,867 | 0.088489 | 53425585 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 553,768 | 0.037495 | 53425585 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 10917 ; routes examinées : 203667552 ; candidats optimisés : 838189 ; net attendu > 0 : 1930 ; dernier cycle 215.9 ms
- Rejets (moteur) : {'spread_below_threshold': 199052730, 'liquidity_below_min': 3208248, 'negative_expected_net': 836259, 'pool_quarantined': 510496, 'unquotable': 45884, 'borrow_bound_too_small': 10914, 'cycle_budget_exhausted': 1091}
- Enregistrements de la session : 838189 ; net attendu > 0 : 1930 ; simulés (eth_call de la vraie tx) : 109 (ok 43, échec 66) ; étiquettes ghost N+1 : 11/78 positives
- Décisions : {'REJECTED': 838189} ; motifs de rejet : {'below_safety_margin': 1550, 'negative_expected_net': 836259, 'p_lower_below_threshold': 1736, 'price_impact': 394, 'reliability_not_demonstrated': 194, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 2, 'simulation_failed': 66, 'stale_data': 54}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53421255 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.022920 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2227 €) | — | 1.36 | 0.015 (n=19) | REJECTED | below_safety_margin(311<458), reliability_not_demonstrated |
| 53421255 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.806328 WETH | 0.000109 WETH | 0.000000 WETH | 0.000003 WETH | 0.000106 WETH (0.2224 €) | — | 1.31 | 0.015 (n=19) | REJECTED | below_safety_margin(105730486160810<161265691126913), reliability_not_demonstrated |
| 53421255 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,798.869495 USDC | 0.248913 USDC | 0.000000 USDC | 0.007636 USDC | 0.241277 USDC (0.2220 €) | — | 1.34 | 0.015 (n=19) | REJECTED | below_safety_margin(241277<359773), reliability_not_demonstrated |
| 53423107 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,463.190229 USDC | 0.236997 USDC | 0.000000 USDC | 0.007581 USDC | 0.229416 USDC (0.2111 €) | — | 1.57 | 0.015 (n=19) | REJECTED | below_safety_margin(229416<292638), reliability_not_demonstrated |
| 53423107 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.018050 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2108 €) | — | 1.64 | 0.015 (n=19) | REJECTED | below_safety_margin(296<360), reliability_not_demonstrated |
| 53423107 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.623407 WETH | 0.000104 WETH | 0.000000 WETH | 0.000003 WETH | 0.000101 WETH (0.2108 €) | — | 1.62 | 0.015 (n=19) | REJECTED | below_safety_margin(100913025911152<124681318574639), reliability_not_demonstrated |
| 53420906 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.015164 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1868 €) | — | 1.72 | 0.039 (n=170) | REJECTED | below_safety_margin(261<303), p_lower_below_threshold(0.04<0.75) |
| 53420906 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 1,239.328545 USDC | 0.207693 USDC | 0.000000 USDC | 0.005181 USDC | 0.202512 USDC (0.1863 €) | — | 1.63 | 0.039 (n=170) | REJECTED | below_safety_margin(202512<247865), p_lower_below_threshold(0.04<0.75) |
| 53423107 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.558889 WETH | 0.000083 WETH | 0.000000 WETH | 0.000003 WETH | 0.000080 WETH (0.1670 €) | — | 1.43 | 0.186 (n=817) | REJECTED | below_safety_margin(79963547611790<111777767764553), p_lower_below_threshold(0.19<0.75) |
| 53423107 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.016032 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1667 €) | — | 1.46 | 0.186 (n=817) | REJECTED | below_safety_margin(234<320), p_lower_below_threshold(0.19<0.75) |
| 53423107 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,242.865749 USDC | 0.188376 USDC | 0.000000 USDC | 0.007237 USDC | 0.181139 USDC (0.1666 €) | — | 1.46 | 0.186 (n=817) | REJECTED | below_safety_margin(181139<248573), p_lower_below_threshold(0.19<0.75) |
| 53423107 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,399.750949 USDC | 0.143343 USDC | 0.000000 USDC | 0.005499 USDC | 0.137844 USDC (0.1268 €) | — | 0.98 | 0.038 (n=176) | REJECTED | below_safety_margin(137844<279950), p_lower_below_threshold(0.04<0.75) |
| 53423107 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.016285 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1261 €) | — | 1.09 | 0.038 (n=176) | REJECTED | below_safety_margin(177<325), p_lower_below_threshold(0.04<0.75) |
| 53421893 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 610.097918 USDC | 0.130437 USDC | 0.000000 USDC | 0.005187 USDC | 0.125250 USDC (0.1152 €) | — | 2.05 | 0.039 (n=173) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53421893 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.267037 WETH | 0.000057 WETH | 0.000000 WETH | 0.000002 WETH | 0.000055 WETH (0.1152 €) | — | 2.05 | 0.039 (n=173) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53421556 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 70.663620 USDC | 0.124475 USDC | 0.000000 USDC | 0.005196 USDC | 0.119279 USDC (0.1097 €) | — | 16.88 | 0.000 (n=67) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53421255 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.570170 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1091 €) | — | 0.91 | 0.186 (n=812) | REJECTED | below_safety_margin(51835095819741<114034094199709), p_lower_below_threshold(0.19<0.75) |
| 53421255 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,203.896089 USDC | 0.125795 USDC | 0.000000 USDC | 0.007289 USDC | 0.118506 USDC (0.1090 €) | — | 0.98 | 0.186 (n=812) | REJECTED | below_safety_margin(118506<240779), p_lower_below_threshold(0.19<0.75) |
| 53421255 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.014959 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1089 €) | — | 1.02 | 0.186 (n=812) | REJECTED | below_safety_margin(152<299), p_lower_below_threshold(0.19<0.75) |
| 53423107 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 851.211948 USDC | 0.121598 USDC | 0.000000 USDC | 0.005499 USDC | 0.116099 USDC (0.1068 €) | — | 1.36 | 0.038 (n=176) | REJECTED | below_safety_margin(116099<170242), p_lower_below_threshold(0.04<0.75) |
| 53423107 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.010269 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1061 €) | — | 1.45 | 0.038 (n=176) | REJECTED | below_safety_margin(149<205), p_lower_below_threshold(0.04<0.75) |
| 53420792 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 176.248588 USDC | 0.115731 USDC | 0.000000 USDC | 0.006923 USDC | 0.108808 USDC (0.1001 €) | — | 6.17 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.077017 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000048 WETH (0.1000 €) | — | 6.17 | 0.159 (n=583) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53421255 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.090996 WETH | 0.000050 WETH | 0.000000 WETH | 0.000002 WETH | 0.000047 WETH (0.0996 €) | 0.000047 WETH | 5.21 | 0.029 (n=203) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53421255 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 207.939361 USDC | 0.113297 USDC | 0.000000 USDC | 0.005192 USDC | 0.108105 USDC (0.0995 €) | — | 5.20 | 0.029 (n=203) | REJECTED | p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 4719 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
