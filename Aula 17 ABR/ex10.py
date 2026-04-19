import pandas as pd

def identificar_aceleracao(df, coluna_leitura):
    df['delta'] = df[coluna_leitura].diff()
    df['delta_delta'] = df['delta'].diff()
    df['alerta_crescimento_exponencial'] = ((df['delta'] > 0) & (df['delta_delta'] > 0)).astype(int)
    return df