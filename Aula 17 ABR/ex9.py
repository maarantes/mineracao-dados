import pandas as pd

def discretizar_turnos(df, coluna_hora):
    bins = [-1, 5, 12, 18, 23]
    labels = ['Madrugada', 'Manha', 'Tarde', 'Noite']
    
    df['turno_comportamento'] = pd.cut(
        df[coluna_hora], 
        bins=bins, 
        labels=labels, 
        right=True
    )
    return df