# -*- coding: ascii -*-
"""PILOTE DU RUN du gel "pont" (seconde partie, piece de canon 428ac47649de31f3 ; rectificatif d'avant run 9e25019f3b9bdf04) -- machine 2, 2026-11-17.
Il ne FAIT que ce que la note de machine 1 demande, avec ses scripts, sans les modifier : la chaine ; par cellule, quatre sondes de densite (A a D, douze barreaux) et vingt boites fermees (cotes 180 a 189, 291 a 300,
chaque cote une fois, repartis en jobs) ; puis les trois feuilles de machine 1 (et, a cote, mes trois feuilles ecrites du texte). Il ajoute : l'ordonnancement (jobs et memoire), le controle de COMPLETUDE de chaque sortie
(rectificatif, 1 : une sortie de densite est complete si elle porte les douze barreaux -3 a 8 ; une sortie incomplete n'est pas une sortie du run et se rejoue telle quelle ; une sortie complete ne se rejoue jamais ;
une boite interrompue se rejoue, ses cotes manquants seuls, dans un fichier neuf), et un journal sans chemin de poste.
GARDES (E19) : le mode `run` exige le dossier de sortie NEUF et l'argument --feu-vert avec la date et l'heure du feu vert ECRIT de l'operateur ; il n'existe aucun mode "rejouer tout".
Modes : selftest (controles de completude et d'ordonnancement sur de faux fichiers, aucune 2D) ; essai (au point sacrifie w2 = 101/50, hors chaine : quelques sondes reelles, petites) ; plan (liste les jobs) ; run.
Usage : py -3.11 -P run_pont_machine2_v1.py selftest
        py -3.11 -P run_pont_machine2_v1.py essai   <registre> <lot de m1 a plat> <dossier neuf>
        py -3.11 -P run_pont_machine2_v1.py plan    <registre> <lot de m1 a plat>
        py -3.11 -P run_pont_machine2_v1.py run     <registre> <lot de m1 a plat> <dossier neuf> --feu-vert "AAAA-MM-JJ HH:MM" [--jobs 8] [--budget-go 12]"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from fractions import Fraction as F

PY = sys.executable
HERE = os.path.dirname(os.path.abspath(__file__))
CELLULES = {'MG3': ('397/200', 3, '3.63872e-03'), 'MG4': ('397/200', 4, '2.77765e-03'), 'MG5': ('397/200', 5, '2.20823e-03'),
            'PG3': ('2019/1000', 3, '5.23478e-03'), 'PG4': ('2019/1000', 4, '3.99601e-03'), 'PG5': ('2019/1000', 5, '3.17683e-03')}
ESSAI_CELLULES = {'SA3': ('101/50', 3, '5.53067e-03')}
COTES_UN = list(range(180, 190))
COTES_DEUX_JOBS = [[291, 292, 293, 294], [295, 296, 297], [298, 299, 300]]
BARREAUX = list(range(-3, 9))
POIDS_GO = {'densite': 0.5, 'boite_UN': 0.8, 'boite_DEUX': 1.9, 'fantome': 0.1}       # memoire de travail estimee par job (mesuree : boite 300 a 5 barreaux 1.71 Go, densite B 0.38 Go)
RELANCES_MAX = 2
PAT_CHEMIN = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/][^\s'\"<>|]*")
T0 = time.time()


def masque(t):
    return PAT_CHEMIN.sub('<chemin>', t)


def journal(msg, fichier=None):
    ligne = '[%6.0f s] %s' % (time.time() - T0, masque(msg))
    print(ligne, flush=True)
    if fichier:
        with open(fichier, 'a', encoding='ascii', errors='replace', newline='\n') as f:
            f.write(ligne + '\n')


# ---------------------------------------------------------------- controles de completude
def complet_densite(chemin, w2, m, g, ks=BARREAUX):
    """Une sortie de densite est COMPLETE si elle porte les barreaux ks (douze : -3 a 8), chacun suivi ou dit non suivi, et la bonne cellule."""
    try:
        d = json.load(open(chemin, encoding='ascii'))
    except (OSError, ValueError):
        return False, 'fichier absent ou JSON illisible'
    if (d.get('w2'), d.get('m'), d.get('g')) != (w2, m, g):
        return False, 'ce n est pas la cellule demandee'
    k = d.get('k', {})
    manque = [b for b in ks if str(b) not in k]
    if manque:
        return False, 'barreaux manquants : %s' % manque
    if any('suivi' not in k[str(b)] for b in ks):
        return False, 'un barreau sans drapeau suivi'
    return True, 'complete (%d barreaux)' % len(ks)


def lignes_boites(chemin):
    out = {}
    try:
        for l in open(chemin, encoding='ascii'):
            if l.strip():
                try:
                    b = json.loads(l)
                except ValueError:
                    continue                                       # une ligne coupee n'est pas une boite
                if 'niveaux' in b and 'cote' in b:
                    out[b['cote']] = b
    except OSError:
        pass
    return out


def cotes_manquants(chemins, cotes, w2, m, g):
    vus = set()
    for c in chemins:
        for cote, b in lignes_boites(c).items():
            if (b.get('w2'), b.get('m'), b.get('g')) == (w2, m, g):
                vus.add(cote)
    return [c for c in cotes if c not in vus]


# ---------------------------------------------------------------- les jobs
class Job:
    def __init__(self, nom, genre, cmd, cellule, sortie, **kw):
        self.nom, self.genre, self.cmd, self.cellule, self.sortie = nom, genre, cmd, cellule, sortie
        self.relances = 0
        self.etat = 'attente'
        self.kw = kw
        self.proc = None
        self.debut = 0.0


def fabrique_jobs(cellules, reg, lot, out, essai=False):
    sonde_d, sonde_b = os.path.join(lot, 'sonde_densite_2d_pont_machine1_v1.py'), os.path.join(lot, 'sonde_boite_fermee_pont_machine1_v1.py')
    jobs = []
    for nom, (w2, m, g) in cellules.items():
        for a in ('B', 'C', 'D', 'A'):                                                       # les plus gros d'abord
            sortie = os.path.join(out, 'densite_2d_%s_%s.json' % (nom, a))
            ks = [8] if essai else []
            jobs.append(Job('densite %s %s' % (nom, a), 'densite', [PY, '-P', sonde_d, reg, w2, str(m), g, a, sortie] + [str(k) for k in ks], nom, sortie, w2=w2, m=m, g=g, ks=(ks or BARREAUX)))
        deux = [[50, 51]] if essai else COTES_DEUX_JOBS
        un = [[52, 53]] if essai else [COTES_UN]
        for j, cotes in enumerate(deux):
            sortie = os.path.join(out, 'boites_%s_DEUX%d.jsonl' % (nom, j + 1))
            jobs.append(Job('boites %s DEUX%d %s' % (nom, j + 1, cotes), 'boite_DEUX', [PY, '-P', sonde_b, reg, w2, str(m), g, sortie] + [str(c) for c in cotes], nom, sortie, w2=w2, m=m, g=g, cotes=cotes, base=sortie))
        for j, cotes in enumerate(un):
            sortie = os.path.join(out, 'boites_%s_UN%d.jsonl' % (nom, j + 1))
            jobs.append(Job('boites %s UN%d %s' % (nom, j + 1, cotes), 'boite_UN', [PY, '-P', sonde_b, reg, w2, str(m), g, sortie] + [str(c) for c in cotes], nom, sortie, w2=w2, m=m, g=g, cotes=cotes, base=sortie))
    return jobs


def valide(job):
    """(complet, message) pour un job termine."""
    if job.genre == 'densite':
        return complet_densite(job.sortie, job.kw['w2'], job.kw['m'], job.kw['g'], job.kw['ks'])
    if job.genre.startswith('boite'):
        fichiers = [job.kw['base']] + ['%s_r%d.jsonl' % (job.kw['base'][:-6], i) for i in range(1, RELANCES_MAX + 1)]
        manque = cotes_manquants(fichiers, job.kw['cotes'], job.kw['w2'], job.kw['m'], job.kw['g'])
        return (not manque), ('toutes les boites sont la' if not manque else 'cotes manquants : %s' % manque)
    return (job.proc.returncode == 0), 'code %s' % job.proc.returncode


def ordonnance(jobs, dossier_logs, nb_jobs, budget_go, etat_fichier, jfile, poll=2.0):
    """Lance les jobs par ordre, jusqu'a nb_jobs a la fois et budget_go de memoire estimee ; valide chaque sortie ; relance (au plus RELANCES_MAX fois) ce qui est incomplet."""
    os.makedirs(dossier_logs, exist_ok=True)
    attente, en_cours = list(jobs), []
    while attente or en_cours:
        utilise = sum(POIDS_GO[j.genre] for j in en_cours)
        i = 0
        while i < len(attente) and len(en_cours) < nb_jobs:
            j = attente[i]
            if utilise + POIDS_GO[j.genre] <= budget_go or not en_cours:
                attente.pop(i)
                cmd = list(j.cmd)
                if j.genre.startswith('boite') and j.relances:                                # une boite interrompue : ses cotes manquants SEULS, dans un fichier neuf
                    fichier_neuf = '%s_r%d.jsonl' % (j.kw['base'][:-6], j.relances)
                    cmd = cmd[:cmd.index(j.kw['base'])] + [fichier_neuf] + [str(c) for c in j.kw['a_rejouer']]
                log = os.path.join(dossier_logs, '%s_essai%d.log' % (re.sub(r'[^A-Za-z0-9]+', '_', j.nom).strip('_'), j.relances))
                j.log = log
                j.proc = subprocess.Popen(cmd, stdout=open(log + '.brut', 'wb'), stderr=subprocess.STDOUT)
                j.debut, j.etat = time.time(), 'en cours'
                en_cours.append(j)
                utilise += POIDS_GO[j.genre]
                journal('LANCE  %-34s (essai %d)  jobs en cours %d, memoire estimee %.1f Go' % (j.nom, j.relances, len(en_cours), utilise), jfile)
            else:
                i += 1
        time.sleep(poll)
        for j in list(en_cours):
            if j.proc.poll() is None:
                continue
            en_cours.remove(j)
            texte = open(j.log + '.brut', 'rb').read().decode('latin-1')
            open(j.log, 'w', encoding='ascii', errors='replace', newline='\n').write(masque(texte))
            os.remove(j.log + '.brut')
            ok, msg = valide(j)
            if ok:
                j.etat = 'fait'
                journal('FAIT   %-34s %.0f s : %s' % (j.nom, time.time() - j.debut, msg), jfile)
            elif j.relances < RELANCES_MAX:
                j.relances += 1
                if j.genre == 'densite' and os.path.isfile(j.sortie):                       # une sortie incomplete n'est pas une sortie du run : on la met de cote, on la rejoue telle quelle
                    os.makedirs(os.path.join(os.path.dirname(dossier_logs), 'incomplets'), exist_ok=True)
                    shutil.move(j.sortie, os.path.join(os.path.dirname(dossier_logs), 'incomplets', '%s.essai%d' % (os.path.basename(j.sortie), j.relances - 1)))
                if j.genre.startswith('boite'):
                    fichiers = [j.kw['base']] + ['%s_r%d.jsonl' % (j.kw['base'][:-6], i) for i in range(1, RELANCES_MAX + 1)]
                    j.kw['a_rejouer'] = cotes_manquants(fichiers, j.kw['cotes'], j.kw['w2'], j.kw['m'], j.kw['g'])
                attente.insert(0, j)
                j.etat = 'a relancer'
                journal('INCOMPLET %-31s %s : relance %d sur %d' % (j.nom, msg, j.relances, RELANCES_MAX), jfile)
            else:
                j.etat = 'ECHEC'
                journal('ECHEC  %-34s %s (apres %d relances)' % (j.nom, msg, j.relances), jfile)
        json.dump({j.nom: dict(etat=j.etat, relances=j.relances) for j in jobs}, open(etat_fichier, 'w'), indent=1, sort_keys=True)
    return [j for j in jobs if j.etat != 'fait']


# ---------------------------------------------------------------- modes
def selftest():
    tmp = tempfile.mkdtemp()
    ok = True

    def verifie(nom, cond):
        nonlocal ok
        print('  %-70s %s' % (nom, 'OK' if cond else 'ECHEC'))
        ok = ok and cond
    d12 = {'w2': '101/50', 'm': 3, 'g': 'x', 'k': {str(b): {'suivi': True} for b in BARREAUX}}
    p = os.path.join(tmp, 'a.json')
    json.dump(d12, open(p, 'w'))
    verifie('densite a 12 barreaux : complete', complet_densite(p, '101/50', 3, 'x')[0])
    d9 = dict(d12, k={str(b): {'suivi': True} for b in range(-3, 6)})
    json.dump(d9, open(p, 'w'))
    verifie('densite a 9 barreaux (interrompue) : INCOMPLETE', not complet_densite(p, '101/50', 3, 'x')[0])
    open(p, 'w').write('{"w2": "101/50", "k": {"-3": {"suivi": tr')
    verifie('JSON coupe en plein milieu : INCOMPLET', not complet_densite(p, '101/50', 3, 'x')[0])
    json.dump(dict(d12, m=4), open(p, 'w'))
    verifie('densite d une autre cellule : refusee', not complet_densite(p, '101/50', 3, 'x')[0])
    d_ns = dict(d12, k=dict({str(b): {'suivi': True} for b in BARREAUX}, **{'8': {'suivi': False}}))
    json.dump(d_ns, open(p, 'w'))
    verifie('barreau dit non suivi : compte comme present', complet_densite(p, '101/50', 3, 'x')[0])
    pb = os.path.join(tmp, 'b.jsonl')
    open(pb, 'w').write(json.dumps({'cote': 180, 'w2': '101/50', 'm': 3, 'g': 'x', 'niveaux': []}) + '\n' + json.dumps({'cote': 181, 'w2': '101/50', 'm': 3, 'g': 'x', 'niveaux': []})[:30])
    verifie('boites : 180 presente, 181 coupee -> manquants [181, 182]', cotes_manquants([pb], [180, 181, 182], '101/50', 3, 'x') == [181, 182])
    verifie('boites : une boite d une autre cellule ne compte pas', cotes_manquants([pb], [180], '101/50', 4, 'x') == [180])
    verifie('masque de chemins : lettre de lecteur et barres', masque('ecrit C:\\a\\b.json et D:/x/y') == 'ecrit <chemin> et <chemin>')
    # ordonnancement : un job qui echoue puis reussit (compteur), un job qui reussit du premier coup (ne doit PAS etre relance), un job qui echoue toujours
    compteur = os.path.join(tmp, 'compteur.txt')
    script = os.path.join(tmp, 'fantome.py')
    open(script, 'w').write("import sys, os\nc = sys.argv[1]\nn = int(open(c).read()) if os.path.exists(c) else 0\nopen(c, 'w').write(str(n + 1))\nsys.exit(0 if n >= int(sys.argv[2]) else 3)\n")
    jobs = []
    for nom, echecs in (('bon', 0), ('un_echec', 1), ('toujours', 99)):
        j = Job('fantome ' + nom, 'fantome', [PY, script, os.path.join(tmp, nom + '.txt'), str(echecs)], 'X', os.path.join(tmp, nom + '.out'))
        jobs.append(j)
    reste = ordonnance(jobs, os.path.join(tmp, 'journaux'), 3, 5.0, os.path.join(tmp, 'etat.json'), os.path.join(tmp, 'j.log'), poll=0.2)
    n = {nom: int(open(os.path.join(tmp, nom + '.txt')).read()) for nom in ('bon', 'un_echec', 'toujours')}
    verifie('job reussi du premier coup : lance UNE seule fois', n['bon'] == 1)
    verifie('job echoue une fois : relance, puis fait (2 lancements)', n['un_echec'] == 2 and jobs[1].etat == 'fait')
    verifie('job qui echoue toujours : %d lancements puis ECHEC, signale' % (RELANCES_MAX + 1), n['toujours'] == RELANCES_MAX + 1 and jobs[2].etat == 'ECHEC' and reste == [jobs[2]])
    shutil.rmtree(tmp)
    print('SELFTEST : %s' % ('tous les controles tiennent' if ok else 'ECHEC'))
    return 0 if ok else 1


def commandes_chaine(reg, lot, out, cellules):
    return [PY, '-P', os.path.join(lot, 'chaine_cellules_pont_machine1_v1.py'), os.path.join(reg, 'scripts', 'm17_chaine_v17.py'), os.path.join(reg, 'scripts', 'chaine_ordre2_bloc_machine1_v1.py'),
            os.path.join(reg, 'scripts', 'ordre3_bloc_machine1_v1.py'), os.path.join(reg, 'scripts', 'chaine_adaptee_bloc_machine1_v1.py'), os.path.join(lot, 'chaine_pont_bloc_machine1_v1.py'),
            os.path.join(out, 'chaine_cellules_pont_v1.json')] + ['%s=%s:%d:%s' % (n, w2, m, g) for n, (w2, m, g) in cellules.items()]


def execute(cmd, log, jfile, desc):
    r = subprocess.run(cmd, capture_output=True)
    texte = (r.stdout + r.stderr).decode('latin-1')
    open(log, 'w', encoding='ascii', errors='replace', newline='\n').write(masque(texte))
    journal('%s : code %d' % (desc, r.returncode), jfile)
    return r.returncode


def feuilles(reg, lot, out, cellules, jfile, avec_verdict):
    """Les trois feuilles de machine 1, puis mes trois feuilles (ecrites du texte) a cote."""
    lj = os.path.join(out, 'journaux')
    chaine = os.path.join(out, 'chaine_cellules_pont_v1.json')
    for nom in cellules:
        execute([PY, '-P', os.path.join(lot, 'lecture_densite_2d_pont_machine1_v1.py'), chaine, nom, os.path.join(out, 'lecture_densite_2d_%s.json' % nom)] +
                [os.path.join(out, 'densite_2d_%s_%s.json' % (nom, a)) for a in 'ABCD'], os.path.join(lj, 'lecture_densite_%s.log' % nom), jfile, 'feuille de densite (m1) %s' % nom)
    fichiers_boites = sorted(f for f in os.listdir(out) if f.startswith('boites_') and f.endswith('.jsonl'))
    execute([PY, '-P', os.path.join(lot, 'lecture_boites_pont_machine1_v1.py'), os.path.join(reg, 'scripts', 'm17_chaine_v17.py'), os.path.join(reg, 'scripts', 'chaine_ordre2_bloc_machine1_v1.py'),
             os.path.join(reg, 'scripts', 'ordre3_bloc_machine1_v1.py'), os.path.join(reg, 'scripts', 'chaine_adaptee_bloc_machine1_v1.py'), os.path.join(lot, 'chaine_pont_bloc_machine1_v1.py'),
             os.path.join(out, 'lecture_boites.json')] + [os.path.join(out, f) for f in fichiers_boites], os.path.join(lj, 'lecture_boites.log'), jfile, 'feuille des boites (m1)')
    if avec_verdict:
        execute([PY, '-P', os.path.join(lot, 'verdict_pont_machine1_v1.py'), chaine, os.path.join(out, 'lecture_boites.json'), os.path.join(out, 'verdict.json')] +
                [os.path.join(out, 'lecture_densite_2d_%s.json' % n) for n in cellules], os.path.join(lj, 'verdict.log'), jfile, 'feuille de verdict (m1)')
    # mes feuilles, a cote
    mo = os.path.join(out, 'feuilles_machine2')
    os.makedirs(mo, exist_ok=True)
    execute([PY, '-P', os.path.join(HERE, 'chaine_pont_machine2_v1.py'), reg, os.path.join(mo, 'ma_chaine.json')] + ['%s=%s:%d:%s' % (n, w2, m, g) for n, (w2, m, g) in cellules.items()], os.path.join(lj, 'ma_chaine.log'), jfile, 'ma chaine')
    for nom in cellules:
        execute([PY, '-P', os.path.join(HERE, 'feuilles_pont_machine2_v1.py'), 'densite', os.path.join(mo, 'ma_chaine.json'), nom, os.path.join(mo, 'lecture_densite_%s.json' % nom)] +
                [os.path.join(out, 'densite_2d_%s_%s.json' % (nom, a)) for a in 'ABCD'], os.path.join(lj, 'ma_lecture_densite_%s.log' % nom), jfile, 'ma feuille de densite %s' % nom)
    execute([PY, '-P', os.path.join(HERE, 'feuilles_pont_machine2_v1.py'), 'boites', reg, os.path.join(mo, 'lecture_boites.json')] + [os.path.join(out, f) for f in fichiers_boites], os.path.join(lj, 'ma_lecture_boites.log'), jfile, 'ma feuille des boites')
    if avec_verdict:
        execute([PY, '-P', os.path.join(HERE, 'feuilles_pont_machine2_v1.py'), 'verdict', os.path.join(mo, 'lecture_boites.json'), os.path.join(mo, 'verdict.json')] + [os.path.join(mo, 'lecture_densite_%s.json' % n) for n in cellules],
                os.path.join(lj, 'mon_verdict.log'), jfile, 'mon verdict')


def main():
    mode = sys.argv[1]
    if mode == 'selftest':
        sys.exit(selftest())
    reg, lot = sys.argv[2].rstrip('/\\'), sys.argv[3].rstrip('/\\')
    if mode == 'plan':
        for j in fabrique_jobs(CELLULES, reg, lot, '<sortie>'):
            print('%-44s poids %.1f Go' % (j.nom, POIDS_GO[j.genre]))
        print('%d jobs' % len(fabrique_jobs(CELLULES, reg, lot, '<sortie>')))
        return
    out = sys.argv[4]
    if os.path.exists(out):
        print('REFUS : le dossier de sortie existe deja (un run ne se rejoue pas : E19)')
        sys.exit(1)
    args = sys.argv[5:]
    nb_jobs = int(args[args.index('--jobs') + 1]) if '--jobs' in args else 8
    budget = float(args[args.index('--budget-go') + 1]) if '--budget-go' in args else 12.0
    if mode == 'run':
        if '--feu-vert' not in args or not re.fullmatch(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', args[args.index('--feu-vert') + 1]):
            print('REFUS : le run exige --feu-vert "AAAA-MM-JJ HH:MM" (date et heure du feu vert ECRIT de l operateur)')
            sys.exit(1)
        cellules, essai = CELLULES, False
    else:
        cellules, essai = ESSAI_CELLULES, True
    os.makedirs(os.path.join(out, 'journaux'))
    jfile = os.path.join(out, 'run_pont_machine2.log')
    journal('MODE %s ; %d jobs a la fois, budget memoire %.1f Go%s' % (mode, nb_jobs, budget, '' if essai else ' ; feu vert ecrit : ' + args[args.index('--feu-vert') + 1]), jfile)
    if execute(commandes_chaine(reg, lot, out, cellules), os.path.join(out, 'journaux', 'chaine.log'), jfile, 'chaine (m1)') != 0:
        journal('ARRET : la chaine echoue', jfile)
        sys.exit(1)
    jobs = fabrique_jobs(cellules, reg, lot, out, essai=essai)
    journal('%d jobs' % len(jobs), jfile)
    reste = ordonnance(jobs, os.path.join(out, 'journaux'), nb_jobs, budget, os.path.join(out, 'etat_run.json'), jfile)
    if reste:
        journal('JOBS NON TERMINES : %s -- pas de feuilles' % [j.nom for j in reste], jfile)
        sys.exit(2)
    if essai:
        journal('ESSAI : sorties completes ; les feuilles ne sont pas passees (un essai n a pas les douze barreaux ni les vingt cotes)', jfile)
        return
    feuilles(reg, lot, out, cellules, jfile, True)
    journal('RUN TERMINE', jfile)


if __name__ == '__main__':
    main()
