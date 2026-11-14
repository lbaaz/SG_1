# -*- coding: ascii -*-
# CONSTRUCTION DU GEL "LA CHAINE E-A PAR ETAT, HORS PLAGE", v1 : le gabarit plus les canons des pieces du lot.
# machine 1, 2026-11-14. Arguments : <gabarit> <gel a ecrire>. Les pieces sont lues a cote du gabarit.
import sys, os, re, hashlib, unicodedata
GAB, GEL = sys.argv[1:3]
ICI = os.path.dirname(os.path.abspath(GAB))
def canon(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
PIECES = {"@@SONDE@@": "sonde_chaine_par_etat_machine1_v1.py", "@@FEUILLE@@": "lecture_chaine_par_etat_machine1_v1.py",
          "@@CONCEPTION@@": "conception_points_chaine_seule_machine1_v1.py",
          "@@CONCEPTION_LOG@@": "conception_points_chaine_seule_machine1_v1.log",
          "@@ESSAI_JSON@@": "sonde_essai_ancres_machine1.json", "@@ESSAI_LECTURE@@": "lecture_essai_ancres_machine1.log",
          "@@SELFTEST@@": "lecture_selftest_machine1.log"}
t = open(GAB, encoding="ascii").read()
for cle, nom in PIECES.items():
    assert t.count(cle) == 1, "gabarit : %s" % cle
    t = t.replace(cle, canon(os.path.join(ICI, nom)))
assert "@@" not in t, "gabarit non rempli"
assert all(ord(c) < 128 for c in t) and "%" not in t, "ASCII ou pour cent"
long_ = [i + 1 for i, l in enumerate(t.split("\n")) if len(l) > 100]
assert not long_, "lignes de plus de 100 colonnes : %s" % long_
# les constantes du gel sont celles de la feuille et de la sonde (controle de coherence, par le texte)
f = open(os.path.join(ICI, PIECES["@@FEUILLE@@"]), encoding="ascii").read()
s = open(os.path.join(ICI, PIECES["@@SONDE@@"]), encoding="ascii").read()
for motif, ou, quoi in (("SIGMA_J_MAX = 0.2", f, "ecart-type de J < 0.2"), ("POIDS_SITE_MIN = 0.5", f, "(n1, n2) >= 0.5"),
                        ("DIX_PLANCHERS = 1.33e-12", f, "Gamma_2D(3) > 1.33e-12"), ("SUIVI_MIN = 0.9", f, "suivi >= 0.9"),
                        ("STABILITE_CIBLE = 2.0", f, "k = 2, 3, 4 <= 2"), ("ETALEMENT_CHAINE = 2.0", f, "quatre valeurs <= 2"),
                        ("MIN_JUGES = 6", f, "moins de 6 etats juges"), ("MIN_POINTS_LISIBLES = 4", f, "moins de 4 des 6"),
                        ("TOL_ANCRE = 1e-2", f, "a 1e-2 pres"), ("2.1623273017950654e-10", f, "2.1623273017950654e-10"),
                        ("2.6613925716641374e-09", f, "2.6613925716641374e-09"), ("N_ETATS = 14", f, "les 14 etats"),
                        ("FRACTION, L_BOITE, N_ETATS = 0.70, 20, 14", s, "N = r_c + 20"), ("KS = (2, 3, 4)", s, "pour k = 2, 3, 4"),
                        ("EF_CHAINE = (0.25, 0.125, 0.0625, 0.03125)", s, "1/4, 1/8, 1/16, 1/32"),
                        ('("J5", "juge", F(39, 20), F(2, 3))', s, "J5  w2 = 39/20  facteur 2/3"),
                        ('"J2": ("juge", "21/10", "1/1")', f, "J2  w2 = 21/10  facteur 1")):
    assert motif in ou, "constante absente du script : " + motif
    assert quoi in t, "phrase absente du gel : " + quoi
assert "SELFTEST : 26 cas, 26 tenus" in open(os.path.join(ICI, PIECES["@@SELFTEST@@"])).read()
open(GEL, "w", encoding="ascii", newline="\n").write(t)
print("gel %s : canon %s, %d lignes, %d octets" % (os.path.basename(GEL), canon(GEL), len(t.split("\n")) - 1, len(t.encode())))
