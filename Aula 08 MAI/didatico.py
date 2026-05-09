import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

np.random.seed(42)

print("=" * 60)
print("  PASSO 1 — Criando a Matriz Redundante")
print("=" * 60)

coluna_base = np.random.uniform(1, 10, size=100)

coluna_a = coluna_base + np.random.normal(0, 0.1, 100)
coluna_b = coluna_base * 2 + np.random.normal(0, 0.2, 100)

X = np.column_stack([coluna_a, coluna_b])

print(f"\nShape da Matriz Original: {X.shape}")
print(f"  → {X.shape[0]} amostras, {X.shape[1]} colunas (features)\n")

correlacao = np.corrcoef(X[:, 0], X[:, 1])[0, 1]
print(f"Correlação entre Coluna A e Coluna B: {correlacao:.4f}")
print("  → Correlação próxima de 1.0 = ALTÍSSIMA REDUNDÂNCIA\n")

print("=" * 60)
print("  PASSO 2 — Matriz de Covariância")
print("=" * 60)

X_scaled = StandardScaler().fit_transform(X)
cov_matrix = np.cov(X_scaled.T)

print("\nMatriz de Covariância (após padronização):")
print(np.array2string(cov_matrix, precision=4))
print("\n  → Valores fora da diagonal altos = redundância detectada!\n")

print("=" * 60)
print("  PASSO 3 — Autovetores e Autovalores")
print("=" * 60)

autovalores, autovetores = np.linalg.eig(cov_matrix)

print("\nAutovalores (variância explicada por cada direção):")

for i, val in enumerate(autovalores):
    pct = val / autovalores.sum() * 100
    print(f"  λ{i+1} = {val:.4f}  →  {pct:.1f}% da variância total")

print("\nAutovetores (direções principais no espaço dos dados):")

for i, vec in enumerate(autovetores.T):
    print(f"  PC{i+1}: {vec}")

print("\n  → PC1 concentra quase TODA a variância")
print("  → PC2 captura apenas o ruído residual\n")

print("=" * 60)
print("  PASSO 4 — Aplicando PCA: 2D → 1D")
print("=" * 60)

pca = PCA(n_components=1)
X_pca = pca.fit_transform(X_scaled)

print(f"\nShape ANTES do PCA: {X_scaled.shape}  (2 colunas)")
print(f"Shape APÓS  o PCA: {X_pca.shape}   (1 coluna — PC1)")
print(f"\nVariância explicada por PC1: {pca.explained_variance_ratio_[0] * 100:.2f}%")
print("  → Com UMA única componente, preservamos quase toda a informação!\n")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.patch.set_facecolor("#0f0f1a")

for ax in axes:
    ax.set_facecolor("#1a1a2e")

cor_pontos = "#00d4ff"
cor_pc1 = "#ff6b6b"

axes[0].scatter(
    X[:, 0],
    X[:, 1],
    color=cor_pontos,
    alpha=0.6,
    s=40,
    edgecolors="white",
    linewidths=0.3
)

axes[0].set_title(
    "Dados Originais\n(2 colunas redundantes)",
    color="white",
    fontsize=11,
    fontweight="bold"
)

axes[0].set_xlabel("Coluna A (comprimento)", color="#aaaacc")
axes[0].set_ylabel("Coluna B (largura ≈ 2×A)", color="#aaaacc")
axes[0].tick_params(colors="#aaaacc")

for spine in axes[0].spines.values():
    spine.set_edgecolor("#333355")

axes[0].text(
    0.05,
    0.92,
    f"Correlação: {correlacao:.3f}",
    transform=axes[0].transAxes,
    color="#ffd700",
    fontsize=9,
    bbox=dict(boxstyle="round", facecolor="#2a2a4a", alpha=0.8)
)

axes[1].scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    color=cor_pontos,
    alpha=0.5,
    s=40,
    edgecolors="white",
    linewidths=0.3
)

vec = pca.components_[0]
escala = 2.5

axes[1].annotate(
    "",
    xy=(vec[0] * escala, vec[1] * escala),
    xytext=(-vec[0] * escala, -vec[1] * escala),
    arrowprops=dict(arrowstyle="<->", color=cor_pc1, lw=2.5)
)

axes[1].text(
    vec[0] * escala * 1.05,
    vec[1] * escala * 1.05,
    "PC1\n(máx variância)",
    color=cor_pc1,
    fontsize=9,
    fontweight="bold"
)

axes[1].set_title(
    "Direção do PC1\n(autovetor principal)",
    color="white",
    fontsize=11,
    fontweight="bold"
)

axes[1].set_xlabel("Coluna A (padronizada)", color="#aaaacc")
axes[1].set_ylabel("Coluna B (padronizada)", color="#aaaacc")
axes[1].tick_params(colors="#aaaacc")

for spine in axes[1].spines.values():
    spine.set_edgecolor("#333355")

axes[1].axhline(0, color="#333355", lw=0.5)
axes[1].axvline(0, color="#333355", lw=0.5)

axes[2].scatter(
    X_pca[:, 0],
    np.zeros_like(X_pca[:, 0]),
    color=cor_pc1,
    alpha=0.7,
    s=50,
    edgecolors="white",
    linewidths=0.3
)

axes[2].set_title(
    "Após PCA: 1 Dimensão\n(PC1 — fusão abstrata)",
    color="white",
    fontsize=11,
    fontweight="bold"
)

axes[2].set_xlabel("PC1 (componente principal)", color="#aaaacc")
axes[2].set_yticks([])
axes[2].tick_params(colors="#aaaacc")

for spine in axes[2].spines.values():
    spine.set_edgecolor("#333355")

axes[2].text(
    0.05,
    0.85,
    f"Variância preservada:\n{pca.explained_variance_ratio_[0] * 100:.1f}%",
    transform=axes[2].transAxes,
    color="#00ff88",
    fontsize=10,
    bbox=dict(boxstyle="round", facecolor="#0a2a1a", alpha=0.85)
)

fig.suptitle(
    "IPE 4 — PCA | Script 1: Exemplo Didático (Redundância 2D → 1D)",
    color="white",
    fontsize=13,
    fontweight="bold",
    y=1.02
)

plt.tight_layout()

plt.savefig(
    "script1_didatico.png",
    dpi=150,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.close()

print("=" * 60)
print("  RESULTADO FINAL")
print("=" * 60)

print(f"\n  • Dimensões originais : 2 colunas")
print(f"  • Dimensões após PCA  : 1 componente (PC1)")
print(f"  • Variância preservada: {pca.explained_variance_ratio_[0] * 100:.2f}%")
print(f"  • Gráfico salvo em    : script1_didatico.png")

print("\n  CONCLUSÃO: Colunas redundantes são COLAPSADAS pelo PCA")
print("  em uma única direção sem perda relevante de informação.\n")