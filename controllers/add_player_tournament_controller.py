"""Module controller pour la création d'un tournoi"""
from views.new_tournament_view import NewTournamentView
from models.entities.tournament_entity import Tournament
from models.manager.tournament_manager import TournamentManager
from models.manager.player_manager import PlayerManager


class AddPlayersTournamentController:
    """Ajout de players au tournoi controller"""

    def __init__(self):
        self.tournament = Tournament
        self.tournament_manager = TournamentManager
        self.player_manager = PlayerManager
        self.view = NewTournamentView()


    def __call__(self):
        #Récupération de la liste des tournois
        data_tournaments = self.tournament_manager.get_all_tournament()
        lists_tournament = []
        for items in data_tournaments:
            lists_tournament.append(self.tournament(**items))
        
        choice = self.view.choice_tournament(lists_tournament)

        # recupération des données du tournois suite au choix via l'ID
        active_tournament = self.tournament_manager.get_tournament(self, choice)
        print("dans le print du controller add player")

        """reste à faire"""
        # envoie des données du tournois (active_tournament) + les players à la vue
        # Dans la vue ajout des joueurs dans (list_of_players)
        #   - Vérification qu'il y a bien un nombre paire de joueur pour le tournoi
        # Récupération des nouvelles données dans le controllers
        # Transformation des données en objet
        # Sauvegarde des données dans dans le modèle manager
        # Est ce que l'on fait l'écrasement des données dans le manager ou dans le controller ?
        # Après enregistrement envoi vers le controller (start_gamme_controller)
        


        # data_players = self.player_manager.get_all_players()
        # print(data_players)

        # self.view.add_player_tournament(data_tournaments, data_players)

