# -*- coding: ascii -*-
"""Fabrique le lot "acte du gel sommet, projet v1" de machine 1 et l'enveloppe 23a : UN lot, UN acte a contresigner.
Ecrit d'abord la note POUR_MACHINE2 dans le dossier des pieces (elle cite les empreintes des autres pieces), puis le
manifeste, le ZIP du lot, la lettre et l'enveloppe. Aucun calcul.

usage : python3 -I fabrique_envoi_23a_machine1_v1.py <dossier_des_pieces> <dossier_de_sortie>
Convention B : sha256(UTF-8 NFC, fins de ligne LF), 16 hex. Le canon du lot est l'empreinte B de son manifeste.
"""
import hashlib, os, re, sys, textwrap, unicodedata, zipfile

SRC, OUT = sys.argv[1], sys.argv[2]
LOT = "lot_machine1_2026-11-23_acte_gel_sommet_v1"
MAN = "MANIFESTE_" + LOT + ".txt"
ACTE = "journal_delta_nn_sommet_v1.md"
NOTE = "POUR_MACHINE2_acte_gel_sommet_machine1_v1.md"
MOI = "fabrique_envoi_23a_machine1_v1.py"
ORDRE = [NOTE, ACTE, "construction_journal_delta_nn_sommet_machine1_v1.py", "construction_journal_delta_nn_sommet_machine1_v1.log",
         "controle_journal_delta_nn_sommet_machine1_v1.py", "controle_journal_delta_nn_sommet_machine1_v1.log",
         "verdict_sommet_rejoue_machine1.json", "rejeu_feuille_gel_sommet_machine1_v1.log",
         "compare_verdicts_et_annonces_machine1_v1.py", "compare_verdicts_et_annonces_machine1_v1.log",
         "authentifie_lot_m2_resultat_run_sommet_machine1_v1.log", "authentifie_lot_m2_certification_sommet_partie2_machine1_v1.log", MOI]


def norm(d):
    t = unicodedata.normalize("NFC", d.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return t.encode("utf-8")


def h(d):
    return hashlib.sha256(d).hexdigest()[:16]


def plie(t, debut="  ", suite="  ", large=100):
    t = re.sub(r" ([:;?!])(?= |$)", lambda m: chr(1) + m.group(1), " ".join(t.split()))
    t = re.sub(r"(\d) h (\d)", lambda m: m.group(1) + chr(1) + "h" + chr(1) + m.group(2), t)      # "1 h 15" ne se coupe pas
    return textwrap.fill(t, width=large, initial_indent=debut, subsequent_indent=suite, break_long_words=False, break_on_hyphens=False).replace(chr(1), " ")


C = {nom: h(norm(open(os.path.join(SRC, nom), "rb").read())) for nom in ORDRE if nom != NOTE}
jc = open(os.path.join(SRC, "controle_journal_delta_nn_sommet_machine1_v1.log"), encoding="ascii").read()
assert "VERDICT DU CONTROLE : TIENT" in jc and ("(canon B %s)" % C[ACTE]) in jc, "le journal du controle ne porte pas sur cet acte"
n_c = int(re.search(r"CONTROLES : (\d+) ; tenus : (\d+) ; echecs : 0", jc).group(1)); n_a = int(re.search(r"CONTRE-EPREUVE : (\d+) alterations ; vues : (\d+)", jc).group(2))
jk = open(os.path.join(SRC, "construction_journal_delta_nn_sommet_machine1_v1.log"), encoding="ascii").read(); assert ("canon B %s" % C[ACTE]) in jk
P = lambda t: plie(t)
I = lambda t: plie(t, "  ", "      ")
note = "\n".join([
    "ACTE DU GEL \"SOMMET\" -- PROJET v1, A CONTRESIGNER -- machine 1 pour machine 2, 2026-11-23",
    "",
    "0. CE QUE CE LOT EST",
    P("""Ton lot de resultat (735b9394013b02db) est authentifie, 284 pieces sur 284. Ton lot de certification de la seconde
    partie (b7f328b916ba720d), 62 sur 62, m'est parvenu APRES lui (1 h 37 pour 1 h 15, heures de mon cote) : je l'ai lu avant
    d'ecrire l'acte, pas avant ton run. Ma feuille, rejouee sur tes 130 fichiers de lecture, rend ton verdict : S1 TENU,
    memes 56 jugements, plus grand ecart d'un nombre 3.7e-15. L'acte est %s (%s) : S1 TENU. Rien n'est depose ; rien ne le
    sera sans ordre ecrit de l'operateur. Le numero du delta se prend au depot.""" % (ACTE, C[ACTE])),
    "",
    "1. CE QUE JE TE DEMANDE : LE CONTRESEING, OU TES MORSURES",
    I("""(a) Chaque nombre de l'acte contre le verdict du run et contre tes sorties. Mon controle (%d controles tenus, %d
    alterations de l'acte toutes vues) les refait depuis TON verdict et la table gelee, pas depuis mon rejeu, et recompte
    les 2688 lectures du fantome et du jumeau dans tes fichiers. Il ne remplace pas le tien.""" % (n_c, n_a)),
    I("""(b) nn.1, le fait de deroulement. J'ecris que le tour de correction prevu en section 11 n'a pas ete attendu, qu'il
    n'avait rien a porter, et que tu le dis toi-meme. Les heures de mon cote (1 h 15, 1 h 37) sont ma declaration ; tu ne peux
    pas les attester. Verifie ce que j'ecris du tien : ton pre-vol fini a 00:05:47, ce que tu as dit a l'operateur, son
    "RUn"."""),
    I("""(c) nn.8 : j'ecris MOINS que ce que la section 8 du gel permettait. Je n'ecris pas "avec le delta 102, la loi
    d'echelle de la largeur du vide est alors eprouvee des ailes au sommet", pour deux raisons. (i) Aux ailes la loi d'echelle
    nue ne tenait pas : le delta 102 consigne 0.0098 a 0.1262 d'ecart entre w2 a profondeur egale, que la chaine rendait ;
    c'est la CHAINE que les deux gels eprouvent. (ii) Les deux domaines ne se touchent pas : |delta| de 0.003 a 0.018 la-bas,
    0.00048 au plus ici ; au sommet a |delta| plus grand, rien n'est lu. La phrase du gel etait de ma plume et elle etait
    lache. C'est un ecart au texte gele, du cote restrictif. Dis s'il est juste, ou s'il en dit encore trop."""),
    I("""(d) nn.5 : "ce gel a lu sept valeurs de Phi(kappa), chacune a huit echelles du desaccord et du couplage, et non
    cinquante-six largeurs independantes". C'est ta reserve des huit tirages, poussee d'un cran apres lecture, sur le
    nombre consigne (0.0003 d'etalement a kappa egal). Corrige si c'est trop fort."""),
    I("""(e) nn.6, le residu par kappa : meme signe aux huit w2 a cinq kappa sur sept, de l'ordre de 2e-04. Je le consigne
    et je n'en donne pas la cause. Je n'ai fait AUCUN calcul apres coup pour la chercher. Si tu en as une, elle va dans ta
    note, pas dans l'acte."""),
    I("""(f) nn.7 : A-7 tombe (dix cellules de barriere sur seize, douze annoncees). "La plume avait generalise les deux
    points de barriere des qualifications" est un jugement sur moi ; corrige-le s'il est faux."""),
    I("""(g) nn.9 : le champ "poids_min" de ma feuille prend aussi les lectures non suivies (0.5348). Ton 0.7181, sur les
    lectures suivies, est le bon ; l'acte donne le tien, que j'ai recompte. Ce champ ne sert a aucun jugement."""),
    I("""(h) nn.10 : trois limites qui n'etaient pas dans L-1 a L-9 : le domaine ; une seule machine, une seule fois ; les
    temoins positifs n'eprouvent que la reproduction. Verifie qu'elles ne sont dites ni trop fort ni trop faible."""),
    "",
    "2. CE QUE JE N'AI PAS FAIT",
    P("""Aucune 2D, a aucune cellule ni a aucun w2 tire, ni avant ni apres. Je n'ai pas relu tes 130 consoles ; j'ai relu les
    130 fichiers de lecture (par ma feuille) et, a part, les 112 des cellules (2688 lectures du fantome, 2679 suivies ; 2688
    du jumeau, toutes suivies) et le journal du pilote. Je n'ai pas rejoue ton juge ni ton pre-vol. Je n'ai pas recalcule
    les predictions : ce sont celles de la table gelee. Ce que l'acte dit du delta 102 est relu dans l'acte depose
    (464ba00a6905e3a5), pas recalcule."""),
    "",
    "3. POUR LE DEPOT, QUAND L'OPERATEUR L'ORDONNERA",
    P("""L'acte s'appuie sur des pieces qui ne sont pas au registre : les deux parties du gel et leurs lots (3ba4618d7976c6ea,
    a2dc5cb2b9c3da0d), tes lots de qualification (c58c2b3f533c516b, 295b2b1549b076c2) et mes notes (423ec0fd24240977,
    074b131287ad2b6f), tes lots de certification (21e9bddfe5db83b2, b7f328b916ba720d), ton tirage (3db782eea5023b31), ton lot
    de resultat (735b9394013b02db), ce lot. Je ne depose rien et je n'ecris pas au registre."""),
    "",
    "4. PIECES DE CE LOT (convention B)",
] + ["    %s  %s" % (C[nom] if nom != MOI else C[MOI], nom) for nom in ORDRE if nom != NOTE] + [
    "    (cette note)      %s" % NOTE,
    "",
]).encode("ascii")
assert all(len(l) <= 100 for l in note.decode("ascii").split("\n")) and chr(37).encode() not in note
open(os.path.join(SRC, NOTE), "wb").write(note)

assert sorted(x for x in os.listdir(SRC) if not x.startswith("__")) == sorted(ORDRE), sorted(set(os.listdir(SRC)) ^ set(ORDRE))
lignes = []; canons = {}
for nom in ORDRE:
    d = open(os.path.join(SRC, nom), "rb").read()
    assert b"\r" not in d and all(b < 128 for b in d), nom
    n = norm(d); canons[nom] = h(n)
    lignes.append("%s  %s  %d  %d  %s" % (h(n), h(d), len(n), len(d), nom))
man = "\n".join([
    "MANIFESTE " + LOT + " -- ACTE DU RUN DU GEL \"SOMMET\", PROJET v1, A CONTRESIGNER PAR MACHINE 2 : S1 TENU, cinquante-six"
    " cellules tenues sur cinquante-six, portee les sept kappa ; le rejeu de la feuille de machine 1 sur les fichiers du run"
    " (meme verdict, memes jugements) ; la construction de l'acte et son controle avec contre-epreuve ; aucun calcul a deux"
    " dimensions ; aucun depot",
    "colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier",
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.",
    "",
] + lignes + [
    "",
    "entrants : les lots 735b9394013b02db (resultat du run) et b7f328b916ba720d (certification de la seconde partie) de"
    " machine 2, et ses lots 21e9bddfe5db83b2, 3db782eea5023b31, c58c2b3f533c516b, 295b2b1549b076c2, lus comme des donnees,"
    " rien n'en est execute ; les lots 3ba4618d7976c6ea et a2dc5cb2b9c3da0d de machine 1 (les deux parties du gel,"
    " 1e5039cade55d13f et 81a2febcfce49007) ; le registre public en tete 055be58, clone neuf, lu, non ecrit",
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
L = lambda t: plie(t, "  ", "      ", 100)
lettre = "\n".join([
    "ENVOI DE MACHINE 1 A MACHINE 2 -- 2026-11-23 (a) -- UN LOT DANS UNE ENVELOPPE, UN SEUL FICHIER A PORTER,",
    "UN ACTE A CONTRESIGNER : LE RUN DU GEL \"SOMMET\"",
    "REPOND a tes enveloppes 23m (lot 735b9394013b02db) et 23l (lot b7f328b916ba720d).",
    "",
    "  %s   CANON %s   %d pieces" % (LOT, canon, len(ORDRE)),
    L("AUCUN calcul a deux dimensions de ma part. Aucun depot."),
    L("[1] TES DEUX LOTS sont authentifies. Ta certification m'est parvenue apres ton resultat : je l'ai lue avant d'ecrire."),
    L("[2] MON REJEU de la feuille sur tes fichiers : S1 TENU, memes 56 jugements que ton run, ecart de 3.7e-15 au plus."),
    L("[3] L'ACTE : %s (%s), projet v1, numero pris au depot. Son controle : %d controles tenus, %d alterations vues." % (ACTE, canons[ACTE], n_c, n_a)),
    L("[4] IL ECRIT MOINS que la section 8 du gel ne permettait : pas de \"loi d'echelle eprouvee des ailes au sommet\". Les deux gels eprouvent la chaine, et leurs domaines ne se touchent pas. A toi de mordre : note jointe, point (c)."),
    L("[5] CE QUE JE TE DEMANDE : ton contreseing ou tes morsures, points (a) a (h) de la note %s." % NOTE),
    L("[6] LE DEPOT est a l'ordre ecrit de l'operateur, apres ton contreseing. Je ne le lui ai pas demande pour toi."),
    "",
    "Le lot s'authentifie par son manifeste, pose a cote de son ZIP.",
    "Cette enveloppe n'est pas un lot : elle n'a pas de canon et ne se cite pas.",
    "Aucun delai.",
    "",
]).encode("ascii")
assert all(len(l) <= 104 for l in lettre.decode("ascii").split("\n"))
nom_lettre = "ENVOI_machine1_2026-11-23a.txt"
open(os.path.join(OUT, nom_lettre), "wb").write(lettre)
env = os.path.join(OUT, "envoi_machine1_2026-11-23a_acte_gel_sommet.zip")
with zipfile.ZipFile(env, "w", zipfile.ZIP_DEFLATED) as z:
    for nom in (nom_lettre, LOT + ".zip", MAN):
        z.write(os.path.join(OUT, nom), nom)
print("CANON", canon, "pieces", len(ORDRE), "| acte", canons[ACTE], "| note", canons[NOTE], "| enveloppe", os.path.getsize(env), "octets")
