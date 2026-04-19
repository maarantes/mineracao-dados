import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({
    "saldo": [1000000, 1000010],
    "risco": [0.1, 0.9]
})

scaler = MinMaxScaler()
df_normalizado = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print(df_normalizado)