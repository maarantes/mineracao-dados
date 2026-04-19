import numpy as np

tempos = np.array([12, 15, 14, 13, 16, 12, 14, 150, 13, 15])

p25 = np.percentile(tempos, 25)
p50 = np.percentile(tempos, 50)
p75 = np.percentile(tempos, 75)

print("Percentil 25:", p25)
print("Percentil 50 (mediana):", p50)
print("Percentil 75:", p75)

iqr = p75 - p25

limite_inferior = p25 - 1.5 * iqr
limite_superior = p75 + 1.5 * iqr

print("IQR:", iqr)
print("Limite Inferior:", limite_inferior)
print("Limite Superior:", limite_superior)