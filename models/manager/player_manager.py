"""Module manager des modèles pour la gestion de la BD des joueurs"""
import json
import os
from models.entities.player_entity import Player

class PlayerManager:
    """Class manager pour les joueurs"""

    def get_player(self, player_id):
        """Methode pour l'appel suivant l'id"""


    def save_player(self, player):
        """Méthodes pour la sauvegarde des joueurs"""
        new_player = {
            "player_id": player.player_id,
            "last_name": player.last_name,
            "first_name": player.first_name,
            "birth_date": player.birth_date,
            "points": player.points
        }

        # récupération des utilisateurs du fichier Json
        data = PlayerManager.get_all_players_json(self)
        # Création d'un liste vide pour mettre les joueurs connus
        new_list = []
        last_id = 1
        #boucle pour lire les joueurs de la DB et récupérer le N° id du dernier joueur
        for items in data:
            new_list.append(items)
            last_id += 1
        # Affection du N° id au nouveau joueur
        new_player["player_id"] = last_id
        # Ajout du nouveau joueur à la liste
        new_list.append(new_player)
        # Sauvegarde de la liste de joueurs
        out_file = open(os.path.join('data/players', "players.json"), "w", encoding="UTF-8")
        json.dump(new_list, out_file, indent=4)
        out_file.close()


    def update_players(self, data):
        """Méthodes pour update la base de joueurs"""
        new_list = []
        for item in data:
            new_player = {
            "player_id": item.player_id,
            "last_name": item.last_name,
            "first_name": item.first_name,
            "birth_date": item.birth_date,
            "points": item.points
        }
            new_list.append(new_player)

        out_file = open(os.path.join('data/players', "players.json"), "w", encoding="UTF-8")
        json.dump(new_list, out_file, indent=4)
        out_file.close()



    def get_all_players(self):
        """Lecture du fichier JSON des joueurs"""
        with open(os.path.join('data/players', "players.json"), "r", encoding="UTF-8") as read_file:
            data = json.load(read_file)
        list_players = []
        for i in data:
            list_players.append(Player(**i))

        return list_players


    def get_all_players_json(self):
        """Lecture du fichier JSON des joueurs"""
        with open(os.path.join('data/players', "players.json"), "r", encoding="UTF-8") as read_file:
            data = json.load(read_file)

        return data
