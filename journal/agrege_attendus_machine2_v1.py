# -*- coding: ascii -*-
"""Lit les JSONL des grandes boites (machine 2) et applique, DEPUIS LE TEXTE de machine 1 (lot 4e15e302d97e26b8, sections 1 et 3), sa mesure et ses attendus :
R = moyenne sur les boites de 1/participation, divisee par la moyenne de 3/(n + 2) (n = niveaux de la boite dans la fenetre) ; Porter-Thomas : R = 1 ; parts plus egales : R < 1.
Trois issues par tranche : R > 1.25 ; 0.85 <= R <= 1.25 ; R < 0.85. Compte attendu (droite ajustee de m1 : 21.6 a 300, 28.8 a 400, donc 14.4 a 200) a 20 pour cent pres ; somme entre 0.90 et 1.10.
References simulees aux MEMES n : Porter-Thomas (parts chi-deux a 1 degre) et exponentielle (parts chi-deux a 2 degres), 20000 tirages, graine fixe.
Usage : py -3.11 -P agrege_attendus_machine2_v1.py <cote_min> <cote_max> <attendu du compte> <fichier.jsonl> [fichier.jsonl ...]"""
import glob
import json
import sys
import numpy as np

CMIN, CMAX, ATT = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]); FICH = []
for a in sys.argv[4:]:
    FICH += sorted(glob.glob(a))
B = []
for f in FICH:
    for l in open(f, encoding='ascii'):
        d = json.loads(l)
        if CMIN <= d['cote'] <= CMAX:
            B.append(d)
B.sort(key=lambda d: d['cote'])
if not B:
    print('aucune boite dans [%d, %d]' % (CMIN, CMAX)); raise SystemExit(1)
ns = np.array([d['n'] for d in B]); part = np.array([d['participation'] for d in B]); som = np.array([d['somme'] for d in B])
print('cotes %d a %d : %d boites (%s)' % (CMIN, CMAX, len(B), ' '.join(str(d['cote']) for d in B)))
print('niveaux par boite : moyenne %.2f (attendu %.1f +- 20 pour cent : %.1f a %.1f) -> %s' % (ns.mean(), ATT, 0.8 * ATT, 1.2 * ATT, 'TIENT' if 0.8 * ATT <= ns.mean() <= 1.2 * ATT else 'NE TIENT PAS'))
print('niveaux non fiables (deux lectures en desaccord a plus de 2 pour cent) : %d sur %d' % (sum(d['n'] - d['fiables'] for d in B), int(ns.sum())))
print('somme / largeur : moyenne %.3f (ecart-type par boite %.3f) -> %s' % (som.mean(), som.std(ddof=1) if len(som) > 1 else float('nan'), 'TIENT (0.90-1.10)' if 0.90 <= som.mean() <= 1.10 else 'NE TIENT PAS'))
print('participation : moyenne %.2f (min %.2f max %.2f)' % (part.mean(), part.min(), part.max()))
ref = (3.0 / (ns + 2.0)).mean()
R = (1.0 / part).mean() / ref
rng = np.random.default_rng(2026)


def sim(df, nrep=20000):
    Rs, Ps = [], []
    for _ in range(nrep):
        pp = []
        for n in ns:
            x = rng.chisquare(df, size=int(n)); pp.append(x.sum() ** 2 / np.sum(x ** 2))
        pp = np.array(pp); Rs.append((1.0 / pp).mean() / ref); Ps.append(pp.mean())
    return np.mean(Rs), np.std(Rs), np.mean(Ps), np.std(Ps)


rpt, spt, ppt, sppt = sim(1); rex, sex, pex, spex = sim(2)
print('R observe = %.3f   | Porter-Thomas aux memes n : R = %.3f +- %.3f, participation moyenne %.2f +- %.2f | exponentielle : R = %.3f +- %.3f, participation moyenne %.2f +- %.2f' % (R, rpt, spt, ppt, sppt, rex, sex, pex, spex))
issue = 'R au-dessus de 1.25 : la participation DECROCHE du compte' if R > 1.25 else ('R entre 0.85 et 1.25 : Porter-Thomas' if R >= 0.85 else 'R sous 0.85 : parts PLUS EGALES que Porter-Thomas')
print('ISSUE (attendus de m1) : %s' % issue)
big = [d for d in B if d['n'] >= 9]
if big:
    x = np.concatenate([np.array([v['y1'] for v in d['niveaux']]) / np.mean([v['y1'] for v in d['niveaux']]) for d in big])
    print('parts normalisees par la moyenne de leur boite, %d niveaux dans %d boites d au moins 9 niveaux : mediane %.3f ; fraction sous 0.1 : %.3f ; fraction au-dessus de 3 : %.3f' % (len(x), len(big), np.median(x), (x < 0.1).mean(), (x > 3).mean()))
    for nom, df in (('Porter-Thomas', 1), ('exponentielle', 2)):
        m, f1, f3 = [], [], []
        for _ in range(4000):
            xs = np.concatenate([(lambda z: z / z.mean())(rng.chisquare(df, size=d['n'])) for d in big]); m.append(np.median(xs)); f1.append((xs < 0.1).mean()); f3.append((xs > 3).mean())
        print('   %-14s : mediane %.3f +- %.3f ; sous 0.1 : %.3f +- %.3f ; au-dessus de 3 : %.3f +- %.3f' % (nom, np.mean(m), np.std(m), np.mean(f1), np.std(f1), np.mean(f3), np.std(f3)))
