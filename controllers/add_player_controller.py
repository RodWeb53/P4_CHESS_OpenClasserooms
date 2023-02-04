"""Module controller du menu joueur"""
from views.add_player_view import AddPlayerView
from models.entities.player_entity import Player
from models.manager.player_manager import PlayerManager


class PlayerController:
    """Menu controller pour l'ajout d'un joueur à la BD Json"""
    def __init__(self):
        self.player = Player
        self.player_manager = PlayerManager
        self.view = AddPlayerView()

    def __call__(self):

        # Menu de création d'un joueur
        user_create = self.view.new_player()
        if user_create == -1:
            print("blocage")
            #reste a faire le choix non a la sauvegarde du joueur
            #   faire un menu pour retour à l'accueil

        user = self.player(**user_create)

        self.player_manager.save_player(self, user)

    # reste a faire le choix non a la sauvegarde du joueur
    #   faire un menu pour retour à l'accueil
    # Si le choix est oui apres l'enregistrement du joueur
    #   renvoie sur le module de création

        return
