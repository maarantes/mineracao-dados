import pandas as pd
import os

caminho = os.path.join(os.path.dirname(__file__), "dados_sensores.csv")
df = pd.read_csv(caminho)

print("---------- Leituras ausentes ----------")
print(df.isna().sum())

df = df.fillna(df.median(numeric_only=True))

print("\n---------- DataFrame após preenchimento ----------")
print(df)