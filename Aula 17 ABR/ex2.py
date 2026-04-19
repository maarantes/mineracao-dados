import pandas as pd

def extrair_flags_tempo(df, coluna_data):
    df[coluna_data] = pd.to_datetime(df[coluna_data])
    df['mes_acesso'] = df[coluna_data].dt.month
    df['dia_semana'] = df[coluna_data].dt.day_name()
    df['flag_fim_de_semana'] = (df[coluna_data].dt.dayofweek >= 5).astype(int)
    return df