# -*- coding: ascii -*-
"""ELIGIBILITE DES CELLULES CANDIDATES DU GEL "PONT" -- machine 1, v1, 2026-11-17.
Derive de eligibilite_vide_machine1_v1.py (registre, 34eb68229983b1f2) : memes cellules (w2, profondeur m), meme couplage
ecrit, meme barriere, memes tables, meme absorbeur adapte. CHANGENT : les creneaux (MG et PG seuls, sans les deux w2 que le
gel du vide a tires), les profondeurs (3, 4, 5), et DEUX conditions de plus, hors de l'energie du vide.
CHAINE SEULE : aucun calcul 2D, ni dense ni creux. Etat : celui que porte le site (0, 0).
    g = kappa_m |w2 - 2| P / X_saut_reel(P, 2, 1, 0, 0, w2), ARRONDI a six chiffres significatifs ("%.5e").
DENSITE du site 0 a l'ecart x, ordre o, variante (a, c, L) de l'absorbeur adapte :
    H = matrice de la chaine d'ordre o sous la variante ; E_v = partie reelle de la valeur propre de H dont le vecteur propre
    porte le plus grand poids sur le site 0 ; E = E_v - x (w2 - 2), c'est-a-dire du cote OPPOSE au desaccord ;
    rho = -(1 / pi) Im [ (E - H)^(-1) ]_00 , lue ici par le flux : (1 / pi) somme_m W_m |y_m|^2 , y = (E - H)^(-1) e_0.
    LISSE rho_o(x) : exponentielle de la mediane des dix-huit ln rho ; ETENDUE : max - min des dix-huit ln rho.
La cellule est ELIGIBLE si : (i) la barriere finit au site m ; (ii) e_bord < 0.7 ; (iii) les dix-huit largeurs au vide sont
strictement positives et leur etendue est <= 0.02 ; (iv) a chacun des douze ecarts x, les dix-huit densites d'ordre 3 sont
strictement positives et leur etendue est <= 0.03 ; (v) a chacun des douze ecarts, |ln rho_2(x) - ln rho_3(x)| <= 0.10.
Un w2 est ELIGIBLE si ses trois cellules le sont.
Usage : python3 -I eligibilite_pont_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <sortie.json> <creneau> [<creneau>]
        python3 -I eligibilite_pont_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <sortie.json> --controle <lisse_chaine_v1.json>"""
import sys, math, json, time, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A, SORTIE = sys.argv[1:6]
ARGS = sys.argv[6:]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
assert M.P == 5 and tuple(M.CANAL) == (2, 1) and M.W1 == 1
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):                    # memoire des appels : memes valeurs, moins de calcul
    cle = (p, k, l, n1, n2, w2)
    if cle not in _cache:
        _cache[cle] = _brut(p, k, l, n1, n2, w2)
    return _cache[cle]
M.X_saut_reel = _X
for bloc in (BLOC2, BLOC3, BLOC_A):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))

EXCLUS = (F(1982, 1000), F(2017, 1000))          # tires et joues en 2D par le gel "largeur du vide" (delta 102)
CRENEAUX = {"MG": [F(k, 1000) for k in range(1981, 1990) if F(k, 1000) not in EXCLUS],
            "PG": [F(k, 1000) for k in range(2011, 2020) if F(k, 1000) not in EXCLUS]}
ORDRE = ("MG", "PG")
KAPPA = {3: "0.0262", 4: "0.0200", 5: "0.0159"}
PROFONDEURS = (3, 4, 5)
ECARTS = (0.05, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0)
SEUIL_ETENDUE = 0.02; SEUIL_ETENDUE_RHO = 0.03; SEUIL_PAS = 0.10; GARDE_E_BORD = 0.7; M_FACTEUR = 4

def couplage(w2, m):
    """Le couplage de la cellule : le decimal a six chiffres significatifs, et son flottant."""
    brut = float(F(KAPPA[m])) * abs(float(w2) - 2.0) * M.P / _brut(M.P, M.CANAL[0], M.CANAL[1], 0.0, 0.0, w2)
    texte = "%.5e" % brut
    return texte, float(texte)

def lisse(tb, t3, ordre):
    """Par ecart : mediane et etendue des dix-huit ln rho (None si une densite n'est pas strictement positive)."""
    LN = []
    for (a, c, L) in VARIANTES_ADAPTEES:
        H, Wd, i0 = matrice_adaptee(tb, t3, a, c, L, ordre)
        val, vec = np.linalg.eig(H); nu = np.lexsort((val.real, -np.abs(vec[i0, :]) ** 2))[0]; Ev = float(val[nu].real)
        e0 = np.zeros(len(H), dtype=complex); e0[i0] = 1.0; r = []
        for x in ECARTS:
            y = np.linalg.solve((Ev - x * tb["d"]) * np.eye(len(H)) - H, e0)
            v = float((Wd @ (np.abs(y) ** 2)) / math.pi)
            r.append(math.log(v) if (v > 0.0 and math.isfinite(v)) else None)
        LN.append(r)
    med, et = [], []
    for i in range(len(ECARTS)):
        col = [r[i] for r in LN]
        if any(v is None for v in col):
            med.append(None); et.append(None); continue
        s = sorted(col); n = len(s); med.append(0.5 * (s[n // 2 - 1] + s[n // 2])); et.append(s[-1] - s[0])
    return med, et

def cellule(w2, m):
    g_txt, g = couplage(w2, m)
    rec = {"m": m, "kappa": KAPPA[m], "g": g_txt}
    sites = M.barriere(0.0, 0.0, w2, g, True)
    if not sites:
        rec.update({"eligible": False, "motif": "barriere vide"}); return rec
    m_bord, e_bord = sites[-1][0], sites[-1][1]
    rec.update({"m_bord": m_bord, "e_bord": e_bord, "r_c": 2 * (m_bord + max(8, m_bord)) + 2})
    tb = tables_ordre2(0.0, 0.0, w2, g, sites, M_facteur=M_FACTEUR); t3 = tables_ordre3(0.0, 0.0, w2, g, tb)
    assert abs(tb["d"] - (float(w2) - 2.0)) < 1e-15
    pl = plateau_adapte(tb, t3, 3)
    d = abs(float(w2) - 2.0)
    rec.update({"ln_G3": pl["ln_G"], "etendue": pl["etendue"], "poids_min": pl["poids_min"], "methodes": sorted(set(x[:2] for x in pl["methodes"]))})
    r3, e3 = lisse(tb, t3, 3); r2, e2 = lisse(tb, t3, 2)
    pas = [None if (a is None or b is None) else a - b for a, b in zip(r2, r3)]
    rec.update({"ln_rho3": r3, "etendue_rho3": e3, "pas_2_3": pas,
                "etendue_rho_max": None if any(v is None for v in e3) else max(e3),
                "pas_max": None if any(v is None for v in pas) else max(abs(v) for v in pas),
                "ln_rho3_8_delta": None if r3[-1] is None else r3[-1] + math.log(d)})
    motifs = []
    if m_bord != m: motifs.append("barriere a %d barreaux" % m_bord)
    if not e_bord < GARDE_E_BORD: motifs.append("e_bord %.3f" % e_bord)
    if pl["ln_G"] is None: motifs.append("largeur non positive")
    elif not pl["etendue"] <= SEUIL_ETENDUE: motifs.append("etendue %.4f" % pl["etendue"])
    if rec["etendue_rho_max"] is None: motifs.append("densite non positive")
    elif not rec["etendue_rho_max"] <= SEUIL_ETENDUE_RHO: motifs.append("etendue du lisse %.4f" % rec["etendue_rho_max"])
    if rec["pas_max"] is None: motifs.append("pas indefini")
    elif not rec["pas_max"] <= SEUIL_PAS: motifs.append("pas de l'ordre 2 a l'ordre 3 %.4f" % rec["pas_max"])
    rec["eligible"] = not motifs
    if motifs: rec["motif"] = " ; ".join(motifs)
    return rec

if ARGS and ARGS[0] == "--controle":
    # Le script rend-il, au point sacrifie w2 = 101/50 (un centieme, non candidat), 3 barreaux, ce que l'exploration a calcule ?
    REF = json.load(open(ARGS[1])); w2 = F(101, 50)
    c = cellule(w2, 3); pire = 0.0; n = 0
    print("CONTROLE contre la piece de l'exploration (w2 = 101/50, 3 barreaux, non candidat) : couplage ecrit %s" % c["g"])
    assert list(REF["X"]) == list(ECARTS) and c["g"] == "%.5e" % REF["g"]
    for i, x in enumerate(ECARTS):
        e3 = abs(c["ln_rho3"][i] - REF["ordres"]["3"]["ln_rho"][i]); e2 = abs((c["ln_rho3"][i] + c["pas_2_3"][i]) - REF["ordres"]["2"]["ln_rho"][i])
        ee = abs(c["etendue_rho3"][i] - REF["ordres"]["3"]["etendue"][i]); pire = max(pire, e3, e2, ee); n += 3
    eg = abs(c["ln_G3"] - REF["ordres"]["3"]["ln_Gamma_vide"]); n += 1
    print("  %d comparaisons sur les densites, plus grand ecart %.2e ; ln de la largeur au vide : ecart %.2e (flux de l'exploration contre plateau du bloc)" % (n - 1, pire, eg))
    print("  la cellule sous la regle : etendue %.4f ; etendue du lisse au plus %.4f ; pas de l'ordre 2 a l'ordre 3 au plus %.4f ; %s" % (
        c["etendue"], c["etendue_rho_max"], c["pas_max"], "ELIGIBLE" if c["eligible"] else "INELIGIBLE (%s)" % c["motif"]))
    ok = n == 37 and pire < 1e-9 and eg < 1e-9
    print("CONTROLE : %s" % ("TIENT" if ok else "NE TIENT PAS"))
    json.dump({"comparaisons": n, "pire_ecart": pire, "ecart_largeur": eg, "tient": ok, "cellule": c}, open(SORTIE, "w"), indent=1, sort_keys=True)
    sys.exit(0 if ok else 1)

assert all(s in CRENEAUX for s in ARGS) and ARGS, "creneaux : MG PG"
out = {"regle": {"kappa": KAPPA, "profondeurs": PROFONDEURS, "ecarts": ECARTS, "seuil_etendue": SEUIL_ETENDUE, "seuil_etendue_rho": SEUIL_ETENDUE_RHO,
                 "seuil_pas": SEUIL_PAS, "garde_e_bord": GARDE_E_BORD, "M_facteur": M_FACTEUR, "variantes": VARIANTES_ADAPTEES,
                 "exclus": ["%d/%d" % (w.numerator, w.denominator) for w in EXCLUS]},
       "creneaux": {}}
t0 = time.time()
for s in ARGS:
    cands = []
    print("creneau %s : %d w2 candidats" % (s, len(CRENEAUX[s])), flush=True)
    for w2 in CRENEAUX[s]:
        cs = [cellule(w2, m) for m in PROFONDEURS]
        el = all(c["eligible"] for c in cs)
        cands.append({"w2": "%d/%d" % (w2.numerator, w2.denominator), "eligible": el, "cellules": cs})
        print("  %.3f  %s  %s" % (float(w2), "  ".join("m%d %s %s %s %s%s" % (c["m"], c["g"], ("%.4f" % c["etendue"]) if c.get("etendue") is not None else "----",
              ("%.4f" % c["etendue_rho_max"]) if c.get("etendue_rho_max") is not None else "----", ("%.4f" % c["pas_max"]) if c.get("pas_max") is not None else "----",
              "" if c["eligible"] else " !") for c in cs), "ELIGIBLE" if el else "INELIGIBLE"), flush=True)
    out["creneaux"][s] = {"candidats": cands}
    print("  -> %d w2 eligibles sur %d ; %.0f s" % (sum(c["eligible"] for c in cands), len(cands), time.time() - t0), flush=True)
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit : %s" % SORTIE)
