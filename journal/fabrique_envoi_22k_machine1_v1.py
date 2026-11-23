# -*- coding: ascii -*-
"""Fabrique le lot "gel sommet seconde partie" de machine 1 et l'enveloppe 22k : UN lot, UNE piece de gel a certifier.

usage : python3 -I fabrique_envoi_22k_machine1_v1.py <dossier_des_pieces> <dossier_de_sortie>
Convention B : sha256(UTF-8 NFC, fins de ligne LF), 16 hex. Le canon du lot est l'empreinte B de son manifeste.
"""
import hashlib, os, sys, unicodedata, zipfile

SRC, OUT = sys.argv[1], sys.argv[2]
LOT = "lot_machine1_2026-11-22_gel_sommet_partie2_v1"
MAN = "MANIFESTE_" + LOT + ".txt"
GEL = "gel_sommet_partie2_instrument_enonce_pre_enregistrement_v1.md"
ORDRE = [GEL, "construction_gel_sommet_partie2_machine1_v1.py", "construction_gel_sommet_partie2_machine1_v1.log",
         "table_cellules_gel_sommet_v1.json", "predictions_sommet_machine1_v1.py", "predictions_sommet_machine1_v1.log",
         "tirage_sommet_graine_114565_machine1_v1.log", "jobs_gel_sommet_v1.txt", "jobs_temoins_sommet_v1.txt",
         "feuille_gel_sommet_machine1_v1.py", "banc_feuille_gel_sommet_machine1_v1.py", "banc_feuille_gel_sommet_machine1_v1.log",
         "garde_sur_les_sorties_de_Q_et_Q2_machine1_v1.log",
         "pilote_gel_sommet_machine1_v1.py", "banc_pilote_gel_sommet_machine1_v1.py", "banc_pilote_gel_sommet_machine1_v1.log",
         "controle_gel_sommet_partie2_machine1_v1.py", "controle_gel_sommet_partie2_machine1_v1.log",
         "recoupe_certification_machine1_v1.py", "recoupe_certification_machine1_v1.log", "tirage_demonstration_deux_tables_machine1_v1.log",
         "fabrique_envoi_22k_machine1_v1.py"]


def norm(d):
    t = unicodedata.normalize("NFC", d.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return t.encode("utf-8")


def h(d):
    return hashlib.sha256(d).hexdigest()[:16]


assert sorted(x for x in os.listdir(SRC) if not x.startswith("__")) == sorted(ORDRE), sorted(set(os.listdir(SRC)) ^ set(ORDRE))
lignes = []; canons = {}
for nom in ORDRE:
    d = open(os.path.join(SRC, nom), "rb").read()
    assert b"\r" not in d and all(b < 128 for b in d), nom
    n = norm(d); canons[nom] = h(n)
    lignes.append("%s  %s  %d  %d  %s" % (h(n), h(d), len(n), len(d), nom))
man = "\n".join([
    "MANIFESTE " + LOT + " -- LA SECONDE PARTIE DU GEL \"SOMMET\" (instrument, enonce, tolerances ; pre-enregistrement v1,"
    " A CERTIFIER PAR MACHINE 2 AVANT TOUTE LECTURE 2D A UNE CELLULE) : le tirage de machine 1 sur la graine 114565 donnee"
    " par l'operateur, la table gelee des 56 cellules avec leurs predictions a une dimension et des neuf temoins positifs,"
    " la feuille et son banc, le pilote et son banc, le controle de la piece ; et le recoupement par machine 1 de la"
    " certification de la premiere partie (lot 21e9bddfe5db83b2) ; aucun calcul a deux dimensions ; aucun depot",
    "colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier",
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.",
    "",
] + lignes + [
    "",
    "entrants : le lot 21e9bddfe5db83b2 de machine 2 (certification, table commune 77ce2a6c7e867011), ses lots"
    " c58c2b3f533c516b et 295b2b1549b076c2 (sorties de Q et de Q2, pilote de lecture 47a84eae6052f006), lus comme des"
    " donnees, rien n'en est execute ; le lot 3ba4618d7976c6ea de machine 1 (premiere partie 1e5039cade55d13f) ; le"
    " registre public en tete 055be58, clone neuf, lu, non ecrit",
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
import textwrap
def plie(t, debut="  ", suite="      "):
    return textwrap.fill(" ".join(t.split()), width=100, initial_indent=debut, subsequent_indent=suite, break_long_words=False, break_on_hyphens=False)
lettre = "\n".join([
    "ENVOI DE MACHINE 1 A MACHINE 2 -- 2026-11-22 (k) -- UN LOT DANS UNE ENVELOPPE, UN SEUL FICHIER A PORTER,",
    "UNE PIECE DE GEL A CERTIFIER : LA SECONDE PARTIE DU GEL \"SOMMET\"",
    "REPOND a ton enveloppe 22j (lot 21e9bddfe5db83b2).",
    "",
    "  %s   CANON %s   %d pieces" % (LOT, canon, len(ORDRE)),
    plie("AUCUN calcul a deux dimensions de ma part. Aucune note a part : tout est dans la piece.", "  ", "  "),
    plie("[1] TA CERTIFICATION, recoupee par mon code : ta table est la mienne octet pour octet ; ton detail est a 2.3e-11 du mien aux 560 cellules ; mon tirage de demonstration a deux tables rend tes 56 cellules."),
    plie("[2] LA GRAINE : l'operateur m'a ecrit \"graine 114565\" a 23 h 21. Je ne sais pas s'il te l'a donnee : dis-le."),
    plie("[3] MON TIRAGE : MP 199989/100000 et 199993/100000 ; PP 25001/12500 et 200011/100000 ; MG 6249/3125 et 49989/25000 ; PG 200039/100000 et 12503/6250 ; rangs 0 et 1 partout ; 56 cellules. Si le tien differe, PAS DE GEL."),
    plie("[4] LA PIECE : %s (%s). Table gelee %s ; feuille %s ; pilote %s." % (GEL, canons[GEL], canons["table_cellules_gel_sommet_v1.json"], canons["feuille_gel_sommet_machine1_v1.py"], canons["pilote_gel_sommet_machine1_v1.py"])),
    plie("[5] L'INSTRUMENT : l'etage A du depot ; NEUF TEMOINS POSITIFS DU SOMMET (les points de Q et de Q2 relus) et une GARDE avant toute cellule ; puis les 56 cellules par TON pilote de lecture (47a84eae6052f006), tel quel. Mon pilote n'a jamais joue une lecture reelle : il est eprouve sur des scripts factices, et ton pre-vol (--prevol : aucune cellule lue) sera sa premiere execution."),
    plie("[6] L'ENONCE : S1 seul, T = 0.01, la bande et le jugement du gel du vide (tes R-1 et R-2 : sections 5 et 14)."),
    plie("[7] CE QUE JE TE DEMANDE : les points (a) a (f) de la section 15, en un seul retour. Le run ne se joue qu'apres le feu vert ECRIT de l'operateur, une fois."),
    "  Lire la piece.",
    "",
    "Le lot s'authentifie par son manifeste, pose a cote de son ZIP.",
    "Cette enveloppe n'est pas un lot : elle n'a pas de canon et ne se cite pas.",
    "Aucun delai.",
    "",
]).encode("ascii")
assert all(len(l) <= 104 for l in lettre.decode("ascii").split("\n"))
nom_lettre = "ENVOI_machine1_2026-11-22k.txt"
open(os.path.join(OUT, nom_lettre), "wb").write(lettre)
env = os.path.join(OUT, "envoi_machine1_2026-11-22k_gel_sommet_partie2.zip")
with zipfile.ZipFile(env, "w", zipfile.ZIP_DEFLATED) as z:
    for nom in (nom_lettre, LOT + ".zip", MAN):
        z.write(os.path.join(OUT, nom), nom)
print("CANON", canon, "pieces", len(ORDRE), "| piece de gel", canons[GEL], "| enveloppe", os.path.getsize(env), "octets")
