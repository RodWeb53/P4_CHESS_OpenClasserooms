"""Module controller du menu rapport"""
from utils.menus import Menu
from controllers import menu_home_controller
from views.menu_report_view import ReportMenuView
from .report_controller import ReportController


class ReportMenuController:
    """Menu controller pour les rapports"""

    def __init__(self):
        self.menu = Menu()
        self.view = ReportMenuView(self.menu)

    def __call__(self):
        self.menu.add("auto", "Liste des joueurs global",
                      ReportController().list_of_global_players)
        self.menu.add("auto", "Liste des tournois",
                      ReportController().list_of_tounaments)
        self.menu.add("auto", "Nom et dates d'un tournoi",
                      ReportController().tournament_information)
        self.menu.add("auto", "Liste des joueurs d'un tournoi",
                      ReportController().list_of_tournament_players)
        self.menu.add("auto", "Liste des tours et matchs d'un tournoi",
                      ReportController().tournament_match_list)
        self.menu.add("auto", "Classement d'un tournoi",
                      ReportController().ranking_of_a_tournament)
        self.menu.add("auto", "Commentaire d'un tournoi",
                      ReportController().tournament_commentary)
        self.menu.add("auto", "Menu accueil", self.menu_back())
        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice_tournament = self.view.get_user_choice_tournament()
        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice_tournament.handler

    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        handler = menu_home_controller.HomeMenuController
        return handler
