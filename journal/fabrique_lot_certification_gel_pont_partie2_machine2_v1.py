# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'CERTIFICATION DU GEL PONT, SECONDE PARTIE' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-17. Meme squelette que fabrique_lot_tirage_graine_456823_pont_machine2_v1.py (non edite).
Aucune 2D a 397/200 ni a 2019/1000 ; aucun depot ; aucune sortie synthetique dans le lot (elles sont dans un dossier temporaire hors de BOCAL4, detruit apres usage).
Usage : py -3.11 -I fabrique_lot_certification_gel_pont_partie2_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; chaque nombre cite par la note est RELU dans le journal qui le porte (et doit etre dans la note) ; la note est ASCII et nomme le canon de CHAQUE piece ; aucune fuite de vie privee ;
LF dans les .py, .md et .json (les JSON ecrits sous Windows par les sondes et mes scripts sont d'abord reecrits en LF : seul le saut de ligne change, le canon B est inchange) ; ZIP relu bit-identique."""
import glob
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'certif_gel_pont_partie2_machine2/'
NOM = 'lot_machine2_2026-11-17_certification_gel_pont_partie2_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_pont_partie2_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_pont_partie2_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_pont_partie2_machine2_v1.py'
SCRIPTS = ['chaine_pont_machine2_v1.py', 'feuilles_pont_machine2_v1.py', 'compare_feuilles_machine2_v1.py', 'genere_synthetique_pont_machine2_v1.py', 'genere_synthetique_pont_machine2_v2.py',
           'genere_synthetique_pont_machine2_v3.py', 'genere_synthetique_pont_machine2_v4.py', 'differentiel_feuilles_machine2_v1.py', 'differentiel_feuilles_machine2_v2.py', 'differentiel_feuilles_machine2_v3.py', 'differentiel_feuilles_machine2_v4.py', 'partition_independante_machine2_v1.py',
           'compare_partition_machine2_v1.py', 'compare_sondes_sacrifie_machine2_v1.py', 'equivalence_hamiltonien_machine2_v1.py', 'confronte_section4_machine2_v1.py', 'verifie_nombres_section6_machine2_v1.py',
           'balayage_2d_candidats_machine2_v1.py', 'verifie_flux_direct_machine2_v1.py', 'cout_run_machine2_v1.py', 'mesure_pic_memoire_machine2_v1.py', 'compare_json_nombres_machine2_v1.py', 'synthese_mutations_feuilles_machine2_v1.py']
JOURNAUX = ['journaux/' + n for n in (
    'confronte_tirage_m1_machine2_v1.log', 'confronte_section4_machine2_v1.log', 'verifie_nombres_section6_machine2_v1.log', 'equivalence_hamiltonien_machine2_v1.log', 'balayage_2d_candidats_machine2_v1.log',
    'cout_run_machine2_v1.log', 'verifie_flux_direct_machine2_v1.log', 'differentiel_feuilles_graines_1_14_machine2_v1.log', 'differentiel_feuilles_v2_graines_1_14_machine2_v1.log', 'differentiel_feuilles_v3_graines_1_14_machine2_v1.log', 'differentiel_feuilles_v4_graines_101_112_machine2_v1.log',
    'matrice_mutations_feuilles_synthese_machine2_v1.log')]
MUTATIONS_LOGS = sorted(os.path.relpath(p, os.path.join(ICI, D)).replace(os.sep, '/') for p in glob.glob(os.path.join(ICI, D, 'journaux', 'mutations*', '*.log')))
AUTRES = ['chaine_pont_machine2_v1.log', 'chaine_pont_machine2_v1.json',
          'feuilles_qualification/lecture_densite_2d_qualification_machine2_v1.log', 'feuilles_qualification/lecture_densite_2d_SA3_machine2.json', 'feuilles_qualification/lecture_densite_2d_SA4_machine2.json',
          'feuilles_qualification/lecture_densite_2d_SA5_machine2.json', 'feuilles_qualification/lecture_boites_repetition_machine2_v1.log', 'feuilles_qualification/lecture_boites_repetition_machine2.json',
          'feuilles_qualification/repetition_verdict_machine2_v1.log', 'feuilles_qualification/repetition_verdict_machine2.json', 'feuilles_qualification/compare_feuilles_repetition_machine2_v1.log',
          'feuilles_qualification/tronque/essai_sortie_tronquee_machine2_v1.log',
          'rejeu_releve_m1/rejeu_releve_gel_pont_partie2_machine2_v1.log', 'rejeu_releve_m1/compare_json_nombres_R11_machine2_v1.log', 'rejeu_releve_m1/repetition_verdict_rejoue_machine2.log',
          'sacrifie/densite_2d_SA5_A_machine2.log', 'sacrifie/densite_2d_SA5_A_machine2.json', 'sacrifie/compare_densite_SA5_A_machine2_v1.log',
          'sacrifie/boite_SA3_185_machine2.log', 'sacrifie/boite_SA3_185_machine2.jsonl', 'sacrifie/compare_boite_SA3_185_machine2_v1.log',
          'sacrifie/boite_SA3_300_machine2.log', 'sacrifie/boite_SA3_300_machine2.jsonl', 'sacrifie/compare_boite_SA3_300_machine2_v1.log',
          'sacrifie/boite_SA4_300_machine2.log', 'sacrifie/boite_SA4_300_machine2.jsonl', 'sacrifie/compare_boite_SA4_300_machine2_v1.log',
          'sacrifie/boite_SA5_300_machine2.log', 'sacrifie/boite_SA5_300_machine2.jsonl', 'sacrifie/compare_boite_SA5_300_machine2_v1.log',
          'sacrifie/boite_SA5_185_machine2.log', 'sacrifie/boite_SA5_185_machine2.jsonl',
          'sacrifie/partition_SA5_300_machine2_v1.log', 'sacrifie/partition_SA5_300_machine2.json', 'sacrifie/compare_partition_SA5_300_machine2_v1.log',
          'sacrifie/pic_memoire/pic_densite_B_k8_machine2.log', 'sacrifie/pic_memoire/pic_boite_300_machine2.log']
PIECES = [D + n for n in SCRIPTS] + [D + n for n in JOURNAUX] + [D + n for n in MUTATIONS_LOGS] + [D + n for n in AUTRES] + [
    'livraison_17b_gel_pont_partie2/authentification_envoi_machine2_v1.log', 'certif_gel_pont_partie1_machine2/authentifie_envoi_m1_machine2_v1.py', SELF]
# NOMBRES : (journal relatif a D, texte que le journal porte ET que la note doit porter) -- completes avec la note (voir plus bas)
NOMBRES = []
exec_nombres = os.path.join(ICI, 'nombres_certification_gel_pont_partie2_machine2_v1.txt')
if os.path.isfile(exec_nombres):
    for l in open(exec_nombres, encoding='ascii').read().split('\n'):
        if '|||' in l:
            a, b = l.split('|||', 1)
            NOMBRES.append((a.strip(), b.strip()))
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


TERMES = [''.join(p) for p in (('ba', 'zil'), ('le', 'beau'), ('gm', 'ail'), ('hot', 'mail'), ('Us', 'ers\\'), ('Us', 'ers/'), ('App', 'Data'), ('.cla', 'ude\\'), ('.cla', 'ude/'), ('Down', 'loads'))]


def fuites(nom, octets):
    t = octets.decode('latin-1').lower()
    out = [(nom, w) for w in TERMES if w.lower() in t]
    out += [(nom, m) for m in re.findall(r'(?<![a-z0-9])[a-z]:[\\/]', t)]
    out += [(nom, m) for m in re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', t)]
    return out


# 0. les JSON ecrits sous Windows : saut de ligne LF (le canon B est inchange ; seuls les octets bruts changent)
for p in PIECES:
    if p.endswith('.json') and os.path.isfile(os.path.join(ICI, p)):
        b = open(os.path.join(ICI, p), 'rb').read()
        if b'\r\n' in b:
            open(os.path.join(ICI, p), 'wb').write(b.replace(b'\r\n', b'\n'))
for p in PIECES + [NOTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
note = lit(NOTE)
INSERTS = {'@@V3@@': ('journaux/differentiel_feuilles_v3_graines_1_14_machine2_v1.log', ('BILAN', 'repartition')), '@@V4@@': ('journaux/differentiel_feuilles_v4_graines_101_112_machine2_v1.log', ('BILAN', 'repartition')),
           '@@COUT@@': ('journaux/cout_run_machine2_v1.log', ('',))}
for marque, (jr, debuts) in INSERTS.items():
    if marque in note:
        vus, sel = set(), []
        for l in lit(D + jr).split(chr(10)):
            if l.strip() and l.startswith(debuts) and l not in vus:
                vus.add(l); sel.append('    ' + l)
        note = note.replace(marque, chr(10).join(sel))
if '@@MUTATIONS@@' in note:        # la synthese de la matrice de mutations est recopiee TELLE QUELLE depuis son journal
    syn = [l for l in lit(D + 'journaux/matrice_mutations_feuilles_synthese_machine2_v1.log').split('\n') if l.strip()]
    note = note.replace('@@MUTATIONS@@', '\n'.join('    ' + l for l in syn))
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
for j, s in NOMBRES:
    if norm(s) not in norm(lit(D + j)):
        arrets.append('le journal %s ne porte pas %r' % (j, s))
    if norm(s) not in norm(note):
        arrets.append('la note ne porte pas %r' % s)
if not NOMBRES:
    arrets.append('aucun nombre a verifier : le fichier des nombres est absent')
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
elif not arrets:
    open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
for p in PIECES + [NOTE]:
    brut = open(os.path.join(ICI, p), 'rb').read()
    for f in fuites(p, brut):
        arrets.append('FUITE de vie privee : %s' % (f,))
    if b'\r' in brut and p.endswith(('.py', '.md', '.json')):
        arrets.append('fins de ligne CRLF dans %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- LA CERTIFICATION par machine 2 de la seconde partie du gel "pont" (piece de canon 428ac47649de31f3, section 12) : tirage, feuilles ecrites du texte et differentiel, sondes rejouees au point sacrifie, '
    'lecture par partition, table de la section 4, aucune 2D aux w2 tires. AUCUNE 2D a ces w2 ; aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : la piece de machine 1 de canon 428ac47649de31f3 (lot 7bf7982cceade968) ; la graine 456823 ; la table commune 0c10ddbf2813d809 ; le registre public en tete 2988237\n")
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
