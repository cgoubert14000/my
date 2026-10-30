# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T13:47:56+00:00 ; durée 6.03 min ; blocs 53289181 → 53289364 (181 vus)

## Connexion
- Requêtes RPC : 2179 ; erreurs : 0 ; latence p50/p95 : 65.8/834.5 ms
- Rafraîchissements d'état : 182 ; âge des données au dernier bloc : 1.65 s ; changements de frais LP observés (pools à frais dynamiques) : 520
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4590 ; cycles déclenchés par événement : 231 ; avance médiane sur le rafraîchissement multicall : 125 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,221.95 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 287 jetons, 18738 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 206, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2224.464255, 'cbBTC': 77004.393698, 'AERO': 0.620215}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,491,011 | 2,221.954788 | 53289364 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,046,388 | 0.028872 | 53289364 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,556,964 | 0.000013 | 53289364 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,987,366 | 0.028860 | 53289364 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,085,698 | 2,217.531115 | 53289364 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,724,085 | 100.151390 | 53289364 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,644,950 | 0.001614 | 53289364 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,050,134 | 1.616507 | 53289364 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,518,769 | 0.028872 | 53289364 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 833 | 4,180,678 | 2,216.779480 | 53289364 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,048,477 | 0.999934 | 53289364 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,027,014 | 2,216.661641 | 53289364 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,539,536 | 36,881.324663 | 53289364 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,747,553 | 0.028852 | 53289364 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,308,446 | 100.181127 | 53289364 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,034,268 | 1,209,548.066080 | 53289364 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,913,684 | 0.000013 | 53289364 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,773,126 | 0.018332 | 53289364 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,696,534 | 0.000000 | 53289364 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,671,793 | 417.554306 | 53289364 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,658,547 | 0.000013 | 53289364 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,560,866 | 0.000013 | 53289364 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,530,499 | 2,222.801572 | 53289364 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,463,389 | 1.643209 | 53289364 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 1,460,590 | 0.000013 | 53289364 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,887 | 0.824971 | 53289364 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,396,103 | 3,589.558744 | 53289364 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,309,081 | 2,217.806590 | 53289364 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,300,194 | 14,464.258912 | 53289364 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,270,724 | 0.005028 | 53289364 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,178,067 | 70.016773 | 53289364 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,096,463 | 36,265,727.250085 | 53289364 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,048,622 | 515,016.534418 | 53289364 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,026,486 | 21,083,127.034335 | 53289364 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,006,194 | 74,483.061252 | 53289364 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,004,975 | 2,221.998250 | 53289364 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | DRB/WETH | 10000 | 997,656 | 0.000000 | 53289364 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,667 | 19.241885 | 53289364 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 968,598 | 66.726688 | 53289364 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 956,682 | 99.903238 | 53289364 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 953,513 | 0.045162 | 53289364 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 923,905 | 1,209,274.366068 | 53289364 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 916,929 | 2,231.397776 | 53289364 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 873,356 | 1,085.143287 | 53289364 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 859,436 | 3,587.716388 | 53289364 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 856,059 | 0.000556 | 53289364 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4600 | 831,763 | 19.647683 | 53289364 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 812,154 | 0.059236 | 53289364 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 783,518 | 17.950100 | 53289364 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 752,093 | 0.803616 | 53289364 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 725,232 | 0.000260 | 53289364 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 709,850 | 0.578961 | 53289364 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 707,464 | 4,659,524.114748 | 53289364 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 688,940 | 0.000008 | 53289364 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 676,979 | 2.330067 | 53289364 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2258 | 651,033 | 518,643.246105 | 53289364 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 650,470 | 147,091.457185 | 53289364 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 640,152 | 0.517611 | 53289364 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 604,168 | 0.091200 | 53289364 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 597,547 | 0.914771 | 53289364 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 412 ; routes examinées : 7720056 ; candidats optimisés : 41469 ; net attendu > 0 : 203 ; dernier cycle 382.0 ms
- Rejets (moteur) : {'spread_below_threshold': 7519704, 'liquidity_below_min': 154069, 'negative_expected_net': 41266, 'unquotable': 4402, 'borrow_bound_too_small': 412}
- Enregistrements de la session : 41469 ; net attendu > 0 : 203 ; simulés (eth_call de la vraie tx) : 9 (ok 7, échec 2) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 41469} ; motifs de rejet : {'below_safety_margin': 190, 'negative_expected_net': 41266, 'p_lower_below_threshold': 181, 'reliability_not_demonstrated': 22, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53289308 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.069651 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0254 €) | — | 1.78 | 0.163 (n=260) | REJECTED | below_safety_margin(12418220348479<13930177782132), p_lower_below_threshold(0.16<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.069651 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0254 €) | — | 1.78 | 0.163 (n=260) | REJECTED | below_safety_margin(12418220348479<13930177782132), p_lower_below_threshold(0.16<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 153.449517 USDC | 0.034317 USDC | 0.000000 USDC | 0.006814 USDC | 0.027503 USDC (0.0253 €) | — | 1.79 | 0.163 (n=260) | REJECTED | below_safety_margin(27503<30689), p_lower_below_threshold(0.16<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 153.449517 USDC | 0.034317 USDC | 0.000000 USDC | 0.006814 USDC | 0.027503 USDC (0.0253 €) | — | 1.79 | 0.163 (n=260) | REJECTED | below_safety_margin(27503<30689), p_lower_below_threshold(0.16<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.087989 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0226 €) | — | 1.26 | 0.137 (n=587) | REJECTED | below_safety_margin(11054198859110<17597794778243), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.087989 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0226 €) | — | 1.26 | 0.137 (n=587) | REJECTED | below_safety_margin(11054198859110<17597794778243), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 194.969906 USDC | 0.031292 USDC | 0.000000 USDC | 0.006814 USDC | 0.024478 USDC (0.0225 €) | — | 1.26 | 0.137 (n=587) | REJECTED | below_safety_margin(24478<38993), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 194.969906 USDC | 0.031292 USDC | 0.000000 USDC | 0.006814 USDC | 0.024478 USDC (0.0225 €) | — | 1.26 | 0.137 (n=587) | REJECTED | below_safety_margin(24478<38993), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.061192 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0193 €) | — | 1.54 | 0.137 (n=587) | REJECTED | below_safety_margin(9420108116413<12238423936110), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.061192 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0193 €) | — | 1.54 | 0.137 (n=587) | REJECTED | below_safety_margin(9420108116413<12238423936110), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 135.598893 USDC | 0.027673 USDC | 0.000000 USDC | 0.006814 USDC | 0.020859 USDC (0.0192 €) | — | 1.54 | 0.137 (n=587) | REJECTED | below_safety_margin(20859<27119), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 135.598893 USDC | 0.027673 USDC | 0.000000 USDC | 0.006814 USDC | 0.020859 USDC (0.0192 €) | — | 1.54 | 0.137 (n=587) | REJECTED | below_safety_margin(20859<27119), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.059869 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0170 €) | — | 1.39 | 0.163 (n=260) | REJECTED | below_safety_margin(8336129713696<11973719896332), p_lower_below_threshold(0.16<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.059869 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0170 €) | — | 1.39 | 0.163 (n=260) | REJECTED | below_safety_margin(8336129713696<11973719896332), p_lower_below_threshold(0.16<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 132.023925 USDC | 0.025269 USDC | 0.000000 USDC | 0.006814 USDC | 0.018455 USDC (0.0170 €) | — | 1.40 | 0.163 (n=260) | REJECTED | below_safety_margin(18455<26404), p_lower_below_threshold(0.16<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 132.023925 USDC | 0.025269 USDC | 0.000000 USDC | 0.006814 USDC | 0.018455 USDC (0.0170 €) | — | 1.40 | 0.163 (n=260) | REJECTED | below_safety_margin(18455<26404), p_lower_below_threshold(0.16<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.073128 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0147 €) | — | 0.99 | 0.137 (n=587) | REJECTED | below_safety_margin(7214824568582<14625650967256), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.073128 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0147 €) | — | 0.99 | 0.137 (n=587) | REJECTED | below_safety_margin(7214824568582<14625650967256), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 162.133909 USDC | 0.022784 USDC | 0.000000 USDC | 0.006814 USDC | 0.015970 USDC (0.0147 €) | — | 0.98 | 0.137 (n=587) | REJECTED | below_safety_margin(15970<32426), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 162.133909 USDC | 0.022784 USDC | 0.000000 USDC | 0.006814 USDC | 0.015970 USDC (0.0147 €) | — | 0.98 | 0.137 (n=587) | REJECTED | below_safety_margin(15970<32426), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.071553 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0123 €) | — | 0.84 | 0.137 (n=587) | REJECTED | below_safety_margin(6030193896602<14310574684974), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.071553 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0123 €) | — | 0.84 | 0.137 (n=587) | REJECTED | below_safety_margin(6030193896602<14310574684974), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 156.664740 USDC | 0.020158 USDC | 0.000000 USDC | 0.006814 USDC | 0.013344 USDC (0.0123 €) | — | 0.85 | 0.137 (n=587) | REJECTED | below_safety_margin(13344<31332), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 156.664740 USDC | 0.020158 USDC | 0.000000 USDC | 0.006814 USDC | 0.013344 USDC (0.0123 €) | — | 0.85 | 0.137 (n=587) | REJECTED | below_safety_margin(13344<31332), p_lower_below_threshold(0.14<0.75) |
| 53289230 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001653 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0113 €) | — | 0.97 | 0.137 (n=587) | REJECTED | below_safety_margin(16<33), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3656 ; taux observé 0.116 ; borne inférieure crédible (0.9) 0.109 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
