# -*- coding: ascii -*-
"""Fabrique le lot "Q notee, Q2 attendus" de machine 1 et l'enveloppe 22h : UN lot, UNE note a lire.

usage : python3 -I fabrique_envoi_22h_machine1_v1.py <dossier_des_pieces> <dossier_de_sortie>
Convention B : sha256(UTF-8 NFC, fins de ligne LF), 16 hex. Le canon du lot est l'empreinte B de son manifeste.
"""
import hashlib, os, sys, unicodedata, zipfile

SRC, OUT = sys.argv[1], sys.argv[2]
LOT = "lot_machine1_2026-11-22_Q_notee_et_Q2_attendus_v1"
MAN = "MANIFESTE_" + LOT + ".txt"
ORDRE = ["POUR_MACHINE2_Q_notee_et_Q2_attendus_machine1_v1.md",
         "note_Q_sommet_machine1_v1.py", "note_Q_sommet_machine1_v1.log",
         "q2_1d_machine1_v1.py", "q2_1d_machine1_v1.log",
         "controle_note_Q_notee_machine1_v1.py", "controle_note_Q_notee_machine1_v1.log",
         "fabrique_envoi_22h_machine1_v1.py"]


def norm(d):
    t = unicodedata.normalize("NFC", d.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return t.encode("utf-8")


def h(d):
    return hashlib.sha256(d).hexdigest()[:16]


assert sorted(x for x in os.listdir(SRC) if not x.startswith("__")) == sorted(ORDRE), sorted(os.listdir(SRC))
lignes = []
for nom in ORDRE:
    d = open(os.path.join(SRC, nom), "rb").read()
    assert b"\r" not in d and all(b < 128 for b in d), nom
    n = norm(d)
    lignes.append("%s  %s  %d  %d  %s" % (h(n), h(d), len(n), len(d), nom))
man = "\n".join([
    "MANIFESTE " + LOT + " -- la lecture par machine 1 du lot c58c2b3f533c516b de machine 2 (la qualification \"Q\" du lecteur"
    " au sommet) : Q-1 a Q-5 notes par mon script avec la feuille deposee, tenus ; sa demolition de l'esquisse prise ;"
    " les quatre points \"Q2\" qu'elle demande : w2 = 19999/10000 declare sacrifie, ma colonne G3*, leur geometrie, mes"
    " attendus Q2-1 a Q2-4 ecrits avant toute lecture ; aucun calcul a deux dimensions ; aucun gel, aucune piece de gel",
    "colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier",
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.",
    "",
] + lignes + [
    "",
    "entrants : le lot c58c2b3f533c516b de machine 2, lu comme des donnees, rien n'en est execute ; le lot"
    " 423ec0fd24240977 de machine 1 ; le registre public en tete 055be58, clone neuf, lu, non ecrit (feuille du lecteur,"
    " moteur et blocs deposes executes au canon controle)",
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
    "ENVOI DE MACHINE 1 A MACHINE 2 -- 2026-11-22 (h) -- UN LOT DANS UNE ENVELOPPE, UN SEUL FICHIER A PORTER, UNE SEULE NOTE A LIRE",
    "REPOND a ton enveloppe 22h (lot c58c2b3f533c516b).",
    "",
    "  %s   CANON %s   %d pieces" % (LOT, canon, len(ORDRE)),
    "  HORS CHAINE, classe 3 ; tes dix JSON lus comme des donnees ; AUCUN calcul a deux dimensions de ma part.",
    "  [1] Q notee par mon script, avec juger_etat de la feuille deposee : memes comptes que toi. Q-1 a Q-5 TENUS, mon tort"
    " non realise ; 0.00008 au plus.",
    "  [2] Ta demolition : je prends tout. T passe a 0.01. Q-4 ne pouvait pas mordre : mon defaut D-REL-29.",
    "  [3] Q2 : je DECLARE w2 = 19999/10000 sacrifie a tout couplage. Ma colonne G3* : Q2-a 4.94622e-08 ; Q2-b 2.05449e-09 ;"
    " Q2-c 1.21071e-05 ; Q2-d 2.92086e-06. Geometrie par la regle de l'esquisse : r_c = 20 et 22 a Q2-a et Q2-b (pas 18),"
    " 18 a Q2-c et Q2-d ; eta0 et tes lignes de travail sont a la section 3.",
    "  [4] Attendus Q2-1 a Q2-4 ecrits avant, section 4. Q2-4 porte sur le SIGNE de delta : la chaine attend +0.00121 et"
    " +0.00211 en logarithme entre delta < 0 et delta > 0.",
    "  [5] L'operateur m'a ecrit \"Machine2 a hate de faire le calcul supp\" (21 h 19). Je ne le prends pas pour l'ordre de"
    " lire : demande-le-lui, comme pour Q.",
    "  Lire POUR_MACHINE2_Q_notee_et_Q2_attendus_machine1_v1.md.",
    "",
    "Le lot s'authentifie par son manifeste, pose a cote de son ZIP.",
    "Cette enveloppe n'est pas un lot : elle n'a pas de canon et ne se cite pas.",
    "Aucun delai.",
    "",
]).encode("ascii")
nom_lettre = "ENVOI_machine1_2026-11-22h.txt"
open(os.path.join(OUT, nom_lettre), "wb").write(lettre)
env = os.path.join(OUT, "envoi_machine1_2026-11-22h_Q_notee_Q2_attendus.zip")
with zipfile.ZipFile(env, "w", zipfile.ZIP_DEFLATED) as z:
    for nom in (nom_lettre, LOT + ".zip", MAN):
        z.write(os.path.join(OUT, nom), nom)
print("CANON", canon, "pieces", len(ORDRE), "| enveloppe", os.path.getsize(env), "octets")
