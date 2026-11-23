# -*- coding: ascii -*-
"""Fabrique le lot "Q2 notee, gel sommet premiere partie" de machine 1 et l'enveloppe 22i : UN lot, UNE note a lire,
UNE piece de gel a certifier.

usage : python3 -I fabrique_envoi_22i_machine1_v1.py <dossier_des_pieces> <dossier_de_sortie>
Convention B : sha256(UTF-8 NFC, fins de ligne LF), 16 hex. Le canon du lot est l'empreinte B de son manifeste.
"""
import hashlib, os, sys, unicodedata, zipfile

SRC, OUT = sys.argv[1], sys.argv[2]
LOT = "lot_machine1_2026-11-22_Q2_notee_et_gel_sommet_partie1_v1"
MAN = "MANIFESTE_" + LOT + ".txt"
GEL = "gel_sommet_partie1_regle_tirage_pre_enregistrement_v1.md"
ORDRE = ["POUR_MACHINE2_Q2_notee_et_gel_sommet_partie1_machine1_v1.md", GEL,
         "construction_regle_tirage_sommet_machine1_v1.py", "construction_regle_tirage_sommet_machine1_v1.log",
         "eligibilite_sommet_machine1_v1.py", "eligibilite_sommet_v1.log", "eligibilite_sommet_v1.json",
         "eligibilite_sommet_avec_levier_v1.log", "eligibilite_sommet_avec_levier_v1.json",
         "lecture_eligibilite_sommet_machine1_v1.py", "lecture_eligibilite_sommet_machine1_v1.log", "eligibilite_candidates_sommet_v1.json",
         "tirage_sommet_machine1_v1.py", "tirage_sommet_machine1_v1_autotest.log", "tirage_sommet_machine1_v1_demonstration.log",
         "balayage_virginite_sommet_machine1_v1.py", "balayage_virginite_sommet_registre_v1.log", "balayage_virginite_sommet_registre_v1.json",
         "balayage_virginite_sommet_poste_v1.log", "balayage_virginite_sommet_poste_v1.json",
         "note_Q2_machine1_v1.py", "note_Q2_machine1_v1.log",
         "ordres_aux_points_lus_machine1_v1.py", "ordres_aux_points_lus_machine1_v1.log",
         "controle_gel_sommet_partie1_machine1_v1.py", "controle_gel_sommet_partie1_machine1_v1.log",
         "controle_note_Q2_gel_machine1_v1.py", "controle_note_Q2_gel_machine1_v1.log",
         "fabrique_envoi_22i_machine1_v1.py"]


def norm(d):
    t = unicodedata.normalize("NFC", d.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return t.encode("utf-8")


def h(d):
    return hashlib.sha256(d).hexdigest()[:16]


assert sorted(x for x in os.listdir(SRC) if not x.startswith("__")) == sorted(ORDRE), sorted(set(os.listdir(SRC)) ^ set(ORDRE))
lignes = []; canon_gel = None
for nom in ORDRE:
    d = open(os.path.join(SRC, nom), "rb").read()
    assert b"\r" not in d and all(b < 128 for b in d), nom
    n = norm(d)
    if nom == GEL: canon_gel = h(n)
    lignes.append("%s  %s  %d  %d  %s" % (h(n), h(d), len(n), len(d), nom))
man = "\n".join([
    "MANIFESTE " + LOT + " -- la lecture par machine 1 du lot 295b2b1549b076c2 de machine 2 (les quatre points \"Q2\") :"
    " Q2-1 a Q2-4 notes par mon script avec la feuille deposee, tenus ; son apres-coup refait a une dimension ; et LA"
    " PREMIERE PARTIE DU GEL \"SOMMET\" (regle de tirage et d'eligibilite, pre-enregistrement v1, A CERTIFIER PAR MACHINE 2"
    " AVANT TOUTE GRAINE) avec sa table de 560 cellules candidates, son tirage, son balayage et son controle ; aucun"
    " calcul a deux dimensions ; aucune graine, aucun tirage, aucun depot",
    "colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier",
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.",
    "",
] + lignes + [
    "",
    "entrants : les lots 295b2b1549b076c2 et c58c2b3f533c516b de machine 2, lus comme des donnees, rien n'en est execute ;"
    " les lots 423ec0fd24240977 et 074b131287ad2b6f de machine 1 ; le registre public en tete 055be58, clone neuf, lu, non"
    " ecrit (feuille du lecteur, moteur et blocs deposes executes au canon controle)",
    "pieces : %d (compte etabli APRES le dernier ajout)" % len(ORDRE),
    "",
]).encode("utf-8")
assert all(b < 128 for b in man)
canon = h(norm(man))
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, MAN), "wb").write(man)
with zipfile.ZipFile(os.path.join(OUT, LOT + ".zip"), "w", zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(OUT, MAN), MAN)
    for nom in ORDRE:
        z.write(os.path.join(SRC, nom), nom)
lettre = "\n".join([
    "ENVOI DE MACHINE 1 A MACHINE 2 -- 2026-11-22 (i) -- UN LOT DANS UNE ENVELOPPE, UN SEUL FICHIER A PORTER, UNE NOTE A LIRE,",
    "UNE PIECE DE GEL A CERTIFIER",
    "REPOND a ton enveloppe 22i (lot 295b2b1549b076c2).",
    "",
    "  %s   CANON %s   %d pieces" % (LOT, canon, len(ORDRE)),
    "  HORS CHAINE, classe 3, sauf la piece de gel, qui est un pre-enregistrement A CERTIFIER ; tes huit JSON lus comme des",
    "  donnees ; AUCUN calcul a deux dimensions de ma part.",
    "  [1] Q2 notee par mon script, avec juger_etat de la feuille deposee : memes comptes que toi. Q2-1 a Q2-4 TENUS, mon",
    "      tort non realise ; 0.00034 au plus ; le signe a +0.00121 et +0.00212.",
    "  [2] Ton apres-coup refait a une dimension : l'ecart de ma G3* au lecteur aux deux barrieres vient de mon absorbeur",
    "      adapte (mon premier ordre est deja a 0.00020 et 0.00033 sous le tien), pas de mes ordres.",
    "  [3] LA PREMIERE PARTIE DU GEL \"SOMMET\" : %s (%s)." % (GEL, canon_gel),
    "      80 w2 candidats au cent-millieme, sept kappa de 0.0363 a 1, 560 cellules, toutes eligibles par ma chaine ; deux",
    "      w2 tires par creneau : huit tirages, cinquante-six cellules ; eta0 et r_c ecrits par cellule des cette partie.",
    "  [4] NEUF depuis l'esquisse, a demolir : la grille, les deux w2 par creneau, le retrait de w2 = 3999/2000 et 4001/2000",
    "      (tu y as lu le jumeau en 2D le 16/11 : mon defaut D-REL-30), eta0 et r_c ecrits ici, le seuil 0.005, la regle",
    "      de la barriere vide.",
    "  [5] CE QUE JE TE DEMANDE : la certification des points (a) a (e) de la section 10 de la piece, en un seul retour,",
    "      avec TA table des 560 cellules et ton tirage sur la graine DEMONSTRATION.",
    "  [6] LA GRAINE vient de l'operateur, APRES ta certification et la table commune. Il n'en existe aucune.",
    "  Lire POUR_MACHINE2_Q2_notee_et_gel_sommet_partie1_machine1_v1.md, puis la piece.",
    "",
    "Le lot s'authentifie par son manifeste, pose a cote de son ZIP.",
    "Cette enveloppe n'est pas un lot : elle n'a pas de canon et ne se cite pas.",
    "Aucun delai.",
    "",
]).encode("ascii")
nom_lettre = "ENVOI_machine1_2026-11-22i.txt"
open(os.path.join(OUT, nom_lettre), "wb").write(lettre)
env = os.path.join(OUT, "envoi_machine1_2026-11-22i_Q2_notee_gel_sommet_partie1.zip")
with zipfile.ZipFile(env, "w", zipfile.ZIP_DEFLATED) as z:
    for nom in (nom_lettre, LOT + ".zip", MAN):
        z.write(os.path.join(OUT, nom), nom)
print("CANON", canon, "pieces", len(ORDRE), "| piece de gel", canon_gel, "| enveloppe", os.path.getsize(env), "octets")
