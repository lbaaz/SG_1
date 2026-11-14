# -*- coding: ascii -*-
# CONSTRUCTION DU GEL "LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT", v1 : le gabarit plus les canons des
# pieces du lot, et les controles de coherence entre le texte, la sonde, la feuille et le journal de la garde.
# machine 1, 2026-11-14. Arguments : <gabarit> <gel a ecrire>. Les pieces sont lues a cote du gabarit.
import sys, os, re, hashlib, unicodedata
GAB, GEL = sys.argv[1:3]
ICI = os.path.dirname(os.path.abspath(GAB))
def canon(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
PIECES = {"@@SONDE@@": "sonde_domaine_G1_machine1_v1.py", "@@CONSTRUCTION_SONDE@@": "construction_sonde_domaine_G1_machine1_v1.py",
          "@@FEUILLE@@": "lecture_domaine_G1_machine1_v1.py", "@@SELFTEST@@": "lecture_selftest_machine1.log",
          "@@BANC@@": "banc_feuille_domaine_G1_machine1_v1.py", "@@BANC_LOG@@": "banc_feuille_domaine_G1_machine1_v1.log",
          "@@CONCEPTION@@": "conception_points_domaine_G1_machine1_v1.py",
          "@@CONCEPTION_LOG@@": "conception_points_domaine_G1_machine1_v1.log",
          "@@GARDE_PY@@": "garde_aux_points_machine1_v1.py", "@@GARDE_LOG@@": "garde_aux_points_machine1_v1.log",
          "@@ESSAI_JSON@@": "sonde_essai_ancres_machine1.json", "@@ESSAI_LECTURE@@": "lecture_essai_ancres_machine1.log"}
t = open(GAB, encoding="ascii").read()
for cle, nom in PIECES.items():
    assert t.count(cle) == 1, "gabarit : %s" % cle
    t = t.replace(cle, canon(os.path.join(ICI, nom)))
assert "@@" not in t, "gabarit non rempli"
assert all(ord(c) < 128 for c in t) and "%" not in t, "ASCII ou pour cent"
long_ = [i + 1 for i, l in enumerate(t.split("\n")) if len(l) > 100]
assert not long_, "lignes de plus de 100 colonnes : %s" % long_
lire = lambda nom: open(os.path.join(ICI, nom), encoding="ascii").read()
f, s = lire(PIECES["@@FEUILLE@@"]), lire(PIECES["@@SONDE@@"])
n = 0
for motif, ou, quoi in (
        ("SIGMA_J_MAX = 0.2", f, "ecart-type de J < 0.2"), ("POIDS_SITE_MIN = 0.5", f, "(n1, n2) >= 0.5"),
        ("DIX_PLANCHERS = 1.33e-12", f, "Gamma_2D(3) > 1.33e-12"), ("SUIVI_MIN = 0.9", f, "suivi >= 0.9"),
        ("STABILITE_CIBLE = 2.0", f, "(k = 2, 3, 4) strictement positives, et max / min <= 2"),
        ("ETALEMENT_CHAINE = 2.0", f, "quatre valeurs strictement positives, et max / min <= 2"),
        ("MIN_JUGES = 6", f, "moins de 6 etats juges"), ("MIN_EN_LISIBLES = 4", f, "moins de 4 des 6 points EN DOMAINE"),
        ("MIN_HORS_LISIBLES = 4", f, "moins de 4 des 6 points HORS DOMAINE"),
        ("MIN_PAIRES_RIVALE = 2", f, "moins de 2 des 3 paires"), ("TOL_ANCRE = 1e-2", f, "a 1e-2 pres"),
        ("TOL_GARDE = 5e-5", f, "a 5e-5 pres"), ("2.1623273017950654e-10", f, "2.1623273017950654e-10"),
        ("2.6613925716641374e-09", f, "2.6613925716641374e-09"), ("N_ETATS = 14", f, "les 14 etats"),
        ('MOTEUR_CANON = "82a0be882568fe0c"', f, "au canon 82a0be882568fe0c"),
        ('PAIRES = {"P1": ("E1", "H1"), "P2": ("E3", "H2"), "P3": ("E4", "H3"), "P4": ("E5", "H4"), "P5": ("E6", "H5")}', f,
         "P1 = (E1, H1) a 2.08    P2 = (E3, H2) a 2.10    P3 = (E4, H3) a 2.12"),
        ('PAIRES_RIVALE = ("P1", "P2", "P3")', f, "sur les trois paires P1, P2, P3"),
        ("if 0.5 <= q <= 2.0:", f, "0.5 <= q <= 2"), ("if q * q >= 0.1 and q * q <= 10.0:", f, "0.1 <= q x q <= 10"),
        ('elif a == 0 and b == 0:', f, "si a = 0 et b = 0"),
        ("FRACTION, L_BOITE, N_ETATS = 0.70, 20, 14", s, "N = r_c + 20"), ("KS = (2, 3, 4)", s, "pour k = 2, 3, 4"),
        ("EF_CHAINE = (0.25, 0.125, 0.0625, 0.03125)", s, "1/4, 1/8, 1/16, 1/32"),
        ('M.seuil_A4(w2, g, lecture=M.LECTURE_OCCUPATIONS)["S_det"]', s, "seuil_A4 en lecture reelle"),
        ("P4 = (E5, H4) a 1.91    P5 = (E6, H5) a 1.90", t, "P4 = (E5, H4) a 1.91")):
    assert motif in ou, "constante absente du script : " + motif
    assert quoi in t, "phrase absente du gel : " + quoi
    n += 1
# la table de la section 4 est celle du journal de la garde, de la feuille et de la sonde
log = lire(PIECES["@@GARDE_LOG@@"])
pts = re.findall(r"^(\w\d) w2=(\S+)\s+x(\S+)\s+g=\S+ Omega_c=\S+\s+D1=(\S+) c_max=(\S+) site=\S+ (EN DOMAINE|HORS DOMAINE)\s+"
                 r"graine=\(.*?\) card=\d+ r_c=(\d+) N=(\d+)$", log, re.M)
assert len(pts) == 14, len(pts)
for pid, w2, fac, d1, cm, st, rc, N in pts:
    ligne = "    %s  w2 = %-7s  facteur %-3s   D1 %s  c_max %s  N %s" % (pid, w2, fac, d1, cm, N)
    assert ligne in t, "ligne de la table absente du gel : " + ligne
    role = "ancre" if pid[0] == "A" else "juge"
    assert (st == "EN DOMAINE") == (pid[0] in "EA"), pid
    facf = fac if "/" in fac else fac + "/1"
    cst = '"%s": ("%s", "%s", "%s", %s, %s, %s)' % (pid, role, w2, facf, "EN" if st == "EN DOMAINE" else "HORS", d1, cm)
    assert cst in f, "tuple absent de la feuille : " + cst
    num, den = (w2.split("/") + ["1"])[:2]
    fn, fd = (fac.split("/") + ["1"])[:2]
    Ffac = "F(%s)" % fn if fd == "1" else "F(%s, %s)" % (fn, fd)
    assert '("%s", "%s", F(%s, %s), %s)' % (pid, role, num, den, Ffac) in s, "point absent de la sonde : " + pid
    assert int(N) <= 120
    n += 1
assert "SELFTEST : 74 cas, 74 tenus" in lire(PIECES["@@SELFTEST@@"])
assert "BANC : 60 alterations, 59 mordues, 1 survivantes" in lire(PIECES["@@BANC_LOG@@"])
assert "hunks appliques : %d" in lire(PIECES["@@CONSTRUCTION_SONDE@@"]) and lire(PIECES["@@CONSTRUCTION_SONDE@@"]).count("\nH('''") == 5
essai = lire(PIECES["@@ESSAI_LECTURE@@"])
assert "garde des ancres : TENUE" in essai and "garde G-6 aux points presents : TENUE" in essai
open(GEL, "w", encoding="ascii", newline="\n").write(t)
print("gel %s : canon %s, %d lignes, %d octets, %d controles de coherence" % (
    os.path.basename(GEL), canon(GEL), len(t.split("\n")) - 1, len(t.encode()), n))
