# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T06:47:31+00:00 ; durée 12.14 min ; blocs 53319584 → 53319951 (363 vus)

## Connexion
- Requêtes RPC : 4194 ; erreurs : 0 ; latence p50/p95 : 203.4/1,384.2 ms
- Rafraîchissements d'état : 364 ; âge des données au dernier bloc : 2.12 s ; changements de frais LP observés (pools à frais dynamiques) : 258
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2824 ; cycles déclenchés par événement : 319 ; avance médiane sur le rafraîchissement multicall : 598 ms
- Gaz : base fee 0.005035 gwei ; prix ETH (pool le plus profond) : 2,240.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 503 pools, 290 jetons, 18766 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 115, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3730 (énumérés 320, par paires 0), mesurés 506, sous le plancher de 10000.0 $ : 3 → gardés 503 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2240.565044, 'cbBTC': 77162.459811, 'AERO': 0.625673}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,182,257 | 2,240.565081 | 53319951 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,989,042 | 0.029034 | 53319951 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,256,732 | 0.000013 | 53319951 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,012,572 | 0.029063 | 53319951 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,187,442 | 2,244.994071 | 53319951 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,672,316 | 101.137662 | 53319951 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,679,944 | 0.001622 | 53319951 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,918,700 | 1.589155 | 53319951 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,478,139 | 0.029024 | 53319951 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,126,207 | 2,245.734267 | 53319951 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,094,714 | 2,245.880491 | 53319951 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,058,069 | 1.000001 | 53319951 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,541,162 | 37,467.288905 | 53319951 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,746,749 | 0.029045 | 53319951 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,327,953 | 101.100534 | 53319951 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,054,306 | 1,206,019.129455 | 53319951 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,972,229 | 0.000013 | 53319951 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,751,314 | 0.000000 | 53319951 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,719,160 | 0.017403 | 53319951 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,680,024 | 421.958765 | 53319951 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,638,447 | 0.000013 | 53319951 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,590,827 | 2,241.185260 | 53319951 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,578,842 | 0.000013 | 53319951 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,540,980 | 1.502063 | 53319951 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/USDC | 3000 | 1,523,040 | 2,248.368867 | 53319951 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,570 | 0.825600 | 53319951 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,425,576 | 3,567.475903 | 53319951 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/cbBTC | 374 | 1,424,658 | 0.000013 | 53319951 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,333,730 | 0.005248 | 53319951 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,301,361 | 14,526.366420 | 53319951 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,280,761 | 2,244.952897 | 53319951 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,176,817 | 70.165644 | 53319951 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,723 | 35,677,478.940151 | 53319951 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,058,688 | 513,305.367906 | 53319951 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,035,536 | 21,070,263.564884 | 53319951 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,017,631 | 74,036.454398 | 53319951 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | DRB/WETH | 10000 | 994,210 | 0.000000 | 53319951 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,524 | 19.305994 | 53319951 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 977,627 | 65.499830 | 53319951 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 963,728 | 100.544276 | 53319951 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 948,063 | 0.045079 | 53319951 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 930,089 | 1,213,318.505662 | 53319951 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,024 | 2,235.963227 | 53319951 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 901,198 | 1,062.711208 | 53319951 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 866,123 | 3,585.793582 | 53319951 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,948 | 0.000554 | 53319951 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 845,228 | 19.181403 | 53319951 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 823,892 | 0.061076 | 53319951 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,758 | 0.802842 | 53319951 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 736,655 | 0.000265 | 53319951 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 725,205 | 4,509,721.302536 | 53319951 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,635 | 0.592661 | 53319951 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 684,886 | 0.000008 | 53319951 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 660,020 | 2.331780 | 53319951 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 659,928 | 145,364.841516 | 53319951 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 657,688 | 513,902.433218 | 53319951 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 626,811 | 0.496993 | 53319951 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 616,002 | 0.093886 | 53319951 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 602,604 | 0.914613 | 53319951 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2730 | 545,201 | 1,062.135123 | 53319951 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 682 ; routes examinées : 12798412 ; candidats optimisés : 40676 ; net attendu > 0 : 4 ; dernier cycle 252.4 ms
- Rejets (moteur) : {'spread_below_threshold': 12555146, 'liquidity_below_min': 200544, 'negative_expected_net': 40672, 'unquotable': 1364, 'borrow_bound_too_small': 682}
- Enregistrements de la session : 40676 ; net attendu > 0 : 4 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 40676} ; motifs de rejet : {'below_safety_margin': 4, 'negative_expected_net': 40672, 'p_lower_below_threshold': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53319947 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 62.336887 USDC | 0.009576 USDC | 0.000000 USDC | 0.006747 USDC | 0.002829 USDC (0.0026 €) | — | 0.45 | 0.144 (n=648) | REJECTED | below_safety_margin(2829<12467), p_lower_below_threshold(0.14<0.75) |
| 53319947 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.027989 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0026 €) | — | 0.45 | 0.144 (n=648) | REJECTED | below_safety_margin(1254117653310<5597783980834), p_lower_below_threshold(0.14<0.75) |
| 53319947 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 54.340932 USDC | 0.007789 USDC | 0.000000 USDC | 0.006747 USDC | 0.001042 USDC (0.0010 €) | — | 0.19 | 0.144 (n=648) | REJECTED | below_safety_margin(1042<10868), p_lower_below_threshold(0.14<0.75) |
| 53319947 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.024129 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.19 | 0.144 (n=648) | REJECTED | below_safety_margin(457863338590<4825825637155), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3907 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
