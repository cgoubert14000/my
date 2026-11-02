# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T18:45:42+00:00 ; durée 241.52 min ; blocs 53420649 → 53427892 (7099 vus)

## Connexion
- Requêtes RPC : 84989 ; erreurs : 35 ; latence p50/p95 : 77.1/1,062.5 ms
- Rafraîchissements d'état : 7099 ; âge des données au dernier bloc : 2.55 s ; changements de frais LP observés (pools à frais dynamiques) : 12561
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 105019 ; cycles déclenchés par événement : 8732 ; avance médiane sur le rafraîchissement multicall : 360 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,253.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 286 jetons, 18656 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 30 (quarantaine 1), uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 310, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2287.70349, 'cbBTC': 77760.832568, 'AERO': 0.623017}
- Pools en quarantaine : 1 — pancakeswap_v3:USDC/PLAY@0xf1CaCd: simulation failed ×5 (model/chain mismatch) — until block 53428107

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,213,396 | 2,253.032467 | 53427891 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,184,481 | 0.029257 | 53427891 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,093,192 | 0.029302 | 53427891 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,017,446 | 0.000013 | 53427891 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,857,170 | 2,247.800273 | 53427891 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,510,439 | 106.173146 | 53427891 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,544,751 | 0.001564 | 53427891 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,389,198 | 1.653634 | 53427891 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,761,415 | 0.029260 | 53427891 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,052,282 | 2,248.699571 | 53427892 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,051,181 | 0.999919 | 53427891 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 609 | 3,930,535 | 2,248.585210 | 53427891 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,499,107 | 38,800.407180 | 53427891 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,633,577 | 0.029289 | 53427891 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,259,256 | 106.149263 | 53427891 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,127,485 | 1,137,028.058993 | 53427891 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 2,075,835 | 0.000013 | 53427891 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,728,021 | 0.017614 | 53427891 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,655,765 | 0.000000 | 53427891 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,607,130 | 0.000013 | 53427891 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,566,359 | 0.000013 | 53427891 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,941 | 1.450900 | 53427891 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,527,756 | 444.832935 | 53427891 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,496,847 | 2,253.149101 | 53427891 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,556 | 0.822512 | 53427891 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,391,070 | 3,716.039962 | 53427891 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,349,400 | 2,253.114332 | 53427891 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,309,551 | 2,247.804349 | 53427891 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,300,148 | 0.005055 | 53427891 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,274,039 | 15,193.265445 | 53427891 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 1,260,398 | 0.000013 | 53427891 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,168,911 | 71.117634 | 53427891 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,093,451 | 38,405,256.857330 | 53427891 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,048,895 | 536,272.731739 | 53427891 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,008,599 | 22,794,286.635066 | 53427891 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 997,201 | 0.000000 | 53427891 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 978,872 | 20.165558 | 53427891 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 968,603 | 82,540.342772 | 53427891 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 933,465 | 1,215,267.237266 | 53427891 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 921,594 | 2,265.210012 | 53427891 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 916,245 | 74.571528 | 53427891 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 911,159 | 1,040.660578 | 53427891 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 899,305 | 105.988988 | 53427891 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | uXRP/WETH | 3000 | 859,573 | 0.000546 | 53427891 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 855,734 | 0.047162 | 53427891 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 829,221 | 3,698.737846 | 53427891 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 820,750 | 20.067436 | 53427891 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,462 | 0.056692 | 53427891 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 763,432 | 0.801881 | 53427891 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 717,824 | 0.000258 | 53427891 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 703,693 | 0.576686 | 53427891 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,603 | 4,974,167.530936 | 53427891 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 669,827 | 0.568839 | 53427891 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 668,643 | 143,317.843696 | 53427891 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 666,546 | 0.000008 | 53427891 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 653,265 | 2.338291 | 53427891 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 646,275 | 540,748.241312 | 53427891 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 605,057 | 0.915126 | 53427891 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 588,579 | 0.087523 | 53427891 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 555,864 | 0.037711 | 53427891 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 15830 ; routes examinées : 295324480 ; candidats optimisés : 1244123 ; net attendu > 0 : 2417 ; dernier cycle 236.0 ms
- Rejets (moteur) : {'spread_below_threshold': 288553395, 'liquidity_below_min': 4642923, 'negative_expected_net': 1241706, 'pool_quarantined': 785422, 'unquotable': 80018, 'borrow_bound_too_small': 15824, 'cycle_budget_exhausted': 2775}
- Enregistrements de la session : 1244123 ; net attendu > 0 : 2417 ; simulés (eth_call de la vraie tx) : 144 (ok 58, échec 86) ; étiquettes ghost N+1 : 22/108 positives
- Décisions : {'REJECTED': 1244123} ; motifs de rejet : {'below_safety_margin': 1945, 'negative_expected_net': 1241706, 'p_lower_below_threshold': 2169, 'price_impact': 398, 'reliability_not_demonstrated': 248, 'sim_below_estimate': 9, 'simulated_net_nonpositive': 5, 'simulation_failed': 86, 'stale_data': 69}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53421255 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.022920 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2227 €) | — | 1.36 | 0.015 (n=19) | REJECTED | below_safety_margin(311<458), reliability_not_demonstrated |
| 53421255 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.806328 WETH | 0.000109 WETH | 0.000000 WETH | 0.000003 WETH | 0.000106 WETH (0.2224 €) | — | 1.31 | 0.015 (n=19) | REJECTED | below_safety_margin(105730486160810<161265691126913), reliability_not_demonstrated |
| 53421255 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,798.869495 USDC | 0.248913 USDC | 0.000000 USDC | 0.007636 USDC | 0.241277 USDC (0.2220 €) | — | 1.34 | 0.015 (n=19) | REJECTED | below_safety_margin(241277<359773), reliability_not_demonstrated |
| 53427335 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.693160 WETH | 0.000108 WETH | 0.000000 WETH | 0.000003 WETH | 0.000105 WETH (0.2182 €) | — | 1.51 | 0.187 (n=831) | REJECTED | below_safety_margin(105006854700363<138632093252889), p_lower_below_threshold(0.19<0.75) |
| 53427335 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.021185 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2180 €) | — | 1.45 | 0.187 (n=831) | REJECTED | below_safety_margin(307<423), p_lower_below_threshold(0.19<0.75) |
| 53427335 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,552.652163 USDC | 0.243304 USDC | 0.000000 USDC | 0.007148 USDC | 0.236156 USDC (0.2173 €) | — | 1.52 | 0.187 (n=831) | REJECTED | below_safety_margin(236156<310530), p_lower_below_threshold(0.19<0.75) |
| 53423107 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,463.190229 USDC | 0.236997 USDC | 0.000000 USDC | 0.007581 USDC | 0.229416 USDC (0.2111 €) | — | 1.57 | 0.015 (n=19) | REJECTED | below_safety_margin(229416<292638), reliability_not_demonstrated |
| 53423107 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.018050 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2108 €) | — | 1.64 | 0.015 (n=19) | REJECTED | below_safety_margin(296<360), reliability_not_demonstrated |
| 53423107 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.623407 WETH | 0.000104 WETH | 0.000000 WETH | 0.000003 WETH | 0.000101 WETH (0.2108 €) | — | 1.62 | 0.015 (n=19) | REJECTED | below_safety_margin(100913025911152<124681318574639), reliability_not_demonstrated |
| 53427335 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.017689 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1903 €) | — | 1.52 | 0.041 (n=20) | REJECTED | below_safety_margin(268<353), reliability_not_demonstrated |
| 53427335 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.604517 WETH | 0.000095 WETH | 0.000000 WETH | 0.000003 WETH | 0.000092 WETH (0.1902 €) | — | 1.51 | 0.041 (n=20) | REJECTED | below_safety_margin(91526851909524<120903357080830), reliability_not_demonstrated |
| 53427335 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,406.773967 USDC | 0.213214 USDC | 0.000000 USDC | 0.007148 USDC | 0.206066 USDC (0.1896 €) | — | 1.46 | 0.041 (n=20) | REJECTED | below_safety_margin(206066<281354), reliability_not_demonstrated |
| 53420906 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.015164 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1868 €) | — | 1.72 | 0.039 (n=170) | REJECTED | below_safety_margin(261<303), p_lower_below_threshold(0.04<0.75) |
| 53420906 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 1,239.328545 USDC | 0.207693 USDC | 0.000000 USDC | 0.005181 USDC | 0.202512 USDC (0.1863 €) | — | 1.63 | 0.039 (n=170) | REJECTED | below_safety_margin(202512<247865), p_lower_below_threshold(0.04<0.75) |
| 53423107 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.558889 WETH | 0.000083 WETH | 0.000000 WETH | 0.000003 WETH | 0.000080 WETH (0.1670 €) | — | 1.43 | 0.186 (n=817) | REJECTED | below_safety_margin(79963547611790<111777767764553), p_lower_below_threshold(0.19<0.75) |
| 53423107 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.016032 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1667 €) | — | 1.46 | 0.186 (n=817) | REJECTED | below_safety_margin(234<320), p_lower_below_threshold(0.19<0.75) |
| 53423107 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,242.865749 USDC | 0.188376 USDC | 0.000000 USDC | 0.007237 USDC | 0.181139 USDC (0.1666 €) | — | 1.46 | 0.186 (n=817) | REJECTED | below_safety_margin(181139<248573), p_lower_below_threshold(0.19<0.75) |
| 53426301 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,333.888851 USDC | 0.154265 USDC | 0.000000 USDC | 0.005441 USDC | 0.148824 USDC (0.1369 €) | — | 1.12 | 0.037 (n=178) | REJECTED | below_safety_margin(148824<266777), p_lower_below_threshold(0.04<0.75) |
| 53426302 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,333.888851 USDC | 0.154265 USDC | 0.000000 USDC | 0.005441 USDC | 0.148824 USDC (0.1369 €) | — | 1.12 | 0.037 (n=178) | REJECTED | below_safety_margin(148824<266777), p_lower_below_threshold(0.04<0.75) |
| 53426301 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.592483 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000066 WETH (0.1368 €) | — | 1.12 | 0.037 (n=178) | REJECTED | below_safety_margin(66099892856396<118496688310974), p_lower_below_threshold(0.04<0.75) |
| 53426302 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.592483 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000066 WETH (0.1368 €) | — | 1.12 | 0.037 (n=178) | REJECTED | below_safety_margin(66099892856396<118496688310974), p_lower_below_threshold(0.04<0.75) |
| 53423107 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,399.750949 USDC | 0.143343 USDC | 0.000000 USDC | 0.005499 USDC | 0.137844 USDC (0.1268 €) | — | 0.98 | 0.038 (n=176) | REJECTED | below_safety_margin(137844<279950), p_lower_below_threshold(0.04<0.75) |
| 53423107 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.016285 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1261 €) | — | 1.09 | 0.038 (n=176) | REJECTED | below_safety_margin(177<325), p_lower_below_threshold(0.04<0.75) |
| 53421893 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 610.097918 USDC | 0.130437 USDC | 0.000000 USDC | 0.005187 USDC | 0.125250 USDC (0.1152 €) | — | 2.05 | 0.039 (n=173) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53421893 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.267037 WETH | 0.000057 WETH | 0.000000 WETH | 0.000002 WETH | 0.000055 WETH (0.1152 €) | — | 2.05 | 0.039 (n=173) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 4749 ; taux observé 0.171 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
