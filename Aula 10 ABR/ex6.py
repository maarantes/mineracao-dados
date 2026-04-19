import numpy as np
from sklearn.ensemble import IsolationForest

np.random.seed(42)

normais = np.random.normal(loc=0, scale=1, size=(1000, 2))

anomalias = np.random.uniform(low=10, high=15, size=(50, 2))

dados = np.vstack([normais, anomalias])

modelo_5 = IsolationForest(contamination=0.05, random_state=42)
pred_5 = modelo_5.fit_predict(dados)

anomalias_5 = np.sum(pred_5 == -1)

modelo_20 = IsolationForest(contamination=0.20, random_state=42)
pred_20 = modelo_20.fit_predict(dados)

anomalias_20 = np.sum(pred_20 == -1)

print(f"Anomalias detectadas (contamination=0.05): {anomalias_5}")
print(f"Anomalias detectadas (contamination=0.20): {anomalias_20}")