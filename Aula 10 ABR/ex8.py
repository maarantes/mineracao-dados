import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.DataFrame({
    "idade": [18, 20, 19, 21, 22, 150],
    "horas_estudo": [10, 12, 9, 11, 13, 2],
    "nota": [7.5, 8.0, 7.0, 8.5, 9.0, 6.0]
})

modelo = IsolationForest(contamination=0.17, random_state=42)
df["Outlier"] = modelo.fit_predict(df)

anomalias = df[df["Outlier"] == -1]

print(anomalias)