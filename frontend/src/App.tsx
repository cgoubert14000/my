import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { api, CycleEvent, eur, openWs, Opportunity, pct, Reliability, Status } from "./api";
import { CriteriaPanel, Kpi, OpportunityTable, PolicyPanel, ReliabilityPanel, Series, statusColor } from "./components";

type Tab = "live" | "history" | "reliability" | "lab" | "executions" | "journal";

export default function App() {
  const [status, setStatus] = useState<Status | null>(null);
  const [wsState, setWsState] = useState<"open" | "closed">("closed");
  const [cycle, setCycle] = useState<CycleEvent | null>(null);
  const [liveRows, setLiveRows] = useState<Opportunity[]>([]);
  const [history, setHistory] = useState<Opportunity[]>([]);
  const [reliability, setReliability] = useState<(Reliability & { required_n_examples?: Record<string, number | null> }) | null>(null);
  const [signer, setSigner] = useState<{ configured: boolean; health: Record<string, unknown> | null; message: string | null } | null>(null);
  const [events, setEvents] = useState<{ ts: number; level: string; kind: string; message: string }[]>([]);
  const [executions, setExecutions] = useState<Record<string, unknown>[]>([]);
  const [changes, setChanges] = useState<Record<string, unknown>[]>([]);
  const [lab, setLab] = useState<Awaited<ReturnType<typeof api.labCurrent>> | null>(null);
  const [labMinutes, setLabMinutes] = useState(60);
  const [tab, setTab] = useState<Tab>("live");
  const [error, setError] = useState<string | null>(null);
  const labLog = useRef<string[]>([]);

  const refresh = useCallback(async () => {
    try {
      const [s, r, sg] = await Promise.all([api.status(), api.reliability(), api.signer()]);
      setStatus(s);
      setReliability(r);
      setSigner(sg);
      setError(null);
    } catch (e) {
      setError(String(e));
    }
  }, []);

  useEffect(() => {
    refresh();
    api.live(60).then(setLiveRows).catch(() => undefined);
    const id = window.setInterval(refresh, 10000);
    return () => window.clearInterval(id);
  }, [refresh]);

  useEffect(() => {
    const stop = openWs((e) => {
      if (e.kind === "cycle") {
        const c = e.data as CycleEvent;
        setCycle(c);
        setLiveRows(c.opportunities ?? []);
      } else if (e.kind === "status") {
        setStatus(e.data as Status);
      } else if (e.kind === "lab") {
        const d = e.data as { message: string };
        labLog.current = [...labLog.current.slice(-200), d.message];
        api.labCurrent().then(setLab).catch(() => undefined);
      } else if (e.kind === "execution" || e.kind === "emergency_stop" || e.kind === "resume") {
        refresh();
      }
    }, setWsState);
    return stop;
  }, [refresh]);

  useEffect(() => {
    const load = () => {
      if (tab === "history") api.opportunities(300).then(setHistory).catch(() => undefined);
      if (tab === "journal") api.events(100).then(setEvents).catch(() => undefined);
      if (tab === "executions") api.executions().then(setExecutions).catch(() => undefined);
      if (tab === "lab") {
        api.labCurrent().then(setLab).catch(() => undefined);
        api.changes().then(setChanges).catch(() => undefined);
      }
    };
    load();
    const id = window.setInterval(load, 8000);
    return () => window.clearInterval(id);
  }, [tab]);

  const positives = useMemo(() => liveRows.filter((o) => Number(o.expected_net) > 0), [liveRows]);
  const best = positives[0];

  const act = async (fn: () => Promise<unknown>) => {
    try {
      await fn();
      await refresh();
    } catch (e) {
      setError(String(e));
    }
  };

  const s = status;
  return (
    <div className="app">
      <div className="topbar">
        <div className="brand">
          arbbot <small>surveillance multi-DEX · simulation · exécution limitée sous politique</small>
        </div>
        <div className="badges">
          {s && (
            <>
              <span className={`badge big ${statusColor(s.risk.status_code)}`}>{s.risk.status}</span>
              <span className={`badge ${s.chain.is_devnet ? "amber" : "blue"}`}>{s.chain.is_devnet ? "DEVNET LOCAL" : s.chain.name}</span>
              <span className="badge">bloc {String(s.last_cycle.block ?? "—")}</span>
              <span className={`badge ${Number(s.collector.block_age_s ?? 0) > 10 ? "red" : ""}`}>données {Number(s.collector.block_age_s ?? 0).toFixed(1)} s</span>
              <span className="badge">gaz {Number(s.gas.base_fee_gwei ?? 0).toFixed(4)} gwei</span>
              <span className="badge">RPC p95 {s.rpc.latency_p95_ms !== null ? `${Number(s.rpc.latency_p95_ms).toFixed(0)} ms` : "—"}</span>
              <span className={`badge ${wsState === "open" ? "green" : "red"}`}>{wsState === "open" ? "WS connecté" : "WS déconnecté"}</span>
              <span className={`badge ${s.mode === "live" ? "green" : "purple"}`}>{s.mode === "live" ? "RÉEL" : "GHOST (aucune tx signée)"}</span>
            </>
          )}
        </div>
        <div className="controls">
          {s && !s.paused && (
            <button className="danger" onClick={() => confirm("Arrêt d'urgence : suspendre toute décision et toute exécution ?") && act(api.emergencyStop)}>
              ■ ARRÊT D'URGENCE
            </button>
          )}
          {s && s.paused && (
            <button className="ok" onClick={() => act(api.resume)}>
              ▶ Reprendre (simulation)
            </button>
          )}
          {s && (
            <button onClick={() => act(() => api.liveEnabled(!s.risk.manual_live_enabled))} title="Interdire / autoriser le passage en réel même si tous les critères sont verts">
              réel {s.risk.manual_live_enabled ? "autorisé" : "interdit"}
            </button>
          )}
          {s && s.risk.status_code === "READY_LIMITED_LIVE" && s.risk.manual_live_enabled && (
            <button className="ok" onClick={() => confirm("Activer l'exécution réelle limitée (politique signée) ?") && act(api.activateLive)}>
              activer le test réel limité
            </button>
          )}
        </div>
      </div>

      {s?.chain.is_devnet && <div className="devnet-banner">⚠️ Réseau de développement local (anvil, chain id 31337) : les pools, prix et opportunités affichés sont générés par le simulateur de marché local. Ce ne sont PAS des marchés réels. Aucun gain affiché ici n'est réel.</div>}
      {error && <div className="notice warn">Erreur API : {error}</div>}

      {s && (
        <div className="grid kpis">
          <Kpi label="Candidats (dernier bloc)" value={String(cycle?.candidates ?? s.last_cycle.candidates ?? 0)} sub={`${cycle?.positives ?? s.last_cycle.positives ?? 0} à net prévu > 0 · cycle ${Number(cycle?.cycle_ms ?? s.last_cycle.cycle_ms ?? 0).toFixed(0)} ms`} />
          <Kpi label="Meilleur net prévu (bloc)" value={eur(best?.expected_net_eur ?? 0, 3)} sub={best ? `${best.route}` : "—"} cls={best && (best.expected_net_eur ?? 0) > 0 ? "pos" : ""} />
          <Kpi label="Net ghost cumulé (N+1)" value={eur(s.cumulative.ghost_net_after_eur, 2)} sub={`${s.ghost.labeled} étiquettes · taux ${pct(s.ghost.rate)}`} cls={s.cumulative.ghost_net_after_eur >= 0 ? "pos" : "neg"} />
          <Kpi label="Net réalisé (réel)" value={`${Number(s.cumulative.realized_net_native).toFixed(6)} ETH`} sub={`${s.cumulative.executions} tx · ${s.cumulative.failures} échecs · gaz perdu ${Number(s.cumulative.failed_gas_native).toFixed(6)} ETH`} cls={s.cumulative.realized_net_native >= 0 ? "pos" : "neg"} />
          <Kpi label="Fiabilité (borne inf.)" value={reliability?.global_lower !== undefined ? pct(reliability.global_lower) : "—"} sub={reliability ? `${reliability.label} · n=${reliability.n}` : ""} cls={reliability?.label === "OK" ? "pos" : "neg"} />
          <Kpi label="Univers" value={`${s.pools} pools · ${s.routes} routes`} sub={`${Object.keys(s.flash_providers).length} fournisseurs flash · ETH ${s.native_price_usd ? `${s.native_price_usd.toFixed(0)} $` : "—"}`} />
          <Kpi label="Rejets (cumul)" value={String(Object.values(s.detector.rejections ?? {}).reduce((a, b) => a + b, 0))} sub={Object.entries(s.detector.rejections ?? {}).slice(0, 3).map(([k, v]) => `${k} ${v}`).join(" · ")} />
        </div>
      )}

      <div className="grid cols">
        <Series title="Meilleur net prévu par bloc (€)" name="best_expected_net_eur" color="#2ecc71" unit=" €" kind="area" />
        <Series title="Candidats par bloc" name="candidates" color="#4da3ff" kind="bar" />
        <Series title="Prix du gaz (base fee, gwei)" name="gas_price_gwei" color="#ffb547" />
        <Series title="Latence du cycle (ms)" name="cycle_ms" color="#b58cff" />
      </div>

      <div className="tabs">
        {(["live", "history", "reliability", "lab", "executions", "journal"] as Tab[]).map((t) => (
          <button key={t} className={tab === t ? "active" : ""} onClick={() => setTab(t)}>
            {{ live: "Opportunités (bloc courant)", history: "Historique", reliability: "Fiabilité", lab: "Laboratoire & auto-correction", executions: "Exécutions", journal: "Journal" }[t]}
          </button>
        ))}
      </div>

      {tab === "live" && (
        <div className="panel" style={{ marginTop: 10 }}>
          <h3>
            Opportunités du bloc {cycle?.block ?? "—"} <span className="right muted">toutes les colonnes de coût · négatifs conservés · décision et motifs</span>
          </h3>
          <OpportunityTable rows={liveRows} status={s} />
        </div>
      )}
      {tab === "history" && (
        <div className="panel" style={{ marginTop: 10 }}>
          <h3>300 dernières opportunités enregistrées (base SQLite)</h3>
          <OpportunityTable rows={history} status={s} />
        </div>
      )}
      {tab === "reliability" && (
        <div className="grid cols">
          <ReliabilityPanel r={reliability} />
          {s && <CriteriaPanel s={s} />}
          {s && <PolicyPanel s={s} signer={signer} />}
        </div>
      )}
      {tab === "lab" && (
        <div className="grid cols">
          <div className="panel">
            <h3>
              Laboratoire d'optimisation autonome
              <span className="right">
                <input type="number" min={3} max={240} value={labMinutes} onChange={(e) => setLabMinutes(Number(e.target.value))} /> min{" "}
                <button disabled={!!lab?.running} onClick={() => act(() => api.labStart(labMinutes))}>
                  démarrer
                </button>{" "}
                <button disabled={!lab?.running} onClick={() => act(api.labStop)}>
                  arrêter
                </button>
              </span>
            </h3>
            {lab?.running && (
              <>
                <div className="muted" style={{ marginBottom: 6 }}>
                  phase <b>{lab.phase}</b> · {((lab.elapsed_s ?? 0) / 60).toFixed(1)} / {((lab.total_s ?? 0) / 60).toFixed(0)} min
                </div>
                <div className="progress">
                  <div style={{ width: `${Math.min(100, (100 * (lab.elapsed_s ?? 0)) / (lab.total_s ?? 1))}%` }} />
                </div>
              </>
            )}
            {!lab?.running && <div className="muted">Phases : diagnostic (0–5) · validation des données (5–15) · recherche + simulation (15–30) · auto-correction (30–45) · validation comparative (45–55) · rapport (55–60). Durée réduite possible pour le devnet.</div>}
            <div className="log" style={{ marginTop: 10 }}>
              {(lab?.results?.log ?? labLog.current).slice(-60).join("\n") || "—"}
            </div>
            {lab?.results?.report_files && <div style={{ marginTop: 8 }}>Rapport : {lab.results.report_files.join(", ")}</div>}
          </div>
          <div className="panel">
            <h3>Auto-correction : changements (paramètres de stratégie uniquement, isolés dans git)</h3>
            <div className="table-wrap" style={{ maxHeight: 360 }}>
              <table>
                <thead>
                  <tr>
                    <th className="left">Date</th>
                    <th className="left">Description</th>
                    <th>Métrique réf.</th>
                    <th>Métrique cand.</th>
                    <th className="left">Décision</th>
                    <th className="left">git</th>
                  </tr>
                </thead>
                <tbody>
                  {changes.map((c, i) => (
                    <tr key={i}>
                      <td className="left">{new Date(Number(c.ts) * 1000).toLocaleString("fr-FR")}</td>
                      <td className="left reasons">{String(c.description)}</td>
                      <td>{c.metric_before === null ? "—" : Number(c.metric_before).toFixed(4)}</td>
                      <td>{c.metric_after === null ? "—" : Number(c.metric_after).toFixed(4)}</td>
                      <td className="left">
                        <span className={`badge ${c.accepted ? "green" : "red"}`}>{c.accepted ? "accepté" : "rollback"}</span>
                      </td>
                      <td className="left mono">{String(c.git_ref ?? "")}</td>
                    </tr>
                  ))}
                  {changes.length === 0 && (
                    <tr>
                      <td colSpan={6} className="left muted">
                        Aucun changement pour l'instant.
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
            {s && (
              <>
                <h3 style={{ marginTop: 14 }}>Paramètres de stratégie actifs (version {String(s.tunables.version)})</h3>
                <div className="log">{JSON.stringify(s.tunables, null, 1)}</div>
              </>
            )}
          </div>
        </div>
      )}
      {tab === "executions" && (
        <div className="panel" style={{ marginTop: 10 }}>
          <h3>Transactions réelles (toutes, y compris les échecs)</h3>
          <div className="table-wrap">
            <table>
              <thead>
                <tr>
                  <th className="left">Date</th>
                  <th className="left">Statut</th>
                  <th className="left">Hash</th>
                  <th>Bloc</th>
                  <th>Gaz utilisé</th>
                  <th>Coût gaz (ETH)</th>
                  <th>Net prévu (unités)</th>
                  <th>Net réalisé (unités)</th>
                  <th className="left">Erreur</th>
                </tr>
              </thead>
              <tbody>
                {executions.map((e, i) => (
                  <tr key={i}>
                    <td className="left">{new Date(Number(e.ts) * 1000).toLocaleString("fr-FR")}</td>
                    <td className="left">
                      <span className={`badge ${e.status === "success" ? "green" : "red"}`}>{String(e.status)}</span>
                    </td>
                    <td className="left mono">{String(e.tx_hash ?? "—").slice(0, 18)}…</td>
                    <td>{String(e.block_number ?? "—")}</td>
                    <td>{String(e.gas_used ?? "—")}</td>
                    <td>{e.gas_cost_wei ? (Number(e.gas_cost_wei) / 1e18).toFixed(8) : "—"}</td>
                    <td>{String(e.expected_net ?? "—")}</td>
                    <td className={Number(e.realized_net) > 0 ? "pos" : "neg"}>{String(e.realized_net ?? "—")}</td>
                    <td className="left reasons">{String(e.error ?? "")}</td>
                  </tr>
                ))}
                {executions.length === 0 && (
                  <tr>
                    <td colSpan={9} className="left muted">
                      Aucune transaction réelle n'a été envoyée.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}
      {tab === "journal" && (
        <div className="panel" style={{ marginTop: 10 }}>
          <h3>Journal des événements</h3>
          <div className="log">{events.map((e) => `${new Date(e.ts * 1000).toLocaleTimeString("fr-FR")} [${e.level}] ${e.kind}: ${e.message}`).join("\n") || "—"}</div>
        </div>
      )}

      <div className="footer">Toutes les valeurs affichées proviennent de mesures (RPC, simulations eth_call, étiquetage ghost au bloc N+1, reçus de transactions). Aucune projection de revenu. Les montants empruntés par flash loan ne sont jamais comptés comme des gains.</div>
    </div>
  );
}
