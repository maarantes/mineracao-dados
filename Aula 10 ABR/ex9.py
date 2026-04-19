from sklearn.preprocessing import MinMaxScaler

pressao = [[100], [200], [500]]

scaler = MinMaxScaler()
normalizado = scaler.fit_transform(pressao)

print(normalizado)