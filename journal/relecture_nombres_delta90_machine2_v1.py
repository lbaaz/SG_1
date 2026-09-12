#!/usr/bin/env python3
# -*- coding: ascii -*-
"""RELECTURE DES NOMBRES DE L'ACTE delta 90 -- AUX SOURCES. machine 2, v1, 12/09/2026.

L'acte `journal_delta_nn_constante_A_v1.md` cite des nombres. Cette feuille de MESURE les
relit A LA SOURCE, en DEUX JAMBES, et il en faut deux :
  (1) le nombre recalcule depuis la source (JSON, log authentifie par canon, note) vaut ce
      que l'acte annonce, ou la chaine est LITTERALEMENT dans la piece citee ;
  (2) la chaine annoncee est LITTERALEMENT dans l'acte.
La jambe (2) seule laisserait passer un nombre juste mais absent ; la jambe (1) seule
laisserait passer une faute de frappe. Chaque source est AUTHENTIFIEE PAR CANON avant
lecture : un nombre relu dans une piece qui n'est pas celle que l'acte cite ne relit rien.
Les sources dont l'acte ne cite que le LOT (notes de machine 1) sont authentifiees contre la
ligne de table de leur manifeste.

DEUX VERBES : `chk` mesure et compte ; `note` porte la prose. Aucune source n'est editee.
"""
import hashlib, json, os, re, sys, unicodedata
from fractions import Fraction as F

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
P = lambda *a: os.path.join(RAC, *a)
ACTE = open(os.path.join(ICI, 'journal_delta_nn_constante_A_v1.md'), encoding='utf-8').read()
OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-56s %s' % ('PASSE' if c else 'MORD ', n[:56], d))


def note(n, d=''):
    print('  [ note] %-56s %s' % (n[:56], d))


def canon(p):
    raw = open(p, 'rb').read()
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8'))
        return hashlib.sha256(t.replace('\r\n', '\n').replace('\r', '\n').encode()).hexdigest()[:16]
    except UnicodeDecodeError:
        return hashlib.sha256(raw).hexdigest()[:16]


def canon_de_table(manifeste, nom):
    """Le canon B d'une piece tel que la TABLE de son manifeste le declare."""
    for l in open(P(*manifeste), encoding='utf-8').read().split('\n'):
        if re.match(r'^[0-9a-f]{16}\s', l) and nom in l:
            return l.split()[0]
    return None


def source(etq, chemin, attendu):
    """Authentifie une source par canon AVANT de la lire ; rend son texte (CRLF normalise)."""
    p = P(*chemin)
    c = canon(p)
    chk('source %-28s %s' % (etq, attendu), c == attendu, os.path.join(*chemin)[-60:])
    return open(p, 'rb').read().replace(b'\r\n', b'\n').decode('utf-8', 'replace')


def js(etq, chemin, attendu):
    p = P(*chemin)
    chk('source %-28s %s' % (etq, attendu), canon(p) == attendu, os.path.join(*chemin)[-60:])
    return json.load(open(p, encoding='utf-8'))


def N(s):
    """Blancs normalises : les pieces sont enveloppees a 72-80 colonnes, une phrase enjambe
    une fin de ligne (regle 4 du 28/08). Les NOMBRES n'ont pas de blanc : inchanges."""
    return re.sub(r'\s+', ' ', s)


ACTE_N = N(ACTE)


def cite(etq, txt, src=None, recalc=None, attendu=None, dans_acte=None):
    """(2) txt (ou dans_acte) est dans l'acte ; (1) txt est dans la source, ou recalc == attendu.
    Les presences se testent sur BLANCS NORMALISES, des deux cotes."""
    a = txt if dans_acte is None else dans_acte
    dans = N(a) in ACTE_N
    if recalc is not None:
        bon = (recalc == attendu)
        d = 'recalcul %r vs annonce %r' % (recalc, attendu)
    elif src is not None:
        bon = N(txt) in N(src)
        d = txt + ('' if bon else '  ABSENT DE LA SOURCE')
    else:
        bon = True
        d = txt
    chk(etq, dans and bon, ('' if dans else 'ABSENT DE L ACTE (%r) ; ' % a[:30]) + d)


# =====================================================================
print('\n1. LA TENAILLE -- RELUE DANS LE LOG DE MESURE, REPRODUIT AU BIT PAR MACHINE 1')
# =====================================================================
LOG3 = source('derivation v3 .log', ('ACTE_constante_A', 'derivation_fenetre_delta_machine2_v3.log'),
              'f60104c0c3ba7ec4')
LOG3_M1 = source('rejeu m1 du meme log', ('entrant_machine1_2026-09-12_rejeu_relivraison', 'lot',
                                          'rejeu_derivation_v3_machine1_v1.log'), 'f60104c0c3ba7ec4')
chk('les deux logs sont IDENTIQUES (CRLF normalise)', LOG3 == LOG3_M1, '%d lignes' % LOG3.count('\n'))
for etq, txt in (('INF retenue', '1.659260768e-05'), ('INF v1 depuis le log', '1.659725811e-05'),
                 ('SUP m=1', '3.457292925e-05'), ('SUP m=2', '1.728646463e-05'),
                 ('SUP m=3', '1.152430975e-05'), ('lecture NOYAU', '1.286193025e-05'),
                 ('lecture LIBM et la mienne', '1.427322916e-05'),
                 ('facteur NOYAU', 'x1.3171'), ('facteur LIBM', 'x1.4616'), ('facteur conservatrice', 'x1.6991'),
                 ('carte m=1 kT=1', 'x2.0836'), ('carte m=2 kT=1', 'x1.0418'), ('carte m=1 kT=1.15', 'x1.8119'),
                 ('carte m=1 kT=1.30', 'x1.6028'), ('carte m=1 kT=1.50', 'x1.3891'), ('carte m=1 kT=1.74', 'x1.1975'),
                 ('forme fermee, ecart max', '7.33e-07'), ('invariance de e', '[0.9367, 1.1625]'),
                 ('bits de INF sous mutation', '3ef1660b5147653b'), ('lecture mutee', '4.287310084e-06'),
                 ('ecart JSON/log', '2.8027e-04'), ('marge', '4.1817e-02'), ('rapport', '149'),
                 ('bilan de la feuille', '22/22'), ('rapport tau_CAP exact', '0.00e+00')):
    cite('%-32s %s' % (etq, txt), txt, src=LOG3)
cite('0 changement de statut', '0 changement', src=LOG3,
     dans_acte='aucune des 15 cellules de la carte ne change de statut')
LOGP = source('precision de la borne .log', ('G5_cloture', 'precision_de_la_borne_machine2_v1.log'),
              '8a23a9227911d398')
cite('fenetre v1 depuis le log             x1.0415', 'x1.0415', src=LOGP)
chk('0.589 (acte) est l arrondi du 0.5886 du log', '0.5886' in LOG3 and '0.589' in ACTE and '%.3f' % 0.5886 == '0.589', '0.589')
chk('l acte dit 15 cellules, le log en compte 15 (3 m x 5 kT)',
    '15 cellules' in ACTE and len(re.findall(r'^\s+\d\.\d\d\s+\|', LOG3, re.M)) == 5, '5 lignes kT x 3 colonnes m')

# =====================================================================
print('\n2. LES JSON -- LE PORTEUR, LES SIX CELLULES, LES QUATRE LUES, LA PORTE, tol_int')
# =====================================================================
J_MOI = js('pre-vol m2 v8 JSON', ('m2_v8_prevol_temoin_resultats.json',), '0a24121e441cc0c3')
J_NOY = js('pre-vol m1 NOYAU JSON', ('entrant_machine1_2026-09-12_reponse_globale', 'lot',
                                     'resultats_temoin_prevol_noyau_machine1.json'), 'd3417a81e03b2861')
J_LIB = js('pre-vol m1 LIBM JSON', ('entrant_machine1_2026-09-12_reponse_globale', 'lot',
                                    'resultats_temoin_prevol_libm_machine1.json'), '95acd5d9c844eacc')
MOI, NOY, LIB = J_MOI['T2']['points'], J_NOY['T2']['points'], J_LIB['T2']['points']
cite('porteur 7|1.73 chez m2, a trois decimales', '0.684', recalc='%.3f' % MOI['7|1.73']['ratio_seuil'], attendu='0.684')
cite('porteur 7|1.73 chez m1 (noyau), a trois decimales', '0.759', recalc='%.3f' % NOY['7|1.73']['ratio_seuil'], attendu='0.759')
cite('5|1.73 sur le fil', '0.991', recalc='%.3f' % MOI['5|1.73']['ratio_seuil'], attendu='0.991')
ecart_pc = abs(NOY['7|1.73']['ratio_seuil'] - MOI['7|1.73']['ratio_seuil']) / MOI['7|1.73']['ratio_seuil'] * 100
cite('ecart au porteur, pour cent', '11.0 pour cent', recalc='%.1f' % ecart_pc, attendu='11.0')
dif = sorted(k for k in MOI if MOI[k]['ratio_seuil'] != NOY[k]['ratio_seuil'])
chk('SIX cellules different au bit', len(dif) == 6 and 'SIX au bit' in ACTE, ','.join(dif))
dif3 = sorted(k for k in MOI if '%.3f' % MOI[k]['ratio_seuil'] != '%.3f' % NOY[k]['ratio_seuil'])
chk('TROIS a la resolution du journal', len(dif3) == 3 and 'TROIS a la resolution du journal' in ACTE, ','.join(dif3))
lues6 = sorted(k for k in dif if MOI[k]['W_plancher'] != 'MORD')
lues3 = sorted(k for k in dif3 if MOI[k]['W_plancher'] != 'MORD')
chk('QUATRE lues sur six, DEUX sur trois', len(lues6) == 4 and len(lues3) == 2 and 'QUATRE lues' in ACTE
    and 'DEUX lues' in ACTE, '%s | %s' % (','.join(lues6), ','.join(lues3)))
chk('mes ratios == son LIBM au bit (9/9)', all(MOI[k]['ratio_seuil'] == LIB[k]['ratio_seuil'] for k in MOI), '0 ecart')
for k in dif:
    r = abs(MOI[k]['ratio_seuil'] - NOY[k]['ratio_seuil']) / MOI[k]['ratio_seuil']
    cite('ecart relatif %s' % k, '%s (%.1e)' % (k, r), recalc='%.1e' % r, attendu='%.1e' % r)
gros = [k for k in dif if abs(MOI[k]['ratio_seuil'] - NOY[k]['ratio_seuil']) / MOI[k]['ratio_seuil'] > 1e-2]
fin = [k for k in dif if abs(MOI[k]['ratio_seuil'] - NOY[k]['ratio_seuil']) / MOI[k]['ratio_seuil'] < 1e-7]
chk('separation nette : 3 grossieres, 3 fines, rien entre 1e-07 et 1e-02', len(gros) == 3 and len(fin) == 3
    and 'aucune entre 1e-07 et 1e-02' in ACTE, '%s | %s' % (','.join(gros), ','.join(fin)))
chk('le porteur est la seule grossiere NON LUE', [k for k in gros if MOI[k]['W_plancher'] == 'MORD'] == ['7|1.73'], '7|1.73')
egal = sorted(k for k in MOI if MOI[k]['ratio_seuil'] == NOY[k]['ratio_seuil'])
chk('trois cellules a ratio egal au bit : 5|2.27, 7|2.27, 7|2.80', egal == ['5|2.27', '7|2.27', '7|2.80']
    and '5|2.27, 7|2.27, 7|2.80' in ACTE, ','.join(egal))
xb = sorted(k for k in MOI if MOI[k]['bascule']['x_b_num'] != NOY[k]['bascule']['x_b_num'])
chk('x_b_num differe sur 7 des 9', len(xb) == 7 and 'differe sur 7 des 9' in ACTE, ','.join(xb))
chk('tau_CAP identique noyau/libm 9/9', all(NOY[k]['tau_CAP'] == LIB[k]['tau_CAP'] for k in NOY) and 'tau_CAP identique 9/9' in ACTE, '9/9')
d_ord = {k: abs(MOI[k]['tol_ordre'] - LIB[k]['tol_ordre']) / MOI[k]['tol_ordre'] for k in MOI}
p7 = sorted(k for k in d_ord if d_ord[k] > 0)
chk('tol_ordre differe BOCAL4/libm sur les trois cellules p = 7 seulement', p7 == ['7|1.73', '7|2.27', '7|2.80'],
    ','.join('%s %.1e' % (k, d_ord[k]) for k in p7))
cite('a un ulp, ecart RELATIF', '(1.6e-16 relatif)', recalc='%.1e' % max(d_ord.values()), attendu='1.6e-16')
cite('champ de forces BOCAL4', 'f7f8be507eb5e9cb', recalc=J_MOI['champ_forces_empreinte'], attendu='f7f8be507eb5e9cb')
cite('champ de forces noyau', '0491b83e6893dbbf', recalc=J_NOY['champ_forces_empreinte'], attendu='0491b83e6893dbbf')
cite('champ de forces libm', 'f150f2685187b9d2', recalc=J_LIB['champ_forces_empreinte'], attendu='f150f2685187b9d2')
cite('verdict du pre-vol', "NON CONCLUANT D'INTEGRATEUR", recalc=J_MOI['verdict'], attendu="NON CONCLUANT D'INTEGRATEUR")
cite('branche 4, les quatre points', 'branche  4 : W-plancher 5|1.73, W-plancher 7|1.73, W-plancher 7|2.27,\n             W-plancher 7|2.80 MORD',
     recalc=J_MOI['branche'], attendu='branche 4 : W-plancher 5|1.73, W-plancher 7|1.73, W-plancher 7|2.27, W-plancher 7|2.80 MORD')
LM1 = source('pre-vol m1 .log 28/08', ('prevol_temoin_v8_machine1.log',), 'c45ac9f59907fbf4')
chk('le pre-vol m1 du 28/08 rend la meme branche 4 (des deux cotes)', 'branche 4' in LM1 and 'des deux cotes' in ACTE, 'branche 4')
cite('41 comptes, 0 saute', '41 comptes, 0 saute, 41 attendus', recalc=(J_MOI['comptes']['comptes'], J_MOI['comptes']['sautes'], J_MOI['attendus_total']),
     attendu=(41, 0, 41))
chk('0 faute de pre-vol', J_MOI['prevol_fautes'] == [] and '0 faute de pre-vol' in ACTE, '[]')
for p_, k in ((4, '4|1.73'), (5, '5|1.73'), (7, '7|1.73')):
    cite('C(p = %d)' % p_, '%.4f (p = %d)' % (MOI[k]['C_effectif'], p_), recalc='%.4f' % MOI[k]['C_effectif'],
         attendu={4: '7.7143', 5: '8.3158', 7: '8.8966'}[p_])
cite('delta-prime = 1/102400', "delta' = 1/102400", recalc=J_MOI['reglage']['delta'], attendu='1/102400')
cite('delta-prime en flottant', '9.765625e-06', recalc='%.6e' % float(F(1, 102400)), attendu='9.765625e-06')
cite('delta-prime / INF', '0.589', recalc='%.3f' % (float(F(1, 102400)) / 1.659260768e-05), attendu='0.589')
J_REF = js('run_temoin_delta85 (registre)', ('registre', 'runs', 'run_temoin_delta85', 'resultats_temoin.json'), '644240dc894c2733')
tol = sorted({repr(v) for c in (J_REF['T1']['A']['W_integrales'], J_REF['T3a']['A']) for k, v in c.items() if k.startswith('tol_int')})
cite('tol_int deposee = valeur machine 2', '0.008578984888782988', recalc=tol, attendu=['0.008578984888782988'])
chk('et c est la valeur du pre-vol BOCAL4', repr(J_MOI['T3a']['A']['tol_int']) == '0.008578984888782988', repr(J_MOI['T3a']['A']['tol_int']))

# =====================================================================
print('\n3. LES COMPTES DU GESTE (2) ET DES TOURS -- RELUS DANS LES LOGS ET LES NOTES')
# =====================================================================
L3 = source('comparaison a trois .log', ('G4_trois', 'comparaison_a_trois_machine2_v1.log'), 'e4a2a6a6f327ee85')
cite('856 feuilles de chaque cote', '856', src=L3)
cite('82 exposees', '82 feuilles', src=L3)
cite('77 == LIBM, 0 == NOYAU', '77 / 82', src=L3, dans_acte='LIBM sur 77 et son run NOYAU\n      sur 0')
chk('0 / 82 dans le log', '0 / 82' in L3, '0 / 82')
cite('14 sur 774 hors exposees', '14 / 774', src=L3, dans_acte='14\n      feuilles sur 774')
LC = source('controle croise .log', ('ACTE_constante_A', 'controle_croise_classes_machine2_v1.log'), '0d0f10fe5c406787')
cite('15/15', '15/15', src=LC)
cite('0 des 9 intacte', '0 cellule intacte', src=LC, dans_acte='0 des 9 intacte')
cite('x_b_num 7 des 9', '7 des 9', src=LC)
cite('ratio_seuil 6 des 9', 'ne differe que sur 6', src=LC, dans_acte='ratio_seuil sur 6 des 9')
L28 = source('verification 28b .log', ('ACTE_constante_A', 'verification_28b_et_conventionB_machine2_v1.log'), '755c4c9ad79fb54b')
chk('91 et 154 CR', '91 CR' in L28 and '154 CR' in L28 and '91 et 154 CR' in ACTE, '91, 154')
cite('19/19', '19/19', src=L28)
chk('0 texte sur 771 .md', '0 texte' in L28 and '771 .md' in L28 and '0 sur 771 .md' in ACTE, '0 / 771')
cite('5639 octets', '5639 octets', src=L28)
cite('brut de la capture temoin', '3833ba551a390945', src=L28)
cite('brut de la capture alpha', '717b61caa5921aaa', src=L28)
cite('B des captures', '10a7ce5688f515d5', src=L28)
cite('B des captures (alpha)', '0e7e56006d2e200a', src=L28)
LG = source('garde chk constante .log (m1)', ('entrant_machine1_2026-09-12_R_G2_5_v2', 'garde_chk_constante_machine1_v1.log'), '28306881ecf4e557')
chk('5 appels a condition constante sur 7 feuilles', '5 appel(s) chk a condition constante sur 7 feuille(s)' in LG
    and '5 appels a condition constante sur 7' in ACTE, '5 / 7')
bloc_vl = LG.split('verifications_lecture_m1_machine2_v1.py')[1].split('r_g2_5')[0]
cite('les trois lignes de D-ACA-7', 'l.69, 126, 180', recalc=sorted(int(m) for m in re.findall(r'l\.(\d+)\s+True', bloc_vl)), attendu=[69, 126, 180])
chk('le False de la l.69 de verification_28b est sous condition', "l.69    False" in LG and 'False sous condition' in ACTE, 'l.69')
LR = source('R-G2-5 v2 sur le registre (m1)', ('entrant_machine1_2026-09-12_R_G2_5_v2', 'r_g2_5_pow_tableau_machine1_v2.log'), 'aa801b13ca41846f')
for etq, s_log, s_acte in (('91 .py', '91 fichiers .py', '91 fichiers .py'), ('545 puissances', 'TOTAL        545', '545 puissances'),
                           ('232 exposables', 'EXPOSABLE    232', '232\n      EXPOSABLES'),
                           ('41 fichiers', 'fichiers portant au moins une EXPOSABLE : 41', 'dans 41 fichiers'),
                           ('coeur du moteur', 'm9_replication_v1.py:324', 'm9_replication_v1.py:324'), ('HEAD d037d21', 'HEAD d037d21', 'd037d21')):
    chk('%-32s %s' % (etq, s_log), s_log in LR and s_acte in ACTE, s_log)
LV8 = source('R-G2-5 v2 sur le v8 (m1)', ('entrant_machine1_2026-09-12_rejeu_relivraison', 'lot', 'rejeu_R_G2_5_v2_sur_le_v8_machine1_v1.log'), 'e14b84d82da3bc47')
cl = {t[0]: int(t[1]) for t in (l.split() for l in LV8.split('\n')) if len(t) == 2 and t[0] in ('EXPOSABLE', 'CARRE', 'CONST') and t[1].isdigit()}
cite('42 / 9 / 6 sur le v8', '42\n      EXPOSABLES, 9 CARRE, 6 CONST', recalc=(cl.get('EXPOSABLE'), cl.get('CARRE'), cl.get('CONST')), attendu=(42, 9, 6))
chk('57 puissances sur le v8', '57 `**` enumeres' in LV8 and '57 puissances' in ACTE, '57')
N25 = source('note m1 lecture reponse (lot 25b6f78bdf2ddcff)', ('entrant_machine1_2026-09-12_R_G2_5', 'note_machine1_lecture_reponse_et_R-G2-5_v1.md'),
             canon_de_table(('entrant_machine1_2026-09-12_R_G2_5', 'MANIFEST_lot_machine1_lecture_reponse_et_R-G2-5_v1.txt'), 'note_machine1_lecture_reponse'))
chk('36 exposables au v3 depose', 'banc_qualification_machine1 v3 36' in N25 and '36 au v3' in ACTE, '36')
chk('207 .md au registre, 0 clause', '207 .md' in N25 and '0 sur 207' in ACTE, '207')
MREJ = source('manifeste rejeu m1', ('entrant_machine1_2026-09-12_rejeu_relivraison', 'lot', 'MANIFEST_lot_machine1_rejeu_relivraison_v1.txt'), 'be5ee780388d1965')
for etq, s_src, s_acte in (('158/158', '158 + absentes 0 + ecarts 0 == 158', '158/158'), ('driver 15/15', '15/15', '15/15'),
                           ('73 lignes, 0 differente', '73 lignes, 0 differente', '73 lignes, 0 differente'),
                           ('relecture 39/39', '39/39', '39/39'), ('6 chemins', '6 differentes, TOUTES des chemins', 'six chemins')):
    chk('%-32s %s' % (etq, s_acte), s_src in MREJ and s_acte in ACTE, s_src)
LAS = source('assemblage re-livraison v2 .log', ('ACTE_constante_A', 'assemblage_relivraison_machine2_v2.log'), 'd08c1d1999a6cd08')
cite('re-livraison 158 pieces', '158 pieces', src=LAS)
NC = source('note m1 cause de l ecart (lot 117bcfaa1f283059)', ('entrant_machine1_2026-09-12_cause_ecart', 'lot', 'note_machine1_cause_ecart_7_1p73_v1.md'),
            canon_de_table(('entrant_machine1_2026-09-12_cause_ecart', 'lot', 'MANIFEST_lot_machine1_cause_ecart_7_1p73_v1.txt'), 'note_machine1_cause_ecart'))
for etq, txt in (('5.2 a 5.5 pour cent', '5.2 a 5.5 pour cent'), ('1, 2, 2, 0', '1, 2, 2, 0'), ('44 grandeurs de flot', '44'),
                 ('temoin x', '1765.6704444885254'), ('pas 707 sur 760', 'pas 707 sur 760'), ('633 a dt2/8', '633'),
                 ('X86_V4', 'X86_V4'), ('...9c5', '9c5'), ('...9c6', '9c6'), ('numpy 2.2.6 sur BOCAL4', '2.2.6')):
    cite('%-32s %s' % (etq, txt), txt, src=NC)
chk('numpy 2.4.4 sur machine 1', 'numpy 2.4.4' in NC and '2.4.4' in ACTE, '2.4.4')
N70 = source('N-70 v2', ('chaine_constante_A_pour_machine1', 'enumeration_cles_prevol_N70_machine2_v2.md'), '4867dffe3392dea6')
for etq, s_src, s_acte in (('245 au run', '**245**', '245'), ('238 identiques', 'PREDITES IDENTIQUES ....... 238', '238 predites identiques'),
                           ('2 absentes', 'PREDITES ABSENTES** ..... 2', '2 predites absentes'), ('16 groupes', '16 groupes', '16 groupes sur 16')):
    chk('%-32s %s' % (etq, s_acte), s_src in N70 and s_acte in ACTE, s_src)
N70v1 = source('N-70 v1', ('enumeration_cles_prevol_N70_machine2_v1.md',), '4ef8235b16f26210')
cite('247 cles a la v1', '247', src=N70v1)
C5 = source('certification v5 (m2)', ('certification_constante_A_v5', 'CERTIFICATION_machine2_constante_A_v5_v1.md'), 'df0431a0a57cc2b6')
cite('104 controles, 104 passent, 0 mord', '104 controles, 104 passent, 0 mord', src=C5)
C4 = source('certification v4 (m2)', ('note_machine2_certification_constante_A_v4_v1.md',), '9e6376f936708077')
chk('96 controles, 95 passent, 1 mord (v4), P-A-1', '96 controles, 95 passent, 1 mord' in C4 and 'P-A-1' in C4
    and '96 controles, 95 passent, 1 MORD' in ACTE, 'P-A-1')
V8 = source('note controle v8 (m2)', ('chaine_constante_A_pour_machine1', 'note_machine2_controle_instrument_v8_v1.md'), '2a618ffb180ea568')
chk('VERDICT CERTIFIEE (v8), selftest 103/103', 'VERDICT : CERTIFIEE.' in V8 and '103/103' in V8
    and 'VERDICT CERTIFIEE ; selftest 103/103' in ACTE, 'v8')
T11 = source('certification temoin v11 (m1)', ('note_machine1_certification_temoin_v11_v2.md',), '7fc5f2412b99ad50')
chk('VERDICT CERTIFIEE (v11), gel a2e7ef3e237c5acf', 'CERTIFIEE' in T11 and 'a2e7ef3e237c5acf' in T11 and 'GEL DU VOLET T' in ACTE, 'v11')
LV5 = source('note livraison v5 (m1)', ('note_machine1_livraison_banc_v5_v1.md',), 'be633ae91ae295b5')
chk('53 remplacements v3 -> v4, 24 remplacements Q01..Q24', '53 rempl' in LV5 and '24 remplacements' in LV5 and 'Q01..Q24' in LV5
    and '53\n      remplacements' in ACTE and 'Q01..Q24' in ACTE, '53 / 24')
LS = source('surface d exposition du registre .log', ('G3_reponse', 'surface_exposition_registre_machine2_v1.log'), '9c707ac4260c3e0a')
chk('34 logs deposes, 0 niveau de dispatch', 'niveau de dispatch     : 0' in LS and '34' in LS and '34 logs deposes' in ACTE, '34 / 0')
S29 = source('SUIVI 29a (m1)', ('SUIVI_campagne_2026-08-29a.md',), 'd0747b01700e4ad8')
chk('neuf defauts D-I-1..9 tous leves (SUIVI 29a)', 'D-I-1..9 tous LEVES' in S29 and 'Neuf\n      defauts D-I-1 a D-I-9 ont ete leves' in ACTE, 'D-I-1..9')

# =====================================================================
print('\n4. LES COMPTES DE L ACTE SUR LUI-MEME')
# =====================================================================
def bloc(a, b):
    i, j = ACTE.index(a), ACTE.index(b)
    return ACTE[i:j]


tours = set(re.findall(r'\b[0-9a-f]{16}\b', bloc('  Les trois tours du 12/09', '  La re-livraison du fond')))
lots_tours = [t for t in ('e3b707c589e9d1d8', '56378e0f371f9681', '1985ad4eea984bf5', '5c84c48e9a9c72eb',
                          'b228e0f5a0197494', '25b6f78bdf2ddcff', '990a8fe5cec6ef87') if t in tours]
chk('sept lots sur l acte le 12/09', len(lots_tours) == 7 and 'Sept lots echanges le 12/09' in ACTE, '%d' % len(lots_tours))
g2 = bloc('  Le geste (2) -- convergence', '  Les trois tours du 12/09')
lots_g2 = [t for t in ('2b155abffbe4f6ff', '117bcfaa1f283059', '5ea2fa8d7457a125', 'ca5456d3b11df0be', '4cb991ce22ca35d0',
                       '1859bbc126bb52c7', 'eb7fb1cefbf2cec4', 'f9e1c1922e32220d', '3675daba802cbc6c', '7883311c6e363b02',
                       'cd70cda556d60380') if t in g2]
chk('onze lots sur le geste (2)', len(lots_g2) == 11 and 'onze sur le geste (2)' in ACTE, '%d' % len(lots_g2))
chk('huit regles candidates en nn.8', len(re.findall(r'^  \d\. ', bloc('nn.8 REGLES', 'nn.9 A ARBITRER'), re.M)) == 8
    and 'HUIT REGLES CANDIDATES' in ACTE, '8')
defs = ' '.join(re.findall(r'^  (D-ACA-\d|D-G2-\d(?:, D-G2-\d)?|D-I-3|D-v5-1)\s', bloc('nn.7 DEFAUTS', 'nn.8 REGLES'), re.M))
n_num = len(set(re.findall(r'D-ACA-\d', defs))) + len(set(re.findall(r'D-G2-\d', defs)))
chk('onze defauts numerotes D-ACA-1..7 et D-G2-1..4', n_num == 11 and 'ONZE DEFAUTS' in ACTE, '%d' % n_num)
chk('trois errata en nn.6', len(re.findall(r'^  \(\d\) ', bloc('nn.6 LES TROIS', 'nn.7 DEFAUTS'), re.M)) == 3
    and 'TROIS\nERRATA' in ACTE, '3')
chk('les sept points de nn.9 sont numerotes (i) a (vii)',
    re.findall(r'^  \((i{1,3}|iv|v|vi|vii)\)', bloc('nn.9 A ARBITRER', 'nn.10 CONSEQUENCES'), re.M)
    == ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii'], '7')
raw = open(os.path.join(ICI, 'journal_delta_nn_constante_A_v1.md'), 'rb').read()
larg = max(len(l) for l in raw.split(b'\n'))
chk('l acte est ASCII, LF, newline final, largeur <= 90', all(b < 128 for b in raw) and b'\r' not in raw
    and raw.endswith(b'\n') and larg <= 90, '%d octets, largeur max %d' % (len(raw), larg))

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN RELECTURE : %d/%d controles PASSENT' % (k, n))
print('=====================================================================')
sys.exit(0 if k == n else 1)
