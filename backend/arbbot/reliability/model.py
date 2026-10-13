"""Reliability engine: measured probability that an accepted opportunity yields a positive NET profit.

Nothing here is a "confidence score" invented by a heuristic. Every probability comes from counted outcomes:

  observation = (features of the opportunity at decision time, label)
  label       = 1 if the net profit measured *after the fact* was > 0, else 0
                 • ghost mode : net profit re-simulated at the block where our tx would have landed
                 • live mode  : realised net profit from the receipt (gas included)

Primary estimator — Beta-Binomial per bucket (margin band × hop count × pool-kind class) with a Jeffreys
prior; the gate uses the one-sided lower credible bound at `credible_level` (conservative by construction).
Secondary estimator — L2-regularised logistic regression on standardised features, trained on the first 70 %
of the time-ordered data and evaluated on the last 30 % (Brier score, log-loss, calibration error). It only
replaces the bucket mean when it is better calibrated on the holdout; it never relaxes the lower bound.

When the bucket has fewer than `min_observations` outcomes the result is
    FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
and the opportunity is not eligible, whatever the point estimate says.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np
from scipy.optimize import minimize
from scipy.stats import beta as beta_dist

INSUFFICIENT = "FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES"

MARGIN_BANDS = ((-1e9, 0.0), (0.0, 3.0), (3.0, 8.0), (8.0, 20.0), (20.0, 50.0), (50.0, 1e9))
FEATURE_NAMES = ("margin_bps", "spread_bps", "hops", "gas_share", "data_age_ms", "impact_bps", "log_amount_usd")


@dataclass
class Observation:
    ts: float
    features: dict
    label: int  # 1 = positive net profit after the fact
    source: str  # "ghost" | "live"
    route_key: str = ""
    net_after: float | None = None  # measured net (token units) for drift analysis
    net_expected: float | None = None


@dataclass
class Estimate:
    p_mean: float | None
    p_lower: float | None
    p_upper: float | None
    n: int
    bucket: str
    method: str
    sufficient: bool
    label: str
    details: dict = field(default_factory=dict)

    def as_dict(self) -> dict:
        return {
            "p_mean": self.p_mean, "p_lower": self.p_lower, "p_upper": self.p_upper, "n": self.n, "bucket": self.bucket,
            "method": self.method, "sufficient": self.sufficient, "label": self.label, **self.details,
        }


def bucket_of(features: dict) -> str:
    m = float(features.get("margin_bps", 0.0))
    band = next((f"{lo:g}-{hi:g}" for lo, hi in MARGIN_BANDS if lo <= m < hi), "?")
    hops = int(features.get("hops", 2))
    cls = str(features.get("route_class", "?"))
    return f"m[{band}]|h{hops}|{cls}"


def beta_interval(k: int, n: int, level: float, a: float = 0.5, b: float = 0.5) -> tuple[float, float, float]:
    """Posterior mean and one-sided lower / upper bounds at `level` (Jeffreys prior by default)."""
    mean = (k + a) / (n + a + b)
    lower = float(beta_dist.ppf(1 - level, k + a, n - k + b))
    upper = float(beta_dist.ppf(level, k + a, n - k + b))
    return mean, lower, upper


def required_sample_size(p_hat: float, threshold: float, level: float, max_n: int = 100_000) -> int | None:
    """Smallest n such that, observing rate p_hat, the lower credible bound reaches `threshold`."""
    if p_hat <= threshold:
        return None
    lo, hi = 1, max_n
    if beta_interval(int(round(p_hat * hi)), hi, level)[1] < threshold:
        return None
    while lo < hi:
        mid = (lo + hi) // 2
        if beta_interval(int(round(p_hat * mid)), mid, level)[1] >= threshold:
            hi = mid
        else:
            lo = mid + 1
    return lo


class _Logistic:
    def __init__(self, l2: float = 1.0):
        self.l2 = l2
        self.w: np.ndarray | None = None
        self.mu: np.ndarray | None = None
        self.sd: np.ndarray | None = None

    def _x(self, feats: list[dict]) -> np.ndarray:
        return np.array([[float(f.get(k, 0.0)) for k in FEATURE_NAMES] for f in feats], dtype=float)

    def fit(self, feats: list[dict], y: list[int]) -> None:
        X = self._x(feats)
        self.mu = X.mean(axis=0)
        self.sd = X.std(axis=0) + 1e-9
        Xs = np.hstack([np.ones((len(X), 1)), (X - self.mu) / self.sd])
        yv = np.array(y, dtype=float)

        def loss(w):
            z = Xs @ w
            p = 1 / (1 + np.exp(-z))
            eps = 1e-9
            nll = -np.mean(yv * np.log(p + eps) + (1 - yv) * np.log(1 - p + eps))
            return nll + self.l2 * np.sum(w[1:] ** 2) / len(yv)

        res = minimize(loss, np.zeros(Xs.shape[1]), method="L-BFGS-B")
        self.w = res.x

    def predict(self, feats: list[dict]) -> np.ndarray:
        X = self._x(feats)
        Xs = np.hstack([np.ones((len(X), 1)), (X - self.mu) / self.sd])
        return 1 / (1 + np.exp(-(Xs @ self.w)))


class ReliabilityModel:
    def __init__(self, *, min_observations: int = 30, credible_level: float = 0.90, threshold: float = 0.75):
        self.min_obs = min_observations
        self.level = credible_level
        self.threshold = threshold
        self.obs: list[Observation] = []
        self._lr: _Logistic | None = None
        self._lr_metrics: dict = {}
        self._dirty = True

    # ------------------------------------------------------------------ data

    def add(self, o: Observation) -> None:
        self.obs.append(o)
        self._dirty = True

    def extend(self, obs: list[Observation]) -> None:
        self.obs.extend(obs)
        self._dirty = True

    @property
    def n(self) -> int:
        return len(self.obs)

    # ------------------------------------------------------------------ estimation

    def _bucket_counts(self, bucket: str) -> tuple[int, int]:
        k = n = 0
        for o in self.obs:
            if bucket_of(o.features) == bucket:
                n += 1
                k += o.label
        return k, n

    def estimate(self, features: dict) -> Estimate:
        bucket = bucket_of(features)
        k, n = self._bucket_counts(bucket)
        kg = sum(o.label for o in self.obs)
        ng = len(self.obs)
        details = {"global_n": ng, "global_rate": (kg / ng) if ng else None, "threshold": self.threshold,
                   "credible_level": self.level, "min_observations": self.min_obs}
        if n < self.min_obs:
            mean, lower, upper = beta_interval(k, n, self.level) if n else (None, None, None)
            if ng >= self.min_obs:
                gm, gl, gu = beta_interval(kg, ng, self.level)
                details["global_lower"] = gl
            details["required_n_at_current_rate"] = (
                required_sample_size(k / n, self.threshold, self.level) if n and k / n > self.threshold else None
            )
            return Estimate(mean, lower, upper, n, bucket, "beta-binomial", False, INSUFFICIENT, details)
        mean, lower, upper = beta_interval(k, n, self.level)
        method = "beta-binomial"
        self._maybe_fit_lr()
        if self._lr is not None and self._lr_metrics.get("lr_better"):
            p_lr = float(self._lr.predict([features])[0])
            details["p_bucket_mean"] = mean
            details["p_logistic"] = p_lr
            mean = p_lr
            method = "logistic(holdout-validated)+beta-lower-bound"
        label = "OK" if lower >= self.threshold else "FIABILITÉ INSUFFISANTE"
        details["lr_metrics"] = self._lr_metrics
        return Estimate(mean, lower, upper, n, bucket, method, True, label, details)

    # ------------------------------------------------------------------ logistic regression + validation

    def _maybe_fit_lr(self) -> None:
        if not self._dirty:
            return
        self._dirty = False
        self._lr = None
        self._lr_metrics = {}
        if len(self.obs) < 200:
            return
        obs = sorted(self.obs, key=lambda o: o.ts)
        cut = int(len(obs) * 0.7)
        train, test = obs[:cut], obs[cut:]
        if len({o.label for o in train}) < 2 or len(test) < 30:
            return
        lr = _Logistic()
        lr.fit([o.features for o in train], [o.label for o in train])
        p_lr = lr.predict([o.features for o in test])
        y = np.array([o.label for o in test], dtype=float)
        # bucket model prediction on the holdout, using only training data
        bk: dict[str, list[int]] = {}
        for o in train:
            bk.setdefault(bucket_of(o.features), []).append(o.label)
        p_bucket = np.array([
            beta_interval(sum(bk.get(bucket_of(o.features), [])), len(bk.get(bucket_of(o.features), [])), self.level)[0]
            for o in test
        ])
        brier_lr = float(np.mean((p_lr - y) ** 2))
        brier_bk = float(np.mean((p_bucket - y) ** 2))
        ece_lr = _ece(p_lr, y)
        ece_bk = _ece(p_bucket, y)
        self._lr = lr
        self._lr_metrics = {
            "holdout_n": len(test), "brier_logistic": brier_lr, "brier_bucket": brier_bk,
            "ece_logistic": ece_lr, "ece_bucket": ece_bk, "lr_better": brier_lr < brier_bk and ece_lr <= ece_bk + 0.02,
        }

    # ------------------------------------------------------------------ reports

    def calibration_report(self, recent: int = 100) -> dict:
        n = len(self.obs)
        k = sum(o.label for o in self.obs)
        rep: dict = {"n": n, "positives": k, "rate": (k / n) if n else None, "threshold": self.threshold,
                     "credible_level": self.level, "min_observations": self.min_obs}
        if n:
            m, lo, hi = beta_interval(k, n, self.level)
            rep.update({"global_mean": m, "global_lower": lo, "global_upper": hi})
            rep["required_n_at_current_rate"] = required_sample_size(k / n, self.threshold, self.level) if k / n > self.threshold else None
        buckets: dict[str, dict] = {}
        for o in self.obs:
            b = buckets.setdefault(bucket_of(o.features), {"n": 0, "k": 0})
            b["n"] += 1
            b["k"] += o.label
        for b, v in buckets.items():
            m, lo, hi = beta_interval(v["k"], v["n"], self.level)
            v.update({"mean": m, "lower": lo, "upper": hi, "sufficient": v["n"] >= self.min_obs,
                      "status": ("OK" if lo >= self.threshold else "FIABILITÉ INSUFFISANTE") if v["n"] >= self.min_obs else INSUFFICIENT})
        rep["buckets"] = buckets
        # drift: predicted (bucket mean at the time) vs observed over the most recent window
        rec = self.obs[-recent:]
        if len(rec) >= 20:
            obs_rate = sum(o.label for o in rec) / len(rec)
            rep["recent"] = {"n": len(rec), "observed_rate": obs_rate}
            errs = [(o.net_after - o.net_expected) for o in rec if o.net_after is not None and o.net_expected is not None]
            if errs:
                rep["recent"]["mean_net_error"] = float(np.mean(errs))
                rep["recent"]["net_error_p10"] = float(np.percentile(errs, 10))
        self._maybe_fit_lr()
        rep["logistic"] = self._lr_metrics or {"status": "not fitted (needs >= 200 observations)"}
        rep["label"] = (
            INSUFFICIENT if n < self.min_obs else ("OK" if rep.get("global_lower", 0) >= self.threshold else "FIABILITÉ INSUFFISANTE")
        )
        return rep

    def drift_detected(self, recent: int = 50, tolerance: float = 0.15) -> tuple[bool, str]:
        """True when the recent observed success rate is far below what the model predicted for those cases."""
        rec = self.obs[-recent:]
        if len(rec) < 20:
            return False, "not enough recent data"
        observed = sum(o.label for o in rec) / len(rec)
        predicted = float(np.mean([o.features.get("p_at_decision", observed) for o in rec]))
        if predicted - observed > tolerance:
            return True, f"recent success {observed:.0%} vs predicted {predicted:.0%}"
        return False, f"recent success {observed:.0%} vs predicted {predicted:.0%}"


def _ece(p: np.ndarray, y: np.ndarray, bins: int = 5) -> float:
    edges = np.linspace(0, 1, bins + 1)
    ece = 0.0
    for i in range(bins):
        m = (p >= edges[i]) & (p < edges[i + 1] if i < bins - 1 else p <= edges[i + 1])
        if m.any():
            ece += m.mean() * abs(p[m].mean() - y[m].mean())
    return float(ece)


def features_of(opp) -> dict:  # opp: Opportunity
    """Decision-time feature vector (must not use any after-the-fact information)."""
    fb = opp.profit.fees
    gross = max(opp.profit.gross_profit, 1)
    amount_usd = opp.profit.amount_in / 10**opp.route.token.decimals
    return {
        "margin_bps": opp.profit.margin_bps,
        "spread_bps": opp.spread_bps,
        "hops": len(opp.route.hops),
        "gas_share": (fb.gas_cost_token + fb.flash_fee) / gross,
        "data_age_ms": opp.data_age_ms,
        "impact_bps": opp.profit.price_impact_bps,
        "log_amount_usd": math.log10(max(amount_usd, 1.0)),
        "route_class": "+".join(sorted({h.pool.kind.name for h in opp.route.hops})),
    }
