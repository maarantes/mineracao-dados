import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Sensor_ID': ['A','A','A','A','B','B','B','B'],
    'Valor_Leitura': [10, 12, 11, 50, 20, 21, 19, 100]
})

def detectar_outliers(grupo):
    q1 = grupo['Valor_Leitura'].quantile(0.25)
    q3 = grupo['Valor_Leitura'].quantile(0.75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    grupo['Anomalia'] = (grupo['Valor_Leitura'] < limite_inferior) | (grupo['Valor_Leitura'] > limite_superior)
    return grupo

resultado = df.groupby('Sensor_ID', group_keys=False).apply(detectar_outliers)

print(resultado)