# -*- coding: ascii -*-
"""RELEVE DE LA PREMIERE PARTIE DU GEL "PONT" -- machine 1, v1, 2026-11-17. Relit le TEXTE contre les pieces ; ne recopie pas
le script de construction : les nombres sont recalcules depuis les JSON, les canons depuis les fichiers, le hachage depuis hashlib.
Usage : python3 -I releve_gel_pont_partie1_machine1_v1.py <texte du gel> <dossier des sorties> <clone du registre>
        <dossier de l'exploration du lisse> <dossier de la lecture des grandes boites> <dossier du lot de machine 2>
        (sur le lot extrait a plat, les trois premiers dossiers sont le meme)
Code de sortie 0 si aucun controle ne mord."""
import sys, os, re, json, math, hashlib, unicodedata
from fractions import Fraction as F
TEXTE, D, CLONE, EXPLO, GB, LOT_M2 = sys.argv[1:7]
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
brut = open(TEXTE, "rb").read(); txt = brut.decode("utf-8", "replace"); lignes = txt.split("\n")
plat = " ".join(txt.split())                      # le texte sans ses retours a la ligne, pour chercher une phrase
mord = []; n = 0
def chk(code, ok, quoi):
    global n
    n += 1
    if not ok: mord.append(code)
    print("%-4s %s %s" % (code, "TIENT" if ok else "MORD ", quoi))
# R01 forme
chk("R01", all(b < 128 for b in brut) and all(len(l) <= 100 for l in lignes) and txt.count("%") == 1 and '"%.5e"' in txt and b"\r" not in brut
    and txt.startswith('GEL "PONT" -- PREMIERE PARTIE') and txt.endswith("-- FIN gel_pont_partie1_regle_tirage_pre_enregistrement_v1 --\n"),
    "ASCII, lignes de 100 colonnes au plus, un seul signe pour cent (le format du couplage), titre et ligne de fin")
# R02 sources
SRC = {"scripts/m17_chaine_v17.py": CLONE, "scripts/chaine_ordre2_bloc_machine1_v1.py": CLONE, "scripts/ordre3_bloc_machine1_v1.py": CLONE,
       "scripts/chaine_adaptee_bloc_machine1_v1.py": CLONE, "scripts/sonde_lecteur_gel_loi_machine1_v1.py": CLONE,
       "gels/gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md": CLONE, "scripts/eligibilite_vide_machine1_v1.py": CLONE,
       "scripts/tirage_vide_machine1_v1.py": CLONE, "journal/journal_delta_102_largeur_vide_v2.md": CLONE}
ok = True; connus = set()
for rel, base in SRC.items():
    c = B(os.path.join(base, rel)); connus.add(c); ok = ok and re.search(re.escape(c) + r"\s+" + re.escape(rel), txt) is not None
hors = {"lot_m2": B(os.path.join(os.path.dirname(LOT_M2.rstrip("/")), "MANIFEST_lot_machine2_grandes_boites_resultats_v1.txt")),
        "note_m2": B(LOT_M2 + "/POUR_MACHINE1_grandes_boites_resultats_machine2_v1.md"),
        "note_gb": B(GB + "/note_machine1_pont_lecture_grandes_boites_2026-11-17_v1.md"), "note_lisse": B(EXPLO + "/note_machine1_pont_lisse_hors_vide_2026-11-17_v1.md"),
        "attendu": B(EXPLO + "/attendu_lisse_hors_vide_machine1_v1.txt"), "rectif": B(EXPLO + "/rectificatif_instrument_lisse_hors_vide_machine1_v1.txt")}
connus |= set(hors.values())
ok = ok and all(v in txt for v in hors.values()) and ("lot de machine 2 lot_machine2_2026-11-17_grandes_boites_resultats_v1" in plat) and (hors["lot_m2"] + " lot de machine 2") in plat
tete = subprocess_tete = None
import subprocess
tete = subprocess.run(["git", "-C", CLONE, "rev-parse", "--short=7", "HEAD"], capture_output=True, text=True).stdout.strip()
chk("R02", ok and ("(registre %s)" % tete) in txt, "les neuf sources du registre (tete %s) et les six canons hors registre sont ceux des fichiers" % tete)
# R04 pieces de la section 13
i13 = lignes.index("13. PIECES DE CE LOT (convention B)"); ok = True; np_ = 0
for l in lignes[i13 + 1:]:
    m = re.match(r"^    ([0-9a-f]{16})  (\S+)$", l)
    if not m: continue
    c, nom = m.groups(); np_ += 1; connus.add(c)
    p = sorted(set(os.path.realpath(os.path.join(x, nom)) for x in (D, EXPLO, GB) if os.path.exists(os.path.join(x, nom))))   # un lot a plat : les trois dossiers sont le meme
    ok = ok and len(p) == 1 and B(p[0]) == c
chk("R04", ok and np_ == 58, "section 13 : %d pieces, chacune trouvee une fois et a son canon" % np_)
# R03 toute empreinte du texte est expliquee
demo = set(re.findall(r"= ([0-9a-f]{16})\.\.\.", txt))
toutes = set(re.findall(r"(?<![0-9a-f])[0-9a-f]{16}(?![0-9a-f])", txt))
inconnues = sorted(toutes - connus - demo - {"4e15e302d97e26b8"})
chk("R03", not inconnues and len(demo) == 4, "empreintes du texte : %d ; hors sources, pieces, quatre hachages de demonstration et le lot declare non detenu : %s" % (len(toutes), inconnues))
# R05-R06 la table
T = json.load(open(D + "/eligibilite_pont_MG_PG_v1.json")); TS = json.load(open(D + "/eligibilite_pont_MG_PG_sans_levier_v1.json")); R = T["regle"]
def eligible(x):
    return (x["m_bord"] == x["m"] and x["e_bord"] < 0.7 and x["etendue"] is not None and x["etendue"] <= 0.02
            and all(e is not None and e <= 0.03 for e in x["etendue_rho3"]) and all(p is not None and abs(p) <= 0.10 for p in x["pas_2_3"]))
ok = True; n_el = {}; hors_v = 0; autres = 0
for s in ("MG", "PG"):
    n_el[s] = 0
    for cd in T["creneaux"][s]["candidats"]:
        e = [eligible(x) for x in cd["cellules"]]; n_el[s] += all(e)
        for x in cd["cellules"]:
            v_seule = (not eligible(x)) and x["m_bord"] == x["m"] and x["e_bord"] < 0.7 and x["etendue"] <= 0.02 and max(x["etendue_rho3"]) <= 0.03
            hors_v += v_seule; autres += (not eligible(x)) and not v_seule
        l = "  %.3f  %s  %s" % (float(F(cd["w2"])), "  ".join("m%d %.4f %.4f %.4f%s" % (x["m"], x["etendue"], max(x["etendue_rho3"]), max(abs(p) for p in x["pas_2_3"]), "" if ex else "!")
                                                          for x, ex in zip(cd["cellules"], e)), "ELIGIBLE" if all(e) else "INELIGIBLE")
        ok = ok and l in lignes and cd["eligible"] == all(e)
    ok = ok and ("  creneau %s : %d w2 eligibles sur %d" % (s, n_el[s], len(T["creneaux"][s]["candidats"]))) in lignes
chk("R05", ok, "section 7 : les seize lignes de candidats et les deux en-tetes de creneau sont ceux que rend la table JSON, eligibilite recalculee des seuils")
p_rien = (1.0 - n_el["MG"] / 8.0) ** 5
chk("R06", (n_el["MG"], n_el["PG"], hors_v, autres) == (5, 8, 6, 0) and "La condition (v) en ecarte 6, toutes dans le creneau MG" in plat
    and ("vaut %.4f pour MG et 0 pour PG" % p_rien) in plat and json.dumps(T, sort_keys=True) == json.dumps(TS, sort_keys=True)
    and (R["seuil_etendue"], R["seuil_etendue_rho"], R["seuil_pas"], R["garde_e_bord"]) == (0.02, 0.03, 0.10, 0.7) and "<= 0.03 ; (v)" in plat and "<= 0.10." in plat,
    "eligibles MG %d, PG %d ; cellules ecartees par (v) seule %d, autrement %d ; probabilite de PAS DE GEL pour MG %.4f ; tables avec et sans levier identiques" % (n_el["MG"], n_el["PG"], hors_v, autres, p_rien))
# R07 le hachage de demonstration, refait
EXCLUS = (F(1982, 1000), F(2017, 1000))
LISTES = {"MG": [F(k, 1000) for k in range(1981, 1990) if F(k, 1000) not in EXCLUS], "PG": [F(k, 1000) for k in range(2011, 2020) if F(k, 1000) not in EXCLUS]}
ok = True
for s in ("MG", "PG"):
    ok = ok and [("%d/%d" % (w.numerator, w.denominator)) for w in LISTES[s]] == [cd["w2"] for cd in T["creneaux"][s]["candidats"]]
    ok = ok and ("%s, delta %s 0 : w2 = %s" % (s, "<" if s == "MG" else ">", ", ".join("%.3f" % float(w) for w in LISTES[s]))) in plat
    for r in (0, 1):
        h = hashlib.sha256(("DEMONSTRATION|%s|%d" % (s, r)).encode("ascii")).hexdigest(); k = int(h, 16) % 8
        ok = ok and ('    sha256("DEMONSTRATION|%s|%d") = %s... ; modulo  8 = %2d -> w2 = %.3f' % (s, r, h[:16], k, float(LISTES[s][k]))) in lignes
chk("R07", ok, "listes des candidats (huit par creneau, sans 1.982 ni 2.017) et quatre lignes de demonstration refaites par hashlib")
# R08 les nombres cites
CT = json.load(open(D + "/controle_point_sacrifie_v1.json")); VR = json.load(open(D + "/balayage_virginite_pont_registre_v1.json")); VP = json.load(open(D + "/balayage_virginite_pont_poste_v1.json"))
LL = json.load(open(EXPLO + "/lecture_lisse_hors_vide_v1.json")); CG = json.load(open(GB + "/regards_complements_v1.json")); RJ = json.load(open(GB + "/rejeu_grandes_boites_v1.json"))
cel = [(s, cd, x) for s in ("MG", "PG") for cd in T["creneaux"][s]["candidats"] for x in cd["cellules"]]
pas = {(s, int(round(abs(float(F(cd["w2"])) - 2.0) * 1000)), x["m"]): max(abs(p) for p in x["pas_2_3"]) for (s, cd, x) in cel}
rap = [pas[("MG", d, m)] / pas[("PG", d, m)] for (s, d, m) in pas if s == "MG" and ("PG", d, m) in pas]
attendus = ["une etendue du lisse de %.4f au plus et un pas de %.4f au plus" % (max(CT["cellule"]["etendue_rho3"]), max(abs(p) for p in CT["cellule"]["pas_2_3"])),
            "elle rend le couplage de l'exploration, %s." % CT["cellule"]["g"],
            "(%d paires), le plus grand pas de l'ordre 2 a l'ordre 3 est de %.1f a %.1f fois plus grand" % (len(rap), min(rap), max(rap)),
            "s'arrete a |delta| = %.3f." % max(abs(float(F(cd["w2"])) - 2.0) for cd in T["creneaux"]["MG"]["candidats"] if cd["eligible"]),
            "Le plus petit poids du site 0 dans l'etat lu est %.4f." % min(x["poids_min"] for (_, _, x) in cel),
            "%d comparaisons, plus grand ecart %g ; la cellule y est eligible." % (CT["comparaisons"], max(CT["pire_ecart"], CT["ecart_largeur"])),
            "Sur %d niveaux, %d n'est pas fiable." % (sum(RJ[k]["niveaux"] for k in RJ), sum(RJ[k]["non_fiables"] for k in RJ)),
            "s'y accordent a %.4f pres sous la routine de plateau deposee" % max(p["etendue_absorbeurs"] for p in LL["par_x"]),
            "Au registre (%s, %d fichiers lus) : %d fichiers portent un w2 candidat, sous %d noms." % (tete, VR["lus"], len(VR["touches"]), len(VR["noms"])),
            "(%d fichiers lus) : %d fichier porte un w2 candidat." % (VP["lus"], len(VP["touches"])),
            "la somme des parts vaut %.3f +- %.3f sur 32 boites" % (CG["E"]["somme"], CG["E"]["erreur"]),
            "rend la densite 2D a %.4f pres en moyenne sur la fenetre" % abs(LL["moyenne_fenetre"] - 1.0),
            "des %d cellules candidates (%d w2)" % (len(cel), 16)]
manque = [a for a in attendus if a not in plat]
chk("R08", not manque and len(VR["nom_2d"]) == 0 and CT["tient"], "treize phrases chiffrees recalculees des pieces et retrouvees dans le texte ; manquent : %s" % manque)
# R09 le tableau par creneau et par profondeur
ok = True
for s in ("MG", "PG"):
    for m in (3, 4, 5):
        X = [x for (s2, _, x) in cel if s2 == s and x["m"] == m]
        l = "    %-7s  %d   %.3f    %.4f    %.4f     %.4f   %.1e a %.1e    %.0e a %.0e" % (s, m, max(x["e_bord"] for x in X), max(x["etendue"] for x in X), max(max(x["etendue_rho3"]) for x in X),
            max(max(abs(p) for p in x["pas_2_3"]) for x in X), math.exp(min(x["ln_G3"] for x in X)), math.exp(max(x["ln_G3"] for x in X)),
            math.exp(min(x["ln_rho3"][-1] + math.log(abs(float(F(cd["w2"])) - 2.0)) for (s2, cd, x) in cel if s2 == s and x["m"] == m)),
            math.exp(max(x["ln_rho3"][-1] + math.log(abs(float(F(cd["w2"])) - 2.0)) for (s2, cd, x) in cel if s2 == s and x["m"] == m)))
        ok = ok and l in lignes
chk("R09", ok, "section 7 : les six lignes par creneau et par profondeur, recalculees")
# R10 les citations de machine 2
note = open(LOT_M2 + "/POUR_MACHINE1_grandes_boites_resultats_machine2_v1.md", encoding="utf-8").read()
cit = re.findall(r'donne : "([^"]+)", et "([^"]+)"', plat)
chk("R10", len(cit) == 1 and all(c in note for c in cit[0]), "les deux citations de la note de machine 2 y sont mot pour mot")
# R11 le tirage de demonstration sur la table
log = open(D + "/tirage_pont_machine1_v1_demonstration.log").read()
gs = {(s, cd["w2"], x["m"]): x["g"] for (s, cd, x) in cel}
ok = all(("%-4s w2 = %-10s m = %d g = %s" % ("%s%d" % (s, m), w, m, gs[(s, w, m)])) in log for s, w in (("MG", "1987/1000"), ("PG", "2019/1000")) for m in (3, 4, 5))
chk("R11", ok and "CE N'EST PAS UN TIRAGE : 6 cellules" in log and "AUTOTEST : TIENT" in open(D + "/tirage_pont_machine1_v1_autotest.log").read(),
    "le journal de demonstration rend six cellules aux couplages de la table ; l'autotest du tirage tient")
print("RELEVE : %d controles, %d mordent : %s" % (n, len(mord), mord))
sys.exit(1 if mord else 0)
