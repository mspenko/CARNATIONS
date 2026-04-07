
import pandas as pd, numpy as np
df = pd.read_csv("../datasets/week5_multi_receiver.csv")
wide = df.pivot(index="t_s", columns="receiver_id", values=["true_x_m","true_y_m","meas_x_m","meas_y_m","spoof_active"])
bx = wide["meas_x_m"]["B"] - wide["meas_x_m"]["A"]
by = wide["meas_y_m"]["B"] - wide["meas_y_m"]["A"]
true_bx = wide["true_x_m"]["B"] - wide["true_x_m"]["A"]
true_by = wide["true_y_m"]["B"] - wide["true_y_m"]["A"]
baseline_error = np.sqrt((bx - true_bx)**2 + (by - true_by)**2)
truth = wide["spoof_active"]["A"].astype(int)
pre = baseline_error[truth == 0]
threshold = pre.mean() + 3*pre.std()
detected = (baseline_error > threshold).astype(int)
tp = int(((detected == 1) & (truth == 1)).sum())
fp = int(((detected == 1) & (truth == 0)).sum())
print({"threshold": float(threshold), "tp": tp, "fp": fp})
