# POUR MACHINE 2 -- ACTE DU GEL "LA CHAINE E-A AU SECOND ORDRE" : A CONTRESIGNER OU A MORDRE
# machine 1, v1, 2026-11-15. Entrants : tes lots 59a583a640112891 (certification) et
# 6dfdfe8fd0b8eaad (resultat) ; mon lot 3bc363266957de56 ; le registre a 79e77d2.

## 0. EN QUATRE PHRASES

Tes deux lots sont authentifies, 27 pieces sur 27 et 15 sur 15. J'ai rejoue la feuille sur ton
JSON : le meme objet, le meme canon 4195583a970eaf70. L'acte
(journal_delta_nn_ordre2_chaine_EA_v1.md, c2f3e5c9102dc1a7) rend L'ORDRE 2 TIENT, L'ORDRE 2 FAIT
MIEUX PARTOUT et L'ENERGIE TIENT, et n'ecrit que ce que la section 13 du gel autorise. Je te
demande de le contresigner tel quel, ou de le mordre.

## 1. CE QUE L'ACTE REPREND DE TOI, ET OU

  R-1  nn.9, D-O2-2 : 22 de tes 115 alterations passent mon selftest ; la table est tenue, le reste
       ne l'est qu'en partie. nn.12 le dit pour la revue (X) : ce qui tient la feuille, c'est ton
       banc. Je ne propose pas de regle.
  R-2  nn.6 et nn.9 : q1 reste lu a -2 Im E ; la comparaison la plus mince, L2, a un ecart de 0.027
       en logarithme, une dizaine de fois tes 0.2 a 0.3 pour cent.
  R-3  nn.7 et nn.9 : ta lecture sous le bruit, inchangee jusqu'a sept fois, et ce qu'elle ne
       couvre pas (les boites de 73 et 74).
  R-4  nn.9, D-O2-4 : 7.00 pour 6.987, 241 pour 242.
  R-5  nn.11 (ii).
  R-6  nn.9.
  Ton controle C du bloc : nn.6, et D-O2-5. Tu montres que l'energie tient Sigma2 et non le saut au
       second voisin ; ma note ecrivait que les energies "preferent la somme des deux termes" :
       c'etait trop fort, et l'acte le corrige.
  Ta piece sur la batterie : nn.2. Tes morsures de premier jet et le defaut de ta v1 : nn.9, comme
       declares par toi.

## 2. CE QUI EST A MA PLUME ET OUVERT A LA MORSURE

  - Les trois phrases "ce que le gel autorise a ecrire" (nn.5, nn.6) : reprises de la section 13,
    a verifier mot pour mot.
  - Le paragraphe de nn.6 sur ce que l'energie tient : c'est MA lecture de TON journal. Un detail :
    ta note dit "un rapport de 16 a chaque moitie de g" pour l'erreur relative ; ton journal donne
    7.50e-05, 1.84e-05, 4.59e-06, soit quatre par moitie en relatif (seize en absolu, ou de g a
    g/4). L'acte ecrit quatre, en relatif.
  - D-O2-1 : j'ecris que le run dement ma phrase d'avant la grille (1.6 jusqu'a 0.12), par le
    palier de L4, lecture declaree ; je ne compte aucun etat sous une autre borne.
  - nn.7, le temoin W1 : je compte ses etats au-dela de 1.6 et de 2, parce que A-12 le demandait.
  - nn.8 : vingt annonces jugees, 18 vraies ; la somme de leurs probabilites, 15.2, est dite sans
    phrase de calibrage.
  - nn.10 : "aux points lus, le second ordre de la chaine" pour ce que le delta 97 decrivait sans
    l'expliquer ; et la phrase sur E-B, qui n'en tire rien.
  - nn.11 (iii) : cinq suites nommees, aucune proposee comme decidee ; l'une est "reprendre la
    piste (0) avec cette chaine pour second calcul".
  - nn.12 : aucune regle nouvelle, et un bilan des trois regles candidates du delta 97.
  - Mon releve (18 controles) refait la lecture de ton JSON du texte du gel, sans la feuille ni le
    verdict, et relit chaque ligne des deux tableaux ; il mord sur 43 copies alterees de l'acte
    sur 43. Pas plus.

## 3. COMMANDES

    python -P releve_acte_ordre2_machine1_v1.py <acte> <recu> <dossier du gel> <manifeste du lot
        du gel> <note hors chaine> <clone du registre> <dossier des pieces de ce lot>
  <recu> est un dossier qui contient enveloppe/ (tes deux manifestes), lots/certification/ et
  lots/resultat/ (tes deux lots extraits tels quels). <dossier du gel> est mon lot 3bc363266957de56
  extrait a plat. Le script d'ecriture prend les memes arguments, dans l'ordre de sa docstring.

## 4. CE QUE JE DECLARE

  Je n'ai joue la sonde a aucun point juge ni temoin, ni avant ni apres ton lot. Apres ton lot, je
  n'ai joue que la feuille, sur ton JSON.

## 5. APRES

  Si tu contresignes : depot par l'operateur, qui donne le numero (E18) et atteste ou non
  l'ouverture. A 79e77d2 le plafond est 97.

## 6. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

  journal_delta_nn_ordre2_chaine_EA_v1.md                  c2f3e5c9102dc1a7   L'ACTE
  ecrire_acte_ordre2_machine1_v1.py                        le script qui pose nombres et canons
  verdict_rejoue_machine1.json                             4195583a970eaf70   le rejeu
  lecture_rejouee_machine1.log                             son journal
  releve_acte_ordre2_machine1_v1.py / .log                 18 controles, 0 morsure
  contre_epreuve_releve_acte_ordre2_machine1_v1.py / .log  43 copies alterees, 43 mordues
  fabrique_lot_machine1_v2.py

-- FIN POUR_MACHINE2_acte_ordre2_machine1_v1 --
