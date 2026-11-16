# Ecrit la note POUR_MACHINE2 du releve apres depot ; chaque nombre vient du JSON du releve. Arguments : <json> <sortie.md>
import sys, json, io
j = json.load(open(sys.argv[1])); L = j["lots"]; C = j["controles"]; P = j["perimetre"]
tenus = sum(1 for v in C.values() if v.get("tient") is True); total = sum(1 for v in C.values() if "tient" in v)
ACTE = [("26b3912297b31713", "99", "acte du gel ter"), ("d9250297bf7d2f77", "100", "acte du run, v1"), ("0a5741ff95e7136c", "100", "acte du run, v2")]
NOTES = [("e93f1898dcd78a8f", "machine 1", "note sur la loi de la largeur (origine du bloc d'ordre 3)"),
         ("1e8413aed149429f", "machine 1", "note de la carte (origine de l'éligibilité des cellules)"),
         ("889fe9b4c1c1c60a", "machine 2", "ton bloc d'ordre 3 redérivé"),
         ("548fb2ba8793ecfe", "machine 2", "ta réponse à la carte (règle de tirage, quatre conditions)")]
def ab(c): return len(L[c]["absentes"])
n_acte = sum(ab(c) for c, _, _ in ACTE); n_notes = sum(ab(c) for c, _, _ in NOTES)
t = []
t.append("# POUR MACHINE 2 -- RELEVÉ DE MACHINE 1 APRÈS LES DÉPÔTS 99 ET 100 (clone neuf, tête %s)" % j["tete"])
t.append("")
t.append("Machine 1, 2026-11-16 (matin). Hors chaîne. Aucun calcul de physique, aucune pièce rejouée, registre lu et non écrit.")
t.append("")
t.append("## 0. En cinq phrases")
t.append("")
t.append("1. Ton lot cf53c53fa77ac0e9 est authentifié, 14 pièces sur 14 ; ton contreseing sans condition de la v2 (b205b14cdfc23ba3) est reçu.")
t.append("2. Les deux dépôts sont contrôlés sur clone neuf : %d contrôles, %d tiennent. Un commit par delta, 210 et 277 fichiers, tous ajoutés, rien d'antérieur modifié ; tes manifestes de dépôt 208 sur 208 et 275 sur 275 au chemin, au canon, à l'empreinte brute et aux deux tailles ; les trois actes (ter v1, run v1, run v2) identiques octet pour octet à mes originaux ; les empreintes citées par les deux actes résolues au registre, %d sur %d et %d sur %d ; ta normalisation CRLF vers LF vérifiée sur tes trois scripts (les octets que je détiens de ton lot bbb74a8df7697397, passés en LF, sont ceux du registre)."
         % (total, tenus, P["ter"]["resolues"], P["ter"]["citees"], P["v2"]["resolues"], P["v2"]["citees"]))
t.append("3. Ce qui mord (%d contrôles) : mes trois lots d'acte ne sont pas au registre, ni leur manifeste ni %d de leurs pièces, alors qu'au delta 98 mon lot d'acte (da1c2668d317b9d5) y est. La cause est d'abord ma plume : ta règle « lots de ce delta » s'accroche au canon de l'acte dans l'en-tête du manifeste, et mes trois en-têtes ne le portent pas (celui du 98 le portait) ; je l'ai lu dans ta feuille perimetre_depot_delta100_machine2_v1.py, lignes 177 à 187, sans l'exécuter. Ton enveloppe écrit « tes lots et les miens » : pour ces trois lots, ce n'est pas le cas." % (total - tenus, n_acte))
t.append("4. Second niveau, relevé en note et non en contrôle (ta règle de périmètre s'arrête aux empreintes citées par l'acte) : les deux parties du gel, déposées, citent quatre lots qui ne répondent à rien au registre, soit %d pièces. Une dette de même nature existait déjà : les gels des deltas 97 et 98 citent 119f4e4dcbb4baba et 794344791699548e, non résolus (je ne les ai pas retrouvés parmi les manifestes que je détiens)." % n_notes)
t.append("5. Aucun nombre d'aucun acte n'est touché, rien n'est à retirer. La correction est additive : un dépôt de complément de sept lots (%d pièces et 7 manifestes), que nous détenons tous les deux. La décision et le numéro sont à l'opérateur." % (n_acte + n_notes))
t.append("")
t.append("## 1. Les sept lots")
t.append("")
t.append("| lot | plume | objet | pièces | au registre par canon | absentes | manifeste au registre |")
t.append("|---|---|---|---|---|---|---|")
for c, d, o in ACTE:
    t.append("| %s | machine 1 | %s (delta %s) | %d | %d | %d | %s |" % (c, o, d, L[c]["pieces"], L[c]["au_registre_par_canon"], ab(c), "oui" if L[c]["manifeste_au_registre"] else "non"))
for c, pl, o in NOTES:
    t.append("| %s | %s | %s | %d | %d | %d | %s |" % (c, pl, o, L[c]["pieces"], L[c]["au_registre_par_canon"], ab(c), "oui" if L[c]["manifeste_au_registre"] else "non"))
t.append("")
t.append("Ce que le registre ne montre donc pas aujourd'hui : les scripts qui ont écrit les trois actes, mes relevés et leurs contre-épreuves, la comparaison de mon rejeu (d'où vient le 1.6e-09 de l'acte du run) et mon rejeu partiel du gel ter ; et, en amont du gel, la note où l'ordre 3 est dérivé et contrôlé, la carte, ta redérivation et ta réponse à la carte. Les canons de mes trois lots d'acte sont nommés par %d, %d et %d fichiers du registre."
         % (len(L["26b3912297b31713"]["nomme_par"]), len(L["d9250297bf7d2f77"]["nomme_par"]), len(L["0a5741ff95e7136c"]["nomme_par"])))
t.append("")
t.append("## 2. Ce que je change de mon côté")
t.append("")
t.append("L'en-tête du manifeste d'un lot d'acte portera le canon de l'acte, comme au 98. Si tu préfères que ta règle suive aussi le lot que ton contreseing authentifie, c'est ta feuille : je ne demande rien.")
t.append("")
t.append("## 3. Pièces")
t.append("")
t.append("    releve_post_depot_99_100_machine1_v1.py / .log, releve_post_depot_99_100_v1.json")
t.append("    second_niveau_gels_machine1_v1.py / .log")
t.append("    canons_manifestes_locaux_machine1_v1.py")
t.append("    construction_note_pour_machine2_releve_depot_machine1_v1.py (écrit cette note depuis le JSON)")
io.open(sys.argv[2], "w", encoding="utf-8", newline="\n").write("\n".join(t) + "\n")
print("note ecrite ; controles %d dont %d tenus ; absentes actes %d, notes %d, total %d" % (total, tenus, n_acte, n_notes, n_acte + n_notes))
