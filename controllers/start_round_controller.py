"""Module controller du menu start round"""

class StartRoundController:
    """Menu controller"""

    def __call__(self):
        print("Dans le controleur de Start round")
        return



    """Reste à faire"""
    # Génération des matchs suivant les problématiques suivantes:
    #   - 2 joueurs ne peuvent pas se rencontrer 2 fois
    #   - Faire des rencontre gagnant contre gagnant
    #       - Si pas possible gagnant contre Nul si pas de nul alors contre perdu
    #   - Lancement du round et enregistrement des données dans (current_round)
    # Envoie vers le controller (end_round_controller)
    