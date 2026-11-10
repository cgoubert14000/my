# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T02:56:35+00:00 ; durée 6.07 min ; blocs 55443239 → 55445054 (292 vus)

## Connexion
- Requêtes RPC : 3655 ; erreurs : 0 ; latence p50/p95 : 290.3/1,796.5 ms
- Rafraîchissements d'état : 292 ; âge des données au dernier bloc : 9.82 s ; changements de frais LP observés (pools à frais dynamiques) : 103
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 182 ; cycles déclenchés par événement : 82 ; avance médiane sur le rafraîchissement multicall : 325 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,121.50 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 465 pools, 270 jetons, 17662 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 99, aerodrome 191, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3655 (énumérés 287, par paires 0), mesurés 467, sous le plancher de 10000.0 $ : 2 → gardés 465 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2121.500856, 'cbBTC': 74826.515907, 'AERO': 0.554783}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,875,564 | 2,121.500875 | 55445080 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,626,413 | 0.028355 | 55445080 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,379,081 | 0.000013 | 55445080 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,771,661 | 0.028376 | 55445080 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,490,977 | 2,122.176281 | 55445080 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,278,261 | 99.204785 | 55445080 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,921,705 | 0.028347 | 55445080 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,478,046 | 1.802508 | 55445080 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,030,734 | 2,121.374118 | 55445080 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,895,336 | 1.000030 | 55445080 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,117,502 | 43,339.924540 | 55445080 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,019,069 | 2,121.362049 | 55445080 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,341,689 | 0.028341 | 55445080 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,023,046 | 1,114,733.552638 | 55445080 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,706,611 | 0.000013 | 55445080 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,683,409 | 0.000013 | 55445080 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,568,596 | 0.015611 | 55445080 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,559,746 | 0.006561 | 55445080 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,557,714 | 0.000000 | 55445080 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,493,208 | 0.000013 | 55445080 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,082 | 1.429325 | 55445080 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,460,359 | 425.606306 | 55445080 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,267 | 0.821811 | 55445080 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,293,996 | 3,820.960879 | 55445080 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,291,312 | 2,121.786435 | 55445080 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,247,512 | 15,032.473215 | 55445080 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,219,617 | 2,123.584494 | 55445080 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,061 | 79.285849 | 55445080 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,105,702 | 2,122.214153 | 55445080 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,052,420 | 35,885,434.420801 | 55445080 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 982,873 | 98.537433 | 55445080 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 966,333 | 568,568.899594 | 55445080 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 955,890 | 0.046797 | 55445080 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 954,938 | 21.740057 | 55445080 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 935,772 | 0.001507 | 55445080 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 933,391 | 23,039,733.174810 | 55445080 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 928,604 | 0.000013 | 55445080 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 917,487 | 74.440379 | 55445080 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 903,195 | 1,040.796394 | 55445080 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 896,476 | 0.000000 | 55445080 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 887,961 | 2,127.924155 | 55445080 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 808,760 | 104,903.418127 | 55445080 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 770,183 | 22.064408 | 55445080 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 760,666 | 0.051601 | 55445080 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 733,705 | 3,794.578430 | 55445080 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 720,235 | 0.798536 | 55445080 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 669,805 | 0.542752 | 55445080 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 659,498 | 4,898,778.652334 | 55445080 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 649,186 | 0.529168 | 55445080 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 615,216 | 150,463.257760 | 55445080 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 607,777 | 0.000007 | 55445080 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 598,550 | 0.000258 | 55445080 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 591,114 | 572,309.818385 | 55445080 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,209 | 0.038497 | 55445080 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 510,871 | 1,040.505501 | 55445080 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/USDT | 100 | 497,025 | 1.001027 | 55445080 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 495,873 | 6,712.469932 | 55445080 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| aerodrome | WETH/msETH (stable) | 500 | 494,896 | 2.404977 | 55445080 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/uSOL | 3000 | 468,097 | 24.728645 | 55445080 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| pancakeswap_v3 | ELSA/USDC | 100 | 465,969 | 0.066912 | 55445080 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 373 ; routes examinées : 6587926 ; candidats optimisés : 15682 ; net attendu > 0 : 16 ; dernier cycle 293.6 ms
- Rejets (moteur) : {'spread_below_threshold': 6452662, 'liquidity_below_min': 118775, 'negative_expected_net': 15666, 'borrow_bound_too_small': 746, 'cycle_budget_exhausted': 61}
- Enregistrements de la session : 15682 ; net attendu > 0 : 16 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 15682} ; motifs de rejet : {'below_safety_margin': 16, 'negative_expected_net': 15666, 'p_lower_below_threshold': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55444678 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 399.069046 USDC | 0.038627 USDC | 0.000000 USDC | 0.004765 USDC | 0.033862 USDC (0.0312 €) | — | 0.85 | 0.069 (n=319) | REJECTED | below_safety_margin(33862<79813), p_lower_below_threshold(0.07<0.75) |
| 55444679 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 399.069046 USDC | 0.038627 USDC | 0.000000 USDC | 0.004765 USDC | 0.033862 USDC (0.0312 €) | — | 0.85 | 0.069 (n=319) | REJECTED | below_safety_margin(33862<79813), p_lower_below_threshold(0.07<0.75) |
| 55444678 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.188631 WETH | 0.000018 WETH | 0.000000 WETH | 0.000002 WETH | 0.000016 WETH (0.0311 €) | — | 0.85 | 0.069 (n=319) | REJECTED | below_safety_margin(15952296321365<37726101222205), p_lower_below_threshold(0.07<0.75) |
| 55444679 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.188631 WETH | 0.000018 WETH | 0.000000 WETH | 0.000002 WETH | 0.000016 WETH (0.0311 €) | — | 0.85 | 0.069 (n=319) | REJECTED | below_safety_margin(15952296321365<37726101222205), p_lower_below_threshold(0.07<0.75) |
| 55444678 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 280.388628 USDC | 0.029064 USDC | 0.000000 USDC | 0.004765 USDC | 0.024299 USDC (0.0224 €) | — | 0.87 | 0.069 (n=319) | REJECTED | below_safety_margin(24299<56077), p_lower_below_threshold(0.07<0.75) |
| 55444679 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 280.388628 USDC | 0.029064 USDC | 0.000000 USDC | 0.004765 USDC | 0.024299 USDC (0.0224 €) | — | 0.87 | 0.069 (n=319) | REJECTED | below_safety_margin(24299<56077), p_lower_below_threshold(0.07<0.75) |
| 55444678 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.132698 WETH | 0.000014 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0223 €) | — | 0.86 | 0.069 (n=319) | REJECTED | below_safety_margin(11447151199638<26539590820553), p_lower_below_threshold(0.07<0.75) |
| 55444679 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.132698 WETH | 0.000014 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0223 €) | — | 0.86 | 0.069 (n=319) | REJECTED | below_safety_margin(11447151199638<26539590820553), p_lower_below_threshold(0.07<0.75) |
| 55444077 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 210.145047 USDC | 0.016167 USDC | 0.000000 USDC | 0.004766 USDC | 0.011401 USDC (0.0105 €) | — | 0.54 | 0.069 (n=319) | REJECTED | below_safety_margin(11401<42029), p_lower_below_threshold(0.07<0.75) |
| 55444078 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 210.145047 USDC | 0.016167 USDC | 0.000000 USDC | 0.004766 USDC | 0.011401 USDC (0.0105 €) | — | 0.54 | 0.069 (n=319) | REJECTED | below_safety_margin(11401<42029), p_lower_below_threshold(0.07<0.75) |
| 55444077 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.098688 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0105 €) | — | 0.54 | 0.069 (n=319) | REJECTED | below_safety_margin(5369444057765<19737553291253), p_lower_below_threshold(0.07<0.75) |
| 55444078 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.098688 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0105 €) | — | 0.54 | 0.069 (n=319) | REJECTED | below_safety_margin(5369444057765<19737553291253), p_lower_below_threshold(0.07<0.75) |
| 55444077 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 161.149451 USDC | 0.006417 USDC | 0.000000 USDC | 0.004766 USDC | 0.001651 USDC (0.0015 €) | — | 0.10 | 0.069 (n=319) | REJECTED | below_safety_margin(1651<32229), p_lower_below_threshold(0.07<0.75) |
| 55444078 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 161.149451 USDC | 0.006417 USDC | 0.000000 USDC | 0.004766 USDC | 0.001651 USDC (0.0015 €) | — | 0.10 | 0.069 (n=319) | REJECTED | below_safety_margin(1651<32229), p_lower_below_threshold(0.07<0.75) |
| 55444077 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.077070 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0015 €) | — | 0.10 | 0.069 (n=319) | REJECTED | below_safety_margin(776869936296<15414037774446), p_lower_below_threshold(0.07<0.75) |
| 55444078 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.077070 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0015 €) | — | 0.10 | 0.069 (n=319) | REJECTED | below_safety_margin(776869936296<15414037774446), p_lower_below_threshold(0.07<0.75) |

## Fiabilité et décision
- Observations ghost : 7203 ; taux observé 0.187 ; borne inférieure crédible (0.9) 0.181 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
