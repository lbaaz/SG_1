# -*- coding: ascii -*-
"""ESSAI A L'AVEUGLE DU CHEMIN delta < 0 DES DEUX SONDES -- machine 1, v1, 2026-11-17. Hors chaine.
Aucune 2D hors de l'energie du vide n'a ete regardee a delta < 0, a aucun w2, et cet essai ne la regarde pas : il lance
les deux sondes a un w2 NON CANDIDAT de desaccord negatif, dans un dossier temporaire, et n'en rend que le code de
sortie et des BOOLEENS de forme. Aucun nombre des sorties (energie, densite, poids, compte, ecart) n'est imprime ni
garde ; les sorties sont detruites avec le dossier. Le journal de cet essai est la seule trace.
Le w2 d'essai est le premier de la liste 197/100, 39/20, 79/40 dont la barriere, calculee par le moteur seul, finit au
site 3 au couplage ecrit de la regle (kappa_3).
Usage : python3 -I -B ce_script <registre> <bloc chaine du pont> <sonde de densite> <sonde de boite fermee>"""
import sys, os, json, math, subprocess, tempfile, importlib.util
from fractions import Fraction as F
REG, BLOC_P, S_DENS, S_BOITE = sys.argv[1].rstrip("/"), sys.argv[2], sys.argv[3], sys.argv[4]
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
src = open(BLOC_P, encoding="ascii").read(); exec(compile(src, BLOC_P, "exec"))
CANDIDATS_DU_GEL = [F(k, 1000) for k in list(range(1981, 1990)) + list(range(2011, 2020))]
choix = None
for w2 in (F(197, 100), F(39, 20), F(79, 40)):
    assert w2 not in CANDIDATS_DU_GEL and w2 < 2
    g = couplage_pont(w2, 3); sites = M.barriere(0.0, 0.0, w2, float(g), True)
    if sites and sites[-1][0] == 3:
        choix = (w2, g); break
if choix is None: raise SystemExit("aucun w2 d'essai n'a une barriere de 3 barreaux")
w2, g = choix; w2s = "%d/%d" % (w2.numerator, w2.denominator)
print("w2 d'essai : %s (delta = %+.3f, non candidat), 3 barreaux, couplage ecrit %s" % (w2s, float(w2) - 2.0, g))
ok = True
with tempfile.TemporaryDirectory() as tmp:
    r = subprocess.run([sys.executable, "-I", "-B", S_DENS, REG, w2s, "3", g, "A", tmp + "/d.json", "3"], capture_output=True, text=True)
    print("sonde de densite (absorbeur A, barreau k = 3) : code de sortie %d" % r.returncode); ok &= r.returncode == 0
    if r.returncode == 0:
        d = json.load(open(tmp + "/d.json")); k = d["k"]["3"]
        b = {"delta negatif": d["delta"] < 0, "vide suivi": bool(k["suivi"]), "douze densites": len(k.get("rho_flux", [])) == 12,
             "densites finies et positives": all(v > 0 and math.isfinite(v) for v in k.get("rho_flux", [])),
             "flux et lecture directe d'accord a 1e-6": all(abs(a / c - 1.0) < 1e-6 for a, c in zip(k.get("rho_direct", []), k.get("rho_flux", [])))}
        for nom, v in b.items(): print("   %s : %s" % (nom, "oui" if v else "NON")); ok &= v
    r = subprocess.run([sys.executable, "-I", "-B", S_BOITE, REG, w2s, "3", g, tmp + "/b.jsonl", "60"], capture_output=True, text=True)
    print("sonde de boite fermee (cote 60) : code de sortie %d" % r.returncode); ok &= r.returncode == 0
    if r.returncode == 0:
        box = json.loads(open(tmp + "/b.jsonl").readline()); nv = box["niveaux"]
        b = {"delta negatif": box["delta"] < 0, "niveau-vide suivi (poids >= 0.5, residu <= 1e-9)": box["w0"] >= 0.5 and box["residu_vide"] <= 1e-9,
             "les deux lectures debordent la fenetre": bool(box["couverte_a"] and box["couverte_b"]), "memes niveaux aux deux lectures": bool(box["listes_identiques"]),
             "tous les ecarts dans la fenetre": all(0.05 < v["x"] < 8.0 for v in nv), "toutes les energies au-dessus du vide": all(v["E"] > box["E_vide"] for v in nv),
             "tous les poids finis et positifs": all(v["c2_a"] > 0 and math.isfinite(v["c2_a"]) and v["c2_b"] is not None and v["c2_b"] > 0 for v in nv),
             "tous les niveaux fiables": all(v["fiable"] for v in nv)}
        for nom, v in b.items(): print("   %s : %s" % (nom, "oui" if v else "NON")); ok &= v
print("ESSAI A L'AVEUGLE : %s. Les sorties sont detruites ; aucun de leurs nombres n'a ete imprime." % ("le chemin delta < 0 s'execute" if ok else "ECHEC"))
sys.exit(0 if ok else 1)
