# 06 — Portefeuille dédié, signer isolé et politique d'autorisation

## Principes (non négociables dans le code)

1. **Le moteur de stratégie ne possède aucune clé.** Il ne connaît qu'une URL locale (`ARB_SIGNER_URL`) et un jeton
   partagé. La clé vit dans un **processus séparé** (`arbbot signer`) qui charge un keystore chiffré et ne la sort
   jamais de sa mémoire.
2. **Le signer applique lui-même la politique** (`authorization.json`) : il refuse tout ce qui n'est pas
   `executeArbitrage(...)` vers le contrat exécuteur autorisé, avec `value = 0`, un `minProfit > 0`, un gaz ≤ plafond,
   un prix du gaz ≤ plafond, dans la fenêtre de validité, et il tient **sa propre comptabilité** (nombre de tx, budget
   gaz cumulé) indépendante de celle du moteur. Un moteur compromis ou bogué ne peut donc pas dépenser plus que la
   politique.
3. **La politique est gelée pour le moteur** : `AuthorizationPolicy` est un modèle immuable chargé depuis un fichier
   que le moteur ouvre en lecture seule ; les clés de l'auto-correction (`TunableParams.ALLOWED_KEYS`) ne contiennent
   aucun paramètre financier (test `test_self_correction_cannot_touch_financial_controls`). Toute modification de la
   politique change son empreinte, affichée dans l'interface et dans chaque rapport.
4. **Portefeuille dédié** : créé pour ce bot, alimenté uniquement du budget de gaz que vous acceptez de perdre
   (10–20 €). Il n'a jamais besoin de détenir le montant emprunté.
5. **Jamais de seed phrase ni de clé en clair** : ni dans `.env`, ni dans le dépôt, ni dans le chat. La variable
   `ARB_SIGNER_PRIVATE_KEY` n'est acceptée que si `ARB_SIGNER_ALLOW_RAW_KEY=1` **et** ne doit servir que sur le devnet.

## Mise en place

```powershell
.\.venv\Scripts\Activate.ps1
arbbot make-keystore                       # crée keystores\executor.json (ignoré par git) ; mot de passe ≥ 10 caractères, saisi au clavier
```

La commande affiche l'adresse du nouveau portefeuille. **Transférez-y uniquement le budget de gaz** (ex. 0,004 ETH sur
Base ≈ 10 € — vérifiez le cours) depuis votre portefeuille habituel ou un échange.

Politique :

```powershell
arbbot policy-example                      # authorization.example.json
Copy-Item authorization.example.json authorization.json
notepad authorization.json
arbbot policy-check
```

Champs à renseigner (tout le reste peut rester tel quel au début) :

| Champ | Sens | Valeur conseillée pour un premier test |
|---|---|---|
| `enabled` | interrupteur général | `false` tant que `docs/07` n'est pas terminé, puis `true` |
| `wallet_address` | adresse du portefeuille dédié (doit correspondre au keystore) | sortie de `make-keystore` |
| `chain_ids` | réseaux autorisés | `[8453]` |
| `executor_contract` | **votre** déploiement de `FlashArbExecutor` | adresse donnée par le script de déploiement |
| `allowed_flash_providers` / `allowed_dexes` / `allowed_tokens` | listes blanches | `MORPHO`, `AAVE_V3` ; `uniswap_v3`, `aerodrome`, `uniswap_v2`, `sushiswap_v2`, `pancakeswap_v3` ; `WETH`, `USDC` |
| `max_total_budget_native` | gaz total maximal dépensable (ETH) sur toute la validité | `0.004` |
| `max_gas_per_tx_native` | coût gaz max par tx | `0.0004` |
| `max_gas_limit` / `max_fee_per_gas_gwei` | plafonds techniques | `900000` / `0.2` |
| `max_transactions` | nombre max de tx signées | `10` |
| `min_net_profit_native` | profit net minimum exigé par tx | `0.0005` (≈ 1 €) |
| `max_slippage_bps` | tolérance par saut appliquée au `minAmountOut` on-chain | `30` |
| `max_cumulative_loss_native` | perte cumulée (gaz des échecs) qui suspend | `0.003` |
| `max_consecutive_failures` | échecs consécutifs qui suspendent | `2` |
| `min_success_probability` | borne inférieure requise | `0.75` (ne pas baisser) |
| `valid_from` / `valid_until` | fenêtre Unix (secondes) ; `0` = non définie → la politique est **invalide** tant que `valid_until` n'est pas fixé | une fenêtre de quelques heures |

Le signer :

```powershell
# Terminal dédié, laissé ouvert pendant toute la session réelle
.\.venv\Scripts\Activate.ps1
$env:ARB_SIGNER_KEYSTORE = "keystores\executor.json"
$env:ARB_SIGNER_TOKEN    = "<jeton aléatoire long : python -c 'import secrets;print(secrets.token_hex(32))'>"
$env:ARB_POLICY_PATH     = "authorization.json"
arbbot signer                               # demande le mot de passe du keystore, écoute sur 127.0.0.1:8787
```

Le moteur (autre terminal) reçoit le **même jeton** via `ARB_SIGNER_TOKEN` (dans `.env` ou l'environnement). Il
vérifie au démarrage que l'adresse annoncée par le signer est bien `wallet_address` de la politique.

## Ce que le signer refuse (tests `tests/test_policy_risk_signer.py`, 26 cas)

mauvais contrat de destination, `value ≠ 0`, sélecteur autre que `executeArbitrage`, `minProfit = 0`, gaz ou prix du
gaz au-dessus des plafonds, chain id non autorisé, politique expirée ou pas encore valide, dépassement du nombre de
transactions ou du budget cumulé, portefeuille différent de celui de la politique, deadline dépassée, jeton d'API
invalide.

## Rotation / révocation

* Révoquer : fermer le signer, mettre `enabled=false`, et/ou appeler `pause()` sur le contrat.
* Changer de portefeuille : nouveau `make-keystore`, nouvelle adresse dans la politique, `setExecutor` sur le
  contrat (propriétaire), retrait des fonds de l'ancien.
* Les retraits du contrat (`withdraw`) ne sont possibles que par le propriétaire ; l'exécuteur ne peut que lancer des
  arbitrages dont le profit reste dans le contrat.
