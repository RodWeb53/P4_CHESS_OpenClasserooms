"""Module manager des modèles pour la gestion de la BD des tournois"""
import json
import os
from models.entities.tournament_entity import Tournament


class TournamentManager:
    """Class manager pour les tournois"""

    def __init__(self):
        self.tournament = Tournament

    def get_tournament(self, id_tournament):
        """Lecture du fichier JSON des tournois pour récupérer un tournoi suivant son id"""
        with open(os.path.join('data/tournaments',
                                "tournaments.json"), "r", encoding="UTF-8") as read_file:
            data = json.load(read_file)

        # list_tournament.append(Tournament(**i))

        list_tournament = []

        # for items in data:
        #     list_tournament.append(Tournament(**items))

        for items in data:
            if str(items["tournament_id"]) == str(id_tournament):
                list_tournament.append(Tournament(**items))

        return list_tournament



    def save_tournament(self, tournament):
        """Méthodes pour la sauvegarde des tournois"""
        new_tournament = {
            "tournament_id": tournament.tournament_id,
            "tournament_name": tournament.tournament_name,
            "tournament_place": tournament.tournament_place,
            "start_date": tournament.start_date,
            "end_round": tournament.end_round,
            "start_round": tournament.start_round,
            "number_of_round": tournament.number_of_round,
            "list_of_rounds": tournament.list_of_rounds,
            "current_round": tournament.current_round,
            "list_of_players": tournament.list_of_players,
            "list_of_matchs": tournament.list_of_matchs,
            "comments": tournament.comments
        }
        # récupération des utilisateurs du fichier Json
        data = TournamentManager.get_all_tournament_json(self)
        # Création d'un liste vide pour mettre les tournois connus
        new_list = []
        last_id = 1
        # boucle pour lire les tournois de la DB et récupérer le N° id du dernier tournoi
        for items in data:
            new_list.append(items)
            last_id += 1

        # Affection du N° id au nouveau tournoi
        new_tournament["tournament_id"] = last_id
        # Ajout du nouveau tournoi à la liste
        new_list.append(new_tournament)

        # Sauvegarde de la liste des tournois

        out_file = open(os.path.join('data/tournaments',
                        "tournaments.json"), "w", encoding="UTF-8")
        json.dump(new_list, out_file, indent=4)
        out_file.close()

    def update_tournament(self, tournament):
        """Méthodes pour la modification des données d'un tournoi"""
        print("print du manager tournament")
        print(tournament)
        print("")
        new_tournament = {
            "tournament_id": tournament[0].tournament_id,
            "tournament_name": tournament[0].tournament_name,
            "tournament_place": tournament[0].tournament_place,
            "start_date": tournament[0].start_date,
            "end_round": tournament[0].end_round,
            "start_round": tournament[0].start_round,
            "number_of_round": tournament[0].number_of_round,
            "list_of_rounds": tournament[0].list_of_rounds,
            "current_round": tournament[0].current_round,
            "list_of_players": tournament[0].list_of_players,
            "list_of_matchs": tournament[0].list_of_matchs,
            "comments": tournament[0].comments
        }
        # récupération des utilisateurs du fichier Json
        data = TournamentManager.get_all_tournament_json(self)
        list_tournament = []

        # Création d'un liste vide pour mettre les tournois connus
        new_list = []

        for item in data:
            new_list.append(item)

        for items in new_list:
            if items["tournament_id"] == new_tournament["tournament_id"]:
                list_tournament.append(new_tournament)
            else:
                list_tournament.append(items)

        # Sauvegarde de la liste des tournois

        out_file = open(os.path.join('data/tournaments',
                        "tournaments.json"), "w", encoding="UTF-8")
        json.dump(list_tournament, out_file, indent=4)
        out_file.close()

    def get_all_tournament(self):
        """Lecture du fichier JSON des tournois"""
        with open(os.path.join('data/tournaments',
                                "tournaments.json"), "r", encoding="UTF-8") as read_file:
            data = json.load(read_file)
        list_tournaments = []

        for i in data:
            list_tournaments.append(Tournament(**i))

        return list_tournaments

    def get_all_tournament_json(self):
        """Lecture du fichier JSON des tournois"""
        with open(os.path.join('data/tournaments',
                                "tournaments.json"), "r", encoding="UTF-8") as read_file:
            data = json.load(read_file)

        return data
