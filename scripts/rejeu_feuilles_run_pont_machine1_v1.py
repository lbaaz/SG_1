# -*- coding: ascii -*-
"""REJEU PAR MACHINE 1 DE SES TROIS FEUILLES SUR LES SORTIES DU RUN DU GEL "PONT" -- v1, 2026-11-18.
Les sorties de sondes de machine 2 sont lues comme des donnees ; aucun script de machine 2 n'est lance ; aucune 2D.
(0) les trois feuilles et le bloc de machine 1 sont ceux du gel (canons de la section 15) ;
(1) COMPLETUDE (rectificatif 9e25019f3b9bdf04) : 24 sorties de densite a douze barreaux k = -3 a 8 ; par cellule, les
    vingt cotes 180 a 189 et 291 a 300, chacun une fois ; cellule de chaque fichier = cellule du tirage ;
(2) la table de la chaine de machine 2 contre celle de machine 1 ;
(3) les trois feuilles rejouees sur ces sorties, avec la table de machine 2 (celle du run) ;
(4) mes sorties contre celles que machine 2 a rendues, nombre par nombre, a 1e-12 pres ;
(5) les verdicts refaits avec MA table de la chaine : memes decisions ?
Usage : python3 -I -B ce_script <dossier du run de machine 2> <dossier partie2 de machine 1> <gel partie 2.md>
                                <clone du registre> <dossier de sortie>"""
import sys, os, re, json, math, subprocess, hashlib, unicodedata
RUN, P2, GEL, CLONE, OUT = [a.rstrip("/") for a in sys.argv[1:6]]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
NOMS = ("MG3", "MG4", "MG5", "PG3", "PG4", "PG5"); res = {}
g = open(GEL, encoding="ascii").read()
feuilles = ("lecture_densite_2d_pont_machine1_v1.py", "lecture_boites_pont_machine1_v1.py", "verdict_pont_machine1_v1.py", "chaine_pont_bloc_machine1_v1.py")
for f in feuilles: assert "    %s  %s\n" % (canon(P2 + "/" + f), f) in g, f
print("(0) les trois feuilles et le bloc de la chaine sont ceux de la section 15 du gel")
MA = json.load(open(P2 + "/chaine_cellules_pont_v1.json")); SA = json.load(open(RUN + "/chaine_cellules_pont_v1.json")); X = MA["ecarts"]
# (1) completude
fautes = []
for n in NOMS:
    c = MA["cellules"][n]
    for a in "ABCD":
        d = json.load(open("%s/densite_2d_%s_%s.json" % (RUN, n, a)))
        if sorted(int(k) for k in d["k"]) != list(range(-3, 9)): fautes.append("barreaux %s %s" % (n, a))
        if (d["w2"], d["m"], d["g"], d["absorbeur"]) != (c["w2"], c["m"], c["g"], a): fautes.append("cellule %s %s" % (n, a))
    cotes = []
    for f in sorted(os.listdir(RUN)):
        if f.startswith("boites_%s_" % n) and f.endswith(".jsonl"):
            for l in open(RUN + "/" + f, encoding="ascii"):
                if l.strip():
                    b = json.loads(l); cotes.append(b["cote"])
                    if (b["w2"], b["m"], b["g"]) != (c["w2"], c["m"], c["g"]): fautes.append("cellule de boite %s" % n)
    if sorted(cotes) != list(range(180, 190)) + list(range(291, 301)): fautes.append("cotes %s : %s" % (n, sorted(cotes)))
res["completude"] = {"fautes": fautes, "sorties_de_densite": 24, "boites": 120}
print("(1) completude : %s" % ("24 sorties de densite a douze barreaux, 120 boites, vingt cotes par cellule, chacun une fois" if not fautes else "FAUTES " + str(fautes)))
# (2) table de la chaine
p = 0.0
for n in NOMS:
    a, b = MA["cellules"][n], SA["cellules"][n]; assert (a["w2"], a["m"], a["g"], a["m_bord"], a["r_c"]) == (b["w2"], b["m"], b["g"], b["m_bord"], b["r_c"])
    p = max([p, abs(a["ln_G3"] - b["ln_G3"]), abs(a["e_bord"] - b["e_bord"])] + [abs(u - v) for k in ("ln_rho3", "ln_rho2", "pas_2_3", "etendue_rho3") for u, v in zip(a[k], b[k])])
res["table_chaine_ecart_max"] = p; print("(2) table de la chaine, machine 2 contre machine 1, six cellules : plus grand ecart %.2e" % p)
# (3) rejeu
env = dict(os.environ)
def lance(args, journal):
    r = subprocess.run([sys.executable, "-I", "-B"] + args, capture_output=True, text=True, env=env)
    open(journal, "w").write(r.stdout + r.stderr); assert r.returncode == 0, (journal, r.stderr[-400:])
S = CLONE + "/scripts/"; blocs = [S + "m17_chaine_v17.py", S + "chaine_ordre2_bloc_machine1_v1.py", S + "ordre3_bloc_machine1_v1.py", S + "chaine_adaptee_bloc_machine1_v1.py", P2 + "/chaine_pont_bloc_machine1_v1.py"]
boites = sorted(RUN + "/" + f for f in os.listdir(RUN) if f.startswith("boites_") and f.endswith(".jsonl"))
lance([P2 + "/lecture_boites_pont_machine1_v1.py"] + blocs + [OUT + "/lecture_boites.json"] + boites, OUT + "/lecture_boites.log")
for table, suff in ((RUN + "/chaine_cellules_pont_v1.json", ""), (P2 + "/chaine_cellules_pont_v1.json", "_table_m1")):
    for n in NOMS:
        lance([P2 + "/lecture_densite_2d_pont_machine1_v1.py", table, n, "%s/lecture_densite_2d_%s%s.json" % (OUT, n, suff)] + ["%s/densite_2d_%s_%s.json" % (RUN, n, a) for a in "ABCD"],
              "%s/lecture_densite_2d_%s%s.log" % (OUT, n, suff))
    lance([P2 + "/verdict_pont_machine1_v1.py", table, OUT + "/lecture_boites.json", "%s/verdict%s.json" % (OUT, suff)] + ["%s/lecture_densite_2d_%s%s.json" % (OUT, n, suff) for n in NOMS],
          "%s/verdict%s.log" % (OUT, suff))
print("(3) trois feuilles rejouees sur les sorties du run")
# (4) contre les sorties rendues par machine 2
def compare(a, b, chemin=""):
    """Rend (nombres compares, plus grand ecart, desaccords de structure ou de valeur non numerique)."""
    if isinstance(a, dict) and isinstance(b, dict):
        n, e, d = 0, 0.0, [chemin + "/cles"] if sorted(a) != sorted(b) else []
        for k in sorted(set(a) & set(b)):
            n2, e2, d2 = compare(a[k], b[k], chemin + "/" + str(k)); n += n2; e = max(e, e2); d += d2
        return n, e, d
    if isinstance(a, list) and isinstance(b, list):
        n, e, d = 0, 0.0, [chemin + "/longueur"] if len(a) != len(b) else []
        for i, (u, v) in enumerate(zip(a, b)):
            n2, e2, d2 = compare(u, v, chemin + "/" + str(i)); n += n2; e = max(e, e2); d += d2
        return n, e, d
    if isinstance(a, bool) or isinstance(b, bool) or a is None or b is None or isinstance(a, str) or isinstance(b, str):
        return 0, 0.0, ([] if a == b else [chemin])
    if a != a and b != b: return 1, 0.0, []
    return 1, abs(a - b) / max(1.0, abs(a), abs(b)), []
tot_n, tot_e, tot_d = 0, 0.0, []
for f in ["lecture_boites.json", "verdict.json"] + ["lecture_densite_2d_%s.json" % n for n in NOMS]:
    n, e, d = compare(json.load(open(OUT + "/" + f)), json.load(open(RUN + "/" + f))); tot_n += n; tot_e = max(tot_e, e); tot_d += [f + x for x in d]
res["contre_machine2"] = {"nombres": tot_n, "ecart_max": tot_e, "desaccords": tot_d}
print("(4) mes sorties contre celles rendues par machine 2 : %d nombres, plus grand ecart %.2e, desaccords non numeriques %d %s" % (tot_n, tot_e, len(tot_d), tot_d[:3]))
# (5) verdicts avec ma table
V = json.load(open(OUT + "/verdict.json")); W = json.load(open(OUT + "/verdict_table_m1.json"))
dv = [(n, f) for n in NOMS for f in ("L", "L2", "S", "C") if V["cellules"][n][f]["verdict"] != W["cellules"][n][f]["verdict"]] + \
     [f for f in ("L", "L2", "S", "C") if V["familles"][f]["verdict"] != W["familles"][f]["verdict"]]
res["verdicts_avec_ma_table_differents"] = dv
print("(5) verdicts avec la table de machine 1 au lieu de celle de machine 2 : %s" % ("les memes, 24 cellule x famille et 4 familles" if not dv else "DIFFERENTS " + str(dv)))
print(open(OUT + "/verdict.log").read())
json.dump(res, open(OUT + "/rejeu_feuilles_run_pont_v1.json", "w"), indent=1, sort_keys=True)
sys.exit(0 if (not fautes and not tot_d and tot_e <= 1e-12 and not dv) else 1)
