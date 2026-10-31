# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T01:01:02+00:00 ; durée 3.02 min ; blocs 53309463 → 53309556 (81 vus)

## Connexion
- Requêtes RPC : 1075 ; erreurs : 0 ; latence p50/p95 : 354.1/1,732.5 ms
- Rafraîchissements d'état : 81 ; âge des données au dernier bloc : 8.92 s ; changements de frais LP observés (pools à frais dynamiques) : 50
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 838 ; cycles déclenchés par événement : 81 ; avance médiane sur le rafraîchissement multicall : 1,221 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,241.47 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 506 pools, 291 jetons, 18872 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 117, aerodrome 207, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 179 (rejetés 2) → 584 jetons ; pools candidats 3782 (énumérés 322, par paires 0), mesurés 509, sous le plancher de 10000.0 $ : 3 → gardés 506 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2241.465194, 'cbBTC': 77391.917525, 'AERO': 0.626719}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,378,083 | 2,241.465206 | 53309555 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,977,500 | 0.029018 | 53309555 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,247,412 | 0.000013 | 53309555 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,020,517 | 0.029091 | 53309555 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,191,396 | 2,246.343680 | 53309555 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,759,178 | 98.974245 | 53309555 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,702,027 | 0.001630 | 53309555 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,907,489 | 1.595612 | 53309555 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,573,264 | 0.029006 | 53309555 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,141,682 | 2,246.707571 | 53309555 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,062,723 | 1.000000 | 53309555 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,049,632 | 2,246.731372 | 53309555 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,542,206 | 37,475.305871 | 53309555 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 2,749,283 | 0.029078 | 53309555 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,351,322 | 99.001427 | 53309555 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,054,854 | 1,206,344.208581 | 53309555 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,987,387 | 0.000013 | 53309555 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,766,052 | 0.000000 | 53309555 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,733,324 | 0.017638 | 53309555 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,688,295 | 416.366191 | 53309555 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,616,171 | 0.000013 | 53309555 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,568,205 | 0.000013 | 53309555 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,523,347 | 2,250.415909 | 53309555 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,520,145 | 1.536599 | 53309555 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,570 | 0.825600 | 53309555 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 1,426,299 | 0.000013 | 53309555 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,420,547 | 3,583.481949 | 53309555 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,313,120 | 2,246.419544 | 53309555 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,309,442 | 0.005131 | 53309555 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,309,405 | 14,336.057994 | 53309555 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,176,817 | 70.165644 | 53309555 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,113,924 | 35,605,065.258765 | 53309555 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,058,986 | 513,475.339366 | 53309555 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,037,358 | 21,020,489.174102 | 53309555 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,022,495 | 73,392.604757 | 53309555 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | DRB/WETH | 10000 | 1,015,681 | 0.000000 | 53309555 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | WETH/USDC | 3000 | 1,009,454 | 2,241.096554 | 53309555 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,006,624 | 18.596300 | 53309555 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 975,021 | 99.067827 | 53309555 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 967,499 | 66.878376 | 53309555 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 959,405 | 0.044075 | 53309555 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 927,289 | 1,221,638.656269 | 53309555 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,546 | 2,235.963227 | 53309555 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 895,687 | 1,072.191558 | 53309555 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 865,578 | 3,608.533624 | 53309555 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,605 | 0.000557 | 53309555 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 849,551 | 19.028175 | 53309555 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 841,272 | 0.063888 | 53309555 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,737 | 0.803531 | 53309555 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 739,147 | 0.000266 | 53309555 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 728,288 | 0.596958 | 53309555 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 727,901 | 4,479,862.917499 | 53309555 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 683,384 | 0.000008 | 53309555 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 680,250 | 2.331396 | 53309555 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 661,573 | 144,754.296800 | 53309555 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 657,823 | 510,925.074083 | 53309555 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 632,328 | 0.505450 | 53309555 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 621,904 | 0.095297 | 53309555 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 602,814 | 0.914710 | 53309555 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 542,574 | 1,071.963553 | 53309555 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 161 ; routes examinées : 3038392 ; candidats optimisés : 26018 ; net attendu > 0 : 0 ; dernier cycle 574.0 ms
- Rejets (moteur) : {'spread_below_threshold': 2976607, 'liquidity_below_min': 35275, 'negative_expected_net': 26018, 'unquotable': 322, 'borrow_bound_too_small': 161, 'cycle_budget_exhausted': 9}
- Enregistrements de la session : 26018 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 26018} ; motifs de rejet : {'negative_expected_net': 26018}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53309549 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→cbBTC | 0.000176 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0014 | -1.14 |
| 53309550 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→cbBTC | 0.000176 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0014 | -1.14 |
| 53309551 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→cbBTC | 0.000176 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0014 | -1.14 |
| 53309550 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→cbBTC | 0.000176 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0014 | -1.14 |
| 53309551 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→cbBTC | 0.000176 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0014 | -1.14 |
| 53309552 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→cbBTC | 0.000176 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0014 | -1.14 |
| 53309553 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→cbBTC | 0.000176 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0014 | -1.14 |
| 53309552 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→cbBTC | 0.000176 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0014 | -1.14 |
| 53309549 | USDC→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 20.408949 USDC | 0.003002 USDC | 0.000000 USDC | 0.004725 USDC | -0.0016 | -0.84 |
| 53309550 | USDC→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 20.408949 USDC | 0.003002 USDC | 0.000000 USDC | 0.004725 USDC | -0.0016 | -0.84 |

## Fiabilité et décision
- Observations ghost : 3898 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
