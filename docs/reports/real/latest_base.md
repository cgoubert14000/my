# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T02:51:47+00:00 ; durée 142.25 min ; blocs 53481408 → 53485676 (4190 vus)

## Connexion
- Requêtes RPC : 49191 ; erreurs : 145 ; latence p50/p95 : 299.2/965.9 ms
- Rafraîchissements d'état : 4190 ; âge des données au dernier bloc : 4.11 s ; changements de frais LP observés (pools à frais dynamiques) : 8854
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 55122 ; cycles déclenchés par événement : 4393 ; avance médiane sur le rafraîchissement multicall : 490 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,257.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 282 jetons, 19430 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 105, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3703 (énumérés 305, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2264.542979, 'cbBTC': 77119.048638, 'AERO': 0.629628}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,623,553 | 2,257.422257 | 53485676 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,555,982 | 0.029426 | 53485676 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,097,843 | 0.029422 | 53485676 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,019,103 | 0.000013 | 53485676 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,973,264 | 2,251.765865 | 53485676 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,593,366 | 103.464442 | 53485676 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,513,298 | 0.001561 | 53485676 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,379,443 | 1.591731 | 53485676 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,745,684 | 0.029420 | 53485676 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,179,401 | 2,251.360300 | 53485676 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,035,866 | 0.999906 | 53485676 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,831,332 | 2,251.288776 | 53485676 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,405,657 | 41,118.694066 | 53485676 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,651,698 | 0.029409 | 53485676 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,133,042 | 1,135,523.265555 | 53485676 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,079,917 | 103.436545 | 53485676 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,800,164 | 0.000013 | 53485676 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,720,843 | 0.017489 | 53485676 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,690,469 | 0.006976 | 53485676 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,656,714 | 0.000000 | 53485676 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,606,345 | 0.000013 | 53485676 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53485676 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,534,535 | 441.585339 | 53485676 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,534,335 | 0.000013 | 53485676 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,498,468 | 2,257.698315 | 53485676 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,931 | 0.819444 | 53485676 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,412,905 | 3,590.706838 | 53485676 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,341,544 | 2,251.767493 | 53485676 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,332,410 | 2,257.386607 | 53485676 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,276,903 | 14,995.339977 | 53485676 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,309 | 72.425481 | 53485676 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,109,758 | 36,969,258.567437 | 53485676 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,040,666 | 0.000000 | 53485676 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,039,725 | 551,665.517425 | 53485676 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,018,327 | 22,061,795.042039 | 53485676 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,561 | 19.250277 | 53485676 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 950,095 | 86,121.555971 | 53485676 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 941,624 | 102.803201 | 53485676 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 941,448 | 1,053.201861 | 53485676 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 933,499 | 0.000013 | 53485676 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 930,869 | 72.247469 | 53485676 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 924,351 | 2,273.536741 | 53485676 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 913,993 | 1,272,501.139785 | 53485676 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 865,966 | 0.045917 | 53485676 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,854 | 0.000551 | 53485676 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 838,520 | 3,608.039436 | 53485676 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4530 | 813,166 | 20.355027 | 53485676 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 788,066 | 0.055583 | 53485676 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 766,230 | 0.799140 | 53485676 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 729,391 | 0.577232 | 53485676 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 717,280 | 0.000257 | 53485676 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 700,114 | 4,916,699.189952 | 53485676 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 667,251 | 0.000008 | 53485676 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 657,751 | 0.543911 | 53485676 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 656,727 | 149,196.428767 | 53485676 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 649,415 | 2.364095 | 53485676 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 638,087 | 555,668.496344 | 53485676 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 606,600 | 0.914029 | 53485676 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 581,077 | 0.085830 | 53485676 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 557,020 | 0.037761 | 53485676 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 8582 ; routes examinées : 166748260 ; candidats optimisés : 551327 ; net attendu > 0 : 586 ; dernier cycle 363.4 ms
- Rejets (moteur) : {'spread_below_threshold': 164017644, 'liquidity_below_min': 2169322, 'negative_expected_net': 550741, 'borrow_bound_too_small': 8558, 'cycle_budget_exhausted': 1409}
- Enregistrements de la session : 551327 ; net attendu > 0 : 586 ; simulés (eth_call de la vraie tx) : 48 (ok 8, échec 40) ; étiquettes ghost N+1 : 6/38 positives
- Décisions : {'REJECTED': 551327} ; motifs de rejet : {'below_safety_margin': 452, 'negative_expected_net': 550741, 'p_lower_below_threshold': 552, 'reliability_not_demonstrated': 34, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 1, 'simulation_failed': 40, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53483785 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDbC→[uniswap_v3]→WETH | 0.045371 WETH | 0.000113 WETH | 0.000000 WETH | 0.000003 WETH | 0.000110 WETH (0.2285 €) | — | 24.18 | 0.059 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53483785 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDbC→[aerodrome_slipstream]→USDC | 118.789241 USDC | 0.222605 USDC | 0.000000 USDC | 0.006487 USDC | 0.216118 USDC (0.1988 €) | — | 18.19 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53483742 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.074462 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1802 €) | — | 11.62 | 0.101 (n=116) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53483742 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 167.964391 USDC | 0.202602 USDC | 0.000000 USDC | 0.007143 USDC | 0.195459 USDC (0.1798 €) | — | 11.64 | 0.101 (n=116) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53483742 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.073580 WETH | 0.000088 WETH | 0.000000 WETH | 0.000003 WETH | 0.000085 WETH (0.1764 €) | — | 11.51 | 0.101 (n=116) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53483742 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 166.124342 USDC | 0.198491 USDC | 0.000000 USDC | 0.007143 USDC | 0.191348 USDC (0.1760 €) | — | 11.52 | 0.101 (n=116) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53483742 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.067052 WETH | 0.000076 WETH | 0.000000 WETH | 0.000003 WETH | 0.000073 WETH (0.1516 €) | — | 10.86 | 0.101 (n=116) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53483742 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 151.170591 USDC | 0.171593 USDC | 0.000000 USDC | 0.007143 USDC | 0.164450 USDC (0.1513 €) | — | 10.88 | 0.101 (n=116) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53483785 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.019952 WETH | 0.000068 WETH | 0.000000 WETH | 0.000003 WETH | 0.000065 WETH (0.1357 €) | — | 32.67 | 0.059 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53483785 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH | 0.021499 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000063 WETH (0.1304 €) | — | 29.12 | 0.059 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53483785 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.021103 WETH | 0.000063 WETH | 0.000000 WETH | 0.000003 WETH | 0.000060 WETH (0.1255 €) | — | 28.56 | 0.059 (n=14) | REJECTED | reliability_not_demonstrated |
| 53483785 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH | 0.019239 WETH | 0.000058 WETH | 0.000000 WETH | 0.000003 WETH | 0.000055 WETH (0.1155 €) | — | 28.82 | 0.075 (n=4) | REJECTED | reliability_not_demonstrated |
| 53483785 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH | 0.018264 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1023 €) | — | 26.91 | 0.059 (n=14) | REJECTED | reliability_not_demonstrated |
| 53483742 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.056994 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1022 €) | — | 8.61 | 0.101 (n=116) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53483742 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 128.192791 USDC | 0.117899 USDC | 0.000000 USDC | 0.007143 USDC | 0.110756 USDC (0.1019 €) | — | 8.64 | 0.101 (n=116) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53483742 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.043036 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1017 €) | — | 11.35 | 0.101 (n=116) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53483742 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 97.050951 USDC | 0.117388 USDC | 0.000000 USDC | 0.007143 USDC | 0.110245 USDC (0.1014 €) | — | 11.36 | 0.101 (n=116) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53483742 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.056445 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1013 €) | — | 8.62 | 0.101 (n=116) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53483742 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 127.250662 USDC | 0.116951 USDC | 0.000000 USDC | 0.007143 USDC | 0.109808 USDC (0.1010 €) | — | 8.63 | 0.101 (n=116) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53483785 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→VIRTUAL→[aerodrome]→cbBTC | 0.000482 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0885 €) | — | 25.94 | 0.007 (n=116) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53483785 | USDC→[uniswap_v3]→AERO→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 37.581875 USDC | 0.093077 USDC | 0.000000 USDC | 0.006487 USDC | 0.086590 USDC (0.0797 €) | — | 23.04 | 0.059 (n=14) | REJECTED | reliability_not_demonstrated |
| 53483742 | WETH→[aerodrome]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.042943 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0683 €) | — | 7.64 | 0.305 (n=144) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 53483742 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 96.590715 USDC | 0.080812 USDC | 0.000000 USDC | 0.006830 USDC | 0.073982 USDC (0.0681 €) | — | 7.66 | 0.305 (n=144) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 53483557 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.070155 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0642 €) | — | 4.39 | 0.157 (n=613) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53483557 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001851 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0637 €) | — | 4.86 | 0.157 (n=613) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 4978 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
