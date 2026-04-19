import numpy as np
from scipy.stats import zscore

medidas = [10, 12, 11, 10, 10000]

media = np.mean(medidas)
desvio = np.std(medidas)

z_scores = zscore(medidas)

z_10000 = z_scores[-1]

print(f"Média: {media:.2f}")
print(f"Desvio padrão: {desvio:.2f}")
print(f"Z-Score do 10000: {z_10000:.2f}")

if abs(z_10000) > 3:
    print("Seria considerado outlier pela regra dos 3 sigmas")
else:
    print("NÃO foi considerado outlier pela regra dos 3 sigmas")