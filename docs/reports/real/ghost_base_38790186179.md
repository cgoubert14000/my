# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T19:19:29+00:00 ; durée 15.31 min ; blocs 52650847 → 52651308 (406 vus)

## Connexion
- Requêtes RPC : 4972 ; erreurs : 60 ; latence p50/p95 : 110.5/1,933.5 ms
- Rafraîchissements d'état : 406 ; âge des données au dernier bloc : 4.61 s ; changements de frais LP observés (pools à frais dynamiques) : 973
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,447.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21444 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 154, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3921 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 3 → gardés 573 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2444.445842, 'AERO': 0.898266, 'cbBTC': 82361.329534}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,643,128 | 2,447.207529 | 52651309 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,704,371 | 1.102681 | 52651309 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,451,561 | 0.029753 | 52651309 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,980,304 | 96.511075 | 52651309 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 11,982,837 | 0.029694 | 52651309 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,592,946 | 0.029678 | 52651309 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,744,653 | 0.000012 | 52651309 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,126,021 | 2,453.613373 | 52651309 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 7,996,890 | 0.000012 | 52651309 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 7,348,804 | 0.000012 | 52651309 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,243,391 | 0.001679 | 52651309 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 684 | 7,025,704 | 2,453.572669 | 52651309 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,027,586 | 1.109146 | 52651309 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,445,353 | 2,447.230597 | 52651309 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,386,618 | 0.029754 | 52651309 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,341,559 | 0.024849 | 52651309 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,747,299 | 0.000278 | 52651309 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,737,797 | 0.802398 | 52651309 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,362,580 | 2,453.395720 | 52651309 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,339,654 | 0.997993 | 52651309 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 436 | 4,040,255 | 2,456.831229 | 52651309 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 3,975,770 | 35,935.405282 | 52651309 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,538,111 | 2,719.930947 | 52651309 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,848,376 | 0.000012 | 52651309 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,821,646 | 401.583842 | 52651309 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,695,168 | 96.497895 | 52651309 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,561,457 | 0.000011 | 52651309 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,546,444 | 1.141670 | 52651309 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,342,290 | 1,012.556240 | 52651309 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,270,365 | 1,179,442.080380 | 52651309 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,377 | 1.196132 | 52651309 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,084,398 | 0.000000 | 52651309 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52651309 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,954,843 | 15.704677 | 52651309 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,830,447 | 0.019129 | 52651309 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | fBOMB/USDC | 10000 | 1,809,226 | 0.022387 | 52651309 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,780,540 | 0.000012 | 52651309 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,689,043 | 2.310264 | 52651309 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,665,866 | 13,509.246087 | 52651309 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,567,297 | 2,700.655850 | 52651309 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,513,085 | 1.105494 | 52651309 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,547 | 0.830165 | 52651309 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,400,120 | 2,701.641718 | 52651309 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,389,073 | 0.000000 | 52651309 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,370,597 | 23.176991 | 52651309 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,368,143 | 0.004833 | 52651309 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,330,541 | 0.000279 | 52651309 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,326,061 | 1.120763 | 52651309 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,286,225 | 0.916559 | 52651309 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/SEND | 3000 | 1,248,967 | 62.293193 | 52651309 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,218,431 | 2,453.492828 | 52651309 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,213,911 | 1.105591 | 52651309 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,213,826 | 35,414,818.528332 | 52651309 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,199,124 | 0.886264 | 52651309 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,191,565 | 1,143,816.926955 | 52651309 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,170,205 | 493,727.267552 | 52651309 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,165,616 | 1.132173 | 52651309 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,163,900 | 0.436670 | 52651309 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/cbBTC | 3000 | 1,159,958 | 0.029671 | 52651309 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,122,374 | 13.989128 | 52651309 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 404 ; routes examinées : 8663376 ; candidats optimisés : 36382 ; net attendu > 0 : 0 ; dernier cycle 373.6 ms
- Rejets (moteur) : {'spread_below_threshold': 8554944, 'liquidity_below_min': 71631, 'negative_expected_net': 36382, 'borrow_bound_too_small': 404, 'cycle_budget_exhausted': 15}
- Enregistrements de la session : 36382 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 36382} ; motifs de rejet : {'negative_expected_net': 36382}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52651243 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 5.151130 USDC | 0.003421 USDC | 0.000000 USDC | 0.005169 USDC | -0.0016 | -3.39 |
| 52651244 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 5.151130 USDC | 0.003421 USDC | 0.000000 USDC | 0.005169 USDC | -0.0016 | -3.39 |
| 52651243 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.002151 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -3.34 |
| 52651244 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.002151 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0016 | -3.34 |
| 52651243 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 5.039891 USDC | 0.003294 USDC | 0.000000 USDC | 0.005169 USDC | -0.0017 | -3.72 |
| 52651244 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 5.039891 USDC | 0.003294 USDC | 0.000000 USDC | 0.005169 USDC | -0.0017 | -3.72 |
| 52651243 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.002098 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0017 | -3.67 |
| 52651244 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.002098 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0017 | -3.67 |
| 52650999 | WETH→[aerodrome_slipstream]→BID→[aerodrome]→WETH | 0.002451 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -3.63 |
| 52651238 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.751621 USDC | 0.002955 USDC | 0.000000 USDC | 0.005168 USDC | -0.0020 | -4.66 |

## Fiabilité et décision
- Observations ghost : 384 ; taux observé 0.151 ; borne inférieure crédible (0.9) 0.129 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
