import pandas as pd
from datetime import datetime

dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Diana"],
    "Ano_Nascimento": [2000, 1998, 2005, 2003],
    "Idade_Declarada": [25, 30, 20, 23]
}

df = pd.DataFrame(dados)

ano_atual = datetime.now().year

df["Idade_Real"] = ano_atual - df["Ano_Nascimento"]

inconsistencias = df[df["Idade_Real"] != df["Idade_Declarada"]]

print("Registros com inconsistência de idade:")
print(inconsistencias)