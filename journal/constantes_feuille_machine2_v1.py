# -*- coding: ascii -*-
"""Constantes de la feuille d'ordre 3 de machine 1 (facd3ceeec07d3bf) lues dans SON texte et comparees a ce que dit le GEL (sections 5, 6, 4.4). Complete la confrontation, qui ne peut pas voir une constante
que les donnees jouees n'approchent pas (mutations K03, K07, K08, K28-K30, K35 : donnees sans sensibilite). Les valeurs attendues sont ecrites ICI a partir du gel, pas lues dans la feuille."""
import re, sys
f = open(sys.argv[1], encoding='ascii').read()
res = []
def ctl(n, ok, d):
    res.append(ok); print('%-4s %-6s %s' % (n, 'TIENT' if ok else 'MORD', d))
def ligne(cle):
    m = re.search(r'^[^\n]*\b' + cle + r'\b[^\n]*$', f, re.M)
    return m.group(0)
att = [('E_MAX', 'E_MAX = 0.7', 'e_bord < 0.7 (gel 5)'), ('STAB_MAX', 'STAB_MAX = 0.05', 'stabilite de la chaine d ordre 3 <= 0.05 (gel 5)'), ('J_NET', 'J_NET = 0.2', 'ecart-type de J < 0.2 (gel 5)'),
       ('E_BAS', 'E_BAS = 0.3', 'T = 0.05 si e_bord < 0.3 (gel 6)'), ('T_BAS', 'T_BAS = 0.05', 'T bas 0.05 (gel 6)'), ('T_HAUT', 'T_HAUT = 0.10', 'T haut 0.10 (gel 6)'),
       ('DOM_MIN', 'DOM_MIN = 5', 'ligne : au moins 5 etats dans le domaine (gel 5)'), ('BORD_MIN', 'BORD_MIN = 2', 'bord : au moins 2 dans le domaine et 2 hors (gel 5)'),
       ('PART_JUGES', 'PART_JUGES = F(2, 3)', 'au moins les deux tiers des etats lus sont juges (gel 5)'), ('PART_E2', 'PART_E2 = F(3, 4)', 'E2 : les trois quarts, arrondis par exces (gel 6)'),
       ('INEXPLOITABLES_E1', 'INEXPLOITABLES_E1 = 2', 'E1 : NON CONCLUANT si PLUS de deux inexploitables (gel 6)'), ('INEXPLOITABLES_E2', 'INEXPLOITABLES_E2 = 1', 'E2 : NON CONCLUANT si plus d une inexploitable (gel 6)'),
       ('N_ETATS', 'N_ETATS = 14', 'quatorze etats par point (gel 4.2)'), ('TOL_ANCRE_REL', 'TOL_ANCRE_REL, TOL_ANCRE_ABS, TOL_ANCRE_E = 1e-3, 1e-12, 1e-9', 'ancres : 1e-3 relatif + 1e-12, energie 1e-9 (gel 4.4)'),
       ('EF', 'EF = 0.0625; ETAS = (0.25, 0.125, 0.0625, 0.03125)', 'facteur d eta 1/16 ; quatre eta de chaine (gel 5)'), ('BANDES', 'BANDES = ((0.06, 1.25), (0.10, 1.6), (0.12, 2.0))', '1.25 jusqu a 0.06, 1.6 jusqu a 0.10 (gel 6, le 2.0 est celui du delta 98 hors gel)')]
for cle, texte, gel in att:
    l = ligne(cle)
    ctl(cle, texte in f, '%s : "%s" dans la feuille ; le gel dit : %s' % (cle, texte, gel))
ctl('STABLE', 'return bool(all(x > 0.0 for x in v) and max(v) / min(v) <= 2.0)' in f, 'stable : quatre valeurs > 0, plus grande / plus petite <= 2 (gel 5)')
ctl('DOMAINE', 'bool(c["G3"] > 0.0 and c["e_bord"] < E_MAX and c["stab3"] is not None and c["stab3"] <= STAB_MAX)' in f, 'domaine : e_bord < E_MAX et stabilite definie et <= STAB_MAX (gel 5)')
ctl('TOL', 'abs(math.log(q3)) <= tol' in f and 'tol = T_BAS if c["e_bord"] < E_BAS else T_HAUT' in f, 'E1 : |ln q3| <= T ; T selon e_bord < E_BAS (gel 6)')
ctl('PRES', 'abs(math.log(q3)) < abs(math.log(q2))' in f, 'E2 : |ln q3| < |ln q2| (gel 6)')
ctl('SEUIL', 'seuil = -(-PART_E2.numerator * len(dom) // PART_E2.denominator)' in f, 'E2 : seuil = les trois quarts arrondis par exces (gel 6)')
ctl('GARDE', 'F(len(jug)) >= PART_JUGES * len(etats)' in f, 'garde des deux tiers : >= (gel 5 : "au moins")')
ctl('EXPL_LIGNE', 'bool(assez and len(dom) >= DOM_MIN)' in f and 'bool(assez and len(dom) >= BORD_MIN and len(hors) >= BORD_MIN)' in f, 'exploitable : ligne >= DOM_MIN dans le domaine ; bord >= BORD_MIN dans le domaine ET >= BORD_MIN hors (gel 5)')
ctl('E1B', 'issue(brd, "E1", 0, 0)' in f, 'E1B : TOMBE si une cellule exploitable tombe ; NON CONCLUANT si l une est inexploitable (gel 6)')
ctl('E2M2', 'issue(ligN, "E2", INEXPLOITABLES_E2, 1)' in f and 'issue(lig, "E1", INEXPLOITABLES_E1, 1)' in f, 'E1 et E2 : une chute admise (TENU SAUF UNE CELLULE) ; E2 = la constante de M-2 / E-2 (le gel 6 ecrit les memes niveaux)')
ctl('E3', 'all(r["dans_la_bande"] for r in jug)' in f and '1.0 / B <= q2 <= B' in f, 'E3 : tous les etats juges, 1/B <= q2 <= B (gel 6)')
i1 = f.find('r["exclu"] = "non qualifie"'); i2 = f.find('r["exclu"] = "J flou"'); i3 = f.find('r["exclu"] = "etiquette double"'); i4 = f.find('r["exclu"] = "barriere vide"'); i5 = f.find('r["exclu"] = "chaine du moteur instable"'); i6 = f.find('r["exclu"] = "chaine d' + chr(39) + 'ordre 2 instable"')
ctl('ORDRE', 0 < i1 < i2 < i3 < i4 < i5 < i6, "exclusion des etats : non qualifie, J flou, etiquette double, barriere vide, chaine du moteur instable, chaine d'ordre 2 instable, dans cet ordre (gel 5 : premier motif)")
ctl('STAB1', 'elif not c["stable1"]:' in f and 'elif not c["stable2"]:' in f and '"stable1": stable(g1)' in f and '"stable2": stable(g2)' in f, 'etats a chaine du moteur ou d ordre 2 instable : exclus ; stable1 = stable(G1 aux quatre eta), stable2 = stable(G2 aux quatre eta) (gel 5)')
ctl('G2IDX', 'q2 = c["G2"][2] / Gpl' in f and '"G2": g2' in f and 'g2 = [r["Gamma_flux"] for r in r2]' in f and 'r2 = [gamma_chaine_ordre2(tb, x) for x in ETAS]' in f and 'ETAS = (0.25, 0.125, 0.0625, 0.03125)' in f, 'q2 = G2 au facteur 1/16 (indice 2 des quatre eta) / Gamma_pl (gel 5, grandeurs)')
ctl('Q3', 'q3 = (c["G3"] / Gpl) if c["G3"] > 0.0 else None' in f and 'r3 = gamma_chaine_ordre3(tb, t3, EF); G3 = r3["Gamma_flux"]' in f, 'q3 = G3 / Gamma_pl, G3 au facteur EF = 1/16 (gel 5)')
ctl('PLATEAU_A', 'Gpl = ev["plateaux"]["A"]["Gamma_pl"]' in f, 'Gamma_pl = largeur de plateau sous l absorbeur A (gel 5)')
print('BILAN : %d controles, %d tiennent' % (len(res), sum(res)))
sys.exit(0 if all(res) else 1)
