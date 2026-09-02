# CERTIFICATION MACHINE 2 -- LE TEXTE NUMEROTE 86 ET LE LOT DE DEPOT
# Certifie journal_delta_86_sequence_P1_v3.md  bdd0a7333ca5de18  20038 o
# et le lot DEPOT_delta86_2026-09-02.zip  0c07d697d6f6f4a3  (neuf pieces).
# Classe 3 ; le depot est classe 1, de la main de l'operateur. E18.

Fichier : CERTIFICATION_machine2_delta86_v1.md
Date    : 02/09/2026
Emetteur: machine 2

-----------------------------------------------------------------------
## 0. VERDICT : DEPOSABLE
-----------------------------------------------------------------------

Le texte numerote se derive de la v3 certifiee (cb3536abfd52c1d6) par
exactement les quatre substitutions declarees, **plus un re-habillage de
lignes non declare, de contenu strictement nul** (section 2). Le
manifeste tient 8/8, le ZIP de depot porte les neuf pieces, le
contreseing leve le conflit de plume et retire le doublon de nom.

**DEPOSABLE.** Une seule reprise, d'une ligne, et elle est de forme.

-----------------------------------------------------------------------
## 1. LE CONTRESEING : CE QU'IL FERME
-----------------------------------------------------------------------

  - **Le conflit de plume est leve.** Machine 1 contresigne la v3 sur
    controle independant (quatre hunks, comptage des nombres, les deux
    hunks verifies avant que je ne les ecrive) et acte que A-3 et A-5
    sont de plume machine 2, ce que l'en-tete du delta dit. Rien ne
    passe pour du machine 1 qui ne le soit. C'etait la seule piece qui
    manquait a la chaine ; elle ne manque plus.
  - **Le doublon de nom est retire.** Machine 1 avait produit dans le
    meme tour une autre v3 (f7a163e7cef65bd3, 19496 o) sous le MEME NOM
    -- la forme exacte de D-P1-5, et elle le nomme ainsi. Retiree, non
    deposable, trace conservee au contreseing. **La v3 est
    cb3536abfd52c1d6, et elle seule.** Je confirme avoir les deux
    fichiers et ne pas les avoir confondus : le mien n'a pas ete ecrase.

-----------------------------------------------------------------------
## 2. LA DERIVATION DU TEXTE 86 : REPRODUITE, ET UN ECART DE FORME
-----------------------------------------------------------------------

J'ai rejoue les quatre substitutions sur cb3536abfd52c1d6 :

    (i)   \bnn\b -> 86 : **18 occurrences**, exactement le compte annonce ;
          zero "nn" residuel dans le resultat ; aucun "nn" interne a un
          mot touche.
    (ii)  le nom de fichier en ligne finale ;
    (iii) la phrase de prise de numero ;
    (iv)  "-- PROJET, VERSION 3" -> "-- VERSION 3 (DEPOSEE)" ; zero
          "PROJET" residuel.

Ma reproduction rend **24eedfb2d9849673**, la sienne **bdd0a7333ca5de18**.
**Elles ne sont pas identiques au bit.** L'ecart, localise :

    identiques jusqu'a la ligne 18 ;
    lignes 19-20 chez moi, 19-21 chez elle : le paragraphe touche par la
      substitution (iii) est RE-HABILLE (les sauts de ligne sont
      redistribues pour tenir la colonne ~72) ;
    a partir de ma ligne 21, tout coincide avec sa ligne 22 :
      **291 lignes sur 291, decalage constant de +1.**

Ce que le re-habillage change, exactement :

    memes octets au total          20038 = 20038
    memes caracteres non blancs    15207 = 15207
    texte a espaces normalises     IDENTIQUE
    une ligne de plus, dans UN paragraphe

**Contenu : rien. Aucun mot, aucun chiffre, aucune empreinte.** Mais le
contreseing ecrit "**Aucun autre caractere ne change**", et c'est
litteralement faux : des positions de saut de ligne changent. La
reprise, d'une ligne, a porter au contreseing avant depot :

    "...(iv) ... Aucun autre caractere ne change, hormis le
     re-habillage des lignes du paragraphe touche par (iii) : une ligne
     de plus, meme nombre d'octets, texte identique a espaces
     normalises."

Je le releve parce que c'est exactement la clause sur laquelle
l'operateur s'appuie pour deposer sans relire, et parce que la sequence
entiere a tenu sur des enonces d'exactitude verifiables. Ce n'est pas
bloquant : la derivation est bonne, et je viens de la refaire.

-----------------------------------------------------------------------
## 3. LE LOT DE DEPOT
-----------------------------------------------------------------------

Manifeste c149363c84ec55f6 : **8 empreintes sur 8 resolvent**, y compris
le binaire e61c778c1e21a68b (qui ne resolvait que dans Downloads : il
est desormais DANS le ZIP de depot, ce qui solde le point (iv) de ma
certification v3).

DEPOT_delta86_2026-09-02.zip 0c07d697d6f6f4a3, neuf pieces, toutes
conformes a leur empreinte :

    bdd0a7333ca5de18  journal_delta_86_sequence_P1_v3.md      <- au journal/
    cb3536abfd52c1d6  journal_delta_nn_sequence_P1_v3.md      la v3 source
    9617f12ca230c74f  CERTIFICATION_machine2_..._v3.md
    47974fc9a0127113  CONTRESEING_machine1_..._v3_v1.md
    26056845c8af61cf  ACTE_P1_cloture_machine2_v1.md
    e4997594734239f1  CONTRESEING_machine1_acte_P1_v1.md
    1e4f296c38accfcb  ANNEXE_P1_cloture_contreseing_machine2_v1.md
    c149363c84ec55f6  MANIFEST_DEPOT_delta86_machine1.txt
    e61c778c1e21a68b  lot_machine1_2026-09-02_P1_reponse_v3.zip

Forme du texte 86 : ASCII pur, LF seuls (zero CRLF), saut final present.

-----------------------------------------------------------------------
## 4. LES DEUX RESERVES QUI RESTENT, ET ELLES SONT A L'OPERATEUR
-----------------------------------------------------------------------

  (a) **LE 86 EST CONDITIONNEL**, et machine 1 l'ecrit dans le texte
      lui-meme : "sous reserve qu'aucun delta n'ait ete depose apres
      a4a907a (git log au depot)". Mon clone n'est pas un clone -- le
      dossier `registre/` a ete peuple par `curl` a l'arbre a4a907a --
      donc **je ne peux pas verifier que 86 est libre**. C'est le
      dernier controle, et il se fait au depot, par vous.
  (b) **L'avis d'arbitrage de sa section 4 est un AVIS**, pas une
      decision : (a) (b)+(c) (e) (f) (g) a adopter, (d) a reporter,
      avec deux numeros N proposes et une date de revue au 28/09. Ni
      machine 1 ni moi ne les arbitrons. Je note seulement que son
      decompte "premiere / seconde exception sous (X)" est coherent, et
      que sa proposition de fusionner (b) et (c) en une regle
      ("l'estimateur et la fenetre T font partie de la mesure") est la
      bonne : ce sont deux faces du meme fait, et la sequence les a
      payes ensemble (A-7 ii et A-5).

-----------------------------------------------------------------------
## 5. FIN DE MA PART
-----------------------------------------------------------------------

Sous la reprise d'une ligne de la section 2, le lot est **DEPOSABLE**.
Je n'ai pas d'autre reserve, et je n'emets plus de piece sur P-1 :
l'acte, l'annexe, les trois certifications et celle-ci ferment ma part
de la sequence. Le depot, le numero, les series et les sept propositions
restent de votre main.

-- FIN CERTIFICATION_machine2_delta86_v1 --
