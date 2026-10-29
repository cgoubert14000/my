# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T10:32:56+00:00 ; durée 58.24 min ; blocs 53238564 → 53240313 (1747 vus)

## Connexion
- Requêtes RPC : 20984 ; erreurs : 10 ; latence p50/p95 : 70.7/1,010.0 ms
- Rafraîchissements d'état : 1748 ; âge des données au dernier bloc : 1.24 s ; changements de frais LP observés (pools à frais dynamiques) : 1162
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11537 ; cycles déclenchés par événement : 1690 ; avance médiane sur le rafraîchissement multicall : 277 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,317.95 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 513 pools, 295 jetons, 18990 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 118, aerodrome 209, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 181 (rejetés 2) → 586 jetons ; pools candidats 3754 (énumérés 326, par paires 0), mesurés 515, sous le plancher de 10000.0 $ : 2 → gardés 513 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2317.952116, 'cbBTC': 80065.266817, 'AERO': 0.676266}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,065,628 | 2,317.952789 | 53240313 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,376,993 | 0.028939 | 53240313 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,701,565 | 0.000012 | 53240313 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,371,987 | 0.028932 | 53240313 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,259,605 | 2,318.755015 | 53240313 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,145,926 | 98.130932 | 53240313 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,957,465 | 0.001633 | 53240313 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,589,185 | 1.476338 | 53240313 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,752,274 | 0.028943 | 53240313 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 654 | 4,759,779 | 2,318.961052 | 53240313 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,392,515 | 2,318.736799 | 53240313 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,217,301 | 0.998890 | 53240313 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,645,666 | 37,834.168943 | 53240313 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,907,963 | 0.028948 | 53240313 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2775 | 2,472,665 | 98.099946 | 53240313 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 2,337,468 | 0.000012 | 53240313 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,117,656 | 1,214,695.556270 | 53240313 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,833,228 | 0.018971 | 53240313 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 1,814,938 | 2,315.739134 | 53240313 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,764,823 | 403.084788 | 53240313 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,754,953 | 0.000000 | 53240313 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,709,985 | 0.000012 | 53240313 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,697,966 | 0.000012 | 53240313 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 1,601,651 | 0.000012 | 53240313 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53240313 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,116 | 0.827421 | 53240313 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,427,904 | 3,424.016517 | 53240313 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,408,151 | 0.005409 | 53240313 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,372,520 | 13,928.857577 | 53240313 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,265,185 | 2,318.719018 | 53240313 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,222,534 | 0.000261 | 53240313 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,189,749 | 68.648579 | 53240313 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,142,031 | 36,689,161.244872 | 53240313 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,137,474 | 1,088,215.555665 | 53240313 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,130,586 | 0.000263 | 53240313 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,097,681 | 509,165.939207 | 53240313 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,077,961 | 0.000000 | 53240313 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,053,356 | 21,637,665.474315 | 53240313 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,049,802 | 74,429.996519 | 53240313 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 1,047,223 | 3,431.052727 | 53240313 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,040,940 | 16.950614 | 53240313 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,025,221 | 2,321.474375 | 53240313 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,011,582 | 61.175259 | 53240313 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 990,450 | 0.042304 | 53240313 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 989,250 | 98.784141 | 53240313 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 935,207 | 2,314.580420 | 53240313 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 914,459 | 1,066.143273 | 53240313 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 890,944 | 0.000554 | 53240313 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | QUID/USDC | 100 | 864,444 | 0.067804 | 53240313 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 863,719 | 18.506293 | 53240313 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/msETH (stable) | 500 | 856,985 | 2.328587 | 53240313 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 827,435 | 17.732343 | 53240313 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 784,491 | 0.803812 | 53240313 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 740,874 | 4,622,041.295914 | 53240313 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 739,423 | 0.000008 | 53240313 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 735,357 | 0.604928 | 53240313 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 692,802 | 140,995.567392 | 53240313 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 682,928 | 513,125.554923 | 53240313 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 648,995 | 0.531887 | 53240313 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 627,808 | 0.096975 | 53240313 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 3437 ; routes examinées : 65268630 ; candidats optimisés : 203388 ; net attendu > 0 : 66 ; dernier cycle 161.3 ms
- Rejets (moteur) : {'spread_below_threshold': 64271362, 'liquidity_below_min': 783569, 'negative_expected_net': 203322, 'unquotable': 6874, 'borrow_bound_too_small': 3437}
- Enregistrements de la session : 203388 ; net attendu > 0 : 66 ; simulés (eth_call de la vraie tx) : 8 (ok 7, échec 1) ; étiquettes ghost N+1 : 1/5 positives
- Décisions : {'REJECTED': 203388} ; motifs de rejet : {'below_safety_margin': 56, 'negative_expected_net': 203322, 'p_lower_below_threshold': 61, 'reliability_not_demonstrated': 5, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53238757 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 40.763407 USDC | 0.024719 USDC | 0.000000 USDC | 0.005204 USDC | 0.019515 USDC (0.0180 €) | — | 4.79 | 0.009 (n=156) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.033201 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0149 €) | 0.000007 WETH | 2.10 | 0.117 (n=430) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.033201 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0149 €) | 0.000007 WETH | 2.10 | 0.117 (n=430) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53239641 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 76.789386 USDC | 0.023141 USDC | 0.000000 USDC | 0.006965 USDC | 0.016176 USDC (0.0149 €) | 0.016176 USDC | 2.11 | 0.117 (n=430) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53239641 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 76.789386 USDC | 0.023141 USDC | 0.000000 USDC | 0.006965 USDC | 0.016176 USDC (0.0149 €) | 0.016176 USDC | 2.11 | 0.117 (n=430) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.032684 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0141 €) | 0.000007 WETH | 2.03 | 0.117 (n=430) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.032684 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0141 €) | 0.000007 WETH | 2.03 | 0.117 (n=430) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53239641 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 75.105168 USDC | 0.022324 USDC | 0.000000 USDC | 0.006965 USDC | 0.015359 USDC (0.0141 €) | — | 2.04 | 0.117 (n=430) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53239641 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 75.105168 USDC | 0.022324 USDC | 0.000000 USDC | 0.006965 USDC | 0.015359 USDC (0.0141 €) | — | 2.04 | 0.117 (n=430) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.030012 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0127 €) | — | 1.98 | 0.165 (n=223) | REJECTED | below_safety_margin(5941873731533<6002426005418), p_lower_below_threshold(0.17<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.030012 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0127 €) | — | 1.98 | 0.165 (n=223) | REJECTED | below_safety_margin(5941873731533<6002426005418), p_lower_below_threshold(0.17<0.75) |
| 53239641 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 69.398813 USDC | 0.020736 USDC | 0.000000 USDC | 0.006965 USDC | 0.013771 USDC (0.0127 €) | — | 1.98 | 0.165 (n=223) | REJECTED | below_safety_margin(13771<13879), p_lower_below_threshold(0.17<0.75) |
| 53239641 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 69.398813 USDC | 0.020736 USDC | 0.000000 USDC | 0.006965 USDC | 0.013771 USDC (0.0127 €) | — | 1.98 | 0.165 (n=223) | REJECTED | below_safety_margin(13771<13879), p_lower_below_threshold(0.17<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.029482 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0120 €) | — | 1.91 | 0.117 (n=430) | REJECTED | below_safety_margin(5623897578786<5896310132719), p_lower_below_threshold(0.12<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.029482 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0120 €) | — | 1.91 | 0.117 (n=430) | REJECTED | below_safety_margin(5623897578786<5896310132719), p_lower_below_threshold(0.12<0.75) |
| 53239641 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 68.142221 USDC | 0.019999 USDC | 0.000000 USDC | 0.006965 USDC | 0.013034 USDC (0.0120 €) | — | 1.91 | 0.117 (n=430) | REJECTED | below_safety_margin(13034<13628), p_lower_below_threshold(0.12<0.75) |
| 53239641 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 68.142221 USDC | 0.019999 USDC | 0.000000 USDC | 0.006965 USDC | 0.013034 USDC (0.0120 €) | — | 1.91 | 0.117 (n=430) | REJECTED | below_safety_margin(13034<13628), p_lower_below_threshold(0.12<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.026335 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0069 €) | — | 1.23 | 0.117 (n=430) | REJECTED | below_safety_margin(3230492056479<5267087249953), p_lower_below_threshold(0.12<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.026335 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0069 €) | — | 1.23 | 0.117 (n=430) | REJECTED | below_safety_margin(3230492056479<5267087249953), p_lower_below_threshold(0.12<0.75) |
| 53239641 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 60.719040 USDC | 0.014451 USDC | 0.000000 USDC | 0.006965 USDC | 0.007486 USDC (0.0069 €) | — | 1.23 | 0.117 (n=430) | REJECTED | below_safety_margin(7486<12143), p_lower_below_threshold(0.12<0.75) |
| 53239641 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 60.719040 USDC | 0.014451 USDC | 0.000000 USDC | 0.006965 USDC | 0.007486 USDC (0.0069 €) | — | 1.23 | 0.117 (n=430) | REJECTED | below_safety_margin(7486<12143), p_lower_below_threshold(0.12<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.023893 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0054 €) | — | 1.06 | 0.165 (n=223) | REJECTED | below_safety_margin(2541514095951<4778568314611), p_lower_below_threshold(0.17<0.75) |
| 53239641 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.023893 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0054 €) | — | 1.06 | 0.165 (n=223) | REJECTED | below_safety_margin(2541514095951<4778568314611), p_lower_below_threshold(0.17<0.75) |
| 53239641 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 55.133536 USDC | 0.012855 USDC | 0.000000 USDC | 0.006965 USDC | 0.005890 USDC (0.0054 €) | — | 1.07 | 0.165 (n=223) | REJECTED | below_safety_margin(5890<11026), p_lower_below_threshold(0.17<0.75) |
| 53239641 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 55.133536 USDC | 0.012855 USDC | 0.000000 USDC | 0.006965 USDC | 0.005890 USDC (0.0054 €) | — | 1.07 | 0.165 (n=223) | REJECTED | below_safety_margin(5890<11026), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 3106 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
