import pandas as pd
import os

caminho = os.path.join(os.path.dirname(__file__), "dados_sensores.csv")
df = pd.read_csv(caminho)

df = df.fillna(df.median(numeric_only=True))

q1_temp = df["temperatura_celsius"].quantile(0.25)
q3_temp = df["temperatura_celsius"].quantile(0.75)
iqr_temp = q3_temp - q1_temp
li_temp = q1_temp - 1.5 * iqr_temp
ls_temp = q3_temp + 1.5 * iqr_temp

q1_press = df["pressao_psi"].quantile(0.25)
q3_press = df["pressao_psi"].quantile(0.75)
iqr_press = q3_press - q1_press
li_press = q1_press - 1.5 * iqr_press
ls_press = q3_press + 1.5 * iqr_press

df_validado = df[
    (df["temperatura_celsius"] >= li_temp) & (df["temperatura_celsius"] <= ls_temp) &
    (df["pressao_psi"] >= li_press) & (df["pressao_psi"] <= ls_press)
]

df_validado.to_csv("dados_validados.csv", index=False, sep=';', decimal=',')

print("Arquivo dados_validados.csv gerado com sucesso!")