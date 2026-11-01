# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T05:03:34+00:00 ; durée 3.04 min ; blocs 53359939 → 53360033 (92 vus)

## Connexion
- Requêtes RPC : 1074 ; erreurs : 0 ; latence p50/p95 : 77.6/1,565.7 ms
- Rafraîchissements d'état : 93 ; âge des données au dernier bloc : 1.15 s ; changements de frais LP observés (pools à frais dynamiques) : 79
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 803 ; cycles déclenchés par événement : 101 ; avance médiane sur le rafraîchissement multicall : 453 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,265.72 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 502 pools, 289 jetons, 18760 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 114, aerodrome 206, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3742 (énumérés 318, par paires 0), mesurés 505, sous le plancher de 10000.0 $ : 3 → gardés 502 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2265.714788, 'cbBTC': 77709.69565, 'AERO': 0.641921}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,864,154 | 2,265.715333 | 53360033 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,144,199 | 0.029147 | 53360033 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,361,055 | 0.000013 | 53360033 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,101,558 | 0.029145 | 53360033 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,948,365 | 96.162233 | 53360033 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,894,973 | 2,265.613449 | 53360033 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,691,710 | 0.001604 | 53360033 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,749,828 | 1.557824 | 53360033 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,169,876 | 0.029150 | 53360033 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,092,855 | 0.998851 | 53360033 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,070,788 | 2,266.324544 | 53360033 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,986,447 | 2,266.400772 | 53360033 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,561,845 | 37,869.351164 | 53360033 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,701,944 | 0.029157 | 53360033 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,433,974 | 96.164136 | 53360033 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,186,878 | 0.000013 | 53360033 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,083,157 | 1,199,321.852139 | 53360033 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,764,244 | 0.000000 | 53360033 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,712,680 | 0.017333 | 53360033 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,678,100 | 0.000013 | 53360033 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,585,835 | 0.000013 | 53360033 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,560,726 | 421.614755 | 53360033 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,546,920 | 1.490152 | 53360033 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,507,911 | 2,268.614553 | 53360033 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,455 | 0.825724 | 53360033 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,435,417 | 3,529.153520 | 53360033 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,412,136 | 2,271.307011 | 53360033 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,351,680 | 2,265.539471 | 53360033 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,324,583 | 0.005159 | 53360033 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,313,632 | 14,456.623602 | 53360033 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,307,985 | 0.000013 | 53360033 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,174,072 | 70.494059 | 53360033 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,145,434 | 33,833,204.438690 | 53360033 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,075,659 | 513,791.540660 | 53360033 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,054,842 | 0.000000 | 53360033 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,032,962 | 21,602,651.733132 | 53360033 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,005,362 | 95.977481 | 53360033 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 1,003,900 | 77,755.236839 | 53360033 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 994,229 | 0.042460 | 53360033 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,025 | 19.334449 | 53360033 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 968,500 | 66.741014 | 53360033 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 962,635 | 1,158,223.277826 | 53360033 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 948,943 | 971.365471 | 53360033 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 925,635 | 2,249.741211 | 53360033 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 879,012 | 3,504.632835 | 53360033 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 866,548 | 0.000548 | 53360033 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 838,815 | 19.410903 | 53360033 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 821,309 | 0.060683 | 53360033 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 767,169 | 0.803065 | 53360033 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 737,675 | 0.000261 | 53360033 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 725,846 | 0.593383 | 53360033 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 714,911 | 4,745,814.016180 | 53360033 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 694,458 | 0.000008 | 53360033 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 676,304 | 141,552.406150 | 53360033 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 664,654 | 513,645.621691 | 53360033 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 660,372 | 2.338238 | 53360033 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 659,572 | 0.547546 | 53360033 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 612,179 | 0.092966 | 53360033 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 608,114 | 0.916175 | 53360033 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2793 | 557,523 | 971.210062 | 53360033 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 193 ; routes examinées : 3620680 ; candidats optimisés : 13465 ; net attendu > 0 : 12 ; dernier cycle 244.6 ms
- Rejets (moteur) : {'spread_below_threshold': 3543877, 'liquidity_below_min': 62759, 'negative_expected_net': 13453, 'unquotable': 386, 'borrow_bound_too_small': 193}
- Enregistrements de la session : 13465 ; net attendu > 0 : 12 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 13465} ; motifs de rejet : {'below_safety_margin': 12, 'negative_expected_net': 13453, 'p_lower_below_threshold': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53360014 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004348 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.45 | 0.189 (n=283) | REJECTED | below_safety_margin(629547186721<869576446142), p_lower_below_threshold(0.19<0.75) |
| 53360014 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004348 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.45 | 0.189 (n=283) | REJECTED | below_safety_margin(629547186721<869576446142), p_lower_below_threshold(0.19<0.75) |
| 53360014 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.906459 USDC | 0.008234 USDC | 0.000000 USDC | 0.006808 USDC | 0.001426 USDC (0.0013 €) | — | 1.44 | 0.189 (n=283) | REJECTED | below_safety_margin(1426<1981), p_lower_below_threshold(0.19<0.75) |
| 53360014 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.906459 USDC | 0.008234 USDC | 0.000000 USDC | 0.006808 USDC | 0.001426 USDC (0.0013 €) | — | 1.44 | 0.189 (n=283) | REJECTED | below_safety_margin(1426<1981), p_lower_below_threshold(0.19<0.75) |
| 53360014 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004225 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.57 | 0.189 (n=283) | REJECTED | below_safety_margin(240924153871<844939461096), p_lower_below_threshold(0.19<0.75) |
| 53360014 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004225 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.57 | 0.189 (n=283) | REJECTED | below_safety_margin(240924153871<844939461096), p_lower_below_threshold(0.19<0.75) |
| 53360014 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.466859 USDC | 0.007353 USDC | 0.000000 USDC | 0.006808 USDC | 0.000545 USDC (0.0005 €) | — | 0.58 | 0.189 (n=283) | REJECTED | below_safety_margin(545<1893), p_lower_below_threshold(0.19<0.75) |
| 53360014 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.466859 USDC | 0.007353 USDC | 0.000000 USDC | 0.006808 USDC | 0.000545 USDC (0.0005 €) | — | 0.58 | 0.189 (n=283) | REJECTED | below_safety_margin(545<1893), p_lower_below_threshold(0.19<0.75) |
| 53360014 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004098 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.05 | 0.140 (n=666) | REJECTED | below_safety_margin(20303525674<819645605003), p_lower_below_threshold(0.14<0.75) |
| 53360014 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004098 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.05 | 0.140 (n=666) | REJECTED | below_safety_margin(20303525674<819645605003), p_lower_below_threshold(0.14<0.75) |
| 53360014 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.139759 USDC | 0.006854 USDC | 0.000000 USDC | 0.006808 USDC | 0.000046 USDC (0.0000 €) | — | 0.05 | 0.140 (n=666) | REJECTED | below_safety_margin(46<1827), p_lower_below_threshold(0.14<0.75) |
| 53360014 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.139759 USDC | 0.006854 USDC | 0.000000 USDC | 0.006808 USDC | 0.000046 USDC (0.0000 €) | — | 0.05 | 0.140 (n=666) | REJECTED | below_safety_margin(46<1827), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 4038 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
