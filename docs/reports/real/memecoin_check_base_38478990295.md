# Bot memecoin — vérification impossible sur RPC public (base)

Généré le 2026-10-13T22:37:44Z. Les journaux historiques (`eth_getLogs` sur 1 j) ne sont pas servis par les points d'accès publics essayés (https://base.drpc.org) : `rpc failed after retries: ranges over 10000 blocks are not supported on free plan`.

Aucun chiffre n'est inventé à la place. Pour exécuter la mesure, fournir une URL RPC d'archive avec clé gratuite (Alchemy, Infura, QuickNode…) dans le secret GitHub `RPC_ARCHIVE_URL_BASE` (ou `--rpc URL` en local).
