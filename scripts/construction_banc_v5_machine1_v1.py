#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
construction_banc_v5_machine1_v1.py -- MACHINE 1
=================================================
Construit banc_qualification_machine1_v5.py par REMPLACEMENTS ANCRES,
en COMPOSITION EPINGLEE :

    v3 DEPOSEE (5fae2a8c94cf8685, arbre a4a907a)
      -- construction_banc_v4_machine1_v1.py (35b9ff3b8e5b7ef0, 53 rempl.)
      --> banc_qualification_machine1_v4.py  **PIN 36a3f06f19871c38**
        -- LE PRESENT SCRIPT (17 remplacements)
        --> banc_qualification_machine1_v5.py

Le fichier v4 doit etre PRESENT a cote et resoudre son PIN : il a ete
reproduit AU BIT par les deux machines depuis la v3 deposee
(certification f882b9c04c7b7ced, section 1). PB-1 : rien n'est edite.

PERIMETRE v5 (fige, 3258684af5ba744c section 3 + contrat e69d8a006f584063) :
  (i)   D-I-1 : un pre-vol n'asserte que ce que son factice determine ;
        le verdict se CONSIGNE ; les sorties s'ecrivent AVANT tout arret.
  (ii)  D-I-2 : dossier de sortie VIDE OU VERSIONNE avant ecriture.
  (iii) critere 5.4 (gel v11 a2e7ef3e237c5acf) : W-plancher = la garde
        e(dt2/2) >= C(p) x plancher_comp, C(p) = 1/(1-2^-tol_ordre) en
        PLEINE PRECISION consigne ; sous le seuil l'ordre N'EST PAS LU.
  (iv)  LD-16 : **HERITE VERBATIM -- dette D-v5-1** : le depot 9bis clos
        (c4310e33da6b9759) fige les lectures de /T1 /T3a (plancher_dt2,
        statuts) ; LD-16bis y changerait des feuilles et ferait mordre
        9bis sur tout run legitime. Arbitrage requis (depot re-ancre ou
        LD-16bis en v6). c_pl survit UNIQUEMENT la, et il est nomme.
  (v)   chargeur --controle-9bis au CONTRAT (a)-(d)+(c') : depot
        autoporteur, comptes ET profondeur re-derives, custody contre le
        registre = MORSURE, absent = NON JOUE consigne, forme canonique
        json.dumps(sort_keys, ensure_ascii, separateurs PAR DEFAUT).

ANCRES E19 : gel temoin v11 (a2e7ef3e237c5acf) + certification v2
(7fc5f2412b99ad50) remplacent v9/b5da7478 ; bases v7/v5 inchangees.
"""
import hashlib, sys, unicodedata

SRC = "banc_qualification_machine1_v4.py"
PIN = "36a3f06f19871c38"
DST = "banc_qualification_machine1_v5.py"

def canon(b):
    return hashlib.sha256(unicodedata.normalize("NFC", b.decode("utf-8"))
                          .replace("\r\n", "\n").encode()).hexdigest()[:16]

raw = open(SRC, "rb").read()
assert canon(raw) == PIN, "PIN v4 : %s attendu %s" % (canon(raw), PIN)
s = raw.decode()

R = []

R.append(('Q01 en-tete : lignee du gel temoin -> v11',
"""gel temoin v9 (403488b4f6c319e9, sections 3, 5.2, 8, 9bis) --""",
"""gel temoin v11 (a2e7ef3e237c5acf, sections 3, 5.2, 5.4, 8, 9bis) --"""))

R.append(('Q02 en-tete : pieces d\'ancre v11 + note v2, lignee v9 conservee',
"""  gels/temoin_negatif_pre_enregistrement_v9.md   403488b4f6c319e9  57914 o  CERTIFIE
    par journal/note_machine1_certification_temoin_v9_v1.md b5da74783e5f97c6 7085 o""",
"""  gels/temoin_negatif_pre_enregistrement_v11.md  a2e7ef3e237c5acf  72281 o  CERTIFIE
    par journal/note_machine1_certification_temoin_v11_v2.md 7fc5f2412b99ad50 3569 o
    (lignee : v9 403488b4f6c319e9 certifiee, superseded par la v11)"""))

R.append(('Q03 VERSION',
"""VERSION = "banc_qualification_machine1_v4\"""",
"""VERSION = "banc_qualification_machine1_v5\""""))

R.append(('Q04 ancres E19 : tuples v11 + note v2',
"""GEL_TEMOIN = ("gels/temoin_negatif_pre_enregistrement_v9.md", "403488b4f6c319e9", 57914)""",
"""GEL_TEMOIN = ("gels/temoin_negatif_pre_enregistrement_v11.md", "a2e7ef3e237c5acf", 72281)"""))

R.append(('Q05 ancres E19 : certification v2',
"""CERT_TEMOIN = ("journal/note_machine1_certification_temoin_v9_v1.md", "b5da74783e5f97c6")""",
"""CERT_TEMOIN = ("journal/note_machine1_certification_temoin_v11_v2.md", "7fc5f2412b99ad50")"""))

R.append(('Q06 c_pl : demote -- il ne survit que dans LD-16 herite (D-v5-1)',
"""C_PL = 10""",
"""C_PL = 10                         # LD-16 HERITE VERBATIM (dette D-v5-1) : le depot
                                  # 9bis clos fige les lectures de /T1 /T3a ; toute
                                  # LD-16bis attend l'arbitrage (depot re-ancre ou v6).
                                  # c_pl ne sert NULLE PART ailleurs (v11 3 : retire)."""))

R.append(('Q07 helpers v5 : lecture_5_4, dossier_vierge, arret differe, forme canonique, chargeur au contrat',
"""def prevol_temoin(registre, sortie, mod):""",
'''def lecture_5_4(e_half, p_obs, alpha_f, pc):
    """Gel v11 5.4 : W-plancher = e(dt2/2) >= C(p) x plancher_comp,
    C(p) = 1/(1-2^-tol_ordre(p)) en PLEINE PRECISION, consigne. Sous le
    seuil : W-plancher MORD et l'ordre N'EST PAS LU, ni dans un sens ni
    dans l'autre. CONDITION NECESSAIRE (D-t-25) : au-dessus, le critere
    ne certifie pas seul -- le residuel se lit aux consignations."""
    tol = tol_ordre(alpha_f)
    C_eff = 1.0 / (1.0 - 2.0 ** (-tol))
    seuil = C_eff * pc
    lu = e_half >= seuil
    return {"tol": tol, "C_effectif": C_eff, "seuil": seuil, "lu": lu,
            "ratio_seuil": (e_half / seuil) if seuil > 0 else float("inf"),
            "W_plancher": "PASSE" if lu else "MORD",
            "W_pas": (("PASSE" if abs(p_obs - ORDRE_SCHEMA) <= tol else "MORD")
                      if lu else "NON LU (plancher, 5.4)")}


def dossier_vierge(sortie):
    """D-I-2 : un dossier de sortie est VIDE ou VERSIONNE avant ecriture."""
    if os.path.isdir(sortie) and os.listdir(sortie):
        anc = sortie + ".avant_" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
        os.rename(sortie, anc)
        JRN("D-I-2", "sortie non vide VERSIONNEE : %s -> %s" % (sortie, anc))
    os.makedirs(sortie, exist_ok=True)
    return sortie


def arret_prevol_si_fautes(fautes):
    """D-I-1, seconde moitie : l'arret vient APRES l'ecriture, toujours."""
    if fautes:
        JRN("ARRET", "PREVOL : fautes du factice, APRES ecriture (D-I-1) : %s" % " ; ".join(fautes))
        raise SystemExit(2)


def hash_canonique(o):
    """Contrat chargeur (e69d8a006f584063) : json.dumps(sort_keys=True,
    ensure_ascii=True), separateurs PAR DEFAUT ; sha256, 16 hex."""
    return hashlib.sha256(json.dumps(o, sort_keys=True, ensure_ascii=True).encode()).hexdigest()[:16]


def charger_depot_9bis(chemin, registre):
    """Contrat (a)-(d)+(c') e69d8a006f584063. La piece opposable est le
    DEPOT (son empreinte B au journal) ; comptes ET profondeur se
    RE-DERIVENT de la copie embarquee ; custody contre le registre est
    une MORSURE ; present-mais-illisible = la meme ; absent = NON JOUE
    consigne. Leve RuntimeError('ARRET 9bis : ...') ; main traduit."""
    def arret(m):
        raise RuntimeError("ARRET 9bis : " + m)
    dep = json.load(open(chemin, encoding="utf-8"))
    emp = empreinte_B(chemin)
    perim = tuple(dep["perimetre"]); prof = int(dep["profondeur"]); exe = set(dep["exemptes"])
    ref = dep["reference"]
    fe, conts = [], []
    def marche(o, ch, p):
        if isinstance(o, dict):
            conts.append(p)
            for k in sorted(o):
                marche(o[k], ch + "/" + str(k), p + 1)
        elif isinstance(o, list):
            conts.append(p)
            for i, v in enumerate(o):
                marche(v, "%s[%d]" % (ch, i), p + 1)
        else:
            fe.append((p, ch.rsplit("/", 1)[-1]))
    for c in perim:
        if c not in ref:
            arret("sous-arbre /%s absent de la copie embarquee." % c)
        marche(ref[c], "/" + c, 0)
    nfe = len(fe); nno = nfe + len(conts)
    nex = sum(1 for _, n in fe if (n.split("[", 1)[0] if n.endswith("]") else n) in exe)
    att = dep["comptes"]
    if not (nno == att["noeuds"] and nfe == att["feuilles"] and nex == att["exemptees"]
            and nfe - nex == att["comparees"]):
        arret("comptes non re-derives de la copie : %d/%d/%d/%d contre %s." % (nno, nfe, nex, nfe - nex, att))
    if any(p > prof for p, _ in fe):
        arret("une feuille depasse la profondeur declaree %d." % prof)
    if all(p <= prof - 1 for p, _ in fe):
        arret("profondeur %d non minimale : prof-1 atteint deja toutes les feuilles." % prof)
    r9 = {"reference": ref, "profondeur": prof, "exemptes": exe,
          "nom": "%s (gel %s)" % (dep.get("nom", os.path.basename(chemin)), dep.get("gel", "?")),
          "depot_empreinte": emp, "custody": None}
    rf = dep.get("reference_fichier")
    ch_r = os.path.join(registre, rf) if rf else None
    if ch_r and os.path.isfile(ch_r):
        try:
            reg = json.load(open(ch_r, encoding="utf-8"))
        except Exception as ex:
            arret("reference %s PRESENTE MAIS ILLISIBLE (%s : %s) -- l'absence se constate, elle ne s'improvise pas."
                  % (rf, type(ex).__name__, ex))
        if empreinte_B(ch_r) != dep["reference_empreinte"]:
            arret("empreinte de %s : %s, attendue %s." % (rf, empreinte_B(ch_r), dep["reference_empreinte"]))
        for c in perim:
            he, hr = hash_canonique(ref[c]), hash_canonique(reg.get(c))
            JRN("9bis", "custody /%s : embarquee %s  registre %s" % (c, he, hr))
            if ref[c] != reg.get(c):
                arret("depot et registre divergent (/%s : %s vs %s)." % (c, he, hr))
        r9["custody"] = "JOUE : embarquee == registre 4/4 (fichier %s)" % dep["reference_empreinte"]
    else:
        r9["custody"] = "NON JOUE (reference absente du registre) -- le controle se joue sur la copie embarquee"
        JRN("NE-JOUE-PAS", "9bis custody : " + r9["custody"])
    JRN("9bis", "depot charge %s  empreinte B %s  gel %s  profondeur %d  exemptes %s"
        % (os.path.basename(chemin), emp, dep.get("gel", "?"), prof, sorted(exe)))
    return r9


def prevol_temoin(registre, sortie, mod):'''))

R.append(('Q08 D-I-1 : prevol_temoin ne presume rien -- fautes collectees, verdict consigne',
"""    L = executer_temoin(registre, sortie, mod, prevol=pv)
    assert L["verdict"] == "REGLAGE QUALIFIE", "PREVOL temoin : verdict inattendu %s" % L["verdict"]
    assert L["W_comptes"] == "PASSE"
    return L""",
"""    L = executer_temoin(registre, sortie, mod, prevol=pv)
    fautes = []
    if L["W_comptes"] != "PASSE":
        fautes.append("W-comptes %s (le factice determine les comptes)" % L["W_comptes"])
    JRN("PREVOL", "verdict CONSIGNE, jamais asserte (D-I-1) : %s -- %s" % (L["verdict"], L["branche"]))
    L["prevol_fautes"] = fautes
    return L"""))

R.append(('Q09 D-I-1 : prevol_alpha au meme regime -- son factice determine, mais l\'ecriture passe d\'abord',
"""    L = executer_alpha(registre, sortie, mod, porte, prevol={"synth": SynthAlpha(s_etoile)})
    assert L["verdict"].endswith("VERIFIE"), "PREVOL alpha : verdict inattendu %s" % L["verdict"]
    assert L["G_lignee"]["n_ok"] == 9 and L["G_lignee"]["n"] == 27, "PREVOL alpha : le factice devait tuer les 18 indices"
    assert L["G_comptes"] == "PASSE"
    return L""",
"""    L = executer_alpha(registre, sortie, mod, porte, prevol={"synth": SynthAlpha(s_etoile)})
    fautes = []
    if not L["verdict"].endswith("VERIFIE"):
        fautes.append("verdict %s (SynthAlpha determine VERIFIE)" % L["verdict"])
    if not (L["G_lignee"]["n_ok"] == 9 and L["G_lignee"]["n"] == 27):
        fautes.append("G-lignee %s/%s (le factice devait tuer les 18 indices)" % (L["G_lignee"]["n_ok"], L["G_lignee"]["n"]))
    if L["G_comptes"] != "PASSE":
        fautes.append("G-comptes %s" % L["G_comptes"])
    JRN("PREVOL", "verdict CONSIGNE, fautes assertees APRES ecriture (D-I-1) : %s -- %d faute(s)"
        % (L["verdict"], len(fautes)))
    L["prevol_fautes"] = fautes
    return L"""))

R.append(('Q10 D-I-2 : la sortie de pre-vol est vierge ou versionnee',
"""        sortie = a.sortie or os.path.join("out_prevol", a.mode)""",
"""        sortie = dossier_vierge(a.sortie or os.path.join("out_prevol", a.mode))"""))

R.append(('Q11 D-I-2 : la sortie de run reel aussi',
"""        sortie = a.sortie or os.path.join("out_banc", a.mode)""",
"""        sortie = dossier_vierge(a.sortie or os.path.join("out_banc", a.mode))"""))

R.append(('Q12 D-I-1 : l\'arret de pre-vol tombe APRES resultats, journal et manifest',
"""    ecrire_manifest(sortie)
    JRN("FIN\"""",
"""    ecrire_manifest(sortie)
    if statut == "PREVOL":
        arret_prevol_si_fautes(L.get("prevol_fautes", []))
    JRN("FIN\""""))

R.append(('Q13 chargeur : main consomme le DEPOT au contrat, plus un chemin nu',
"""            ref_9bis = None
            if a.controle_9bis:
                c9 = json.load(open(a.controle_9bis, encoding="utf-8"))
                ch_r = os.path.join(a.registre, c9["reference"])
                if empreinte_B(ch_r) != c9["reference_empreinte"]:
                    sys.exit("ARRET 9bis : la reference %s ne resout pas %s." % (ch_r, c9["reference_empreinte"]))
                ref_9bis = {"reference": json.load(open(ch_r, encoding="utf-8")),
                            "profondeur": int(c9["profondeur"]), "exemptes": set(c9["exemptes"]),
                            "nom": "%s (%s)" % (c9["reference"], c9["reference_empreinte"])}
                JRN("9bis", "controle depose lu : %s" % a.controle_9bis)""",
"""            ref_9bis = None
            if a.controle_9bis:
                try:
                    ref_9bis = charger_depot_9bis(a.controle_9bis, a.registre)
                except RuntimeError as ex:
                    sys.exit(str(ex))"""))

R.append(('Q14 consignation 9bis : le depot et sa custody entrent au JSON',
"""                                  "ecarts": ec[:40], "reference": ref_9bis.get("nom", "?")}""",
"""                                  "ecarts": ec[:40], "reference": ref_9bis.get("nom", "?"),
                                  "depot_empreinte": ref_9bis.get("depot_empreinte"),
                                  "custody": ref_9bis.get("custody")}"""))

R.append(('Q15 critere 5.4 dans T-2 : lecture_5_4 remplace le plancher c_pl',
"""            R_comp = float(np.max((np.abs(ph["x1"]) + np.abs(ph["x2"])) / np.maximum(np.abs(ph["x1"] + ph["x2"]), 1e-300)))
            plancher_composantes = eps * R_comp
            tol_o = tol_ordre(a)""",
"""            R_comp = float(np.max((np.abs(ph["x1"]) + np.abs(ph["x2"])) / np.maximum(np.abs(ph["x1"] + ph["x2"]), 1e-300)))
            plancher_composantes = eps * R_comp
            tol_o = tol_ordre(a)
            lec = lecture_5_4(err["dt2/2"]["e"], p_obs, a, plancher_composantes)"""))

R.append(('Q16 T-2 : W-pas a trois etats -- l\'ordre d\'un point sous le plancher n\'est pas lu',
"""                  "W_pas": "PASSE" if abs(p_obs - ORDRE_SCHEMA) <= tol_o else "MORD",""",
"""                  "W_pas": lec["W_pas"],"""))

R.append(('Q17 T-2 : le plancher du gel v11 remplace c_pl x eps x N ; C effectif et ratio consignes',
"""                  "plancher": plancher, "c_pl_plancher": C_PL * plancher,""",
"""                  "plancher_accum": plancher, "C_effectif": lec["C_effectif"],
                  "seuil_5_4": lec["seuil"], "ratio_seuil": lec["ratio_seuil"],"""))

R.append(('Q18 T-2 : W-plancher est la garde 5.4 (v11 8, ligne 1008)',
"""                  "W_plancher": "PASSE" if err["dt2/2"]["e"] >= C_PL * plancher else "MORD",""",
"""                  "W_plancher": lec["W_plancher"],"""))

R.append(('Q19 T-2 : p_obs d\'un point non lu ne se consigne pas -- ni dans un sens ni dans l\'autre',
"""            R["points"][cle] = pt
            JRN("T2-%s" % cle, "e(dt2)=%.4e (%d pas) e(dt2/2)=%.4e (%d) p_obs=%.4f tol_ordre=%.4f (plafond %.2f) W-pas %s ; plancher c_pl x %.2e W-plancher %s ; e/ln10=%.3e conversion(plafond 2/15) %s"
                % (err["dt2"]["e"], err["dt2"]["n_pas"], err["dt2/2"]["e"], err["dt2/2"]["n_pas"], p_obs, tol_o,
                   PLAFOND_ORDRE, pt["W_pas"], C_PL * plancher, pt["W_plancher"], pt["e_sur_ln10"], pt["conversion_ok"]))""",
"""            if not lec["lu"]:
                pt["p_obs"] = None
            R["points"][cle] = pt
            JRN("T2-%s" % cle, "e(dt2)=%.4e (%d pas) e(dt2/2)=%.4e (%d) p_obs=%s tol_ordre=%.4f (plafond %.2f) W-pas %s ; 5.4 e/seuil=%.3f (C_eff=%.4f) W-plancher %s ; e/ln10=%.3e conversion(plafond 2/15) %s"
                % (err["dt2"]["e"], err["dt2"]["n_pas"], err["dt2/2"]["e"], err["dt2/2"]["n_pas"],
                   ("%.4f" % p_obs) if lec["lu"] else "NON LU", tol_o,
                   PLAFOND_ORDRE, pt["W_pas"], lec["ratio_seuil"], lec["C_effectif"], pt["W_plancher"], pt["e_sur_ln10"], pt["conversion_ok"]))"""))

R.append(('Q20 lectures non lues : chaque point 5.4 ecarte est nomme APRES l\'init de la liste',
"""        L["lectures_non_lues"] = []""",
"""        L["lectures_non_lues"] = []
        for _k in sorted(L["T2"]["points"]):
            if L["T2"]["points"][_k]["W_pas"].startswith("NON LU"):
                L["lectures_non_lues"].append("W-pas %s NON LU (plancher de composition, 5.4)" % _k)"""))

R.append(('Q21 banc : G29-G33 -- chargeur au contrat, ordre D-I-1, 5.4 deux sens',
"""    JRN("BANC", "bilan %d/%d scenarios mordent""",
'''    # -- G29..G31 : le CHARGEUR au contrat (e69d8a006f584063), sur le depot REEL
    ch_dep = os.path.join(REGISTRE_BANC, "journal", "depot_9bis_temoin_v1.json")
    if os.path.isfile(ch_dep):
        r9 = charger_depot_9bis(ch_dep, REGISTRE_BANC)
        ec0 = controle_9bis({c: r9["reference"][c] for c in ("T1", "T1b", "T3a", "T3b")},
                            r9["reference"], r9["profondeur"], r9["exemptes"])
        scenario("G29 chargeur : depot REEL charge, comptes et profondeur RE-DERIVES, custody %s, identite -> 0 ecart"
                 % ("JOUEE" if r9["custody"].startswith("JOUE") else "NON JOUEE"),
                 (not ec0) and r9["depot_empreinte"] == "c4310e33da6b9759",
                 "empreinte %s ; %s" % (r9["depot_empreinte"], r9["custody"][:60]), gardes=())
        dep2 = json.load(open(ch_dep, encoding="utf-8"))
        dep2["reference"]["T1b"]["recherches"]["a"]["seuil"] += 1e-9
        ch2 = os.path.join("/tmp", "depot_9bis_perturbe.json")
        with open(ch2, "w") as f2:
            json.dump(dep2, f2, indent=1); f2.write("\\n")
        try:
            charger_depot_9bis(ch2, REGISTRE_BANC)
            rate30, det30 = False, "aucun arret"
        except RuntimeError as ex30:
            rate30, det30 = ("divergent" in str(ex30)), str(ex30)[:96]
        scenario("G30 chargeur : copie embarquee PERTURBEE d'une feuille -> ARRET 9bis, depot et registre divergent",
                 rate30, det30, gardes=())
        dep3 = json.load(open(ch_dep, encoding="utf-8"))
        dep3["reference_fichier"] = "runs/absent_9bis.json"
        ch3 = os.path.join("/tmp", "depot_9bis_absent.json")
        with open(ch3, "w") as f3:
            json.dump(dep3, f3, indent=1); f3.write("\\n")
        r93 = charger_depot_9bis(ch3, REGISTRE_BANC)
        scenario("G31 chargeur : reference ABSENTE du registre -> custody NON JOUE consigne, le controle se joue quand meme",
                 r93["custody"].startswith("NON JOUE"), r93["custody"], gardes=())
    else:
        scenario("G29 chargeur : depot 9bis ABSENT de journal/ -- les scenarios du contrat ne peuvent pas jouer",
                 False, ch_dep, gardes=())
    # -- G32 : D-I-1, l'ORDRE ecrire-puis-arreter
    d32 = os.path.join("/tmp", "banc_di1")
    os.makedirs(d32, exist_ok=True)
    f32 = os.path.join(d32, "resultats_ordre.json")
    ecrire_ascii(f32, "{}\\n")
    try:
        arret_prevol_si_fautes(["scenario de banc"])
        rate32 = False
    except SystemExit:
        rate32 = os.path.isfile(f32)
    scenario("G32 D-I-1 : l'arret de pre-vol tombe APRES l'ecriture -- la sortie existe quand il tombe",
             rate32, "ordre ecrire-puis-arreter demontre", gardes=())
    # -- G33 : la lecture 5.4, DEUX sens (v11 8 : W-plancher est la garde)
    a33 = float(alpha_de(7)); eps33 = float(np.finfo(float).eps)
    pc33 = eps33 * 2 * a33 * (a33 + 1) / ((1.73 * 1.73 - 1) * tau_cap(1.73) ** 2)
    l_bas = lecture_5_4(0.5 * pc33 * 8.0, 3.99, a33, pc33)
    l_ok = lecture_5_4(2.0 * l_bas["seuil"], 3.99, a33, pc33)
    l_mord = lecture_5_4(2.0 * l_bas["seuil"], 3.40, a33, pc33)
    scenario("G33 5.4 : sous le seuil -> W-plancher MORD et l'ordre NON LU ; au-dessus -> PASSE, puis MORD au p_obs",
             l_bas["W_plancher"] == "MORD" and l_bas["W_pas"].startswith("NON LU")
             and l_ok["W_plancher"] == "PASSE" and l_ok["W_pas"] == "PASSE" and l_mord["W_pas"] == "MORD",
             "C_eff=%.4f seuil=%.3e" % (l_bas["C_effectif"], l_bas["seuil"]), gardes=("W-plancher", "W-pas"))
    JRN("BANC", "bilan %d/%d scenarios mordent'''))

R.append(('Q22 selftest v5 : C(p), lecture_5_4, forme canonique -- asserts durs avant le bilan',
"""    JRN("SELFTEST", "bilan %d/%d" % (n_ok, len(T)))""",
"""    C4v, C5v, C7v = [1.0 / (1.0 - 2.0 ** (-tol_ordre(alpha_de(pv)))) for pv in (4, 5, 7)]
    assert 1.0 < C4v < C5v < C7v < 9.0, "selftest v5 : C(p) ordonnees"
    lv = lecture_5_4(1.0, 4.0, alpha_de(5), 0.01)
    assert lv["W_plancher"] == "PASSE" and abs(lv["C_effectif"] - C5v) < 1e-12
    assert lecture_5_4(0.05, 4.0, alpha_de(5), 0.01)["W_pas"].startswith("NON LU")
    assert hash_canonique({"x": [1, 2]}) == hashlib.sha256(b'{"x": [1, 2]}').hexdigest()[:16], \\
        "selftest v5 : forme canonique = separateurs PAR DEFAUT"
    JRN("SELFTEST", "v5 : C(p) = %.4f / %.4f / %.4f (pleine precision), lecture_5_4 trois branches, forme canonique -- PASSENT"
        % (C4v, C5v, C7v))
    JRN("SELFTEST", "bilan %d/%d" % (n_ok, len(T)))"""))

R.append(('Q23 reglage : c_pl se nomme herite au JSON',
""""q": Q_ECH, "c_T": C_T, "c_pl": C_PL, "c_0": C_0, "k_prime": KP_BASC, "eta_R": str(ETA_R),""",
""""q": Q_ECH, "c_T": C_T, "c_pl_ld16_herite": C_PL, "c_0": C_0, "k_prime": KP_BASC, "eta_R": str(ETA_R),"""))

R.append(('Q24 branche 9bis : la voix du gel passe a la v11',
"""                    "9bis : ecart sur cle du perimetre, prononce AVANT toute lecture de verdict (v9 9bis) -- %s" % ec[0])""",
"""                    "9bis : ecart sur cle du perimetre, prononce AVANT toute lecture de verdict (v11 9bis) -- %s" % ec[0])"""))

# ------------------------------------------------------------------ apply
n = 0
for (lab, old, new) in R:
    c = s.count(old)
    assert c == 1, "ANCRE '%s' : %d occurrence(s)" % (lab, c)
    s = s.replace(old, new)
    n += 1
    print("  ok " + lab)

b = s.encode()
assert all(x < 128 for x in b), "sortie non ASCII"
assert b"\r" not in b, "CR dans la sortie"
open(DST, "wb").write(b)
print()
print("v4 %s  %d o  (PIN)" % (PIN, len(raw)))
print("v5 %s  %d o  (%d remplacements)" % (canon(b), len(b), n))
