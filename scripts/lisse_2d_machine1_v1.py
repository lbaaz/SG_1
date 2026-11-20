# -*- coding: utf-8 -*-
# Densite locale de l'etat (0, 0) du H 2D du moteur sous absorbeur, hors de l'energie du vide, lue par le flux.
# Hors chaine, classe 3, point sacrifie w2 = 101/50, 3 barreaux. Le hamiltonien, les absorbeurs et la lecture du vide sont
# ceux du bloc "LECTEUR CREUX" depose (canon controle), execute tel quel ; seule la resolution a energie fixee est neuve :
#   (A - E) y = e_(0,0),  A = H0 + diag - i eta W,  rho(E) = (eta / pi) somme_j W_j |y_j|^2  (identique a Im(y_0) / pi).
# Usage : python3 -I lisse_2d_machine1_v1.py <registre> <absorbeur A|B|C|D|E> <sortie.json> <k> [k ...]
import sys, os, math, json, time, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl
REG, NOM, SORTIE = sys.argv[1].rstrip("/"), sys.argv[2], sys.argv[3]; KS = [int(k) for k in sys.argv[4:]]
def canon_B(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
MOTEUR = REG + "/scripts/m17_chaine_v17.py"; SOURCE = REG + "/scripts/sonde_lecteur_gel_loi_machine1_v1.py"
if canon_B(MOTEUR) != "82a0be882568fe0c" or canon_B(SOURCE) != "d5cc48f48e37af99": raise SystemExit("REFUS : canons")
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
src = open(SOURCE, encoding="ascii").read(); i0 = src.index("# --- LECTEUR CREUX"); i1 = src.index("# --- fin du bloc ---", i0)
exec(compile(src[i0:i1], "bloc_lecteur_depose", "exec"))
W2 = F(101, 50); AD = abs(float(W2) - 2.0); g = 5.53067e-03; m = 3; r_c = 2 * (m + max(8, m)) + 2; eta0 = AD
ABS = {"A": ("F2", 0, 80), "B": ("F2", 0, 100), "C": ("F1", 0, 100), "D": ("F2", 10, 80), "E": ("F2", 30, 80)}   # E : hors lecteur depose, bord recule de 30
X = [0.05, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
forme, dr, L = ABS[NOM]; bord = r_c + dr; N = bord + L
t0 = time.time(); H0, dg = assembler(W2, g, N, signe=-1); H0 = H0.tocsc(); W = table_W(N, forme, bord, L)
print("absorbeur %s : forme %s, bord %d, couches %d, boite %d x %d ; assemblage %.0f s" % (NOM, forme, bord, L, N, N, time.time() - t0), flush=True)
n = N * N; e0 = np.zeros(n, dtype=complex); e0[0] = 1.0; I = sp.identity(n, format="csc", dtype=complex)
out = {"absorbeur": NOM, "forme": forme, "bord": bord, "couches": L, "N": N, "X": X, "r_c": r_c, "eta0": eta0, "k": {}}
for k in KS:
    eta = eta0 * 2.0 ** (-k); t1 = time.time()
    r, xv = lire_etat(H0, dg, W, eta, N, (0, 0), 0.0)
    if not r["suivi"]:
        print("  k = %d : vide non suivi" % k, flush=True); out["k"][str(k)] = {"suivi": False}; continue
    A = (H0 + sp.diags(dg - 1j * eta * W)).tocsc().astype(complex)
    rf = []; rd = []
    for x in X:
        E = r["E_re"] - x * AD
        y = sl.splu((A - E * I).tocsc(), permc_spec="MMD_ATA").solve(e0)
        rf.append(float(eta * np.sum(W * np.abs(y) ** 2) / math.pi)); rd.append(float(y[0].imag / math.pi))
    out["k"][str(k)] = {"suivi": True, "eta": eta, "E_vide": r["E_re"], "gamma_vide": r["gamma"], "w0": r["poids_site"], "rho_flux": rf, "rho_direct": rd}
    print("  k = %2d : E_vide %+.6e, Gamma %.4e, w0 %.8f ; ln rho : %s (%.0f s)"
          % (k, r["E_re"], r["gamma"], r["poids_site"], " ".join("%.3f" % math.log(v) for v in rf), time.time() - t1), flush=True)
    json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit %s (%.0f s)" % (SORTIE, time.time() - t0))
