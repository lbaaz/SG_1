# -*- coding: utf-8 -*-
# Densite locale du site 0 de la chaine sous absorbeur adapte, hors de l'energie du vide, lue par le flux.
# Hors chaine, classe 3, point sacrifie. Blocs du registre (canons controles), non modifies.
# Usage : python3 -I lisse_chaine_machine1_v1.py <registre> <sortie.json>
import sys, os, math, json, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
import numpy as np
mp = None      # le bloc adapte ne se sert de mpmath que dans sa reprise en precision arbitraire, non appelee ici
REG, SORTIE = sys.argv[1].rstrip("/"), sys.argv[2]
CANONS = {"m17_chaine_v17.py": "82a0be882568fe0c", "chaine_ordre2_bloc_machine1_v1.py": "7cd5977bc27bebc1",
          "ordre3_bloc_machine1_v1.py": "534ba246aa3b8973", "chaine_adaptee_bloc_machine1_v1.py": "49a40d9098b55361"}
def canon_B(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
for nom, c in CANONS.items():
    if canon_B(REG + "/scripts/" + nom) != c: raise SystemExit("REFUS : canon de %s" % nom)
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = REG + "/scripts/" + bloc; exec(compile(open(p, encoding="ascii").read(), p, "exec"))
W2 = F(101, 50); AD = abs(float(W2) - 2.0); g = 5.53067e-03
X = [0.05, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
sites = M.barriere(0, 0, W2, g, True); tb = tables_ordre2(0, 0, W2, g, sites); t3 = tables_ordre3(0, 0, W2, g, tb)
print("barriere : m_bord = %d ; d = %+.4f ; tables jusqu'au site %d" % (tb["m2_bord"], tb["d"], tb["Mh"]))
def matrice(a, c, L, ordre):
    if ordre in (2, 3): return matrice_adaptee(tb, t3, a, c, L, ordre)
    H, Wd, i0 = matrice_adaptee(tb, t3, a, c, L, 2)          # ordre 1 : sauts t seuls, energies libres m d, meme absorbeur
    n = len(H); H1 = np.zeros((n, n), dtype=complex); m_min = tb["m_min"]
    for i in range(n):
        m = i + m_min; H1[i, i] = m * tb["d"] - 1j * Wd[i]
        if i + 1 < n: H1[i, i + 1] = tb["t"][m]; H1[i + 1, i] = tb["t"][m]
    return H1, Wd, i0
out = {"X": X, "ordres": {}, "delta_abs": AD, "g": g}
for ordre in (1, 2, 3):
    LN = []; EV = []; G0 = []; DIR = []
    for (a, c, L) in VARIANTES_ADAPTEES:
        H, Wd, i0 = matrice(a, c, L, ordre)
        val, vec = np.linalg.eig(H); nu = int(np.lexsort((val.real, -np.abs(vec[i0, :]) ** 2))[0]); Ev = float(val[nu].real)
        psi2 = np.abs(vec[:, nu]) ** 2; G0.append(float(2.0 * (Wd @ psi2) / psi2.sum()))
        e0 = np.zeros(len(H), dtype=complex); e0[i0] = 1.0; r = []
        for x in X:
            y = np.linalg.solve((Ev - x * AD) * np.eye(len(H)) - H, e0)
            r.append(float((Wd @ (np.abs(y) ** 2)) / math.pi))
            DIR.append(abs((-y[i0].imag / math.pi) / r[-1] - 1.0))      # la forme directe -Im G_00 / pi, celle des grandes boites
        LN.append([math.log(v) for v in r]); EV.append(Ev)
    LN = np.array(LN); med = np.median(LN, axis=0); et = LN.max(axis=0) - LN.min(axis=0)
    lnG = float(np.median(np.log(G0)))
    out["ordres"][str(ordre)] = {"ln_rho": med.tolist(), "etendue": et.tolist(), "E_vide": float(np.median(EV)), "ln_Gamma_vide": lnG,
                                 "etendue_Gamma_vide": float(np.log(G0).max() - np.log(G0).min())}
    print("ordre %d : E_vide %+.6e ; Gamma au vide %.4e (etendue %.1e) ; 2 pi x^2 delta^2 rho / Gamma : %s"
          % (ordre, np.median(EV), math.exp(lnG), np.log(G0).max() - np.log(G0).min(), "  ".join("%.3f" % (2 * math.pi * (x * AD) ** 2 * math.exp(m) / math.exp(lnG)) for x, m in zip(X, med))))
    print("          etendue des ln rho entre les dix-huit variantes : %s" % "  ".join("%.1e" % e for e in et))
    print("          forme directe (-Im G_00 / pi) contre flux : ecart relatif au plus %.1e sur %d lectures" % (max(DIR), len(DIR)))
    out["ordres"][str(ordre)]["direct_contre_flux_max"] = float(max(DIR))
o1, o2, o3 = (np.array(out["ordres"][k]["ln_rho"]) for k in "123")
print("x (|delta|)             : %s" % "  ".join("%5.2f" % x for x in X))
print("rho ordre 1 / ordre 3   : %s" % "  ".join("%.3f" % v for v in np.exp(o1 - o3)))
print("rho ordre 2 / ordre 3   : %s" % "  ".join("%.3f" % v for v in np.exp(o2 - o3)))
print("log10 rho ordre 3       : %s" % "  ".join("%.2f" % (v / math.log(10)) for v in o3))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
