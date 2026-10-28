# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T12:12:31+00:00 ; durée 64.51 min ; blocs 53198162 → 53200097 (1908 vus)

## Connexion
- Requêtes RPC : 22772 ; erreurs : 18 ; latence p50/p95 : 251.9/1,205.1 ms
- Rafraîchissements d'état : 1908 ; âge des données au dernier bloc : 7.79 s ; changements de frais LP observés (pools à frais dynamiques) : 2212
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 19013 ; cycles déclenchés par événement : 1753 ; avance médiane sur le rafraîchissement multicall : 1,208 ms
- Gaz : base fee 0.005118 gwei ; prix ETH (pool le plus profond) : 2,352.29 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 525 pools, 303 jetons, 18974 routes
- Par DEX : uniswap_v3 148, aerodrome_slipstream 121, aerodrome 211, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 186 (rejetés 2) → 591 jetons ; pools candidats 3816 (énumérés 332, par paires 0), mesurés 527, sous le plancher de 10000.0 $ : 2 → gardés 525 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2367.672797, 'cbBTC': 81332.776577, 'AERO': 0.700175}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,055,607 | 2,352.285765 | 53200097 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,651,701 | 0.028985 | 53200097 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,834,244 | 0.000012 | 53200097 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,493,724 | 0.029057 | 53200097 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,464,299 | 2,346.355174 | 53200097 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,346,866 | 96.338172 | 53200097 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 7,221,281 | 1.426163 | 53200097 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,082,479 | 0.001648 | 53200097 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,750,180 | 0.028974 | 53200097 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 922 | 5,005,497 | 2,345.588025 | 53200097 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,450,796 | 2,345.454278 | 53200097 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,273,009 | 0.998874 | 53200097 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,773,019 | 36,382.172934 | 53200097 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 2,961,574 | 0.029044 | 53200097 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,545,252 | 96.318185 | 53200097 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 2,465,195 | 0.000012 | 53200097 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,146,557 | 1,217,487.019299 | 53200097 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,862,359 | 2,347.259190 | 53200097 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,835,464 | 0.018917 | 53200097 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,802,371 | 0.000000 | 53200097 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,790,971 | 400.185125 | 53200097 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,725,414 | 0.000012 | 53200097 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 1,702,349 | 0.000012 | 53200097 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,695,707 | 0.000012 | 53200097 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,513,071 | 0.005789 | 53200097 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,274 | 1.655260 | 53200097 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,463,956 | 3,355.735174 | 53200097 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,097 | 0.826865 | 53200097 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,394,934 | 13,793.374922 | 53200097 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,253,857 | 0.000267 | 53200097 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,238,714 | 2,346.351777 | 53200097 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,206,855 | 3,355.250368 | 53200097 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,193,895 | 68.172568 | 53200097 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,185,040 | 0.000267 | 53200097 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,164,367 | 1,070,201.036586 | 53200097 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,163,807 | 36,234,123.650805 | 53200097 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,152,774 | 0.000000 | 53200097 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,117,493 | 504,705.178922 | 53200097 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,108,578 | 20,917,744.539074 | 53200097 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,076,433 | 72,962.789008 | 53200097 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,050,045 | 16.557093 | 53200097 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,039,813 | 57.897831 | 53200097 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 1,005,010 | 96.901501 | 53200097 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 1,000,038 | 0.041048 | 53200097 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 940,586 | 2,360.576085 | 53200097 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 929,896 | 1,067.448651 | 53200097 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 907,408 | 0.000558 | 53200097 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 883,211 | 2.332609 | 53200097 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4555 | 880,751 | 17.924092 | 53200097 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 850,170 | 2,352.759845 | 53200097 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 848,584 | 17.492966 | 53200097 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 807,916 | 0.058612 | 53200097 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 796,424 | 0.803180 | 53200097 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 759,943 | 0.000009 | 53200097 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 751,323 | 0.626870 | 53200097 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 751,013 | 4,631,668.741584 | 53200097 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 720,381 | 134,268.925179 | 53200097 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 696,100 | 501,733.318550 | 53200097 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 670,543 | 0.107802 | 53200097 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 651,407 | 0.536347 | 53200097 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 3660 ; routes examinées : 69444840 ; candidats optimisés : 289502 ; net attendu > 0 : 82 ; dernier cycle 879.8 ms
- Rejets (moteur) : {'spread_below_threshold': 67826345, 'liquidity_below_min': 1324726, 'negative_expected_net': 289420, 'borrow_bound_too_small': 3658, 'cycle_budget_exhausted': 609}
- Enregistrements de la session : 289502 ; net attendu > 0 : 82 ; simulés (eth_call de la vraie tx) : 9 (ok 1, échec 8) ; étiquettes ghost N+1 : 1/6 positives
- Décisions : {'REJECTED': 289502} ; motifs de rejet : {'below_safety_margin': 64, 'negative_expected_net': 289420, 'p_lower_below_threshold': 70, 'reliability_not_demonstrated': 12, 'simulation_failed': 8, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53199512 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 111.039812 USDC | 0.179775 USDC | 0.000000 USDC | 0.005316 USDC | 0.174459 USDC (0.1605 €) | — | 15.71 | 0.000 (n=58) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53199823 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.491950 WETH | 0.000031 WETH | 0.000000 WETH | 0.000002 WETH | 0.000029 WETH (0.0629 €) | — | 0.59 | 0.026 (n=110) | REJECTED | below_safety_margin(28936252376355<98390013216214), p_lower_below_threshold(0.03<0.75) |
| 53199823 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,159.092536 USDC | 0.073774 USDC | 0.000000 USDC | 0.005687 USDC | 0.068087 USDC (0.0626 €) | — | 0.59 | 0.026 (n=110) | REJECTED | below_safety_margin(68087<231818), p_lower_below_threshold(0.03<0.75) |
| 53198655 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000372 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0547 €) | — | 19.62 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.013055 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0542 €) | — | 19.08 | 0.000 (n=65) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53198655 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000537 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0532 €) | — | 13.23 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 48.139367 USDC | 0.064903 USDC | 0.000000 USDC | 0.007118 USDC | 0.057785 USDC (0.0532 €) | — | 12.00 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.013055 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0517 €) | — | 18.22 | 0.000 (n=65) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53198655 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000346 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0517 €) | — | 19.92 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000374 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0517 €) | — | 18.44 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.012296 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0511 €) | — | 19.11 | 0.000 (n=65) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53198655 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000373 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0487 €) | — | 17.44 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.012296 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0483 €) | — | 18.05 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000489 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0382 €) | — | 10.43 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 40.356372 USDC | 0.048173 USDC | 0.000000 USDC | 0.007118 USDC | 0.041055 USDC (0.0378 €) | — | 10.17 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53199512 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 49.113470 USDC | 0.035056 USDC | 0.000000 USDC | 0.005316 USDC | 0.029740 USDC (0.0274 €) | — | 6.06 | 0.005 (n=150) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53199513 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 49.113470 USDC | 0.035056 USDC | 0.000000 USDC | 0.005316 USDC | 0.029740 USDC (0.0274 €) | — | 6.06 | 0.005 (n=150) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53199513 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 49.113470 USDC | 0.035056 USDC | 0.000000 USDC | 0.005316 USDC | 0.029740 USDC (0.0274 €) | 0.029740 USDC | 6.06 | 0.009 (n=151) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53199532 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 37.493937 USDC | 0.020257 USDC | 0.000000 USDC | 0.005317 USDC | 0.014940 USDC (0.0137 €) | — | 3.98 | 0.009 (n=151) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53199447 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 30.971822 USDC | 0.014100 USDC | 0.000000 USDC | 0.005317 USDC | 0.008783 USDC (0.0081 €) | — | 2.84 | 0.026 (n=109) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53199823 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.079059 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0071 €) | — | 0.41 | 0.013 (n=23) | REJECTED | below_safety_margin(3271387487448<15811732896822), reliability_not_demonstrated |
| 53199823 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 185.402244 USDC | 0.013368 USDC | 0.000000 USDC | 0.005687 USDC | 0.007681 USDC (0.0071 €) | — | 0.41 | 0.013 (n=23) | REJECTED | below_safety_margin(7681<37080), reliability_not_demonstrated |
| 53199822 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.027767 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0065 €) | — | 1.07 | 0.125 (n=404) | REJECTED | below_safety_margin(2969227372641<5553480541158), p_lower_below_threshold(0.12<0.75) |
| 53199823 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.027767 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0065 €) | — | 1.07 | 0.125 (n=404) | REJECTED | below_safety_margin(2969227372641<5553480541158), p_lower_below_threshold(0.12<0.75) |
| 53199823 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.027617 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0064 €) | — | 1.07 | 0.125 (n=404) | REJECTED | below_safety_margin(2963344142044<5523495233966), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 2938 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
