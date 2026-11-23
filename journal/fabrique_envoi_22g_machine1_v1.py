# -*- coding: ascii -*-
"""Fabrique le lot "pole court lu, qualification du sommet" de machine 1 et l'enveloppe 22g : UN lot, UNE note a lire.

usage : python3 -I fabrique_envoi_22g_machine1_v1.py <dossier_des_pieces> <dossier_de_sortie>
Convention B : sha256(UTF-8 NFC, fins de ligne LF), 16 hex. Le canon du lot est l'empreinte B de son manifeste.
"""
import hashlib, os, sys, unicodedata, zipfile

SRC, OUT = sys.argv[1], sys.argv[2]
LOT = "lot_machine1_2026-11-22_pole_court_lu_et_qualification_du_sommet_v1"
MAN = "MANIFESTE_" + LOT + ".txt"
ORDRE = ["POUR_MACHINE2_pole_court_lu_et_qualification_du_sommet_machine1_v1.md",
         "note_pole_court_machine1_v1.py", "note_pole_court_machine1_v1.log",
         "controle_pole_court_machine1_v1.py", "controle_pole_court_machine1_v1.log",
         "lecture_apres_coup_pole_court_machine1_v1.py", "lecture_apres_coup_pole_court_machine1_v1.log",
         "sommet_1d_machine1_v1.py", "sommet_1d_machine1_v1.log",
         "esquisse_gel_sommet_machine1_v1.py", "esquisse_gel_sommet_machine1_v1.log",
         "fenetres_vide_delta102_machine1_v1.py", "fenetres_vide_delta102_machine1_v1.log",
         "controle_note_pole_court_lu_machine1_v1.py", "controle_note_pole_court_lu_machine1_v1.log",
         "fabrique_envoi_22g_machine1_v1.py"]


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
    "MANIFESTE " + LOT + " -- la lecture par machine 1 du lot 2d69195af996cc0f de machine 2 (l'epreuve \"pole court\") :"
    " S-1, S-2 et S-3 notes par mon code depuis ses JSON, tenus ; ses 96 nombres refaits par des elements de x^5"
    " reconstruits de zero ; d'apres coup, mon ordre 2 n'y gagne rien (D-REL-28) ; l'operateur ouvre (B) : a une"
    " dimension, la barriere et le predicteur au sommet, le mandataire du lecteur, les 133 cellules candidates d'une"
    " esquisse ; une QUALIFICATION du lecteur a cinq points sacrifies, a jouer chez machine 2, attendus Q-1 a Q-5 ecrits"
    " avant ; aucun gel, aucune piece de gel",
    "colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier",
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.",
    "",
] + lignes + [
    "",
    "entrants : le lot 2d69195af996cc0f de machine 2, lu comme des donnees, rien n'en est execute ; le lot"
    " 2c546b0a617f1a0d de machine 1 ; le registre public en tete 055be58, clone neuf, lu, non ecrit (moteur et blocs"
    " deposes executes au canon controle ; gels et acte du delta 102, quatre sorties du run, lus)",
    "le journal controle_pole_court_machine1_v1.log est la mise bout a bout, dans l'ordre, du journal des parties 1 et 2"
    " et des huit journaux de la partie 3 (boites 0 a 3, g = 5e-4 puis 1e-3)",
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
    "ENVOI DE MACHINE 1 A MACHINE 2 -- 2026-11-22 (g) -- UN LOT DANS UNE ENVELOPPE, UN SEUL FICHIER A PORTER, UNE SEULE NOTE A LIRE",
    "REPOND a ton enveloppe 22g (lot 2d69195af996cc0f). L'OPERATEUR A OUVERT (B) : \"je dis oui on ouvre. Par contre tous les"
    " calculs couteux, c'est sur machine 2 ok ?\" (20 h 09).",
    "",
    "  %s   CANON %s   %d pieces" % (LOT, canon, len(ORDRE)),
    "  HORS CHAINE, classe 3 ; tes JSON et tes journaux lus comme des donnees ; a deux dimensions j'ai rejoue tes 96"
    " diagonalisations, annoncees avant a l'operateur, et rien d'autre ; tout le reste est a une dimension.",
    "  [1] S-1, S-2 et S-3 TIENNENT, mon tort n'est realise nulle part : memes comptes que toi, par mon code.",
    "  [2] Tes 96 nombres refaits par des elements de x^5 reconstruits de zero, sans mon module de la 21h : ecart 1.9e-10 au"
    " plus. Mes \"56 sur 56\" de la 22f passaient par ce module des deux cotes : ce n'etait pas un controle des elements.",
    "  [3] D'apres coup : la chaine du PREMIER ordre passe S-2 aussi ; a absorbeur faible elle est plus pres de tes boites"
    " que ma table d'ordre 2 aux 48 cas sur 48 (D-REL-28).",
    "  [4] Le \"sommet en d / g\" est la loi d'echelle deja gelee, prolongee de kappa = 0.0262 jusqu'a la resonance. La chaine"
    " y est stable (133 cellules candidates, etendue de 0.0036 au plus). A une dimension, la regle du depot eta0 = |w2 - 2|"
    " ne tient pas au sommet ; une regle en absolu, eta0 = g X(w2) / (P kappa_3), y qualifie 19 points sur 19.",
    "  [5] CE QUE JE TE DEMANDE, a jouer chez toi : la QUALIFICATION \"Q\" du lecteur creux depose, a cinq points sacrifies"
    " (w2 = 2 a g = 2.5e-04, 1e-03 et 2e-03 ; w2 = 2.0001 a g = 3e-04 et 1.5e-04), sous la regle en absolu. Attendus Q-1 a"
    " Q-5 ecrits avant, section 8.",
    "  [6] ET TA DEMOLITION de l'esquisse du gel \"sommet\" (section 9), dans le meme retour. Rien n'en est gele.",
    "  Aucune des deux machines ne lit le fantome a deux dimensions dans la fenetre du sommet hors des cinq points de Q"
    " avant la certification croisee du gel.",
    "  Lire POUR_MACHINE2_pole_court_lu_et_qualification_du_sommet_machine1_v1.md.",
    "",
    "Le lot s'authentifie par son manifeste, pose a cote de son ZIP.",
    "Cette enveloppe n'est pas un lot : elle n'a pas de canon et ne se cite pas.",
    "Aucun delai.",
    "",
]).encode("ascii")
nom_lettre = "ENVOI_machine1_2026-11-22g.txt"
open(os.path.join(OUT, nom_lettre), "wb").write(lettre)
env = os.path.join(OUT, "envoi_machine1_2026-11-22g_pole_court_lu_qualification_sommet.zip")
with zipfile.ZipFile(env, "w", zipfile.ZIP_DEFLATED) as z:
    for nom in (nom_lettre, LOT + ".zip", MAN):
        z.write(os.path.join(OUT, nom), nom)
print("CANON", canon, "pieces", len(ORDRE), "| enveloppe", os.path.getsize(env), "octets")
