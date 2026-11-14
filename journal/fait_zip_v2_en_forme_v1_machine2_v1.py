# -*- coding: ascii -*-
"""Fabrique un zip = le lot v1 de m1, avec l'acte REMPLACE par la v2 (meme nom de piece), pour rejouer mes 34 controles sur la v2 :
les controles qui mordent doivent etre exactement ceux qui portent sur un texte que la v2 change."""
import sys
import zipfile

src, v2, out = sys.argv[1:4]
zi = zipfile.ZipFile(src)
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zo:
    for n in zi.namelist():
        if n == 'journal_delta_nn_qualification_EB_bis_v1.md':
            zo.writestr(n, open(v2, 'rb').read())
        else:
            zo.writestr(n, zi.read(n))
print('ok', out)
