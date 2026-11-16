# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'certification de la seconde partie du gel loi de la largeur, ordre 3' -- manifeste + ZIP. 2026-11-16. Meme squelette que fabrique_lot_tirage_graine_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_certification_gel_loi_partie2_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; MES journaux LUS (authentification 64/64 ; table 7/7 ; reconstruction 16/16 ; banc ter sur la feuille derivee 43/43 ; confrontation 40 + 12 essais sans difference ;
sensibilite 27 tuees / 8 survivantes ; constantes 31/31 ; banc rejoue 17/17 ; verification des nombres : seul N11N mord ; contre-epreuve 14/14 ; essai NON LU 5/5 ; pre-vol 5/5, ancres tenues, pilote v2 au canon dit) ;
les canons du lot de machine 1, de son gel, de son pilote et du mien recalcules ; note ASCII ; les canons de CHAQUE piece nommes dans la note ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-16_certification_gel_loi_partie2_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_loi_partie2_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_loi_partie2_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_loi_partie2_machine2_v1.py'
D = 'certif_gel_loi_partie2_machine2/'
PRE = D + 'prevol/'
LOT1 = 'livraison_16a_gel_loi_partie2/ext/lot_m1/'
NOMS_D = ['authentifie_lot_partie2_machine2_v1.py', 'authentifie_lot_partie2_machine2_v1.log',
          'verif_table_machine2_v1.py', 'verif_table_machine2_v1.log', 'verif_table_machine2_v1_premier_passage.log',
          'reconstruction_derives_machine2_v1.py', 'reconstruction_derives_machine2_v1.log',
          'banc_ter_sur_feuille_derivee_machine2_v1.log', 'selftest_feuille_lecteur_derivee_machine2_v1.log',
          'essai_non_lu_machine2_v1.py', 'essai_non_lu_machine2_v1.log', 'essai_non_lu_machine2_v1_premier_passage.log',
          'feuille_independante_gel_loi_machine2_v1.py', 'retro_machine2_v1.json', 'retro_machine2_v1.log', 'compare_retro_machine2_v1.py', 'compare_retro_machine2_v1.log',
          'confrontation_feuilles_gel_loi_machine2_v1.py', 'confrontation_feuilles_gel_loi_machine2_v1.log', 'confrontation_feuilles_gel_loi_machine2_v1.json',
          'confrontation_limites_gel_loi_machine2_v1.py', 'confrontation_limites_gel_loi_machine2_v1.log', 'confrontation_limites_gel_loi_machine2_v1.json',
          'sensibilite_confrontation_machine2_v1.py', 'sensibilite_confrontation_machine2_v1.log', 'sensibilite_confrontation_machine2_v1.json',
          'sensibilite_limites_machine2_v1.log', 'sensibilite_limites_machine2_v1.json', 'sensibilite_union_machine2_v1.log',
          'constantes_feuille_machine2_v1.py', 'constantes_feuille_machine2_v1.log',
          'banc_feuille_ordre3_machine1_derive_P.py', 'banc_feuille_ordre3_rejoue_machine2_v1.log', 'banc_feuille_ordre3_rejoue_machine2_v1.json',
          'verification_nombres_gel_machine2_v1.py', 'verification_nombres_gel_machine2_v1.log', 'verification_nombres_gel_machine2_v1.json',
          'verification_nombres_gel_machine2_v1_premier_jet.py', 'verification_nombres_gel_machine2_v1_premier_passage.log', 'verification_nombres_gel_machine2_v1_second_passage.log',
          'verification_nombres_gel_machine2_v1_troisieme_passage.log',
          'contre_epreuve_nombres_gel_machine2_v1.py', 'contre_epreuve_nombres_gel_machine2_v1.log', 'contre_epreuve_nombres_gel_machine2_v1.json',
          'contre_epreuve_nombres_gel_machine2_v1_premier_passage_invalide.log',
          'dense_rejoue_C3_A1_A2_machine2.log', 'dense_rejoue_C3_A1_A2_machine2.json', 'ancres_dense_rejoue_machine2_v1.py', 'ancres_dense_rejoue_machine2_v1.log',
          'derive_pilote_machine2_v1.py', 'pilote_gel_loi_machine2_v1_premier_jet.diff', 'derive_pilote_machine2_v2.py', 'pilote_gel_loi_machine2_v2.py', 'pilote_gel_loi_machine2_v2.diff',
          'lancer_prevol.sh', 'comparaison_prevol_machine2_v1.log', 'comparaison_prevol_machine2_v1.json',
          'lancer_run_gel_loi_machine2_v1.py', 'lancer_verifs_nombres.sh']
PRE_NOMS = ['pilote_gel_loi.log', 'console_etage0.log', 'console_ancres.log', 'console_etage1.log', 'console_point_C3.log', 'lecture_ter_instrument.console.log', 'lecture_ter_instrument.log',
            'lecture_ter.console.log', 'lecture_ter.log', 'feuille_ordre3.log', 'sonde_ter_etage0.json', 'sonde_ter_ancres.json', 'sonde_ter_etage1.json', 'sonde_ter_point_C3.json',
            'verdict_ter_instrument.json', 'verdict_ter.json', 'verdict_ordre3.json']
PIECES = [D + x for x in NOMS_D] + [PRE + x for x in PRE_NOMS] + [D + 'prevol_abandonne_pilote_v1/pilote_gel_loi.log', SELF]
CITES = ((LOT1 + 'gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1.md', '543d8b33e5c9afb8'), (LOT1 + 'pilote_gel_loi_machine1_v1.py', '2882de31bc49ce2f'),
         (D + 'pilote_gel_loi_machine2_v2.py', '15998497f3422765'), (LOT1 + 'feuille_ordre3_machine1_v1.py', 'facd3ceeec07d3bf'))
arrets = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def lit(p):
    return open(os.path.join(ICI, p), encoding='utf-8', errors='replace').read()


for p in PIECES + [NOTE] + [c[0] for c in CITES]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

note = lit(NOTE)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append('la note n est pas ASCII')
nn = re.sub(r'\s+', ' ', note)
# --- mes journaux, lus ---
for nom, chem, xs in (
        ('authentification', D + 'authentifie_lot_partie2_machine2_v1.log', ('CANON du manifeste : 76ed746ef4db3b0c', 'pieces du zip : 64', 'MORSURES : 0')),
        ('table', D + 'verif_table_machine2_v1.log', ('BILAN : 7 controles, 7 tiennent',)),
        ('reconstruction', D + 'reconstruction_derives_machine2_v1.log', ('BILAN : 16 controles, 16 tiennent',)),
        ('banc ter', D + 'banc_ter_sur_feuille_derivee_machine2_v1.log', ('BANC : 43 alterations, 43 mordues, 0 survivantes [], 0 cibles refusees [] ; base saine : True',)),
        ('selftest', D + 'selftest_feuille_lecteur_derivee_machine2_v1.log', ('selftest : 68 tenus sur 68',)),
        ('retro', D + 'compare_retro_machine2_v1.log', ('etats juges compares : 131 (dont 56 dans le domaine)', "differences de cellule ou d'issue : 0 []", "differences d'etat (exclusion, domaine) : 0 []")),
        ('confrontation', D + 'confrontation_feuilles_gel_loi_machine2_v1.log', ('BILAN : 40 essais, 0 avec une difference ; cellules 480',)),
        ('limites', D + 'confrontation_limites_gel_loi_machine2_v1.log', ('BILAN : 12 essais, 0 avec une difference ; cellules 144',)),
        ('sensibilite', D + 'sensibilite_union_machine2_v1.log', ('35 mutations de ma feuille ; tuees par l un ou l autre jeu : 27 ; survivantes aux deux : 8',)),
        ('constantes', D + 'constantes_feuille_machine2_v1.log', ('BILAN : 31 controles, 31 tiennent',)),
        ('banc rejoue', D + 'banc_feuille_ordre3_rejoue_machine2_v1.log', ("BANC DE LA FEUILLE D'ORDRE 3 : 17 mutations, 17 mordent comme attendu : TIENT",)),
        ('nombres', D + 'verification_nombres_gel_machine2_v1.log', ('BILAN : 13 controles, 12 tiennent', 'N11N  MORD', 'N01   TIENT', 'N08   TIENT', 'N12   TIENT')),
        ('contre-epreuve', D + 'contre_epreuve_nombres_gel_machine2_v1.log', ('CONTRE-EPREUVE : 14 corruptions, 14 mordues comme attendu',)),
        ('non lu', D + 'essai_non_lu_machine2_v1.log', ('BILAN : 5 controles, 5 tiennent', "etat_lu du point C3 : 'NON LU'")),
        ('ancres', D + 'ancres_dense_rejoue_machine2_v1.log', ('TIENNENT', 'ecart relatif maximal de Gamma_2D(3) au-dessus de dix planchers 0.00e+00')),
        ('comparaison pre-vol', D + 'comparaison_prevol_machine2_v1.log', ('PRE-VOL : 5 controles, 5 tiennent', 'pire ecart relatif 0.0e+00 (tolerance 1e-6)', 'pire ecart relatif de Gamma_2D(3) au-dessus de dix planchers 0.0e+00')),
        ('pilote du pre-vol', PRE + 'pilote_gel_loi.log', ('pilote pilote_gel_loi_machine2_v2.py canon 15998497f3422765', 'INSTRUMENT DU LECTEUR : TIENT', 'FIN DU PILOTE ; duree totale 2206 s'))):
    t = lit(chem)
    for x in xs:
        if x not in t:
            arrets.append('journal %s : %r absent' % (nom, x))
t = lit(D + 'verification_nombres_gel_machine2_v1.log')
mordus = sorted(set(l.split()[0] for l in t.split('\n') if len(l.split()) > 1 and l.split()[1] == 'MORD'))
if mordus != ['N11N']:
    arrets.append('verification des nombres : controles qui mordent %s (attendu : N11N seul)' % mordus)
for x in ('76ed746ef4db3b0c', '543d8b33e5c9afb8', '2882de31bc49ce2f', '15998497f3422765', '624 cellules', '2206 s', '0.16338', '0.163', '0.164', 'O-1', 'R-1', 'R-2', 'R-3', 'R-4', 'M-1', 'M-11', 'E-2', 'E19',
          'Tu peux considerer que tu as mon feu vert pour lancer', 'si et seulement si la', 'N11N', 'K18', 'SetThreadExecutionState', 'site utilisateur', 'run_gel_loi_ordre3'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
for p, att in CITES:
    c = emp(open(os.path.join(ICI, p), 'rb').read())[0]
    if c != att:
        arrets.append('canon de %s : %s, attendu %s' % (p, c, att))
mp1 = os.path.join(ICI, 'livraison_16a_gel_loi_partie2/ext/MANIFEST_lot_machine1_gel_loi_partie2_instrument_enonces_v1.txt')
if emp(open(mp1, 'rb').read())[0] != '76ed746ef4db3b0c':
    arrets.append('le lot de machine 1 n a plus le canon 76ed746ef4db3b0c')
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CERTIFICATION PAR MACHINE 2 DE LA SECONDE PARTIE DU GEL "LOI DE LA LARGEUR, ORDRE 3" (543d8b33e5c9afb8, lot de machine 1 76ed746ef4db3b0c) : aucune morsure d instrument, une morsure de description '
    '(O-1), quatre reserves sans correction ; pre-vol sur BOCAL4 5 sur 5 ; pilote derive pour BOCAL4. Aucune largeur 2D aux cellules. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : gel 543d8b33e5c9afb8 ; lot de machine 1 76ed746ef4db3b0c ; mon tirage 220a0970134335e1 ; ma certification de la premiere partie 4fb1dc66f96f57f6 ; le feu vert ecrit de l operateur (session du 16/11)\n')
lignes.append('pieces : %d (compte etabli APRES le dernier ajout)\n' % (len(PIECES) + 1))
with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lignes)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(MAN, os.path.basename(MAN))
    for p in [NOTE] + PIECES:
        z.write(os.path.join(ICI, p), p)
with zipfile.ZipFile(ZIP) as z:
    attendu = {os.path.basename(MAN): open(MAN, 'rb').read()}
    for p in [NOTE] + PIECES:
        attendu[p] = open(os.path.join(ICI, p), 'rb').read()
    mauvais = [n for n in z.namelist() if z.read(n) != attendu.get(n)]
    manque = sorted(set(attendu) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)
print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP)))
