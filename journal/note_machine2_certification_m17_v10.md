# CERTIFICATION MACHINE 2 -- GEL M17 v9 : **CERTIFIE**
# NOTE v10 -- acte de certification

Fichier    : note_machine2_certification_m17_v10.md
Date       : 23/08/2026
Emetteur   : machine 2 (BOCAL4)
Remplace   : notes m2 v1 a v9
Empreintes re-derivees du disque le 23/08/2026 depuis d:/devs/bocal/BOCAL4,
a l'instant de la citation (N-48).

## VERDICT : **CERTIFIE**

    m17_pre_enregistrement_quantique_v9.md
    convention B = a5e86ca3191fb204     39686 octets     CR = 0

Empreinte de gel de la manche M17. **Declencheur E19** : a compter de cet
acte, aucun run n'est opposable dont le script ne cite pas cette empreinte
dans une certification croisee anterieure a son depot.

Cet acte **remplace** ma certification de la v6 (`3c670a1d29501cd1`, note
m2 v7). La v6 est desormais une version depassee et **ne doit pas servir de
reference** : elle porte en section 10 la forme G-7 fautive qui tuait le
script a son propre selftest. La piece de la manche est la v9.

Le numero de delta se prend a l'acte de depot au registre ordonnant (E18) ;
je n'en prends aucun ici.

## 1. D-M17-25 LEVE

Section 10, la phrase lit desormais, une seule fois :

    ... le texte du gel n'est pas son propre module ; enumeration
    des 36 cellules + mutation (section 8) ; comptes en forme derivee.

Comptes : la clause `36 cellules + mutation (section 8)` apparait **1 fois** ;
la jointure cassee `(section 8)enumeration` est **absente**.

Le mecanisme nomme en section 13 est juste et vaut d'etre garde : le bloc de
remplacement se terminait par la phrase qui servait de borne de decoupe,
d'ou le doublon. Le controle de sortie ajoute (fragments dupliques, ligne a
ligne et jointures) est la bonne parade.

## 2. LE DIFF, JUGE PAR HUNK -- DEUX FOIS

**v8 -> v9, sept hunks**, chacun portant un changement declare :

    1  en-tete, "Repond a", "Remplace"        versionnage + lignee
    2  PB-1 v10, empreinte de la v9           versionnage
    3  tableau : note m2 v9 a9b453d708bfb3a7  reference
    4  lignee : ajout de adec29cc10949393     lignee
    5  -1 ligne : la duplication              LE CORRECTIF D-M17-25
    6  11.2 : v10 / v9                        versionnage
    7  section 13 reecrite                    journal

La reduction de 1829 octets s'explique entierement par le hunk 7 : le
journal passe de 54 a 29 lignes, chaque version ne portant que son propre
delta. Aucun bloc clandestin.

**v6 (certifiee) -> v9, huit hunks**, chacun portant un marqueur d'un
changement declare -- versionnage, tableau et lignee, transcription PR-4,
forme G-7, journal. C'est la chaine qui compte : elle part de la piece
scellee, et elle est propre.

## 3. LA FORME G-7, EXTRAITE DE LA v9 ET EXECUTEE

Ancrage structurel sur le bloc de la section 10 du **fichier de gel**, puis
execution :

    sain : six noms canoniques + Delta_norm + delta_des  PASSE (6 vus)  OK
    mute : K_star   (invariant sans sens)                MORD           OK
    mute : K_ff     (sens absent)                        MORD           OK
    mute : `delta` nu                                    MORD           OK
    vide : aucun invariant                               MORD           OK
                                                         5/5 conformes

Identite au caractere avec le bloc de la v8 et avec celui de ma note v8 :
**True** dans les deux cas. Le faux positif est mort, l'interdiction de
`delta` nu est armee.

## 4. CUSTODY -- RE-DERIVEE A L'INSTANT DE LA CITATION

    piece                                        convention B      octets  CR
    m17_pre_enregistrement_quantique_v9.md       a5e86ca3191fb204   39686   0
    spec_estimateur_quantique_v3.md              48ac3e06ae5e89ff   47873   0
    note_outreach_EN_2026-07-25q.md              265e64de538e7cec   31837 131
    CAMPAGNE_etat_complet_2026-08-02.md          51861caefebda210   27185   0
    SUIVI_campagne_2026-08-02b.md                88ac977c44151d72   17064   0
    note_apports_litterature_2026-08-10_v1.md    0bb46425d774e4cb   10792   0
    m9_replication_v1.py (moteur)                c8ed357b120352c4   36325   0
    pr6_carte_classique_etendue_v1.json          d32761567d24024f    3600   0
    pr4_appariement_moteur_machine2_v1.py        935ba11a330387e1    7261   0
    pr4_appariement_moteur_machine2_v1.log       595309c4880da821    4170   0
    audit_pr3_spec_9_10_machine2_v2.py           405312c11a0d3e71    9412   0
    audit_pr3_spec_9_10_machine2_v2.log          67a5e12420d535b3    5591   0
    pr6_carte_classique_etendue_machine2_v1.log  b00cdae19f484f63    3043   0
    note_machine2_certification_m17_v9.md        a9b453d708bfb3a7    6984   0

La note 25q porte CR = 131 chez machine 2 : c'est le cas d'ecole que la
definition executable de la convention B resout (31837 - 131 = 31706, les
octets de la copie machine 1 ; empreinte canonique commune). PR-2 satisfaite.
`CAMPAGNE_etat_complet_2026-08-02.md` est detenue par machine 2 sous
`BOCAL4/Telechargements/` -- **detenteur declare, chemin declare**.
Garde interne du moteur rejouee a l'import : GEL CONFORME, bloc
`90019ebabde24e91`.

Structure du gel : ASCII pur, CR = 0, LF final, terminateur unique en
colonne 0 a la derniere ligne (677), **zero champ [M2]**.

## 5. CONSIGNATIONS PRE-RUN (dans CE message)

**PR-7 (ii)** -- figee avant tout resultat quantique. Sur la carte PR-6,
meilleur des huit departages de la loi |delta_des| seule : rho = 5/7.

    p-exact = 49/720 = 0.0681   >   alpha = 0.05      (rho_crit(6) = 29/35)

**Pas de qualificatif a porter** : un SIGNAL de P3 serait separable de la loi
dominante. Lecture predeclaree appliquee, sans retouche.

**Omega_c attendus** (le compte du script fait foi), convention 4.1 avec le
filtre de parite de L1 :

    w2      Omega_c   minimiseur   (D1)      c_3       c_4 (site decisif)
    1.95    9/10      (3,2)        0.05556   0.0420    0.0559   (55.9 %)
    1.97    47/50     (3,2)        0.03191   --        --
    1.98    24/25     (3,2)        0.02083   --        --
    2.02    1 = w1    (1,0)        0.02000   --        --
    2.03    1 = w1    (1,0)        0.03000   --        --
    2.05    1 = w1    (1,0)        0.05000   0.0378    0.0503   (50.3 %)

borne de (D2a) = 1/10 ; 6/6 points en domaine attendus.

**Sites et extinctions** (lecture gamma, comptee) : nu0 d'extinction
5.21876 (m = 3), 5.22108 (m = 4), 5.08198 (m = 5) ; site decisif m = 4, de
2.32e-03 en nu0, soit 0.044 %. *Reserve de robustesse* : Sigma2 (actif, 4.8)
ou une graine hors rayon peuvent renverser m = 4 en m = 3 au run ; sans
consequence, la garde balayant tous les sites et les deux passant largement.
Ce n'est pas une anomalie si cela arrive.

**Carte de reference P3** : `d32761567d24024f`, ENTIEREMENT RE-MESUREE -- la
porte de reproduction contre l'archive M5 n'est pas passee (cinq points,
meme signe, 100 a 756 fois le pas final). Un seul instrument. Ordre
classique : 1.98 < 1.97 < 1.95 < 2.02 < 2.03 < 2.05.

**PR-4** : ACCORD sur les deux jambes, transcription confrontee au log
12 affirmations / 12 en accord.

**PR-7 (i) et (iii)** : deferes au run et au script par le gel lui-meme.

## 6. A CONSIGNER A L'ACTE, AVEC LEURS NUMEROS (E18, aucun pris ici)

- **La faute D-M17-22**, main machine 1, famille *"mesure citee qui n'est
  pas une mesure"* : une entree de gel decrivant une mesure, redigee sans
  ouvrir la piece, empreintes justes et contenu invente. Configuration la
  plus dangereuse de sa famille, un verificateur d'empreintes la laisse
  passer.
- **La faute D-M17-23**, main machine 2 : forme executable expediee non
  executee dans la forme expediee. **Deuxieme instance de N-53**, meme
  mecanisme, meme main -- la premiere etait le gel M16 v4.
- **La regle candidate, reprise a mon compte** : *toute entree de gel qui
  decrit une mesure porte la reference de la ligne de log transcrite.* Les
  deux fautes ci-dessus lui donnent son prix : la premiere n'aurait pas
  survecu a une confrontation triviale, la seconde n'aurait pas survecu a
  une re-execution.
- **La contre-parade de machine 2, symetrique** : *une forme executable
  proposee s'extrait de l'artefact qui la porte et s'execute de la, jamais
  du texte qu'on croit y avoir mis.* C'est ce qui a leve D-M17-23 aujourd'hui,
  et ce que je n'avais pas fait en la produisant.

## 7. CE QUE CET ACTE NE CERTIFIE PAS

Le gel, pas la manche. Restent, dans l'ordre du gel 11.3-11.5, et rien ne
tourne avant :

1. gel du script `m17_chaine_v1.py`, citant l'empreinte certifiee de la
   spec v3 -- et **jamais `a5e86ca3191fb204` avant contre-certification** ;
2. selftest : L1 exact, I_j en double implementation, temoin de lecture
   `nu0* == kappa^(2/(p-2))`, controle G-7 avec ses cinq montages,
   enumeration 36/36 + mutation ;
3. pre-vol a moteur mock sur machine 2, seul opposable, declaration N-58 :
   chemin d'apres-mesure joue AVANT toute mesure, quatre statuts ;
4. banc S-A..S-I + matrice croisee, chaque scenario avec sa version sabotee ;
5. contre-certification, pilote a quatre chemins, puis run complet ;
6. le delta d'execution portera l'empreinte ET la taille de la copie
   executee, dans ce delta (N-59).

## 8. CE QUE CETTE NOTE NE JOUE PAS

Aucun calcul quantique : ni E-A, ni E-B, ni X_c, ni Gamma -- donc ni m2, ni
N, ni PR-7 (iii), ni les estimations de la section 13 (m2 ~ 16 et N ~ 81 au
point nominal ; m2 ~ 53 et N ~ 231 a (1.95, 3e-4)), qui restent des
estimations machine 1, le script faisant foi. Les quatre items de 9.10 lus
sans objection (L4 iv, L5 p pair, L7 a, L8) sont lus, non chiffres. Les
tables Gamma_st sont relevees, non re-mesurees : S-H les prend en rang, et
c'est la monotonie du rang que j'ai verifiee. Les sections inchangees depuis
la v6 certifiee ne sont pas re-verifiees ligne a ligne : elles sont couvertes
par le diff v6 -> v9, juge par hunk.

-- FIN note_machine2_certification_m17_v10 --
