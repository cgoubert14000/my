# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T19:07:14+00:00 ; durée 3.05 min ; blocs 52650847 → 52650943 (64 vus)

## Connexion
- Requêtes RPC : 926 ; erreurs : 13 ; latence p50/p95 : 158.1/2,687.5 ms
- Rafraîchissements d'état : 65 ; âge des données au dernier bloc : 1.61 s ; changements de frais LP observés (pools à frais dynamiques) : 215
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
| uniswap_v3 | WETH/USDC | 3000 | 146,588,699 | 2,445.656346 | 52650943 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,730,654 | 1.101367 | 52650943 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 19,783,165 | 0.029688 | 52650943 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,441,063 | 0.029744 | 52650943 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,969,202 | 96.514938 | 52650943 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,587,460 | 0.029675 | 52650943 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,743,253 | 0.000012 | 52650943 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,125,048 | 2,452.104420 | 52650943 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 7,995,784 | 0.000012 | 52650943 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 7,668,255 | 0.000012 | 52650943 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 639 | 7,484,223 | 2,452.301492 | 52650943 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,244,679 | 0.001681 | 52650943 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,443,627 | 2,445.742932 | 52650943 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,384,661 | 0.029741 | 52650943 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,338,047 | 0.024853 | 52650943 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,744,237 | 0.000278 | 52650943 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,734,794 | 0.802398 | 52650943 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,360,634 | 2,452.030360 | 52650943 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,338,144 | 0.997991 | 52650943 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,979,216 | 35,827.736753 | 52650943 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,590,572 | 1.109146 | 52650943 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,539,111 | 2,719.750295 | 52650943 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 421 | 3,365,294 | 2,455.449132 | 52650943 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,847,787 | 0.000012 | 52650943 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2805 | 2,693,446 | 96.497890 | 52650943 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,556,116 | 1.141629 | 52650943 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,445,212 | 0.000011 | 52650943 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,331,130 | 401.495680 | 52650943 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,264,943 | 1,183,594.563434 | 52650943 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,377 | 1.196132 | 52650943 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,083,078 | 0.000000 | 52650943 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52650943 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,941,473 | 15.704879 | 52650943 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,823,816 | 0.019078 | 52650943 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | fBOMB/USDC | 10000 | 1,806,664 | 0.022331 | 52650943 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,780,328 | 0.000012 | 52650943 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,688,236 | 2.309693 | 52650943 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2730 | 1,683,442 | 1,011.104630 | 52650943 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/AERO | 3000 | 1,567,205 | 2,699.688489 | 52650943 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,542,095 | 13,509.246087 | 52650943 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,512,126 | 1.105494 | 52650943 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,148 | 0.828707 | 52650943 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3316 | 1,400,210 | 2,701.641730 | 52650943 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,388,199 | 0.000000 | 52650943 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,367,496 | 23.176991 | 52650943 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,353,061 | 0.004813 | 52650943 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,329,689 | 0.000279 | 52650943 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,326,390 | 1.121169 | 52650943 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,285,449 | 0.916559 | 52650943 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/SEND | 3000 | 1,248,967 | 62.293193 | 52650943 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,224,226 | 0.886465 | 52650943 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,219,148 | 2,452.126615 | 52650943 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,213,255 | 35,397,498.267493 | 52650943 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,213,141 | 1.105591 | 52650943 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,190,855 | 1,143,728.726466 | 52650943 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,169,464 | 493,727.267552 | 52650943 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,168,259 | 1.132150 | 52650943 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/cbBTC | 3000 | 1,167,704 | 0.029671 | 52650943 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,163,009 | 0.436172 | 52650943 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,124,582 | 13.920902 | 52650943 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 64 ; routes examinées : 1372416 ; candidats optimisés : 6179 ; net attendu > 0 : 0 ; dernier cycle 263.4 ms
- Rejets (moteur) : {'spread_below_threshold': 1352096, 'liquidity_below_min': 14062, 'negative_expected_net': 6179, 'borrow_bound_too_small': 64, 'cycle_budget_exhausted': 15}
- Enregistrements de la session : 6179 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 6179} ; motifs de rejet : {'negative_expected_net': 6179}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52650921 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.007173 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0025 | -1.56 |
| 52650917 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.008644 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -1.30 |
| 52650921 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.007138 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0026 | -1.60 |
| 52650922 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.007030 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0027 | -1.69 |
| 52650922 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.006995 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0027 | -1.73 |
| 52650918 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.007573 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -1.83 |
| 52650926 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.005796 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0035 | -2.66 |
| 52650927 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.005796 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0035 | -2.66 |
| 52650928 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.005796 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0035 | -2.66 |
| 52650929 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.005796 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0035 | -2.66 |

## Fiabilité et décision
- Observations ghost : 384 ; taux observé 0.151 ; borne inférieure crédible (0.9) 0.129 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
