# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T11:23:21+00:00 ; durée 15.34 min ; blocs 53198162 → 53198624 (448 vus)

## Connexion
- Requêtes RPC : 5330 ; erreurs : 0 ; latence p50/p95 : 215.0/1,271.4 ms
- Rafraîchissements d'état : 448 ; âge des données au dernier bloc : 5.75 s ; changements de frais LP observés (pools à frais dynamiques) : 608
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4361 ; cycles déclenchés par événement : 390 ; avance médiane sur le rafraîchissement multicall : 839 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,364.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 525 pools, 303 jetons, 18974 routes
- Par DEX : uniswap_v3 148, aerodrome_slipstream 121, aerodrome 211, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 186 (rejetés 2) → 591 jetons ; pools candidats 3816 (énumérés 332, par paires 0), mesurés 527, sous le plancher de 10000.0 $ : 2 → gardés 525 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2367.672797, 'cbBTC': 81332.776577, 'AERO': 0.700175}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,376,847 | 2,364.230697 | 53198625 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,764,585 | 0.029036 | 53198625 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,890,151 | 0.000012 | 53198625 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,536,085 | 0.029095 | 53198625 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,495,296 | 2,362.927174 | 53198625 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,369,748 | 96.787314 | 53198625 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 7,217,569 | 1.428215 | 53198625 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,106,580 | 0.001649 | 53198625 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,758,845 | 0.029044 | 53198625 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 654 | 5,039,778 | 2,361.755629 | 53198625 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,467,436 | 2,361.930272 | 53198625 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,287,304 | 0.998874 | 53198625 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,792,675 | 36,372.652230 | 53198625 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,975,384 | 0.029081 | 53198625 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2754 | 2,552,272 | 96.732660 | 53198625 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,470,015 | 0.000012 | 53198625 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,157,482 | 1,217,459.143201 | 53198625 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,925,741 | 2,364.840395 | 53198625 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,840,756 | 0.019017 | 53198625 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,811,753 | 0.000000 | 53198625 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,800,468 | 399.860434 | 53198625 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,728,740 | 0.000012 | 53198625 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,705,418 | 0.000012 | 53198625 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,697,868 | 0.000012 | 53198625 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,522,021 | 0.005795 | 53198625 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,274 | 1.655260 | 53198625 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,465,334 | 3,378.689665 | 53198625 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,097 | 0.826865 | 53198625 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,400,940 | 13,752.741323 | 53198625 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,261,767 | 0.000267 | 53198625 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,238,732 | 2,361.006353 | 53198625 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,209,064 | 3,355.250368 | 53198625 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,193,954 | 68.165887 | 53198625 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,192,546 | 0.000267 | 53198625 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,170,280 | 1,070,201.036586 | 53198625 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,169,717 | 36,234,123.650805 | 53198625 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,164,625 | 0.000000 | 53198625 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,135,089 | 504,705.590106 | 53198625 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,086,228 | 72,382.496770 | 53198625 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,076,475 | 20,995,330.703511 | 53198625 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,052,643 | 16.448055 | 53198625 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,043,859 | 57.449840 | 53198625 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 1,007,726 | 97.124928 | 53198625 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 1,000,383 | 0.040992 | 53198625 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 942,440 | 2,360.576085 | 53198625 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 935,599 | 1,065.299887 | 53198625 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 912,015 | 0.000558 | 53198625 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 887,255 | 2.334541 | 53198625 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 881,612 | 17.895343 | 53198625 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 852,894 | 17.492966 | 53198625 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 852,381 | 2,364.541464 | 53198625 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 807,299 | 0.058517 | 53198625 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 800,469 | 0.803180 | 53198625 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 760,745 | 0.000009 | 53198625 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 755,305 | 0.630485 | 53198625 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 753,735 | 4,645,053.126900 | 53198625 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 720,118 | 135,731.266451 | 53198625 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 699,626 | 503,906.528839 | 53198625 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,766 | 0.108908 | 53198625 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 665,002 | 0.557772 | 53198625 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 837 ; routes examinées : 15881238 ; candidats optimisés : 75247 ; net attendu > 0 : 0 ; dernier cycle 374.3 ms
- Rejets (moteur) : {'spread_below_threshold': 15428601, 'liquidity_below_min': 376413, 'negative_expected_net': 75247, 'borrow_bound_too_small': 837, 'cycle_budget_exhausted': 140}
- Enregistrements de la session : 75247 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 75247} ; motifs de rejet : {'negative_expected_net': 75247}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53198489 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000453 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0022 | -0.66 |
| 53198489 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000453 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0022 | -0.66 |
| 53198450 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001295 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0022 | -0.23 |
| 53198450 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001295 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0022 | -0.23 |
| 53198466 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 8.680991 USDC | 0.002855 USDC | 0.000000 USDC | 0.005318 USDC | -0.0023 | -2.84 |
| 53198467 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 8.680991 USDC | 0.002855 USDC | 0.000000 USDC | 0.005318 USDC | -0.0023 | -2.84 |
| 53198492 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 4.779626 USDC | 0.002289 USDC | 0.000000 USDC | 0.004992 USDC | -0.0025 | -5.66 |
| 53198493 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 4.779626 USDC | 0.002289 USDC | 0.000000 USDC | 0.004992 USDC | -0.0025 | -5.66 |
| 53198493 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 4.779626 USDC | 0.002289 USDC | 0.000000 USDC | 0.004993 USDC | -0.0025 | -5.66 |
| 53198494 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 4.779626 USDC | 0.002289 USDC | 0.000000 USDC | 0.004993 USDC | -0.0025 | -5.66 |

## Fiabilité et décision
- Observations ghost : 2932 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
