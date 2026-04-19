from sklearn.preprocessing import MinMaxScaler

temps = [[-20], [-10], [0], [20]]

scaler = MinMaxScaler()
normalizado = scaler.fit_transform(temps)

print(normalizado)