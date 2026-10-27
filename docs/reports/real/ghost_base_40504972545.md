# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T17:48:21+00:00 ; durée 306.1 min ; blocs 53157790 → 53166972 (8983 vus)

## Connexion
- Requêtes RPC : 105545 ; erreurs : 50 ; latence p50/p95 : 248.9/1,909.0 ms
- Rafraîchissements d'état : 8984 ; âge des données au dernier bloc : 1.96 s ; changements de frais LP observés (pools à frais dynamiques) : 15545
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 90625 ; cycles déclenchés par événement : 6090 ; avance médiane sur le rafraîchissement multicall : 554 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,348.44 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 301 jetons, 19174 routes
- Par DEX : uniswap_v3 145, aerodrome 212, aerodrome_slipstream 123, pancakeswap_v3 28, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 188 (rejetés 2) → 593 jetons ; pools candidats 3787 (énumérés 335, par paires 0), mesurés 527, sous le plancher de 10000.0 $ : 3 → gardés 524 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2324.722428, 'cbBTC': 80182.929325, 'AERO': 0.68845}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,511,880 | 2,348.441593 | 53166972 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,615,828 | 0.029147 | 53166972 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,197,921 | 0.029106 | 53166972 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,641,071 | 0.000012 | 53166972 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,627,328 | 90.834448 | 53166972 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,435,399 | 2,349.120339 | 53166972 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,051,031 | 1.426238 | 53166972 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,008,441 | 0.001638 | 53166972 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,412,824 | 0.029151 | 53166972 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,077,441 | 2,349.180713 | 53166972 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,491,644 | 2,349.013249 | 53166972 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,244,003 | 0.998745 | 53166972 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,721,813 | 37,268.056216 | 53166972 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,002,864 | 0.029122 | 53166972 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,575,443 | 90.809791 | 53166972 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,366,821 | 2,349.847261 | 53166972 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,198,451 | 0.000012 | 53166972 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,145,604 | 1,214,589.168919 | 53166972 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,856,709 | 0.000000 | 53166972 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,828,952 | 0.018695 | 53166972 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,788,430 | 399.505341 | 53166972 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,695,696 | 0.000012 | 53166972 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,686,214 | 0.000012 | 53166972 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,681,321 | 0.000012 | 53166972 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,531,555 | 0.005887 | 53166972 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,016 | 0.826585 | 53166972 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,460,351 | 3,353.671920 | 53166972 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,146 | 1.698043 | 53166972 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,388,783 | 13,698.095080 | 53166972 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,252,123 | 0.000267 | 53166972 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,251,075 | 2,349.130717 | 53166972 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,218,353 | 3,328.970099 | 53166972 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,201,201 | 67.345844 | 53166972 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,184,867 | 0.000266 | 53166972 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,171,348 | 35,382,703.435446 | 53166972 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,160,126 | 1,074,547.000565 | 53166972 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,148,186 | 0.000000 | 53166972 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,117,277 | 502,640.698009 | 53166972 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,079,657 | 72,298.179112 | 53166972 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,051,703 | 21,123,207.055875 | 53166972 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,035,559 | 17.188145 | 53166972 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,033,929 | 0.038660 | 53166972 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 1,025,516 | 59.523325 | 53166972 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 944,382 | 2,331.655283 | 53166972 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 911,960 | 1,087.864077 | 53166972 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 906,805 | 0.000559 | 53166972 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 899,677 | 91.133002 | 53166972 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/msETH (stable) | 500 | 886,153 | 2.315658 | 53166972 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 880,416 | 17.931797 | 53166972 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 850,091 | 2,354.838310 | 53166972 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 840,291 | 17.671173 | 53166972 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 811,420 | 0.000009 | 53166972 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 802,489 | 0.057784 | 53166972 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 795,123 | 0.803179 | 53166972 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 755,981 | 4,555,639.310578 | 53166972 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 750,288 | 0.625842 | 53166972 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 702,865 | 140,524.440802 | 53166972 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2105 | 697,303 | 500,113.538587 | 53166972 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 680,388 | 0.583054 | 53166972 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,851 | 0.108958 | 53166972 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 15073 ; routes examinées : 289009702 ; candidats optimisés : 975297 ; net attendu > 0 : 426 ; dernier cycle 335.3 ms
- Rejets (moteur) : {'spread_below_threshold': 284308151, 'liquidity_below_min': 3635358, 'negative_expected_net': 974871, 'borrow_bound_too_small': 88706, 'cycle_budget_exhausted': 2190}
- Enregistrements de la session : 975297 ; net attendu > 0 : 426 ; simulés (eth_call de la vraie tx) : 25 (ok 7, échec 18) ; étiquettes ghost N+1 : 3/24 positives
- Décisions : {'REJECTED': 975297} ; motifs de rejet : {'below_safety_margin': 350, 'negative_expected_net': 974871, 'p_lower_below_threshold': 400, 'reliability_not_demonstrated': 26, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 18, 'stale_data': 38}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53163475 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.004089 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2877 €) | — | 9.51 | 0.000 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53163475 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.146914 WETH | 0.000136 WETH | 0.000000 WETH | 0.000003 WETH | 0.000133 WETH (0.2868 €) | — | 9.05 | 0.000 (n=61) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53163475 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 272.922832 USDC | 0.240492 USDC | 0.000000 USDC | 0.007090 USDC | 0.233402 USDC (0.2147 €) | — | 8.55 | 0.000 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53163475 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003154 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2145 €) | — | 9.19 | 0.000 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53159906 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.794482 WETH | 0.000094 WETH | 0.000000 WETH | 0.000002 WETH | 0.000091 WETH (0.1957 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(91426168727046<158896479878237), p_lower_below_threshold(0.02<0.75) |
| 53159907 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.794482 WETH | 0.000094 WETH | 0.000000 WETH | 0.000002 WETH | 0.000091 WETH (0.1957 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(91426168727046<158896479878237), p_lower_below_threshold(0.02<0.75) |
| 53159906 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,843.634528 USDC | 0.217677 USDC | 0.000000 USDC | 0.005610 USDC | 0.212067 USDC (0.1951 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(212067<368726), p_lower_below_threshold(0.02<0.75) |
| 53159907 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,843.634528 USDC | 0.217677 USDC | 0.000000 USDC | 0.005610 USDC | 0.212067 USDC (0.1951 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(212067<368726), p_lower_below_threshold(0.02<0.75) |
| 53163475 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002668 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1708 €) | — | 8.66 | 0.000 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53163475 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.095794 WETH | 0.000082 WETH | 0.000000 WETH | 0.000003 WETH | 0.000079 WETH (0.1701 €) | — | 8.23 | 0.000 (n=61) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53163475 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002651 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1523 €) | — | 7.77 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 218.103405 USDC | 0.172592 USDC | 0.000000 USDC | 0.007090 USDC | 0.165502 USDC (0.1523 €) | — | 7.59 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002524 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1220 €) | — | 6.54 | 0.094 (n=302) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53163475 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.087276 WETH | 0.000059 WETH | 0.000000 WETH | 0.000003 WETH | 0.000056 WETH (0.1216 €) | — | 6.46 | 0.094 (n=302) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53162545 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,457.453219 USDC | 0.137624 USDC | 0.000000 USDC | 0.005604 USDC | 0.132020 USDC (0.1215 €) | — | 0.91 | 0.020 (n=106) | REJECTED | below_safety_margin(132020<291490), p_lower_below_threshold(0.02<0.75) |
| 53162547 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,457.453219 USDC | 0.137624 USDC | 0.000000 USDC | 0.005604 USDC | 0.132020 USDC (0.1215 €) | — | 0.91 | 0.020 (n=106) | REJECTED | below_safety_margin(132020<291490), p_lower_below_threshold(0.02<0.75) |
| 53162545 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.624317 WETH | 0.000059 WETH | 0.000000 WETH | 0.000002 WETH | 0.000056 WETH (0.1211 €) | — | 0.90 | 0.020 (n=106) | REJECTED | below_safety_margin(56476157983539<124863325293708), p_lower_below_threshold(0.02<0.75) |
| 53162547 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.624317 WETH | 0.000059 WETH | 0.000000 WETH | 0.000002 WETH | 0.000056 WETH (0.1211 €) | — | 0.90 | 0.020 (n=106) | REJECTED | below_safety_margin(56476157983539<124863325293708), p_lower_below_threshold(0.02<0.75) |
| 53162317 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.102608 WETH | 0.000057 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1168 €) | — | 5.31 | 0.047 (n=45) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 53163475 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002260 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1124 €) | — | 6.73 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 183.933967 USDC | 0.129150 USDC | 0.000000 USDC | 0.007090 USDC | 0.122060 USDC (0.1123 €) | — | 6.64 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 196.102605 USDC | 0.127845 USDC | 0.000000 USDC | 0.007090 USDC | 0.120755 USDC (0.1111 €) | — | 6.16 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002307 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1109 €) | — | 6.50 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002404 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1050 €) | — | 5.91 | 0.094 (n=302) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53163475 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.087276 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1050 €) | — | 5.58 | 0.094 (n=302) | REJECTED | p_lower_below_threshold(0.09<0.75) |

## Fiabilité et décision
- Observations ghost : 2856 ; taux observé 0.090 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
