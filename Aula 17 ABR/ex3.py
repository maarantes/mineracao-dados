import pandas as pd
import holidays

def flag_eventos_comerciais(df, coluna_data):
    df[coluna_data] = pd.to_datetime(df[coluna_data])
    feriados_br = holidays.Brazil()
    
    def verificar_evento(data):
        if data in feriados_br:
            return 1
        if data.month == 11 and data.weekday() == 4 and 22 <= data.day <= 28:
            return 1
        return 0

    df['flag_pico_esperado'] = df[coluna_data].apply(verificar_evento)
    return df