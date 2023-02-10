"""Module controller pour la création d'un tournoi"""
from views.new_tournament_view import NewTournamentView
from models.entities.tournament_entity import Tournament
from models.manager.tournament_manager import TournamentManager


class NewTournamentController:
    """Tournoi controller"""

    def __init__(self):
        self.tournament = Tournament
        self.tournament_manager = TournamentManager
        self.view = NewTournamentView()


    def __call__(self):
        #Création du tournoi avec la vue
        tournament_create = self.view.new_tournament()

        #Récupération des informations et création des données du tournoi
        tournament = self.tournament(**tournament_create)
        #Sauvegarde des données dans la base par le model manager
        self.tournament_manager.save_tournament(self, tournament)



        return 
        