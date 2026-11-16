# -*- coding: ascii -*-
"""BALAYAGE DE VIRGINITE DES w2 CANDIDATS DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16. Aucun calcul.
Cherche, dans TOUS les fichiers des dossiers donnes (sous-dossiers compris, .git exclu), toute trace d'un w2 candidat :
(1) sa fraction irreductible ("397/200") ; (2) son ecriture decimale au millieme a moins de seize caracteres non
numeriques apres "w2", "w_2", "omega2" ou "omega_2" (casse indifferente). Un fichier de ce gel qui porte ces ecritures
par construction (tables d'eligibilite, tirage, cette piece) est compte a part : il est donne apres --connus.
(3) dans les fichiers .json seulement : une etiquette d'etat (0, 0), ecrite "n1": 0, "n2": 0 ou "etiquette": [0, 0] ;
(4) dans les fichiers .json seulement : une cle "delta" dont la valeur d fait de 2 + d un w2 candidat (a 1e-9 pres).
Ce balayage ne voit que ce qui est ecrit sur le poste de machine 1 ; il ne dit rien des archives de machine 2.
Un sous-dossier nomme apres --hors n'est pas parcouru (le dossier des pieces de ce gel, qui portent les candidats par
construction).
Usage : python3 -I -B balayage_virginite_machine1_v1.py <sortie.json> <dossier> [<dossier> ...] [--hors <nom de sous-dossier>] [--connus <prefixe de nom> ...]"""
import sys, os, re, json
from fractions import Fraction as F
SORTIE = sys.argv[1]; reste = sys.argv[2:]
connus = reste[reste.index("--connus") + 1:] if "--connus" in reste else []
reste = reste[:reste.index("--connus")] if "--connus" in reste else reste
hors = reste[reste.index("--hors") + 1:] if "--hors" in reste else []
dossiers = reste[:reste.index("--hors")] if "--hors" in reste else reste
cands = [F(k, 1000) for k in list(range(1981, 1990)) + list(range(1991, 2000)) + list(range(2001, 2010)) + list(range(2011, 2020))]
dec = sorted(set("%.3f" % float(w) for w in cands)); fr = sorted(set("%d/%d" % (w.numerator, w.denominator) for w in cands))
rx_fr = re.compile(r"(?<![0-9/])(" + "|".join(re.escape(p) for p in fr) + r")(?![0-9/])")
rx_w2 = re.compile(r"(?i)(w2|w_2|omega2|omega_2)[^0-9\n]{0,16}(" + "|".join(re.escape(p) for p in dec) + r")(?![0-9])")
rx_00 = re.compile(r'"n1":\s*0(\.0)?,\s*"n2":\s*0(\.0)?[,}\s]|"etiquette":\s*\[\s*0,\s*0\s*\]')
lus = 0; illisibles = 0; traces = {}; par_construction = {}; json_lus = 0; etiquettes_00 = {}; deltas = {}; json_non_lus = 0
def marche(o, out):
    if isinstance(o, dict):
        d = o.get("delta")
        if isinstance(d, (int, float)) and not isinstance(d, bool):
            w = F(2) + F(d).limit_denominator(10 ** 6)
            if w in cands and abs(float(w) - 2.0 - d) < 1e-9:
                out.add("%.3f" % float(w))
        for v in o.values():
            marche(v, out)
    elif isinstance(o, list):
        for v in o:
            marche(v, out)
for racine in dossiers:
    for d, sous, fs in os.walk(racine):
        sous[:] = sorted(x for x in sous if x != ".git" and x not in hors)
        for f in sorted(fs):
            p = os.path.join(d, f)
            try:
                t = open(p, "rb").read().decode("utf-8", errors="ignore")
            except OSError:
                illisibles += 1; continue
            lus += 1
            if f.endswith(".json"):
                json_lus += 1; n00 = len(rx_00.findall(t))
                if n00 and not any(f.startswith(c) for c in connus):
                    etiquettes_00[p] = n00
                try:
                    vus = set(); marche(json.loads(t), vus)
                    if vus and not any(f.startswith(c) for c in connus):
                        deltas[p] = sorted(vus)
                except ValueError:
                    json_non_lus += 1
            a = sorted(set(rx_fr.findall(t))); b = sorted(set(x[1] for x in rx_w2.findall(t)))
            if a or b:
                (par_construction if any(f.startswith(c) for c in connus) else traces)[p] = {"fractions": a, "decimaux_apres_w2": b}
print("dossiers : %s%s" % (" ; ".join(dossiers), (" ; sous-dossiers non parcourus : " + " ".join(hors)) if hors else ""))
print("fichiers lus : %d ; illisibles : %d ; w2 candidats : %d" % (lus, illisibles, len(cands)))
print("fichiers de ce gel portant les candidats par construction : %d" % len(par_construction))
for p in sorted(par_construction):
    print("  (par construction) %s" % p)
print("AUTRES fichiers portant la trace d'un w2 candidat : %d" % len(traces))
for p in sorted(traces):
    print("  TRACE %s : %s %s" % (p, traces[p]["fractions"], traces[p]["decimaux_apres_w2"]))
print("fichiers .json lus : %d ; portant une etiquette d'etat (0, 0) hors des pieces de ce gel : %d" % (json_lus, len(etiquettes_00)))
for p in sorted(etiquettes_00):
    print("  ETIQUETTE (0, 0) %s : %d fois" % (p, etiquettes_00[p]))
print("fichiers .json portant une cle delta qui designe un w2 candidat, hors des pieces de ce gel : %d ; .json non analyses : %d" % (len(deltas), json_non_lus))
for p in sorted(deltas):
    print("  DELTA %s : %s" % (p, " ".join(deltas[p])))
print("BALAYAGE : %s" % ("AUCUNE TRACE hors des pieces de ce gel" if not (traces or etiquettes_00 or deltas) else "DES TRACES, a lire une par une"))
json.dump({"dossiers": dossiers, "hors": hors, "lus": lus, "illisibles": illisibles, "candidats": len(cands), "par_construction": sorted(par_construction), "traces": traces,
           "json_lus": json_lus, "etiquettes_00": etiquettes_00, "deltas": deltas, "json_non_lus": json_non_lus}, open(SORTIE, "w"), indent=1, sort_keys=True)
