"""Module manager des modèles pour la gestion de la BD des tournois"""
from models.entities.tournament_entity import Tournament
import json
import os

class TournamentManager:
    """Class manager pour les tournois"""

    def get_tournament(self, id_tournament):
        """Lecture du fichier JSON des tournois pour récupérer un tournoi suivant son id"""
        with open(os.path.join('data/tournaments', "tournaments.json"), "r", encoding="UTF-8") as read_file:
            data = json.load(read_file)

        list_tournament = []

        for items in data:
            list_tournament.append(Tournament(**items))

        for items in list_tournament:
            if str(items.tournament_id) == str(id_tournament):
                list_tournament = items

        return list_tournament


    def save_tournament(self, tournament):
        """Méthodes pour la sauvegarde des tournois"""
        new_tournament = {
            "tournament_id": tournament.tournament_id,
            "tournament_name": tournament.tournament_name,
            "tournament_place": tournament.tournament_place,
            "start_date": tournament.start_date,
            "number_of_round": tournament.number_of_round,
            "list_of_rounds": tournament.list_of_rounds,
            "current_round": tournament.current_round,
            "list_of_players": tournament.list_of_players,
            "list_of_matchs": tournament.list_of_matchs,
            "comments": tournament.comments
        }
        # récupération des utilisateurs du fichier Json
        data = TournamentManager.get_all_tournament()
        # Création d'un liste vide pour mettre les tournois connus
        new_list = []
        last_id = 1
        #boucle pour lire les tournois de la DB et récupérer le N° id du dernier tournoi
        for items in data:
            new_list.append(items)
            last_id += 1

        # Affection du N° id au nouveau tournoi
        new_tournament["tournament_id"] = last_id
        # Ajout du nouveau tournoi à la liste
        new_list.append(new_tournament)

        # Sauvegarde de la liste des tournois

       
        out_file = open(os.path.join('data/tournaments', "tournaments.json"), "w", encoding="UTF-8")
        json.dump(new_list, out_file, indent=4)
        out_file.close()



    def get_all_tournament():
        """Lecture du fichier JSON des tournois"""
        with open(os.path.join('data/tournaments', "tournaments.json"), "r", encoding="UTF-8") as read_file:
            data = json.load(read_file)
            
        return data