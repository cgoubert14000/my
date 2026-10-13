import { useEffect, useState } from "react";
import { Area, AreaChart, Bar, BarChart, CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { api, eur, Opportunity, pct, Reliability, Status, units } from "./api";

export function statusColor(code: string): string {
  switch (code) {
    case "LIVE_ACTIVE":
      return "green";
    case "READY_LIMITED_LIVE":
      return "blue";
    case "SUSPENDED":
      return "red";
    case "RELIABILITY_INSUFFICIENT":
      return "amber";
    case "SIMULATION":
      return "purple";
    default:
      return "amber";
  }
}

export function Kpi({ label, value, sub, cls }: { label: string; value: string; sub?: string; cls?: string }) {
  return (
    <div className="kpi">
      <div className="label">{label}</div>
      <div className={`value ${cls ?? ""}`}>{value}</div>
      {sub && <div className="sub">{sub}</div>}
    </div>
  );
}

const fmtTime = (ts: number) => new Date(ts * 1000).toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit", second: "2-digit" });

export function Series({ title, name, color, minutes = 30, unit = "", kind = "line" }: { title: string; name: string; color: string; minutes?: number; unit?: string; kind?: "line" | "area" | "bar" }) {
  const [data, setData] = useState<{ ts: number; value: number }[]>([]);
  useEffect(() => {
    let alive = true;
    const load = () => api.metrics(name, minutes).then((d) => alive && setData(d)).catch(() => undefined);
    load();
    const id = window.setInterval(load, 5000);
    return () => {
      alive = false;
      window.clearInterval(id);
    };
  }, [name, minutes]);
  const Chart = kind === "bar" ? BarChart : kind === "area" ? AreaChart : LineChart;
  return (
    <div className="panel">
      <h3>
        {title} <span className="right muted">{data.length} points · {minutes} min</span>
      </h3>
      <div className="chart">
        <ResponsiveContainer>
          <Chart data={data} margin={{ top: 5, right: 10, left: 0, bottom: 0 }}>
            <CartesianGrid stroke="#22304d" strokeDasharray="3 3" />
            <XAxis dataKey="ts" tickFormatter={fmtTime} stroke="#8b98b8" fontSize={11} minTickGap={40} />
            <YAxis stroke="#8b98b8" fontSize={11} width={60} tickFormatter={(v) => `${Number(v).toLocaleString("fr-FR", { maximumFractionDigits: 3 })}${unit}`} />
            <Tooltip contentStyle={{ background: "#0f162a", border: "1px solid #22304d" }} labelFormatter={(v) => fmtTime(Number(v))} formatter={(v) => [`${Number(v).toLocaleString("fr-FR", { maximumFractionDigits: 6 })}${unit}`, title]} />
            {kind === "bar" ? <Bar dataKey="value" fill={color} isAnimationActive={false} /> : kind === "area" ? <Area dataKey="value" stroke={color} fill={color} fillOpacity={0.2} isAnimationActive={false} dot={false} /> : <Line dataKey="value" stroke={color} dot={false} isAnimationActive={false} strokeWidth={1.6} />}
          </Chart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

function tokenEur(raw: string | number | null | undefined, o: Opportunity, s: Status | null): string {
  if (raw === null || raw === undefined || !s) return "—";
  const n = Number(raw) / 10 ** o.token_decimals;
  const expected = Number(o.expected_net) / 10 ** o.token_decimals;
  if (!o.expected_net_eur || !expected) return "—";
  return eur((n * o.expected_net_eur) / expected, 3);
}

export function OpportunityTable({ rows, status }: { rows: Opportunity[]; status: Status | null }) {
  return (
    <div className="table-wrap">
      <table>
        <thead>
          <tr>
            <th className="left">Bloc</th>
            <th className="left">Route</th>
            <th>Emprunt</th>
            <th>Brut</th>
            <th>Frais flash</th>
            <th>Gaz</th>
            <th>Net prévu</th>
            <th>Net prévu €</th>
            <th>Net simulé</th>
            <th>Net N+1 (ghost)</th>
            <th>Net réalisé</th>
            <th>Marge</th>
            <th>Impact</th>
            <th>P(succès) borne inf.</th>
            <th className="left">Incertitude</th>
            <th>Sim</th>
            <th className="left">Décision</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((o) => {
            const d = o.token_decimals;
            const net = Number(o.expected_net);
            return (
              <tr key={o.id}>
                <td className="left mono">{o.block_number}</td>
                <td className="left mono" title={o.route}>
                  {o.route}
                </td>
                <td>
                  {units(o.amount_in, d, 2)} {o.token}
                </td>
                <td className={Number(o.gross_profit) > 0 ? "pos" : "neg"}>{units(o.gross_profit, d, 6)}</td>
                <td>{units(o.fees.flash_fee, d, 6)}</td>
                <td title={`${o.fees.gas_units} gaz × ${(o.fees.gas_price_wei / 1e9).toFixed(4)} gwei${o.fees.l1_data_fee_wei ? ` + L1 ${(o.fees.l1_data_fee_wei / 1e18).toFixed(8)} ETH` : ""}`}>{units(o.fees.gas_cost_token, d, 6)}</td>
                <td className={net > 0 ? "pos" : "neg"}>{units(o.expected_net, d, 6)}</td>
                <td className={net > 0 ? "pos" : "neg"}>{eur(o.expected_net_eur, 3)}</td>
                <td className={o.simulated_net === null ? "muted" : Number(o.simulated_net) > 0 ? "pos" : "neg"} title={o.simulated_net === null ? "non simulé" : tokenEur(o.simulated_net, o, status)}>
                  {o.simulated_net === null ? "—" : units(o.simulated_net, d, 6)}
                </td>
                <td className={o.ghost_next_block_net === null || o.ghost_next_block_net === undefined ? "muted" : Number(o.ghost_next_block_net) > 0 ? "pos" : "neg"}>
                  {o.ghost_next_block_net === null || o.ghost_next_block_net === undefined ? "—" : units(o.ghost_next_block_net, d, 6)}
                </td>
                <td className={o.realized_net === null ? "muted" : Number(o.realized_net) > 0 ? "pos" : "neg"}>{o.realized_net === null ? "—" : units(o.realized_net, d, 6)}</td>
                <td>{o.margin_bps.toFixed(2)} bps</td>
                <td>{o.price_impact_bps.toFixed(1)} bps</td>
                <td title={`moyenne ${pct(o.p_success)} · borne sup ${pct(o.p_upper)} · n=${o.p_n}`}>
                  {o.p_lower === null ? "—" : `${pct(o.p_lower)} (n=${o.p_n})`}
                </td>
                <td className="left">
                  <span className={`badge ${o.uncertainty === "OK" ? "green" : "amber"}`}>{o.uncertainty}</span>
                </td>
                <td title={o.sim?.error ?? ""}>{o.sim ? (o.sim.ok ? <span className="pos">OK</span> : <span className="neg">échec</span>) : <span className="muted">—</span>}</td>
                <td className="left">
                  <span className={`badge ${o.decision === "SELECTED" || o.decision === "EXECUTED" ? "green" : o.decision === "ELIGIBLE" ? "blue" : o.decision === "FAILED" ? "red" : ""}`}>{o.decision}</span>
                  <div className="reasons">{o.reasons.join(" · ")}</div>
                </td>
              </tr>
            );
          })}
          {rows.length === 0 && (
            <tr>
              <td colSpan={17} className="left muted">
                Aucune opportunité enregistrée pour l'instant.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export function ReliabilityPanel({ r }: { r: Reliability | null }) {
  if (!r) return null;
  const buckets = Object.entries(r.buckets ?? {}).sort((a, b) => b[1].n - a[1].n).slice(0, 12);
  const ok = r.label === "OK";
  return (
    <div className="panel">
      <h3>
        Fiabilité mesurée <span className={`badge ${ok ? "green" : "amber"}`}>{r.label}</span>
      </h3>
      <div className="kv">
        <span className="k">Observations (ghost N+1 + réel)</span>
        <span>
          {r.n} / minimum {r.min_observations}
        </span>
        <span className="k">Taux observé de net &gt; 0</span>
        <span>{pct(r.rate)}</span>
        <span className="k">Borne inférieure crédible ({pct(r.credible_level, 0)})</span>
        <span className={r.global_lower !== undefined && r.global_lower >= r.threshold ? "pos" : "neg"}>{pct(r.global_lower)}</span>
        <span className="k">Seuil requis</span>
        <span>{pct(r.threshold, 0)}</span>
        {r.required_n_at_current_rate !== undefined && (
          <>
            <span className="k">n requis au taux actuel pour atteindre le seuil</span>
            <span>{r.required_n_at_current_rate ?? "impossible (taux ≤ seuil)"}</span>
          </>
        )}
        <span className="k">Régression logistique (validation holdout)</span>
        <span className="mono">{"brier_logistic" in r.logistic ? `Brier ${(r.logistic.brier_logistic as number).toFixed(3)} vs buckets ${(r.logistic.brier_bucket as number).toFixed(3)} · n holdout ${r.logistic.holdout_n as number}` : String(r.logistic.status ?? "—")}</span>
      </div>
      <div className="table-wrap" style={{ marginTop: 10, maxHeight: 240 }}>
        <table>
          <thead>
            <tr>
              <th className="left">Segment (marge | sauts | pools)</th>
              <th>n</th>
              <th>succès</th>
              <th>moyenne</th>
              <th>borne inf.</th>
              <th className="left">statut</th>
            </tr>
          </thead>
          <tbody>
            {buckets.map(([k, v]) => (
              <tr key={k}>
                <td className="left mono">{k}</td>
                <td>{v.n}</td>
                <td>{v.k}</td>
                <td>{pct(v.mean)}</td>
                <td className={v.lower >= r.threshold ? "pos" : "neg"}>{pct(v.lower)}</td>
                <td className="left">
                  <span className={`badge ${v.status === "OK" ? "green" : "amber"}`}>{v.status}</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export function CriteriaPanel({ s }: { s: Status }) {
  return (
    <div className="panel">
      <h3>
        Décision de maturité <span className={`badge big ${statusColor(s.risk.status_code)}`}>{s.risk.status}</span>
      </h3>
      <div className="muted" style={{ marginBottom: 8 }}>
        {s.risk.sub_status}
        {s.risk.suspended_reason && <span className="neg"> — {s.risk.suspended_reason}</span>}
      </div>
      <ul className="criteria">
        {s.risk.criteria.map((c) => (
          <li key={c.name}>
            <span>{c.ok ? "✅" : "❌"}</span>
            <span>{c.name}</span>
            <span className="detail">{c.detail}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export function PolicyPanel({ s, signer }: { s: Status; signer: { configured: boolean; health: Record<string, unknown> | null; message: string | null } | null }) {
  const p = s.policy as Record<string, string | number | boolean | null>;
  return (
    <div className="panel">
      <h3>
        Politique d'autorisation (lecture seule pour le moteur) <span className={`badge ${p.valid ? "green" : "amber"}`}>{p.valid ? "valide" : String(p.reason)}</span>
      </h3>
      {signer && !signer.configured && <div className="notice warn">{signer.message}</div>}
      {signer && signer.configured && <div className="notice">Signer : {String(signer.health?.address ?? "—")} · tx signées {String(signer.health?.tx_count ?? "—")} · politique {signer.health?.policy_valid ? "valide" : "invalide"}</div>}
      <div className="kv" style={{ marginTop: 8 }}>
        <span className="k">Empreinte</span>
        <span className="mono">{String(p.digest)}</span>
        <span className="k">Portefeuille dédié</span>
        <span className="mono">{String(p.wallet_address || "—")}</span>
        <span className="k">Contrat exécuteur</span>
        <span className="mono">{String(p.executor_contract || "—")}</span>
        <span className="k">Budget gaz total / par tx</span>
        <span>
          {String(p.max_total_budget_native)} / {String(p.max_gas_per_tx_native)} ETH
        </span>
        <span className="k">Nombre max de tx</span>
        <span>{String(p.max_transactions)}</span>
        <span className="k">Profit net minimum</span>
        <span>{String(p.min_net_profit_native)} ETH</span>
        <span className="k">Slippage max / perte cumulée max</span>
        <span>
          {String(p.max_slippage_bps)} bps / {String(p.max_cumulative_loss_native)} ETH
        </span>
        <span className="k">Probabilité de succès minimale</span>
        <span>{pct(Number(p.min_success_probability), 0)}</span>
        <span className="k">Emprunt max</span>
        <span>{String(p.max_borrow_usd)} USD</span>
        <span className="k">Validité</span>
        <span>{p.valid_until ? new Date(Number(p.valid_until) * 1000).toLocaleString("fr-FR") : "non définie (0)"}</span>
      </div>
      <h3 style={{ marginTop: 14 }}>Comptabilité réelle</h3>
      <div className="kv">
        <span className="k">Transactions</span>
        <span>{s.risk.ledger.tx_count}</span>
        <span className="k">Gaz dépensé</span>
        <span>{Number(s.risk.ledger.gas_spent_native).toFixed(6)} ETH</span>
        <span className="k">Net réalisé</span>
        <span className={Number(s.risk.ledger.realized_net_native) >= 0 ? "pos" : "neg"}>{Number(s.risk.ledger.realized_net_native).toFixed(6)} ETH</span>
        <span className="k">Échecs / consécutifs</span>
        <span>
          {s.risk.ledger.failures} / {s.risk.ledger.consecutive_failures}
        </span>
      </div>
    </div>
  );
}
