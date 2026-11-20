# -*- coding: ascii -*-
"""SONDE DE DENSITE 2D A ENERGIE FIXEE, gel "pont" -- machine 1, v1, 2026-11-17.
Densite locale du site (0, 0) du H 2D du moteur sous absorbeur, HORS de l'energie du vide, pour UNE cellule (w2, m, g)
et UN absorbeur du lecteur depose. Derivee de lisse_2d_machine1_v1.py (95a91f49bb5db12e, exploration du 17/11 au point
sacrifie) : meme calcul ; CHANGENT : la cellule est un argument, l'ecart est pris du cote oppose au desaccord pour les
deux signes de delta, la barriere est relue (m_bord doit valoir m), l'absorbeur E de l'exploration est retire.
Le hamiltonien, les absorbeurs et la lecture du vide sont ceux du bloc "LECTEUR CREUX" depose (canon controle), execute
tel quel ; la resolution a energie fixee :
    (A - E) y = e_(0,0),  A = H0 + diag - i eta W,  E = E_v(eta) - x delta,
    rho(E) = (eta / pi) somme_j W_j |y_j|^2      (egale a Im(y_0) / pi, consignee a cote),
E_v(eta) etant la partie reelle de la valeur propre du vide lue au meme barreau. eta_k = |delta| 2^(-k).
Geometrie : r_c = 2 (m + max(8, m)) + 2 ; absorbeurs A (F2, bord r_c, 80 couches), B (F2, r_c, 100), C (F1, r_c, 100),
D (F2, r_c + 10, 80) ; boite = bord + couches.
AUCUN tirage aleatoire. Cette sonde ne lit pas la chaine et ne juge rien.
Usage : python3 -I -B sonde_densite_2d_pont_machine1_v1.py <registre> <w2 en fraction> <m> <g ecrit> <A|B|C|D>
                      <sortie.json> [k ...]          (sans k : les douze barreaux -3 a 8)"""
import sys, math, json, time, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl
REG, W2S, MS, G_TXT, NOM, SORTIE = sys.argv[1].rstrip("/"), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
KS = [int(k) for k in sys.argv[7:]] or list(range(-3, 9))
def canon_B(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
MOTEUR = REG + "/scripts/m17_chaine_v17.py"; SOURCE = REG + "/scripts/sonde_lecteur_gel_loi_machine1_v1.py"
if canon_B(MOTEUR) != "82a0be882568fe0c" or canon_B(SOURCE) != "d5cc48f48e37af99": raise SystemExit("REFUS : canons")
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
src = open(SOURCE, encoding="ascii").read(); i0 = src.index("# --- LECTEUR CREUX"); i1 = src.index("# --- fin du bloc ---", i0)
exec(compile(src[i0:i1], "bloc_lecteur_depose", "exec"))
W2 = F(W2S); m = int(MS); g = float(G_TXT); D = float(W2) - 2.0; AD = abs(D)
if "%.5e" % g != G_TXT: raise SystemExit("REFUS : le couplage n'est pas ecrit a six chiffres")
sites = M.barriere(0.0, 0.0, W2, g, True)
if not sites or sites[-1][0] != m: raise SystemExit("REFUS : la barriere ne finit pas au site %d" % m)
r_c = 2 * (m + max(8, m)) + 2; eta0 = AD
ABS = {"A": ("F2", 0, 80), "B": ("F2", 0, 100), "C": ("F1", 0, 100), "D": ("F2", 10, 80)}
X = [0.05, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
forme, dr, L = ABS[NOM]; bord = r_c + dr; N = bord + L
t0 = time.time(); H0, dg = assembler(W2, g, N, signe=-1); H0 = H0.tocsc(); W = table_W(N, forme, bord, L)
print("cellule w2 = %s, m = %d, g = %s, delta = %+.4f ; absorbeur %s : forme %s, bord %d, couches %d, boite %d x %d ; assemblage %.0f s"
      % (W2S, m, G_TXT, D, NOM, forme, bord, L, N, N, time.time() - t0), flush=True)
n = N * N; e0 = np.zeros(n, dtype=complex); e0[0] = 1.0; I = sp.identity(n, format="csc", dtype=complex)
out = {"w2": W2S, "m": m, "g": G_TXT, "delta": D, "absorbeur": NOM, "forme": forme, "bord": bord, "couches": L, "N": N, "X": X,
       "r_c": r_c, "eta0": eta0, "k": {}}
for k in KS:
    eta = eta0 * 2.0 ** (-k); t1 = time.time()
    r, xv = lire_etat(H0, dg, W, eta, N, (0, 0), 0.0)
    if not r["suivi"]:
        print("  k = %d : vide non suivi" % k, flush=True); out["k"][str(k)] = {"suivi": False}; continue
    A = (H0 + sp.diags(dg - 1j * eta * W)).tocsc().astype(complex)
    rf = []; rd = []
    for x in X:
        E = r["E_re"] - x * D
        y = sl.splu((A - E * I).tocsc(), permc_spec="MMD_ATA").solve(e0)
        rf.append(float(eta * np.sum(W * np.abs(y) ** 2) / math.pi)); rd.append(float(y[0].imag / math.pi))
    out["k"][str(k)] = {"suivi": True, "eta": eta, "E_vide": r["E_re"], "gamma_vide": r["gamma"], "w0": r["poids_site"],
                        "rho_flux": rf, "rho_direct": rd}
    print("  k = %2d : E_vide %+.6e, Gamma %.4e, w0 %.8f ; ln rho : %s (%.0f s)"
          % (k, r["E_re"], r["gamma"], r["poids_site"], " ".join("%.3f" % (math.log(v) if v > 0 else float("nan")) for v in rf),
             time.time() - t1), flush=True)
    json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit %s (%.0f s)" % (SORTIE, time.time() - t0))
