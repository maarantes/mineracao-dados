import pandas as pd
import random
from datetime import datetime, timedelta

df_usuarios = pd.DataFrame({
    "id_usuario": range(1, 11),
    "nome_usuario": [f"Funcionario {i}" for i in range(1, 11)],
    "departamento": random.choices(["Financeiro", "RH", "TI", "Vendas"], k=10)
})

df_equipamentos = pd.DataFrame({
    "id_equipamento": range(101, 111),
    "tipo_equipamento": random.choices(["Notebook", "Desktop"], k=10),
    "sistema_operacional": random.choices(["Windows 10", "Windows 11", "Linux"], k=10)
})

df_chamados = pd.DataFrame({
    "id_ticket": range(1001, 1021),
    "id_usuario": [random.randint(1, 10) for _ in range(20)],
    "id_equipamento": [random.randint(101, 110) for _ in range(20)],
    "horas_resolucao": [random.randint(1, 10) for _ in range(20)]
})

df_usuarios.to_csv("usuarios.csv", index=False)
df_equipamentos.to_csv("equipamentos.csv", index=False)
df_chamados.to_csv("chamados.csv", index=False)

print("Arquivos CSV de Helpdesk gerados com sucesso!")