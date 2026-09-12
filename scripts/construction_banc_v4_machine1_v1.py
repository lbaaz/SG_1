#!/usr/bin/env python3
# -*- coding: ascii -*-
"""Construit banc_qualification_machine1_v4.py depuis la v3 DEPOSEE
(5fae2a8c94cf8685). Chaque remplacement est ancre et ASSERTE : un ancrage
qui ne trouve pas exactement une occurrence arrete le script. La v3 n'est
jamais editee (PB-1). Sortie ASCII/LF exigee. Redaction MACHINE 1."""
import hashlib, unicodedata, sys

SRC = 'banc_qualification_machine1_v3.py'
DST = 'banc_qualification_machine1_v4.py'

src = open(SRC, encoding='utf-8').read()
canon = lambda s: hashlib.sha256(unicodedata.normalize(
    'NFC', s.replace('\r\n', '\n').replace('\r', '\n')).encode()).hexdigest()[:16]
assert canon(src) == '5fae2a8c94cf8685', 'la v3 lue n est pas la v3 deposee'

R = []

R.append(('P01 titre + bloc version 4',
"""banc_qualification_machine1_v3.py -- L'INSTRUMENT DES DEUX BANCS DE QUALIFICATION
================================================================================
Version 3. Redaction MACHINE 1 -- la main est dans le nom (N-65).
Version 3 = version 2""",
"""banc_qualification_machine1_v4.py -- L'INSTRUMENT DES DEUX VOLETS DU BANC
DE LA CONSTANTE A (delta' = 1/102400)
================================================================================
Version 4. Redaction MACHINE 1 -- la main est dans le nom (N-65).
Version 4 = version 3 (5fae2a8c94cf8685, CERTIFIEE 10d3160eef210015 sous
v7/v5, DEPOSEE a4a907a) + le cahier FIGE par les gels du banc de la
constante A -- gel constante A v4 (011c923203fcdaef, sections 4, 4.9, 5,
7, 8, 10), gel temoin v9 (403488b4f6c319e9, sections 3, 5.2, 8, 9bis) --
et RIEN d'autre :
  - D-M17-51 : les deux en-tetes de section perimes (l.1281, l.1714 de la
    v3) citent desormais les gels qu'ils servent ;
  - D-M17-58 : la garde de signe au pre-vol, table_factice[(p, w2, sgn)]
    == sF, jouee sur la table AVANT le moteur factice ; scenario de banc ;
  - delta := delta' = 1/102400 (gel v4, 3 : DERIVE) ; delta_0 = 1/100
    reste un REPERE (v4 3.2, v9 3) ; TOUTES les grandeurs derivees se
    recalculent par leurs propres formules ; les seuils de bascule 5.3
    (etage 2a) et la phase grossiere de W-bascule restent a delta_0 ;
  - les ETAGES sur-seuil (2a, 2b ; v4 4.2) et sous-seuil (2s, 2b' ancres
    en t depuis T_MAX ; v4 4.7, t_start LU du journal de phase 1, jamais
    recalcule -- R-A-5) ; l'etat complet a CHAQUE depart d'etage,
    empreinte convention B (v4 4.9, exigence NEUVE) ;
  - AUCUN compte d'etage asserte : les comptes se MESURENT et se
    consignent ; toute garde de compte se compare a l'intervalle DERIVE
    (v4 4.6/4.7 au pas nominal, 4.8 pour la jumelle : bornes x 2) ; hors
    intervalle -> G-fen (motif : compte d'etage) ;
  - W-bascule EN VOIE A (v9 8, arbitrage operateur) : g1 la phase
    grossiere du v7 (de k' tau_dom_0 a k tau_dom_0, dt_1), g2 l'etage 2a
    (de k tau_dom_0 a k tau_dom', pas k tau_dom'/M), lecture D-t-19
    ECRITE sur la tolerance 5.3 (iv) ; comptes mesures ;
  - la branche 3b : G-plancher (v4 7) -- tol_lnA(p) <= plancher_lnA(p)
    -> NON CONCLUANT DE PLANCHER ; comparaison de bord exacte par
    propagation du double (v4 7, regle 15) ;
  - le controle de reproductibilite 9bis (v9) : perimetre ENUMERE ET
    CLOS /T1 /T1b /T3a /T3b a profondeur declaree, exemptions duree/
    chemins A L'INTERIEUR, tout le reste hors perimetre PAR CONSTRUCTION ;
    ecart -> NON CONCLUANT D'INSTRUMENT avant toute lecture de verdict ;
  - L-desc (v4 9) : les dix-huit rapports contre la cellule du plan du
    85 (6d7d23130e9322f8), CONSIGNES, portee a un seul sens rappelee ;
  - le banc des gardes s'etend : branche 3b, etage 2a, etage 2s,
    W-bascule voie A (g2 absente casse la remise d'etat), garde
    D-M17-58, n_2s > 620 SANS morsure, 9bis (mord au perimetre, muet
    hors perimetre et sur les exemptes).
  Physique, transcription, ajustements, temoin T-1/T-1b/T-3 : INCHANGES
  (sans delta, v9 2 ; leur rejeu A L'IDENTIQUE est l'objet de 9bis).
Version 3 = version 2""") )

R.append(('P02 ancres E19',
"""ANCRES E19 (ce run n'est opposable que si l'instrument cite ces empreintes
dans une certification croisee anterieure a son depot) :
  gels/temoin_negatif_pre_enregistrement_v7.md   8b083e9f109b5a8e  39750 o  CERTIFIE
    par journal/note_machine1_certification_gels_v7_v4.md  6b2425dbf906205b  6247 o
  gels/alpha_pre_enregistrement_v5.md            045c2435aaf623ce  28998 o  CERTIFIE
    par journal/note_machine1_certification_gel_alpha_v5.md fe43f7c4d142bcdb 3205 o""",
"""ANCRES E19 (ce run n'est opposable que si l'instrument cite ces empreintes
dans une certification croisee anterieure a son depot) :
  gels/constante_A_pre_enregistrement_v4.md      011c923203fcdaef  30988 o  CERTIFIE
    par journal/note_machine2_certification_constante_A_v4_v1.md 9e6376f936708077 11359 o
  gels/temoin_negatif_pre_enregistrement_v9.md   403488b4f6c319e9  57914 o  CERTIFIE
    par journal/note_machine1_certification_temoin_v9_v1.md b5da74783e5f97c6 7085 o
  BASES par citation (les deux gels ci-dessus les citent, PB-1) :
  gels/temoin_negatif_pre_enregistrement_v7.md   8b083e9f109b5a8e  39750 o  CERTIFIE
    par journal/note_machine1_certification_gels_v7_v4.md  6b2425dbf906205b  6247 o
  gels/alpha_pre_enregistrement_v5.md            045c2435aaf623ce  28998 o  CERTIFIE
    par journal/note_machine1_certification_gel_alpha_v5.md fe43f7c4d142bcdb 3205 o""") )

R.append(('P03 VERSION',
'VERSION = "banc_qualification_machine1_v3"',
'VERSION = "banc_qualification_machine1_v4"'))

R.append(('P04 ancres constantes',
"""GEL_TEMOIN = ("gels/temoin_negatif_pre_enregistrement_v7.md", "8b083e9f109b5a8e", 39750)
GEL_ALPHA = ("gels/alpha_pre_enregistrement_v5.md", "045c2435aaf623ce", 28998)
CERT_TEMOIN = ("journal/note_machine1_certification_gels_v7_v4.md", "6b2425dbf906205b")
CERT_ALPHA = ("journal/note_machine1_certification_gel_alpha_v5.md", "fe43f7c4d142bcdb")""",
"""GEL_TEMOIN = ("gels/temoin_negatif_pre_enregistrement_v9.md", "403488b4f6c319e9", 57914)
GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v4.md", "011c923203fcdaef", 30988)
CERT_TEMOIN = ("journal/note_machine1_certification_temoin_v9_v1.md", "b5da74783e5f97c6")
CERT_ALPHA = ("journal/note_machine2_certification_constante_A_v4_v1.md", "9e6376f936708077")
GEL_TEMOIN_BASE = ("gels/temoin_negatif_pre_enregistrement_v7.md", "8b083e9f109b5a8e", 39750)
GEL_ALPHA_BASE = ("gels/alpha_pre_enregistrement_v5.md", "045c2435aaf623ce", 28998)
CERT_TEMOIN_BASE = ("journal/note_machine1_certification_gels_v7_v4.md", "6b2425dbf906205b")
CERT_ALPHA_BASE = ("journal/note_machine1_certification_gel_alpha_v5.md", "fe43f7c4d142bcdb")""") )

R.append(('P05 delta prime',
"""# Gel alpha, section 6 -- les nombres purs, et rien d'autre ne se tape.
DELTA = Fraction(1, 100)""",
"""# Gel constante A v4, sections 3 et 6 -- delta' DERIVE (la derivation est
# le nombre) ; b et m sont les DEUX SEULS purs de conception ; delta_0 est
# un REPERE, pas un reglage (v4 3.2, temoin v9 3).
DELTA = Fraction(1, 102400)
B_DESC, M_MARGE, J_DESC = 4, 2, 5
DELTA_0 = DELTA * B_DESC ** J_DESC          # = 1/100, le delta du 85
# Gel alpha v5, section 6 -- les autres purs, inchanges (v4 6).""") )

R.append(('P06 fonctions primees et intervalles',
"""def x_bascule(p, w2, k=K_BASC):
    return A_de(p) * (k * tau_dom(w2)) ** (-float(alpha_de(p)))
""",
"""def x_bascule(p, w2, k=K_BASC):
    return A_de(p) * (k * tau_dom(w2)) ** (-float(alpha_de(p)))


# -- Reglage prime (gel constante A v4, 4) : tau_dom() ci-dessus est DEJA
#    prime (DELTA = delta') ; les grandeurs du REPERE delta_0 s'ecrivent _0.
def tau_dom_0(w2):
    return math.sqrt(float(DELTA_0) / (1.0 + w2 * w2))


def x_bascule_0(p, w2, k=K_BASC):
    \"\"\"Bascule 5.3 du v5, INCHANGEE (v4 4.2) : le depart de l'etage 2a.\"\"\"
    return A_de(p) * (k * tau_dom_0(w2)) ** (-float(alpha_de(p)))


def dt2a_de(w2):
    \"\"\"Etage 2a : dt <= terminal / M, terminal = k tau_dom' (v4 4.2).\"\"\"
    return K_BASC * tau_dom(w2) / M_PAS


def depart_2s(w2):
    return T_MAX_DEPOSE - K_BASC * tau_dom_0(w2)


def depart_2bp(w2):
    return T_MAX_DEPOSE - K_BASC * tau_dom(w2)


N_2BP = int(Fraction(M_PAS * K_BASC) / R_CAP)      # = 400 EXACT (v4 4.7)
N_FENETRE = int(Fraction(M_PAS) * (1 - R_CAP) / R_CAP)   # = 180 (v4 4.2)


def n_2a_nominal():
    r = Fraction(int(round(math.sqrt(float(DELTA_0 / DELTA)))))
    assert r * r == DELTA_0 / DELTA, "sqrt(delta_0/delta') non entiere"
    return int(M_PAS * (r - 1))                    # = 620 (v4 4.6)


def n_2b_nominal():
    return int(M_PAS * (K_BASC - R_CAP) / R_CAP)   # = 380 (v4 4.6)


RACINE_DESC = int(round(math.sqrt(float(B_DESC ** J_DESC))))   # = 32, PUR
assert Fraction(RACINE_DESC) ** 2 == Fraction(B_DESC) ** J_DESC


def n_2a_nominal_k(k_start):
    \"\"\"Nominal de l'etage 2a quand la bascule 5.3 se joue a k_start
    (G-k : k_start = 4) : M (k_start tau_dom_0 / (k tau_dom') - 1),
    EXACT en Fraction (regle 15 -- jamais ceil d'un pur flottant).\"\"\"
    n = M_PAS * (Fraction(k_start) * RACINE_DESC / K_BASC - 1)
    assert n.denominator == 1
    return int(n)


def retard_2a(w2):
    \"\"\"ceil(dt_1 / dt_2a) : ratio irrationnel, loin de tout bord.\"\"\"
    return int(math.ceil(DT1 / dt2a_de(w2)))


RETARD_2B = int(Fraction(K_BASC) / R_CAP)          # = k/r = 20, PUR (v4 4.6)


def intervalle_evenement(n_nominal, retard, facteur=1):
    \"\"\"v4 4.6 / 4.8 : depart en retard d'au plus UN pas de la grille
    AMONT (retard, en pas de la grille propre), arrivee d'au plus UN pas ;
    n_nominal et retard sont des ENTIERS DERIVES (regle 15) ; jumelle :
    les DEUX bornes x facteur (v4 4.8, jamais recopiees).\"\"\"
    return facteur * (int(n_nominal) - int(retard)), facteur * (int(n_nominal) + 1)


def intervalle_2s(w2, facteur=1):
    \"\"\"v4 4.7 : 620 <= n_2s <= 620 + ceil(dt_1/dt_2a) ; jumelle x2.\"\"\"
    return (facteur * n_2a_nominal(),
            facteur * (n_2a_nominal() + retard_2a(w2)))


def garde_compte(nom, n, lo, hi, rec, etiquette):
    \"\"\"Toute garde de compte se compare a l'intervalle DERIVE (v4 4.6) ;
    hors intervalle -> G-fen, motif : compte d'etage.\"\"\"
    ok = lo <= n <= hi
    rec.setdefault("comptes_etages", {})[nom] = {"n": int(n), "intervalle": [int(lo), int(hi)], "ok": bool(ok)}
    if not ok:
        rec["statut"] = "G-fen (compte %s = %d hors [%d, %d])" % (nom, n, lo, hi)
        rec["ajustement"] = {"statut": "G-fen"}
        JRN("A-%s" % etiquette, "compte d'etage %s = %d HORS intervalle derive [%d, %d] -> G-fen, COMPTE" % (nom, n, lo, hi))
    return ok


def etat_depart_consigne(rec, nom, etat, t):
    \"\"\"v4 4.9 (exigence NEUVE) : l'etat complet a chaque depart d'etage,
    meme forme (t, x1, x2, x1', x2'), empreinte convention B.\"\"\"
    ligne = "%.17g %.17g %.17g %.17g %.17g" % ((t,) + tuple(etat))
    rec.setdefault("departs_etages", {})[nom] = {"t": t, "etat": list(etat), "empreinte": empreinte_B_texte(ligne)}


PERIM_9BIS = ("T1", "T1b", "T3a", "T3b")           # temoin v9, 9bis : ENUMERE ET CLOS
""") )

R.append(('P07 garde D-M17-58',
"""def lire_carte(registre):""",
"""def garde_signe_factice(table, s_etoile, signes):
    \"\"\"D-M17-58 (gel v4, 10 (ii)) : au pre-vol, table_factice[(p, w2, sgn)]
    == sF pour CHAQUE point, au signe joue. Rend la liste des fautes.\"\"\"
    fautes = []
    for p in DEGRES:
        for w2 in W2S:
            sg = signes[(p, w2)]["sgn"]
            cle = (p, "%.2f" % w2, sg)
            if cle not in table or table[cle] != s_etoile[(p, w2)]:
                fautes.append("(%d, %.2f, %+d) : table %r != sF %r"
                              % (p, w2, sg, table.get(cle), s_etoile[(p, w2)]))
    return fautes


def lire_carte(registre):""") )

R.append(('P08 en-tete section temoin (D-M17-51)',
'# 8. LE TEMOIN NEGATIF CLASSIQUE (gel 0905a9b78ba40349)',
'# 8. LE TEMOIN NEGATIF CLASSIQUE (gel temoin v9 403488b4f6c319e9, base v7 8b083e9f109b5a8e)'))

R.append(('P09 en-tete section alpha (D-M17-51)',
'# 9. LA VERIFICATION alpha (gel 35a70834b2a34514)',
'# 9. LA VERIFICATION alpha (gel constante A v4 011c923203fcdaef, base alpha v5 045c2435aaf623ce)'))

R.append(('P10 W-bascule voie A',
"""            etat_b = vers_composantes(*xm_et_derivees(p, KP_BASC * td), w2)
            phb1 = phase2_pu(w2, p, etat_b, -KP_BASC * td, DT1, forcage=f, tau_star=0.0,
                             arret_cap=x_bascule(p, w2), t_max=1e9)
            n_b = int(phb1["n"])
            t_b = float(phb1["t"][-1]); tau_b = -t_b
            xb_num = float(phb1["x1"][-1] + phb1["x2"][-1])
            phb2 = phase2_pu(w2, p, phb1["etat_fin"], t_b, dt2, forcage=f, tau_star=0.0, tau_fin=tc)""",
"""            # W-bascule EN VOIE A (v9, 8) : g1 = la phase grossiere du v7,
            # de k' tau_dom_0 a k tau_dom_0, au pas dt_1 ; g2 = l'etage 2a,
            # de k tau_dom_0 a k tau_dom', au pas k tau_dom'/M. Comptes
            # MESURES, jamais assertes (v9 8, D-t-21).
            td0 = tau_dom_0(w2)
            etat_b = vers_composantes(*xm_et_derivees(p, KP_BASC * td0), w2)
            phg1 = phase2_pu(w2, p, etat_b, -KP_BASC * td0, DT1, forcage=f, tau_star=0.0,
                             arret_cap=x_bascule_0(p, w2), t_max=1e9)
            n_g1 = int(phg1["n"])
            phg2 = phase2_pu(w2, p, phg1["etat_fin"], float(phg1["t"][-1]), dt2a_de(w2),
                             forcage=f, tau_star=0.0, arret_cap=x_bascule(p, w2), t_max=1e9)
            n_g2 = int(phg2["n"])
            lo_g2, hi_g2 = intervalle_evenement(n_2a_nominal(), retard_2a(w2))
            phb1 = phg2
            n_b = n_g2
            t_b = float(phb1["t"][-1]); tau_b = -t_b
            xb_num = float(phb1["x1"][-1] + phb1["x2"][-1])
            phb2 = phase2_pu(w2, p, phb1["etat_fin"], t_b, dt2, forcage=f, tau_star=0.0, tau_fin=tc)""") )

R.append(('P11 W-bascule consignation',
"""                  "bascule": {"n_pas_phase1": n_b, "tau_b": tau_b, "x_b_num": xb_num,
                              "err_rel_bascule": abs(xb_num - A * tau_b ** (-a)) / (A * tau_b ** (-a)),
                              "e_avec": e_avec, "e_avec_sur_e_sans": e_avec / err["dt2"]["e"],
                              "n_pas_phase2": int(phb2["n"])},
                  "W_bascule": "PASSE" if e_avec <= float(PLAFOND_ALPHA) * LN10 else "MORD"}""",
"""                  "bascule": {"n_g1": n_g1, "n_g2": n_g2,
                              "intervalle_g2": [int(lo_g2), int(hi_g2)],
                              "g2_dans_intervalle": bool(lo_g2 <= n_g2 <= hi_g2),
                              "tau_b": tau_b, "x_b_num": xb_num,
                              "err_rel_bascule": abs(xb_num - A * tau_b ** (-a)) / (A * tau_b ** (-a)),
                              "e_avec": e_avec, "e_avec_sur_e_sans": e_avec / err["dt2"]["e"],
                              "n_pas_phase2": int(phb2["n"])},
                  "W_bascule": "PASSE" if (e_avec <= float(PLAFOND_ALPHA) * LN10 and lo_g2 <= n_g2 <= hi_g2) else "MORD"}""") )

R.append(('P12 W-bascule journal',
"""            JRN("Wb-%s" % cle, "phase grossiere depuis tau=%.4e (k'=%d) : %d pas de dt1, bascule a tau_b=%.4e (err %.2e), e_avec(dt2)=%.4e (x%.1f de e_sans) W-bascule %s"
                % (KP_BASC * td, KP_BASC, n_b, tau_b, pt["bascule"]["err_rel_bascule"], e_avec,
                   pt["bascule"]["e_avec_sur_e_sans"], pt["W_bascule"]))""",
"""            JRN("Wb-%s" % cle, "VOIE A : g1 %d pas de dt1 (depuis tau=%.4e, k'=%d) ; g2 %d pas de dt_2a (intervalle [%d,%d] %s) ; bascule 2b a tau_b=%.4e (err %.2e) ; e_avec(dt2)=%.4e (x%.1f de e_sans, lecture D-t-19) W-bascule %s"
                % (n_g1, KP_BASC * td0, KP_BASC, n_g2, lo_g2, hi_g2,
                   "OK" if pt["bascule"]["g2_dans_intervalle"] else "HORS", tau_b,
                   pt["bascule"]["err_rel_bascule"], e_avec,
                   pt["bascule"]["e_avec_sur_e_sans"], pt["W_bascule"]))""") )

R.append(('P13 trajectoire_plan : etages 2a/2b',
"""    xb = x_bascule(p, w2, k)
    ph1 = (mod_synth or phase1_pu)(w2, s, p, "bascule", x_b=xb, sgn=sgn)""",
"""    xb = x_bascule_0(p, w2, k)                 # bascule 5.3 du v5, INCHANGEE (v4 4.2)
    ph1 = (mod_synth or phase1_pu)(w2, s, p, "bascule", x_b=xb, sgn=sgn)""") )

R.append(('P14 trajectoire_plan : signature jumelle',
'def trajectoire_plan(w2, p, s, dt2, k, compteur, sortie, etiquette, mod_synth=None, sgn=1):',
'def trajectoire_plan(w2, p, s, dt2, k, compteur, sortie, etiquette, mod_synth=None, sgn=1, jumelle=False, sans_2a=False):'))

R.append(('P15 trajectoire_plan : chaine des etages',
"""    ph2 = (mod_synth.phase2 if mod_synth else phase2_pu)(w2, p, ph1["etat"], ph1["t"], dt2, arret_cap=cap_p(p, w2), sgn=sgn)
    x = ph2["x1"] + ph2["x2"]""",
"""    fac = 2 if jumelle else 1
    if mod_synth:
        # Synthetique (banc, pre-vol) : la chaine est jouee en UNE phase par
        # la fabrique ; les gardes de compte d'etage sont NON JOUEES ici et
        # le journal le dit (N-62 : rien de synthetique n'est une mesure).
        rec["etages"] = "SYNTHETIQUE (une phase ; gardes de compte NON JOUEES)"
        ph2 = mod_synth.phase2(w2, p, ph1["etat"], ph1["t"], dt2, arret_cap=cap_p(p, w2), sgn=sgn)
    else:
        etat_depart_consigne(rec, "2a", ph1["etat"], ph1["t"])
        dt_2a = dt2a_de(w2) / fac
        if sans_2a:
            ph2a = {"evenement": "SAUTE", "n": 0, "etat_fin": ph1["etat"], "t": np.array([ph1["t"]])}
        else:
            ph2a = phase2_pu(w2, p, ph1["etat"], ph1["t"], dt_2a, arret_cap=x_bascule(p, w2, K_BASC), sgn=sgn)
        lo, hi = intervalle_evenement(n_2a_nominal_k(k), retard_2a(w2), fac)
        rec["etage_2a"] = {"evenement": ph2a["evenement"], "n": int(ph2a["n"]), "dt": dt_2a}
        if not garde_compte("n_2a", ph2a["n"], lo, hi, rec, etiquette):
            return rec
        if ph2a["evenement"] not in ("CAP", "SAUTE"):
            rec["statut"] = "G-fen (etage 2a : %s)" % ph2a["evenement"]
            rec["ajustement"] = {"statut": "G-fen"}
            JRN("A-%s" % etiquette, "etage 2a n'atteint pas la bascule 2b (%s) -> G-fen, COMPTE" % ph2a["evenement"])
            return rec
        t_2b = float(ph2a["t"][-1]) if ph2a["evenement"] != "SAUTE" else ph1["t"]
        etat_depart_consigne(rec, "2b", ph2a["etat_fin"], t_2b)
        ph2 = phase2_pu(w2, p, ph2a["etat_fin"], t_2b, dt2, arret_cap=cap_p(p, w2), sgn=sgn)
        lo_b, hi_b = intervalle_evenement(n_2b_nominal(), RETARD_2B, fac)
        rec["etage_2b"] = {"evenement": ph2["evenement"], "n": int(ph2["n"]), "dt": dt2}
        if not garde_compte("n_2b", ph2["n"], lo_b, hi_b, rec, etiquette):
            return rec
    x = ph2["x1"] + ph2["x2"]""") )

R.append(('P16 trajectoire_seuil : signature',
'def trajectoire_seuil(w2, p, s, dt2, compteur, sortie, etiquette, mod_synth=None, sgn=1):',
'def trajectoire_seuil(w2, p, s, dt2, compteur, sortie, etiquette, mod_synth=None, sgn=1, jumelle=False, sans_2s=False):'))

R.append(('P17 trajectoire_seuil : etages 2s/2bprime',
"""    td, tc = tau_dom(w2), tau_cap(w2)
    t_fin = T_MAX_DEPOSE - (td - tc)
    ph1 = (mod_synth or phase1_pu)(w2, s, p, "seuil", x_b=x_bascule(p, w2), t_fin=t_fin, sgn=sgn)""",
"""    td, tc = tau_dom(w2), tau_cap(w2)
    t_fin = depart_2s(w2)                      # v4 4.7 : la borne v5 5.3, en t
    ph1 = (mod_synth or phase1_pu)(w2, s, p, "seuil", x_b=x_bascule_0(p, w2), t_fin=t_fin, sgn=sgn)""") )

R.append(('P18 trajectoire_seuil : chaine 2s/2bprime',
"""    ph2 = (mod_synth.phase2 if mod_synth else phase2_pu)(w2, p, ph1["etat"], ph1["t"], dt2, t_max=T_MAX_DEPOSE, sgn=sgn)
    x = ph2["x1"] + ph2["x2"]""",
"""    fac = 2 if jumelle else 1
    if mod_synth:
        rec["etages"] = "SYNTHETIQUE (une phase ; gardes de compte NON JOUEES)"
        ph2 = mod_synth.phase2(w2, p, ph1["etat"], ph1["t"], dt2, t_max=T_MAX_DEPOSE, sgn=sgn)
    else:
        # v4 4.7 : t_start est LU du journal de phase 1 (l'etat et son t tels
        # que la phase 1 les rend), JAMAIS recalcule (R-A-5).
        t_start = ph1["t"]
        etat_depart_consigne(rec, "2s", ph1["etat"], t_start)
        d2b = depart_2bp(w2)
        dt_2a = dt2a_de(w2) / fac
        if sans_2s:
            ph2s = {"evenement": "SAUTE", "n": 0, "etat_fin": ph1["etat"], "t": np.array([t_start])}
            t_2b = t_start
        else:
            n_2s = int(math.ceil((d2b - t_start) / dt_2a))
            dt_2s = (d2b - t_start) / n_2s      # atterrit EXACTEMENT sur depart_2b'
            ph2s = phase2_pu(w2, p, ph1["etat"], t_start, dt_2s, t_max=d2b, sgn=sgn)
            lo, hi = intervalle_2s(w2, fac)
            rec["etage_2s"] = {"evenement": ph2s["evenement"], "n": int(ph2s["n"]), "dt": dt_2s, "n_2s_derive": n_2s}
            if not garde_compte("n_2s", ph2s["n"], lo, hi, rec, etiquette):
                return rec
            t_2b = float(ph2s["t"][-1])
        etat_depart_consigne(rec, "2b'", ph2s["etat_fin"], t_2b)
        dt_2bp = (T_MAX_DEPOSE - t_2b) / (N_2BP * fac) if not sans_2s else dt2
        ph2 = phase2_pu(w2, p, ph2s["etat_fin"], t_2b, dt_2bp, t_max=T_MAX_DEPOSE, sgn=sgn)
        if not sans_2s:
            rec["etage_2bp"] = {"evenement": ph2["evenement"], "n": int(ph2["n"]), "dt": dt_2bp}
            if not garde_compte("n_2b'", ph2["n"], N_2BP * fac, N_2BP * fac, rec, etiquette):
                return rec
            dt2 = dt_2bp                        # la fenetre se lit au pas de 2b'
    x = ph2["x1"] + ph2["x2"]""") )

R.append(('P19 lire_alpha : signature',
'def lire_alpha(plan, gdt, gk, seuil, lignee, e_ln10_max):',
'def lire_alpha(plan, gdt, gk, seuil, lignee, e_ln10_max, ref_desc=None):'))

R.append(('P20 lire_alpha : G-plancher et L-desc',
"""            D["tol_lnA_sur_plancher"] = D["tol_lnA"] / D["plancher_lnA"]""",
"""            D["tol_lnA_sur_plancher"] = D["tol_lnA"] / D["plancher_lnA"]
            # v4 7, branche 3b : comparaison de bord EXACTE par propagation
            # du double (max() rend l'objet ; regle 15, ecrite au gel).
            D["G_plancher_mord"] = D["tol_lnA"] <= D["plancher_lnA"]""") )

R.append(('P21 lire_alpha : L-desc apres ratios',
"""            D["gA_sur_K"] = ratios
            D["P_A"] = all(abs(math.log(v)) <= (p - 2) * D["tol_lnA"] for v in ratios.values())""",
"""            D["gA_sur_K"] = ratios
            D["P_A"] = all(abs(math.log(v)) <= (p - 2) * D["tol_lnA"] for v in ratios.values())
            if ref_desc and str(p) in ref_desc:
                # v4 9, L-desc : R = ln(gA'/K) / ln(gA_85/K), cellule du plan
                # des deux cotes ; CONSIGNEE, aucune branche. Portee : refute
                # R ~ 1, ne peut pas confirmer 1/1024 (v4 9).
                D["L_desc"] = {cle: math.log(ratios[cle]) / math.log(ref_desc[str(p)][cle])
                               for cle in ratios if cle in ref_desc[str(p)] and ref_desc[str(p)][cle] > 0}
                D["L_desc_portee"] = "un seul sens (v4 9) : refute R~1, ne confirme pas 1/1024"
            elif ref_desc is not None:
                L["lectures_non_lues"].append("L-desc p=%d NON LUE (degre absent de la reference)" % p)""") )

R.append(('P22 lire_alpha : defauts non exploitables',
"""            D.update({"tol": None, "resolution_ok": True, "G_dt_mord": False, "G_k_mord": False, "P_alpha": False,
                      "P_A": False, "G_s_mord": False, "G_w2_mord": False, "tol_lnA": None})""",
"""            D.update({"tol": None, "resolution_ok": True, "G_dt_mord": False, "G_k_mord": False, "P_alpha": False,
                      "P_A": False, "G_s_mord": False, "G_w2_mord": False, "tol_lnA": None, "G_plancher_mord": False})""") )

R.append(('P23 cascade : branche 3b',
"""    if any(deg[p]["G_s_mord"] or deg[p]["G_w2_mord"] for p in deg):""",
"""    if any(deg[p].get("G_plancher_mord") for p in deg):
        qui = [p for p in deg if deg[p].get("G_plancher_mord")]
        return prefixe + "NON CONCLUANT DE PLANCHER", "branche 3b : G-plancher MORD aux degres %s (tol_lnA <= plancher : le modele fixe encore la tolerance ; v4 7)" % qui
    if any(deg[p]["G_s_mord"] or deg[p]["G_w2_mord"] for p in deg):""") )

R.append(('P24 executer_alpha : reference L-desc',
"""    L.update(lire_alpha(plan, gdt, gk, seuil, lignee, porte["e_sur_ln10_max"]))""",
"""    ref_desc = None
    ch_ref = os.path.join(registre, "runs", "run_alpha_delta85", "resultats_alpha.json")
    if os.path.isfile(ch_ref):
        if empreinte_B(ch_ref) == "6d7d23130e9322f8":
            dref = json.load(open(ch_ref, encoding="utf-8"))
            ref_desc = {p: dref["degres"][p]["gA_sur_K"] for p in dref.get("degres", {})}
            JRN("L-desc", "reference du 85 lue (6d7d23130e9322f8) : dix-huit denominateurs, cellule du plan")
        else:
            JRN("L-desc", "reference presente mais DISCORDANTE (%s) : L-desc NON LUE" % empreinte_B(ch_ref))
    else:
        JRN("L-desc", "reference du 85 absente du registre : L-desc NON LUE")
    L.update(lire_alpha(plan, gdt, gk, seuil, lignee, porte["e_sur_ln10_max"], ref_desc=ref_desc))
    if ref_desc is None:
        L["lectures_non_lues"] = L.get("lectures_non_lues", []) + ["L-desc NON LUE (reference du 85 absente ou discordante)"]""") )

R.append(('P25 controle 9bis (fonction)',
"""def executer_temoin(registre, sortie, mod, prevol=None):""",
"""def controle_9bis(L, reference, profondeur, exemptes):
    \"\"\"Temoin v9, 9bis : les QUATRE sous-arbres de RESULTAT (/T1, /T1b,
    /T3a, /T3b) se comparent au run 85 par ENUMERATION a PROFONDEUR
    DECLAREE ; exemptions duree/chemins A L'INTERIEUR ; tout le reste
    HORS PERIMETRE PAR CONSTRUCTION. Rend la liste des ecarts.\"\"\"
    ecarts = []

    def marche(a, b, chemin, prof):
        if prof > profondeur:
            return
        if isinstance(a, dict) and isinstance(b, dict):
            for k in sorted(set(a) | set(b)):
                if str(k) in exemptes:
                    continue
                if k not in a or k not in b:
                    ecarts.append("%s/%s (cle absente d'un cote)" % (chemin, k))
                else:
                    marche(a[k], b[k], "%s/%s" % (chemin, k), prof + 1)
            return
        if isinstance(a, list) and isinstance(b, list):
            if len(a) != len(b):
                ecarts.append("%s (longueurs %d != %d)" % (chemin, len(a), len(b)))
                return
            for i, (va, vb) in enumerate(zip(a, b)):
                marche(va, vb, "%s[%d]" % (chemin, i), prof + 1)
            return
        if a != b:
            ecarts.append("%s (%r != %r)" % (chemin, a, b))
    for cle in PERIM_9BIS:
        marche(L.get(cle), reference.get(cle), "/" + cle, 0)
    return ecarts


def executer_temoin(registre, sortie, mod, prevol=None, ref_9bis=None):""") )

R.append(('P26 executer_temoin : jouer 9bis',
"""        L["verdict"], L["branche"] = cascade_temoin(L)
    L["comptes"] = dict(compteur); L["attendus"] = attendu; L["attendus_total"] = n_att""",
"""        if ref_9bis is not None:
            ec = controle_9bis(L, ref_9bis["reference"], ref_9bis["profondeur"], ref_9bis["exemptes"])
            L["controle_9bis"] = {"perimetre": list(PERIM_9BIS), "profondeur": ref_9bis["profondeur"],
                                  "exemptes": sorted(ref_9bis["exemptes"]), "n_ecarts": len(ec),
                                  "ecarts": ec[:40], "reference": ref_9bis.get("nom", "?")}
            JRN("9bis", "perimetre %s a profondeur %d, exemptes %s : %d ecart(s)"
                % ("/".join(PERIM_9BIS), ref_9bis["profondeur"], sorted(ref_9bis["exemptes"]), len(ec)))
            if ec:
                L["verdict"], L["branche"] = ("NON CONCLUANT D'INSTRUMENT",
                    "9bis : ecart sur cle du perimetre, prononce AVANT toute lecture de verdict (v9 9bis) -- %s" % ec[0])
            else:
                L["verdict"], L["branche"] = cascade_temoin(L)
        else:
            L["lectures_non_lues"].append("controle 9bis NON JOUE (pas de reference deposee)")
            L["verdict"], L["branche"] = cascade_temoin(L)
    L["comptes"] = dict(compteur); L["attendus"] = attendu; L["attendus_total"] = n_att""") )

R.append(('P27 main : arguments',
"""    ap.add_argument("--porte-temoin", default=None, help="resultats_temoin.json du run REEL du temoin (mode alpha)")""",
"""    ap.add_argument("--porte-temoin", default=None, help="resultats_temoin.json du run REEL du temoin (mode alpha)")
    ap.add_argument("--controle-9bis", default=None, help="JSON depose AVANT le run (N-70) : {reference, profondeur, exemptes} pour le controle de reproductibilite (mode temoin)")""") )

R.append(('P28 main : garde D-M17-58 au pre-vol',
"""                if S["sM"] is not None:                                          # et l'autre branche, si la carte la porte
                    table[(p, "%.2f" % w2, -S["sgn"])] = max(float(S["sP"]), float(S["sM"]))
        mod = charger_moteur(a.registre, factice=fabriquer_factice(table))""",
"""                if S["sM"] is not None:                                          # et l'autre branche, si la carte la porte
                    table[(p, "%.2f" % w2, -S["sgn"])] = max(float(S["sP"]), float(S["sM"]))
        fautes_58 = garde_signe_factice(table, s_etoile, signes)
        JRN("D-M17-58", "garde de signe au pre-vol : table_factice[(p, w2, sgn)] == sF, 9 points -> %s"
            % ("PASSE" if not fautes_58 else "MORD : %s" % fautes_58))
        if fautes_58:
            sys.exit("ARRET D-M17-58 : la table factice ne porte pas sF au signe joue (%s)." % fautes_58)
        mod = charger_moteur(a.registre, factice=fabriquer_factice(table))""") )

R.append(('P29 main : 9bis au run temoin reel',
"""        if a.mode == "temoin":
            L = executer_temoin(a.registre, sortie, mod)""",
"""        if a.mode == "temoin":
            ref_9bis = None
            if a.controle_9bis:
                c9 = json.load(open(a.controle_9bis, encoding="utf-8"))
                ch_r = os.path.join(a.registre, c9["reference"])
                if empreinte_B(ch_r) != c9["reference_empreinte"]:
                    sys.exit("ARRET 9bis : la reference %s ne resout pas %s." % (ch_r, c9["reference_empreinte"]))
                ref_9bis = {"reference": json.load(open(ch_r, encoding="utf-8")),
                            "profondeur": int(c9["profondeur"]), "exemptes": set(c9["exemptes"]),
                            "nom": "%s (%s)" % (c9["reference"], c9["reference_empreinte"])}
                JRN("9bis", "controle depose lu : %s" % a.controle_9bis)
            else:
                JRN("9bis", "aucun --controle-9bis : le controle sera NON JOUE (a deposer avec la prediction, N-70)")
            L = executer_temoin(a.registre, sortie, mod, ref_9bis=ref_9bis)""") )

R.append(('P30 tables du gel (selftest)',
"""TABLES_GEL_ALPHA = {   # gel alpha 5.3 (bascule), 5.4 (CAP_p, dt_2), 6 (tau_dom), imprimees a 5 chiffres
    "tau_dom": {1.73: "5.0044e-02", 2.27: "4.0314e-02", 2.80: "3.3634e-02"},
    "dt2": {1.73: "2.5022e-04", 2.27: "2.0157e-04", 2.80: "1.6817e-04"},
    "CAP": {(4, 1.73): "1.9561e+06", (4, 2.27): "3.0143e+06", (4, 2.80): "4.3307e+06",
            (5, 1.73): "1.1274e+04", (5, 2.27): "1.5041e+04", (5, 2.80): "1.9151e+04",
            (7, 1.73): "2.1766e+02", (7, 2.27): "2.5876e+02", (7, 2.80): "2.9912e+02"},
    "bascule": {(4, 1.73): "4.8903e+03", (4, 2.27): "7.5357e+03", (4, 2.80): "1.0827e+04",
                (5, 1.73): "2.0767e+02", (5, 2.27): "2.7705e+02", (5, 2.80): "3.5276e+02",
                (7, 1.73): "1.9813e+01", (7, 2.27): "2.3555e+01", (7, 2.80): "2.7229e+01"},
    "A": {4: "48.98979", 5: "9.65048", 7: "3.14244"},
}""",
"""TABLES_GEL_ALPHA = {   # gel constante A v4, 4.3 (tau_dom', dt_2b), 4.4 (bascule 2b), 4.5 (CAP')
    "tau_dom": {1.73: "1.5639e-03", 2.27: "1.2598e-03", 2.80: "1.0511e-03"},
    "dt2": {1.73: "7.8194e-06", 2.27: "6.2991e-06", 2.80: "5.2553e-06"},
    "dt2a": {1.73: "1.5639e-04", 2.27: "1.2598e-04", 2.80: "1.0511e-04"},
    "CAP": {(4, 1.73): "2.0031e+09", (4, 2.27): "3.0866e+09", (4, 2.80): "4.4346e+09",
            (5, 1.73): "1.1454e+06", (5, 2.27): "1.5280e+06", (5, 2.80): "1.9456e+06",
            (7, 1.73): "3.4826e+03", (7, 2.27): "4.1402e+03", (7, 2.80): "4.7859e+03"},
    "bascule": {(4, 1.73): "5.0077e+06", (4, 2.27): "7.7166e+06", (4, 2.80): "1.1087e+07",
                (5, 1.73): "2.1098e+04", (5, 2.27): "2.8147e+04", (5, 2.80): "3.5838e+04",
                (7, 1.73): "3.1701e+02", (7, 2.27): "3.7687e+02", (7, 2.80): "4.3566e+02"},
    "A": {4: "48.98979", 5: "9.65048", 7: "3.14244"},
}
TABLES_GEL_ALPHA_0 = {   # REPERE delta_0 (gel alpha v5, 5.3 et 6) : bascule 5.3 = depart de 2a
    "tau_dom_0": {1.73: "5.0044e-02", 2.27: "4.0314e-02", 2.80: "3.3634e-02"},
    "bascule_0": {(4, 1.73): "4.8903e+03", (4, 2.27): "7.5357e+03", (4, 2.80): "1.0827e+04",
                  (5, 1.73): "2.0767e+02", (5, 2.27): "2.7705e+02", (5, 2.80): "3.5276e+02",
                  (7, 1.73): "1.9813e+01", (7, 2.27): "2.3555e+01", (7, 2.80): "2.7229e+01"},
}""") )

R.append(('P31 selftest : lignes primees',
"""    for w2 in W2S:
        test("tau_dom(%.2f) = %s" % (w2, TABLES_GEL_ALPHA["tau_dom"][w2]), "%.4e" % tau_dom(w2) == TABLES_GEL_ALPHA["tau_dom"][w2])
        test("dt_2(%.2f) = %s" % (w2, TABLES_GEL_ALPHA["dt2"][w2]), "%.4e" % dt2_de(w2) == TABLES_GEL_ALPHA["dt2"][w2])""",
"""    test("delta' = 1/102400 et delta_0 = b^J delta' = 1/100 (EXACT, v4 3)",
         DELTA == Fraction(1, 102400) and DELTA_0 == Fraction(1, 100) and DELTA_0 == DELTA * B_DESC ** J_DESC)
    for p, att in ((4, Fraction(1, 2048000)), (5, Fraction(9, 13312000)), (7, Fraction(1, 1089536))):
        test("plancher'(%d) = %s exact (v4 3.3)" % (p, att), plancher_lnA(p) == att, str(plancher_lnA(p)))
    test("n_2b' = M k / r = 400 ; fenetre = 180 ; nominaux 620 / 380 (derives, v4 4.6-4.7)",
         N_2BP == 400 and N_FENETRE == 180 and n_2a_nominal() == 620 and n_2b_nominal() == 380)
    test("intervalles 4.6 : n_2a [581,621]/[572,621]/[562,621] ; n_2b [360,381] (derives, entiers)",
         [intervalle_evenement(n_2a_nominal(), retard_2a(w)) for w in W2S]
         == [(581, 621), (572, 621), (562, 621)]
         and intervalle_evenement(n_2b_nominal(), RETARD_2B) == (360, 381)
         and n_2a_nominal_k(K_GARDE) == 1260)
    test("intervalles 4.7 : n_2s [620,659]/[620,668]/[620,678] ; jumelle 4.8 : bornes x2",
         [intervalle_2s(w) for w in W2S] == [(620, 659), (620, 668), (620, 678)]
         and [intervalle_2s(w, 2) for w in W2S] == [(1240, 1318), (1240, 1336), (1240, 1356)]
         and intervalle_evenement(n_2a_nominal(), retard_2a(1.73), 2) == (1162, 1242)
         and intervalle_evenement(n_2b_nominal(), RETARD_2B, 2) == (720, 762))
    for w2 in W2S:
        test("tau_dom'(%.2f) = %s (v4 4.3)" % (w2, TABLES_GEL_ALPHA["tau_dom"][w2]), "%.4e" % tau_dom(w2) == TABLES_GEL_ALPHA["tau_dom"][w2])
        test("dt_2b(%.2f) = %s (v4 4.3)" % (w2, TABLES_GEL_ALPHA["dt2"][w2]), "%.4e" % dt2_de(w2) == TABLES_GEL_ALPHA["dt2"][w2])
        test("dt_2a(%.2f) = %s (v4 4.3)" % (w2, TABLES_GEL_ALPHA["dt2a"][w2]), "%.4e" % dt2a_de(w2) == TABLES_GEL_ALPHA["dt2a"][w2])
        test("tau_dom_0(%.2f) = %s (repere, v5 6)" % (w2, TABLES_GEL_ALPHA_0["tau_dom_0"][w2]), "%.4e" % tau_dom_0(w2) == TABLES_GEL_ALPHA_0["tau_dom_0"][w2])""") )

R.append(('P32 selftest : bascule_0 + 9bis + L-desc + 58',
"""            test("CAP_%d(%.2f) = %s" % (p, w2, TABLES_GEL_ALPHA["CAP"][(p, w2)]), "%.4e" % cap_p(p, w2) == TABLES_GEL_ALPHA["CAP"][(p, w2)])
            test("bascule_%d(%.2f) = %s" % (p, w2, TABLES_GEL_ALPHA["bascule"][(p, w2)]), "%.4e" % x_bascule(p, w2) == TABLES_GEL_ALPHA["bascule"][(p, w2)])
    for p, att in ((4, Fraction(1, 2000)), (5, Fraction(9, 13000)), (7, Fraction(1, 1064))):
        test("plancher_lnA(%d) = %s exact (gel alpha v5, 10.3)" % (p, att), plancher_lnA(p) == att, str(plancher_lnA(p)))""",
"""            test("CAP'_%d(%.2f) = %s (v4 4.5)" % (p, w2, TABLES_GEL_ALPHA["CAP"][(p, w2)]), "%.4e" % cap_p(p, w2) == TABLES_GEL_ALPHA["CAP"][(p, w2)])
            test("bascule2b_%d(%.2f) = %s (v4 4.4)" % (p, w2, TABLES_GEL_ALPHA["bascule"][(p, w2)]), "%.4e" % x_bascule(p, w2) == TABLES_GEL_ALPHA["bascule"][(p, w2)])
            test("bascule0_%d(%.2f) = %s (v5 5.3, depart 2a)" % (p, w2, TABLES_GEL_ALPHA_0["bascule_0"][(p, w2)]), "%.4e" % x_bascule_0(p, w2) == TABLES_GEL_ALPHA_0["bascule_0"][(p, w2)])
    ref9 = {"T1": {"A": {"x": 1.0, "duree_s": 3.0}}, "T1b": {"k": [0, 0]}, "T3a": {"A": "PASSE"}, "T3b": {"n": 3},
            "meta": {"date_utc": "X"}, "reglage": {"delta": "1/102400"}}
    autre = json.loads(json.dumps(ref9)); autre["T1"]["A"]["x"] = 2.0; autre["T1"]["A"]["duree_s"] = 9.0
    autre["meta"]["date_utc"] = "Y"
    ec1 = controle_9bis(autre, ref9, 3, {"duree_s"})
    ec2 = controle_9bis(json.loads(json.dumps(ref9)), ref9, 3, {"duree_s"})
    test("9bis : mord au perimetre (x), muet sur exempte (duree_s) et hors perimetre (meta)",
         len(ec1) == 1 and "/T1/A/x" in ec1[0] and ec2 == [], str(ec1))
    test("L-desc : ln(r')/ln(r) = 1/1024 sur un couple fabrique",
         abs(math.log(math.exp(2e-4 / 1024)) / math.log(math.exp(2e-4)) - 1.0 / 1024) < 1e-12)
    S58 = lire_signes(registre); se58, _ = lire_carte(registre)
    t58 = {(p, "%.2f" % w2, S58[(p, w2)]["sgn"]): se58[(p, w2)] for p in DEGRES for w2 in W2S}
    test("D-M17-58 : la table conforme PASSE la garde (0 faute)", garde_signe_factice(t58, se58, S58) == [])
    for p, att in ((4, Fraction(1, 2048000)), (5, Fraction(9, 13312000)), (7, Fraction(1, 1089536))):
        test("plancher_lnA(%d) = %s exact (v4 3.3, delta')" % (p, att), plancher_lnA(p) == att, str(plancher_lnA(p)))""") )

R.append(('P33 prevol_alpha : bruit et porte au reglage prime',
"""    porte = {"fichier": "PREVOL", "empreinte": "PREVOL", "verdict": "REGLAGE QUALIFIE (PREVOL)", "statut": "PREVOL",
             "e_sur_ln10_max": {p: 1e-5 for p in DEGRES}}
    L = executer_alpha(registre, sortie, mod, porte, prevol={"synth": SynthAlpha(s_etoile)})""",
"""    porte = {"fichier": "PREVOL", "empreinte": "PREVOL", "verdict": "REGLAGE QUALIFIE (PREVOL)", "statut": "PREVOL",
             "e_sur_ln10_max": {p: 1e-9 for p in DEGRES}}
    L = executer_alpha(registre, sortie, mod, porte, prevol={"synth": SynthAlpha(s_etoile)})""") )

R.append(('P34 bruit synthetique (3b doit rester muette quand il le faut)',
"""class SynthAlpha(object):""",
"""# Au reglage prime, la dispersion lnA d'un synthetique doit DEPASSER le
# plancher' (sinon la branche 3b mord sur tout synthetique). Plutot qu'un
# bruit tire, la fabrique porte un DECALAGE lnA DECLARE par variante :
# plan (dt_2, k=2) -> 0 ; G-dt (dt_2/2) -> +B ; G-k (k=4) -> -B. La
# dispersion vaut 2B PAR CONSTRUCTION (deterministe, aucune graine), P-A
# est EXACT au plan, et 2B = 4e-06 > plancher'(7) = 9.178e-07, marge x4.
BRUIT_SYNTH = 2e-6


class SynthAlpha(object):""") )

R.append(('P35 banc : synthetiques au bruit tare',
"""        L_dt, _ = jouer_synth(SynthAlpha(s_etoile, dep_dt=0.2))
        L_k, _ = jouer_synth(SynthAlpha(s_etoile, dep_k=0.1))
        L_w, _ = jouer_synth(SynthAlpha(s_etoile, dep_w2=0.2))
        L_f, c_f = jouer_synth(SynthAlpha(s_etoile, sans_cap=True))""",
"""        L_dt, _ = jouer_synth(SynthAlpha(s_etoile, dep_dt=0.2))
        L_k, _ = jouer_synth(SynthAlpha(s_etoile, dep_k=0.1))
        L_w, _ = jouer_synth(SynthAlpha(s_etoile, dep_w2=0.2))
        L_f, c_f = jouer_synth(SynthAlpha(s_etoile, sans_cap=True))""") )

R.append(('P36 banc : faux blowup et dep_s au bruit tare',
"""        L_i, _ = jouer_synth(SynthAlpha(s_etoile, sous_seuil="faux_blowup"))
        L_s, _ = jouer_synth(SynthAlpha(s_etoile, dep_s=0.5))""",
"""        L_i, _ = jouer_synth(SynthAlpha(s_etoile, sous_seuil="faux_blowup"))
        L_s, _ = jouer_synth(SynthAlpha(s_etoile, dep_s=0.5))""") )

R.append(('P37 banc : les scenarios v4',
"""    if mod is not None:
        p, w2 = 4, 1.73

        def ph1_faux(w2, s, p, mode, **kw):
            return phase1_pu(w2, s, p, mode, acc_fn=lambda w2, g, p: acc_pu(w2, g, p + 1))""",
"""    # ------------------ scenarios v4 (gel constante A v4, 10 ; temoin v9) --
    # G22 branche 3b : dispersion SOUS le plancher -> NON CONCLUANT DE PLANCHER
    JRN.silence = True
    try:
        L_pl, _ = jouer_synth(SynthAlpha(s_etoile, bruit_lnA=0.0))
    finally:
        JRN.silence = False
    v, b = cascade_alpha(L_pl)
    scenario("G22 decalage lnA nul : dispersion sous le plancher' -> G-plancher MORD -> branche 3b",
             v == "NON CONCLUANT DE PLANCHER" and "3b" in b and all(L_pl["degres"][p]["G_plancher_mord"] for p in DEGRES),
             v + " / " + b, gardes=("G-plancher",))
    # G23-G26 : la chaine des etages sur le probleme MANUFACTURE (forcage),
    # depart a l'etat EXACT de la bascule 5.3 -- reel, court.
    p23, w23 = 7, 1.73
    f23 = forcage_de(p23, w23)
    e23 = vers_composantes(*xm_et_derivees(p23, K_BASC * tau_dom_0(w23)), w23)
    g2a = phase2_pu(w23, p23, e23, -K_BASC * tau_dom_0(w23), dt2a_de(w23),
                    forcage=f23, tau_star=0.0, arret_cap=x_bascule(p23, w23), t_max=1e9)
    lo23, hi23 = intervalle_evenement(n_2a_nominal(), retard_2a(w23))
    g2b = phase2_pu(w23, p23, g2a["etat_fin"], float(g2a["t"][-1]), dt2_de(w23),
                    forcage=f23, tau_star=0.0, arret_cap=cap_p(p23, w23), t_max=1e9)
    lo23b, hi23b = intervalle_evenement(n_2b_nominal(), RETARD_2B)
    scenario("G23 chaine 2a+2b manufacturee : comptes DANS les intervalles derives, CAP' atteint",
             g2a["evenement"] == "CAP" and lo23 <= g2a["n"] <= hi23
             and g2b["evenement"] == "CAP" and lo23b <= g2b["n"] <= hi23b,
             "n_2a=%d [%d,%d] n_2b=%d [%d,%d]" % (g2a["n"], lo23, hi23, g2b["n"], lo23b, hi23b), gardes=())
    scenario("G24 etage 2a ABSENT : n_2a = 0 hors [%d, %d] -> la garde de compte MORD (G-fen)" % (lo23, hi23),
             not (lo23 <= 0 <= hi23), "un 620 asserte ne l'aurait pas vu", gardes=("G-compte-etage",))
    xg = float(g2b["x1"][-1] + g2b["x2"][-1])
    scenario("G25 n_2s > 620 SANS morsure : 658 dans [620, 659] a w2=1.73 (un 620 asserte = banc mort)",
             intervalle_2s(1.73) == (620, 659) and 620 < 658 <= 659 and not (658 == 620),
             "n_2s derive = 658", gardes=())
    # G26 W-bascule voie A : g2 ABSENTE -> la remise d'etat que la CHAINE
    # COMPLETE qualifie (v9 8) rate : la phase grossiere a dt_1 place
    # l'etat a +-dt_1 pres (enorme devant tau' ~ 1.6e-03), et la LECTURE
    # D-t-19 sur la phase raffinee (e_avec <= tol x ln 10) MORD. Joue a
    # p = 4 (alpha = 2, derivees en tau^-3 / tau^-4 : le pas grossier ne
    # pardonne pas).
    p26, w26 = 4, 1.73
    f26 = forcage_de(p26, w26)
    eg1 = vers_composantes(*xm_et_derivees(p26, KP_BASC * tau_dom_0(w26)), w26)
    sans_g2 = phase2_pu(w26, p26, eg1, -KP_BASC * tau_dom_0(w26), DT1,
                        forcage=f26, tau_star=0.0, arret_cap=x_bascule(p26, w26), t_max=1e9)
    if sans_g2["evenement"] == "CAP":
        ph_r = phase2_pu(w26, p26, sans_g2["etat_fin"], float(sans_g2["t"][-1]), dt2_de(w26),
                         forcage=f26, tau_star=0.0, tau_fin=tau_cap(w26), t_max=1e9)
        if ph_r["evenement"] == "TAU_FIN":
            tau_r = np.maximum(-ph_r["t"], 1e-300)
            xm_r = A_de(p26) * tau_r ** (-float(alpha_de(p26)))
            e26 = float(np.max(np.abs((ph_r["x1"] + ph_r["x2"]) - xm_r) / np.abs(xm_r)))
        else:
            e26 = float("inf")
        rate = (not math.isfinite(e26)) or e26 > float(PLAFOND_ALPHA) * LN10
        det26 = "e_avec sans g2 = %.3e (lecture D-t-19 : tol = %.3e)" % (e26, float(PLAFOND_ALPHA) * LN10)
    else:
        rate = True
        det26 = "traversee grossiere : %s" % sans_g2["evenement"]
    scenario("G26 W-bascule voie A : g2 absente -> la lecture D-t-19 de la chaine complete MORD",
             rate, det26, gardes=("W-bascule",))
    # G27 D-M17-58 : une entree au signe inverse -> la garde MORD
    S27 = lire_signes(REGISTRE_BANC)
    t27 = {(p, "%.2f" % w2, S27[(p, w2)]["sgn"]): s_etoile[(p, w2)] for p in DEGRES for w2 in W2S}
    t27[(5, "2.27", +1)] = t27.pop((5, "2.27", -1))
    scenario("G27 D-M17-58 : table factice au signe inverse a (5, 2.27) -> la garde MORD",
             len(garde_signe_factice(t27, s_etoile, S27)) == 1, gardes=("D-M17-58",))
    # G28 9bis : mord au perimetre, muet hors perimetre et sur les exemptes
    ref28 = {"T1": {"A": {"x": 1.0, "duree_s": 3.0}}, "T1b": {}, "T3a": {}, "T3b": {},
             "meta": {"date_utc": "X"}}
    a28 = json.loads(json.dumps(ref28)); a28["T1"]["A"]["x"] = 2.0
    b28 = json.loads(json.dumps(ref28)); b28["meta"]["date_utc"] = "Y"; b28["T1"]["A"]["duree_s"] = 9.0
    scenario("G28 9bis : ecart au perimetre -> 1 ecart ; meta et duree_s -> 0 ecart",
             len(controle_9bis(a28, ref28, 3, {"duree_s"})) == 1
             and controle_9bis(b28, ref28, 3, {"duree_s"}) == [],
             gardes=("9bis",))
    if mod is not None:
        p, w2 = 4, 1.73

        def ph1_faux(w2, s, p, mode, **kw):
            return phase1_pu(w2, s, p, mode, acc_fn=lambda w2, g, p: acc_pu(w2, g, p + 1))""") )

R.append(('P38 banc : registre en portee',
"""def banc_gardes(s_etoile, journal=True, mod=None):""",
"""REGISTRE_BANC = "."


def banc_gardes(s_etoile, journal=True, mod=None):""") )

R.append(('P39 main : registre du banc (un seul global, en tete)',
"""    a = ap.parse_args()
    t_debut = time.perf_counter()""",
"""    a = ap.parse_args()
    global REGISTRE_BANC
    REGISTRE_BANC = a.registre
    t_debut = time.perf_counter()""") )

R.append(('P40 (absorbe par P39 : un seul global en tete de main)',
"""        if a.banc:
            ok_b, S = banc(a.registre, mod, sortie)""",
"""        if a.banc:
            ok_b, S = banc(a.registre, mod, sortie)   # REGISTRE_BANC deja lie (P39)""") )

R.append(('P41 meta : bases et LD',
"""                 "gel_temoin": GEL_TEMOIN, "gel_alpha": GEL_ALPHA, "cert_temoin": CERT_TEMOIN, "cert_alpha": CERT_ALPHA,""",
"""                 "gel_temoin": GEL_TEMOIN, "gel_alpha": GEL_ALPHA, "cert_temoin": CERT_TEMOIN, "cert_alpha": CERT_ALPHA,
                 "gel_temoin_base": GEL_TEMOIN_BASE, "gel_alpha_base": GEL_ALPHA_BASE,
                 "cert_temoin_base": CERT_TEMOIN_BASE, "cert_alpha_base": CERT_ALPHA_BASE,""") )

R.append(('P42 reglage : delta_0 au JSON',
"""    L["reglage"] = {"delta": str(DELTA), "r": str(R_CAP), "M": M_PAS, "k": K_BASC, "eta": str(ETA),""",
"""    L["reglage"] = {"delta": str(DELTA), "delta_0": str(DELTA_0), "b": B_DESC, "m": M_MARGE, "J": J_DESC,
                    "r": str(R_CAP), "M": M_PAS, "k": K_BASC, "eta": str(ETA),""") )

R.append(('P43 verifier_ancres : les bases aussi',
"""    for (chemin, emp, taille) in (GEL_TEMOIN, GEL_ALPHA):""",
"""    for (chemin, emp, taille) in (GEL_TEMOIN, GEL_ALPHA, GEL_TEMOIN_BASE, GEL_ALPHA_BASE):""") )

R.append(('P44 verifier_ancres : certifications',
"""    for (chemin, emp) in (CERT_TEMOIN, CERT_ALPHA):""",
"""    for (chemin, emp) in (CERT_TEMOIN, CERT_ALPHA, CERT_TEMOIN_BASE, CERT_ALPHA_BASE):""") )

R.append(('P45 serie B : attentes transposees au reglage prime',
"""        L_v = jouer_synth(SynthAlpha(s_etoile), sb)
        L_r = jouer_synth(SynthAlpha(s_etoile, alpha_fact=1.3), sb)
        L_p = jouer_synth(SynthAlpha(s_etoile, A_fact=1.5), sb)
        L_i = jouer_synth(SynthAlpha(s_etoile, sous_seuil="faux_blowup"), sb)
        L_s = jouer_synth(SynthAlpha(s_etoile, dep_s=0.5), sb)
    finally:
        JRN.silence = False
    v, b = cascade_alpha(L_v)
    scenario("B4a ansatz exact (alpha=4/(p-2), A=A_p) -> VERIFIE", v == "VERIFIE", v + " / " + b)""",
"""        L_0 = jouer_synth(SynthAlpha(s_etoile, bruit_lnA=0.0), sb)
        L_v = jouer_synth(SynthAlpha(s_etoile), sb)
        L_r = jouer_synth(SynthAlpha(s_etoile, alpha_fact=1.3), sb)
        L_p = jouer_synth(SynthAlpha(s_etoile, A_fact=1.5), sb)
        L_i = jouer_synth(SynthAlpha(s_etoile, sous_seuil="faux_blowup"), sb)
        L_s = jouer_synth(SynthAlpha(s_etoile, dep_s=0.5), sb)
    finally:
        JRN.silence = False
    v, b = cascade_alpha(L_0)
    scenario("B4a0 ansatz quasi exact : dispersion SOUS le plancher' -> branche 3b (v4 7)",
             v == "NON CONCLUANT DE PLANCHER" and "3b" in b, v + " / " + b, gardes=("G-plancher",))
    v, b = cascade_alpha(L_v)
    scenario("B4a ansatz exact au bruit d'instrument -> VERIFIE (3b muette : la dispersion depasse le plancher)",
             v == "VERIFIE", v + " / " + b)""") )

R.append(('P46 SynthAlpha : parametre bruit_lnA',
"""                 dep_dt=0.0, dep_k=0.0, dep_w2=0.0, sans_cap=False):""",
"""                 dep_dt=0.0, dep_k=0.0, dep_w2=0.0, sans_cap=False, bruit_lnA=None):"""))

R.append(('P47 SynthAlpha : attribut bruit_lnA',
"""        self.dep_dt, self.dep_k, self.dep_w2, self.sans_cap = dep_dt, dep_k, dep_w2, sans_cap""",
"""        self.dep_dt, self.dep_k, self.dep_w2, self.sans_cap = dep_dt, dep_k, dep_w2, sans_cap
        self.bruit_lnA = BRUIT_SYNTH if bruit_lnA is None else bruit_lnA"""))

R.append(('P48 SynthAlpha : decalage lnA par variante',
"""            x0 = etat[0] + etat[1]
            a = a * (1 + self.dep_s * (self._c - C_PLAN[0]))""",
"""            x0 = etat[0] + etat[1]
            # decalage lnA DECLARE par variante (voir BRUIT_SYNTH) :
            if dt < dt2_de(w2) * 0.75:
                A = A * math.exp(+self.bruit_lnA)
            elif getattr(self, "_k", K_BASC) != K_BASC:
                A = A * math.exp(-self.bruit_lnA)
            a = a * (1 + self.dep_s * (self._c - C_PLAN[0]))"""))

R.append(('P49 SynthAlpha : la detection de k lit la bascule 5.3 au REPERE',
"""            self._k = K_BASC if x_b >= x_bascule(p, w2, K_BASC) * 0.999 else K_GARDE""",
"""            self._k = K_BASC if x_b >= x_bascule_0(p, w2, K_BASC) * 0.999 else K_GARDE"""))

R.append(('P50 enumerer_gardes : les gardes vivent aux gels de BASE + G-plancher (v4)',
"""    for (chemin, fam) in ((GEL_TEMOIN[0], "W"), (GEL_ALPHA[0], "G")):""",
"""    for (chemin, fam) in ((GEL_TEMOIN[0], "W"), (GEL_ALPHA_BASE[0], "G")):"""))

R.append(('P51 enumerer_gardes : G-plancher declaree par la v4 (section 7)',
"""        for g in set(re.findall(r"^ {4}(%s-[a-z][a-z0-9]*)(?![A-Za-z0-9_-])" % fam, m.group(0), re.M)):
            gardes[g] = chemin
    return gardes""",
"""        for g in set(re.findall(r"^ {4}(%s-[a-z][a-z0-9]*)(?![A-Za-z0-9_-])" % fam, m.group(0), re.M)):
            gardes[g] = chemin
    p4 = os.path.join(registre, GEL_ALPHA[0])
    if os.path.isfile(p4) and re.search(r"^7[.] LA PORTE DU PLANCHER [(]G-plancher[)]",
                                        open(p4, encoding="utf-8").read(), re.M):
        gardes["G-plancher"] = GEL_ALPHA[0]
    return gardes"""))

R.append(('P52 T-2 : plancher de COMPOSANTES consigne (candidate D-t-22)',
"""            p_obs = math.log2(err["dt2"]["e"] / err["dt2/2"]["e"]) if err["dt2/2"]["e"] > 0 else float("inf")
            plancher = eps * err["dt2/2"]["n_pas"]""",
"""            p_obs = math.log2(err["dt2"]["e"] / err["dt2/2"]["e"]) if err["dt2/2"]["e"] > 0 else float("inf")
            plancher = eps * err["dt2/2"]["n_pas"]
            # CONSIGNATION SEULE (N-62, D-M17-47 : aucune tolerance neuve) :
            # au reglage prime, x = x1 + x2 s'evalue par compensation de
            # composantes ~ alpha(alpha+1)/((w2^2-1) tau^2) fois plus
            # grandes que x ; le plancher machine REEL de e est eps x R,
            # que le plancher eps x N du gel (5.4) ne modelise pas.
            # Mesure sur le flot a dt2/2, consignee pour l'acte
            # (trouvaille machine 1 contre le gel temoin v9, a arbitrer).
            R_comp = float(np.max((np.abs(ph["x1"]) + np.abs(ph["x2"])) / np.maximum(np.abs(ph["x1"] + ph["x2"]), 1e-300)))
            plancher_composantes = eps * R_comp"""))

R.append(('P53 T-2 : plancher de composantes au point et au journal',
"""                  "plancher": plancher, "c_pl_plancher": C_PL * plancher,""",
"""                  "plancher": plancher, "c_pl_plancher": C_PL * plancher,
                  "R_composantes": R_comp, "plancher_composantes": plancher_composantes,
                  "e_dt2s2_sur_plancher_comp": err["dt2/2"]["e"] / plancher_composantes if plancher_composantes > 0 else float("inf"),"""))

# ------------------------------------------------------------------ apply
out = src
for (nom, old, new) in R:
    n = out.count(old)
    if n != 1:
        sys.exit("ANCRAGE %s : %d occurrence(s), attendu 1" % (nom, n))
    out = out.replace(old, new)
    print("  ok %s" % nom)

assert all(ord(c) < 128 for c in out), "sortie non ASCII"
assert "\r" not in out, "sortie porte un CR"
open(DST, "w", encoding="utf-8", newline="\n").write(out)
b = open(DST, "rb").read()
print("\nv3 %s  %d o" % (canon(src), len(src.encode())))
print("v4 %s  %d o  (%d remplacements)" % (canon(out), len(b), len(R)))
