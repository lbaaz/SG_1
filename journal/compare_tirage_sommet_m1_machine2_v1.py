# -*- coding: ascii -*-
"""Certification (c) : MON tirage de DEMONSTRATION (tirage_demonstration_sommet_machine2_v1.log) contre (1) les huit lignes de la section 3 de la piece, (2) le journal d'autotest de machine 1 (hachages, modulos, w2 aux rangs 0, 1, 2),
(3) son journal de demonstration (les huit w2 retenus et les cinquante-six cellules : g, eta0, r_c). Ses journaux sont lus comme des TEXTES, apres le mien.
Usage : py -3.11 -I compare_tirage_sommet_m1_machine2_v1.py <mon journal> <la piece de gel .md> <son autotest .log> <sa demonstration .log>"""
import re
import sys

MOI, PIECE, AUTO, DEMO = (open(p, encoding='ascii').read() for p in sys.argv[1:5])
re_h = re.compile(r'sha256\("DEMONSTRATION\|(MP|PP|MG|PG)\|(\d)"\) = ([0-9a-f]{16})\.\.\. ; modulo\s+(\d+) =\s+(\d+) -> w2 = ([0-9.]+)')
mes = {(m[0], int(m[1])): m[2:] for m in re_h.findall(MOI)}
piece = {(m[0], int(m[1])): m[2:] for m in re_h.findall(PIECE)}
auto = {(m[0], int(m[1])): m[2:] for m in re_h.findall(AUTO)}
print('lignes de hachage : miennes %d ; section 3 de la piece %d ; autotest de machine 1 %d' % (len(mes), len(piece), len(auto)))
d1 = [k for k in piece if mes.get(k) != piece[k]]
print('(1) section 3 de la piece : %d lignes sur %d, identiques aux miennes (hachage, modulo, numero, w2) : %s' % (len(piece) - len(d1), len(piece), 'OUI' if not d1 and len(piece) == 8 else 'NON %s' % d1))
d2 = [k for k in mes if auto.get(k) != mes[k]]
print('(2) autotest : mes %d lignes retrouvees dans son journal, identiques : %s' % (len(mes) - len(d2), 'OUI' if not d2 else 'NON %s' % d2))
# cellules
re_m = re.compile(r'(MP|PP|MG|PG)([ab])(\d)\s+kappa ([0-9.]+)\s+g = ([0-9.e+-]+)\s+eta0 = ([0-9.e+-]+)\s+r_c = (\d+)')
re_s = re.compile(r'(MP|PP|MG|PG)([ab])(\d)\s+w2 = (\S+)\s+kappa = ([0-9.]+)\s+g = ([0-9.e+-]+)\s+eta0 = ([0-9.e+-]+)\s+r_c = (\d+)')
cm = {m[0] + m[1] + m[2]: (m[3], m[4], m[5], m[6]) for m in re_m.findall(MOI)}
cs = {m[0] + m[1] + m[2]: (m[4], m[5], m[6], m[7]) for m in re_s.findall(DEMO)}
d3 = [k for k in cm if cs.get(k) != cm[k]]
print('(3) cellules : miennes %d ; siennes %d ; identiques (kappa, g, eta0, r_c, chaines) : %d sur %d : %s' % (len(cm), len(cs), len(cm) - len(d3), len(cm), 'OUI' if not d3 and len(cm) == 56 == len(cs) else 'NON %s' % d3[:5]))
re_w = re.compile(r'=> (MP|PP|MG|PG)([ab]) : w2 = (\S+) = ([0-9.]+)')
wm = {m[0] + m[1]: m[2] for m in re_w.findall(MOI)}
re_ws = re.compile(r'creneau (MP|PP|MG|PG) rang (\d) : numero\s+(\d+) sur (\d+) -> w2 = (\S+) \(([0-9.]+)\) : ELIGIBLE, retenu')
ws = {m[0] + 'ab'[int(m[1])]: m[4] for m in re_ws.findall(DEMO)}
print('    w2 retenus : miens %s ; siens %s ; identiques : %s' % (wm, ws, 'OUI' if wm == ws and len(wm) == 8 else 'NON'))
