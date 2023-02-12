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


    def __call__(self):

        # Menu de création d'un joueur
        user_create = self.view.new_player()
        #Si l'utilisateur ne veut pas créer le joueur
        if user_create == -1:
            choice_new = self.view.choice_player_new()
            # demande s'il veut créer un nouveau joueur
            if choice_new == -1:
                # Si non alors menu d'accueil
                self.menu_back()
               
        else:
            #Si l'utilisateur crée le joueur
            user = self.player(**user_create)
            # Création de l'objet utilisateur
            self.player_manager.save_player(self, user)
            # Sauvegarde du joueur dans la BD Json
            choice_next = self.view.choice_player_next()
            # Demande si l'utilisateur veut créer un nouveau joueur

            if choice_next == -1:
                # Si non alors menu d'accueil
                self.menu_back()

        return self.handler
    
    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController
        return self.handler
