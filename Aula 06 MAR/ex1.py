import pandas as pd

dados = {
    "Sensor_ID": [1, 2, 3, 4, 5],
    "Temperatura_C": ["23.5", "25.1", "falha_sinal", "22.8", "erro"]
}

df = pd.DataFrame(dados)

df["Temperatura_C_convertida"] = pd.to_numeric(df["Temperatura_C"], errors="coerce")

falhas = df[df["Temperatura_C_convertida"].isna()]

print(falhas)