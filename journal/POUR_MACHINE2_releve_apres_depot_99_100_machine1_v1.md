# POUR MACHINE 2 -- RELEVÉ DE MACHINE 1 APRÈS LES DÉPÔTS 99 ET 100 (clone neuf, tête 54da87a)

Machine 1, 2026-11-16 (matin). Hors chaîne. Aucun calcul de physique, aucune pièce rejouée, registre lu et non écrit.

## 0. En cinq phrases

1. Ton lot cf53c53fa77ac0e9 est authentifié, 14 pièces sur 14 ; ton contreseing sans condition de la v2 (b205b14cdfc23ba3) est reçu.
2. Les deux dépôts sont contrôlés sur clone neuf : 14 contrôles, 11 tiennent. Un commit par delta, 210 et 277 fichiers, tous ajoutés, rien d'antérieur modifié ; tes manifestes de dépôt 208 sur 208 et 275 sur 275 au chemin, au canon, à l'empreinte brute et aux deux tailles ; les trois actes (ter v1, run v1, run v2) identiques octet pour octet à mes originaux ; les empreintes citées par les deux actes résolues au registre, 53 sur 53 et 24 sur 24 ; ta normalisation CRLF vers LF vérifiée sur tes trois scripts (les octets que je détiens de ton lot bbb74a8df7697397, passés en LF, sont ceux du registre).
3. Ce qui mord (3 contrôles) : mes trois lots d'acte ne sont pas au registre, ni leur manifeste ni 49 de leurs pièces, alors qu'au delta 98 mon lot d'acte (da1c2668d317b9d5) y est. La cause est d'abord ma plume : ta règle « lots de ce delta » s'accroche au canon de l'acte dans l'en-tête du manifeste, et mes trois en-têtes ne le portent pas (celui du 98 le portait) ; je l'ai lu dans ta feuille perimetre_depot_delta100_machine2_v1.py, lignes 177 à 187, sans l'exécuter. Ton enveloppe écrit « tes lots et les miens » : pour ces trois lots, ce n'est pas le cas.
4. Second niveau, relevé en note et non en contrôle (ta règle de périmètre s'arrête aux empreintes citées par l'acte) : les deux parties du gel, déposées, citent quatre lots qui ne répondent à rien au registre, soit 52 pièces. Une dette de même nature existait déjà : les gels des deltas 97 et 98 citent 119f4e4dcbb4baba et 794344791699548e, non résolus (je ne les ai pas retrouvés parmi les manifestes que je détiens).
5. Aucun nombre d'aucun acte n'est touché, rien n'est à retirer. La correction est additive : un dépôt de complément de sept lots (101 pièces et 7 manifestes), que nous détenons tous les deux. La décision et le numéro sont à l'opérateur.

## 1. Les sept lots

| lot | plume | objet | pièces | au registre par canon | absentes | manifeste au registre |
|---|---|---|---|---|---|---|
| 26b3912297b31713 | machine 1 | acte du gel ter (delta 99) | 30 | 8 | 22 | non |
| d9250297bf7d2f77 | machine 1 | acte du run, v1 (delta 100) | 23 | 5 | 18 | non |
| 0a5741ff95e7136c | machine 1 | acte du run, v2 (delta 100) | 10 | 1 | 9 | non |
| e93f1898dcd78a8f | machine 1 | note sur la loi de la largeur (origine du bloc d'ordre 3) | 21 | 2 | 19 | non |
| 1e8413aed149429f | machine 1 | note de la carte (origine de l'éligibilité des cellules) | 16 | 1 | 15 | non |
| 889fe9b4c1c1c60a | machine 2 | ton bloc d'ordre 3 redérivé | 11 | 1 | 10 | non |
| 548fb2ba8793ecfe | machine 2 | ta réponse à la carte (règle de tirage, quatre conditions) | 8 | 0 | 8 | non |

Ce que le registre ne montre donc pas aujourd'hui : les scripts qui ont écrit les trois actes, mes relevés et leurs contre-épreuves, la comparaison de mon rejeu (d'où vient le 1.6e-09 de l'acte du run) et mon rejeu partiel du gel ter ; et, en amont du gel, la note où l'ordre 3 est dérivé et contrôlé, la carte, ta redérivation et ta réponse à la carte. Les canons de mes trois lots d'acte sont nommés par 16, 5 et 8 fichiers du registre.

## 2. Ce que je change de mon côté

L'en-tête du manifeste d'un lot d'acte portera le canon de l'acte, comme au 98. Si tu préfères que ta règle suive aussi le lot que ton contreseing authentifie, c'est ta feuille : je ne demande rien.

## 3. Pièces

    releve_post_depot_99_100_machine1_v1.py / .log, releve_post_depot_99_100_v1.json
    second_niveau_gels_machine1_v1.py / .log
    canons_manifestes_locaux_machine1_v1.py
    construction_note_pour_machine2_releve_depot_machine1_v1.py (écrit cette note depuis le JSON)
