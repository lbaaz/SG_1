#!/usr/bin/env python3
# -*- coding: ascii -*-
"""RELECTURE DES NOMBRES DE LA FEUILLE DE LECTURE. machine 2, 12/09/2026.

La feuille de LECTURE (`DOSSIER_ARBITRAGE_constante_A_operateur_v1.md`) cite des nombres
et des empreintes. Cette feuille de MESURE les recalcule A LA SOURCE et verifie qu'ils
sont LITTERALEMENT dans la note.

DEUX JAMBES, ET IL EN FAUT DEUX :
  (1) le nombre recalcule depuis la source vaut ce que la note annonce ;
  (2) la chaine annoncee est PRESENTE dans la note, telle quelle.
La jambe (2) seule laisserait passer un nombre juste mais absent ; la jambe (1) seule
laisserait passer une faute de FRAPPE dans la note. L'issue qui ferait mordre est
ecrivable dans les deux cas : changer un chiffre de la note, ou changer une source.

Aucune source n'est editee (PB-1).
"""
import hashlib, json, os, unicodedata
from fractions import Fraction as F

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
P = lambda *a: os.path.join(RAC, *a)
NOTE = open(os.path.join(ICI, 'DOSSIER_ARBITRAGE_constante_A_operateur_v1.md'),
            encoding='utf-8').read()
LOG = open(os.path.join(ICI, 'derivation_fenetre_delta_machine2_v2.log'),
           encoding='utf-8', errors='replace').read()
OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-52s %s' % ('PASSE' if c else 'MORD ', n[:52], d))


def cite(etq, txt, valeur=None, attendu=None):
    """(2) la chaine est dans la note ; (1) si un couple est donne, il concorde."""
    dans = txt in NOTE
    bon = True if valeur is None else (valeur == attendu)
    chk(etq, dans and bon, '%s%s' % ('' if dans else 'ABSENTE DE LA NOTE ; ',
                                     'recalcul %r vs annonce %r' % (valeur, attendu)
                                     if valeur is not None else txt))


def canon(p):
    raw = open(p, 'rb').read()
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8'))
        t = t.replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
        return hashlib.sha256(t).hexdigest()[:16]
    except UnicodeDecodeError:
        return hashlib.sha256(raw).hexdigest()[:16]


def pts(*a):
    return json.load(open(P(*a), encoding='utf-8'))['T2']['points']


# =====================================================================
print("\n1. LES CINQ EMPREINTES DU DOSSIER -- RECALCULEES, PAS CITEES")
# =====================================================================
SOURCES = (
    ('gel v5, le LOT', 'd5ace962a3a6e413',
     ('entrant_machine1_2026-09-09_constante_A_v5',
      'MANIFEST_lot_machine1_constante_A_v5.txt')),
    ('gel v5, le FICHIER (GEL COURANT)', '2c0d2dc86054838c',
     ('entrant_machine1_2026-09-09_constante_A_v5',
      'constante_A_pre_enregistrement_v5.md')),
    ('ma certification du v5', '13d2973b0e143a20',
     ('certification_constante_A_v5',
      'MANIFEST_lot_machine2_certification_constante_A_v5_v1.txt')),
    ('la chaine, 8 pieces', 'a4c35a2ee691c9a7',
     ('chaine_constante_A_pour_machine1',
      'MANIFEST_lot_machine2_chaine_constante_A_v1.txt')),
    ('le lot qui porte la tenaille v1', '7883311c6e363b02',
     ('G4_trois', 'MANIFEST_lot_machine2_comparaison_a_trois_v1.txt')),
)
for etq, emp, chemin in SOURCES:
    c = canon(P(*chemin))
    chk('%-34s %s' % (etq, emp), c == emp and emp in NOTE,
        '%s  %s' % (c, os.path.join(*chemin)))

# =====================================================================
print("\n2. LA BORNE ET LA FENETRE -- RELUES DANS LE LOG DE LA FEUILLE DE MESURE")
# =====================================================================
for etq, txt in (('INF pleine precision', '1.659260768e-05'),
                 ('INF v1, depuis le log', '1.659725811e-05'),
                 ('borne superieure a m=2', '1.728646463e-05'),
                 ('lecture NOYAU', '1.286193025e-05'),
                 ('lecture LIBM et la mienne', '1.427322916e-05'),
                 ('ecart JSON/log', '2.8027e-04'),
                 ('marge de la fenetre', '4.1817e-02'),
                 ('empreinte bit de INF sous mutation', '3ef1660b5147653b'),
                 ('lecture NOYAU mutee', '4.287310084e-06'),
                 ('fenetre a m=2, kT=1', 'x1.0418'),
                 ('fenetre a m=1, kT=1', 'x2.0836'),
                 ('bilan de la feuille de mesure', '21/21')):
    chk('%-38s %s' % (etq, txt), txt in NOTE and txt in LOG,
        ('note %s ; log %s' % ('oui' if txt in NOTE else 'NON',
                               'oui' if txt in LOG else 'NON')))

# =====================================================================
print("\n3. LE PORTEUR ET LES SIX CELLULES -- RELUS DANS LES JSON")
# =====================================================================
MOI = pts('m2_v8_prevol_temoin_resultats.json')
NOY = pts('entrant_machine1_2026-09-12_reponse_globale', 'lot',
          'resultats_temoin_prevol_noyau_machine1.json')
LIB = pts('entrant_machine1_2026-09-12_reponse_globale', 'lot',
          'resultats_temoin_prevol_libm_machine1.json')
# La note imprime le ratio au format `%.17g`, celui de la feuille de mesure. `repr()`
# rendrait l'ecriture courte du meme double : deux RENDUS, un seul nombre. On compare
# donc au rendu annonce, ET on verifie que la chaine de la note relit bien le double.
POR = MOI['7|1.73']['ratio_seuil']
cite('le ratio du porteur 7|1.73, au format de la note',
     '0.68419170555697806', '%.17g' % POR, '0.68419170555697806')
chk('et la chaine de la note relit le double AU BIT',
    float('0.68419170555697806') == POR, '%.17g' % POR)
dif = sorted(k for k in MOI if MOI[k]['ratio_seuil'] != NOY[k]['ratio_seuil'])
chk('SIX cellules different au bit, et la note dit six', len(dif) == 6
    and 'Au bit elles sont SIX' in NOTE, ','.join(dif))
dif3 = sorted(k for k in MOI if '%.3f' % MOI[k]['ratio_seuil']
              != '%.3f' % NOY[k]['ratio_seuil'])
chk('TROIS a la resolution du journal', len(dif3) == 3, ','.join(dif3))
chk('mes ratios == son LIBM au bit (9/9)',
    all(MOI[k]['ratio_seuil'] == LIB[k]['ratio_seuil'] for k in MOI), '0 ecart')
for k in dif:
    t = '%.17g' % MOI[k]['ratio_seuil']
    chk('la note porte la valeur de %s' % k, t in NOTE, t)
lues = sorted(k for k in dif if MOI[k]['W_plancher'] != 'MORD')
chk('quatre des six sont LUES, et la note dit quatre',
    len(lues) == 4 and 'dont quatre LUES' in NOTE, ','.join(lues))

# =====================================================================
print("\n4. LA PORTE ET LE REGLAGE")
# =====================================================================
DP = float(F(1, 102400))
cite('delta-prime', '9.765625e-06', '%.6e' % DP, '9.765625e-06')
cite('delta-prime / INF', '0.589', '%.3f' % (DP / 1.659260768e-05), '0.589')
chk('la note dit que le pre-vol rend branche 4',
    'branche 4' in NOTE and 'branche 5' in NOTE, 'porte inchangee')

# =====================================================================
print("\n5. N-70 -- LA VALEUR DEPOSEE, RELUE AU REGISTRE")
# =====================================================================
REF = json.load(open(P('registre', 'runs', 'run_temoin_delta85', 'resultats_temoin.json'),
                     encoding='utf-8'))
tol = sorted({repr(v) for c in (REF['T1']['A']['W_integrales'], REF['T3a']['A'])
              for k, v in c.items() if k.startswith('tol_int')})
chk('les cles tol_int du run depose portent UNE seule valeur', len(tol) == 1,
    ','.join(tol))
cite('et c est la valeur machine 2', '0.008578984888782988', tol[0],
     '0.008578984888782988')

# =====================================================================
print("\n6. LA PIECE DE LA DECISION (v) -- ABSENTE, ET CITEE AU GEL COURANT")
# =====================================================================
gel = open(P('entrant_machine1_2026-09-09_constante_A_v5',
             'constante_A_pre_enregistrement_v5.md'), encoding='utf-8').read()
chk('SUIVI_campagne_2026-08-28b est cite au GEL COURANT (v5)',
    'SUIVI_campagne_2026-08-28b.md' in gel and 'b6d13e6a1559e850' in gel,
    'b6d13e6a1559e850')
cherches = [P('SUIVI_campagne_2026-08-28b.md'),
            os.path.join(os.path.expanduser('~'), 'Downloads',
                         'SUIVI_campagne_2026-08-28b.md')]
absents = [c for c in cherches if not os.path.exists(c)]
chk('et il est ABSENT des deux emplacements cherches', len(absents) == 2,
    ' ; '.join(absents))
chk('la note le declare INTROUVABLE', 'INTROUVABLE -- cite au gel v5' in NOTE,
    'decision (v) non tranchable')

# =====================================================================
print("\n7. FORME DES DEUX PIECES DE CE LOT")
# =====================================================================
for nom in ('DOSSIER_ARBITRAGE_constante_A_operateur_v1.md',
            'derivation_fenetre_delta_machine2_v2.py'):
    raw = open(os.path.join(ICI, nom), 'rb').read()
    chk('%-46s ASCII pur' % nom, all(c < 128 for c in raw),
        '%d octets' % len(raw))

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN RELECTURE : %d/%d controles PASSENT' % (k, n))
print('=====================================================================')
