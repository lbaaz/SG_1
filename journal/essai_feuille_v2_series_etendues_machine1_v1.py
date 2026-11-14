# -*- coding: ascii -*-
# ESSAI A BLANC, NON OPPOSABLE : la feuille de lecture v2 (fonction
# juger_etage1, pas sa ligne de commande) appliquee a la sortie de la nuit du
# 12/11 completee, aux barreaux k = -5, -4, -3, par les largeurs du diagnostic
# de machine 2 (autre code, sans suivi). Il ne mesure rien et ne juge rien
# d'opposable : il verifie que la feuille v2 lit l'echelle du gel bis.
# Arguments : <feuille v2> <sonde_etage1.json de la nuit> <table> <dossier diagnostic> <journal>
import sys, os, json, copy, importlib.util
feuille, nuit, table, diagd, journal = sys.argv[1:6]
spec = importlib.util.spec_from_file_location("lec2", feuille)
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)
s1 = json.load(open(nuit))
ref = json.load(open(table))
n = 0
for g in ("G20", "G30"):
    for r in json.load(open(os.path.join(diagd, "diag_%s.json" % g), encoding="utf-8")):
        if -5 <= r["k"] <= -3:
            tr = s1["TP"]["j%02d" % r["j"]]["traj"]["F1" + g]
            assert str(r["k"]) not in tr
            tr[str(r["k"])] = {"k": r["k"], "eta": r["eta"], "saute": False, "etats": [
                {"suivi": True, "ov": None, "E_re": r["E_re"], "E_im": r["E_im"], "gamma": r["gamma"]}]}
            n += 1
L.dire.f = open(journal, "w", encoding="ascii", newline="\n")
L.dire("ESSAI A BLANC, NON OPPOSABLE : feuille v2 sur la nuit du 12/11 + %d largeurs du diagnostic (k = -5, -4, -3)" % n)
v, motifs, det = L.juger_etage1(s1, ref)
L.dire("essai a blanc : etage 1 %s %s ; TN %s" % (v, motifs, det["TN"]))
L.dire("-- FIN essai_feuille_v2_series_etendues_machine1_v1 --")
assert n == 12 and v == "TIENT" and motifs == []
