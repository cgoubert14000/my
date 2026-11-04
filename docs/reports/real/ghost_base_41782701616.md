# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T07:45:21+00:00 ; durée 98.26 min ; blocs 53491535 → 53494484 (2934 vus)

## Connexion
- Requêtes RPC : 33182 ; erreurs : 0 ; latence p50/p95 : 237.9/1,279.0 ms
- Rafraîchissements d'état : 2934 ; âge des données au dernier bloc : 5.3 s ; changements de frais LP observés (pools à frais dynamiques) : 4639
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1342 ; cycles déclenchés par événement : 180 ; avance médiane sur le rafraîchissement multicall : 611 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,297.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 284 jetons, 19492 routes
- Par DEX : uniswap_v3 141, aerodrome_slipstream 106, aerodrome 204, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3704 (énumérés 307, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2296.568203, 'cbBTC': 77781.37292, 'AERO': 0.62987}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,525,401 | 2,297.894374 | 53494485 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,841,269 | 0.029463 | 53494485 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,264,659 | 0.029470 | 53494485 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,154,831 | 0.000013 | 53494485 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,078,392 | 2,300.577104 | 53494485 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,060,491 | 95.141806 | 53494485 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,620,893 | 0.001560 | 53494485 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,374,361 | 1.579571 | 53494485 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,829,860 | 0.029475 | 53494485 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,187,749 | 2,301.403146 | 53494485 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,103,183 | 0.999894 | 53494485 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,883,533 | 2,301.374931 | 53494485 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,454,653 | 41,406.355850 | 53494485 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,697,310 | 0.029478 | 53494485 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2742 | 2,206,020 | 95.171921 | 53494485 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,163,610 | 1,143,593.095050 | 53494485 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,820,462 | 0.000013 | 53494485 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,729,508 | 0.017667 | 53494485 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,685,374 | 0.000000 | 53494485 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,681,564 | 0.006732 | 53494485 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,625,082 | 0.000013 | 53494485 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,572,353 | 432.100045 | 53494485 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,552,822 | 1.432992 | 53494485 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,552,261 | 0.000013 | 53494485 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,444 | 0.817942 | 53494485 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,433,682 | 3,632.610744 | 53494485 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,362,044 | 2,300.589302 | 53494485 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,343,482 | 2,299.945003 | 53494485 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,342,870 | 2,295.625641 | 53494485 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,311,108 | 14,689.887759 | 53494485 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,309 | 72.425481 | 53494485 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,128,183 | 37,096,595.697474 | 53494485 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,057,961 | 552,259.857272 | 53494485 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,039,533 | 0.000000 | 53494485 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,032,773 | 22,200,681.403136 | 53494485 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,005,089 | 18.679113 | 53494485 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 1,004,695 | 95.691150 | 53494485 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 970,097 | 1,034.326223 | 53494485 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 958,295 | 87,716.582842 | 53494485 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 945,901 | 0.000013 | 53494485 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/WELL | 10000 | 931,979 | 1,268,138.692297 | 53494485 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 930,430 | 2,281.231869 | 53494485 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 929,744 | 0.041371 | 53494485 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 926,411 | 72.944475 | 53494485 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 879,388 | 0.000550 | 53494485 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 848,092 | 3,625.917024 | 53494485 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 825,784 | 19.901719 | 53494485 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 792,937 | 0.056307 | 53494485 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 779,967 | 0.799140 | 53494485 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,792 | 0.593197 | 53494485 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 730,178 | 0.000257 | 53494485 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 713,187 | 4,909,647.483770 | 53494485 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 675,788 | 0.000008 | 53494485 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 675,574 | 146,103.673767 | 53494485 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 652,870 | 0.536249 | 53494485 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 649,196 | 547,717.838200 | 53494485 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 644,700 | 2.453307 | 53494485 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 617,466 | 0.914056 | 53494485 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 608,102 | 0.091891 | 53494485 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 584,058 | 0.040645 | 53494485 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 3113 ; routes examinées : 60678596 ; candidats optimisés : 189355 ; net attendu > 0 : 10 ; dernier cycle 354.8 ms
- Rejets (moteur) : {'spread_below_threshold': 59629973, 'liquidity_below_min': 855984, 'negative_expected_net': 189345, 'borrow_bound_too_small': 3110, 'cycle_budget_exhausted': 174}
- Enregistrements de la session : 189355 ; net attendu > 0 : 10 ; simulés (eth_call de la vraie tx) : 2 (ok 2, échec 0) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 189355} ; motifs de rejet : {'below_safety_margin': 8, 'negative_expected_net': 189345, 'p_lower_below_threshold': 9, 'reliability_not_demonstrated': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53494276 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 33.907595 USDC | 0.013550 USDC | 0.000000 USDC | 0.006904 USDC | 0.006646 USDC (0.0061 €) | — | 1.96 | 0.183 (n=877) | REJECTED | below_safety_margin(6646<6781), p_lower_below_threshold(0.18<0.75) |
| 53494276 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.014874 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0061 €) | — | 1.94 | 0.183 (n=877) | REJECTED | below_safety_margin(2887177192559<2974705983682), p_lower_below_threshold(0.18<0.75) |
| 53494083 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.002833 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0022 €) | 0.000001 WETH | 3.64 | 0.068 (n=75) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53493884 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 7.751162 USDC | 0.006402 USDC | 0.000000 USDC | 0.004835 USDC | 0.001567 USDC (0.0014 €) | 0.001567 USDC | 2.02 | 0.083 (n=26) | REJECTED | reliability_not_demonstrated |
| 53494276 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 34.411901 USDC | 0.008455 USDC | 0.000000 USDC | 0.006904 USDC | 0.001551 USDC (0.0014 €) | — | 0.45 | 0.183 (n=877) | REJECTED | below_safety_margin(1551<6882), p_lower_below_threshold(0.18<0.75) |
| 53494276 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.014988 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.45 | 0.183 (n=877) | REJECTED | below_safety_margin(671722791653<2997602352129), p_lower_below_threshold(0.18<0.75) |
| 53492556 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.020021 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0003 €) | — | 0.08 | 0.045 (n=204) | REJECTED | below_safety_margin(159445314040<4004255597769), p_lower_below_threshold(0.04<0.75) |
| 53492556 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 45.295213 USDC | 0.005510 USDC | 0.000000 USDC | 0.005147 USDC | 0.000363 USDC (0.0003 €) | — | 0.08 | 0.045 (n=204) | REJECTED | below_safety_margin(363<9059), p_lower_below_threshold(0.04<0.75) |
| 53493609 | USDC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 1.372889 USDC | 0.001162 USDC | 0.000000 USDC | 0.001154 USDC | 0.000008 USDC (0.0000 €) | — | 0.06 | 0.183 (n=877) | REJECTED | below_safety_margin(8<274), p_lower_below_threshold(0.18<0.75) |
| 53493609 | USDC→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1.372889 USDC | 0.001162 USDC | 0.000000 USDC | 0.001154 USDC | 0.000008 USDC (0.0000 €) | — | 0.06 | 0.183 (n=877) | REJECTED | below_safety_margin(8<274), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 5045 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
