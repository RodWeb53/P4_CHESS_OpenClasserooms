"""Module controller pour la création d'un tournoi"""
from datetime import datetime
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


    def new_tournament(self):
        """Création d'un nouveau tournoi"""
        # Création du tournoi avec la vue
        tournament_create = self.view.new_tournament()
        # Récupération des informations et création des données du tournoi
        tournament = self.tournament(**tournament_create)
        # Sauvegarde des données dans la base par le model manager
        self.tournament_manager.save_tournament(self, tournament)

        question = "Souhaitez vous ajouter des joueurs au Tournoi ?"
        validation = self.view.validation_request(question)
        if validation:
            return self.add_players_tournament()

        return self.menu_back()


    def choice_tournaments(self):
        """Méthodes pour choisir le tournoi en cours et retourner les données"""
        # Récupération de la liste des tournois
        data_tournaments = self.tournament_manager.get_all_tournament_in_progress(self)
        # Récupération du choix utilisateur pour le N° de tournoi
        choice_tournament = self.view.choice_tournament(data_tournaments)
        # recupération des données du tournoi suite au choix via l'ID
        active_tournament = self.tournament_manager.get_tournament(
            self, choice_tournament)

        return active_tournament


    def add_players_tournament(self):
        """Ajout de player dans le tournoi"""
        active_tournament = NewTournamentController.choice_tournaments(self)

        if active_tournament[0].current_round == "":
            # récupération id des joueurs déja saisie dans le tournoi courant
            list_base = []
            for number in active_tournament[0].list_of_players:
                list_base.append(number["player_id"])
            # chargement de tous les joueurs
            data_players = self.player_manager.get_all_players(self)
            lists_players_all = []
            # Boucle pour enlever les joueurs déja enregistrés
            for item in data_players:
                if item.player_id in list_base:
                    pass
                else:
                    lists_players_all.append(item)
            list_start = []
            list_players_choice = self.view.add_player_tournament(
                lists_players_all, list_start)

            # Récupération de la liste des joueurs sélectionnés
            list_add = []
            for item_player in list_players_choice:
                list_add.append({
                                "player_id": item_player.player_id,
                                "last_name": item_player.last_name,
                                "first_name": item_player.first_name,
                                "points": 0,
                                "players_played": []
                                })
            # Ajouts des joueurs dans le tournoi en cours
            active_tournament[0].list_of_players = active_tournament[0].list_of_players + list_add
            # Sauvegarde des données dans la base par le model manager
            self.tournament_manager.update_tournament(self, active_tournament)
            question = "Souhaitez-vous lancer le tournoi ?"
            validation = self.view.validation_request(question)
            if validation:
                return self.start_gamme_controller()

        else:
            information = "Impossible d'ajouter des joueurs, le tournoi est commencé"
            self.view.information(information)

        return self.menu_back()


    def start_gamme_controller(self):
        """Lancement du tournoi et du premier round"""
        # Récupération du choix du tournoi et des données
        active_tournament = NewTournamentController.choice_tournaments(self)
        #Vérification que le tournoi n'est pas commencé
        if active_tournament[0].current_round == "":
            number_player = 0
            list_player_gamme = []

            for item in active_tournament[0].list_of_players:
                list_player_gamme.append(item)
                number_player += 1

            if number_player > 0 and int(number_player % 2) == 0:
                # Si le nombre de joueurs est pair
                date_time = datetime.now()
                first_round = self.view.start_gamme_tournament(
                    list_player_gamme)
                active_tournament[0].list_of_matchs = first_round
                active_tournament[0].current_round = 1
                active_tournament[0].start_round = date_time.strftime(
                    "%d/%m/%Y, %H:%M:%S")
                #Demande si validation du tournoi
                question = "Confirmez-vous le lancement d'un tournoi ?"
                validation = self.view.validation_request(question)
                if validation:
                    # Sauvegarde des données dans la base json
                    self.tournament_manager.update_tournament(
                        self, active_tournament)
                else:
                    self.menu_back()

            else:
                # Si le nombre de joueur est impair demande pour ajouter un joueur
                question = "Le nombre de joueur est impair souhaitez-vous ajouter un joueur ?"
                self.view.missing_a_player()
                validation = self.view.validation_request(question)
                if not validation:
                    return self.menu_back()
                else:
                    return NewTournamentController.add_players_tournament(self)
        else:
            information = "Impossible le tournoi est déja commencé !"
            self.view.information(information)
            return self.menu_back()

        #Demande si on fini un tour
        question = "Souhaitez-vous terminer le tour et donner les résultats ?"
        validation = self.view.validation_request(question)
        if validation:
            self.end_round_controller()
        else:
            self.menu_back()

        return self.menu_back()


    def start_round_controller(self):
        """Création des round à partir du 2° round"""
        active_tournament = NewTournamentController.choice_tournaments(self)
        #Si le tournoi n'est pas lancé
        if active_tournament[0].current_round == "":
            information = "Impossible de créer un tour le tournoi n'est pas lancé ! "
            self.view.information(information)
            return self.menu_back()
        #Si le tour est en cours
        elif active_tournament[0].start_round:
            information = "Impossible le tour est en cours !"
            self.view.information(information)
            return self.menu_back()
        else:
            round_in_progress = self.view.start_round_tournament(active_tournament)
            date_time = datetime.now()
            active_tournament[0].list_of_matchs = round_in_progress
            active_tournament[0].start_round = date_time.strftime(
                        "%d/%m/%Y, %H:%M:%S")
            # Sauvegarde des données dans la base json
            self.tournament_manager.update_tournament(self, active_tournament)

        #Demande si on fini un tour
        question = "Souhaitez-vous terminer le tour et donner les résultats ?"
        validation = self.view.validation_request(question)
        if validation:
            return self.end_round_controller()
        else:
            return self.menu_back()


    def end_round_controller(self):
        """Terminer un tour et affecter les points aux joueurs"""
        active_tournament = NewTournamentController.choice_tournaments(self)
        if active_tournament[0].current_round == "":
            information = "Désolé le tournoi n'est pas encore lancé !"
            self.view.information(information)
            return self.menu_back()
        elif not active_tournament[0].start_round:
            information = "Impossible il n'y a pas de tour commencer ! \n\nVeuillez lancer un tour"
            self.view.information(information)
            return self.menu_back()

        else:
            round_end = self.view.end_round_tournament(active_tournament)
            date_time = datetime.now()
            active_tournament[0].end_round = date_time.strftime(
                "%d/%m/%Y, %H:%M:%S")
            active_tournament[0].list_of_matchs = round_end
            round_update = []
            round_update.append({
                                "round": "Round " + str(active_tournament[0].current_round),
                                "start_round": active_tournament[0].start_round,
                                "end_round": active_tournament[0].end_round,
                                "list_of_match": active_tournament[0].list_of_matchs
                                })
            active_tournament[0].list_of_rounds.append(round_update)

            for items in active_tournament[0].list_of_matchs:
                position = 0
                player_1 = []
                player_2 = []
                player_1.append(items[0])
                player_2.append(items[1])

                for item in active_tournament[0].list_of_players:
                    if player_1[0]["player_id"] == item["player_id"]:
                        active_tournament[0].list_of_players[position]["points"] += (
                            player_1[0]["points"])
                        active_tournament[0].list_of_players[position]["players_played"].append(
                            player_2[0]["player_id"])
                    elif player_2[0]["player_id"] == item["player_id"]:
                        active_tournament[0].list_of_players[position]["points"] += (
                            player_2[0]["points"])
                        active_tournament[0].list_of_players[position]["players_played"].append(
                            player_1[0]["player_id"])
                    position += 1

            active_tournament[0].start_round = ""
            active_tournament[0].end_round = ""
            active_tournament[0].list_of_matchs = []
            active_tournament[0].current_round += 1

            if active_tournament[0].current_round > active_tournament[0].number_of_round:
                information = "Fin du tournoi ! "
                self.view.information(information)
                active_tournament[0].tournament_valid = False
                self.tournament_manager.update_tournament(self, active_tournament)
                #Récupération des joueurs de la base
                data_players = self.player_manager.get_all_players(self)
                player_id = 0
                for player_tournament in active_tournament[0].list_of_players:
                    for player_base in data_players:
                        if player_base.player_id == player_tournament["player_id"]:
                            data_players[player_id].points += player_tournament["points"]
                            break
                    player_id +=1
                self.player_manager.update_players(self, data_players)

            else:
                self.tournament_manager.update_tournament(self, active_tournament)
                #Demande si on fini un tour pour démmarer un nouveau tour
                question = "Souhaitez-vous démarrer un nouveau tour ?"
                validation = self.view.validation_request(question)
                if validation:
                    return self.start_round_controller()
                else:
                    return self.menu_back()


    def comment_controller(self):
        """Reste à faire"""
        active_tournament = NewTournamentController.choice_tournaments(self)
        comment = self.view.add_comment()
        active_tournament[0].comments += comment
        self.tournament_manager.update_tournament(self, active_tournament)

        return self.menu_back()


    def end_screen_controller(self):
        """Sortie du programme"""
        return


    def menu_back(self):
        """Méthodes pour aller au menu d'accueil"""
        handler = menu_tournament_controller.TournamentMenuController()
        return handler
