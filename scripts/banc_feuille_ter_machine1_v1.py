# -*- coding: ascii -*-
"""BANC QUI TUE de la feuille ter : chaque alteration du code de la feuille doit faire mordre son selftest.
Usage : python3 -I banc_feuille_ter_machine1_v1.py <feuille.py> <dossier de travail>"""
import sys, os, subprocess
SRC = open(sys.argv[1]).read(); TRAVAIL = sys.argv[2]
os.makedirs(TRAVAIL, exist_ok=True)
MUT = [
 ("M01 tolerance de plateau doublee", "TAU = Fraction(1, 20)", "TAU = Fraction(1, 10)"),
 ("M02 tolerance d'accord desserree", "TAU_F = 0.05", "TAU_F = 0.06"),
 ("M03 fenetre de quatre", "v = [ser.get(k) for k in range(k0, k0 + 5)]", "v = [ser.get(k) for k in range(k0, k0 + 4)]"),
 ("M04 borne stricte", "ok = mx <= (1 + TAU) * mn", "ok = mx < (1 + TAU) * mn"),
 ("M05 derniere fenetre oubliee", "for k0 in range(K_MIN, K_MAX - 3):", "for k0 in range(K_MIN, K_MAX - 4):"),
 ("M06 premiere fenetre oubliee", "for k0 in range(K_MIN, K_MAX - 3):", "for k0 in range(K_MIN + 1, K_MAX - 3):"),
 ("M07 fenetre de plus grand rapport", "cand = (not ok, mx / mn, k0)", "cand = (not ok, -mx / mn, k0)"),
 ("M08 a egalite le plus grand k", "cand = (not ok, mx / mn, k0)", "cand = (not ok, mx / mn, -k0)"),
 ("M09 moyenne arithmetique", '"Gamma_pl": math.exp(sum(math.log(x) for x in v) / 5.0)}', '"Gamma_pl": sum(v) / 5.0}'),
 ("M10 accord d'un seul cote", "return abs(math.log(a / b)) <= tau", "return math.log(a / b) <= tau"),
 ("M11 accord au temoin sans u_ref", "return e, e <= TAU_F + u_ref", "return e, e <= TAU_F"),
 ("M12 plancher de lisibilite remis", "math.isfinite(g) and g > 0.0", "math.isfinite(g) and g > 1e-12"),
 ("M13 suivi ignore", 'g = rec.get("gamma") if rec.get("suivi") else None', 'g = rec.get("gamma")'),
 ("M14 infini lisible", "g is not None and math.isfinite(g) and g > 0.0", "g is not None and g > 0.0"),
 ("M15 nul lisible", "math.isfinite(g) and g > 0.0", "math.isfinite(g) and g >= 0.0"),
 ("M16 non lisible avant echec", 'st = "NON QUALIFIE" if ech else ("NON LISIBLE" if nl else "QUALIFIE")', 'st = "NON LISIBLE" if nl else ("NON QUALIFIE" if ech else "QUALIFIE")'),
 ("M17 epreuve (d) oubliee", 'for x in ("B", "C", "D"):\n        if P["A"]["statut"]', 'for x in ("B", "C"):\n        if P["A"]["statut"]'),
 ("M18 epreuve (b) oubliee", 'for x in ("B", "C", "D"):\n        if P["A"]["statut"]', 'for x in ("C", "D"):\n        if P["A"]["statut"]'),
 ("M19 epreuve (c) oubliee", 'for x in ("B", "C", "D"):\n        if P["A"]["statut"]', 'for x in ("B", "D"):\n        if P["A"]["statut"]'),
 ("M20 accord entre absorbeurs desserre", "            if e > TAU_F:", "            if e > 2 * TAU_F:"),
 ("M21 absence de plateau non comptee", 'elif P[x]["statut"] == "PAS DE PLATEAU":', "elif False:"),
 ("M22 non lisible non compte", '        if P[x]["statut"] == "AUCUNE FENETRE":\n            nl.append(x)', '        if False:\n            nl.append(x)'),
 ("M23 consigne (e) toujours vraie", 'lu = accord(g_dep3, P["A"]["Gamma_pl"])', "lu = True"),
 ("M24 consigne (e) lue sans plateau", 'if P["A"]["statut"] == "PLATEAU" and g_dep3 is not None:', "if g_dep3 is not None:"),
 ("M25 onze etats lus suffisent", "    if q0 == len(JUGES):", "    if q0 >= len(JUGES) - 1:"),
 ("M26 part des etats stricte", "        if Fraction(nq) >= PART_ETATS * nj:", "        if Fraction(nq) > PART_ETATS * nj:"),
 ("M27 part des etats a huit dixiemes", "PART_ETATS = Fraction(9, 10)", "PART_ETATS = Fraction(8, 10)"),
 ("M28 part des etats ignoree", "        if Fraction(nq) >= PART_ETATS * nj:", "        if True:"),
 ("M29 par point a partir de deux", "    if q0 >= 1:", "    if q0 >= 2:"),
 ("M30 non qualifie et non lisible echanges", '    return "NON QUALIFIE" if n0 >= 1 else "NON LISIBLE"', '    return "NON LISIBLE" if n0 >= 1 else "NON QUALIFIE"'),
 ("M31 instrument ignore", '    if instrument != "TIENT":', "    if False:"),
 ("M32 run incomplet ignore", "    if sorted(pts) != sorted(JUGES):", "    if False:"),
 ("M33 depot : un manque tolere", "    if nlu == npl:", "    if nlu >= npl - 1:"),
 ("M34 depot : part stricte", "    if Fraction(nlu) >= PART_ETATS * npl:", "    if Fraction(nlu) > PART_ETATS * npl:"),
 ("M35 depot : aucun plateau non distingue", "    if npl == 0:", "    if False:"),
 ("M36 etage 0 sans plancher absolu", "<= TOL_E0_REL * g_dep + TOL_E0_ABS", "<= TOL_E0_REL * g_dep"),
 ("M37 etage 0 plancher absolu double", "TOL_E0_REL, TOL_E0_ABS = 1e-3, 1e-12", "TOL_E0_REL, TOL_E0_ABS = 1e-3, 2e-12"),
 ("M38 etage 0 tolerance relative doublee", "TOL_E0_REL, TOL_E0_ABS = 1e-3, 1e-12", "TOL_E0_REL, TOL_E0_ABS = 2e-3, 1e-12"),
 ("M39 etage 0 suivi ignore", "return bool(suivi) and g_lu is not None and", "return g_lu is not None and"),
 ("M40 etage 0 d'un seul cote", "abs(g_lu - g_dep) <= TOL_E0_REL", "(g_lu - g_dep) <= TOL_E0_REL"),
 ("M41 echelle raccourcie", "K_MIN, K_MAX = -3, 8", "K_MIN, K_MAX = -3, 7"),
 ("M42 plateau en flottants", "mx, mn = Fraction(max(v)), Fraction(min(v))", "mx, mn = max(v), min(v)"),
 ("M43 epreuve (a) rattachee a B", 'EPREUVE = {"A": "a", "B": "b", "C": "c", "D": "d"}', 'EPREUVE = {"A": "b", "B": "a", "C": "c", "D": "d"}'),
]
def jouer(nom, texte):
    f = os.path.join(TRAVAIL, nom + ".py"); open(f, "w", newline="\n").write(texte)
    return subprocess.run([sys.executable, "-I", f, "--selftest"], capture_output=True, text=True).returncode
base = jouer("base", SRC)
print("base saine : code %d (attendu 0)" % base)
mordues, survivantes, refus = 0, [], []
for nom, vieux, neuf in MUT:
    if SRC.count(vieux) != 1:
        refus.append((nom, SRC.count(vieux))); print("  %-44s CIBLE ABSENTE OU MULTIPLE (%d)" % (nom, SRC.count(vieux))); continue
    code = jouer(nom.split()[0], SRC.replace(vieux, neuf))
    if code == 1:
        mordues += 1; print("  %-44s MORDUE" % nom)
    else:
        survivantes.append(nom); print("  %-44s SURVIT (code %d)" % (nom, code))
print("BANC : %d alterations, %d mordues, %d survivantes %s, %d cibles refusees %s ; base saine : %s" % (
    len(MUT), mordues, len(survivantes), survivantes, len(refus), refus, base == 0))
sys.exit(0 if (base == 0 and mordues == len(MUT)) else 1)
