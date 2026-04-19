import pandas as pd
import random
from datetime import datetime, timedelta

df_ambientes = pd.DataFrame({
    "id_ambiente": [1, 2, 3],
    "nome_setor": ["Caldeira", "Estacionamento", "Escritório"]
})

df_dispositivos = pd.DataFrame({
    "id_dispositivo": [101, 102, 103, 104],
    "tipo_dispositivo": ["RPI", "ESP32", "Orange Pi", "ESP32"],
    "id_ambiente": [1, 2, 3, 1]
})

fim = datetime.now()
inicio = fim - timedelta(days=365)

datas = []
for _ in range(50):
    data_aleatoria = inicio + timedelta(seconds=random.randint(0, int((fim - inicio).total_seconds())))
    datas.append(data_aleatoria)

datas.sort()

df_telemetria = pd.DataFrame({
    "id_telemetria": range(1, 51),
    "id_dispositivo": [random.choice([101, 102, 103, 104]) for _ in range(50)],
    "data_hora": datas,
    "temperatura_c": [round(random.uniform(20.0, 45.0), 2) for _ in range(50)],
    "umidade_perc": [round(random.uniform(30.0, 80.0), 2) for _ in range(50)]
})

df_ambientes.to_csv("ambientes.csv", index=False)
df_dispositivos.to_csv("dispositivos.csv", index=False)
df_telemetria.to_csv("telemetria.csv", index=False)

print("Arquivos CSV de IoT gerados com sucesso com datas distribuídas!")