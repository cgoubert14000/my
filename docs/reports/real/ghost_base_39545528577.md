# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T05:28:45+00:00 ; durée 39.9 min ; blocs 52884388 → 52885587 (1133 vus)

## Connexion
- Requêtes RPC : 13800 ; erreurs : 0 ; latence p50/p95 : 317.0/1,891.1 ms
- Rafraîchissements d'état : 1133 ; âge des données au dernier bloc : 2.89 s ; changements de frais LP observés (pools à frais dynamiques) : 2145
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 496 ; cycles déclenchés par événement : 36 ; avance médiane sur le rafraîchissement multicall : 1,078 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,447.38 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 328 jetons, 21464 routes
- Par DEX : uniswap_v3 137, aerodrome 236, aerodrome_slipstream 158, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 396, par paires 0), mesurés 582, sous le plancher de 10000.0 $ : 2 → gardés 580 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2447.377823, 'AERO': 0.859444, 'cbBTC': 82692.945421}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,605,192 | 2,447.379502 | 52885588 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,653,452 | 1.171916 | 52885588 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,614,970 | 0.029563 | 52885588 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,988,837 | 95.215912 | 52885588 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,518,718 | 0.029537 | 52885588 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,548,039 | 0.029573 | 52885588 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,927,663 | 0.000012 | 52885588 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,612,743 | 2,444.903735 | 52885588 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,377,574 | 2,447.995825 | 52885588 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,168,224 | 0.000012 | 52885588 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,655,770 | 2,444.128950 | 52885588 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 7,550,264 | 0.000012 | 52885588 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,272,361 | 0.001671 | 52885588 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,542,593 | 0.029531 | 52885588 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,256,325 | 0.024753 | 52885588 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 412 | 5,108,518 | 2,447.289629 | 52885588 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,717,443 | 0.802393 | 52885588 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,699,499 | 0.000277 | 52885588 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,455,525 | 2,443.965062 | 52885588 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,394,166 | 0.998741 | 52885588 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,041,013 | 34,789.318651 | 52885588 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,361,684 | 2,844.546331 | 52885588 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,275,960 | 1.164668 | 52885588 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/VVV | 2754 | 2,753,755 | 95.238922 | 52885588 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,718,347 | 397.225594 | 52885588 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,535,395 | 1.142084 | 52885588 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,449,333 | 0.000010 | 52885588 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,274,082 | 0.000012 | 52885588 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,241,238 | 1,210,470.665103 | 52885588 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,074,199 | 0.000012 | 52885588 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,210 | 1.238682 | 52885588 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,028,014 | 1.383164 | 52885588 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,948,268 | 0.000000 | 52885588 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,906,644 | 1.105697 | 52885588 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,818,102 | 0.019383 | 52885588 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,735,441 | 15.776688 | 52885588 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,715,773 | 0.021479 | 52885588 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,703,483 | 13,436.269958 | 52885588 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,689,054 | 2.311287 | 52885588 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,680,768 | 2,866.209642 | 52885588 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,569,319 | 0.916062 | 52885588 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,348 | 0.826534 | 52885588 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,423,360 | 1.122574 | 52885588 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,352,814 | 0.004809 | 52885588 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,328,058 | 0.000278 | 52885588 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,327,724 | 0.000000 | 52885588 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,309,705 | 0.029583 | 52885588 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,286,614 | 2,444.555379 | 52885588 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,876 | 63.619861 | 52885588 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,222,414 | 34,988,111.001513 | 52885588 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,220,926 | 23.087739 | 52885588 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,208,210 | 69,949.725712 | 52885588 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,195,631 | 1,135,982.068717 | 52885588 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,280 | 0.436726 | 52885588 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,179,497 | 484,016.326784 | 52885588 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,159,219 | 0.886245 | 52885588 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,156,834 | 47.082870 | 52885588 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,153,465 | 1.106158 | 52885588 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,116,071 | 20,316,195.460132 | 52885588 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,072,365 | 15.717376 | 52885588 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 1168 ; routes examinées : 25069952 ; candidats optimisés : 133820 ; net attendu > 0 : 0 ; dernier cycle 394.5 ms
- Rejets (moteur) : {'spread_below_threshold': 24772559, 'liquidity_below_min': 161799, 'negative_expected_net': 133820, 'borrow_bound_too_small': 1165, 'cycle_budget_exhausted': 609}
- Enregistrements de la session : 133820 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 133820} ; motifs de rejet : {'negative_expected_net': 133820}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52885496 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 75.502446 USDC | 0.007421 USDC | 0.000000 USDC | 0.007725 USDC | -0.0003 | -0.04 |
| 52885496 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.030311 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0003 | -0.05 |
| 52885496 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001024 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0008 | -0.10 |
| 52884780 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 6.147294 USDC | 0.003645 USDC | 0.000000 USDC | 0.005157 USDC | -0.0014 | -2.46 |
| 52884781 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 6.147294 USDC | 0.003645 USDC | 0.000000 USDC | 0.005157 USDC | -0.0014 | -2.46 |
| 52885416 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.052331 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0015 | -0.13 |
| 52885416 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 126.852193 USDC | 0.003860 USDC | 0.000000 USDC | 0.005494 USDC | -0.0015 | -0.13 |
| 52884845 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.003669 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0019 | -2.35 |
| 52885391 | WETH→[aerodrome]→MEY→[uniswap_v3]→WETH | 0.003924 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -2.24 |
| 52885392 | WETH→[aerodrome]→MEY→[uniswap_v3]→WETH | 0.003924 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -2.24 |

## Fiabilité et décision
- Observations ghost : 1593 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
