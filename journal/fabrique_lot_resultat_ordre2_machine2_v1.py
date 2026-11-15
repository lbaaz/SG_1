# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'resultat du run du gel la chaine E-A au second ordre' (41153158190cf7f1) -- manifeste + ZIP. 2026-11-15.
Usage : python -P fabrique_lot_resultat_ordre2_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; les chiffres cles de la note (heures, code, duree, verdict, bandes, comparaison, energies, ecarts de ma lecture et de mon
lecteur independant, ancres au bit, sensibilite au bruit, defaut de la v1, annonces, batterie) RELUS dans le JSON du verdict et dans les journaux ; le JSON de la sonde
porte 16 points de 14 etats, la sonde 24315c52b234319c et le moteur 82a0be882568fe0c ; les canons des pieces recalcules et ecrits dans la section des pieces de la
note (gabarit @@PIECES@@) ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'ordre2/'
SO = D + 'sortie/'
NOM = 'lot_machine2_2026-11-15_resultat_ordre2_chaine_EA_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_resultat_ordre2_chaine_EA_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_resultat_ordre2_machine2_v1.md'
SELF = 'fabrique_lot_resultat_ordre2_machine2_v1.py'
PIECES = [SO + x for x in ('console_ordre2.log', 'sonde_ordre2.log', 'sonde_ordre2.json', 'lecture_ordre2.log', 'verdict_ordre2.json',
                           'lecture_resultat_machine2.log', 'relecture_independante_machine2.log', 'compare_run_essai_ancres_machine2.log',
                           'stabilite_cascade_machine2.log', 'sensibilite_bruit_machine2.log', 'stabilite_cascade_machine2_v1_defaut.log',
                           'etat_machine_machine2.log')] + [D + 'stabilite_cascade_machine2_v2.py'] + [SELF]
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


for p in PIECES + [NOTE]:
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
# le JSON de la sonde et le verdict
S = json.load(open(os.path.join(ICI, SO + 'sonde_ordre2.json'), encoding='ascii'))
V = json.load(open(os.path.join(ICI, SO + 'verdict_ordre2.json'), encoding='ascii'))
if not (len(S['points']) == 16 and all(len(p['etats']) == 14 for p in S['points']) and S['sonde_canon'] == '24315c52b234319c' and S['moteur_canon'] == '82a0be882568fe0c'):
    arrets.append('JSON de la sonde : 16 points de 14 etats, sonde, moteur')
if not (V['verdict'] == "L'ORDRE 2 TIENT" and V['verdict_sans_marge'] == "L'ORDRE 2 TIENT" and V['motifs'] == [] and V['gardes_par_la_marge'] == []
        and all(V['bandes'][b]['issue'] == 'TENUE' and V['bandes'][b]['lisibles'] == 4 and V['bandes'][b]['tombes'] == [] for b in ('proche', 'moyenne', 'lointaine'))
        and V['comparaison']['issue'] == "L'ORDRE 2 FAIT MIEUX PARTOUT" and V['comparaison']['lisibles'] == 12 and V['comparaison']['pas_mieux'] == []
        and V['energie']['issue'] == "L'ENERGIE TIENT" and V['energie']['lisibles'] == 12 and V['energie']['non_tenue'] == []):
    arrets.append('verdict : %s' % V['verdict'])
cl = lit(SO + 'console_ordre2.log')
for x in ('2026-11-14 23:26:01 LANCEMENT DE LA SONDE', '2026-11-15 00:41:24 FIN DE LA SONDE code=0 duree=4524 s', 'FIN DE LA FEUILLE code=0'):
    if x not in cl:
        arrets.append('console : %r absent' % x)
if 'FIN : 16 points' not in lit(SO + 'sonde_ordre2.log'):
    arrets.append('journal de la sonde : FIN : 16 points absent')
ll = lit(SO + 'lecture_ordre2.log')
for x in ('SELFTEST : 160 cas, 160 tenus', "VERDICT : L'ORDRE 2 TIENT", "COMPARAISON au pire etat : L'ORDRE 2 FAIT MIEUX PARTOUT (12 lisibles ; pas mieux : aucun)",
          "ENERGIES : L'ENERGIE TIENT (12 lisibles ; non tenue : aucun)", 'W2 temoin w2=209/100 x1/2 hors enonce               : NON LISIBLE (moins de 6 etats juges), 3 etats juges'):
    if x not in ll:
        arrets.append('lecture : %r absent' % x)
rl = lit(SO + 'lecture_resultat_machine2.log')
for x in ('BILAN DE MA LECTURE : 0 ecart(s)', 'A-11 (0.60)', 'A-13 (0.65) W2 est joue et lisible : FAUSSE', 'A-9b (0.70) le plus grand ecart d energie des points juges est < 0.006 : VRAIE (0.0046, au point L1)'):
    if x not in rl:
        arrets.append('ma lecture : %r absent' % x)
if len(re.findall(r': VRAIE', rl)) != 18 or len(re.findall(r': FAUSSE', rl)) != 2:
    arrets.append('ma lecture : comptes des annonces (VRAIE %d, FAUSSE %d)' % (len(re.findall(r': VRAIE', rl)), len(re.findall(r': FAUSSE', rl))))
ri = lit(SO + 'relecture_independante_machine2.log')
if 'ECARTS ENTRE MON LECTEUR ET LA FEUILLE : 0 []' not in ri:
    arrets.append('relecture independante : ecarts')
cp = lit(SO + 'compare_run_essai_ancres_machine2.log')
if 'BILAN : 28 etats, 0 etiquettes differentes ; ecart absolu max de Gamma_2D (k = 2, 3, 4) 0.00e+00 ; relatif max 0.00e+00 ; relatif max au-dessus de 1e-10 0.00e+00 ; chaine : ecart relatif max 0.00e+00' not in cp:
    arrets.append('ancres : bilan')
sc = lit(SO + 'stabilite_cascade_machine2.log')
sb = lit(SO + 'sensibilite_bruit_machine2.log')
s1 = lit(SO + 'stabilite_cascade_machine2_v1_defaut.log')
if not ('VERDICT INCHANGE' in sc and "verdicts possibles sous le bruit : [\"L'ORDRE 2 TIENT\"]" in sc and 'PEUT CHANGER' not in sc.split('verdicts possibles')[0]):
    arrets.append('stabilite v2 au bruit mesure')
sens = {}
for l in sb.split('\n'):
    m = re.match(r'x(\d+)\s+\(bruit [0-9.e+-]+\) : .*VERDICT (INCHANGE|PEUT CHANGER)', l)
    if m:
        sens[int(m.group(1))] = m.group(2)
if not (all(sens.get(k) == 'INCHANGE' for k in range(1, 8)) and all(sens.get(k) == 'PEUT CHANGER' for k in (8, 9, 10, 30))):
    arrets.append('sensibilite : %s' % sens)
if 'verdicts possibles sous le bruit : [] ' not in s1 or 'VERDICT PEUT CHANGER' not in s1 or 'M3 bande moyenne   statut TENU  ; possibles sous le bruit []' not in s1:
    arrets.append('defaut de la v1')
em = lit(SO + 'etat_machine_machine2.log')
if 'BatteryStatus 1' not in em or '62 pour cent' not in em or 'CurrentClockSpeed 2516 MHz ; MaxClockSpeed 3801 MHz' not in em:
    arrets.append('etat de la machine')
for x in ('4524 s', "L'ORDRE 2 TIENT", '160 sur 160', '2516 MHz', '100 pour cent', '62 pour cent', 'BATTERIE', '59a583a640112891', 'SEPT FOIS', 'Dix-huit sur vingt',
          'A-11 et A-13', '1346 s', '23:26:01', '00:41:24', 'DEFAUT DE MON OUTIL', '1.679', '1.447', '1.136'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    "MANIFESTE %s -- RESULTAT DU RUN DE MACHINE 2 DU GEL LA CHAINE E-A AU SECOND ORDRE (41153158190cf7f1 ; sonde 24315c52b234319c ; feuille "
    "0dc8241c680eb1ff ; certification 59a583a640112891) : 16 points, un seul run ; verdict de la feuille L'ORDRE 2 TIENT (trois bandes TENUES, FAIT MIEUX PARTOUT, "
    "L'ENERGIE TIENT), W2 NON LISIBLE ; ma lecture ecrite avant le run et mon lecteur independant : 0 ecart. machine 2, classe B\n" % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : mon lot de certification 59a583a640112891 ; le lot de machine 1 3bc363266957de56\n')
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
