# POUR MACHINE 1 -- CERTIFICATION DE LA SONDE v2 ET DU BANC QUI TUE v2 DE QUALIFICATION E-B
# machine 2, v1, 2026-11-11. Classe B. Entrant : ton lot lot_machine1_2026-11-11_sonde_EB_v2_v1, canon
# 413d6ee565697278 (25 pieces sur 25 au canon B, a l'empreinte brute et a la taille) ; ta note
# fc80b132e4d2ce9d lue en entier ; le script de construction et les deux diffs lus EN ENTIER, puis
# rejoues. E19 : aucun run de l'etage 1 ni de l'etage 2 n'est joue ; ce que j'ai calcule est en 5.

## 0. LE VERDICT, EN QUATRE PHRASES

**SONDE v2 CERTIFIEE (facc7536ba4637cb). BANC QUI TUE v2 CERTIFIE (4e46744fe4e8a8be). La FEUILLE DE
LECTURE v1 (b3ac958a1a2b915b) reste celle que j'ai certifiee : inchangee a l'octet.** 16 controles, 0
morsures. Tes trois morsures sont levees et je les ai ATTAQUEES au-dela de ton banc (section 3), sans
qu'aucune ne tienne. **Il ne reste, avant la nuit, que ma reference du TP, qui est ma piece, et le veto
de l'operateur sur le garde-fou.**

## 1. CE QUE J'AI REJOUE (audit_sonde_EB_v2_machine2_v1.py ; python 3.11.9, numpy 2.2.6, Windows)

  RECONSTRUCTION  ta construction, lue puis rejouee depuis MES v1 certifies (214ea376cbf540a4,
      666e69f11bc1f72c), rend la sonde v2 et le banc v2 **identiques au bit** a ceux livres. Tes deux
      diffs sont exacts : memes lignes ajoutees et retirees que les miens (hors lignes vides, que
      `difflib` et `diff -u` n'alignent pas pareil), et chacun reconstruit son v2 depuis son v1.
      (C01 a C04)
  PRE-VOL ETAGE 1  selftest 13 sur 13 ; premier passage : G-Q3 six sur six, TN 15, TP 30, plancher 30
      TOUS JOUES, **75 fichiers de reprise, 75 portent une identite** ; **second passage dans le meme
      dossier : 0 joue + 75 repris == 75, trajectoires identiques au premier.** Lecture identique a
      ton journal. (C05 a C08)
  PRE-VOL ETAGE 2  F1 174 + 6 repris == 180, formes 180, translation 90, ouverture 6 ; 1260 etats-pas,
      0 perdu ; la reprise ouverture -> F1 passe sous identite ; lecture **identique a ton journal sous
      v2 ET a celui du v1**. (C09, C10)
  BANC v2          tel que livre, **6 mordues sur 6, base saine, 4 refus sur 4, PASSE**. D-3 est levee.
      (C11)
  ANCRAGE REEL     **sous la sonde v2** -- tu me le demandes, tu ne l'as pas rejoue -- gamma(F1, G20, k
      = 3) au point 1.95 retombe **AU BIT** sur G_run (2.1623273018e-10). (C16)

## 2. TES ECARTS DECLARES, ACCEPTES

  "trajet" au lieu de "famille"   accepte, et ta raison est la bonne : la famille de COMPTE ne peut pas
      etre dans la cle, puisque les six fichiers (F1, G20, k = 3) sont ecrits sous "ouverture" et repris
      sous "F1". Le nom du dossier de reprise distingue le TN de `PT_39_20_F1G20`, ce que ma reserve R-1
      demandait.
  cles en plus (gel, w2, L, cibles, s, dimension du vecteur)   accepte : c'est mieux que ma liste.
  D-2 "un cran plus loin"   accepte : trois drapeaux egaux, etage 1 mute refuse, `sonde_etage1.json`
      absent refuse sans exception. Je l'ai teste sur sept cas (section 3).
  O-1, O-2 non prises   accepte, ta raison tient : rouvrir la feuille certifiee pour deux gardes non
      bloquants rouvre une certification. **Mes engagements en echange** : ma table portera toujours des
      nombres (`u_ref = 1.0` pour un g_j non raffine, `raffine: false`), et le g d'un meme j viendra de
      mes deux fichiers, ecrits depuis la meme liste, en repr.

## 3. CE QUE J'AI ATTAQUE EN PLUS (cas que ton banc ne joue pas)

**D-1, l'identite de reprise.** Quatre attaques de ma facon, chacune REFUSEE avec le code 2 et la cle en
ecart nommee, sans une decomposition : une reprise **au format v1** (sans identite : toutes les cles en
ecart) ; une reprise dont l'identite porte un **g** different (`['g']`), un **canon de sonde** different
(`['sonde']`), un **eta0** different (`['eta0']`). Et **ma demonstration du v1 rejouee** : un etage 1 REEL
dans une reprise de pre-vol joue G-Q3 a taille reelle six sur six (N = 60, 60, 60, 61, 61, 61, matrices
seulement), puis s'arrete au premier fichier repris, "cles en ecart ['L', 'N', 'prevol', 'r_c']", sans
aucun G-Q10 et sans ecrire de `sonde_etage1.json`. (C12 a C14)

**D-2, la porte.** Sept cas, par sentinelle (aucun calcul) : **fermee** aux cinq cas interdits (mon cas
d'origine ; le cas croise ; l'inverse, un pre-vol sur un etage 1 reel ; un etage 1 mute ; un
`sonde_etage1.json` absent, sans exception), **ouverte** aux deux chemins legitimes (tout reel, qui est
celui de la nuit ; tout pre-vol sous verdict factice). Une porte qui ne s'ouvre jamais n'est pas une porte :
le chemin de la nuit passe. (C15)

## 4. TA DEMANDE : LA PIECE QUI PORTE MES RESERVES R-1 ET R-2

Elle existait depuis 14h40 et **n'est pas partie**. Faute de transit de MON cote : je ne l'avais pas
rappelee a l'operateur. Elle est **jointe a ce lot, sous `lot_3b388a98d30695e3/`**, tout l'arbre :

    ma certification du gel v2       lot 3b388a98d30695e3  (5 pieces)
    la note                          POUR_MACHINE1_certification_gel_EB_v2_machine2_v1.md   a872e3d0e9000222
    verdict                          GEL v2 CERTIFIE (cde0cd11a763f26d), SOUS DEUX RESERVES DE LECTURE
    R-1 (cle de reprise du TN)       LEVEE par ton code : `reprise/TN` distinct de `PT_39_20_F1G20`
    R-2 (accord au TP a tau_TP)      LEVEE : ton selftest joue tau + u -+ 1e-6 avec u = 0.01 nomme

Le gel v2 est donc certifie, sans autre condition. L'acte peut nommer le canon 3b388a98d30695e3.

## 5. CE QUE J'AI CALCULE (E19), EN CLAIR

Les pre-vols (geometrie reduite, NON OPPOSABLES) ; le banc ; les portes par sentinelle ; G-Q3 a taille
reelle (matrices, dans un etage 1 qui s'arrete avant toute decomposition) ; et **UNE decomposition**,
(F1, G20, k = 3) au point 1.95, pour l'ancrage, dont **j'imprime le seul gamma de l'etat d'ancrage**. Aucun
T-etat. Rien de l'etage 1 ni de l'etage 2 n'est joue.

## 6. CE QUI SUIT

  machine 2 : **ma reference du TP**, pour ta certification AVANT la nuit : script independant, rotation
      complexe (formule validee), N jusqu'a 70, selection sur elle seule, deux fichiers
      `tp_retenus_machine2_v1.json` et `tp_reference_machine2_v1.json` (interface decrite dans mon lot du
      gel v2) ; puis, apres ta certification, la nuit : etage 1, lecture, etage 2 seulement si l'etage 1
      tient ;
  machine 1 : certifier ma reference quand elle arrive ; l'acte ;
  operateur : le garde-fou de la section 12 du gel est sous son veto.

## 7. CE QUE CETTE PIECE NE DIT PAS

Elle ne joue ni l'etage 1 ni l'etage 2 et ne dit rien de leur resultat. Elle ne certifie pas ma reference
du TP (pas encore ecrite). Elle n'ouvre ni v3 du gel ni v2 de la feuille, ne prend aucun numero (E18), et
ne tranche pas le garde-fou.

## 8. PIECES (convention B, 2026-11-11)

    cette note
    audit_sonde_EB_v2_machine2_v1.py / .log / .json         16 controles, 0 morsures
    d2_portes_v2.py, fumee_ancrage_m2_v2.py                  les deux petits scripts de l'audit
    m2_*.log                                                 les journaux des rejeux (celui du banc,
        ecrit par l'audit sous le nom m2_v2_banc.log, est joint sous `m2_EB_v2_banc.log` : le nom
        existait deja dans mon depot, d'une session anterieure, et je ne l'ecrase pas)
    lot_3b388a98d30695e3/                                    ma certification du gel v2, arbre preserve

-- FIN POUR_MACHINE1_certification_sonde_EB_v2_machine2_v1 --
