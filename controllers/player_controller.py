"""Module controller du menu joueur"""
from views.player_view import AddPlayerView
from models.entities.player_entity import Player
from models.manager.player_manager import PlayerManager
from controllers import menu_home_controller



class PlayerController:
    """Menu controller pour l'ajout d'un joueur à la BD Json"""
    def __init__(self):
        self.player = Player
        self.player_manager = PlayerManager
        self.view = AddPlayerView()
        self.handler = ""


    def new_player(self):
        """Ajout d'un joueur"""

        # Menu de création d'un joueur
        user_create = self.view.new_player()
        # validation de la création du joueur
        if not user_create == -1:
            user = self.player(**user_create)
            self.player_manager.save_player(self, user)
        # Demande si on veut créerun nouveau joueur
        choice_new = self.view.choice_player_new()
        # Si oui relance du new player
        if choice_new == 1:
            PlayerController.new_player(self)
        # Sinon retour au menu principal
        elif choice_new == -1:
            self.menu_back()


    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController
        return self.handler
