import pandas as pd

from ex1 import flag_provedor_email
from ex2 import extrair_flags_tempo
from ex3 import flag_eventos_comerciais
from ex4 import gerar_modelo_rfm
from ex5 import calcular_evolucao_sensor
from ex6 import razao_comprometimento_credito
from ex7 import preencher_nulos_com_alerta
from ex8 import calcular_ranking_interno
from ex9 import discretizar_turnos
from ex10 import identificar_aceleracao

print("--- 1. Domínio Corporativo ---")
df_emails = pd.DataFrame({'email': ['joao@gmail.com', 'maria@itau.com.br', 'contato@hotmail.com']})
print(flag_provedor_email(df_emails.copy(), 'email'))

print("\n--- 2. Decomposição de Tempo ---")
df_datas = pd.DataFrame({'acessos': ['2023-11-01', '2023-11-04']})
print(extrair_flags_tempo(df_datas.copy(), 'acessos'))

print("\n--- 3. Feriados e Black Friday ---")
df_eventos = pd.DataFrame({'transacao': ['2023-12-25', '2023-11-24', '2023-10-10']})
print(flag_eventos_comerciais(df_eventos.copy(), 'transacao'))

print("\n--- 4. Perfil RFM ---")
df_rfm_raw = pd.DataFrame({
    'id_cliente': [1, 1, 2, 2, 2],
    'data_compra': ['2023-10-01', '2023-11-01', '2023-01-15', '2023-06-20', '2023-11-01'],
    'valor': [100, 250, 50, 50, 100]
})
print(gerar_modelo_rfm(df_rfm_raw.copy(), 'id_cliente', 'data_compra', 'valor'))

print("\n--- 5. Sensores (Delta e Evolução) ---")
df_sensores = pd.DataFrame({'leitura_ontem': [100, 200, 50], 'leitura_hoje': [120, 150, 50]})
print(calcular_evolucao_sensor(df_sensores.copy(), 'leitura_ontem', 'leitura_hoje'))

print("\n--- 6. Razão de Comprometimento (Crédito) ---")
df_credito = pd.DataFrame({'divida': [3000, 5000, 0], 'renda_mensal': [10000, 5000, 2000]})
print(razao_comprometimento_credito(df_credito.copy(), 'divida', 'renda_mensal'))

print("\n--- 7. Indicador de Omissão (NaN) ---")
df_nulos = pd.DataFrame({'idade': [25, None, 30, pd.NA]})
print(preencher_nulos_com_alerta(df_nulos.copy(), 'idade', valor_default=0))

print("\n--- 8. Ranking Interno ---")
df_vendas = pd.DataFrame({'produto': ['A', 'B', 'C', 'D'], 'volume': [1000, 1000, 500, 1200]})
print(calcular_ranking_interno(df_vendas.copy(), 'volume'))

print("\n--- 9. Parser de Turnos ---")
df_horarios = pd.DataFrame({'hora_acesso': [3, 10, 15, 21, 0]})
print(discretizar_turnos(df_horarios.copy(), 'hora_acesso'))

print("\n--- 10. Delta do Delta (Aceleração) ---")
df_leitura = pd.DataFrame({'medicao': [10, 12, 16, 24]})
print(identificar_aceleracao(df_leitura.copy(), 'medicao'))