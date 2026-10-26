# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T08:40:31+00:00 ; durée 3.01 min ; blocs 53107248 → 53107341 (90 vus)

## Connexion
- Requêtes RPC : 1134 ; erreurs : 0 ; latence p50/p95 : 242.5/1,702.8 ms
- Rafraîchissements d'état : 90 ; âge des données au dernier bloc : 2.6 s ; changements de frais LP observés (pools à frais dynamiques) : 247
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 524 ; cycles déclenchés par événement : 28 ; avance médiane sur le rafraîchissement multicall : 1,135 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,320.66 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 527 pools, 302 jetons, 19574 routes
- Par DEX : uniswap_v3 142, aerodrome 213, aerodrome_slipstream 127, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 188 (rejetés 2) → 593 jetons ; pools candidats 3779 (énumérés 339, par paires 0), mesurés 529, sous le plancher de 10000.0 $ : 2 → gardés 527 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2317.899718, 'cbBTC': 80102.759686, 'AERO': 0.672129}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,443,362 | 2,320.661501 | 53107342 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,461,802 | 0.029003 | 53107342 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,170,418 | 0.028978 | 53107342 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,473,230 | 0.000012 | 53107342 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,820,487 | 93.799559 | 53107342 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,311,103 | 2,326.497437 | 53107342 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,176,632 | 1.487810 | 53107342 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,982,733 | 0.001649 | 53107342 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,397,188 | 2,325.940867 | 53107342 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,358,292 | 0.029003 | 53107342 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,467,152 | 2,325.929614 | 53107342 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,212,099 | 0.998980 | 53107342 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,823,573 | 34,480.318705 | 53107342 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,760,235 | 2,320.722629 | 53107342 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,193,470 | 0.028970 | 53107342 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2835 | 2,492,405 | 93.790066 | 53107342 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 2,478,903 | 0.000012 | 53107342 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,193,519 | 411.257938 | 53107342 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,124,107 | 1,210,151.770244 | 53107342 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,891,999 | 0.000013 | 53107342 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,889,148 | 0.000000 | 53107342 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,804,556 | 0.018208 | 53107342 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,712,774 | 0.000012 | 53107342 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 1,696,975 | 0.000012 | 53107342 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,556,934 | 0.000265 | 53107342 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,199 | 0.825536 | 53107342 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53107342 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,433,271 | 0.005516 | 53107342 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,419,543 | 3,454.771542 | 53107342 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,360,681 | 14,195.128111 | 53107342 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/AERO | 10000 | 1,234,544 | 3,469.603693 | 53107342 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,233,013 | 0.000265 | 53107342 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,220,823 | 65.198383 | 53107342 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,218,677 | 2,326.405871 | 53107342 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,157,676 | 0.000000 | 53107342 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,155,051 | 35,513,300.369835 | 53107342 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,129,524 | 1,107,504.316125 | 53107342 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,109,208 | 499,904.824560 | 53107342 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,079,673 | 19,723,527.660333 | 53107342 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,067,895 | 54.924105 | 53107342 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,066,164 | 72,604.066496 | 53107342 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,032,692 | 17.316995 | 53107342 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 967,858 | 0.040318 | 53107342 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 922,703 | 2,304.341200 | 53107342 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 908,367 | 2.308521 | 53107342 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 889,308 | 0.000551 | 53107342 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 875,561 | 17.205690 | 53107342 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/MORPHO | 3000 | 874,541 | 1,149.849364 | 53107342 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 870,640 | 18.249152 | 53107342 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 868,712 | 94.428428 | 53107342 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 844,920 | 2,320.239489 | 53107342 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 796,492 | 0.000008 | 53107342 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 789,630 | 0.055853 | 53107342 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 785,736 | 0.803142 | 53107342 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 775,858 | 1.105941 | 53107342 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 744,123 | 0.615693 | 53107342 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 730,338 | 4,766,292.445206 | 53107342 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 711,121 | 0.635188 | 53107342 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 700,602 | 138,095.572323 | 53107342 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2138 | 690,932 | 500,475.460137 | 53107342 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 117 ; routes examinées : 2290158 ; candidats optimisés : 11990 ; net attendu > 0 : 5 ; dernier cycle 312.1 ms
- Rejets (moteur) : {'spread_below_threshold': 2246276, 'liquidity_below_min': 29435, 'negative_expected_net': 11985, 'unquotable': 2340, 'borrow_bound_too_small': 117}
- Enregistrements de la session : 11990 ; net attendu > 0 : 5 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 11990} ; motifs de rejet : {'below_safety_margin': 5, 'negative_expected_net': 11985, 'p_lower_below_threshold': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53107313 | USDC→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 30.930355 USDC | 0.007910 USDC | 0.000000 USDC | 0.006981 USDC | 0.000929 USDC (0.0009 €) | — | 0.30 | 0.133 (n=344) | REJECTED | below_safety_margin(929<6186), p_lower_below_threshold(0.13<0.75) |
| 53107313 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC | 0.000380 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.26 | 0.133 (n=344) | REJECTED | below_safety_margin(1<7), p_lower_below_threshold(0.13<0.75) |
| 53107313 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000379 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.26 | 0.133 (n=344) | REJECTED | below_safety_margin(1<7), p_lower_below_threshold(0.13<0.75) |
| 53107313 | USDC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 30.898475 USDC | 0.007709 USDC | 0.000000 USDC | 0.006981 USDC | 0.000728 USDC (0.0007 €) | — | 0.24 | 0.133 (n=344) | REJECTED | below_safety_margin(728<6179), p_lower_below_threshold(0.13<0.75) |
| 53107313 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 62.977460 USDC | 0.007340 USDC | 0.000000 USDC | 0.006981 USDC | 0.000359 USDC (0.0003 €) | — | 0.06 | 0.133 (n=344) | REJECTED | below_safety_margin(359<12595), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2607 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
