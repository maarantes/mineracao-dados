import pandas as pd

dados = {
    "Placa_Veiculo": [
        "ABC1234",
        "XYZ987",
        "ABCD123",
        "12345678",
        "QWE1234"
    ]
}

df = pd.DataFrame(dados)

placas_incorretas = df[df["Placa_Veiculo"].str.len() != 7]

print("Placas com tamanho incorreto:")
print(placas_incorretas)