
import numpy as np, pandas as pd
df = pd.read_csv("../datasets/week4_gnss_imu_fusion.csv")
dt = 1.0
A = np.array([[1, dt],[0, 1]])
B = np.array([[0.5*dt**2],[dt]])
H = np.array([[1, 0]])
Q = np.array([[0.5, 0.0],[0.0, 0.5]])
R = np.array([[6.0]])
xhat = np.zeros((len(df), 2))
P = np.eye(2)
for k in range(1, len(df)):
    u = df.loc[k-1, "imu_acc_mps2"]
    x_pred = A @ xhat[k-1] + (B.flatten() * u)
    P_pred = A @ P @ A.T + Q
    z = np.array([[df.loc[k, "gnss_pos_meas_m"]]])
    y = z - H @ x_pred.reshape(-1,1)
    S = H @ P_pred @ H.T + R
    K = P_pred @ H.T @ np.linalg.inv(S)
    x_post = x_pred.reshape(-1,1) + K @ y
    P = (np.eye(2) - K @ H) @ P_pred
    xhat[k] = x_post.flatten()
df["fused_error_m"] = xhat[:,0] - df["true_x_m"]
df["gnss_error_m"] = df["gnss_pos_meas_m"] - df["true_x_m"]
pre = df["spoof_active"] == 0
post = df["spoof_active"] == 1
metrics = {
    "gnss_rmse_pre": float(np.sqrt(np.mean(df.loc[pre, "gnss_error_m"]**2))),
    "gnss_rmse_post": float(np.sqrt(np.mean(df.loc[post, "gnss_error_m"]**2))),
    "fused_rmse_pre": float(np.sqrt(np.mean(df.loc[pre, "fused_error_m"]**2))),
    "fused_rmse_post": float(np.sqrt(np.mean(df.loc[post, "fused_error_m"]**2))),
}
print(metrics)
