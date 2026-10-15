# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T19:10:19+00:00 ; durée 6.14 min ; blocs 52650847 → 52651036 (151 vus)

## Connexion
- Requêtes RPC : 1925 ; erreurs : 15 ; latence p50/p95 : 108.5/1,907.4 ms
- Rafraîchissements d'état : 152 ; âge des données au dernier bloc : 0.65 s ; changements de frais LP observés (pools à frais dynamiques) : 445
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,445.66 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21444 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 154, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3921 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 3 → gardés 573 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2444.445842, 'AERO': 0.898266, 'cbBTC': 82361.329534}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,589,608 | 2,445.657032 | 52651036 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,701,966 | 1.102750 | 52651036 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 19,244,488 | 0.029688 | 52651036 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,443,046 | 0.029733 | 52651036 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,969,259 | 96.514344 | 52651036 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,589,229 | 0.029675 | 52651036 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,744,763 | 0.000012 | 52651036 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,125,050 | 2,448.714768 | 52651036 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,172,342 | 0.000012 | 52651036 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,996,972 | 0.000012 | 52651036 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 698 | 7,607,644 | 2,448.067671 | 52651036 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,243,375 | 0.001679 | 52651036 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,085,104 | 1.109146 | 52651036 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,443,628 | 2,445.832673 | 52651036 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,384,430 | 0.029721 | 52651036 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,334,684 | 0.024853 | 52651036 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,744,238 | 0.000278 | 52651036 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,734,796 | 0.802398 | 52651036 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,360,532 | 2,447.800345 | 52651036 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,339,872 | 0.997991 | 52651036 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,979,217 | 35,827.736753 | 52651036 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,536,882 | 2,719.751313 | 52651036 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 433 | 3,416,689 | 2,451.211274 | 52651036 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,848,444 | 0.000012 | 52651036 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,817,977 | 401.561986 | 52651036 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,693,452 | 96.497890 | 52651036 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,556,116 | 1.141628 | 52651036 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,475,055 | 0.000011 | 52651036 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,264,943 | 1,183,594.563434 | 52651036 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,377 | 1.196132 | 52651036 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,083,078 | 0.000000 | 52651036 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52651036 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,953,605 | 15.704677 | 52651036 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,823,364 | 0.019068 | 52651036 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | fBOMB/USDC | 10000 | 1,806,666 | 0.022331 | 52651036 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,780,553 | 0.000012 | 52651036 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,688,236 | 2.309693 | 52651036 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,657,620 | 13,509.246087 | 52651036 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,566,591 | 2,700.690993 | 52651036 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/MORPHO | 2727 | 1,518,945 | 1,012.108210 | 52651036 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | weETH_04c0/WETH | 500 | 1,512,126 | 1.105494 | 52651036 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,547 | 0.830165 | 52651036 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3152 | 1,399,582 | 2,701.641730 | 52651036 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,388,193 | 0.000000 | 52651036 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,367,508 | 23.176991 | 52651036 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,362,775 | 0.004813 | 52651036 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,329,690 | 0.000279 | 52651036 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,326,377 | 1.121152 | 52651036 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,285,449 | 0.916559 | 52651036 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/SEND | 3000 | 1,248,967 | 62.293193 | 52651036 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,223,148 | 0.886464 | 52651036 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,219,140 | 2,448.885027 | 52651036 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,213,256 | 35,397,498.267493 | 52651036 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,213,142 | 1.105591 | 52651036 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,190,856 | 1,143,728.726466 | 52651036 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,169,464 | 493,727.267552 | 52651036 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,168,523 | 1.132148 | 52651036 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/cbBTC | 3000 | 1,167,937 | 0.029671 | 52651036 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,163,009 | 0.436172 | 52651036 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,123,591 | 13.951438 | 52651036 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 151 ; routes examinées : 3238044 ; candidats optimisés : 12256 ; net attendu > 0 : 0 ; dernier cycle 341.1 ms
- Rejets (moteur) : {'spread_below_threshold': 3196809, 'liquidity_below_min': 28813, 'negative_expected_net': 12256, 'borrow_bound_too_small': 151, 'cycle_budget_exhausted': 15}
- Enregistrements de la session : 12256 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 12256} ; motifs de rejet : {'negative_expected_net': 12256}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52650999 | WETH→[aerodrome_slipstream]→BID→[aerodrome]→WETH | 0.002451 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -3.63 |
| 52650988 | WETH→[aerodrome_slipstream]→BID→[aerodrome]→WETH | 0.002323 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0023 | -4.37 |
| 52650989 | WETH→[aerodrome_slipstream]→BID→[aerodrome]→WETH | 0.002323 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0023 | -4.37 |
| 52650921 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.007173 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0025 | -1.56 |
| 52650917 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.008644 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -1.30 |
| 52650921 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.007138 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0026 | -1.60 |
| 52650922 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.007030 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0027 | -1.69 |
| 52650922 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.006995 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0027 | -1.73 |
| 52650918 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.007573 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -1.83 |
| 52651036 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 3.558017 USDC | 0.001594 USDC | 0.000000 USDC | 0.005169 USDC | -0.0033 | -10.05 |

## Fiabilité et décision
- Observations ghost : 384 ; taux observé 0.151 ; borne inférieure crédible (0.9) 0.129 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
