"""Module controller du menu tournoi"""
from utils.menus import Menu
from controllers import menu_home_controller
from views.menu_tournament_view import TournamentMenuView
from .tournaments_controller import NewTournamentController


class TournamentMenuController:
    """Menu controller"""

    def __init__(self):
        self.menu = Menu()
        self.view = TournamentMenuView(self.menu)

    def __call__(self):
        print("entrez dans menu tournament controller")
        # 1. Construire le menu (utils/menus.py)
        self.menu.add("auto", "Créer un nouveau tournoi",
                      NewTournamentController().new_tournament)
        self.menu.add("auto", "Ajouter des joueurs",
                      NewTournamentController().add_players_tournament)
        self.menu.add("auto", "Lancer un tournoi",
                      NewTournamentController().start_gamme_controller)
        self.menu.add("auto", "Terminer un tour",
                      NewTournamentController().end_round_controller)
        self.menu.add("auto", "Lancer un tour",
                      NewTournamentController().start_round_controller)
        self.menu.add("auto", "Commentaire sur le tournoi",
                      NewTournamentController().comment_controller)
        self.menu.add("auto", "Menu accueil", self.menu_back())

        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        print("demande du choix utilisateur")
        user_choice_tournament = self.view.get_user_choice_tournament()
        print("recuperation du choix")
        print(user_choice_tournament)

        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice_tournament.handler

    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        handler = menu_home_controller.HomeMenuController
        return handler
