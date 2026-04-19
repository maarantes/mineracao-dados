import pandas as pd

def razao_comprometimento_credito(df, col_divida, col_renda):
    """
    Justificativa: Variáveis absolutas de dívida ou renda carregam ruídos de 
    escala (ex: dívida de 10k para quem ganha 5k vs 100k). A proporção 
    captura a pressão financeira de vdd e isola a capacidade de pagamento, 
    criando uma fronteira de decisão direta e linear para o algoritmo.
    """
    df['razao_comprometimento'] = df[col_divida] / df[col_renda].replace(0, pd.NA)
    return df