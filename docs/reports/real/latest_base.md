# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T19:07:46+00:00 ; durée 27.49 min ; blocs 54432179 → 54440411 (2317 vus)

## Connexion
- Requêtes RPC : 22961 ; erreurs : 0 ; latence p50/p95 : 103.4/1,641.5 ms
- Rafraîchissements d'état : 2317 ; âge des données au dernier bloc : 9.0 s ; changements de frais LP observés (pools à frais dynamiques) : 564
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2763 ; cycles déclenchés par événement : 781 ; avance médiane sur le rafraîchissement multicall : 194 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,234.63 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 277 jetons, 17824 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 96, aerodrome 198, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 169 (rejetés 2) → 574 jetons ; pools candidats 3672 (énumérés 292, par paires 0), mesurés 476, sous le plancher de 10000.0 $ : 3 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2234.638115, 'cbBTC': 75748.316454, 'AERO': 0.612979}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,734,911 | 2,234.629462 | 54440434 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,807,706 | 0.029493 | 54440434 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,341,206 | 0.000013 | 54440434 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,160,420 | 0.029513 | 54440434 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,057,793 | 2,232.664642 | 54440434 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,334,798 | 108.448201 | 54440434 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,411,870 | 0.001550 | 54440434 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,165,002 | 0.029481 | 54440434 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,892,176 | 1.637228 | 54440434 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,169,748 | 2,232.070814 | 54440434 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,988,310 | 0.998992 | 54440434 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,330,718 | 42,126.029875 | 54440434 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 594 | 3,187,408 | 2,232.975221 | 54440434 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,546,673 | 0.029525 | 54440434 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,100,349 | 1,147,424.274597 | 54440434 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,736,807 | 0.000013 | 54440434 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,706,274 | 0.006798 | 54440434 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,645,006 | 0.000013 | 54440434 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,631,049 | 0.000000 | 54440434 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,598,932 | 0.015974 | 54440434 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,524,827 | 437.525152 | 54440434 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,504,333 | 0.000013 | 54440434 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,494,357 | 1.466903 | 54440434 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,111 | 0.819634 | 54440434 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,393,796 | 3,654.273167 | 54440434 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,324,789 | 2,234.918105 | 54440434 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,322,643 | 2,238.811178 | 54440434 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,269,003 | 14,848.856752 | 54440434 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,200,306 | 2,232.899050 | 54440434 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,471 | 76.986684 | 54440434 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,106,166 | 36,110,001.238542 | 54440434 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,044,785 | 109.234868 | 54440434 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,016,447 | 570,245.029699 | 54440434 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 995,400 | 22,537,303.536336 | 54440434 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 983,232 | 19.904042 | 54440434 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 969,499 | 0.000000 | 54440434 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/MORPHO | 3000 | 941,376 | 1,055.564869 | 54440434 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,369 | 2,228.787514 | 54440434 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 925,504 | 0.000013 | 54440434 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 918,723 | 74.240206 | 54440434 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 875,059 | 99,479.785313 | 54440434 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 818,371 | 0.048523 | 54440434 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 793,996 | 3,663.435290 | 54440434 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 793,459 | 21.140028 | 54440434 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,337 | 0.055302 | 54440434 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,089 | 0.799699 | 54440434 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 718,350 | 0.565149 | 54440434 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,795 | 4,895,624.471225 | 54440434 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 683,149 | 0.000253 | 54440434 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 674,688 | 0.574487 | 54440434 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 659,453 | 0.000008 | 54440434 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 648,662 | 150,054.851366 | 54440434 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 621,540 | 569,652.832857 | 54440434 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 587,320 | 2.472336 | 54440434 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 586,047 | 0.040678 | 54440434 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 527,490 | 1,055.355672 | 54440434 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 519,366 | 899,970.460963 | 54440434 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 515,636 | 2,231.910930 | 54440434 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | ELSA/USDC | 100 | 513,030 | 0.076052 | 54440434 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 504,516 | 7,194.447926 | 54440434 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 3097 ; routes examinées : 55200928 ; candidats optimisés : 19622 ; net attendu > 0 : 59 ; dernier cycle 73.7 ms
- Rejets (moteur) : {'spread_below_threshold': 54432983, 'liquidity_below_min': 744796, 'negative_expected_net': 19563, 'borrow_bound_too_small': 3097, 'pool_quarantined': 216, 'cycle_budget_exhausted': 214}
- Enregistrements de la session : 19622 ; net attendu > 0 : 59 ; simulés (eth_call de la vraie tx) : 13 (ok 0, échec 13) ; étiquettes ghost N+1 : 1/9 positives
- Décisions : {'REJECTED': 19622} ; motifs de rejet : {'below_safety_margin': 35, 'negative_expected_net': 19563, 'p_lower_below_threshold': 59, 'simulation_failed': 13, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54435870 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.087948 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1784 €) | — | 9.86 | 0.074 (n=158) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 54435870 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002515 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1777 €) | — | 10.14 | 0.074 (n=158) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54435870 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001967 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1429 €) | — | 10.42 | 0.074 (n=158) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54435870 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.069372 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1425 €) | — | 9.99 | 0.074 (n=158) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 54435870 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.054134 WETH | 0.000067 WETH | 0.000000 WETH | 0.000003 WETH | 0.000064 WETH (0.1315 €) | — | 11.82 | 0.074 (n=158) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 54435870 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.001453 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1310 €) | — | 12.94 | 0.074 (n=158) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54435870 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.001377 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1185 €) | — | 12.35 | 0.074 (n=158) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54435870 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.047760 WETH | 0.000060 WETH | 0.000000 WETH | 0.000003 WETH | 0.000057 WETH (0.1181 €) | — | 12.03 | 0.074 (n=158) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54435870 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.066906 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1060 €) | — | 7.70 | 0.155 (n=825) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54435870 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001924 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1059 €) | — | 7.90 | 0.155 (n=825) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54435870 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.001212 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0871 €) | — | 10.31 | 0.074 (n=158) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54435870 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.045296 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0869 €) | — | 9.34 | 0.074 (n=158) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54435870 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.001146 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0753 €) | — | 9.43 | 0.074 (n=158) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54435870 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.039030 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0750 €) | — | 9.35 | 0.074 (n=158) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54434682 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.012724 WETH | 0.000032 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0612 €) | — | 23.40 | 0.000 (n=33) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54434684 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.012724 WETH | 0.000032 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0612 €) | — | 23.40 | 0.000 (n=33) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54434479 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.284702 WETH | 0.000031 WETH | 0.000000 WETH | 0.000002 WETH | 0.000028 WETH (0.0581 €) | — | 0.99 | 0.050 (n=266) | REJECTED | below_safety_margin(28236311157226<56940397032977), stale_data(4254ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54434479 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 634.607403 USDC | 0.068450 USDC | 0.000000 USDC | 0.005356 USDC | 0.063094 USDC (0.0580 €) | — | 0.99 | 0.050 (n=266) | REJECTED | below_safety_margin(63094<126921), stale_data(4260ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54434479 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 393.937658 USDC | 0.050344 USDC | 0.000000 USDC | 0.005356 USDC | 0.044988 USDC (0.0414 €) | — | 1.14 | 0.051 (n=85) | REJECTED | below_safety_margin(44988<78787), stale_data(4248ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54434479 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.176431 WETH | 0.000023 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0414 €) | — | 1.14 | 0.051 (n=85) | REJECTED | below_safety_margin(20131146646179<35286103490181), stale_data(4241ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54436226 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 52.292697 USDC | 0.028203 USDC | 0.000000 USDC | 0.006716 USDC | 0.021487 USDC (0.0198 €) | — | 4.11 | 0.155 (n=825) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 54440056 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 52.763043 USDC | 0.026891 USDC | 0.000000 USDC | 0.006715 USDC | 0.020176 USDC (0.0186 €) | — | 3.82 | 0.155 (n=826) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 54440056 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.000727 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0181 €) | — | 3.57 | 0.155 (n=826) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 54434479 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.004090 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0118 €) | — | 0.42 | 0.182 (n=1058) | REJECTED | below_safety_margin(17<81), stale_data(4297ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54434479 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 339.884453 USDC | 0.018952 USDC | 0.000000 USDC | 0.006715 USDC | 0.012237 USDC (0.0113 €) | — | 0.36 | 0.182 (n=1058) | REJECTED | below_safety_margin(12237<67976), stale_data(4314ms>4000.0), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 6080 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
