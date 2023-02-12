"""Module controller du menu d'accueil"""
from utils.menus import Menu
from views.menu_player_view import PlayerMenuView
from .player_controller import PlayerController
from controllers import menu_home_controller



class PlayerMenuController:
    """Home menu controller"""
    def __init__(self):
        self.menu = Menu()
        self.view = PlayerMenuView(self.menu)

    def __call__(self):
        # 1. Construire le menu (utils/menus.py)
        self.menu.add("auto", "Ajouter un joueur", PlayerController())
        # self.menu.add("auto", "Menu principal", PlayerMenuController())
        # Ajouter les autres lignes d'option du menus
        self.menu.add("auto", "Menu principal", menu_home_controller.HomeMenuController())

        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()

        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
