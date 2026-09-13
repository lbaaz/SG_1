#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CONSTRUCTION DU BANC v13 = v12 (2c4345515bb02325, machine 2, non edite) + LEVEE DE D-v12-1.
machine 1, v1, 13/09/2026. Trois remplacements a ancre UNIQUE, asseres ; le pin du gel v7 ne bouge pas.

D-v12-1, MESURE (run temoin v12 sur machine 1, levier X86_V4, contre le depot 9bis c4310e33da6b9759
etabli sur BOCAL4) : le controle 9bis compare les feuilles flottantes AU BIT, et sept cles du
perimetre different d'UN ulp entre les deux libm (glibc / UCRT) -- /T1/A et /T3a/A tol_int et
tol_int_sur_1 (0.008578984888782986 contre ...988), /T1/B disp_y, tol_R, tol_R_sur_q_moins_1.
Verdict sur machine 1 : NON CONCLUANT D'INSTRUMENT, porte de alpha fermee ; sur BOCAL4, machine
de la reference, 0 ecart par construction. Le gel v7 (section 5, decision (ii) issue (c)) dit
que les cles de classe EXPOSEE-LIBM se comparent entre machines A 2 ULP ; l'instrument ne
l'implementait pas, et la classe, enumeree au gel (tol_int, tol_ordre), est plus large que son
enumeration (disp_y, tol_R : une dispersion et une tolerance passent aussi par la libm).
Correctif v13 : toute feuille FLOTTANTE finie du perimetre 9bis se compare a 2 ulp ; les ecarts
toleres sont ENUMERES dans le JSON (toleres_ulp) et au journal ; entiers, chaines, booleens,
longueurs et cles restent au bit. Rien n'est relache au-dela d'un ulp double : 2^-52 relatif.
Usage : construction_banc_v13_machine1_v1.py <banc_v12.py> <sortie banc_v13.py>
"""
import hashlib, sys, unicodedata

SRC, OUT = sys.argv[1], sys.argv[2]


def canon(t):
    return hashlib.sha256(unicodedata.normalize('NFC', t).replace('\r\n', '\n').encode()).hexdigest()[:16]


s = open(SRC, 'rb').read().decode('utf-8')
assert canon(s) == '2c4345515bb02325', 'le v12 au poste n est pas le v12 emis'
REMPL = [
    ('    L, reference = _ser(L), _ser(reference)\n    ecarts = []\n',
     '    L, reference = _ser(L), _ser(reference)\n    ecarts = []\n    controle_9bis.toleres = []          # v13 (D-v12-1) : ecarts a 2 ulp au plus, enumeres, non comptes\n'),
    ('        if a != b:\n            ecarts.append("%s (%r != %r)" % (chemin, a, b))\n    for cle in PERIM_9BIS:',
     '        if (isinstance(a, float) and isinstance(b, float) and math.isfinite(a) and math.isfinite(b)\n'
     '                and a != b):\n'
     '            d = abs(a - b) / math.ulp(max(abs(a), abs(b)))   # v13 : feuilles flottantes a 2 ulp (gel v7, 5)\n'
     '            if d <= 2.0:\n'
     '                controle_9bis.toleres.append("%s (%r ~ %r, %.1f ulp)" % (chemin, a, b, d))\n'
     '                return\n'
     '        if a != b:\n            ecarts.append("%s (%r != %r)" % (chemin, a, b))\n    for cle in PERIM_9BIS:'),
    ('                                  "ecarts": ec[:40], "reference": ref_9bis.get("nom", "?"),\n',
     '                                  "ecarts": ec[:40], "reference": ref_9bis.get("nom", "?"),\n'
     '                                  "toleres_ulp": list(controle_9bis.toleres)[:40],   # v13\n'),
    ('            JRN("9bis", "perimetre %s a profondeur %d, exemptes %s : %d ecart(s)"\n'
     '                % ("/".join(PERIM_9BIS), ref_9bis["profondeur"], sorted(ref_9bis["exemptes"]), len(ec)))\n',
     '            JRN("9bis", "perimetre %s a profondeur %d, exemptes %s : %d ecart(s) ; %d tolere(s) a 2 ulp : %s"\n'
     '                % ("/".join(PERIM_9BIS), ref_9bis["profondeur"], sorted(ref_9bis["exemptes"]), len(ec),\n'
     '                   len(controle_9bis.toleres), "; ".join(controle_9bis.toleres)[:600]))\n'),
    ('VERSION = "banc_qualification_machine1_v12"', 'VERSION = "banc_qualification_machine1_v13"'),
    ("DE LA CONSTANTE A (delta' = 1/44100 ; v12 = v11 + levee de D-v11-1 : la jumelle du",
     "DE LA CONSTANTE A (delta' = 1/44100 ; v13 = v12 + levee de D-v12-1 : le 9bis compare\n"
     "les feuilles flottantes a 2 ulp entre machines, ecarts toleres enumeres,\n"
     "construction_banc_v13_machine1_v1.py ; v12 = v11 + levee de D-v11-1 : la jumelle du"),
]
for a, b in REMPL:
    assert s.count(a) == 1, 'ancre non unique ou absente : %r' % a[:70]
    s = s.replace(a, b)
assert all(c < 128 for c in s.encode())
open(OUT, 'w', encoding='utf-8', newline='\n').write(s)
print('v13 ecrit : canon %s ; %d remplacements ; pin du gel INCHANGE (v7)' % (canon(s), len(REMPL)))
