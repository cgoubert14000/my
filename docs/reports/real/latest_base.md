# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T00:32:33+00:00 ; durée 3.01 min ; blocs 53481408 → 53481502 (90 vus)

## Connexion
- Requêtes RPC : 1027 ; erreurs : 0 ; latence p50/p95 : 315.5/1,536.2 ms
- Rafraîchissements d'état : 90 ; âge des données au dernier bloc : 2.36 s ; changements de frais LP observés (pools à frais dynamiques) : 219
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 102 ; cycles déclenchés par événement : 14 ; avance médiane sur le rafraîchissement multicall : 714 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,264.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 282 jetons, 19430 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 105, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3703 (énumérés 305, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2264.542979, 'cbBTC': 77119.048638, 'AERO': 0.629628}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,945,459 | 2,264.540173 | 53481502 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,617,659 | 0.029384 | 53481502 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,120,132 | 0.029422 | 53481502 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,031,750 | 0.000013 | 53481502 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,991,279 | 2,265.092068 | 53481502 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,701,085 | 101.225585 | 53481502 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,543,318 | 0.001561 | 53481502 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,393,789 | 1.588237 | 53481502 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,787,451 | 0.029397 | 53481502 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,200,578 | 2,265.267865 | 53481502 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,054,332 | 0.999909 | 53481502 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,842,601 | 2,265.501787 | 53481502 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,407,758 | 41,327.432070 | 53481502 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,661,363 | 0.029408 | 53481502 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,139,787 | 1,135,502.765144 | 53481502 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,112,060 | 101.257328 | 53481502 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 1,805,608 | 0.000013 | 53481502 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,734,346 | 0.017739 | 53481502 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,662,443 | 0.000000 | 53481502 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,647,587 | 0.006712 | 53481502 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,618,111 | 0.000013 | 53481502 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53481502 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,548,167 | 0.000013 | 53481502 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,542,159 | 438.914475 | 53481502 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,500,820 | 2,265.516962 | 53481502 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,819 | 0.821830 | 53481502 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,416,441 | 3,600.808778 | 53481502 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,334,509 | 2,266.012909 | 53481502 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,328,639 | 2,265.100874 | 53481502 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,285,275 | 14,946.590059 | 53481502 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,466 | 72.405863 | 53481502 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,864 | 37,029,594.047280 | 53481502 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,055,604 | 0.000000 | 53481502 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,045,050 | 549,003.576608 | 53481502 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,024,315 | 21,959,035.191017 | 53481502 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 995,033 | 19.223873 | 53481502 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 957,928 | 101.018629 | 53481502 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 953,090 | 86,121.555971 | 53481502 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/MORPHO | 3000 | 939,485 | 1,060.061391 | 53481502 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 936,812 | 0.000013 | 53481502 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 929,960 | 72.388791 | 53481502 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 925,411 | 2,280.773375 | 53481502 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 917,070 | 1,271,961.163077 | 53481502 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 882,068 | 0.044744 | 53481502 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 870,830 | 0.000555 | 53481502 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 841,191 | 3,611.587591 | 53481502 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 820,288 | 20.093057 | 53481502 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 789,392 | 0.055780 | 53481502 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 768,646 | 0.799140 | 53481502 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 731,281 | 0.584204 | 53481502 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 719,541 | 0.000257 | 53481502 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 705,004 | 4,879,466.432812 | 53481502 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 669,392 | 0.000008 | 53481502 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 662,195 | 147,654.322779 | 53481502 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 652,562 | 0.535861 | 53481502 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 651,281 | 2.365071 | 53481502 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 641,713 | 553,049.745599 | 53481502 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 608,283 | 0.914716 | 53481502 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 584,603 | 0.086620 | 53481502 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 561,459 | 0.038227 | 53481502 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 103 ; routes examinées : 2001290 ; candidats optimisés : 5056 ; net attendu > 0 : 0 ; dernier cycle 308.2 ms
- Rejets (moteur) : {'spread_below_threshold': 1973962, 'liquidity_below_min': 22169, 'negative_expected_net': 5056, 'borrow_bound_too_small': 103}
- Enregistrements de la session : 5056 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 5056} ; motifs de rejet : {'negative_expected_net': 5056}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53481455 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 11.119686 USDC | 0.001739 USDC | 0.000000 USDC | 0.005090 USDC | -0.0031 | -3.01 |
| 53481484 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC | 19.785019 USDC | 0.003085 USDC | 0.000000 USDC | 0.006808 USDC | -0.0034 | -1.88 |
| 53481485 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC | 19.785019 USDC | 0.003085 USDC | 0.000000 USDC | 0.006808 USDC | -0.0034 | -1.88 |
| 53481486 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC | 19.785019 USDC | 0.003085 USDC | 0.000000 USDC | 0.006808 USDC | -0.0034 | -1.88 |
| 53481461 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 9.468775 USDC | 0.001251 USDC | 0.000000 USDC | 0.005089 USDC | -0.0035 | -4.05 |
| 53481502 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000349 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0035 | -1.43 |
| 53481485 | cbBTC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000157 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0035 | -3.19 |
| 53481485 | cbBTC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000238 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0035 | -2.10 |
| 53481486 | cbBTC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000157 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0035 | -3.19 |
| 53481486 | cbBTC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000238 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0035 | -2.10 |

## Fiabilité et décision
- Observations ghost : 4940 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
