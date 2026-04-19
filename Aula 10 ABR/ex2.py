import numpy as np
from scipy.stats import zscore

voltagem = [3.3, 3.2, 3.3, 3.4, 3.3, 1.2, 3.2, 3.3]

z_scores = zscore(voltagem)

for v, z in zip(voltagem, z_scores):
    if z < -2.0:
        print(f"Falha de Energia! Voltagem: {v} (Z-Score: {z:.2f})")