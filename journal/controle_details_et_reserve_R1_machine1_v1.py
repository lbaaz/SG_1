# -*- coding: ascii -*-
"""machine 1, 2026-11-17. Deux controles sur la certification par machine 2 du gel "pont", premiere partie.
(A) Ses DETAILS (sa chaine a elle, ecrite depuis le texte du gel) contre mes nombres, SANS arrondi : 48 cellules.
(B) Sa reserve R1 : Gamma = -2 Im(E) lu en double precision sur la valeur propre, contre la lecture du bloc depose
    (flux, ou precision arbitraire sous le seuil), sur MES matrices : ecart relatif, et effet sur l'etendue au vide.
Aucun script de machine 2 n'est lance : ses fichiers sont lus comme des donnees. CHAINE SEULE, aucune 2D.
Usage : python3 -I -B ce_script <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <ma table.json>
                                <details de machine 2.json> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A, MA_TABLE, DETAILS, SORTIE = sys.argv[1:8]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
assert M.P == 5 and tuple(M.CANAL) == (2, 1) and M.W1 == 1
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):
    cle = (p, k, l, n1, n2, w2)
    if cle not in _cache:
        _cache[cle] = _brut(p, k, l, n1, n2, w2)
    return _cache[cle]
M.X_saut_reel = _X
for bloc in (BLOC2, BLOC3, BLOC_A):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))

moi = json.load(open(MA_TABLE, encoding="utf-8"))
det = json.load(open(DETAILS, encoding="utf-8"))
mes = {}
for nom, cr in moi["creneaux"].items():
    for c in cr["candidats"]:
        for x in c["cellules"]:
            mes[(c["w2"], x["m"])] = x
ses = {(r["w2"], r["m"]): r for r in det}
res = {"A": {}, "B": {}}

# ---------- (A)
assert sorted(mes) == sorted(ses) and len(mes) == 48
pire = {"e_bord": 0.0, "etendue_vide": 0.0, "ln_plateau": 0.0, "ln_rho3": 0.0, "pas": 0.0, "etendue_lisse": 0.0,
        "pas_max": 0.0, "etendue_lisse_max": 0.0}
desaccords = {"g": 0, "eligible": 0, "m_bord": 0}
ECARTS = moi["regle"]["ecarts"]
for cle in sorted(mes):
    a, b = mes[cle], ses[cle]
    desaccords["g"] += a["g"] != b["g"]; desaccords["eligible"] += a["eligible"] != b["eligible"]
    desaccords["m_bord"] += a["m_bord"] != b["m_bord"]
    pire["e_bord"] = max(pire["e_bord"], abs(a["e_bord"] - b["e_bord"]))
    pire["etendue_vide"] = max(pire["etendue_vide"], abs(a["etendue"] - b["etendue_vide"]))
    pire["ln_plateau"] = max(pire["ln_plateau"], abs(a["ln_G3"] - math.log(b["plateau"])))
    pire["pas_max"] = max(pire["pas_max"], abs(a["pas_max"] - b["pas_max"]))
    pire["etendue_lisse_max"] = max(pire["etendue_lisse_max"], abs(a["etendue_rho_max"] - b["etendue_lisse_max"]))
    assert [e["x"] for e in b["ecarts"]] == list(ECARTS)
    for i, e in enumerate(b["ecarts"]):
        pire["ln_rho3"] = max(pire["ln_rho3"], abs(a["ln_rho3"][i] - e["ln3"]))
        pire["pas"] = max(pire["pas"], abs(a["pas_2_3"][i] - e["pas"]))
        pire["etendue_lisse"] = max(pire["etendue_lisse"], abs(a["etendue_rho3"][i] - e["etendue"]))
res["A"] = {"cellules": 48, "desaccords": desaccords, "plus_grand_ecart_absolu": pire}
# marges de la condition (v), lues chez elle et chez moi
pm = sorted((mes[c]["pas_max"], c) for c in mes)
dernier_el = max(v for v, c in pm if v <= 0.10); premier_in = min(v for v, c in pm if v > 0.10)
res["A"]["v_derniere_eligible"] = dernier_el; res["A"]["v_premiere_ecartee"] = premier_in
res["A"]["v_ecartees"] = sorted("%s m%d" % c for v, c in pm if v > 0.10)
res["A"]["max_autres"] = {"e_bord": max(mes[c]["e_bord"] for c in mes), "etendue_vide": max(mes[c]["etendue"] for c in mes),
                          "etendue_lisse": max(mes[c]["etendue_rho_max"] for c in mes)}
res["A"]["sa_colonne_gamma_double_max"] = max(r["gamma_double_vs_hp_rel"] for r in det)

# ---------- (B)
KAPPA = moi["regle"]["kappa"]
par_m = {3: 0.0, 4: 0.0, 5: 0.0}; change = {3: 0, 4: 0, 5: 0}; pire_etendue_double = 0.0; decisions_changent = 0
methodes = set()
for (w2s, m) in sorted(mes):
    w2 = F(w2s); g = float(mes[(w2s, m)]["g"])
    sites = M.barriere(0.0, 0.0, w2, g, True)
    tb = tables_ordre2(0.0, 0.0, w2, g, sites, M_facteur=moi["regle"]["M_facteur"]); t3 = tables_ordre3(0.0, 0.0, w2, g, tb)
    lb, ld = [], []
    for (a, c, L) in VARIANTES_ADAPTEES:
        G, meth, p = largeur_adaptee(tb, t3, a, c, L, 3); methodes.add(meth[:2])
        H, Wd, i0 = matrice_adaptee(tb, t3, a, c, L, 3)
        val, vec = np.linalg.eig(H); nu = np.lexsort((val.real, -np.abs(vec[i0, :]) ** 2))[0]
        Gd = float(-2.0 * val[nu].imag)
        par_m[m] = max(par_m[m], abs(Gd / G - 1.0))
        lb.append(math.log(G)); ld.append(math.log(Gd) if Gd > 0 else float("nan"))
    eb = max(lb) - min(lb); ed = max(ld) - min(ld)
    assert abs(eb - mes[(w2s, m)]["etendue"]) < 1e-12
    if abs(ed - eb) > 5e-5: change[m] += 1
    pire_etendue_double = max(pire_etendue_double, ed)
    decisions_changent += (ed <= 0.02) != (eb <= 0.02)
res["B"] = {"ecart_relatif_max_par_profondeur": {str(k): v for k, v in par_m.items()},
            "cellules_dont_l_etendue_change_de_plus_de_5e-5": {str(k): v for k, v in change.items()},
            "plus_grande_etendue_en_double": pire_etendue_double, "decisions_iii_qui_changent": decisions_changent,
            "methodes_du_bloc": sorted(methodes)}
json.dump(res, open(SORTIE, "w"), indent=1, sort_keys=True)
print(json.dumps(res, indent=1, sort_keys=True))
