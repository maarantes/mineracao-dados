import pandas as pd

def preencher_nulos_com_alerta(df, coluna, valor_default=0):
    df[f'flag_omissao_{coluna}'] = df[coluna].isna().astype(int)
    df[coluna] = df[coluna].fillna(valor_default)
    return df