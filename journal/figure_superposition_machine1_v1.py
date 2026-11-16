# -*- coding: ascii -*-
"""FIGURE DE LA SUPERPOSITION -- machine 1, v1, 2026-11-16. Hors chaine. Lit superposition_v1.json, ne calcule rien.
Trois cadres : (A) ln10 de Gamma_pl / |delta| contre ln10 de Phi(kappa) ; (B) le residu r contre delta ; (C) le residu r*
de la variante (variable prise sur le saut lointain, essayee apres coup) contre delta.
Usage : python3 -I figure_superposition_machine1_v1.py <superposition.json> <sortie.png>"""
import sys, json, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
ENTREE, SORTIE = sys.argv[1:3]
for f in font_manager.findSystemFonts():
    if "Inter" in f:
        font_manager.fontManager.addfont(f)
plt.rcParams["font.family"] = ["Inter", "DejaVu Sans"]
SURFACE, TEXTE, SECOND, MUET, GRILLE, AXE = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
BLEU, ORANGE = "#2a78d6", "#eb6834"          # emplacements 1 et 2, valides toutes paires (validate_palette.js)
J = json.load(open(ENTREE))
D = [e for e in J["etats"] if e["domaine"]]
neg = [e for e in D if e["delta"] < 0]; pos = [e for e in D if e["delta"] > 0]
L10 = math.log(10.0)

fig = plt.figure(figsize=(15.0, 5.9), dpi=160, facecolor=SURFACE)
gs = fig.add_gridspec(1, 3, left=0.055, right=0.985, top=0.775, bottom=0.115, wspace=0.24)
axes = [fig.add_subplot(gs[0, i]) for i in range(3)]
for ax in axes:
    ax.set_facecolor(SURFACE)
    for c in ("top", "right"):
        ax.spines[c].set_visible(False)
    for c in ("left", "bottom"):
        ax.spines[c].set_color(AXE); ax.spines[c].set_linewidth(0.8)
    ax.grid(True, color=GRILLE, linewidth=0.8); ax.set_axisbelow(True)
    ax.tick_params(colors=MUET, labelsize=10, length=0)

def points(ax, fx, fy):
    for L, coul, nom in ((neg, BLEU, "w2 < 2  (\u03b4 < 0) : %d \u00e9tats" % len(neg)), (pos, ORANGE, "w2 > 2  (\u03b4 > 0) : %d \u00e9tats" % len(pos))):
        ax.scatter([fx(e) for e in L], [fy(e) for e in L], s=46, color=coul, edgecolors=SURFACE, linewidths=1.3, label=nom, zorder=3)

a = axes[0]
lo, hi = -11.2, -3.2
a.plot([lo, hi], [lo, hi], color=AXE, linewidth=1.2, zorder=1)
points(a, lambda e: e["ln_Phi"] / L10, lambda e: e["ln_G_sur_delta"] / L10)
a.set_xlim(lo, hi); a.set_ylim(lo, hi)
a.set_xlabel("log10 de \u03a6(\u03ba), la fonction d'\u00e9chelle (aucun param\u00e8tre)", color=SECOND, fontsize=10.5)
a.set_ylabel("log10 de la largeur 2D lue, divis\u00e9e par |\u03b4|", color=SECOND, fontsize=10.5)
a.set_title("A.  La largeur lue contre la loi d'\u00e9chelle", loc="left", color=TEXTE, fontsize=12.5, fontweight="semibold", pad=10)
a.text(-10.9, -3.9, "sur la droite : largeur = |\u03b4| \u00d7 \u03a6", color=SECOND, fontsize=10)
a.legend(loc="lower right", frameon=False, fontsize=10, labelcolor=SECOND, handletextpad=0.3)

for ax, cle, titre in ((axes[1], "r", "B.  Ce que la loi laisse (variable \u03ba)"),
                       (axes[2], "r_etoile", "C.  Idem, variable du saut lointain")):
    ax.axhline(0.0, color=AXE, linewidth=1.2, zorder=1)
    points(ax, lambda e: e["delta"], lambda e, c=cle: e[c])
    ax.set_xlim(-0.092, 0.08); ax.set_ylim(-1.0, 0.5)
    ax.set_xlabel("\u03b4 = w2 \u2212 2", color=SECOND, fontsize=10.5)
    ax.set_title(titre, loc="left", color=TEXTE, fontsize=12.5, fontweight="semibold", pad=10)
axes[1].set_ylabel("r\u00e9sidu ln( largeur / (|\u03b4| \u03a6) )", color=SECOND, fontsize=10.5)
axes[1].text(-0.088, -0.93, "0,89 au pire : un facteur 2,4", color=SECOND, fontsize=10)
axes[2].text(-0.088, -0.95, "essay\u00e9e apr\u00e8s coup ; \u00e0 \u03b4 > 0 le r\u00e9sidu\nne d\u00e9pend presque plus de l'\u00e9tat", color=SECOND, fontsize=10)

fig.text(0.055, 0.945, "La loi d'\u00e9chelle  largeur = |\u03b4| \u00d7 \u03a6(\u03ba)  sur les 185 \u00e9tats d\u00e9j\u00e0 jou\u00e9s du domaine", color=TEXTE, fontsize=15.5, fontweight="semibold", ha="left")
fig.text(0.055, 0.893, "Largeurs de plateau lues aux deltas 99 et 100 (douze points, douze cellules), sept d\u00e9cades. Lecture apr\u00e8s coup, hors cha\u00eene, sans 2D nouveau. "
                       "\u03ba = saut du site de d\u00e9part / |\u03b4|.", color=SECOND, fontsize=10.5, ha="left")
fig.savefig(SORTIE, facecolor=SURFACE)
print("figure ecrite :", SORTIE, "; points :", len(D))
