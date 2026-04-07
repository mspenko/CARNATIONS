
import numpy as np, pandas as pd
df = pd.read_csv("../datasets/week3_residual_detection.csv")
agg = df.groupby("t_s").agg(
    mean_abs_residual_m=("residual_m", lambda s: np.mean(np.abs(s))),
    rms_residual_m=("residual_m", lambda s: np.sqrt(np.mean(np.square(s)))),
    truth_spoof=("spoof_active", "max")
).reset_index()
pre = agg.loc[agg["truth_spoof"] == 0, "rms_residual_m"]
threshold = pre.mean() + 3 * pre.std()
agg["detected"] = (agg["rms_residual_m"] > threshold).astype(int)
tp = int(((agg["detected"] == 1) & (agg["truth_spoof"] == 1)).sum())
fp = int(((agg["detected"] == 1) & (agg["truth_spoof"] == 0)).sum())
fn = int(((agg["detected"] == 0) & (agg["truth_spoof"] == 1)).sum())
first_truth = agg.loc[agg["truth_spoof"] == 1, "t_s"].min()
first_det = agg.loc[agg["detected"] == 1, "t_s"].min()
print({"threshold": float(threshold), "tp": tp, "fp": fp, "fn": fn, "delay_s": int(first_det - first_truth)})
