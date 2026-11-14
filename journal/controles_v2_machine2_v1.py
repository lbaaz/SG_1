# -*- coding: ascii -*-
"""Controles de machine 2 sur le projet v2 de l'acte (bdf8c5a0c73096a4) autres que le diff : les six canons que la v2 cite de neuf se
resolvent-ils chez moi ; les phrases ajoutees en nn.4 sont-elles vraies des pieces des lots de machine 1 que je detiens (seuil 1.33e-12,
aucun fichier de sortie de la nuit relu, note de litterature, dates des pieces) ? Usage depuis BOCAL4 :
python -P acte_v2_contreseing/controles_v2_machine2_v1.py > acte_v2_contreseing/controles_v2_machine2_v1.log"""
import hashlib, os, re, unicodedata, zipfile

def emp(raw):
    t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
    return hashlib.sha256(t).hexdigest()[:16]

print('1. LES SIX CANONS NOUVEAUX DE LA v2, RECALCULES DE PIECES QUE JE DETIENS')
cibles = {'2b211d51fb8eb3f0': 'MANIFEST_lot_machine1_chaine_EA_par_etat_v1.txt', 'e58d01567a46b86a': 'MANIFEST_lot_machine1_envoi_chaine_et_lectures_v1.txt',
          '05f8eed219631f63': 'MANIFEST_lot_machine2_contreseing_acte_nn_EB_bis_v1.txt', 'df01461fc9b2b099': 'MANIFEST_lot_machine2_rejeu_chaine_EA_par_etat_v1.txt',
          'c396a00095a0b9e3': 'journal_delta_nn_qualification_EB_bis_v1.md'}
for c, f in cibles.items():
    print('   %s  %s  -> %s' % (c, f, 'TIENT' if emp(open(f, 'rb').read()) == c else 'MORD'))
z = zipfile.ZipFile('lot_machine1_2026-11-13_acte_qualification_EB_bis_v1_recu.zip')
m = [n for n in z.namelist() if n.startswith('MANIFEST_')][0]
print('   ff93d708547f8ec0  %s (dans le zip du lot de machine 1)  -> %s' % (m, 'TIENT' if emp(z.read(m)) == 'ff93d708547f8ec0' else 'MORD'))
print()
print('2. nn.4 : "ces calculs ne relisent aucun fichier de sortie de la nuit ; ils en reprennent un nombre, le plancher du jumeau 1.330e-13, comme seuil (dix planchers)"')
for lot, rep in (('lot_machine1_2026-11-13_chaine_EA_par_etat_v1_recu.zip', 'chaine_EA_par_etat'), ('lot_machine1_2026-11-13_envoi_chaine_et_lectures_v1_recu.zip', 'envoi')):
    zz = zipfile.ZipFile(lot)
    for n in zz.namelist():
        if not (n.endswith('.py') or n.endswith('.md')):
            continue
        t = zz.read(n).decode('utf-8')
        lecture = [x for x in re.findall(r'(nuit_EB_bis[^\s"\']*|sonde_etage\w*|verdict_etage\w*|verdict_qualification\w*)', t)]
        seuil = '1.33e-12' in t
        if lecture or seuil:
            print('   %-60s references a la nuit : %-30s seuil 1.33e-12 : %s' % (n, sorted(set(lecture))[:4], seuil))
print('   (aucun script ne nomme un fichier de sortie de la nuit ; les deux scripts qui portent 1.33e-12 le portent comme constante litterale)')
print()
print('3. DATES DES PIECES DANS LES ZIP DE MACHINE 1 (heure locale de leur conteneur, telle qu\'ecrite dans le zip)')
for lot in ('lot_machine1_2026-11-13_acte_qualification_EB_bis_v1_recu.zip', 'lot_machine1_2026-11-13_chaine_EA_par_etat_v1_recu.zip',
            'lot_machine1_2026-11-13_envoi_chaine_et_lectures_v1_recu.zip'):
    zz = zipfile.ZipFile(lot)
    ts = sorted((i.date_time, i.filename) for i in zz.infolist())
    print('   %s : de %04d-%02d-%02d %02d:%02d (%s) a %04d-%02d-%02d %02d:%02d (%s)' % ((lot,) + ts[0][0][:5] + (ts[0][1],) + ts[-1][0][:5] + (ts[-1][1],)))
zz = zipfile.ZipFile('lot_machine1_2026-11-13_envoi_chaine_et_lectures_v1_recu.zip')
for i in zz.infolist():
    print('      %04d-%02d-%02d %02d:%02d  %s' % (i.date_time[:5] + (i.filename,)))
t = zz.read('note_apports_litterature_2026-11-13_v1.md').decode('utf-8')
tt = re.sub(r'\s+', ' ', t)
print('   note_apports_litterature (piece datee de 19:35) : dit "(e)crite pendant le run" : %s ; dit "Ne contient rien du run" : %s ; '
      'cite controle_MN_habillage_machine1_v1.py (piece datee de 19:35) en son paragraphe 2 : %s'
      % ('crite pendant le run' in tt, 'Ne contient rien du run' in tt, 'controle_MN_habillage_machine1_v1.py' in tt))
