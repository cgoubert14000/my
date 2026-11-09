# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T21:15:49+00:00 ; durée 3.08 min ; blocs 55341906 → 55342836 (141 vus)

## Connexion
- Requêtes RPC : 2119 ; erreurs : 0 ; latence p50/p95 : 339.0/1,219.0 ms
- Rafraîchissements d'état : 141 ; âge des données au dernier bloc : 7.28 s ; changements de frais LP observés (pools à frais dynamiques) : 109
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 94 ; cycles déclenchés par événement : 48 ; avance médiane sur le rafraîchissement multicall : 449 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,127.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 468 pools, 272 jetons, 17716 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 193, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3654 (énumérés 289, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 3 → gardés 468 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2127.766856, 'cbBTC': 74794.411024, 'AERO': 0.572023}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,784,534 | 2,127.766910 | 55342857 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,653,194 | 0.028420 | 55342857 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,321,769 | 0.000013 | 55342857 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,789,192 | 0.028437 | 55342857 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,480,379 | 2,125.744049 | 55342857 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,339,637 | 98.130473 | 55342857 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,933,749 | 0.028422 | 55342857 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,578,498 | 1.748181 | 55342857 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,009,897 | 2,126.399299 | 55342857 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,894,405 | 1.000033 | 55342857 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,106,959 | 43,892.698508 | 55342857 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,028,738 | 2,126.387206 | 55342857 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,348,952 | 0.028441 | 55342857 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,031,757 | 1,111,732.813378 | 55342857 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,706,723 | 0.000013 | 55342857 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,692,695 | 0.000013 | 55342857 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,583,146 | 0.015786 | 55342857 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,563,594 | 0.006563 | 55342857 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,562,252 | 0.000000 | 55342857 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,493,979 | 0.000013 | 55342857 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,481,281 | 1.407587 | 55342857 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,466,019 | 424.216542 | 55342857 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,949 | 0.821811 | 55342857 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,320,246 | 3,719.511342 | 55342857 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,293,210 | 2,130.632508 | 55342857 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,251,302 | 14,912.051908 | 55342857 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,417 | 2,130.837232 | 55342857 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,263 | 79.257048 | 55342857 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,102,797 | 2,125.764526 | 55342857 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,796 | 36,372,708.938556 | 55342857 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 989,321 | 98.507473 | 55342857 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 970,756 | 565,877.730937 | 55342857 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 964,993 | 0.046126 | 55342857 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,947 | 21.255866 | 55342857 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 938,467 | 0.001514 | 55342857 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 936,790 | 23,213,728.096903 | 55342857 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 928,979 | 0.000013 | 55342857 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 919,209 | 74.161721 | 55342857 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 909,813 | 1,032.686922 | 55342857 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 887,623 | 2,127.924155 | 55342857 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 887,405 | 0.000000 | 55342857 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 816,369 | 103,565.930578 | 55342857 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4600 | 774,233 | 21.902365 | 55342857 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 771,091 | 0.053079 | 55342857 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 746,117 | 3,692.738593 | 55342857 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 722,419 | 0.798411 | 55342857 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,289 | 0.550997 | 55342857 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 664,771 | 4,849,665.129233 | 55342857 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 647,922 | 0.527215 | 55342857 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 622,534 | 0.000008 | 55342857 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 616,166 | 150,883.061464 | 55342857 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 601,085 | 0.000258 | 55342857 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 594,335 | 569,519.491237 | 55342857 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,127 | 0.039223 | 55342857 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 514,860 | 1,033.255495 | 55342857 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/msETH (stable) | 500 | 498,158 | 2.400596 | 55342857 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/DRV | 3000 | 491,698 | 6,867.322545 | 55342857 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 471,809 | 0.067995 | 55342857 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/uSOL | 3000 | 469,938 | 24.679366 | 55342857 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 468,118 | 303.348820 | 55342857 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 188 ; routes examinées : 3330608 ; candidats optimisés : 8782 ; net attendu > 0 : 0 ; dernier cycle 84.1 ms
- Rejets (moteur) : {'spread_below_threshold': 3280280, 'liquidity_below_min': 41158, 'negative_expected_net': 8782, 'borrow_bound_too_small': 376, 'cycle_budget_exhausted': 12}
- Enregistrements de la session : 8782 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 8782} ; motifs de rejet : {'negative_expected_net': 8782}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 55342739 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.002328 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -7.39 |
| 55342740 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.002328 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -7.39 |
| 55342742 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.002328 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -7.39 |
| 55342741 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.002328 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -7.39 |
| 55342742 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.002328 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -7.39 |
| 55342740 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.002328 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -7.39 |
| 55342741 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.002328 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -7.39 |
| 55342739 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 4.879442 USDC | 0.001131 USDC | 0.000000 USDC | 0.004792 USDC | -0.0034 | -7.50 |
| 55342740 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 4.879442 USDC | 0.001131 USDC | 0.000000 USDC | 0.004792 USDC | -0.0034 | -7.50 |
| 55342741 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 4.879442 USDC | 0.001131 USDC | 0.000000 USDC | 0.004792 USDC | -0.0034 | -7.50 |

## Fiabilité et décision
- Observations ghost : 7101 ; taux observé 0.184 ; borne inférieure crédible (0.9) 0.179 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
