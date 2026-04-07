
import pandas as pd
df = pd.read_csv("../datasets/week2_error_signatures.csv")
signals = [c for c in df.columns if c != "t_s"]
summary = []
for c in signals:
    s = df[c]
    summary.append({"signal": c, "mean_m": s.mean(), "std_m": s.std(), "max_abs_m": s.abs().max()})
print(pd.DataFrame(summary))
