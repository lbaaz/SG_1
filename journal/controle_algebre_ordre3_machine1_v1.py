# -*- coding: ascii -*-
"""CONTROLE D'ALGEBRE DU TERME D'ORDRE 3 -- machine 1, v1, 2026-11-15. Hors chaine. AUCUNE LARGEUR N'EST LUE ICI :
matrices hermitiennes, sans absorbeur, petites bases de Fock ; ce n'est pas une lecture 2D du fantome.
(V0) les elements de x^5 du moteur (X_saut_reel) sont ceux d'une matrice x^5 construite a part (operateurs d'echelle).
(V1) la formule de Lowdin a l'ordre 3 (ecrite ici en matrices denses, a part du bloc) contre le hamiltonien effectif
     canonique EXACT d'une petite base : le reste sur le saut entre voisins doit decroitre comme g^5 avec le terme
     d'ordre 3, comme g^3 sans lui ; sur la diagonale et le second voisin, comme g^4 (ordre 2 complet). De meme
     au 3e voisin ; au 5e voisin (un seul element, vite au plancher d'arrondi) : g^3 sans le terme, et le terme en
     retire plus de 99 pour cent au plus fort couplage ; au 4e voisin, interdit a l'ordre 3 : g^4.
(V2) les tables du bloc (T3, W3, W5 : sommes sur les chemins, elements du moteur) contre la formule dense de (V1)
     appliquee a une base assez grande pour que la troncature ne touche pas les sites bas.
Usage : python3 -I controle_algebre_ordre3_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sortie.json>"""
import sys, math, json, importlib.util
import numpy as np
MOTEUR, BLOC2, BLOC3, SORTIE = sys.argv[1:5]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec")); exec(compile(open(BLOC3, encoding="ascii").read(), BLOC3, "exec"))
from fractions import Fraction as F

def x5_a_part(N, w2, marge=8):
    """x^5 dans la base |n1, n2>, n < N, par puissance de matrice dans une base plus grande puis restriction."""
    Ng = N + marge; _, l1, l2 = M.lambdas(w2)
    a = np.diag(np.sqrt(np.arange(1, Ng)), 1); q = a + a.T; I = np.eye(Ng)
    X = l1 * np.kron(q, I) + l2 * np.kron(I, q)
    X5 = np.linalg.matrix_power(X, 5)
    idx = [i * Ng + j for i in range(N) for j in range(N)]
    return X5[np.ix_(idx, idx)]

def lowdin(E, V, A):
    """Ordres 2 et 3 du hamiltonien effectif sur A (formules de Lowdin, forme symetrique), en matrices denses."""
    n = len(E); B = [i for i in range(n) if i not in set(A)]
    VA = V[np.ix_(A, A)]; VAB = V[np.ix_(A, B)]; VBB = V[np.ix_(B, B)]
    D = 1.0 / (E[A][:, None] - E[B][None, :]); G = VAB * D
    H2 = 0.5 * (G @ VAB.T + VAB @ G.T)
    T1 = np.zeros((len(A), len(A)))
    for m in range(len(A)):
        T1[m, :] = VAB @ ((G[m, :] @ VBB) * D[m, :])
    Fm = np.zeros((len(A), len(A)))
    for m in range(len(A)):
        for mp in range(len(A)):
            Fm[m, mp] = sum(VA[mm, mp] * np.sum(VAB[m, :] * G[mm, :] * D[mp, :]) for mm in range(len(A)) if VA[mm, mp] != 0.0)
    H3 = 0.5 * (T1 + T1.T) - 0.5 * (Fm + Fm.T)
    return H2, H3

def effectif_exact(H, A):
    """Hamiltonien effectif canonique (des Cloizeaux) sur A : vecteurs propres de plus grand poids sur A."""
    val, vec = np.linalg.eigh(H)
    poids = np.sum(vec[A, :] ** 2, axis=0)
    choix = np.argsort(-poids)[:len(A)]
    U = vec[:, choix]; S = U[A, :]                       # projection sur A
    Q = S @ S.T                                           # P0 P P0
    w, R = np.linalg.eigh(Q); Qm12 = R @ np.diag(w ** -0.5) @ R.T
    return Qm12 @ (S @ np.diag(val[choix]) @ S.T) @ Qm12, float(poids[choix].min())

out = {}
# ---------------- (V0)
w2 = F(211, 100); N = 12; X5 = x5_a_part(N, w2); pire = 0.0; n_el = 0
for a in range(N):
    for b in range(N):
        for (k, l) in PAS_IMPAIRS:
            if 0 <= a + k < N and 0 <= b + l < N:
                ref = X5[(a + k) * N + (b + l), a * N + b]; x = M.X_saut_reel(M.P, k, l, float(a), float(b), w2)
                pire = max(pire, abs(x - ref) / max(abs(ref), 1e-300)); n_el += 1
out["V0"] = {"elements": n_el, "pire_ecart_relatif": pire}
print("(V0) elements de x^5 du moteur contre une matrice construite a part : %d elements, pire ecart relatif %.1e" % (n_el, pire))
# ---------------- (V1)
N = 13; n1, n2 = 3, 1; c0, c1 = M.CANAL
E0 = np.array([M.energie_libre(a, b, w2) for a in range(N) for b in range(N)])
X5 = x5_a_part(N, w2, marge=0)                            # troncature franche : une matrice hermitienne coherente
A = [(n1 + c0 * m) * N + (n2 + c1 * m) for m in range(-1, 5) if 0 <= n1 + c0 * m < N and 0 <= n2 + c1 * m < N]
res = {"voisin_avec": [], "voisin_sans": [], "diag": [], "second": [], "troisieme_avec": [], "troisieme_sans": [], "cinquieme_avec": [], "cinquieme_sans": [],
       "quatrieme": [], "g": [], "poids_min": []}
for g in (2e-4, 4e-4, 8e-4, 1.6e-3):
    V = (g / M.P) * X5; H = np.diag(E0) + V
    Hx, pm = effectif_exact(H, A)
    H2, H3 = lowdin(E0, V, A)
    Hp2 = np.diag(E0[A]) + V[np.ix_(A, A)] + H2; Hp3 = Hp2 + H3
    nA = len(A)
    res["g"].append(g); res["poids_min"].append(pm)
    res["voisin_avec"].append(max(abs(Hx[i, i + 1] - Hp3[i, i + 1]) for i in range(nA - 1)))
    res["voisin_sans"].append(max(abs(Hx[i, i + 1] - Hp2[i, i + 1]) for i in range(nA - 1)))
    res["diag"].append(max(abs(Hx[i, i] - Hp3[i, i]) for i in range(nA)))
    res["second"].append(max(abs(Hx[i, i + 2] - Hp3[i, i + 2]) for i in range(nA - 2)))
    res["troisieme_avec"].append(max(abs(Hx[i, i + 3] - Hp3[i, i + 3]) for i in range(nA - 3)))
    res["troisieme_sans"].append(max(abs(Hx[i, i + 3] - Hp2[i, i + 3]) for i in range(nA - 3)))
    res["cinquieme_avec"].append(max(abs(Hx[i, i + 5] - Hp3[i, i + 5]) for i in range(nA - 5)))
    res["cinquieme_sans"].append(max(abs(Hx[i, i + 5] - Hp2[i, i + 5]) for i in range(nA - 5)))
    res["quatrieme"].append(max(abs(Hx[i, i + 4] - Hp3[i, i + 4]) for i in range(nA - 4)))
def pente(y):
    x = [math.log(v) for v in res["g"]]; yy = [math.log(v) for v in y]
    mx, my = sum(x) / len(x), sum(yy) / len(yy)
    return sum((a - mx) * (b - my) for a, b in zip(x, yy)) / sum((a - mx) ** 2 for a in x)
res["pentes"] = {k: pente(res[k]) for k in ("voisin_avec", "voisin_sans", "diag", "second", "troisieme_avec", "troisieme_sans", "cinquieme_avec", "cinquieme_sans",
                                              "quatrieme")}
out["V1"] = res
print("(V1) base %d x %d, w2 = %s, %d sites de l'echelle de (%d, %d) ; reste = |effectif exact - perturbatif|, plus grand element" % (N, N, w2, len(A), n1, n2))
print("     g          saut voisin, avec ordre 3   sans ordre 3    diagonale    second voisin   3e voisin avec   sans    poids min")
for i, g in enumerate(res["g"]):
    print("     %.1e    %.3e                   %.3e       %.3e    %.3e       %.3e        %.3e   %.6f" % (g, res["voisin_avec"][i], res["voisin_sans"][i],
          res["diag"][i], res["second"][i], res["troisieme_avec"][i], res["troisieme_sans"][i], res["poids_min"][i]))
print("     pentes en g : saut voisin avec ordre 3 %.2f (attendu 5), sans %.2f (attendu 3) ; diagonale %.2f (attendu 4) ; second voisin %.2f (attendu 4) ;"
      % (res["pentes"]["voisin_avec"], res["pentes"]["voisin_sans"], res["pentes"]["diag"], res["pentes"]["second"]))
print("                   3e voisin avec ordre 3 %.2f (attendu 5), sans %.2f (attendu 3)" % (res["pentes"]["troisieme_avec"], res["pentes"]["troisieme_sans"]))
res["cinquieme_rapport_g_max"] = res["cinquieme_avec"][-1] / res["cinquieme_sans"][-1]
print("     5e voisin (un element) : reste sans ordre 3 %s ; pente %.2f (attendu 3)" % (" ".join("%.2e" % v for v in res["cinquieme_sans"]), res["pentes"]["cinquieme_sans"]))
print("                              reste avec ordre 3 %s : au plancher d'arrondi aux petits couplages, la pente n'y est pas lisible ;" % " ".join("%.2e" % v for v in res["cinquieme_avec"]))
print("                              rapport avec / sans au plus fort couplage : %.1e" % res["cinquieme_rapport_g_max"])
print("     4e voisin (interdit a l'ordre 3 par la parite ; premier terme : ordre 4) : reste %s ; pente %.2f (attendu 4)" % (
      " ".join("%.2e" % v for v in res["quatrieme"]), res["pentes"]["quatrieme"]))
# ---------------- (V2)
N = 34; g = 5e-3; pires = {}
for (n1, n2, w2) in ((3, 1, F(211, 100)), (7, 2, F(197, 100)), (4, 2, F(47, 25))):
    E0 = np.array([M.energie_libre(a, b, w2) for a in range(N) for b in range(N)]); V = (g / M.P) * x5_a_part(N, w2)
    ms = [m for m in range(-min(n1 // c0, n2 // c1), 40) if n1 + c0 * m < N and n2 + c1 * m < N]
    A = [(n1 + c0 * m) * N + (n2 + c1 * m) for m in ms]
    H2, H3 = lowdin(E0, V, A)
    sites = [(8, 1.0, 1.0)]                                # seule la longueur des tables en depend
    tb = tables_ordre2(float(n1), float(n2), w2, g, sites, M_facteur=1); t3 = tables_ordre3(float(n1), float(n2), w2, g, tb)
    m_sur = [m for m in ms if n1 + c0 * (m + 3) + 2 * M.P < N and n2 + c1 * (m + 3) + 2 * M.P < N]   # chemins entiers dans la base
    def ecart(x, y):
        return abs(x - y) / max(abs(y), 1e-300)
    p = {"T3": max(ecart(t3["T3"][m], H3[ms.index(m), ms.index(m) + 1]) for m in m_sur),
         "W3": max(ecart(t3["W3"][m], H3[ms.index(m), ms.index(m) + 3]) for m in m_sur),
         "W5": max(ecart(t3["W5"][m], H3[ms.index(m), ms.index(m) + 5]) for m in m_sur if m + 5 in ms),
         "W5_sur_W3_max": max(abs(t3["W5"][m] / t3["W3"][m]) for m in m_sur if m + 5 in ms),
         "S": max(ecart(tb["S"][m] - tb["S"][m_sur[0]], H2[ms.index(m), ms.index(m)] - H2[ms.index(m_sur[0]), ms.index(m_sur[0])]) for m in m_sur[1:]),
         "U": max(ecart(tb["U"][m], H2[ms.index(m), ms.index(m) + 2]) for m in m_sur), "sites": len(m_sur),
         "T3_sur_t_max": max(abs(t3["T3"][m] / tb["t"][m]) for m in m_sur)}
    pires["%d,%d,%s" % (n1, n2, w2)] = p
    print("(V2) echelle de (%d, %d) a w2 = %s, g = %.0e, %d sites : tables du bloc contre la formule dense, pire ecart relatif : T3 %.1e, W3 %.1e, W5 %.1e, Sigma2 %.1e, u %.1e"
          % (n1, n2, w2, g, p["sites"], p["T3"], p["W3"], p["W5"], p["S"], p["U"]))
out["V2"] = pires
ok = (out["V0"]["pire_ecart_relatif"] < 1e-9 and abs(res["pentes"]["voisin_avec"] - 5) < 0.3 and abs(res["pentes"]["voisin_sans"] - 3) < 0.3
      and abs(res["pentes"]["diag"] - 4) < 0.3 and abs(res["pentes"]["second"] - 4) < 0.3
      and abs(res["pentes"]["cinquieme_sans"] - 3) < 0.3 and res["cinquieme_rapport_g_max"] < 1e-2 and abs(res["pentes"]["quatrieme"] - 4) < 0.3
      and all(p[k] < 1e-8 for p in pires.values() for k in ("T3", "W3", "W5", "S", "U")))
out["tient"] = bool(ok)
print("CONTROLE D'ALGEBRE : %s" % ("TIENT" if ok else "NE TIENT PAS"))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
sys.exit(0 if ok else 1)
