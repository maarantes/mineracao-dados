import pandas as pd

dados = {
    "Item": ["Teclado", "Mouse", "Monitor", "Cabo HDMI"],
    "Data_Compra": ["2026-03-01", "2026-03-05", "2026-03-07", "2026-03-10"],
    "Data_Entrega": ["2026-03-03", "2026-03-02", "2026-03-09", "2026-03-08"]
}

df = pd.DataFrame(dados)

df["Data_Compra"] = pd.to_datetime(df["Data_Compra"])
df["Data_Entrega"] = pd.to_datetime(df["Data_Entrega"])

erros = df[df["Data_Entrega"] < df["Data_Compra"]]

print(erros)