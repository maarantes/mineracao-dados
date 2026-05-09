import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

print("=" * 60)
print("  PASSO 1 — Carregando o Dataset")
print("=" * 60)

wine = load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names
class_names = wine.target_names

print(f"\nDataset: Wine Recognition (UCI / sklearn)")
print(f"  • Amostras  : {X.shape[0]}")
print(f"  • Features  : {X.shape[1]}  ← alta dimensionalidade!")
print(f"  • Classes   : {list(class_names)}")

print(f"\nFeatures originais (13 colunas):")

for i, name in enumerate(feature_names, 1):
    print(f"  {i:2d}. {name}")

print("\n" + "=" * 60)
print("  PASSO 2 — Padronização com StandardScaler")
print("=" * 60)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"\nAntes do scaler — Média e Desvio de 'alcohol':")
print(f"  Média : {X[:, 0].mean():.4f}")
print(f"  Desvio: {X[:, 0].std():.4f}")

print(f"\nApós o scaler  — Média e Desvio de 'alcohol':")
print(f"  Média : {X_scaled[:, 0].mean():.6f}  ≈ 0")
print(f"  Desvio: {X_scaled[:, 0].std():.6f}  ≈ 1")

print(
    "\n  → Todas as 13 colunas agora têm mesma escala.\n"
    "    Sem isso, features com valores grandes dominam o PCA!"
)

print("\n" + "=" * 60)
print("  PASSO 3 — Matriz de Covariância (13×13)")
print("=" * 60)

cov = np.cov(X_scaled.T)

print(f"\nShape da Matriz de Covariância: {cov.shape}")
print("  (mostrando apenas o canto superior-esquerdo 4×4)")
print(np.array2string(cov[:4, :4], precision=3))

print("\n  → Valores altos fora da diagonal = correlação/redundância")

print("\n" + "=" * 60)
print("  PASSO 4 — Variância Explicada por cada PC")
print("=" * 60)

pca_full = PCA(n_components=13)
pca_full.fit(X_scaled)

print("\n  PC  | Variância Explicada | Acumulada")
print("  ––|———————————————|––––––––––")

acumulada = 0

for i, vr in enumerate(pca_full.explained_variance_ratio_, 1):
    acumulada += vr
    barra = "█" * int(vr * 40)
    print(f"  PC{i:02d}| {vr*100:5.1f}%  {barra:<20} | {acumulada*100:.1f}%")

print(
    f"\n  → PC1 + PC2 já explicam "
    f"{pca_full.explained_variance_ratio_[:2].sum()*100:.1f}% da variância total!"
)

print("  → Reduzir de 13 para 2 dimensões é VIÁVEL!\n")

print("=" * 60)
print("  PASSO 5 — Aplicando PCA com n_components=2")
print("=" * 60)

pca2 = PCA(n_components=2)
X_pca2 = pca2.fit_transform(X_scaled)

print(f"\nShape ANTES : {X_scaled.shape}   (13 features)")
print(f"Shape DEPOIS: {X_pca2.shape}    (2 componentes principais)")

print(f"\nPC1 explica: {pca2.explained_variance_ratio_[0]*100:.2f}%")
print(f"PC2 explica: {pca2.explained_variance_ratio_[1]*100:.2f}%")

print(
    f"Total      : "
    f"{pca2.explained_variance_ratio_.sum()*100:.2f}% da variância preservada"
)

print("\n  ATENÇÃO — Perda de Interpretabilidade:")
print("  PC1 é uma COMBINAÇÃO LINEAR das 13 features originais:")

for fname, coef in zip(feature_names, pca2.components_[0]):
    sinal = "+" if coef >= 0 else "-"
    print(f"    {sinal} {abs(coef):.4f} × {fname}")

print("\n  → PC1 não é mais 'alcohol' nem 'proline'.")
print("  → É uma fusão matemática abstrata focada na VARIÂNCIA.\n")

cores = ["#ff6b6b", "#00d4ff", "#00ff88"]
marker = ["o", "s", "D"]

fig = plt.figure(figsize=(18, 10))
fig.patch.set_facecolor("#0d0d1a")

ax_scatter = fig.add_subplot(1, 3, (1, 2))
ax_scree = fig.add_subplot(2, 3, 3)
ax_loadings = fig.add_subplot(2, 3, 6)

ax_scatter.set_facecolor("#1a1a2e")

for i, (classe, nome) in enumerate(zip(np.unique(y), class_names)):
    mask = y == classe

    ax_scatter.scatter(
        X_pca2[mask, 0],
        X_pca2[mask, 1],
        c=cores[i],
        marker=marker[i],
        s=80,
        alpha=0.85,
        edgecolors="white",
        linewidths=0.4,
        label=nome.replace("_", " ").title()
    )

ax_scatter.set_xlabel(
    "PC1  (componente principal 1 — abstrata)",
    color="#aaaacc",
    fontsize=11
)

ax_scatter.set_ylabel(
    "PC2  (componente principal 2 — abstrata)",
    color="#aaaacc",
    fontsize=11
)

ax_scatter.set_title(
    "Scatter Plot 2D após PCA\n"
    f"13 features originais → 2 componentes  "
    f"({pca2.explained_variance_ratio_.sum()*100:.1f}% variância preservada)",
    color="white",
    fontsize=12,
    fontweight="bold"
)

ax_scatter.tick_params(colors="#aaaacc")

for spine in ax_scatter.spines.values():
    spine.set_edgecolor("#2a2a4a")

ax_scatter.axhline(0, color="#2a2a4a", lw=0.8, ls="--")
ax_scatter.axvline(0, color="#2a2a4a", lw=0.8, ls="--")

ax_scatter.legend(
    fontsize=10,
    facecolor="#1a1a2e",
    labelcolor="white",
    edgecolor="#333355",
    markerscale=1.2
)

ax_scatter.text(
    0.02,
    0.02,
    "As classes permanecem SEPARÁVEIS\nmesmo após compressão extrema!",
    transform=ax_scatter.transAxes,
    color="#ffd700",
    fontsize=9,
    va="bottom",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#1a1000", alpha=0.9)
)

ax_scree.set_facecolor("#1a1a2e")

pcs = [f"PC{i}" for i in range(1, 14)]
var = pca_full.explained_variance_ratio_ * 100
acum = np.cumsum(var)

bar_colors = ["#ff6b6b" if i < 2 else "#4a4a6a" for i in range(13)]

ax_scree.bar(
    pcs,
    var,
    color=bar_colors,
    edgecolor="white",
    linewidth=0.4,
    alpha=0.9
)

ax_scree2 = ax_scree.twinx()

ax_scree2.plot(
    pcs,
    acum,
    color="#ffd700",
    marker="o",
    markersize=4,
    lw=1.5,
    zorder=5
)

ax_scree2.axhline(
    pca2.explained_variance_ratio_.sum() * 100,
    color="#00ff88",
    ls="--",
    lw=1.2,
    alpha=0.7
)

ax_scree2.set_ylim(0, 105)
ax_scree2.tick_params(colors="#ffd700", labelsize=7)

ax_scree2.set_ylabel(
    "Variância Acumulada (%)",
    color="#ffd700",
    fontsize=8
)

ax_scree.set_title(
    "Scree Plot",
    color="white",
    fontsize=10,
    fontweight="bold"
)

ax_scree.set_xlabel("Componentes", color="#aaaacc", fontsize=8)
ax_scree.set_ylabel("Variância Explicada (%)", color="#aaaacc", fontsize=8)

ax_scree.tick_params(colors="#aaaacc", labelsize=7)

for spine in ax_scree.spines.values():
    spine.set_edgecolor("#2a2a4a")

patch_sel = mpatches.Patch(
    color="#ff6b6b",
    label="PCs selecionados (n=2)"
)

patch_rest = mpatches.Patch(
    color="#4a4a6a",
    label="Descartados"
)

ax_scree.legend(
    handles=[patch_sel, patch_rest],
    fontsize=7,
    facecolor="#1a1a2e",
    labelcolor="white",
    edgecolor="#333355"
)

ax_loadings.set_facecolor("#1a1a2e")

loadings = pca2.components_[0]
sorted_idx = np.argsort(np.abs(loadings))[::-1]

names_short = [
    feature_names[i]
    .replace("od280/od315_of_diluted_wines", "od280")
    .replace("_", " ")
    for i in sorted_idx
]

vals = loadings[sorted_idx]

bar_c = ["#00d4ff" if v > 0 else "#ff6b6b" for v in vals]

ax_loadings.barh(
    names_short,
    vals,
    color=bar_c,
    edgecolor="white",
    linewidth=0.3,
    alpha=0.9
)

ax_loadings.axvline(0, color="white", lw=0.8)

ax_loadings.set_title(
    "Loadings — PC1\n(contribuição de cada feature)",
    color="white",
    fontsize=9,
    fontweight="bold"
)

ax_loadings.tick_params(colors="#aaaacc", labelsize=7)

for spine in ax_loadings.spines.values():
    spine.set_edgecolor("#2a2a4a")

ax_loadings.set_xlabel(
    "Coeficiente",
    color="#aaaacc",
    fontsize=8
)

fig.suptitle(
    "IPE 4 — PCA | Script 2: Exemplo Real — Wine Dataset "
    "(178 amostras · 13 features → 2D)",
    color="white",
    fontsize=12,
    fontweight="bold",
    y=1.01
)

plt.tight_layout()

plt.savefig(
    "script2_real.png",
    dpi=150,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.close()

print("=" * 60)
print("  RESUMO FINAL — Script 2")
print("=" * 60)

print(f"\n  Dataset            : Wine Recognition (UCI)")
print(f"  Amostras           : {X.shape[0]}")
print(f"  Features originais : {X.shape[1]}")
print(f"  Features após PCA  : 2  (PC1 e PC2)")

print(
    f"  Variância preserv. : "
    f"{pca2.explained_variance_ratio_.sum()*100:.1f}%"
)

print(f"  Classes separáveis : SIM (visível no Scatter Plot 2D)")
print(f"\n  Gráfico salvo em   : script2_real.png")

print("\n  CONCLUSÃO: O PCA comprimiu 13 dimensões em 2 sem perder")
print("  a capacidade de SEPARAR as 3 classes de vinho.")
print("  Um classificador treinado em 2D terá desempenho similar")
print("  ao treinado em 13D, com muito mais eficiência!\n")