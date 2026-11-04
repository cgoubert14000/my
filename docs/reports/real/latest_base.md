# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T00:35:37+00:00 ; durée 6.07 min ; blocs 53481408 → 53481594 (179 vus)

## Connexion
- Requêtes RPC : 1978 ; erreurs : 0 ; latence p50/p95 : 330.3/1,612.3 ms
- Rafraîchissements d'état : 180 ; âge des données au dernier bloc : 1.92 s ; changements de frais LP observés (pools à frais dynamiques) : 469
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 102 ; cycles déclenchés par événement : 14 ; avance médiane sur le rafraîchissement multicall : 714 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,263.63 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 282 jetons, 19430 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 105, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3703 (énumérés 305, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2264.542979, 'cbBTC': 77119.048638, 'AERO': 0.629628}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,908,656 | 2,263.627927 | 53481594 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,610,067 | 0.029390 | 53481594 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,115,643 | 0.029422 | 53481594 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,028,849 | 0.000013 | 53481594 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,988,930 | 2,260.568332 | 53481594 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,687,537 | 101.500867 | 53481594 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,538,535 | 0.001560 | 53481594 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,393,721 | 1.588277 | 53481594 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,785,217 | 0.029399 | 53481594 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,203,710 | 2,260.849627 | 53481594 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,051,937 | 0.999909 | 53481594 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,841,410 | 2,260.799341 | 53481594 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,406,385 | 41,327.432070 | 53481594 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,660,138 | 0.029408 | 53481594 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,138,925 | 1,135,502.765144 | 53481594 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2769 | 2,108,058 | 101.522709 | 53481594 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,804,902 | 0.000013 | 53481594 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,730,561 | 0.017675 | 53481594 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,661,773 | 0.000000 | 53481594 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,647,180 | 0.006713 | 53481594 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,617,454 | 0.000013 | 53481594 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53481594 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,547,649 | 0.000013 | 53481594 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,539,821 | 440.538798 | 53481594 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,500,518 | 2,263.847002 | 53481594 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,819 | 0.821830 | 53481594 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,416,189 | 3,604.389488 | 53481594 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,334,240 | 2,264.323395 | 53481594 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,328,264 | 2,260.604872 | 53481594 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,282,573 | 14,967.318027 | 53481594 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,466 | 72.405863 | 53481594 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,416 | 37,029,594.047280 | 53481594 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,055,178 | 0.000000 | 53481594 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,044,012 | 549,931.380420 | 53481594 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,600 | 21,970,183.467339 | 53481594 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,509 | 19.253142 | 53481594 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 955,045 | 101.018629 | 53481594 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 952,706 | 86,121.555971 | 53481594 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/MORPHO | 3000 | 939,052 | 1,060.150709 | 53481594 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 368 | 936,384 | 0.000013 | 53481594 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 929,082 | 72.525608 | 53481594 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 925,286 | 2,279.786354 | 53481594 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 916,700 | 1,271,961.163077 | 53481594 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 880,070 | 0.044939 | 53481594 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 869,527 | 0.000554 | 53481594 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 841,011 | 3,611.587591 | 53481594 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4615 | 818,921 | 20.143079 | 53481594 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 789,351 | 0.055774 | 53481594 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 768,336 | 0.799140 | 53481594 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 731,047 | 0.582585 | 53481594 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 719,251 | 0.000257 | 53481594 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 704,720 | 4,879,466.432812 | 53481594 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 669,199 | 0.000008 | 53481594 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 661,929 | 147,654.322779 | 53481594 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 652,534 | 0.535817 | 53481594 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 651,155 | 2.364339 | 53481594 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2135 | 640,889 | 554,055.679799 | 53481594 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 608,038 | 0.914716 | 53481594 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 582,534 | 0.086162 | 53481594 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 560,117 | 0.038087 | 53481594 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 193 ; routes examinées : 3749990 ; candidats optimisés : 11302 ; net attendu > 0 : 0 ; dernier cycle 296.8 ms
- Rejets (moteur) : {'spread_below_threshold': 3695380, 'liquidity_below_min': 43045, 'negative_expected_net': 11302, 'borrow_bound_too_small': 192}
- Enregistrements de la session : 11302 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 11302} ; motifs de rejet : {'negative_expected_net': 11302}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53481570 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 6.046525 USDC | 0.003951 USDC | 0.000000 USDC | 0.004881 USDC | -0.0009 | -1.54 |
| 53481572 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.004118 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0025 | -2.96 |
| 53481572 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 9.184218 USDC | 0.003895 USDC | 0.000000 USDC | 0.006665 USDC | -0.0025 | -3.02 |
| 53481572 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.003835 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0027 | -3.33 |
| 53481572 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 8.581004 USDC | 0.003761 USDC | 0.000000 USDC | 0.006665 USDC | -0.0027 | -3.38 |
| 53481572 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.004085 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0027 | -3.16 |
| 53481572 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 8.939790 USDC | 0.003737 USDC | 0.000000 USDC | 0.006665 USDC | -0.0027 | -3.28 |
| 53481577 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 8.864997 USDC | 0.001993 USDC | 0.000000 USDC | 0.005138 USDC | -0.0029 | -3.55 |
| 53481512 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 17.615644 USDC | 0.001767 USDC | 0.000000 USDC | 0.005086 USDC | -0.0031 | -1.88 |
| 53481512 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.007842 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -1.87 |

## Fiabilité et décision
- Observations ghost : 4940 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
