
import numpy as np, pandas as pd
from scipy.optimize import least_squares

df = pd.read_csv("../datasets/week1_pseudorange_static.csv")
sat_xyz = df[["sat_x_m","sat_y_m","sat_z_m"]].to_numpy()
rho_meas = df["pseudorange_m"].to_numpy()

def pseudorange_residuals(state, sat_xyz, rho_meas):
    x, y, z, b = state
    predicted = np.linalg.norm(sat_xyz - np.array([x, y, z]), axis=1) + b
    return rho_meas - predicted

result = least_squares(pseudorange_residuals, np.zeros(4), args=(sat_xyz, rho_meas))
print("Estimated [x, y, z, b] =", result.x)
print("Residual norm =", np.linalg.norm(result.fun))
