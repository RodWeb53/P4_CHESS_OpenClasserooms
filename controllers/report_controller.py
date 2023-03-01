"""Module controller pour la création des rapports"""
from views.report_view import ReportView
from models.entities.tournament_entity import Tournament
from models.entities.player_entity import Player
from models.manager.tournament_manager import TournamentManager
from models.manager.player_manager import PlayerManager
from controllers import menu_report_controller


class ReportController:
    """Tournoi controller"""

    def __init__(self):
        self.tournament = Tournament
        self.player = Player
        self.view = ReportView
        self.tournament_manager = TournamentManager
        self.player_manager = PlayerManager


    def list_of_global_players(self):
        """Liste global des joueurs de la base de données"""
        # Chargement des joueurs
        data_players = self.player_manager.get_all_players(self)
        # Choix du mode de tri
        choice = self.view.sort_order(self)
        # Affichage dans la vue
        self.view.list_global_players(self, choice, data_players)

        return self.menu_back()


    def list_of_tounaments(self):
        """Liste des tournois"""
        # Récupération de la liste des tournois
        data_tournaments = self.tournament_manager.get_all_tournament(self)
        self.view.tournaments_list(self, data_tournaments)

        return self.menu_back()


    def tournament_information(self):
        """Information sur un tournoi"""
        # Récupération du choix du tournoi
        choice_tournament = ReportController.choice_tournaments(self)
        # Affichage du tournoi dans la vue
        self.view.tournament_details(self, choice_tournament)

        return self.menu_back()


    def list_of_tournament_players(self):
        """Liste des joueurs pour un tournoi"""
        # Récupération du choix du tournoi
        choice_tournament = ReportController.choice_tournaments(self)
        # Choix du mode de tri
        choice = self.view.sort_order(self)
        self.view.player_list_tournament(self, choice, choice_tournament)

        return self.menu_back()


    def tournament_match_list(self):
        """Liste des tours et matchs d'un tournoi"""
        # Récupération du choix du tournoi
        tournament = ReportController.choice_tournaments(self)
        self.view.tournament_match(self, tournament)

        return self.menu_back()


    def ranking_of_a_tournament(self):
        """Classement d'un tournoi"""
        # Récupération du choix du tournoi
        choice_tournament = ReportController.choice_tournaments(self)
        # Choix du mode de tri
        choice = 2
        self.view.player_list_tournament(self, choice, choice_tournament)

        return self.menu_back()


    def tournament_commentary(self):
        """Commentaire d'un tournoi"""
        # Récupération du choix du tournoi
        comments = ReportController.choice_tournaments(self)
        self.view.commentary_tournament(self, comments)

        return self.menu_back()


    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        handler = menu_report_controller.ReportMenuController()
        return handler


    def choice_tournaments(self):
        """Méthodes pour choisir le tournoi en cours et retourner les données"""
        # Récupération de la liste des tournois
        data_tournaments = self.tournament_manager.get_all_tournament(self)
        # Récupération du choix utilisateur pour le N° de tournoi
        choice_tournament = self.view.choice_tournament(self, data_tournaments)
        # recupération des données du tournoi suite au choix via l'ID
        active_tournament = self.tournament_manager.get_tournament(
            self, choice_tournament)

        return active_tournament
