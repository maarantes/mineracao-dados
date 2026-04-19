import pandas as pd

def calcular_ranking_interno(df, col_volume_vendas):
    df['ranking_forca_relativa'] = df[col_volume_vendas].rank(method='dense', ascending=False).astype(int)
    return df