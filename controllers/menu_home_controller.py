"""Module controller du menu d'accueil"""
from utils.menus import Menu
from views.menu_home_view import HomeMenuView
from .menu_player_controller import PlayerMenuController
from .menu_tournament_controller import TournamentMenuController
from .menu_report_controller import ReportMenuController


class HomeMenuController:
    """Home Menu controller"""
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)


    def __call__(self):
        # 1. Construire le menu (utils/menus.py)
        self.menu.add("auto", "Menu joueur", PlayerMenuController())
        self.menu.add("auto", "Menu tournoi", TournamentMenuController())
        self.menu.add("auto", "Menu rapport", ReportMenuController())
        self.menu.add("q", "Quitter l'application", self.end_screen_controller())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler

    def end_screen_controller(self):
        """Sortie du programme"""
        return
    