from sklearn.ensemble import IsolationForest

dados = [[8, 2], [7, 4], [9, 1], [8, 3], [2, 25], [9, 25]]

modelo = IsolationForest(contamination=0.33, random_state=42)
predicoes = modelo.fit_predict(dados)

print(predicoes)

for ponto, pred in zip(dados, predicoes):
    print(ponto, "->", pred)