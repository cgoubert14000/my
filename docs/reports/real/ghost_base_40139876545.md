# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T23:01:46+00:00 ; durée 12.21 min ; blocs 53046410 → 53046779 (360 vus)

## Connexion
- Requêtes RPC : 4380 ; erreurs : 0 ; latence p50/p95 : 101.7/1,255.0 ms
- Rafraîchissements d'état : 361 ; âge des données au dernier bloc : 1.51 s ; changements de frais LP observés (pools à frais dynamiques) : 310
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3013 ; cycles déclenchés par événement : 300 ; avance médiane sur le rafraîchissement multicall : 366 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,338.78 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 538 pools, 309 jetons, 19504 routes
- Par DEX : uniswap_v3 143, aerodrome 216, aerodrome_slipstream 134, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 194 (rejetés 2) → 599 jetons ; pools candidats 3810 (énumérés 349, par paires 0), mesurés 540, sous le plancher de 10000.0 $ : 2 → gardés 538 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2338.582041, 'cbBTC': 80471.362994, 'AERO': 0.693033}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,434,233 | 2,338.781394 | 53046779 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,223,957 | 0.029116 | 53046779 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,169,702 | 0.029071 | 53046779 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,514,504 | 0.000012 | 53046779 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,874,251 | 97.018221 | 53046779 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,455,189 | 2,344.553083 | 53046779 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 8,030,250 | 1.437001 | 53046779 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,005,789 | 0.001647 | 53046779 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,662,525 | 2,344.252699 | 53046779 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,403,270 | 0.029115 | 53046779 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,457,052 | 2,344.286988 | 53046779 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,226,758 | 0.999829 | 53046779 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,881,640 | 34,376.536899 | 53046779 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,798,305 | 2,343.480492 | 53046779 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,258,448 | 0.029085 | 53046779 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,557,083 | 0.000012 | 53046779 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,489,350 | 97.061310 | 53046779 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,218,281 | 409.754789 | 53046779 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,112,162 | 1,243,064.919347 | 53046779 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,901,526 | 0.000000 | 53046779 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,900,534 | 0.000012 | 53046779 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,793,330 | 0.018098 | 53046779 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,728,383 | 0.000012 | 53046779 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,719,213 | 0.000012 | 53046779 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,573,526 | 0.000265 | 53046779 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,469,617 | 1.675565 | 53046779 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,859 | 0.826892 | 53046779 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,449,889 | 3,368.252358 | 53046779 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,414,890 | 0.005383 | 53046779 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,370,006 | 14,082.170084 | 53046779 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/AERO | 10000 | 1,280,388 | 3,354.530354 | 53046779 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,241,606 | 0.000266 | 53046779 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,237,880 | 2,344.599115 | 53046779 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,221,567 | 65.118992 | 53046779 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,197,022 | 0.000000 | 53046779 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,164,571 | 35,494,240.689132 | 53046779 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,130,957 | 1,122,024.394578 | 53046779 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,119,913 | 49.939984 | 53046779 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,116,100 | 498,179.264456 | 53046779 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,036,865 | 77,990.997510 | 53046779 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,028,195 | 17.522765 | 53046779 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,955 | 21,823,007.922020 | 53046779 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 950,991 | 17.097857 | 53046779 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | USDC/VVV | 3000 | 949,114 | 0.041502 | 53046779 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 925,799 | 2,323.794498 | 53046779 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 922,054 | 2.307052 | 53046779 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 921,239 | 1,102.034480 | 53046779 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 896,434 | 0.000551 | 53046779 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 883,520 | 17.806181 | 53046779 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 861,588 | 96.914711 | 53046779 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 848,103 | 2,338.862796 | 53046779 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 822,618 | 0.000009 | 53046779 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 819,879 | 0.060499 | 53046779 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 798,718 | 1.105872 | 53046779 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 791,877 | 0.803130 | 53046779 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,633 | 0.622804 | 53046779 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 739,313 | 4,723,215.600001 | 53046779 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 736,844 | 0.679611 | 53046779 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 718,305 | 133,398.443725 | 53046779 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2111 | 697,754 | 494,974.754233 | 53046779 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 660 ; routes examinées : 12872640 ; candidats optimisés : 31930 ; net attendu > 0 : 0 ; dernier cycle 98.9 ms
- Rejets (moteur) : {'spread_below_threshold': 12580100, 'liquidity_below_min': 258630, 'negative_expected_net': 31930, 'unquotable': 1320, 'borrow_bound_too_small': 660}
- Enregistrements de la session : 31930 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 31930} ; motifs de rejet : {'negative_expected_net': 31930}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53046693 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 16.951992 USDC | 0.004061 USDC | 0.000000 USDC | 0.005249 USDC | -0.0011 | -0.70 |
| 53046693 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.007297 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0011 | -0.70 |
| 53046737 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 16.232098 USDC | 0.003893 USDC | 0.000000 USDC | 0.005249 USDC | -0.0012 | -0.84 |
| 53046737 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.007062 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0013 | -0.83 |
| 53046737 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 14.868486 USDC | 0.003148 USDC | 0.000000 USDC | 0.005249 USDC | -0.0019 | -1.41 |
| 53046737 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.006316 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0019 | -1.43 |
| 53046737 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 14.867150 USDC | 0.003115 USDC | 0.000000 USDC | 0.005249 USDC | -0.0020 | -1.44 |
| 53046737 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 14.867150 USDC | 0.003115 USDC | 0.000000 USDC | 0.005249 USDC | -0.0020 | -1.44 |
| 53046737 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.006338 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -1.45 |
| 53046737 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.006338 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -1.45 |

## Fiabilité et décision
- Observations ghost : 2331 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
