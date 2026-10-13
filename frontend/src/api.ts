// Thin API client. All URLs are relative: the dev server (or the backend itself in production) serves the UI
// and proxies /api + /ws, so the browser never talks to localhost directly.

export type Criterion = { name: string; ok: boolean; detail: string };

export type Status = {
  chain: { id: string; chain_id: number; name: string; verified: boolean; is_devnet: boolean; rpc_host?: string; verification?: { ts: number; pools: number; rpc_host: string } | null };
  uptime_s: number;
  mode: "ghost" | "live";
  paused: boolean;
  risk: {
    status: string;
    status_code: string;
    sub_status: string;
    suspended_reason: string;
    kill_switch: boolean;
    criteria: Criterion[];
    ledger: Record<string, number>;
    policy: Record<string, unknown>;
    flags: Record<string, unknown>;
    manual_live_enabled: boolean;
  };
  collector: Record<string, number | boolean | null>;
  rpc: Record<string, number | null>;
  gas: Record<string, number>;
  native_price_usd: number | null;
  pools: number;
  routes: number;
  detector: { cycles: number; candidates: number; positive_net: number; last_cycle_ms: number; rejections: Record<string, number> };
  ghost: { pending: number; labeled: number; positives: number; errors: number; rate: number | null };
  reliability: Reliability;
  cumulative: Record<string, number>;
  executions: Record<string, { n: number; gas_wei: number; net: number }>;
  last_cycle: Record<string, number | string | null>;
  tunables: Record<string, unknown>;
  policy: Record<string, unknown>;
  signer: Record<string, unknown> | null;
  flash_providers: Record<string, { fee_bps: number; verified: boolean }>;
  episodes_open: number;
};

export type Reliability = {
  n: number;
  positives: number;
  rate: number | null;
  threshold: number;
  credible_level: number;
  min_observations: number;
  global_mean?: number;
  global_lower?: number;
  global_upper?: number;
  required_n_at_current_rate?: number | null;
  buckets: Record<string, { n: number; k: number; mean: number; lower: number; upper: number; sufficient: boolean; status: string }>;
  recent?: { n: number; observed_rate: number; mean_net_error?: number };
  logistic: Record<string, unknown>;
  label: string;
};

export type Opportunity = {
  id: string;
  ts: number;
  block_number: number;
  route: string;
  route_key: string;
  token: string;
  token_decimals: number;
  flash_source: string;
  amount_in: string | number;
  amount_out: string | number;
  gross_profit: string | number;
  expected_net: string | number;
  simulated_net: string | number | null;
  realized_net: string | number | null;
  expected_net_eur: number | null;
  margin_bps: number;
  price_impact_bps: number;
  spread_bps: number;
  fees: {
    flash_fee: string | number;
    swap_fees: string | number;
    gas_units: number;
    gas_price_wei: number;
    l1_data_fee_wei: number;
    gas_cost_wei: number;
    gas_cost_token: string | number;
    native_price_in_token: number;
    failure_cost_wei: number;
    unknowns: string[];
  };
  decision: string;
  reasons: string[];
  p_success: number | null;
  p_lower: number | null;
  p_upper: number | null;
  p_n: number;
  uncertainty: string;
  sim: { ok: boolean; profit: string | number | null; error: string | null; gas_estimate: number | null; mode: string } | null;
  data_age_ms: number;
  ghost_next_block_net: string | number | null;
  ghost_label?: number;
  tx_hash: string | null;
};

export type CycleEvent = {
  block: number;
  candidates: number;
  positives: number;
  cycle_ms: number;
  best_expected_net_eur: number;
  ts: number;
  selected: Opportunity | null;
  execution?: string;
  opportunities: Opportunity[];
};

async function j<T>(url: string, init?: RequestInit): Promise<T> {
  const r = await fetch(url, init);
  if (!r.ok) throw new Error(`${url}: ${r.status} ${await r.text()}`);
  return (await r.json()) as T;
}

export const api = {
  status: () => j<Status>("/api/status"),
  opportunities: (limit = 200) => j<Opportunity[]>(`/api/opportunities?limit=${limit}`),
  live: (limit = 60) => j<Opportunity[]>(`/api/opportunities/live?limit=${limit}`),
  metrics: (name: string, minutes = 60) => j<{ ts: number; value: number }[]>(`/api/metrics/${name}?minutes=${minutes}`),
  reliability: () => j<Reliability & { required_n_examples: Record<string, number | null> }>("/api/reliability"),
  executions: () => j<Record<string, unknown>[]>("/api/executions"),
  events: (limit = 50) => j<{ ts: number; level: string; kind: string; message: string }[]>(`/api/events?limit=${limit}`),
  changes: () => j<Record<string, unknown>[]>("/api/changes"),
  pools: () => j<Record<string, unknown>[]>("/api/pools"),
  labCurrent: () => j<{ running: boolean; phase?: string; elapsed_s?: number; total_s?: number; results?: { log: string[]; phases: Record<string, unknown>; report_files?: string[] } }>("/api/lab/current"),
  labRuns: () => j<Record<string, unknown>[]>("/api/lab/runs"),
  signer: () => j<{ configured: boolean; health: Record<string, unknown> | null; message: string | null }>("/api/signer"),
  emergencyStop: () => j("/api/control/emergency-stop", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ reason: "UI" }) }),
  resume: () => j("/api/control/resume", { method: "POST" }),
  liveEnabled: (enabled: boolean) => j("/api/control/live-enabled", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ enabled }) }),
  activateLive: () => j<{ ok: boolean }>("/api/control/activate-live", { method: "POST" }),
  labStart: (minutes: number) => j("/api/lab/start", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ minutes }) }),
  labStop: () => j("/api/lab/stop", { method: "POST" }),
};

export function units(raw: string | number | null | undefined, decimals: number, digits = 4): string {
  if (raw === null || raw === undefined) return "—";
  const n = typeof raw === "string" ? Number(raw) : raw;
  if (!Number.isFinite(n)) return "—";
  return (n / 10 ** decimals).toLocaleString("fr-FR", { maximumFractionDigits: digits, minimumFractionDigits: 0 });
}

export function eur(x: number | null | undefined, digits = 2): string {
  if (x === null || x === undefined || !Number.isFinite(x)) return "—";
  return x.toLocaleString("fr-FR", { style: "currency", currency: "EUR", maximumFractionDigits: digits });
}

export function pct(x: number | null | undefined, digits = 1): string {
  if (x === null || x === undefined || !Number.isFinite(x)) return "—";
  return `${(x * 100).toFixed(digits)} %`;
}

export function openWs(onEvent: (e: { kind: string; ts: number; data: unknown }) => void, onState: (s: "open" | "closed") => void): () => void {
  let ws: WebSocket | null = null;
  let closed = false;
  let timer: number | undefined;
  const connect = () => {
    const proto = location.protocol === "https:" ? "wss" : "ws";
    ws = new WebSocket(`${proto}://${location.host}/ws`);
    ws.onopen = () => onState("open");
    ws.onmessage = (m) => {
      try {
        onEvent(JSON.parse(m.data));
      } catch {
        /* ignore */
      }
    };
    ws.onclose = () => {
      onState("closed");
      if (!closed) timer = window.setTimeout(connect, 2000);
    };
    ws.onerror = () => ws?.close();
  };
  connect();
  return () => {
    closed = true;
    if (timer) window.clearTimeout(timer);
    ws?.close();
  };
}
