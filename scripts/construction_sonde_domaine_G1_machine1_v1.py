# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1. Construit la sonde du gel "domaine G-1" a partir de la sonde
# certifiee du gel precedent (acf7e26dedfa8abc) par hunks ancres. usage : <sonde_v1.py> <sortie.py>
import sys, hashlib, unicodedata
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="ascii").read()
canon = lambda s: hashlib.sha256(unicodedata.normalize("NFC", s).replace("\r\n", "\n").encode("utf-8")).hexdigest()[:16]
assert canon(t) == "acf7e26dedfa8abc", canon(t)
n = [0]
def H(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:70])
    t = t.replace(old, new); n[0] += 1

H('''"""SONDE DU GEL "LA CHAINE E-A PAR ETAT, HORS PLAGE" -- machine 1, v1, 2026-11-14.
ELLE MESURE ET NE JUGE PAS : aucun rapport chaine / 2D n'est affiche, aucun seuil du gel n'est applique.
Usage : python -P sonde_chaine_par_etat_machine1_v1.py <moteur_v17.py> <sortie.json> [id ...]
Sans id : les douze points du gel. Avec id : ces points seulement (essai a blanc ; machine 1 ne joue que A1 A2).
''', '''"""SONDE DU GEL "LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT" -- machine 1, v1, 2026-11-14.
ELLE MESURE ET NE JUGE PAS : aucun rapport chaine / 2D n'est affiche, aucun seuil du gel n'est applique.
Derivee par hunks de sonde_chaine_par_etat_machine1_v1.py (acf7e26dedfa8abc) : memes mesures ; autres points ;
EN PLUS, a chaque point, la garde de domaine G-1 du moteur, calculee comme mesurer_point la calcule
(seuil_A4 puis garde_domaine), CONSIGNEE et jamais appliquee : la sonde lit la chaine que la garde dise
EN DOMAINE ou HORS DOMAINE.
Usage : python -P sonde_domaine_G1_machine1_v1.py <moteur_v17.py> <sortie.json> [id ...]
Sans id : les quatorze points du gel. Avec id : ces points seulement (essai a blanc ; machine 1 ne joue que A1 A2).
''')
H('''    ("J1", "juge", F(19, 10), F(1)), ("J2", "juge", F(21, 10), F(1)),
    ("J3", "juge", F(39, 20), F(3, 2)), ("J4", "juge", F(41, 20), F(3, 2)),
    ("J5", "juge", F(39, 20), F(2, 3)), ("J6", "juge", F(41, 20), F(2, 3)),
    ("T1", "temoin", F(49, 25), F(1)), ("T2", "temoin", F(51, 25), F(1)),
    ("T3", "temoin", F(37, 20), F(1)), ("T4", "temoin", F(43, 20), F(1)),
    ("A1", "ancre", F(39, 20), F(1)), ("A2", "ancre", F(41, 20), F(1)),
''', '''    ("E1", "juge", F(52, 25), F(1)), ("E2", "juge", F(209, 100), F(1)),
    ("E3", "juge", F(21, 10), F(3, 2)), ("E4", "juge", F(53, 25), F(3, 2)),
    ("E5", "juge", F(191, 100), F(1)), ("E6", "juge", F(19, 10), F(3, 2)),
    ("H1", "juge", F(52, 25), F(2, 3)), ("H2", "juge", F(21, 10), F(2, 3)),
    ("H3", "juge", F(53, 25), F(1)), ("H4", "juge", F(191, 100), F(2, 3)),
    ("H5", "juge", F(19, 10), F(2, 3)), ("H6", "juge", F(189, 100), F(1)),
    ("A1", "ancre", F(39, 20), F(1)), ("A2", "ancre", F(41, 20), F(1)),
''')
H('''          "faisable": bool(N <= M.N_MAX_EB), "etats": []}
''', '''          "faisable": bool(N <= M.N_MAX_EB), "etats": []}
    Oc = M.Omega_du_canal(w2)[0]            # garde G-1 du moteur : consignee, jamais appliquee
    gm = {"Omega_c": float(Oc), "D1": None, "c_max": None, "site_c_max": None, "statut": None, "erreur": None}
    try:
        gd = M.garde_domaine(w2, g, M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"], Oc)
        gm.update({"D1": float(gd["D1"]), "c_max": float(gd["c_max"]), "site_c_max": gd["site_c_max"],
                   "statut": gd["statut"]})
    except BaseException as x:
        gm["erreur"] = "%s: %s" % (type(x).__name__, str(x)[:200])
    pt["garde_moteur"] = gm
''')
H('''    sortie = {"sonde": "sonde_chaine_par_etat_machine1_v1", "moteur_canon": canon_B(MOTEUR),''',
  '''    sortie = {"sonde": "sonde_domaine_G1_machine1_v1", "moteur_canon": canon_B(MOTEUR),''')
H('''        print("%s %-6s w2=%s x%s g=%.6e graine=(%.3f, %.3f) r_c=%d N=%d : %s, %d etats, %s s" % (
            pid, role, pt["w2"], pt["facteur"], pt["g"], pt["graine"][0], pt["graine"][1], pt["r_c"], pt["N"],
''', '''        print("%s %-6s w2=%s x%s g=%.6e graine=(%.3f, %.3f) r_c=%d N=%d garde du moteur %s : %s, %d etats, %s s" % (
            pid, role, pt["w2"], pt["facteur"], pt["g"], pt["graine"][0], pt["graine"][1], pt["r_c"], pt["N"],
            pt["garde_moteur"]["statut"] or "EN ERREUR",
''')
open(dst, "w", encoding="ascii", newline="\n").write(t)
print("hunks appliques : %d ; canon de la sortie : %s" % (n[0], canon(t)))
