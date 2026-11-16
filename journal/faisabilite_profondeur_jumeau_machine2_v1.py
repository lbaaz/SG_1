# -*- coding: ascii -*-
"""FAISABILITE DE LA LIGNE PROFONDE, AU JUMEAU SANS FANTOME -- machine 1, v1, 2026-11-16. Piece du gel "largeur du vide",
premiere partie. AUCUNE LARGEUR DU SYSTEME A FANTOME N'EST CALCULEE ICI, et w2 = 101/50 N'EST PAS UN CANDIDAT (centieme).
Le lecteur creux DEPOSE (bloc lu tel quel dans sonde_lecteur_gel_loi_machine1_v1.py, canon controle) lit l'etat porte
par (0, 0) du JUMEAU H+ (signe +1) a la geometrie qu'aurait une cellule de 8, 12 et 16 barreaux : r_c = 2 (m + max(8, m))
+ 2, eta0 = |delta|, absorbeurs A (F2, 80 couches) et B (F2, 100 couches : la plus grande boite), barreaux k = -3, 3, 8.
Sert a une chose : le cout (duree, memoire) d'une lecture aux boites de la ligne profonde, avant de geler ses profondeurs.
Le couplage est celui de la regle des cellules : g = kappa_m |delta| P / X(0, 0), arrondi a six chiffres.
Usage : python3 -I faisabilite_profondeur_jumeau_machine1_v1.py <moteur> <sonde_lecteur_gel_loi.py> <sortie.json>"""
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
import ctypes
from ctypes import wintypes


def pic_memoire_Mo():
    """pic de l'ensemble de travail du processus, en Mo (Windows)."""
    class PMC(ctypes.Structure):
        _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD), ("PeakWorkingSetSize", ctypes.c_size_t),
                    ("WorkingSetSize", ctypes.c_size_t), ("QuotaPeakPagedPoolUsage", ctypes.c_size_t), ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t), ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t), ("PeakPagefileUsage", ctypes.c_size_t)]
    c = PMC(); c.cb = ctypes.sizeof(PMC)
    k32 = ctypes.WinDLL("kernel32"); k32.GetCurrentProcess.restype = wintypes.HANDLE
    ps = ctypes.WinDLL("psapi"); ps.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(PMC), wintypes.DWORD]
    ps.GetProcessMemoryInfo.restype = wintypes.BOOL
    if not ps.GetProcessMemoryInfo(k32.GetCurrentProcess(), ctypes.byref(c), c.cb):
        raise RuntimeError("GetProcessMemoryInfo a echoue")
    return c.PeakWorkingSetSize / 1048576.0
KS = [-3, 3, 8]
ABSORBEURS = [("A", "F2", 0, 80), ("B", "F2", 0, 100)]
KAPPA = {8: "0.00928", 12: "0.00558", 16: "0.00382"}
W2 = F(101, 50)
def couplage(m):
    return float("%.5e" % (float(F(KAPPA[m])) * abs(float(W2) - 2.0) * M.P / M.X_saut_reel(M.P, M.CANAL[0], M.CANAL[1], 0.0, 0.0, W2)))
CAS = [(m, W2, couplage(m)) for m in (8, 12, 16)]
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
        print("  geometrie de %d barreaux, w2 = %s, g = %.3e, r_c = %d, absorbeur %s (N = %d) : %d/%d suivis, %.1f s, largeur du jumeau de %.1e a %.1e" % (
            mb, rec["w2"], g, r_c, nom, N, sum(s_), len(KS), dt, min(g_), max(g_)), flush=True)
    rec.update({"lectures": lus, "suivies": suivis, "plus_grande_largeur": pire, "duree_totale_s": round(time.time() - t0, 1),
                "memoire_max_Mo": round(pic_memoire_Mo(), 0)})
    out["cas"].append(rec)
    print("  -> %d lectures, %d suivies, plus grande largeur du jumeau %.2e, %.0f s en tout, memoire max %.0f Mo" % (lus, suivis, pire, time.time() - t0, rec["memoire_max_Mo"]), flush=True)
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
