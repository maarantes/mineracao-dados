import pandas as pd
import random

df_clientes = pd.DataFrame({
    "id_cliente": [1,2,3,4,5,6],
    "nome_cliente": ["Ana","Bruno","Carlos","Daniela","Eduardo","Fernanda"],
    "estado": ["SP","RJ","MG","SP","RS","BA"]
})

df_produtos = pd.DataFrame({
    "id_produto": [1,2,3,4],
    "nome_produto": ["SSD 1TB","Placa de Vídeo","Memória RAM 16GB","Fonte 600W"],
    "preco": [450, 2500, 320, 380]
})

df_vendas = pd.DataFrame({
    "id_venda": range(1,21),
    "id_cliente": [random.randint(1,6) for _ in range(20)],
    "id_produto": [random.randint(1,4) for _ in range(20)],
    "quantidade": [random.randint(1,5) for _ in range(20)]
})

df_clientes.to_csv("clientes.csv", index=False)
df_produtos.to_csv("produtos.csv", index=False)
df_vendas.to_csv("vendas.csv", index=False)