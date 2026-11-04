# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T07:20:43+00:00 ; durée 73.62 min ; blocs 53491535 → 53493747 (2198 vus)

## Connexion
- Requêtes RPC : 24906 ; erreurs : 0 ; latence p50/p95 : 252.0/1,338.1 ms
- Rafraîchissements d'état : 2199 ; âge des données au dernier bloc : 1.29 s ; changements de frais LP observés (pools à frais dynamiques) : 3411
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1342 ; cycles déclenchés par événement : 180 ; avance médiane sur le rafraîchissement multicall : 611 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,294.79 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 284 jetons, 19492 routes
- Par DEX : uniswap_v3 141, aerodrome_slipstream 106, aerodrome 204, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3704 (énumérés 307, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2296.568203, 'cbBTC': 77781.37292, 'AERO': 0.62987}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,403,741 | 2,294.791004 | 53493747 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,820,924 | 0.029458 | 53493747 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,252,968 | 0.029470 | 53493747 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,149,068 | 0.000013 | 53493747 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,070,716 | 2,297.476460 | 53493747 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,957,285 | 97.362267 | 53493747 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,609,053 | 0.001558 | 53493747 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,382,117 | 1.575021 | 53493747 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,823,619 | 0.029454 | 53493747 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,199,235 | 2,298.405247 | 53493747 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,098,388 | 0.999894 | 53493747 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 579 | 3,879,567 | 2,298.487356 | 53493747 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,449,966 | 41,406.867167 | 53493747 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,693,837 | 0.029479 | 53493747 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2766 | 2,183,367 | 97.387242 | 53493747 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,160,688 | 1,143,593.095050 | 53493747 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,819,058 | 0.000013 | 53493747 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,726,733 | 0.017621 | 53493747 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,684,797 | 0.006760 | 53493747 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,683,420 | 0.000000 | 53493747 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,623,837 | 0.000013 | 53493747 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,568,207 | 433.974131 | 53493747 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,552,822 | 1.432992 | 53493747 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,551,299 | 0.000013 | 53493747 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,067 | 0.818342 | 53493747 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,435,187 | 3,613.857664 | 53493747 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,360,762 | 2,297.668474 | 53493747 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,342,575 | 2,299.173001 | 53493747 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,341,961 | 2,295.020411 | 53493747 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,307,078 | 14,744.582167 | 53493747 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,309 | 72.425481 | 53493747 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,126,658 | 37,096,759.634312 | 53493747 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,055,456 | 553,879.321853 | 53493747 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,038,191 | 0.000000 | 53493747 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,031,368 | 22,201,054.916258 | 53493747 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,003,347 | 18.771407 | 53493747 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 992,595 | 97.947624 | 53493747 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 964,627 | 1,041.581465 | 53493747 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 962,685 | 86,683.855142 | 53493747 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 945,054 | 0.000013 | 53493747 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/WELL | 10000 | 930,720 | 1,268,138.692297 | 53493747 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 929,988 | 2,279.828359 | 53493747 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 926,579 | 72.918071 | 53493747 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 915,190 | 0.042373 | 53493747 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 878,815 | 0.000550 | 53493747 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 848,936 | 3,625.917024 | 53493747 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4535 | 824,094 | 19.962435 | 53493747 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 792,794 | 0.056286 | 53493747 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 778,914 | 0.799140 | 53493747 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 738,927 | 0.591150 | 53493747 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 729,153 | 0.000257 | 53493747 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 712,192 | 4,910,083.926225 | 53493747 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 676,381 | 0.000008 | 53493747 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 671,682 | 147,400.548853 | 53493747 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 652,870 | 0.536249 | 53493747 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 647,322 | 549,364.789571 | 53493747 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 643,875 | 2.453046 | 53493747 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 616,632 | 0.914056 | 53493747 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 604,625 | 0.091092 | 53493747 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 564,659 | 0.038552 | 53493747 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 2378 ; routes examinées : 46351976 ; candidats optimisés : 148792 ; net attendu > 0 : 4 ; dernier cycle 380.6 ms
- Rejets (moteur) : {'spread_below_threshold': 45578844, 'liquidity_below_min': 621918, 'negative_expected_net': 148788, 'borrow_bound_too_small': 2377, 'cycle_budget_exhausted': 45}
- Enregistrements de la session : 148792 ; net attendu > 0 : 4 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 148792} ; motifs de rejet : {'below_safety_margin': 4, 'negative_expected_net': 148788, 'p_lower_below_threshold': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53492556 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.020021 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0003 €) | — | 0.08 | 0.045 (n=204) | REJECTED | below_safety_margin(159445314040<4004255597769), p_lower_below_threshold(0.04<0.75) |
| 53492556 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 45.295213 USDC | 0.005510 USDC | 0.000000 USDC | 0.005147 USDC | 0.000363 USDC (0.0003 €) | — | 0.08 | 0.045 (n=204) | REJECTED | below_safety_margin(363<9059), p_lower_below_threshold(0.04<0.75) |
| 53493609 | USDC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 1.372889 USDC | 0.001162 USDC | 0.000000 USDC | 0.001154 USDC | 0.000008 USDC (0.0000 €) | — | 0.06 | 0.183 (n=877) | REJECTED | below_safety_margin(8<274), p_lower_below_threshold(0.18<0.75) |
| 53493609 | USDC→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1.372889 USDC | 0.001162 USDC | 0.000000 USDC | 0.001154 USDC | 0.000008 USDC (0.0000 €) | — | 0.06 | 0.183 (n=877) | REJECTED | below_safety_margin(8<274), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 5043 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
