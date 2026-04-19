import pandas as pd

def gerar_modelo_rfm(df, col_cliente, col_data, col_valor):
    df[col_data] = pd.to_datetime(df[col_data])
    data_referencia = df[col_data].max()
    
    df_rfm = df.groupby(col_cliente).agg({
        col_data: lambda x: (data_referencia - x.max()).days,
        col_cliente: 'count',
        col_valor: 'sum'
    }).rename(columns={
        col_data: 'Recencia_dias',
        col_cliente: 'Frequencia_pedidos',
        col_valor: 'Valor_Monetario_Total'
    }).reset_index()
    
    return df_rfm