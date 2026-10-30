# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T07:58:27+00:00 ; durée 330.32 min ; blocs 53268968 → 53278871 (9514 vus)

## Connexion
- Requêtes RPC : 114296 ; erreurs : 335 ; latence p50/p95 : 65.7/1,142.3 ms
- Rafraîchissements d'état : 9515 ; âge des données au dernier bloc : 1.97 s ; changements de frais LP observés (pools à frais dynamiques) : 20296
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 151347 ; cycles déclenchés par événement : 11014 ; avance médiane sur le rafraîchissement multicall : 405 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,234.51 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 287 jetons, 18448 routes
- Par DEX : uniswap_v3 134, aerodrome 205, aerodrome_slipstream 111, pancakeswap_v3 28 (quarantaine 1), uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 314, par paires 0), mesurés 494, sous le plancher de 10000.0 $ : 2 → gardés 492 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2206.596047, 'cbBTC': 77084.188033, 'AERO': 0.611873}
- Pools en quarantaine : 1 — pancakeswap_v3:WETH/EURC@0xb4a43D: simulation failed ×5 (model/chain mismatch) — until block 53278911

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,289,813 | 2,234.510994 | 53278871 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,133,570 | 0.028603 | 53278871 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,521,759 | 0.000013 | 53278871 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,063,832 | 0.028627 | 53278871 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,096,478 | 2,231.111613 | 53278871 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,896,273 | 97.032797 | 53278871 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,768,336 | 0.001627 | 53278871 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,064,458 | 1.613799 | 53278871 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,581,840 | 0.028607 | 53278871 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,143,906 | 2,232.032976 | 53278871 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,111,792 | 0.999256 | 53278871 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,748,961 | 2,231.775709 | 53278871 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,572,033 | 36,623.754243 | 53278871 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,770,129 | 0.028619 | 53278871 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,362,970 | 97.065158 | 53278871 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,036,961 | 1,220,025.263374 | 53278871 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,934,373 | 0.000013 | 53278871 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,796,807 | 0.018781 | 53278871 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,680,614 | 417.981712 | 53278871 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,672,336 | 0.000000 | 53278871 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,670,489 | 0.000013 | 53278871 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,647,541 | 0.000013 | 53278871 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,539,788 | 2,236.445671 | 53278871 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,476,171 | 0.000013 | 53278871 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,464,202 | 1.642297 | 53278871 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,513 | 0.825814 | 53278871 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,394,384 | 3,599.216074 | 53278871 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,314,056 | 14,592.392235 | 53278871 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,299,025 | 0.005129 | 53278871 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,294,096 | 2,231.441125 | 53278871 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,178,305 | 69.988581 | 53278871 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,100,646 | 36,634,242.088427 | 53278871 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,053,586 | 516,035.322484 | 53278871 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,019,032 | 73,441.236956 | 53278871 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,013,387 | 21,772,283.244597 | 53278871 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v2 | WETH/USDC | 3000 | 1,007,782 | 2,234.758675 | 53278871 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | DRB/WETH | 10000 | 1,001,181 | 0.000000 | 53278871 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 997,170 | 19.102843 | 53278871 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 977,730 | 96.987659 | 53278871 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 954,722 | 68.680021 | 53278871 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 947,760 | 0.043503 | 53278871 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 944,062 | 3,600.937902 | 53278871 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/WELL | 10000 | 920,304 | 1,232,570.204532 | 53278871 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 914,088 | 2,231.397776 | 53278871 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 878,292 | 1,078.051975 | 53278871 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,745 | 0.000557 | 53278871 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 835,108 | 19.525733 | 53278871 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 817,231 | 0.060029 | 53278871 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 790,974 | 17.868824 | 53278871 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 756,343 | 0.803616 | 53278871 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 730,590 | 0.000259 | 53278871 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 708,258 | 0.579474 | 53278871 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 706,190 | 4,729,181.635584 | 53278871 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 693,467 | 0.000008 | 53278871 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 680,835 | 2.329979 | 53278871 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 654,001 | 518,482.651818 | 53278871 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 653,590 | 147,338.833224 | 53278871 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 648,007 | 0.529917 | 53278871 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 602,112 | 0.090742 | 53278871 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 600,739 | 0.915335 | 53278871 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 20528 ; routes examinées : 378700544 ; candidats optimisés : 1849355 ; net attendu > 0 : 2507 ; dernier cycle 209.3 ms
- Rejets (moteur) : {'spread_below_threshold': 370392968, 'liquidity_below_min': 5734927, 'negative_expected_net': 1846848, 'pool_quarantined': 679590, 'unquotable': 21883, 'borrow_bound_too_small': 20522, 'cycle_budget_exhausted': 1299}
- Enregistrements de la session : 1849355 ; net attendu > 0 : 2507 ; simulés (eth_call de la vraie tx) : 184 (ok 96, échec 88) ; étiquettes ghost N+1 : 6/115 positives
- Décisions : {'REJECTED': 1849355} ; motifs de rejet : {'below_safety_margin': 1731, 'negative_expected_net': 1846848, 'p_lower_below_threshold': 2250, 'reliability_not_demonstrated': 257, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 2, 'simulation_failed': 88, 'stale_data': 22}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53273243 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 910.657981 USDC | 1.498119 USDC | 0.000000 USDC | 0.006462 USDC | 1.491657 USDC (1.3723 €) | — | 16.38 | 0.033 (n=153) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53273243 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.406659 WETH | 0.000669 WETH | 0.000000 WETH | 0.000003 WETH | 0.000666 WETH (1.3701 €) | — | 16.37 | 0.033 (n=153) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53273243 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 878.630274 USDC | 1.422401 USDC | 0.000000 USDC | 0.006462 USDC | 1.415939 USDC (1.3027 €) | — | 16.12 | 0.079 (n=27) | REJECTED | reliability_not_demonstrated |
| 53273243 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.392266 WETH | 0.000635 WETH | 0.000000 WETH | 0.000003 WETH | 0.000632 WETH (1.3007 €) | — | 16.11 | 0.079 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53273243 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 489.246425 USDC | 1.288026 USDC | 0.000000 USDC | 0.007820 USDC | 1.280206 USDC (1.1778 €) | — | 26.17 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53273243 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.218464 WETH | 0.000575 WETH | 0.000000 WETH | 0.000003 WETH | 0.000571 WETH (1.1758 €) | — | 26.15 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53273243 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 481.373808 USDC | 1.254002 USDC | 0.000000 USDC | 0.007820 USDC | 1.246182 USDC (1.1465 €) | — | 25.89 | 0.013 (n=60) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53273243 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 1,126.922470 USDC | 1.252212 USDC | 0.000000 USDC | 0.006801 USDC | 1.245411 USDC (1.1458 €) | — | 11.05 | 0.079 (n=27) | REJECTED | reliability_not_demonstrated |
| 53273243 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.215031 WETH | 0.000560 WETH | 0.000000 WETH | 0.000003 WETH | 0.000556 WETH (1.1446 €) | — | 25.87 | 0.013 (n=60) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53273243 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.014302 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1437 €) | — | 11.14 | 0.079 (n=27) | REJECTED | reliability_not_demonstrated |
| 53273243 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 1,199.671056 USDC | 1.249553 USDC | 0.000000 USDC | 0.006462 USDC | 1.243091 USDC (1.1436 €) | — | 10.36 | 0.033 (n=153) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53273243 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.015054 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1416 €) | — | 10.56 | 0.033 (n=153) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53273243 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 1,155.395800 USDC | 1.243714 USDC | 0.000000 USDC | 0.006462 USDC | 1.237252 USDC (1.1383 €) | — | 10.71 | 0.033 (n=153) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53273243 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.014307 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1365 €) | — | 11.06 | 0.033 (n=153) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53273243 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 444.333979 USDC | 1.150042 USDC | 0.000000 USDC | 0.007480 USDC | 1.142562 USDC (1.0512 €) | — | 25.71 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53273243 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.198400 WETH | 0.000514 WETH | 0.000000 WETH | 0.000003 WETH | 0.000510 WETH (1.0498 €) | — | 25.72 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53273243 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 707.573747 USDC | 1.136346 USDC | 0.000000 USDC | 0.006801 USDC | 1.129545 USDC (1.0392 €) | — | 15.96 | 0.033 (n=153) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53273243 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.316143 WETH | 0.000508 WETH | 0.000000 WETH | 0.000003 WETH | 0.000505 WETH (1.0382 €) | — | 15.96 | 0.033 (n=153) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53273243 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 757.993558 USDC | 1.014114 USDC | 0.000000 USDC | 0.006801 USDC | 1.007313 USDC (0.9267 €) | — | 13.29 | 0.079 (n=27) | REJECTED | reliability_not_demonstrated |
| 53273243 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.338616 WETH | 0.000453 WETH | 0.000000 WETH | 0.000003 WETH | 0.000450 WETH (0.9257 €) | — | 13.29 | 0.079 (n=27) | REJECTED | reliability_not_demonstrated |
| 53273243 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 435.577972 USDC | 1.012435 USDC | 0.000000 USDC | 0.007820 USDC | 1.004615 USDC (0.9242 €) | — | 23.06 | 0.013 (n=60) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53273243 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.194682 WETH | 0.000452 WETH | 0.000000 WETH | 0.000003 WETH | 0.000449 WETH (0.9232 €) | — | 23.04 | 0.013 (n=60) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53273243 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 408.595260 USDC | 0.887296 USDC | 0.000000 USDC | 0.007480 USDC | 0.879816 USDC (0.8094 €) | — | 21.53 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53273243 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.182780 WETH | 0.000396 WETH | 0.000000 WETH | 0.000003 WETH | 0.000393 WETH (0.8087 €) | — | 21.50 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53273243 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 680.108867 USDC | 0.806378 USDC | 0.000000 USDC | 0.006462 USDC | 0.799916 USDC (0.7359 €) | — | 11.76 | 0.033 (n=153) | REJECTED | p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 3591 ; taux observé 0.112 ; borne inférieure crédible (0.9) 0.105 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
