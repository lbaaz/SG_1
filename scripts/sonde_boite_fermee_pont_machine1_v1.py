# -*- coding: ascii -*-
"""SONDE DE BOITE FERMEE, gel "pont" -- machine 1, v1, 2026-11-17.
Pour UNE cellule (w2, m, g) et des cotes N : les niveaux de la boite FERMEE N x N (aucun absorbeur) dans la fenetre
    0.05 < x < 8 ,  x = (E_v - E) / delta     (du cote oppose au desaccord pour les deux signes de delta),
et, pour chacun, le poids c^2 du site (0, 0) dans son vecteur propre norme.
Le hamiltonien est celui du bloc "LECTEUR CREUX" depose (assembler, canon controle), execute tel quel : H = H0 + diag,
reel symetrique, sur a < N, b < N. Ecrite sans recopier la sonde de machine 2 ; ce qui en differe :
  - le niveau-vide est lu par iteration inverse a decalage 0 depuis le site (0, 0) : E_v, w0 = poids du site (0, 0) ;
  - DEUX lectures a decalage-inversion (ARPACK par scipy eigsh, factorisation creuse splu d'ordre COLAMD, vecteur de depart FIXE, aucun
    tirage aleatoire), decalages E_v - 2.5 delta et E_v - 5.5 delta ; le nombre de niveaux demandes double tant que les
    niveaux trouves ne debordent pas la fenetre des deux cotes ;
  - le poids du site (0, 0) est lu DEUX fois par lecture : BRUT (le composant du vecteur d'ARPACK), et PAR PARTITION :
    le vecteur est coupe en dedans I (sites max(a, b) <= r_I) et dehors O ; le dedans est RECALCULE depuis le dehors,
        (H_II - E) psi_I = - H_IO psi_O ,     c^2 = psi_I(0,0)^2 / (|psi_I|^2 + |psi_O|^2) ,
    resolution dense dans l'ordre naturel des sites (le site (0, 0) en premier). r_I = r_c = 2 (m + max(8, m)) + 2 ;
    la meme lecture est refaite a r_I + 6 pour la premiere lecture, a titre de controle.
Un niveau est FIABLE si ses deux lectures par partition s'accordent a 2 pour cent.
Cette sonde ne lit pas la chaine, ne calcule aucune part et ne juge rien. Une ligne JSON par boite.
Usage : python3 -I -B sonde_boite_fermee_pont_machine1_v1.py <registre> <w2 en fraction> <m> <g ecrit> <sortie.jsonl>
                      <cote> [cote ...]"""
import sys, math, json, time, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl
REG, W2S, MS, G_TXT, SORTIE = sys.argv[1].rstrip("/"), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
COTES = [int(c) for c in sys.argv[6:]]
X_LO, X_HI, S_A, S_B, K_DEPART, K_MAX, TOL_FIABLE, TOL_LISTE, ELARGI = 0.05, 8.0, 2.5, 5.5, 24, 768, 0.02, 1e-9, 6
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
r_c = 2 * (m + max(8, m)) + 2
if min(COTES) < r_c + ELARGI + 8: raise SystemExit("REFUS : cote trop petit")

def vide(H, n):
    """Iteration inverse a decalage 0 depuis le site (0, 0)."""
    lu = sl.splu(H, permc_spec="COLAMD")
    x = np.zeros(n); x[0] = 1.0; lam, res, it = 0.0, float("inf"), 0
    for it in range(1, 13):
        y = lu.solve(x); x = y / np.linalg.norm(y)
        Hx = H @ x; lam = float(x @ Hx); res = float(np.linalg.norm(Hx - lam * x))
        if it >= 2 and res <= 1e-11 * max(1.0, abs(lam)): break
    return lam, float(x[0] ** 2), res, it

def lecture(H, n, sigma, E_lo, E_hi):
    """Niveaux autour de sigma par decalage-inversion ; k double tant que la fenetre n'est pas debordee."""
    lu = sl.splu((H - sigma * sp.identity(n, format="csc")).tocsc(), permc_spec="COLAMD")
    op = sl.LinearOperator((n, n), matvec=lu.solve, dtype=float)
    v0 = np.cos(np.arange(1, n + 1, dtype=float)); rayon = max(abs(sigma - E_lo), abs(sigma - E_hi)); k = K_DEPART
    while True:
        E, V = sl.eigsh(H, k=k, sigma=sigma, which="LM", OPinv=op, v0=v0, tol=0)
        couverte = bool(np.max(np.abs(E - sigma)) > rayon)
        if couverte or k >= K_MAX: break
        k *= 2
    lo, hi = min(E_lo, E_hi), max(E_lo, E_hi); sel = (E > lo) & (E < hi); o = np.argsort(E[sel])
    return E[sel][o], V[:, sel][:, o], k, couverte

def partition(H, N, E, psi, r_I):
    """Le dedans recalcule depuis le dehors ; rend c^2 du site (0, 0)."""
    a = np.arange(N * N) // N; b = np.arange(N * N) % N; dedans = np.maximum(a, b) <= r_I
    I = np.nonzero(dedans)[0]; O = np.nonzero(~dedans)[0]
    HI = H[I]; H_II = HI[:, I].toarray(); second = -(HI[:, O] @ psi[O])
    psi_I = np.linalg.solve(H_II - E * np.eye(len(I)), second)
    return float(psi_I[0] ** 2 / (psi_I @ psi_I + psi[O] @ psi[O]))

t0 = time.time(); Nmax = max(COTES); H0max, dgmax = assembler(W2, g, Nmax, signe=-1)
print("# cellule w2 = %s, m = %d, g = %s, delta = %+.4f, r_c = %d ; assemblage au cote %d : %.0f s" % (W2S, m, G_TXT, D, r_c, Nmax, time.time() - t0), flush=True)
print("# cote  E_vide         w0          niveaux  fiables  k_a/k_b  listes  brut/partition max  r_I/r_I+6 max  secondes", flush=True)
sortie = open(SORTIE, "a", encoding="ascii")
for N in COTES:
    t1 = time.time(); n = N * N
    if N == Nmax: H0, dg = H0max.tocsc(), dgmax
    else: H0, dg = restreindre(H0max, dgmax, Nmax, N)
    H = (H0 + sp.diags(dg)).tocsc()
    Ev, w0, res, it = vide(H, n)
    E_lo, E_hi = Ev - X_LO * D, Ev - X_HI * D
    Ea, Va, ka, cva = lecture(H, n, Ev - S_A * D, E_lo, E_hi)
    Eb, Vb, kb, cvb = lecture(H, n, Ev - S_B * D, E_lo, E_hi)
    memes = bool(len(Ea) == len(Eb) and (len(Ea) == 0 or float(np.max(np.abs(Ea - Eb))) <= TOL_LISTE))
    niveaux = []; pire_bp = 0.0; pire_r = 0.0
    for j in range(len(Ea)):
        ca = partition(H, N, float(Ea[j]), Va[:, j], r_c); cl = partition(H, N, float(Ea[j]), Va[:, j], r_c + ELARGI)
        rec = {"x": float((Ev - Ea[j]) / D), "E": float(Ea[j]), "c2_a": ca, "brut_a": float(Va[0, j] ** 2), "c2_a_large": cl}
        if memes:
            cb = partition(H, N, float(Eb[j]), Vb[:, j], r_c)
            rec.update({"c2_b": cb, "brut_b": float(Vb[0, j] ** 2), "fiable": bool(abs(ca - cb) <= TOL_FIABLE * ca)})
        else:
            rec.update({"c2_b": None, "brut_b": None, "fiable": False})
        pire_bp = max(pire_bp, abs(rec["brut_a"] / ca - 1.0)); pire_r = max(pire_r, abs(cl / ca - 1.0))
        niveaux.append(rec)
    box = {"cote": N, "w2": W2S, "m": m, "g": G_TXT, "delta": D, "r_c": r_c, "E_vide": Ev, "w0": w0, "residu_vide": res,
           "iterations_vide": it, "k_a": ka, "k_b": kb, "couverte_a": cva, "couverte_b": cvb, "listes_identiques": memes,
           "n": len(niveaux), "n_b": int(len(Eb)), "fiables": sum(v["fiable"] for v in niveaux), "niveaux": niveaux,
           "secondes": time.time() - t1}
    sortie.write(json.dumps(box, sort_keys=True) + "\n"); sortie.flush()
    print("%-6d %+.6e  %.8f  %-7d  %-7d  %d/%d    %s     %.2e            %.2e       %.0f"
          % (N, Ev, w0, box["n"], box["fiables"], ka, kb, "oui" if memes else "NON", pire_bp, pire_r, box["secondes"]), flush=True)
try:
    import resource
    pic = " ; pic de memoire %.0f Mo" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0)
except ImportError:                                # pas de module resource hors d'Unix : le pic n'est pas mesure
    pic = ""
print("# fini (%.0f s)%s" % (time.time() - t0, pic))
