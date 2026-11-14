# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-14T13:53:09+00:00 ; durée 27.45 min ; blocs 57361800 → 57370029 (1665 vus)

## Connexion
- Requêtes RPC : 17766 ; erreurs : 0 ; latence p50/p95 : 367.5/1,379.3 ms
- Rafraîchissements d'état : 1665 ; âge des données au dernier bloc : 8.3 s ; changements de frais LP observés (pools à frais dynamiques) : 929
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2228 ; cycles déclenchés par événement : 794 ; avance médiane sur le rafraîchissement multicall : 296 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,890.15 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 441 pools, 257 jetons, 13788 routes
- Par DEX : uniswap_v3 130, aerodrome_slipstream 91, aerodrome 181, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 152 (rejetés 2) → 557 jetons ; pools candidats 3597 (énumérés 271, par paires 0), mesurés 444, sous le plancher de 10000.0 $ : 3 → gardés 441 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1887.935902, 'cbBTC': 66533.577566, 'AERO': 0.448525}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 122,725,576 | 1,890.147586 | 57370052 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 13,483,772 | 0.028319 | 57370052 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,049,806 | 0.028363 | 57370052 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,827,130 | 0.000015 | 57370052 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,620,882 | 1,889.448267 | 57370052 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,310,022 | 104.506136 | 57370052 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,209,181 | 0.028320 | 57370052 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,090,733 | 1,889.064530 | 57370052 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | USDC/AERO | 3000 | 3,785,092 | 2.231484 | 57370052 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,514,646 | 0.998788 | 57370052 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,826,515 | 41,849.798855 | 57370052 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 262 | 2,566,548 | 1,888.687426 | 57370052 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,995,028 | 0.028358 | 57370052 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,783,457 | 1,138,576.220041 | 57370052 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,707,044 | 0.017774 | 57370052 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 1,517,379 | 0.000015 | 57370052 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,509,343 | 0.000015 | 57370052 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,467,828 | 0.000000 | 57370052 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,762 | 0.839134 | 57370052 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,373,248 | 0.006494 | 57370052 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,283,584 | 442.067219 | 57370052 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,243,489 | 0.000015 | 57370052 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,094,812 | 15,592.649247 | 57370052 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,081,658 | 4,219.291837 | 57370052 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,063,335 | 1,893.408764 | 57370052 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,061,991 | 86.158308 | 57370052 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,012,880 | 1,889.879855 | 57370052 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | WETH/USDC | 3000 | 1,011,892 | 1,890.457611 | 57370052 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 975,898 | 20.356571 | 57370052 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/doginme | 10000 | 967,700 | 32,902,379.748126 | 57370052 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 953,797 | 104.722603 | 57370052 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 873,718 | 545,670.339691 | 57370052 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/MORPHO | 3000 | 856,969 | 999.374672 | 57370052 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 834,243 | 0.055240 | 57370052 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 830,895 | 23,126,308.060026 | 57370052 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 827,948 | 0.001482 | 57370052 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | DRB/WETH | 10000 | 745,645 | 0.000000 | 57370052 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 742,742 | 85.261803 | 57370052 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 732,631 | 0.047779 | 57370052 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/USDC | 10000 | 730,787 | 1,898.055716 | 57370052 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 709,210 | 24.759978 | 57370052 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 640,786 | 0.800795 | 57370052 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 620,207 | 0.484832 | 57370052 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/AERO | 10000 | 604,332 | 4,201.743145 | 57370052 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | TIG/USDC | 10000 | 596,366 | 0.447567 | 57370052 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 595,317 | 4,783,628.948483 | 57370052 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | WETH/USDC | 100 | 593,083 | 1,889.147032 | 57370052 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v2 | WETH/NPC | 3000 | 566,110 | 141,464.578053 | 57370052 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 538,465 | 548,301.673035 | 57370052 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | VIRTUAL/WETH | 10000 | 531,103 | 0.000259 | 57370052 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 526,470 | 1.375166 | 57370052 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | FLOCK/USDC | 3000 | 516,348 | 0.033505 | 57370052 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 479,991 | 0.000007 | 57370052 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 457,265 | 999.486846 | 57370052 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 450,934 | 0.064411 | 57370052 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 11 | 446,864 | 1.001016 | 57370052 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 428,932 | 0.525678 | 57370052 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 402,602 | 24.944596 | 57370052 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 402,560 | 886,970.112182 | 57370052 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | WETH/msETH (stable) | 500 | 397,510 | 2.350456 | 57370052 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |

## Recherche d'opportunités
- Cycles : 2458 ; routes examinées : 33890904 ; candidats optimisés : 9555 ; net attendu > 0 : 0 ; dernier cycle 0.0 ms
- Rejets (moteur) : {'spread_below_threshold': 33099832, 'liquidity_below_min': 568735, 'negative_expected_net': 9555, 'borrow_bound_too_small': 2458}
- Enregistrements de la session : 0 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {} ; motifs de rejet : {}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

## Fiabilité et décision
- Observations ghost : 8573 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
