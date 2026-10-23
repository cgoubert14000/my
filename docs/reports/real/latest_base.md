# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T18:42:30+00:00 ; durée 6.04 min ; blocs 52995614 → 52995800 (175 vus)

## Connexion
- Requêtes RPC : 2206 ; erreurs : 0 ; latence p50/p95 : 307.4/1,837.4 ms
- Rafraîchissements d'état : 175 ; âge des données au dernier bloc : 2.84 s ; changements de frais LP observés (pools à frais dynamiques) : 277
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1638 ; cycles déclenchés par événement : 161 ; avance médiane sur le rafraîchissement multicall : 655 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,404.30 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 317 jetons, 19488 routes
- Par DEX : uniswap_v3 138, aerodrome 222, aerodrome_slipstream 137, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 200 (rejetés 2) → 605 jetons ; pools candidats 3880 (énumérés 359, par paires 0), mesurés 548, sous le plancher de 10000.0 $ : 2 → gardés 546 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2404.297357, 'AERO': 0.765849, 'cbBTC': 81434.30056}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,320,324 | 2,404.297098 | 52995801 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,580,805 | 0.029508 | 52995801 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,651,672 | 94.979005 | 52995801 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 10,619,814 | 1.308142 | 52995801 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,289,387 | 0.029437 | 52995801 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,775,595 | 0.000012 | 52995801 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,862,386 | 0.029452 | 52995801 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,694,795 | 2,401.748657 | 52995801 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,155,465 | 0.001670 | 52995801 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,347,474 | 0.000012 | 52995801 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,479,072 | 2,401.751837 | 52995801 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,452,985 | 0.029498 | 52995801 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 4,922,553 | 0.000012 | 52995801 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,558,618 | 2,401.732966 | 52995801 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,288,167 | 0.999604 | 52995801 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,242,739 | 2,408.016429 | 52995801 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,994,154 | 34,333.198049 | 52995801 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,412,261 | 0.000275 | 52995801 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 415 | 2,808,578 | 2,405.735572 | 52995801 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2730 | 2,539,392 | 95.003741 | 52995801 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,312,936 | 394.418358 | 52995801 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,213,232 | 1,196,441.544061 | 52995801 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,069,471 | 3,147.955966 | 52995801 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,947,573 | 0.000000 | 52995801 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,929,350 | 0.000012 | 52995801 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,778,688 | 0.018127 | 52995801 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,745,715 | 0.000012 | 52995801 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,556,011 | 1.605522 | 52995801 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,533,285 | 3,140.666553 | 52995801 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,102 | 0.824389 | 52995801 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,416,389 | 13,367.671129 | 52995801 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,386,309 | 0.005033 | 52995801 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,304,689 | 2.309413 | 52995801 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,300,099 | 0.000275 | 52995801 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,296,898 | 2,401.586857 | 52995801 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,266,078 | 0.000000 | 52995801 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,228,362 | 64.400566 | 52995801 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,806 | 35,714,679.691501 | 52995801 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,170,015 | 483,625.137105 | 52995801 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,169,134 | 1,114,911.728779 | 52995801 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,148,541 | 47.494524 | 52995801 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,146,382 | 16.265509 | 52995801 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,081,950 | 75,714.256358 | 52995801 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,077,364 | 20,962,238.217469 | 52995801 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,073,144 | 0.039546 | 52995801 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,051,967 | 16.470323 | 52995801 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 994,932 | 23.117455 | 52995801 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 961,658 | 1,049.541643 | 52995801 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 940,240 | 2,390.810405 | 52995801 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 914,713 | 0.000543 | 52995801 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 911,182 | 0.000009 | 52995801 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 895,936 | 17.374848 | 52995801 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 859,977 | 2,408.158728 | 52995801 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 831,954 | 0.062445 | 52995801 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 831,230 | 1.105789 | 52995801 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 814,646 | 0.803225 | 52995801 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 780,358 | 0.661754 | 52995801 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 778,038 | 4,505,902.995784 | 52995801 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 732,375 | 135,528.705428 | 52995801 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 731,579 | 0.670931 | 52995801 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 335 ; routes examinées : 6528480 ; candidats optimisés : 22205 ; net attendu > 0 : 0 ; dernier cycle 164.3 ms
- Rejets (moteur) : {'spread_below_threshold': 6445867, 'liquidity_below_min': 60073, 'negative_expected_net': 22205, 'borrow_bound_too_small': 335}
- Enregistrements de la session : 22205 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 22205} ; motifs de rejet : {'negative_expected_net': 22205}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52995771 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.001315 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -11.86 |
| 52995771 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.001315 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -11.86 |
| 52995772 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.001315 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -11.86 |
| 52995773 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.001315 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -11.86 |
| 52995773 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.001315 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -11.86 |
| 52995771 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 3.124438 USDC | 0.001326 USDC | 0.000000 USDC | 0.005077 USDC | -0.0035 | -12.01 |
| 52995771 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 3.124438 USDC | 0.001326 USDC | 0.000000 USDC | 0.005077 USDC | -0.0035 | -12.01 |
| 52995772 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 3.124438 USDC | 0.001326 USDC | 0.000000 USDC | 0.005077 USDC | -0.0035 | -12.01 |
| 52995773 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 3.124438 USDC | 0.001326 USDC | 0.000000 USDC | 0.005077 USDC | -0.0035 | -12.01 |
| 52995773 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 3.124438 USDC | 0.001326 USDC | 0.000000 USDC | 0.005077 USDC | -0.0035 | -12.01 |

## Fiabilité et décision
- Observations ghost : 2049 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
