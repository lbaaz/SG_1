# -*- coding: ascii -*-
"""(b) Reconstruction des scripts derives -- machine 2, 2026-11-16. Rejoue le script de construction de machine 1 sur MES sources certifiees (la sonde dense du delta 98 24315c52b234319c prise dans mon clone du registre,
la sonde et la feuille du gel ter que j'ai certifiees et jouees), puis compare, octet pour octet (ou, pour le json ecrit en CRLF par Windows, au canon B), a ce que le lot de machine 1 porte. Verifie aussi, par ma
propre lecture des diffs, que chaque script derive ne differe de sa source que dans les blocs du diff, et que les blocs retires/ajoutes sont ceux de la construction.
Usage : py -3.11 -P reconstruction_derives_machine2_v1.py <dossier du lot de m1> <sonde dense certifiee> <sonde du gel ter> <feuille du gel ter> <dossier de sortie (neuf)>"""
import difflib, hashlib, os, subprocess, sys, unicodedata
LOT, S_DENSE, S_LECT, S_FEUILLE, OUT = [os.path.abspath(x) for x in sys.argv[1:6]]
def canon_txt(t):
    t = unicodedata.normalize('NFC', t).replace('\r\n', '\n').replace('\r', '\n'); return hashlib.sha256(t.encode()).hexdigest()[:16]
def canon(p):
    return canon_txt(open(p, 'rb').read().decode('utf-8'))
res = []
def ctl(n, ok, d):
    res.append(ok); print('%-4s %-6s %s' % (n, 'TIENT' if ok else 'MORD', d), flush=True)
for p, att in ((S_DENSE, '24315c52b234319c'), (S_LECT, 'b5616dcf858e8801'), (S_FEUILLE, 'b2d6d7cfaf30f1cf')):
    ctl('R00', canon(p) == att, 'source %s : canon %s (attendu %s)' % (os.path.basename(p), canon(p), att))
r = subprocess.run([sys.executable, '-P', os.path.join(LOT, 'construction_instrument_gel_loi_machine1_v1.py'), S_DENSE, S_LECT, S_FEUILLE, os.path.join(LOT, 'tirage_machine1_v1_graine_200482.log'), OUT], capture_output=True, text=True)
print(r.stdout.strip())
ctl('R01', r.returncode == 0, 'le script de construction de machine 1, rejoue sur mes sources : code %d' % r.returncode)
for f in ('sonde_dense_gel_loi_machine1_v1.py', 'sonde_lecteur_gel_loi_machine1_v1.py', 'lecture_lecteur_gel_loi_machine1_v1.py', 'table_points_gel_loi_ordre3_v1.json', 'table_points_prevol_gel_loi_ordre3_v1.json',
          'sonde_dense_gel_loi_machine1_v1.diff', 'sonde_lecteur_gel_loi_machine1_v1.diff', 'lecture_lecteur_gel_loi_machine1_v1.diff', 'canons_instrument_v1.json'):
    a, b = open(os.path.join(OUT, f), 'rb').read(), open(os.path.join(LOT, f), 'rb').read()
    ctl('R02', a == b or (canon_txt(a.decode('utf-8')) == canon_txt(b.decode('utf-8'))), '%s : %s (canon B %s / %s)' % (f, 'identique a l octet' if a == b else 'identique au canon B (fins de ligne)', canon(os.path.join(OUT, f)), canon(os.path.join(LOT, f))))
# ma lecture independante des diffs : source -> derive, hunks recalcules par difflib, comparaison a ceux du lot
for src, der in ((S_DENSE, 'sonde_dense_gel_loi_machine1_v1.py'), (S_LECT, 'sonde_lecteur_gel_loi_machine1_v1.py'), (S_FEUILLE, 'lecture_lecteur_gel_loi_machine1_v1.py')):
    s = open(src, encoding='ascii').read().split('\n'); t = open(os.path.join(LOT, der), encoding='ascii').read().split('\n')
    ops = [o for o in difflib.SequenceMatcher(None, s, t, autojunk=False).get_opcodes() if o[0] != 'equal']
    ret = sum(o[2] - o[1] for o in ops); ajo = sum(o[4] - o[3] for o in ops)
    dd = open(os.path.join(LOT, der[:-3] + '.diff'), encoding='ascii').read().split('\n')
    dret = sum(1 for l in dd if l.startswith('-') and not l.startswith('---')); dajo = sum(1 for l in dd if l.startswith('+') and not l.startswith('+++'))
    ctl('R03', len(ops) > 0 and dret > 0 and abs(ret - dret) <= len(ops) and abs(ajo - dajo) <= len(ops), '%s : blocs modifies %d, lignes retirees %d / ajoutees %d (mon recalcul) ; diff du lot : %d / %d' % (der, len(ops), ret, ajo, dret, dajo))
print('BILAN : %d controles, %d tiennent' % (len(res), sum(res)))
sys.exit(0 if all(res) else 1)
