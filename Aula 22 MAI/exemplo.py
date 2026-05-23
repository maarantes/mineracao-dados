import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# ===========================
# 1. CARREGAMENTO DOS DADOS
# ===========================
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_do_csv = os.path.join(diretorio_do_script, 'AmesHousing.csv')
df = pd.read_csv(caminho_do_csv)

TARGET = 'SalePrice'

# ==============================================
# 2. EDA E HIGIENIZAÇÃO DE DADOS (Requisito 1)
# ==============================================
print("--- Iniciando Análise Exploratória e Tratamento de Outliers ---")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Gr Liv Area', y=TARGET, alpha=0.6, color='blue')
plt.title('Dispersão: Área Útil vs Preço de Venda (Antes da Limpeza)')
plt.xlabel('Área Útil Acima do Solo (sq ft)')
plt.ylabel('Preço de Venda ($)')
plt.savefig('grafico_dispersao.png', bbox_inches='tight')

outliers_condition = (df['Gr Liv Area'] > 4000) & (df[TARGET] < 300000)
df_clean = df.drop(df[outliers_condition].index)

print(f"Linhas antes da limpeza: {df.shape[0]}")
print(f"Linhas após remoção de outliers: {df_clean.shape[0]}\n")

X = df_clean.drop(columns=[TARGET, 'Order', 'PID']) 
y = df_clean[TARGET]

# =============================================
# 3. PIPELINES DE TRANSFORMAÇÃO (Requisito 2)
# =============================================
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object', 'string']).columns

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# ===================================
# 4. DIVISÃO DE DADOS (Requisito 3)
# ===================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ========================================
# 5. TREINAMENTO PREDITIVO (Requisito 4)
# ========================================
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42, max_depth=15))
])

print("Treinando o modelo (isso pode levar alguns segundos)...")
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# =========================================================
# 6. AVALIAÇÃO NUMÉRICA DUPLA E DIAGNÓSTICO (Requisito 5)
# =========================================================
print("\n--- Diagnóstico de Erros e Generalização ---")

mae_train = mean_absolute_error(y_train, y_pred_train)
r2_train = r2_score(y_train, y_pred_train)

mae_test = mean_absolute_error(y_test, y_pred_test)
r2_test = r2_score(y_test, y_pred_test)

print("RESULTADOS NOS DADOS DE TREINO:")
print(f"MAE:  ${mae_train:,.2f}")
print(f"R²:   {r2_train:.4f} ({(r2_train*100):.1f}% da variância explicada)")

print("\nRESULTADOS NOS DADOS DE TESTE:")
print(f"MAE:  ${mae_test:,.2f}")
print(f"R²:   {r2_test:.4f} ({(r2_test*100):.1f}% da variância explicada)")

print("\nANÁLISE FINAL:")
if r2_train - r2_test > 0.10:
    print("O modelo apresenta sinais de OVERFITTING. O R² no treino está significativamente maior que no teste.")
    print("Isso indica que o algoritmo decorou o ruído ao invés de aprender as relações estruturais.")
else:
    print("O modelo apresenta boa GENERALIZAÇÃO. As métricas de treino e teste estão equilibradas, indicando baixo Overfitting.")