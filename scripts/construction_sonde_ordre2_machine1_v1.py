# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1, 2026-11-14. Construit la sonde du gel "chaine d'ordre 2" a partir de la sonde
# certifiee du gel precedent (940a21b1d562bb49) par hunks ancres, le bloc d'ordre 2 etant insere tel quel.
# usage : python3 -I construction_sonde_ordre2_machine1_v1.py <sonde_domaine_G1_v1.py> <bloc.py> <sortie.py>
import sys, hashlib, unicodedata
src, bloc, dst = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding="ascii").read()
b = open(bloc, encoding="ascii").read()
canon = lambda s: hashlib.sha256(unicodedata.normalize("NFC", s).replace("\r\n", "\n").encode("utf-8")).hexdigest()[:16]
assert canon(t) == "940a21b1d562bb49", canon(t)
n = [0]
def H(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:70])
    t = t.replace(old, new); n[0] += 1

H('''"""SONDE DU GEL "LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT" -- machine 1, v1, 2026-11-14.
ELLE MESURE ET NE JUGE PAS : aucun rapport chaine / 2D n'est affiche, aucun seuil du gel n'est applique.
Derivee par hunks de sonde_chaine_par_etat_machine1_v1.py (acf7e26dedfa8abc) : memes mesures ; autres points ;
EN PLUS, a chaque point, la garde de domaine G-1 du moteur, calculee comme mesurer_point la calcule
(seuil_A4 puis garde_domaine), CONSIGNEE et jamais appliquee : la sonde lit la chaine que la garde dise
EN DOMAINE ou HORS DOMAINE.
Usage : python -P sonde_domaine_G1_machine1_v1.py <moteur_v17.py> <sortie.json> [id ...]
Sans id : les quatorze points du gel. Avec id : ces points seulement (essai a blanc ; machine 1 ne joue que A1 A2).
''', '''"""SONDE DU GEL "LA CHAINE E-A AU SECOND ORDRE" -- machine 1, v1, 2026-11-14.
ELLE MESURE ET NE JUGE PAS : aucun rapport chaine / 2D n'est affiche, aucun seuil du gel n'est applique.
Derivee par hunks de sonde_domaine_G1_machine1_v1.py (940a21b1d562bb49) : memes mesures 2D, meme chaine du moteur,
meme garde du moteur consignee et jamais appliquee ; autres points ;
EN PLUS, pour chaque etat, la CHAINE D'ORDRE 2 (bloc insere ci-dessous : deplacements Sigma2, saut au second voisin,
sites m < 0), a quatre eta de chaine, et l'energie libre du site de l'etiquette. Le moteur n'est pas modifie.
Usage : python -P sonde_ordre2_machine1_v1.py <moteur_v17.py> <sortie.json> [id ...]
Sans id : les seize points du gel. Avec id : ces points seulement (essai a blanc ; machine 1 ne joue que A1 A2).
''')
H('''    ("E1", "juge", F(52, 25), F(1)), ("E2", "juge", F(209, 100), F(1)),
    ("E3", "juge", F(21, 10), F(3, 2)), ("E4", "juge", F(53, 25), F(3, 2)),
    ("E5", "juge", F(191, 100), F(1)), ("E6", "juge", F(19, 10), F(3, 2)),
    ("H1", "juge", F(52, 25), F(2, 3)), ("H2", "juge", F(21, 10), F(2, 3)),
    ("H3", "juge", F(53, 25), F(1)), ("H4", "juge", F(191, 100), F(2, 3)),
    ("H5", "juge", F(19, 10), F(2, 3)), ("H6", "juge", F(189, 100), F(1)),
    ("A1", "ancre", F(39, 20), F(1)), ("A2", "ancre", F(41, 20), F(1)),
''', '''    ("C1", "juge", F(197, 100), F(2, 3)), ("C2", "juge", F(97, 50), F(3, 4)),
    ("C3", "juge", F(203, 100), F(3, 2)), ("C4", "juge", F(103, 50), F(4, 3)),
    ("M1", "juge", F(193, 100), F(1)), ("M2", "juge", F(48, 25), F(4, 3)),
    ("M3", "juge", F(207, 100), F(2, 3)), ("M4", "juge", F(21, 10), F(3, 4)),
    ("L1", "juge", F(189, 100), F(4, 3)), ("L2", "juge", F(47, 25), F(1)),
    ("L3", "juge", F(211, 100), F(3, 2)), ("L4", "juge", F(53, 25), F(2, 3)),
    ("A1", "ancre", F(39, 20), F(1)), ("A2", "ancre", F(41, 20), F(1)),
    ("W1", "temoin", F(107, 50), F(1)), ("W2", "temoin", F(209, 100), F(1, 2)),   # les temoins en dernier
''')
H('''EF_CHAINE = (0.25, 0.125, 0.0625, 0.03125)
''', '''EF_CHAINE = (0.25, 0.125, 0.0625, 0.03125)

''' + b)
H('''        e["chaine"] = ch
''', '''        e["chaine"] = ch
        e["E_libre"] = float(M.energie_libre(float(n1), float(kk), w2)) if dans else None
        c2 = {"definie": False, "m_bord": None, "m_min": None, "gammas_flux": None, "gammas_im": None, "dE": None,
              "Sigma2_0": None, "erreur": None}
        if dans and ch["definie"]:
            try:
                tb = tables_ordre2(float(n1), float(kk), w2, g, sites, M_facteur=4)
                rs = [gamma_chaine_ordre2(tb, ef) for ef in EF_CHAINE]
                c2.update({"definie": True, "m_bord": int(tb["m2_bord"]), "m_min": int(tb["m_min"]),
                           "gammas_flux": [r["Gamma_flux"] for r in rs], "gammas_im": [r["Gamma_c2"] for r in rs],
                           "dE": [r["dE"] for r in rs], "Sigma2_0": float(tb["S"][0])})
            except BaseException as x:          # se consigne, ne se rattrape pas
                c2["erreur"] = "%s: %s" % (type(x).__name__, str(x)[:200])
        e["chaine2"] = c2
''')
H('''    sortie = {"sonde": "sonde_domaine_G1_machine1_v1", "moteur_canon": canon_B(MOTEUR),''',
  '''    sortie = {"sonde": "sonde_ordre2_machine1_v1", "moteur_canon": canon_B(MOTEUR),''')
H('''                          "ef_chaine": list(EF_CHAINE), "potentiel": "x5", "signe_fantome": -1, "P": int(M.P)},''',
  '''                          "ef_chaine": list(EF_CHAINE), "potentiel": "x5", "signe_fantome": -1, "P": int(M.P),
                          "ordre2": {"M_facteur": 4, "forme": "symetrique", "sites_bas": True,
                                     "sauts_hors_echelle": len(SAUTS_HORS_ECHELLE)}},''')
open(dst, "w", encoding="ascii", newline="\n").write(t)
print("hunks appliques : %d ; canon du bloc : %s ; canon de la sortie : %s" % (n[0], canon(b), canon(t)))
