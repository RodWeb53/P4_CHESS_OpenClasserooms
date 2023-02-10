"""Module controller du menu end round"""

class EndRoundController:
    """Menu controller"""

    def __call__(self):
        print("Dans le controleur de end round")
        return
    

    """Reste à faire"""

    # Faire la validation des matchs
    #   - Si reprise des résultats alors récupération des données dans (current_round)
    #   - Demander sur un match le premier joueur est "gagnant" "perdant" "match nul"
    #   - En fonction de la réponse affection du nombre de point au 1° joueur et au 2 joueur pour ce match seulement
    #   - Donner la possibilité de ne pas donner de résultat et revenir dessus ?
    #   - Marquer que le tour est terminé
    #   - Vérification que tous les matchs on un résultat
    #   - Enregistrement du round dans (list_of_rounds)
    #   - Ajouter les points du tour sur la liste des joueurs
    # Envoie vers (start_round_controller) si les rounds ne sont pas fini
    #   -  Si fini alors mettre un message que le tournoi est fini et un lien vers les rapports

