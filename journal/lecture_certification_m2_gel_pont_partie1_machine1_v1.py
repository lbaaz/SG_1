#!/usr/bin/env python3
# machine 1, 2026-11-17. Lecture de la certification par machine 2 du gel "pont", premiere partie.
# Ne lance AUCUN script de machine 2 : ses fichiers sont lus comme des donnees.
# Usage : python3 -I -B ce_script <ma table d03c...json> <dossier certif de machine 2> <mon gel .md>
#                                 <sortie.json>
import hashlib
import json
import math
import re
import sys
import unicodedata


def canon_b(octets):
    t = unicodedata.normalize("NFC", octets.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


def sous_ensemble(table):
    """La table au format de la section 5 du gel : decisions et couplages seuls."""
    out = {"creneaux": {}}
    for nom, cr in table["creneaux"].items():
        cands = []
        for c in cr["candidats"]:
            cands.append({"w2": c["w2"], "eligible": c["eligible"],
                          "cellules": [{"m": x["m"], "g": x["g"], "eligible": x["eligible"]}
                                       for x in c["cellules"]]})
        out["creneaux"][nom] = {"candidats": cands}
    return out


def main():
    ma_table, dossier, gel, sortie = sys.argv[1:5]
    res = {}
    moi = json.load(open(ma_table, encoding="utf-8"))
    brut_commune = open(dossier + "/table_commune_pont_v1.json", "rb").read()
    brut_sienne = open(dossier + "/table_eligibilite_pont_machine2_v1.json", "rb").read()
    commune = json.loads(brut_commune.decode("utf-8"))

    # 1. la table commune : mon sous-ensemble, serialise comme machine 2 le dit, contre ses octets
    sub = sous_ensemble(moi)
    texte = json.dumps(sub, indent=1, sort_keys=True)
    essais = {"tel quel": texte.encode("utf-8"), "avec LF final": (texte + "\n").encode("utf-8")}
    res["serialisation_identique"] = {k: (v == brut_commune) for k, v in essais.items()}
    res["canon_commune_fichier"] = canon_b(brut_commune)
    res["canon_mon_sous_ensemble"] = canon_b(texte.encode("utf-8"))
    res["sa_table_egale_commune_octets"] = (brut_sienne == brut_commune)
    res["objets_egaux"] = (sub == commune)
    res["cles_hors_format"] = sorted(set(commune.keys()) - {"creneaux"})

    # 2. compte de la table commune
    compte = {}
    for nom, cr in commune["creneaux"].items():
        el = [c["w2"] for c in cr["candidats"] if c["eligible"]]
        compte[nom] = {"candidats": len(cr["candidats"]), "eligibles": len(el), "w2_eligibles": el,
                       "cellules": sum(len(c["cellules"]) for c in cr["candidats"])}
    res["compte"] = compte

    # 3. ses details (sa chaine a elle) contre mes nombres, sans arrondi
    det = json.load(open(dossier + "/details_eligibilite_pont_machine2_v1.json", encoding="utf-8"))
    res["details_cles_racine"] = sorted(det.keys())[:12] if isinstance(det, dict) else "liste"
    json.dump(res, open(sortie, "w", encoding="utf-8"), indent=1, sort_keys=True)
    for k in sorted(res):
        print(k, ":", json.dumps(res[k], sort_keys=True))


if __name__ == "__main__":
    main()
