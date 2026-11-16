# -*- coding: ascii -*-
"""TEMOIN SANS FANTOME A LA GEOMETRIE DU VIDE -- machine 1, v1, 2026-11-16. Hors chaine, classe 3.
AUCUNE LARGEUR DU SYSTEME A FANTOME N'EST CALCULEE ICI. Le lecteur creux DEPOSE (bloc lu tel quel dans
sonde_lecteur_gel_loi_machine1_v1.py, canon controle) lit l'etat porte par (0, 0) du JUMEAU H+ (signe +1 : pas
d'echelle resonante, la largeur n'y est fabriquee que par l'absorbeur), a l'energie de depart 0, comme le fait deja
le mode "etage1" du depot. Geometrie : r_c = 2 (m_bord + max(8, m_bord)) + 2 (la regle du depot, sans graine),
eta0 = |delta|, les quatre absorbeurs et les douze barreaux du depot. Sert a deux choses : le cout d'une lecture a
cette taille de boite, et le plancher numerique du lecteur a cette geometrie.
Usage : python3 -I temoin_lecteur_vide_machine1_v1.py <moteur> <sonde_lecteur_gel_loi.py> <sortie.json>"""
import sys, time, math, json, hashlib, unicodedata
import importlib.util
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl
MOTEUR, SONDE, SORTIE = sys.argv[1:4]
CANON_SONDE = "d5cc48f48e37af99"
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
if canon_B(SONDE) != CANON_SONDE:
    raise SystemExit("REFUS : la sonde du lecteur n'est pas au canon %s" % CANON_SONDE)
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
src = open(SONDE, encoding="ascii").read()
i0 = src.index("# --- LECTEUR CREUX"); i1 = src.index("# --- fin du bloc ---", i0)
exec(compile(src[i0:i1], "bloc_lecteur_depose", "exec"))
KS = list(range(-3, 9))
ABSORBEURS = [("A", "F2", 0, 80), ("B", "F2", 0, 100), ("C", "F1", 0, 100), ("D", "F2", 10, 80)]
CAS = [(3, F(101, 50), 5.536e-03), (4, F(199, 100), 1.887e-03), (5, F(101, 50), 3.351e-03)]   # m_bord du vide, w2, g (ordres de grandeur de la sonde du vide)
out = {"sonde_canon": CANON_SONDE, "cas": []}
for (mb, w2, g) in CAS:
    r_c = 2 * (mb + max(8, mb)) + 2; eta0 = abs(float(w2) - 2.0)
    geo = [(nom, forme, r_c + dr, L, r_c + dr + L) for nom, forme, dr, L in ABSORBEURS]
    Nmax = max(x[4] for x in geo)
    t0 = time.time(); H0m, dm = assembler(w2, g, Nmax, signe=+1); t_ass = time.time() - t0
    rec = {"m_bord_du_vide": mb, "w2": "%d/%d" % (w2.numerator, w2.denominator), "g": g, "r_c": r_c, "eta0": eta0, "Nmax": Nmax, "assemblage_s": round(t_ass, 1), "absorbeurs": {}}
    pire, lus, suivis = 0.0, 0, 0
    for nom, forme, bord, L, N in geo:
        H0, dg = restreindre(H0m, dm, Nmax, N)
        t1 = time.time(); tr = trajectoire(H0, dg, table_W(N, forme, bord, L), eta0, N, (0, 0), 0.0, KS); dt = time.time() - t1
        g_ = [tr[str(k)]["gamma"] for k in KS]; s_ = [tr[str(k)]["suivi"] for k in KS]
        rec["absorbeurs"][nom] = {"N": N, "duree_s": round(dt, 1), "gamma": g_, "suivi": s_, "poids_min": min(tr[str(k)]["poids_site"] for k in KS)}
        lus += len(KS); suivis += sum(s_); pire = max(pire, max(x for x in g_ if x is not None))
        print("  vide a %d barreaux, w2 = %s, g = %.3e, r_c = %d, absorbeur %s (N = %d) : %d/%d suivis, %.1f s, largeur du jumeau de %.1e a %.1e" % (
            mb, rec["w2"], g, r_c, nom, N, sum(s_), len(KS), dt, min(g_), max(g_)), flush=True)
    rec.update({"lectures": lus, "suivies": suivis, "plus_grande_largeur": pire, "duree_totale_s": round(time.time() - t0, 1)})
    out["cas"].append(rec)
    print("  -> %d lectures, %d suivies, plus grande largeur du jumeau %.2e, %.0f s en tout" % (lus, suivis, pire, time.time() - t0), flush=True)
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
