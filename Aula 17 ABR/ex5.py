import pandas as pd

def calcular_evolucao_sensor(df, sensor_t1, sensor_t2):
    df['delta_bruto'] = df[sensor_t2] - df[sensor_t1]    
    df['evolucao_pct'] = (df['delta_bruto'] / df[sensor_t1].replace(0, pd.NA)).astype(float)
    
    def tendencia(delta):
        if pd.isna(delta): return 'Indisponível'
        if delta > 0: return 'Crescimento'
        if delta < 0: return 'Queda'
        return 'Estabilidade'
        
    df['tendencia_atual'] = df['delta_bruto'].apply(tendencia)
    return df