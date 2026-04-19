import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

producao = [100, 102, 98, 105, 500, 101]

z_scores = zscore(producao)

dados_limpos = [p for p, z in zip(producao, z_scores) if abs(z) <= 2]

scaler = MinMaxScaler()
normalizado = scaler.fit_transform([[p] for p in dados_limpos])

print(normalizado)