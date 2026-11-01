# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T20:02:47+00:00 ; durée 230.66 min ; blocs 53380086 → 53387006 (5258 vus)

## Connexion
- Requêtes RPC : 68279 ; erreurs : 45 ; latence p50/p95 : 343.6/1,292.3 ms
- Rafraîchissements d'état : 5259 ; âge des données au dernier bloc : 4.37 s ; changements de frais LP observés (pools à frais dynamiques) : 3677
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 54218 ; cycles déclenchés par événement : 8307 ; avance médiane sur le rafraîchissement multicall : 1,268 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,259.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 289 jetons, 18734 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 111 (quarantaine 1), aerodrome 206 (quarantaine 2), pancakeswap_v3 29 (quarantaine 1), uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3737 (énumérés 315, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2264.227713, 'cbBTC': 77906.671325, 'AERO': 0.64119}
- Pools en quarantaine : 4 — pancakeswap_v3:USDC/PLAY@0xf1CaCd: simulation failed ×5 (model/chain mismatch) — until block 53387142; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 53387123; aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 53387123; aerodrome_slipstream:USDC/PLAY@0xF2c832: simulation failed ×5 (model/chain mismatch) — until block 53387142

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,449,415 | 2,259.032632 | 53387005 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,137,477 | 0.029047 | 53387004 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,324,924 | 0.000013 | 53387004 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,140,913 | 0.029102 | 53387004 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,874,691 | 2,257.088008 | 53387004 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,790,943 | 99.338550 | 53387004 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,644,153 | 0.001580 | 53387004 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,574,618 | 1.584565 | 53387004 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,150,740 | 0.029036 | 53387004 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,094,846 | 0.998850 | 53387004 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,049,852 | 2,257.561897 | 53387004 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,013,246 | 2,257.379249 | 53387004 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,531,770 | 38,290.177810 | 53387004 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,695,096 | 0.029087 | 53387004 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,371,381 | 99.311832 | 53387004 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 2,127,587 | 0.000013 | 53387004 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,086,803 | 1,188,094.920793 | 53387004 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,755,076 | 0.018049 | 53387004 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,752,504 | 0.000000 | 53387004 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,626,791 | 0.000013 | 53387004 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,581,628 | 0.000013 | 53387004 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,548,115 | 429.301102 | 53387004 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,533,296 | 1.503377 | 53387004 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,505,284 | 2,259.744691 | 53387004 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,184 | 0.826015 | 53387004 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,420,367 | 3,576.186268 | 53387004 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,379,331 | 2,263.130537 | 53387004 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,335,042 | 0.005226 | 53387004 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,323,554 | 2,256.953516 | 53387004 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 1,307,002 | 0.000013 | 53387004 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,302,633 | 14,740.416038 | 53387004 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,169,003 | 71.106813 | 53387004 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,121,174 | 35,769,795.142745 | 53387004 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,063,410 | 519,884.151444 | 53387004 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,049,621 | 0.000000 | 53387004 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,011,592 | 22,295,854.410072 | 53387004 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 989,741 | 98.680861 | 53387004 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 989,697 | 19.524050 | 53387004 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 974,184 | 82,085.514362 | 53387004 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 952,126 | 1,174,325.100955 | 53387004 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 948,332 | 69.610348 | 53387004 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 927,599 | 1,004.247705 | 53387004 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 922,317 | 2,252.785626 | 53387004 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 913,276 | 0.043985 | 53387004 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 865,908 | 3,551.195514 | 53387004 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,179 | 0.000547 | 53387004 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 833,853 | 19.589760 | 53387004 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,728 | 0.060590 | 53387004 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,470 | 0.801881 | 53387004 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 726,443 | 0.000261 | 53387004 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 726,322 | 0.588291 | 53387004 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 716,720 | 4,695,223.191324 | 53387004 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 688,250 | 135,929.292559 | 53387004 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 687,498 | 0.000008 | 53387006 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 681,662 | 0.582556 | 53387004 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 658,574 | 518,570.196842 | 53387004 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 658,023 | 2.340198 | 53387004 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 608,347 | 0.092059 | 53387004 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 606,498 | 0.915639 | 53387004 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| uniswap_v3 | FLOCK/USDC | 3000 | 569,252 | 0.039112 | 53387004 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 13565 ; routes examinées : 254126710 ; candidats optimisés : 779539 ; net attendu > 0 : 1236 ; dernier cycle 166.0 ms
- Rejets (moteur) : {'spread_below_threshold': 249846833, 'liquidity_below_min': 3189574, 'negative_expected_net': 778303, 'pool_quarantined': 267780, 'unquotable': 28823, 'borrow_bound_too_small': 13565, 'cycle_budget_exhausted': 596}
- Enregistrements de la session : 779539 ; net attendu > 0 : 1236 ; simulés (eth_call de la vraie tx) : 68 (ok 15, échec 53) ; étiquettes ghost N+1 : 1/38 positives
- Décisions : {'REJECTED': 779539} ; motifs de rejet : {'below_safety_margin': 944, 'negative_expected_net': 778303, 'p_lower_below_threshold': 1062, 'price_impact': 83, 'reliability_not_demonstrated': 174, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 1, 'simulation_failed': 53, 'stale_data': 164}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53386937 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.753952 WETH | 0.000119 WETH | 0.000000 WETH | 0.000003 WETH | 0.000115 WETH (0.2397 €) | — | 1.53 | 0.000 (n=18) | REJECTED | below_safety_margin(115351922245862<150790482795254), reliability_not_demonstrated |
| 53386937 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.022115 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2397 €) | — | 1.51 | 0.000 (n=18) | REJECTED | below_safety_margin(335<442), reliability_not_demonstrated |
| 53386937 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,747.135213 USDC | 0.267802 USDC | 0.000000 USDC | 0.007473 USDC | 0.260329 USDC (0.2395 €) | — | 1.49 | 0.000 (n=18) | REJECTED | below_safety_margin(260329<349427), reliability_not_demonstrated |
| 53385529 | WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.876972 WETH | 0.000108 WETH | 0.000000 WETH | 0.000003 WETH | 0.000105 WETH (0.2187 €) | — | 1.20 | 0.137 (n=703) | REJECTED | below_safety_margin(105126532557613<175394338841049), p_lower_below_threshold(0.14<0.75) |
| 53380235 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 158.478005 USDC | 0.223007 USDC | 0.000000 USDC | 0.007148 USDC | 0.215859 USDC (0.1986 €) | — | 13.62 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53380235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.069998 WETH | 0.000098 WETH | 0.000000 WETH | 0.000003 WETH | 0.000095 WETH (0.1983 €) | — | 13.60 | 0.017 (n=85) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53380235 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 156.834999 USDC | 0.211689 USDC | 0.000000 USDC | 0.007148 USDC | 0.204541 USDC (0.1882 €) | — | 13.04 | 0.065 (n=103) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53380235 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.069172 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000090 WETH (0.1879 €) | — | 13.04 | 0.065 (n=103) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53380235 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 155.799299 USDC | 0.208980 USDC | 0.000000 USDC | 0.007148 USDC | 0.201832 USDC (0.1857 €) | — | 12.95 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53380235 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.068819 WETH | 0.000092 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1854 €) | — | 12.93 | 0.017 (n=85) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53385529 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.587098 WETH | 0.000074 WETH | 0.000000 WETH | 0.000003 WETH | 0.000071 WETH (0.1478 €) | — | 1.21 | 0.137 (n=703) | REJECTED | below_safety_margin(71058742290886<117419624951970), p_lower_below_threshold(0.14<0.75) |
| 53385529 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.015779 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1474 €) | — | 1.31 | 0.137 (n=703) | REJECTED | below_safety_margin(206<315), p_lower_below_threshold(0.14<0.75) |
| 53385529 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,390.001571 USDC | 0.166242 USDC | 0.000000 USDC | 0.006794 USDC | 0.159448 USDC (0.1467 €) | — | 1.15 | 0.137 (n=703) | REJECTED | below_safety_margin(159448<278000), p_lower_below_threshold(0.14<0.75) |
| 53381335 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.570288 WETH | 0.000070 WETH | 0.000000 WETH | 0.000003 WETH | 0.000067 WETH (0.1393 €) | — | 1.17 | 0.000 (n=18) | REJECTED | below_safety_margin(66872132995536<114057586661070), reliability_not_demonstrated |
| 53381335 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.015460 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1391 €) | — | 1.25 | 0.000 (n=18) | REJECTED | below_safety_margin(194<309), reliability_not_demonstrated |
| 53381335 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,363.148149 USDC | 0.158575 USDC | 0.000000 USDC | 0.007491 USDC | 0.151084 USDC (0.1390 €) | — | 1.11 | 0.000 (n=18) | REJECTED | below_safety_margin(151084<272629), reliability_not_demonstrated |
| 53381677 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,192.811264 USDC | 0.154774 USDC | 0.000000 USDC | 0.007146 USDC | 0.147628 USDC (0.1358 €) | — | 1.24 | 0.138 (n=691) | REJECTED | below_safety_margin(147628<238562), p_lower_below_threshold(0.14<0.75) |
| 53381678 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,192.811264 USDC | 0.154774 USDC | 0.000000 USDC | 0.007146 USDC | 0.147628 USDC (0.1358 €) | — | 1.24 | 0.138 (n=691) | REJECTED | below_safety_margin(147628<238562), p_lower_below_threshold(0.14<0.75) |
| 53381677 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.015042 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1355 €) | — | 1.26 | 0.138 (n=691) | REJECTED | below_safety_margin(189<300), p_lower_below_threshold(0.14<0.75) |
| 53381678 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.015042 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1355 €) | — | 1.26 | 0.138 (n=691) | REJECTED | below_safety_margin(189<300), p_lower_below_threshold(0.14<0.75) |
| 53381677 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.528775 WETH | 0.000068 WETH | 0.000000 WETH | 0.000003 WETH | 0.000065 WETH (0.1354 €) | — | 1.23 | 0.138 (n=691) | REJECTED | below_safety_margin(65014853912624<105755020338891), p_lower_below_threshold(0.14<0.75) |
| 53381678 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.528775 WETH | 0.000068 WETH | 0.000000 WETH | 0.000003 WETH | 0.000065 WETH (0.1354 €) | — | 1.23 | 0.138 (n=691) | REJECTED | below_safety_margin(65014853912624<105755020338891), p_lower_below_threshold(0.14<0.75) |
| 53386937 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.516383 WETH | 0.000066 WETH | 0.000000 WETH | 0.000003 WETH | 0.000063 WETH (0.1299 €) | — | 1.21 | 0.137 (n=704) | REJECTED | below_safety_margin(62508383618039<103276626781918), p_lower_below_threshold(0.14<0.75) |
| 53386937 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,225.839976 USDC | 0.147974 USDC | 0.000000 USDC | 0.007130 USDC | 0.140844 USDC (0.1296 €) | — | 1.15 | 0.137 (n=704) | REJECTED | below_safety_margin(140844<245167), p_lower_below_threshold(0.14<0.75) |
| 53386937 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.014465 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1295 €) | — | 1.25 | 0.137 (n=704) | REJECTED | below_safety_margin(181<289), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 4169 ; taux observé 0.127 ; borne inférieure crédible (0.9) 0.120 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
