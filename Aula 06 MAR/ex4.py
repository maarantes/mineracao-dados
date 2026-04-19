import pandas as pd

dados = {
    "Sistema_Operacional": [
        "Ubuntu","Ubuntu","Ubuntu","Debian", "Ubuntu","Armbian","Ubuntu","Armbian","Debian",
        "Ubuntu","Ubuntu","Ubuntu","Debian", "Ubuntu","Armbian","Ubuntu","Armbian","Debian",
        "Armbian","Ubuntu","Ubuntu","Ubntu","Debia"
    ]
}

df = pd.DataFrame(dados)

proporcoes = df["Sistema_Operacional"].value_counts(normalize=True)

print("Proporção de cada categoria:")
print(proporcoes)

raras = proporcoes[proporcoes < 0.05]

print("\nCategorias com menos de 5% dos dados:")
print(raras)