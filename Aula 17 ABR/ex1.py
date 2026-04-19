import pandas as pd

def flag_provedor_email(df, coluna_email):
    provedores_comuns = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'uol.com.br']
    df['dominio'] = df[coluna_email].str.split('@').str[1].str.lower()
    df['flag_infra_empresarial'] = (~df['dominio'].isin(provedores_comuns)).astype(int)
    return df