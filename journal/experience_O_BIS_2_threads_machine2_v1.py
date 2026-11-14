# -*- coding: ascii -*-
"""EXPERIENCE HORS GEL, NON OPPOSABLE, machine 2, 2026-11-13 (suite de experience_O_BIS_2_machine2_v1.py) : MEME decomposition
(j = 6, G30, N = 70, k = -2), voie du diagnostic, sous un nombre de fils BLAS impose par l'environnement
(OPENBLAS_NUM_THREADS / OMP_NUM_THREADS). Usage : OPENBLAS_NUM_THREADS=n OMP_NUM_THREADS=n python -P <ce script>"""
import hashlib, importlib.util, os, platform, time, unicodedata
from fractions import Fraction
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
t = unicodedata.normalize('NFC', open('m17_chaine_v17.py', 'rb').read().decode('utf-8')).replace('\r\n', '\n')
assert hashlib.sha256(t.encode()).hexdigest()[:16] == '82a0be882568fe0c'
spec = importlib.util.spec_from_file_location('m', 'm17_chaine_v17.py'); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
try:
    from threadpoolctl import threadpool_info
    info = [(d.get('internal_api'), d.get('num_threads')) for d in threadpool_info()]
except Exception:
    info = 'threadpoolctl indisponible'
t0 = time.time()
H = M.H_2D(70, Fraction(39, 20), 0.08408964152537146, +1, 'x5', 0.05 * 2.0 ** 2, 40)[0]
vals, vecs = np.linalg.eig(H)
ov = np.abs(vecs[0, :]) ** 2 / np.sum(np.abs(vecs) ** 2, axis=0); i = int(np.argmax(ov))
print('fils OPENBLAS=%s OMP=%s ; pool %s : gamma = %.12e E_re = %.15e recouvrement %.6f (%.0f s)' % (
    os.environ.get('OPENBLAS_NUM_THREADS'), os.environ.get('OMP_NUM_THREADS'), info, -2.0 * vals[i].imag, vals[i].real, ov[i], time.time() - t0), flush=True)
