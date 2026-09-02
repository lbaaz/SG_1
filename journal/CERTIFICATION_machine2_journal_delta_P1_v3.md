# CERTIFICATION MACHINE 2 -- JOURNAL DELTA nn v3 (SEQUENCE P-1) -- PRET AU DEPOT
# Certifie journal_delta_nn_sequence_P1_v3.md  cb3536abfd52c1d6  19981 o
# Remplace mes certifications v1 4f7c52ac9279f161 et v2 928c9e67ede3e30e,
# non editees. Classe 3 ; le depot est classe 1, de la main de l'operateur.
# E18 : aucun numero pris.

Fichier : CERTIFICATION_machine2_journal_delta_P1_v3.md
Date    : 02/09/2026
Emetteur: machine 2

-----------------------------------------------------------------------
## 0. VERDICT : PRET AU DEPOT, SANS RESERVE DE FOND
-----------------------------------------------------------------------

C-1', C-2 et C-3' sont refermees. Aucune reserve ne subsiste de mon cote
sur le contenu. **UN POINT DE PROCEDURE, ci-dessous en 1, doit etre lu
avant le depot : la v3 est de ma main.**

-----------------------------------------------------------------------
## 1. CONFLIT DE PLUME, DECLARE
-----------------------------------------------------------------------

La v3 n'est pas de machine 1 : **j'ai applique moi-meme C-1' et C-3'** a
sa v2, dans la formulation de ma certification v2. Je certifie donc un
texte dont deux paragraphes sont de moi.

**Ce que cela vaut, exactement** : ma certification de ces deux hunks
n'est PAS un controle independant -- c'est un controle de soi. Ce qui
reste independamment verifiable, et que j'ai verifie, est que le diff
**ne contient QUE** ces deux hunks (plus l'en-tete de version et la
ligne finale) :

    diff v2 -> v3 : QUATRE hunks
      @@ -4,13 +4,17 @@     en-tete : numero de version et note de remplacement
      @@ -100,18 +104,21 @@  nn.2 A-3   (C-1')
      @@ -128,8 +135,14 @@   nn.2 A-5   (C-3')
      @@ -294,4 +307,4 @@    ligne finale
    empreintes : 43 communes ; retiree 7b2054fac9e1b61a (lot de ma
      certification v1, remplace) ; ajoutees 928c9e67ede3e30e (ma
      certification v2) et e5d56ef55800c2ef (la v2, citee comme
      remplacee) -- les trois dans le seul en-tete.
    nombres hors des deux hunks de fond et de l'en-tete : **aucune
      difference**, sauf "version 2" -> "version 3".

**Le geste propre serait un contreseing de machine 1 sur la v3.** Elle a
declare ne plus emettre ; si l'operateur veut la chaine complete, c'est
la seule piece qui manque. Si l'operateur depose sans, **le delta doit
porter que ses paragraphes A-3 et A-5 sont de plume machine 2**, comme
la presente section le dit -- et non passer pour du machine 1.

-----------------------------------------------------------------------
## 2. LES TROIS CORRECTIONS, REFERMEES
-----------------------------------------------------------------------

  C-1'  nn.2 A-3. Le critere de recevabilite est desormais pose sur
        **l'ajustement seul** (B eps/F0 <= 0.04), avant de regarder
        l'ecart ; il retient **NEUF** colonnes ; sur ces neuf, l'accord
        est meilleur que 0.6 % sur **SIX** (2:1, degres 5, 7, 9, deux
        signes) et **sort de la barre sur TROIS**, qui sont nommement
        R-2 ((2,1;11)) et R-1 ((4,1;7) signe -1). Le critere ne contient
        plus son resultat ; les echecs sont comptes avec les reussites ;
        et la restriction de portee de la v2 ("un site a trois degres,
        pas plusieurs sites") est conservee.
  C-2   nn.2 A-4. Inchangee depuis la v2, ou elle etait juste : B de 2 a
        6 aux huit colonnes 2:1 ; de 0.3 a 157 aux dix autres directes ;
        la dichotomie "petit B au site, grand ailleurs" est niee.
  C-3'  nn.2 A-5. L'ecart de 1.4 % est desormais attribue au **terme B
        de A-4** : eps T = F T/(T - B) = F (1 + B/(T - B)), soit
        +1.47 % pour B = 5.78 a l'ancre deposee, mesure +1.36 %. La
        fausse explication (le pas de grille) est **ecartee
        explicitement**, avec son chiffre : elle porterait l'ecart a
        +5.22 %. Et le delta note que c'est la troisieme occurrence du
        meme terme B, apres A-1 et A-4.

-----------------------------------------------------------------------
## 3. CE QUI RESTE A L'OPERATEUR AVANT ET PENDANT LE DEPOT
-----------------------------------------------------------------------

  (i)   **Le numero.** "nn" n'est pas un numero ; il se prend a l'acte
        (N-68). Le delta s'insere apres le delta 85 (a4a907a).
  (ii)  **L'attribution des series.** Aucun N, E ni D n'est pris ; les
        files libres relevees sur a4a907a sont N > 70, E > 45,
        D-M17 > 58. Les defauts portent leurs etiquettes de chantier
        (D-P1-1..5, N-P1-a) et attendent l'attribution si l'operateur en
        decide.
  (iii) **Les sept propositions de nn.6** : non arbitrees, ni par
        machine 1 ni par moi.
  (iv)  **e61c778c1e21a68b** (ZIP de reponse machine 1) : cite au delta,
        mais ne resout que dans Downloads. **A verser au registre.**
  (v)   **c9fc0815cba888dc** : ce n'est pas un fichier (canon du JSON
        hors champ `duree`). Le delta le dit desormais en nn.1 ; il ne
        doit pas etre cherche comme piece.
  (vi)  **La dette de canal est soldee** : la reemission
        62a9850e43133478 porte les lots v2 et v4.

-----------------------------------------------------------------------
## 4. CE QUE JE NE PEUX PAS FAIRE
-----------------------------------------------------------------------

**Je ne peux pas deposer.** Il n'existe aucun clone git local (le
dossier `registre/` de BOCAL4 a ete peuple par `curl` depuis
lbaaz/SG_1 a l'arbre a4a907a, pas par un clone), je n'ai aucun droit de
poussee, et la convention de la campagne place le depot et le numero a
la main de l'operateur. Ce lot est l'etat pret au depot, pas un depot.

-- FIN CERTIFICATION_machine2_journal_delta_P1_v3 --
