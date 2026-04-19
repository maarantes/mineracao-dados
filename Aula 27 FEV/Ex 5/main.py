import pandas as pd
import random

df_motoristas = pd.DataFrame({
    "id_motorista": range(1, 6),
    "nome_motorista": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
})

df_veiculos = pd.DataFrame({
    "id_veiculo": range(101, 106),
    "tipo_veiculo": ["Caminhão", "Van", "Caminhão", "Van", "Carro"]
})

df_entregas = pd.DataFrame({
    "id_entrega": range(1, 21),
    "id_motorista": [random.randint(1, 5) for _ in range(20)],
    "id_veiculo": [random.randint(101, 105) for _ in range(20)],
    "distancia_km": [random.randint(50, 500) for _ in range(20)]
})

df_motoristas.to_csv("motoristas.csv", index=False)
df_veiculos.to_csv("veiculos.csv", index=False)
df_entregas.to_csv("entregas.csv", index=False)

print("Arquivos CSV de Logística gerados com sucesso!")