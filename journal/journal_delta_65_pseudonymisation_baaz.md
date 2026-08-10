JOURNAL DELTA 65 -- PSEUDONYMISATION DU DEPOT PUBLIC, NOTE e,
README QUARTIQUE EN PAR DEFAUT (machine 2, 2026-08-10)
=======================================================================
S'insere apres journal_delta_64_revue_note_c.md.

65.1 DECISION OPERATEUR (post-publication du depot)
   Toutes les occurrences du prenom et du nom de l'operateur sont
   remplacees par le pseudonyme "baaz" sur L'ENSEMBLE de l'historique
   public ; l'email est retire de la copie publique de la note (la
   copie de correspondance, envoyee par mail, reste signee par
   l'auteur). Motif : pseudonymat du depot public ; l'identite reste
   communiquee en prive aux destinataires.

65.2 MECANIQUE DE LA RE-COUPE
   Les trois commits (v1/v2/v3) sont reconstruits, les MANIFEST
   regeneres, les tags re-etiquetes, l'historique force-pousse.
   L'ancienne coupe (manifeste 88ed9158f3681cd9...) n'est plus servie
   par le depot ; des clones antecedents peuvent exister ; le tar.gz
   remis a machine 1 correspond a l'ancienne coupe -- ecart de
   custody CONSIGNE, pas cache. Substitution de nom SEULE aux etages
   v1/v2 ; les changements editoriaux ci-dessous vivent au seul
   etage v3.

65.3 FICHIERS MODIFIES (sha16 ancien -> nouveau)
     journal/journal_delta_59_stop_pieces.md : 10efa4b4c9e277a8 -> 19db329be0d247a0
     journal/journal_delta_60_montage_arbitrages.md : b67c2776756a4ccd -> 1161b385923d096e
     journal/journal_delta_64_revue_note_c.md : f4552c5f6fe40446 -> a33fe404b81552a1
     journal/registre_de_coupe_bundle_v1.md : 1fe303909f4455fb -> 1629bfc2b2aecf39
     journal/revue_pre_envoi_2026-08-10b_machine2_v1.md : 81cdb7c6c96ba623 -> 1344c0ff52c00e13
     notes/note_outreach_EN_unified_2026-08-10d.md : 74950a6b6912699c -> 4e51d08af0145c7b
     quartic-bundle-MANIFEST-2026-08-10.sha256.txt : f2c95d299d42c0a6 -> 2b9f89ff1d392acf
   Les references de custody pointant vers les anciens sha16 depuis
   des fichiers NON modifies (journal_delta_60 et note_machine2_
   coupe_montage_v1.md vers delta 59 et le manifeste quartique ;
   delta 59 vers le registre de coupe ; delta 64 vers la revue v1)
   deviennent HISTORIQUES : elles decrivent la coupe d'origine et ne
   sont pas reecrites.

65.4 CHANGEMENTS EDITORIAUX (etage v3 seulement)
   (a) Note publique : version e (signature pseudonyme, empreinte
       v1 mise a jour en section 8, mention de la re-coupe).
   (b) quartic-bundle : README anglais par DEFAUT (README.md),
       version francaise conservee (README_FR.md), entrees du
       manifeste quartique permutees en consequence, renvoi du
       changelog FR mis a jour. Ecart au "unchanged" du contrat A :
       DOCUMENTATION SEULE, aucun script ni donnee touche.
   (c) README racine : note (e), deltas 1..60+64-65, contact via
       GitHub, renvoi README quartique.
   (d) journal/revue_pre_envoi_2026-08-10b_machine2_v1.md mise a
       jour vers l'etat v1.1 (addendum H : validation de la
       version d, cloture A3, validation PDF).

=== FIN DU JOURNAL DELTA 65 ===
