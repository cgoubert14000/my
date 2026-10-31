# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T07:27:35+00:00 ; durée 52.21 min ; blocs 53319584 → 53321152 (1563 vus)

## Connexion
- Requêtes RPC : 18377 ; erreurs : 0 ; latence p50/p95 : 188.0/1,100.4 ms
- Rafraîchissements d'état : 1563 ; âge des données au dernier bloc : 3.3 s ; changements de frais LP observés (pools à frais dynamiques) : 1274
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11074 ; cycles déclenchés par événement : 1377 ; avance médiane sur le rafraîchissement multicall : 496 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,240.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 503 pools, 290 jetons, 18766 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 115, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3730 (énumérés 320, par paires 0), mesurés 506, sous le plancher de 10000.0 $ : 3 → gardés 503 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2240.565044, 'cbBTC': 77162.459811, 'AERO': 0.625673}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,951,514 | 2,240.566938 | 53321153 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,993,798 | 0.029010 | 53321153 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,257,036 | 0.000013 | 53321153 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,017,505 | 0.029063 | 53321153 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,179,662 | 2,242.987647 | 53321153 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,684,817 | 100.809064 | 53321153 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,678,381 | 0.001619 | 53321153 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,898,561 | 1.596027 | 53321153 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,479,096 | 0.029019 | 53321153 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,123,850 | 2,243.364001 | 53321153 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,062,239 | 2,243.418442 | 53321153 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,061,419 | 1.000001 | 53321153 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,541,137 | 37,467.883220 | 53321153 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,747,303 | 0.029045 | 53321153 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,332,277 | 100.812788 | 53321153 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,054,307 | 1,206,019.129455 | 53321153 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,973,064 | 0.000013 | 53321153 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,751,313 | 0.000000 | 53321153 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,717,084 | 0.017362 | 53321153 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,677,599 | 423.740143 | 53321153 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,639,416 | 0.000013 | 53321153 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,590,828 | 2,241.609652 | 53321153 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,579,196 | 0.000013 | 53321153 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,540,980 | 1.502063 | 53321153 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/USDC | 3000 | 1,523,041 | 2,248.609143 | 53321153 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,358 | 0.825821 | 53321153 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,425,544 | 0.000013 | 53321153 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,422,060 | 3,580.302150 | 53321153 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,333,731 | 0.005248 | 53321153 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,299,723 | 14,581.188317 | 53321153 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,281,218 | 2,242.928299 | 53321153 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,176,817 | 70.165644 | 53321153 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,724 | 35,677,478.940151 | 53321153 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,058,686 | 513,309.025665 | 53321153 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,034,714 | 21,099,479.852687 | 53321153 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,018,303 | 73,938.882946 | 53321153 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,971 | 19.280926 | 53321153 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 978,700 | 0.000000 | 53321153 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/VVV | 10000 | 965,681 | 100.544353 | 53321153 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 960,118 | 67.910628 | 53321153 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 950,404 | 0.044964 | 53321153 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 930,090 | 1,213,318.505662 | 53321153 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,025 | 2,235.963227 | 53321153 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 903,622 | 1,057.597517 | 53321153 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 864,252 | 3,585.793582 | 53321153 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,949 | 0.000554 | 53321153 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 845,699 | 19.165042 | 53321153 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 822,305 | 0.060853 | 53321153 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,759 | 0.802842 | 53321153 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 734,709 | 0.000265 | 53321153 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,631 | 0.592661 | 53321153 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 724,089 | 4,523,670.101312 | 53321153 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 683,474 | 0.000008 | 53321153 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 660,020 | 2.331780 | 53321153 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 659,928 | 145,364.841516 | 53321153 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 657,688 | 515,183.639941 | 53321153 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 626,810 | 0.496993 | 53321153 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 615,759 | 0.093828 | 53321153 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 602,124 | 0.916073 | 53321153 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 546,465 | 1,057.270996 | 53321153 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 2939 ; routes examinées : 55153274 ; candidats optimisés : 151587 ; net attendu > 0 : 16 ; dernier cycle 89.0 ms
- Rejets (moteur) : {'spread_below_threshold': 54204594, 'liquidity_below_min': 788276, 'negative_expected_net': 151571, 'unquotable': 5878, 'borrow_bound_too_small': 2939}
- Enregistrements de la session : 151587 ; net attendu > 0 : 16 ; simulés (eth_call de la vraie tx) : 2 (ok 2, échec 0) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 151587} ; motifs de rejet : {'below_safety_margin': 14, 'negative_expected_net': 151571, 'p_lower_below_threshold': 14, 'reliability_not_demonstrated': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53320499 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 9.115824 USDC | 0.008518 USDC | 0.000000 USDC | 0.004731 USDC | 0.003787 USDC (0.0035 €) | 0.003787 USDC | 4.15 | 0.031 (n=26) | REJECTED | reliability_not_demonstrated |
| 53320499 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 9.115824 USDC | 0.008518 USDC | 0.000000 USDC | 0.004731 USDC | 0.003787 USDC (0.0035 €) | 0.003787 USDC | 4.15 | 0.031 (n=26) | REJECTED | reliability_not_demonstrated |
| 53320642 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.421282 USDC | 0.008777 USDC | 0.000000 USDC | 0.005049 USDC | 0.003728 USDC (0.0034 €) | — | 1.92 | 0.039 (n=152) | REJECTED | below_safety_margin(3728<3884), p_lower_below_threshold(0.04<0.75) |
| 53320642 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.421282 USDC | 0.008777 USDC | 0.000000 USDC | 0.005049 USDC | 0.003728 USDC (0.0034 €) | — | 1.92 | 0.039 (n=152) | REJECTED | below_safety_margin(3728<3884), p_lower_below_threshold(0.04<0.75) |
| 53319947 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 62.336887 USDC | 0.009576 USDC | 0.000000 USDC | 0.006747 USDC | 0.002829 USDC (0.0026 €) | — | 0.45 | 0.144 (n=648) | REJECTED | below_safety_margin(2829<12467), p_lower_below_threshold(0.14<0.75) |
| 53319947 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.027989 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0026 €) | — | 0.45 | 0.144 (n=648) | REJECTED | below_safety_margin(1254117653310<5597783980834), p_lower_below_threshold(0.14<0.75) |
| 53319947 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 54.340932 USDC | 0.007789 USDC | 0.000000 USDC | 0.006747 USDC | 0.001042 USDC (0.0010 €) | — | 0.19 | 0.144 (n=648) | REJECTED | below_safety_margin(1042<10868), p_lower_below_threshold(0.14<0.75) |
| 53319947 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.024129 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.19 | 0.144 (n=648) | REJECTED | below_safety_margin(457863338590<4825825637155), p_lower_below_threshold(0.14<0.75) |
| 53320534 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 276.339348 USDC | 0.006281 USDC | 0.000000 USDC | 0.005383 USDC | 0.000898 USDC (0.0008 €) | — | 0.03 | 0.039 (n=152) | REJECTED | below_safety_margin(898<55267), p_lower_below_threshold(0.04<0.75) |
| 53320535 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 276.339348 USDC | 0.006281 USDC | 0.000000 USDC | 0.005383 USDC | 0.000898 USDC (0.0008 €) | — | 0.03 | 0.039 (n=152) | REJECTED | below_safety_margin(898<55267), p_lower_below_threshold(0.04<0.75) |
| 53320534 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.123318 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0008 €) | — | 0.03 | 0.039 (n=152) | REJECTED | below_safety_margin(397195907984<24663691844641), p_lower_below_threshold(0.04<0.75) |
| 53320535 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.123318 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0008 €) | — | 0.03 | 0.039 (n=152) | REJECTED | below_safety_margin(397195907984<24663691844641), p_lower_below_threshold(0.04<0.75) |
| 53320389 | WETH→[pancakeswap_v3]→AAVE→[aerodrome_slipstream]→WETH | 0.013105 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0008 €) | — | 0.28 | 0.039 (n=152) | REJECTED | below_safety_margin(370718746071<2621054809821), p_lower_below_threshold(0.04<0.75) |
| 53320389 | WETH→[pancakeswap_v3]→AAVE→[aerodrome_slipstream]→WETH | 0.013105 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0008 €) | — | 0.28 | 0.039 (n=152) | REJECTED | below_safety_margin(370718746071<2621054809821), p_lower_below_threshold(0.04<0.75) |
| 53320540 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 14.632642 USDC | 0.005118 USDC | 0.000000 USDC | 0.005042 USDC | 0.000076 USDC (0.0001 €) | — | 0.05 | 0.039 (n=152) | REJECTED | below_safety_margin(76<2926), p_lower_below_threshold(0.04<0.75) |
| 53320540 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 14.632642 USDC | 0.005118 USDC | 0.000000 USDC | 0.005042 USDC | 0.000076 USDC (0.0001 €) | — | 0.05 | 0.039 (n=152) | REJECTED | below_safety_margin(76<2926), p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 3908 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
