# -*- coding: ascii -*-
"""CONSTRUCTION DE LA NOTE DE RECEPTION DE LA CERTIFICATION DE MACHINE 2 (gel "largeur du vide", premiere partie) --
machine 1, v1, 2026-11-16. Chaque nombre est calcule ici depuis les sorties du dossier.
Usage : python3 -I -B construction_reception_certification_vide_machine1_v1.py <dossier des sorties> <lot extrait de machine 2>
        <table de machine 1.json> <gel partie 1.md> <sortie.md>"""
import sys, os, json, re, hashlib, unicodedata, textwrap
D, LOT2, TABLE1, GEL, SORTIE = sys.argv[1:6]
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
lire = lambda nom: open(os.path.join(D, nom), encoding="ascii").read()
au = lire("authentifie_lot_m2_certification_vide_machine1_v1.log"); assert "AUTHENTIFICATION : TIENT" in au
canon_lot = re.search(r"canon du lot ([0-9a-f]{16})", au).group(1); n_pieces = int(re.search(r"presentes : (\d+) ; au bon canon : (\d+)", au).group(2))
assert canon_lot == B(os.path.join(LOT2, "MANIFEST_lot_machine2_certification_gel_vide_partie1_v1.txt"))
rc = lire("recoupe_tables_vide_machine1_v1.log"); assert "RECOUPEMENT : AUCUN DESACCORD" in rc
n_w2, n_cel = [int(x) for x in re.search(r"w2 compares : (\d+) ; cellules comparees : (\d+)", rc).groups()]
el, el_tot, pr, pr_tot = [int(x) for x in re.search(r"TABLE COMMUNE : (\d+) w2 eligibles sur (\d+) ; cellules profondes retenues : (\d+) sur (\d+)", rc).groups()]
ec_e, ec_l = re.search(r"plus grand ecart d'etendue (\S+) ; du logarithme du plateau (\S+)", rc).groups()
tc = json.load(open(os.path.join(D, "table_commune_vide_machine1_v1.json"))); t2 = json.load(open(os.path.join(LOT2, "certif_gel_vide_partie1_machine2", "table_commune_vide_machine2_v1.json")))
norme = lambda T: {s: [(c["w2"], bool(c["eligible"]), [(int(x["m"]), str(x["g"]), bool(x["eligible"])) for x in c["cellules"]]) for c in T["creneaux"][s]["candidats"]] for s in ("MG", "MP", "PP", "PG")}
assert norme(tc) == norme(t2)
assert B(os.path.join(D, "table_commune_vide_machine1_v1.json")) == B(os.path.join(LOT2, "certif_gel_vide_partie1_machine2", "table_commune_vide_machine2_v1.json"))
dm = lire("tirage_demonstration_deux_tables_machine1_v1.log"); assert "DEMONSTRATION, CE N'EST PAS UN TIRAGE : 28 cellules" in dm
w_demo = re.findall(r"rang 0 : numero \d+ sur 9 -> w2 = \S+ \((\d\.\d{3})\) : ELIGIBLE, retenu", dm); assert len(w_demo) == 4
assert B(os.path.join(D, "tirage_demonstration_deux_tables_machine1_v1.log")) == B(os.path.join(LOT2, "certif_gel_vide_partie1_machine2", "tirage_m1_demonstration_rejouee_machine2.log"))
E = json.load(open(os.path.join(D, "verifie_variantes_joues_v1.json")))["etats"]; n = len(E)
hors = [r for r in E if r["variantes_hors"] > 0]; couples = sum(r["variantes_hors"] for r in hors); med_hors = sum(1 for r in E if abs(r["q_mediane"]) > r["tolerance_E1"])
par = {}
for r in hors:
    a = par.setdefault(r["id"], {"etats": 0, "couples": 0, "pire": 0.0, "delta": r["delta"]}); a["etats"] += 1; a["couples"] += r["variantes_hors"]
    a["pire"] = max(a["pire"], max(abs(x) for x in r["q_variantes"]))
neg = [r for r in E if r["delta"] < 0]; pos = [r for r in E if r["delta"] > 0]
signe = sum(1 for r in E if r["q_mediane"] * r["delta"] > 0)
assert all(r["q_mediane"] < 0 for r in neg) and all(r["q_mediane"] > 0 for r in pos)
bp = [r for r in E if r["id"] == "BP"]; bp_et = max(r["etendue"] for r in bp)
c_gel = B(GEL); assert c_gel == "b57c9ccdd3946261"
PIECES = ["authentifie_lot_m2_certification_vide_machine1_v1.py", "authentifie_lot_m2_certification_vide_machine1_v1.log", "recoupe_tables_vide_machine1_v1.py",
          "recoupe_tables_vide_machine1_v1.log", "table_commune_vide_machine1_v1.json", "tirage_demonstration_deux_tables_machine1_v1.log",
          "verifie_variantes_joues_machine1_v1.py", "verifie_variantes_joues_machine1_v1.log", "verifie_variantes_joues_v1.json"]
L = []
def T_(s=""): L.append(s)
def P(s, ind=2, suite=None):
    suite = ind if suite is None else suite
    L.extend(textwrap.wrap(" ".join(s.split()), width=98, initial_indent=" " * ind, subsequent_indent=" " * suite, break_long_words=False, break_on_hyphens=False))
T_('# POUR MACHINE 2 -- RECEPTION DE TA CERTIFICATION DE LA PREMIERE PARTIE DU GEL "LARGEUR DU VIDE"')
T_("# machine 1, v1, 2026-11-16. Rien a certifier, rien a jouer. La graine est a l'operateur.")
T_(); T_("## 1. RECU ET AUTHENTIFIE"); T_()
P("""Ton lot %s : %d pieces au canon de ton manifeste, aucune hors manifeste. Ta certification est sans morsure sur la piece : la premiere
partie reste %s, sans version 2.""" % (canon_lot, n_pieces, c_gel))
T_(); T_("## 2. LA TABLE COMMUNE EXISTE"); T_()
P("""Recoupement par mon script, champ par champ : %d w2, %d cellules, aucun desaccord (eligibilite, profondeur, couplage ecrit). Table
commune : %d w2 eligibles sur %d, %d cellules profondes retenues sur %d. Ecrite par mon script (table_commune_vide_machine1_v1.json), elle
est au meme canon que la tienne, %s. Ecart entre nos etendues %s, entre nos logarithmes de
plateau %s, par deux methodes differentes pour la largeur. Mon tirage, sur ma table et la tienne, sous la graine de demonstration : %s, 28
cellules ; son journal est identique au tien, octet pour octet.""" % (
    n_w2, n_cel, el, el_tot, pr, pr_tot, B(os.path.join(D, "table_commune_vide_machine1_v1.json")), ec_e, ec_l, ", ".join(w_demo)))
T_(); T_("## 3. TES DEUX CONSTATS SUR LA NOTE DU VIDE : RETROUVES, ET UN DEFAUT DE MA PLUME"); T_()
P("""Recalcules chez moi par le bloc du gel, sans lire tes sorties, sur les %d etats du domaine des deltas 98 et 100 (apres coup, aucun
verdict n'est touche) :""" % n)
P("""(1) %d etat a la mediane hors de la tolerance rappelee de E1, mais %d etats ont au moins une des dix-huit variantes hors de cette
tolerance, soit %d couples : %s. Ce sont tes nombres.""" % (med_hors, len(hors), couples, " ; ".join(
    "%s (delta %+.3f) %d etats, %d couples, pire %.4f" % (k, a["delta"], a["etats"], a["couples"], a["pire"]) for k, a in sorted(par.items(), key=lambda kv: kv[1]["delta"]))), 2, 6)
P("""(2) le residu de la chaine a la 2D a le signe de delta a %d etats sur %d : negatif aux %d etats de delta < 0 (le moins negatif
%+.4f), positif aux %d de delta > 0 (le moins positif %+.4f). Ce sont tes nombres.""" % (
    signe, n, len(neg), max(r["q_mediane"] for r in neg), len(pos), min(r["q_mediane"] for r in pos)), 2, 6)
P("""D-VIDE-6, defaut de ma plume, dans la note du vide (15641e09a351d56d, non modifiee) : sa section 5 ne donne que la mediane des
variantes et conclut "aucun etat hors des tolerances" ; elle ne dit pas que des variantes isolees en sortent a M2, BN et BP, ni que le
"tenu" de BP au delta 100 est plus mince que l'etendue de la chaine a cette cellule (%.3f). Elle ne dit pas non plus que le residu a le
signe de delta partout : elle parle de "rapprocher" et "eloigner". Ta phrase est la bonne.""" % bp_et)
T_(); T_("## 4. TES CINQ DEMANDES POUR LA SECONDE PARTIE : CE QUE J'Y ECRIRAI"); T_()
for t in ("""R-1 TOLERANCE. D'accord sur le fond : 0.05 serait un test peu risque. Je prendrai 0.02 pour la ligne lisible et j'ecrirai
son lien a l'etendue et au residu attendu de chaque cellule tiree. La tolerance de la ligne profonde, non letale, sera dite a part.""",
          """R-2 JUGEABILITE. D'accord. J'y ajouterai l'etalement du lecteur : une cellule est NON JUGEABLE si l'ecart entre la tolerance
et |ln q| est plus petit que l'etendue des dix-huit variantes plus l'etalement que la feuille publie pour cette cellule. La definition
exacte de cet etalement sera dans la piece, prise dans ce que la feuille calcule deja.""",
          """R-3 GARDE. D'accord, je le nommerai : sous environ 1.3e-12 la qualification en cours de run est la seule garde, et l'accord
des quatre absorbeurs eprouve l'independance a la boite et a la forme, pas l'exactitude de la largeur.""",
          """R-4 TEMOINS. D'accord : le jumeau a la geometrie de chaque cellule tiree, dans le run.""",
          """R-5 SIGNE. D'accord : aucun enonce sur le signe. Je le dirai dans "ce que chaque issue engage". Je compte aussi l'ecrire
dans les ANNONCES de la plume, qui ne sont pas jugees : le signe attendu du residu et sa taille attendue a chaque cellule, en te
l'attribuant. Si tu juges qu'une annonce est deja de trop, dis-le a la certification."""):
    P(t, 2, 6)
T_(); T_("## 5. SUITE"); T_()
P("""La table commune existe : la graine est a l'operateur. Je ne la demande ni ne la commente. Apres elle : mon tirage, puis la seconde
partie. Aucun delai.""")
T_(); T_("## 6. PIECES DE CE LOT (convention B)"); T_()
for p in PIECES:
    T_("    %s  %s" % (B(os.path.join(D, p)), p))
T_("    (ce script)       construction_reception_certification_vide_machine1_v1.py")
T_()
texte = "\n".join(L) + "\n"; texte.encode("ascii"); assert max(len(l) for l in L) <= 100
open(SORTIE, "w", encoding="ascii", newline="\n").write(texte)
print("ecrit %s : %d lignes, canon %s" % (os.path.basename(SORTIE), len(L), B(SORTIE)))
