import pandas as pd

dados = {
    "Paciente": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],
    "Altura_Metros": [1.65, 1.80, 170, 0.45, 2.10]
}

df = pd.DataFrame(dados)

altura_min = 0.5
altura_max = 2.5

alturas_impossiveis = df[
    (df["Altura_Metros"] < altura_min) |
    (df["Altura_Metros"] > altura_max)
]

print("Pacientes com alturas fisicamente impossíveis:")
print(alturas_impossiveis)