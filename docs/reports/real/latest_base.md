# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T09:54:57+00:00 ; durée 79.55 min ; blocs 53818717 → 53842570 (3863 vus)

## Connexion
- Requêtes RPC : 58281 ; erreurs : 3 ; latence p50/p95 : 251.1/1,005.4 ms
- Rafraîchissements d'état : 3863 ; âge des données au dernier bloc : 6.82 s ; changements de frais LP observés (pools à frais dynamiques) : 2428
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3468 ; cycles déclenchés par événement : 1604 ; avance médiane sur le rafraîchissement multicall : 456 ms
- Gaz : base fee 0.005003 gwei ; prix ETH (pool le plus profond) : 2,238.04 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 484 pools, 281 jetons, 17914 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 103, aerodrome 201, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3751 (énumérés 303, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 3 → gardés 484 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.035754, 'cbBTC': 75513.528915, 'AERO': 0.590274}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,236,249 | 2,238.042423 | 53842590 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,663,155 | 0.029419 | 53842590 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,395,636 | 0.000013 | 53842590 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,142,226 | 0.029418 | 53842590 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,005,103 | 2,235.164013 | 53842590 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,391,594 | 107.134569 | 53842590 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,436,007 | 0.001549 | 53842590 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,055,203 | 1.677326 | 53842590 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,709,895 | 0.029407 | 53842590 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,104,408 | 2,234.380684 | 53842590 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,009,982 | 0.998447 | 53842590 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,306,329 | 42,880.485448 | 53842590 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,208,191 | 2,234.383917 | 53842590 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,561,035 | 0.029434 | 53842590 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,081,225 | 1,172,181.068675 | 53842590 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,806,081 | 0.007367 | 53842590 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,740,607 | 0.000013 | 53842590 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,662,295 | 0.000013 | 53842590 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,646,269 | 0.016579 | 53842590 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,641,807 | 0.000000 | 53842590 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,161 | 1.444757 | 53842590 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,533,480 | 0.000013 | 53842590 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,522,492 | 441.587815 | 53842590 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,908 | 0.818149 | 53842590 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,371,637 | 3,757.422138 | 53842590 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,325,686 | 2,237.814625 | 53842590 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,324,198 | 2,239.020572 | 53842590 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,267,180 | 14,995.801261 | 53842590 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,175,321 | 2,235.274125 | 53842590 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,886 | 76.929838 | 53842590 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,095,401 | 37,376,035.646740 | 53842590 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,046,924 | 107.682094 | 53842590 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,022,412 | 563,507.700249 | 53842590 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,009,711 | 0.000000 | 53842590 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,006,428 | 22,469,739.284491 | 53842590 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 986,842 | 19.712868 | 53842590 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 936,606 | 2,225.328831 | 53842590 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 934,405 | 1,070.214514 | 53842590 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 926,973 | 0.000013 | 53842590 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 926,528 | 73.041380 | 53842590 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 863,512 | 102,470.103624 | 53842590 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 842,827 | 0.000532 | 53842590 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 811,023 | 20.482758 | 53842590 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | USDC/VVV | 3000 | 810,829 | 0.047950 | 53842590 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,774 | 0.056711 | 53842590 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 792,807 | 3,782.541679 | 53842590 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 759,247 | 0.799699 | 53842590 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 720,788 | 0.573089 | 53842590 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 693,528 | 4,927,567.775310 | 53842590 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 686,422 | 0.000255 | 53842590 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 661,168 | 144,834.028132 | 53842590 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 655,951 | 0.540495 | 53842590 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 649,203 | 0.000008 | 53842590 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 626,212 | 559,453.876174 | 53842590 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 600,005 | 0.914223 | 53842590 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 589,846 | 2.462288 | 53842590 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 559,905 | 0.037986 | 53842590 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 530,326 | 871,287.001969 | 53842590 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 526,555 | 0.078989 | 53842590 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 523,016 | 1,070.546540 | 53842590 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 5466 ; routes examinées : 97917924 ; candidats optimisés : 288108 ; net attendu > 0 : 47 ; dernier cycle 210.4 ms
- Rejets (moteur) : {'spread_below_threshold': 96529087, 'liquidity_below_min': 1095263, 'negative_expected_net': 288061, 'borrow_bound_too_small': 5466}
- Enregistrements de la session : 288108 ; net attendu > 0 : 47 ; simulés (eth_call de la vraie tx) : 7 (ok 2, échec 5) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 288108} ; motifs de rejet : {'below_safety_margin': 40, 'negative_expected_net': 288061, 'p_lower_below_threshold': 41, 'reliability_not_demonstrated': 6, 'simulation_failed': 5, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53823058 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 49.007869 USDC | 0.030104 USDC | 0.000000 USDC | 0.005012 USDC | 0.025092 USDC (0.0231 €) | 0.025092 USDC | 5.12 | 0.028 (n=300) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53823641 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 47.715028 USDC | 0.028656 USDC | 0.000000 USDC | 0.005013 USDC | 0.023643 USDC (0.0218 €) | — | 4.96 | 0.028 (n=301) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53838404 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 264.555975 USDC | 0.024400 USDC | 0.000000 USDC | 0.005038 USDC | 0.019362 USDC (0.0178 €) | — | 0.73 | 0.054 (n=80) | REJECTED | below_safety_margin(19362<52911), p_lower_below_threshold(0.05<0.75) |
| 53838404 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 264.555975 USDC | 0.024400 USDC | 0.000000 USDC | 0.005038 USDC | 0.019362 USDC (0.0178 €) | — | 0.73 | 0.054 (n=80) | REJECTED | below_safety_margin(19362<52911), p_lower_below_threshold(0.05<0.75) |
| 53838404 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 223.293117 USDC | 0.018971 USDC | 0.000000 USDC | 0.005378 USDC | 0.013593 USDC (0.0125 €) | — | 0.61 | 0.054 (n=80) | REJECTED | below_safety_margin(13593<44658), p_lower_below_threshold(0.05<0.75) |
| 53838404 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 223.293117 USDC | 0.018971 USDC | 0.000000 USDC | 0.005378 USDC | 0.013593 USDC (0.0125 €) | — | 0.61 | 0.054 (n=80) | REJECTED | below_safety_margin(13593<44658), p_lower_below_threshold(0.05<0.75) |
| 53840843 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 36.991359 USDC | 0.017072 USDC | 0.000000 USDC | 0.005034 USDC | 0.012038 USDC (0.0111 €) | — | 3.25 | 0.027 (n=302) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53838629 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003749 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0091 €) | — | 0.35 | 0.029 (n=28) | REJECTED | below_safety_margin(13<74), reliability_not_demonstrated |
| 53838629 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003749 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0091 €) | — | 0.35 | 0.029 (n=28) | REJECTED | below_safety_margin(13<74), reliability_not_demonstrated |
| 53838629 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.145673 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0090 €) | — | 0.30 | 0.029 (n=28) | REJECTED | below_safety_margin(4365843303114<29134531427720), reliability_not_demonstrated |
| 53838629 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.145673 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0090 €) | — | 0.30 | 0.029 (n=28) | REJECTED | below_safety_margin(4365843303114<29134531427720), reliability_not_demonstrated |
| 53838629 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 324.978221 USDC | 0.016455 USDC | 0.000000 USDC | 0.006742 USDC | 0.009713 USDC (0.0089 €) | — | 0.30 | 0.029 (n=28) | REJECTED | below_safety_margin(9713<64995), reliability_not_demonstrated |
| 53838629 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 324.978221 USDC | 0.016455 USDC | 0.000000 USDC | 0.006742 USDC | 0.009713 USDC (0.0089 €) | — | 0.30 | 0.029 (n=28) | REJECTED | below_safety_margin(9713<64995), reliability_not_demonstrated |
| 53838907 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 32.829338 USDC | 0.013202 USDC | 0.000000 USDC | 0.005038 USDC | 0.008164 USDC (0.0075 €) | — | 2.49 | 0.046 (n=235) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 53831928 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 32.441807 USDC | 0.012869 USDC | 0.000000 USDC | 0.005039 USDC | 0.007830 USDC (0.0072 €) | 0.007830 USDC | 2.41 | 0.046 (n=234) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 53831480 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 29.603942 USDC | 0.010814 USDC | 0.000000 USDC | 0.005038 USDC | 0.005776 USDC (0.0053 €) | — | 1.95 | 0.046 (n=234) | REJECTED | below_safety_margin(5776<5920), p_lower_below_threshold(0.05<0.75) |
| 53831481 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 29.603942 USDC | 0.010814 USDC | 0.000000 USDC | 0.005038 USDC | 0.005776 USDC (0.0053 €) | — | 1.95 | 0.046 (n=234) | REJECTED | below_safety_margin(5776<5920), p_lower_below_threshold(0.05<0.75) |
| 53838629 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.135189 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0052 €) | — | 0.19 | 0.169 (n=1024) | REJECTED | below_safety_margin(2532646321556<27037794443924), p_lower_below_threshold(0.17<0.75) |
| 53838629 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.135189 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0052 €) | — | 0.19 | 0.169 (n=1024) | REJECTED | below_safety_margin(2532646321556<27037794443924), p_lower_below_threshold(0.17<0.75) |
| 53832143 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 29.379544 USDC | 0.010641 USDC | 0.000000 USDC | 0.005039 USDC | 0.005602 USDC (0.0052 €) | — | 1.91 | 0.046 (n=235) | REJECTED | below_safety_margin(5602<5875), p_lower_below_threshold(0.05<0.75) |
| 53832143 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 29.379544 USDC | 0.010641 USDC | 0.000000 USDC | 0.005039 USDC | 0.005602 USDC (0.0052 €) | — | 1.91 | 0.046 (n=235) | REJECTED | below_safety_margin(5602<5875), p_lower_below_threshold(0.05<0.75) |
| 53838629 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 326.544032 USDC | 0.012332 USDC | 0.000000 USDC | 0.006742 USDC | 0.005590 USDC (0.0051 €) | — | 0.17 | 0.169 (n=1024) | REJECTED | below_safety_margin(5590<65308), p_lower_below_threshold(0.17<0.75) |
| 53838629 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 326.544032 USDC | 0.012332 USDC | 0.000000 USDC | 0.006742 USDC | 0.005590 USDC (0.0051 €) | — | 0.17 | 0.169 (n=1024) | REJECTED | below_safety_margin(5590<65308), p_lower_below_threshold(0.17<0.75) |
| 53838629 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.002861 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0049 €) | — | 0.24 | 0.169 (n=1024) | REJECTED | below_safety_margin(7<57), p_lower_below_threshold(0.17<0.75) |
| 53838629 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.002861 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0049 €) | — | 0.24 | 0.169 (n=1024) | REJECTED | below_safety_margin(7<57), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 5807 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
