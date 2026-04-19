import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Nome": ["Ana", "Bruno", None, "Carlos", "Diana"],
    "Email": ["ana@email.com", None, "bruno@email.com", None, "diana@email.com"],
    "Idade": [25, None, 30, 22, None],
    "Cidade": ["SP", "RJ", None, "MG", "SP"]
}

df = pd.DataFrame(dados)

faltantes = df.isna()

plt.figure(figsize=(8,4))
plt.imshow(faltantes, aspect="auto")
plt.colorbar(label="Valor ausente")

plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df)))

plt.title("Mapa de calor de valores ausentes")
plt.xlabel("Colunas")
plt.ylabel("Registros")

plt.savefig("heatmap_nan.png")