"""Module controller pour la création d'un tournoi"""
from views.tournament_view import NewTournamentView
from models.entities.tournament_entity import Tournament
from models.entities.player_entity import Player
from models.manager.tournament_manager import TournamentManager
from models.manager.player_manager import PlayerManager
from controllers import menu_tournament_controller

class NewTournamentController:
    """Tournoi controller"""

    def __init__(self):
        self.tournament = Tournament
        self.player = Player
        self.tournament_manager = TournamentManager
        self.player_manager = PlayerManager
        self.view = NewTournamentView()


    # def __call__(self):
    #     #Création du tournoi avec la vue
    #     tournament_create = self.view.new_tournament()

    #     #Récupération des informations et création des données du tournoi
    #     tournament = self.tournament(**tournament_create)
    #     #Sauvegarde des données dans la base par le model manager
    #     self.tournament_manager.save_tournament(self, tournament)



    #     return 


    def new_tournament(self):
        self.tournament = Tournament
        self.tournament_manager = TournamentManager
        self.player_manager = PlayerManager
        self.view = NewTournamentView()
        print("Entrer dans new tournoi")
        #Création du tournoi avec la vue
        tournament_create = self.view.new_tournament()

        #Récupération des informations et création des données du tournoi
        tournament = self.tournament(**tournament_create)

        #Sauvegarde des données dans la base par le model manager
        self.tournament_manager.save_tournament(self, tournament)

        # **** faire les enchainements des modules ****
        # **** Faire la sortie du module

        return
    
    def choice_tournaments(self):
        """Méthodes pour choisir le tournoi en cours et retourner les données"""
        self.tournament = Tournament
        self.tournament_manager = TournamentManager
        self.tournament = Tournament
        self.view = NewTournamentView()
        #Récupération de la liste des tournois
        data_tournaments = self.tournament_manager.get_all_tournament()
        lists_tournament = []
        for items in data_tournaments:
            lists_tournament.append(self.tournament(**items))
        
        # Récupération du choix utilisateur pour le N° de tournoi
        choice_tournament = self.view.choice_tournament(lists_tournament)

        # recupération des données du tournoi suite au choix via l'ID
        active_tournament = self.tournament_manager.get_tournament(self, choice_tournament)

        return active_tournament
    
    def add_players_tournament(self):
        self.tournament = Tournament
        self.tournament_manager = TournamentManager
        self.tournament = Tournament
        self.view = NewTournamentView()

        active_tournament = NewTournamentController.choice_tournaments(self)

        #récpération id des joueurs déja saisie dans le tournoi courant
        list_base = []
        for number in active_tournament["list_of_players"]:
            list_base.append(number["id"])

        #chargement de tous les joueurs
        data_players = self.player_manager.get_all_players()
        lists_players_all = []
        # Boucle pour enlever les joueurs déja enregistrés
        for item in data_players:
            if item["id"] in list_base:
                pass
            else:
                lists_players_all.append(self.player(**item))

        list_start = []
        #  ******Faire un test si la liste des joueurs est vide pour ne pas envoyer la liste ? *****
        list_players_choice = self.view.add_player_tournament(lists_players_all, list_start)
        # Récupération de la liste des joueurs sélectionnés
        list_add= []
        for item_player in list_players_choice:
            list_add.append({
                            "id": item_player.id,
                            "last_name": item_player.last_name,
                            "first_name": item_player.first_name,
                            "points":0,
                            })
        # Ajouts des joueurs dans le tournoi en cours
        active_tournament["list_of_players"] = active_tournament["list_of_players"] + list_add 

        tournament = self.tournament(**active_tournament)

        #Sauvegarde des données dans la base par le model manager
        self.tournament_manager.update_tournament(self, tournament)

        # Dans la vue ajout des joueurs dans (list_of_players)
        #   - Vérification qu'il y a bien un nombre paire de joueur pour le tournoi
        # Récupération des nouvelles données dans le controllers
        # Transformation des données en objet
        # Sauvegarde des données dans dans le modèle manager
        # Est ce que l'on fait l'écrasement des données dans le manager 
        # Après enregistrement envoi vers le controller (start_gamme_controller)
        

        

    def start_gamme_controller(self):
        """Reste à faire"""
        self.tournament = Tournament
        self.tournament_manager = TournamentManager
        self.tournament = Tournament
        self.view = NewTournamentView()

        # Demande si validation du tournoi
        question = "Confirmez-vous le lancement du tournoi ?"
        validation = self.view.validation_request(question)
        print("retour active ")

        if validation:
            # Récupération du choix du tournoi et des données
            active_tournament = NewTournamentController.choice_tournaments(self)
            print("retour active ")
            print(active_tournament)

            if active_tournament["current_round"] == "":
                print("Le lancement du tournoi")

                number_player = 0
                list_player_gamme = []

                for item in active_tournament["list_of_players"]:
                    list_player_gamme.append(item)
                    number_player +=1

                if int(number_player % 2) == 0:
                    # Si le nombre de joueurs est pair
                    first_round = self.view.start_gamme_tournament(list_player_gamme)
                    active_tournament["list_of_matchs"] = first_round
                    active_tournament["current_round"] = 1
                    tournament = self.tournament(**active_tournament)

                    #Sauvegarde des données dans la base par le model manager
                    self.tournament_manager.update_tournament(self, tournament)

                else:
                    question = "Souhaitez-vous ajouter un joueur"
                    self.view.missing_a_player()
                    validation = self.view.validation_request(question)
                    print("retour dans le controller")
                    if validation == False:
                        self.menu_back()
                        
                    else:
                        print("validation True")
                        NewTournamentController.add_players_tournament(self)
            else:
                self.view.tournament_current()
    
        return self.menu_back()       

        


    def start_round_controller(self):
        """Reste à faire"""
        # Génération des matchs suivant les problématiques suivantes:
        #   - 2 joueurs ne peuvent pas se rencontrer 2 fois
        #   - Faire des rencontre gagnant contre gagnant
        #       - Si pas possible gagnant contre Nul si pas de nul alors contre perdu
        #   - Lancement du round et enregistrement des données dans (current_round)
        # Envoie vers le controller (end_round_controller)
        pass


    def end_round_controller(self):
        """Reste à faire"""

        # Faire la validation des matchs
        #   - Si reprise des résultats alors récupération des données dans (current_round)
        #   - Demander sur un match le premier joueur est "gagnant" "perdant" "match nul"
        #   - En fonction de la réponse affection du nombre de point au 1° joueur et au 2 joueur pour ce match seulement
        #   - Donner la possibilité de ne pas donner de résultat et revenir dessus non
        #   - Marquer que le tour est terminé
        #   - Vérification que tous les matchs on un résultat
        #   - Enregistrement du round dans (list_of_rounds)
        #   - Ajouter les points du tour sur la liste des joueurs
        # Envoie vers (start_round_controller) si les rounds ne sont pas fini
        #   -  Si fini alors mettre un message que le tournoi est fini et un lien vers les rapports
        pass

    def comment_controller(self):
        """Reste à faire"""
        # permettre de mettre un commentaire sur le tournoi
        # enregistrement des données dans (comments)
        # Est ce que l'on donne la possibilité de faire plusieurs commentaires ?
        pass

    def end_screen_controller(self):
        pass


    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        self.handler = menu_tournament_controller.TournamentMenuController()
        return self.handler