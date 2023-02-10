"""Module controller du menu tournoi"""
from utils.menus import Menu
from views.tournament_menu_view import TournamentMenuView
from .new_tournament_controller import NewTournamentController
from .add_player_tournament_controller import AddPlayersTournamentController
from .start_gamme_controller import StartGameController
from .end_round_controller import EndRoundController
from .start_round_controller import StartRoundController
from .comment_tournament_controller import CommentTournamentController
from controllers import menu_home_controller


class TournamentMenuController:
    """Menu controller"""
    def __init__(self):
        self.menu = Menu()
        self.view = TournamentMenuView(self.menu)

    def __call__(self):
        # 1. Construire le menu (utils/menus.py)
        self.menu.add("auto", "Créer un nouveau tournoi", NewTournamentController())
        self.menu.add("auto", "Ajouter des joueurs", AddPlayersTournamentController())
        self.menu.add("auto", "Lancer un tournoi", StartGameController())
        self.menu.add("auto", "Terminer un tour", EndRoundController())
        self.menu.add("auto", "Lancer un tour", StartRoundController())
        self.menu.add("auto", "Commentaire sur le tournoi", CommentTournamentController())
        self.menu.add("auto", "Menu accueil", self.menu_back())

        # 2 Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()

        # 3. Retourner le controleur associé au choix de l'utilisateur au controleur principal
        return user_choice.handler
    

    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_home_controller.HomeMenuController
        return self.handler
