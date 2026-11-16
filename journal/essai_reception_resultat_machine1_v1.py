# -*- coding: ascii -*-
"""ESSAI DE LA RECEPTION DU RESULTAT -- machine 1, v1, 2026-11-16. Ecrit pendant le run, avant tout resultat. Il doit MORDRE.
Joue reception_resultat_gel_vide_machine1_v1.py sur les dossiers SYNTHETIQUES du banc de la feuille (aucune mesure ; ils ne
disent rien des cellules) et sur des retouches de ces dossiers, et compare a l'effet ecrit avant.
Usage : python3 -I -B essai_reception_resultat_machine1_v1.py <reception_resultat.py> <feuille_vide.py> <lecture_lecteur (deposee)>
        <table gelee.json> <gel partie 2.md> <dossier des cas du banc (garde)> <dossier de travail (neuf)>"""
import sys, os, json, math, shutil, subprocess
RECEPTION, FEUILLE, F_LECT, TABLE, GEL, BANC, TRAVAIL = sys.argv[1:8]
os.makedirs(TRAVAIL, exist_ok=False)
CAS = []
def jouer(nom, run):
    d = os.path.join(TRAVAIL, "r_" + nom)
    p = subprocess.run([sys.executable, "-I", "-B", RECEPTION, FEUILLE, F_LECT, TABLE, GEL, run, d], capture_output=True, text=True)
    f = os.path.join(d, "reception_resultat_vide_v1.json")
    return p.returncode, (json.load(open(f)) if os.path.exists(f) else None), p.stdout + p.stderr
def copie(nom, source):
    d = os.path.join(TRAVAIL, "run_" + nom); shutil.copytree(os.path.join(BANC, source), d); return d
def cas(nom, attendu, run, test):
    code, R, console = jouer(nom, run)
    try:
        ok = bool(test(code, R))
    except Exception as e:
        ok = False; attendu += " [exception : %r]" % (e,)
    CAS.append((nom, ok)); print("  %-4s %s : %s" % ("TENU" if ok else "RATE", nom, attendu), flush=True)
    if not ok:
        print(console)
an = lambda R, k: R["annonces"][k]
B = lambda nom: os.path.join(BANC, nom)

cas("r00_base", "cas de base : verdicts identiques, ecart nul ; A-1 a A-6 vraies, V1 TENU a 0.50, VP TENU a 0.35, MG positif a 0.40", B("b00_base"),
    lambda c, R: c == 0 and R["comparaison"]["issue"] == "VERDICTS IDENTIQUES" and R["comparaison"]["plus_grand_ecart"] == 0.0 and an(R, "A-1")["realise"] is True
    and an(R, "A-2")["realise"] is True and an(R, "A-3")["realise"] == {"seize": True, "douze_au_moins": True} and an(R, "A-4")["realise"] == "TENU"
    and an(R, "A-4")["probabilite_de_l_issue"] == 0.50 and an(R, "A-5")["probabilite_de_l_issue"] == 0.35 and an(R, "A-6")["realise"] is True and an(R, "A-7")["realise"] == "positif")
cas("r01_sauf_une", "une cellule tombe : V1 TENU SAUF UNE CELLULE a 0.05 ; A-6 fausse (|ln q| = 0.05)", B("b01_une_tombe"),
    lambda c, R: an(R, "A-4")["realise"] == "TENU SAUF UNE CELLULE" and an(R, "A-4")["probabilite_de_l_issue"] == 0.05 and an(R, "A-6")["realise"] is False and an(R, "A-6")["cellule"] == "MG4")
cas("r02_tombe", "deux cellules tombent : V1 TOMBE a 0.08", B("b03_deux_tombent"), lambda c, R: an(R, "A-4")["realise"] == "TOMBE" and an(R, "A-4")["probabilite_de_l_issue"] == 0.08)
cas("r03_non_concluant", "cinq non jugeables : V1 NON CONCLUANT a 0.32", B("b05_trop_de_non_jugeables"),
    lambda c, R: an(R, "A-4")["realise"] == "NON CONCLUANT" and an(R, "A-4")["probabilite_de_l_issue"] == 0.32)
cas("r04_non_qualifie", "PP4 NON QUALIFIE : A-3 quinze (seize fausse, douze vraie) ; A-2 INDETERMINEE (27 temoins juges et tenus)", B("b07_desaccord_C"),
    lambda c, R: an(R, "A-3")["qualifiees"] == 15 and an(R, "A-3")["realise"] == {"seize": False, "douze_au_moins": True} and an(R, "A-2")["realise"] == "INDETERMINEE"
    and an(R, "A-2")["temoins_tenus"] == 27 and an(R, "A-2")["indication_cellules"] == 28)
cas("r05_temoin", "le jumeau de PP4 est trop large : A-2 FAUSSE, PP4 nommee", B("b10_temoin_trop_large"),
    lambda c, R: an(R, "A-2")["realise"] is False and an(R, "A-2")["temoins_non_tenus"] == ["PP4"])
cas("r06_instrument", "l'instrument ne tient pas : A-1 fausse ; A-4 et A-5 a 'instrument' (0.05) ; A-6 INDETERMINEE", B("b12_instrument"),
    lambda c, R: an(R, "A-1")["realise"] is False and an(R, "A-4")["realise"] == "instrument" and an(R, "A-5")["probabilite_de_l_issue"] == 0.05 and an(R, "A-6")["realise"] == "INDETERMINEE")
cas("r07_incomplet", "un fichier manque : l'inventaire le nomme ; rien n'est juge ; A-4 a 'instrument'", B("b13_fichier_absent"),
    lambda c, R: R["inventaire"]["manquent"] == ["sonde_vide_MG8.json"] and an(R, "A-4")["realise"] == "instrument" and R["comparaison"]["issue"] == "VERDICTS IDENTIQUES")
cas("r08_profondes_tombent", "deux profondes tombent : VP TOMBE a 0.10, V1 TENU", B("b18_profondes_tombent"),
    lambda c, R: an(R, "A-5")["realise"] == "TOMBE" and an(R, "A-5")["probabilite_de_l_issue"] == 0.10 and an(R, "A-4")["realise"] == "TENU")
cas("r09_profondes_non_lues", "aucune profonde lue : VP NON LUE, comptee 'NON LUE ou NON CONCLUANT' a 0.45", B("b19_profondes_non_lues"),
    lambda c, R: an(R, "A-5")["realise"] == "NON LUE ou NON CONCLUANT" and an(R, "A-5")["probabilite_de_l_issue"] == 0.45)
cas("r10_profondes_peu_lues", "cinq profondes jugees : VP NON CONCLUANT, meme case a 0.45", B("b20_profondes_peu_lues"),
    lambda c, R: an(R, "A-5")["realise"] == "NON LUE ou NON CONCLUANT")

# retouches du verdict "de machine 2" : la comparaison doit mordre
d = copie("m_issue", "b00_base"); f = os.path.join(d, "verdict_vide.json"); V = json.load(open(f)); V["V1"]["issue"] = "TOMBE"; json.dump(V, open(f, "w"))
cas("r11_issue_retouchee", "le verdict de machine 2 dit V1 TOMBE, le rejeu dit TENU : VERDICTS DIFFERENTS, champ nomme", d,
    lambda c, R: R["comparaison"]["issue"] == "VERDICTS DIFFERENTS" and [x["champ"] for x in R["comparaison"]["champs_discrets_differents"]] == ["/V1/issue"])
d = copie("m_jugement", "b00_base"); f = os.path.join(d, "verdict_vide.json"); V = json.load(open(f))
[x for x in V["cellules"] if x["id"] == "PG6"][0]["jugement"] = "NON JUGEABLE"; json.dump(V, open(f, "w"))
cas("r12_jugement_retouche", "une cellule jugee autrement par machine 2 : VERDICTS DIFFERENTS, cellule nommee", d,
    lambda c, R: [x["champ"] for x in R["comparaison"]["champs_discrets_differents"]] == ["/cellules/PG6/jugement"])
d = copie("m_nombre", "b00_base"); f = os.path.join(d, "verdict_vide.json"); V = json.load(open(f))
[x for x in V["cellules"] if x["id"] == "MP5"][0]["ln_q"] += 1e-9; json.dump(V, open(f, "w"))
cas("r13_nombre_retouche", "un ln q de machine 2 deplace de 1e-9 : verdicts identiques (aucun champ discret), mais l'ecart est rendu et le champ nomme", d,
    lambda c, R: R["comparaison"]["issue"] == "VERDICTS IDENTIQUES" and 0.5e-9 < R["comparaison"]["plus_grand_ecart"] < 2e-9 and R["comparaison"]["plus_grand_ecart_champ"] == "/cellules/MP5/ln_q")
d = copie("m_absent", "b00_base"); os.remove(os.path.join(d, "verdict_vide.json"))
cas("r14_verdict_absent", "le verdict de machine 2 manque : dit, et les annonces sont lues quand meme sur le rejeu", d,
    lambda c, R: R["comparaison"]["issue"] == "LE VERDICT DE MACHINE 2 MANQUE AU DOSSIER" and R["inventaire"]["manquent"] == ["verdict_vide.json"] and an(R, "A-4")["realise"] == "TENU")

# retouches des fichiers de cellule : le signe a MG
def deplacer(d, ids, decalage):
    for i in ids:
        f = os.path.join(d, "sonde_vide_%s.json" % i); S = json.load(open(f))
        for a in S["fantome"]["traj"]:
            for k in S["fantome"]["traj"][a]:
                for cle in ("gamma", "gamma_im"):
                    S["fantome"]["traj"][a][k][cle] *= math.exp(decalage)
        json.dump(S, open(f, "w"))
d = copie("mg_negatif", "b00_base"); deplacer(d, ("MG3", "MG4", "MG5"), +0.006)
cas("r15_mg_negatif", "trois plateaux de MG releves de 0.006 (ln q = -0.004) : A-7 'negatif' a 0.40 ; le verdict de machine 2, reste celui du cas de base, DIFFERE : les signes consignes de MG3, MG4, MG5 sont nommes, aucune issue ni aucun jugement", d,
    lambda c, R: an(R, "A-7")["realise"] == "negatif" and an(R, "A-7")["negatives"] == ["MG3", "MG4", "MG5"] and an(R, "A-7")["probabilite_de_l_issue"] == 0.40
    and R["comparaison"]["plus_grand_ecart"] > 0.005 and R["comparaison"]["issue"] == "VERDICTS DIFFERENTS"
    and [x["champ"] for x in R["comparaison"]["champs_discrets_differents"]][:3] == ["/cellules/%s/consigne/signe_de_ln_q" % i for i in ("MG3", "MG4", "MG5")]
    and not any(x["champ"].endswith(("/issue", "/jugement")) for x in R["comparaison"]["champs_discrets_differents"]))
d = copie("mg_partage", "b00_base"); deplacer(d, ("MG3", "MG4"), +0.006)
cas("r16_mg_partage", "deux negatifs et deux positifs a MG : A-7 'ni l'un ni l'autre', a 0.20 (le reste)", d,
    lambda c, R: an(R, "A-7")["realise"] == "ni l'un ni l'autre" and abs(an(R, "A-7")["probabilite_de_l_issue"] - 0.20) < 1e-9)
d = copie("mg_bande", "b00_base"); deplacer(d, ("MG3", "MG4", "MG5", "MG6"), -0.010)
cas("r17_mg_au_dela_de_la_bande", "quatre plateaux de MG abaisses de 0.010 (ln q = +0.012) : positifs, et au-dela de la bande aux quatre", d,
    lambda c, R: an(R, "A-7")["realise"] == "positif" and an(R, "A-7")["au_dela_de_la_bande"] == ["MG3", "MG4", "MG5", "MG6"] and an(R, "A-6")["realise"] is False)

# refus
code, R, console = jouer("refus_sortie", B("b00_base")); code2, R2, console2 = jouer("refus_sortie", B("b00_base"))
ok = code == 0 and code2 != 0; CAS.append(("r18_sortie_existante", ok)); print("  %-4s r18_sortie_existante : la reception refuse d'ecrire dans un dossier de sortie qui existe" % ("TENU" if ok else "RATE"))
avant = sorted(os.listdir(B("b00_base"))); jouer("intact", B("b00_base")); ok = sorted(os.listdir(B("b00_base"))) == avant
CAS.append(("r19_run_intact", ok)); print("  %-4s r19_run_intact : rien n'est ecrit dans le dossier du run" % ("TENU" if ok else "RATE"))
n = sum(1 for _, ok in CAS if ok)
print("ESSAI DE LA RECEPTION : %d cas tenus sur %d : %s" % (n, len(CAS), "IL MORD COMME ATTENDU" if n == len(CAS) else "A REPRENDRE"))
sys.exit(0 if n == len(CAS) else 1)
