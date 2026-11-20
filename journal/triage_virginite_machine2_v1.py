# -*- coding: ascii -*-
"""TRI des touches du balayage de virginite (machine 2). Chaque fichier touche est classe par son chemin dans une famille dont j'ai LU le contexte (journal contexte_touches_*.log et lectures
manuelles du 17/11) :
 A  gel du vide : tables d'eligibilite, tirages, certifications, balayages, lots du gel du vide (chaines a une dimension et listes) ;
 B  le present gel et le present lot de m1 (17a), mes propres dossiers de certification du pont ;
 C  coincidence numerique, contexte lu : valeur dans un tableau, nombre hexadecimal, duree, chiffres d'un Gamma, liste de valeurs d'un temoin ; aucun sens de w2 ;
 D  materiel d'explorations anciennes a une dimension (chaine E-A, lecteur creux au vide, pistes du 11 et 15/11) ou lecture de lots deja certifies, sans sortie 2D a un w2 candidat.
Un fichier non classe arrete le tri : il faut le lire. Lecture seule.
Usage : py -3.11 -I triage_virginite_machine2_v1.py <journal du balayage>"""
import re
import sys

FAM = [
    ('A', ['DEPOT_delta102', 'livraison_16f_', 'livraison_16g_', 'livraison_16h_', 'certif_gel_vide_partie1_machine2', 'certification_gel_vide_partie1', 'fabrique_lot_certification_gel_vide',
           'reg_pont/gels', 'gels/gel_largeur_vide', 'tirage_vide', 'eligibilite_vide', 'table_machine2_vide', 'detail_machine2_vide', 'table_eligibilite_vide', 'balayage_E19_vide', 'balayage_virginite_machine1',
           'lecture_eligibilite_vide', 'reception_certification_gel_vide', 'lot_d4f95772710d545c', 'eligibilite_candidates_vide']),
    ('B', ['livraison_17a_gel_pont_partie1', 'certif_gel_pont_partie1_machine2']),
    ('C', ['out_prevol', 'prevol_temoin', 'm2_v', 'm1_v', 'prevol_alpha', 'prevol_opposable', 'REPETITION_m1', 'diagnostic_pow', 'cause_ecart', 'reponse_cas_durs', 'reponse_globale', 'lot_117bcfaa1f283059',
           'diagnostic_v2_contre', 'P1_test_parite_signe', 'rejeu_excursion', 'excursion_parite', 'entrant_machine1_2026-09', 'lot_machine1_2026-09', 'lot_machine2_2026-09', 'lot_machine2_2026-08',
           'POUR_MACHINE1_P1', 'POUR_MACHINE2_instrument_bancs', 'banc_feuille_lecteur_sur_derivee', 'resultats_temoin_prevol', 'certif_boite2d_machine2', 'boite2d_et_laboratoire', 'reg_pont/runs',
           'journal_alpha', 'gel_v7_banc_v10', 'lot_machine1_2026-09', 'rejeu_complet_stdout']),
    ('D', ['chaine_EA_rejeu', 'rejeu_chaine_EA', 'bissection_39_20', 'point_39_20', 'point_41_20', 'lecteur_creux_m2', 'rejeu_absorbeurs_longs', 'lecture_piste0_etape0', 'exploration_v1', 'lecture_emulation',
           'note_piste0_reprise', 'lecture_resultat_machine2', 'nuit_EB_bis', 'lot_machine1_2026-11-11', 'DEPOT_delta94', 'DEPOT_delta95', 'DEPOT_delta99', 'DEPOT_delta100', 'livraison_16a_gel_loi']),
]
cnt = {k: 0 for k, _ in FAM}; non = []
for l in open(sys.argv[1], encoding='utf-8'):
    if not l.startswith('  '):
        continue
    ch = l.strip().split(' : ', 1)[0].replace('\\', '/')
    for k, pats in FAM:
        if any(p in ch for p in pats):
            cnt[k] += 1; break
    else:
        non.append(ch)
print('fichiers touches classes : A (gel du vide, 1D) %d ; B (present gel, present lot, mes certifications du pont) %d ; C (coincidences numeriques) %d ; D (explorations anciennes 1D / lots certifies) %d' % (cnt['A'], cnt['B'], cnt['C'], cnt['D']))
print('NON CLASSES : %d' % len(non))
for c in non:
    print('   ', c)
