import pandas as pd

dados = {
    "Componente": ["Resistor", "Capacitor", "Transistor", "LED", "Diodo"],
    "Quantidade_Estoque": [150, -5, 42.5, 300, 0]
}

df = pd.DataFrame(dados)

erros = df[
    (df["Quantidade_Estoque"] < 0) |
    (df["Quantidade_Estoque"] % 1 != 0)
]

print("Componentes com falhas de integridade matemática:")
print(erros)