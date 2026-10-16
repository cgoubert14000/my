# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T06:26:34+00:00 ; durée 9.17 min ; blocs 52671044 → 52671323 (249 vus)

## Connexion
- Requêtes RPC : 2967 ; erreurs : 0 ; latence p50/p95 : 217.2/2,139.1 ms
- Rafraîchissements d'état : 250 ; âge des données au dernier bloc : 1.37 s ; changements de frais LP observés (pools à frais dynamiques) : 466
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,445.33 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 327 jetons, 21788 routes
- Par DEX : uniswap_v3 137, aerodrome 236, aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 392, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 3 → gardés 576 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2445.329592, 'AERO': 0.931569, 'cbBTC': 81962.021553}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,812,510 | 2,445.329593 | 52671323 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 47,410,009 | 1.072383 | 52671323 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,495,791 | 0.029780 | 52671323 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,550,891 | 99.951667 | 52671323 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,472,551 | 0.029754 | 52671323 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,584,732 | 0.029738 | 52671323 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,745,248 | 0.000012 | 52671323 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,131,286 | 2,442.368338 | 52671323 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,088,283 | 0.000012 | 52671323 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 7,586,675 | 0.000012 | 52671323 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 609 | 7,277,418 | 2,442.759063 | 52671323 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,241,627 | 0.001684 | 52671323 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | fBOMB/AERO | 10000 | 5,510,493 | 0.024690 | 52671323 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,444,236 | 2,445.624215 | 52671323 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,410,065 | 0.029790 | 52671323 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,225,246 | 1.000855 | 52671323 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,887,715 | 0.802398 | 52671323 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,753,220 | 0.000280 | 52671323 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,379,923 | 2,442.972709 | 52671323 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,359,879 | 0.998882 | 52671323 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,062,733 | 34,360.677314 | 52671323 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,003,541 | 1.079738 | 52671323 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,586,535 | 2,636.924234 | 52671323 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 415 | 3,453,983 | 2,446.358073 | 52671323 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,043,434 | 1.141827 | 52671323 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,846,842 | 0.000012 | 52671323 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,741,176 | 400.521840 | 52671323 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,673,274 | 99.922180 | 52671323 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,665,435 | 0.000011 | 52671323 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,293,997 | 1,153,495.001439 | 52671323 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,736 | 1.195936 | 52671323 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,103,523 | 0.000000 | 52671323 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,461 | 1.403757 | 52671323 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,926,161 | 15.372487 | 52671323 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,835,663 | 0.023018 | 52671323 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,802,898 | 0.019239 | 52671323 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,386 | 0.000012 | 52671323 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,715,343 | 13,460.154711 | 52671323 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,687,722 | 2.309855 | 52671323 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,580,522 | 2,617.696611 | 52671323 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,519,985 | 0.916551 | 52671323 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,511,963 | 1.105492 | 52671323 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,497,166 | 2,618.346502 | 52671323 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,179 | 0.829157 | 52671323 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,371,285 | 0.000000 | 52671323 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,368,983 | 0.004831 | 52671323 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,338,896 | 23.218499 | 52671323 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,333,278 | 0.000282 | 52671323 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,296,380 | 0.436346 | 52671323 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,262,406 | 1.123099 | 52671323 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,248,987 | 62.291240 | 52671323 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,220,902 | 2,442.297152 | 52671323 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,216,750 | 35,046,432.847538 | 52671323 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,216,378 | 0.029726 | 52671323 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,213,455 | 1.105591 | 52671323 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,191,108 | 1,142,938.389757 | 52671323 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,185,946 | 0.886093 | 52671323 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,172,858 | 496,814.181422 | 52671323 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,137,614 | 13.531807 | 52671323 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,113,798 | 83,915.376150 | 52671323 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 249 ; routes examinées : 5425212 ; candidats optimisés : 43907 ; net attendu > 0 : 0 ; dernier cycle 547.0 ms
- Rejets (moteur) : {'spread_below_threshold': 5332819, 'liquidity_below_min': 48237, 'negative_expected_net': 43907, 'borrow_bound_too_small': 249}
- Enregistrements de la session : 43907 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 43907} ; motifs de rejet : {'negative_expected_net': 43907}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52671214 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 12.067168 USDC | 0.003227 USDC | 0.000000 USDC | 0.005494 USDC | -0.0021 | -1.88 |
| 52671216 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 12.067168 USDC | 0.003227 USDC | 0.000000 USDC | 0.005494 USDC | -0.0021 | -1.88 |
| 52671217 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 12.067168 USDC | 0.003227 USDC | 0.000000 USDC | 0.005494 USDC | -0.0021 | -1.88 |
| 52671218 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 12.067168 USDC | 0.003227 USDC | 0.000000 USDC | 0.005494 USDC | -0.0021 | -1.88 |
| 52671219 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 12.067168 USDC | 0.003227 USDC | 0.000000 USDC | 0.005494 USDC | -0.0021 | -1.88 |
| 52671220 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 12.067168 USDC | 0.003227 USDC | 0.000000 USDC | 0.005494 USDC | -0.0021 | -1.88 |
| 52671221 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 12.067168 USDC | 0.003227 USDC | 0.000000 USDC | 0.005494 USDC | -0.0021 | -1.88 |
| 52671222 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 12.067168 USDC | 0.003227 USDC | 0.000000 USDC | 0.005494 USDC | -0.0021 | -1.88 |
| 52671223 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 12.067168 USDC | 0.003227 USDC | 0.000000 USDC | 0.005494 USDC | -0.0021 | -1.88 |
| 52671252 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.001195 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0038 | -14.03 |

## Fiabilité et décision
- Observations ghost : 443 ; taux observé 0.131 ; borne inférieure crédible (0.9) 0.112 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
