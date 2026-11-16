# -*- coding: ascii -*-
"""SONDE DU VIDE A PROFONDEUR LISIBLE -- machine 1, v1, 2026-11-16. Hors chaine, classe 3. Aucun calcul 2D.
Etat (0, 0), barrieres de 2 a 6 sites, petits desaccords : la loi d'echelle, la forme fermee a trois termes, et ce
que les chaines d'ordre 2 et 3 (blocs deposes) en disent, avec leur stabilite sous l'absorbeur de la chaine.
Sert a dire si une prediction du vide est possible la ou un lecteur 2D lit (Gamma / |delta| au-dessus de 3e-11).
Les constantes de la forme fermee (B = 2 I, c_L, d_L de l'etiquette (0, 0)) sont LUES dans forme_phi_v1.json.
Usage : python3 -I sonde_vide_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <phi_echelle.py> <carte.py> <forme_phi.json> <sortie.json>"""
import sys, math, json, importlib.util
MOTEUR, BLOC2, BLOC3, PHI, CARTE, FORME, SORTIE = sys.argv[1:8]
sys.argv = [CARTE, MOTEUR, BLOC2, BLOC3, PHI, SORTIE]
spec = importlib.util.spec_from_file_location("carte", CARTE); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
PH = C.PH; M = C.M
from fractions import Fraction as F
XC = M.coeff_homogene_X_s(F(2))
FP = json.load(open(FORME)); B = 2.0 * FP["I"]
ref = [x for x in FP["B"] if (x["n1"], x["n2"], x["M0"]) == (0, 0, 4096)][0]
C0, D0 = ref["c_L"], -ref["reste3"]               # c_L derive, d_L lu a 4096 barreaux
print("constantes lues : B = %.9f, c_L = %.6f, d_L = %.4f" % (B, C0, D0))
out = {"points": [], "constantes": {"B": B, "c_L": C0, "d_L": D0}}
print("  m_cible  kappa       M0      nu0*    -ln Phi   forme fermee  ecart    | delta      g           Gamma/|delta|   r2        r3        stab3")
for mc in (2, 3, 4, 5, 6):
    k, kb, kh = C.kappa_pour_m_bord(0, 0, mc)
    lam = k * XC / (M.P * PH.tau(0, 0, 0)); M0 = (2.0 * lam) ** (-2.0 / 3.0); nu = M0 / ((5.0 / 2.0) ** (2.0 / 3.0) * (5.0 / 3.0))
    f = PH.phi_fc(k, 0, 0); ferme = -B * M0 + C0 * math.log(M0) + D0
    for d in (-0.02, -0.01, -0.005, 0.005, 0.01, 0.02):
        C._cache.clear()
        p = C.point(0, 0, k, d)
        p.update({"m_cible": mc, "M0": M0, "nu0": nu, "forme_fermee": ferme})
        out["points"].append(p)
        if p["vide"]:
            print("  %4d    %.4e  %6.3f  %6.3f  %8.3f   %9.3f   %+.3f   | %+.4f   %s" % (mc, k, M0, nu, -f["ln_Phi"], -ferme, f["ln_Phi"] - ferme, d, p["motif"])); continue
        print("  %4d    %.4e  %6.3f  %6.3f  %8.3f   %9.3f   %+.3f   | %+.4f   %.3e   %.3e       %+.4f   %+.4f   %s" % (
            mc, k, M0, nu, -f["ln_Phi"], -ferme, f["ln_Phi"] - ferme, p["delta"], p["g"], math.exp(p["ln_Phi"]),
            p["r2"], p["r3"], ("%.4f" % p["stab3"]) if p["stab3"] is not None else "-"))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
