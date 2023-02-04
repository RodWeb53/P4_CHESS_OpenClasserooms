"""Module controller du menu d'accueil"""
from utils.menus import Menu
from views.home_menu_view import HomeMenuView
from views.player_menu_view import PlayerMenuView
from .menu_player_controller import PlayerMenuController
from .add_player_controller import PlayerController
from .menu_tournament_controller import TournamentMenuController
from .end_screen_controller import EndScreenController


class HomeMenuController:
    """Home Menu controller"""
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        # 1. Construire le menu (utils/menus.py)
        self.menu.add("auto", "Menu joueur", PlayerMenuController())
        self.menu.add("auto", "Menu tournoi", TournamentMenuController())
        self.menu.add("q", "Quitter l'application", EndScreenController())

        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()

        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
