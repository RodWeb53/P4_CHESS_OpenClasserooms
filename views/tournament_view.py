"""Module views du menu Tournoi"""
import time
import random
from utils.tournament import UtilsTournament
from utils.clean_screen import clear


class NewTournamentView:
    """View de création d'un tournoi"""

    def __init__(self):
        self.utils_tournament = UtilsTournament

    def new_tournament(self):
        """Vue pour la création d'un nouveau tournoi"""
        create_entry = True
        while create_entry:
            tournament_name = self.utils_tournament.display_menu_name(self)
            tournament_place = self.utils_tournament.display_menu_place(self)
            start_date = self.utils_tournament.display_menu_days(self)
            number_of_round = self.utils_tournament.display_menu_number_of_rounds(
                self)
            create_entry = False
        new_tournament_add = {
            "tournament_name": tournament_name,
            "tournament_place": tournament_place,
            "start_date": start_date,
            "number_of_round": number_of_round,
            }
        return new_tournament_add

    def choice_tournament(self, data_tournaments):
        """Méthodes pour choisir un tournoi"""
        number = []
        clear()
        print("Sélectionner un tournoi dans la liste suivante :\n")
        print("".ljust(96, "-"))
        print("|  N° ".ljust(11) + "|".ljust(16) + "Nom".ljust(26) +
              "|".ljust(16) + "Emplacement".ljust(26) + "|")
        print("".ljust(96, "-"))
        for item in data_tournaments:
            number.append(item.tournament_id)
            print("|  " + str(item.tournament_id).ljust(8) + "| " +
                  str(item.tournament_name).ljust(40) + "| " +
                  str(item.tournament_place).ljust(40) + "| ")
            print("".ljust(96, "-"))
        print("".ljust(96, "-") + "\n")
        print("Entrez le N° de tournoi souhaité :\n")
        choice = input("Votre choix >>  ")
        entry = True
        while entry:
            if not choice.isnumeric() or int(choice) not in number:
                print("Le numéro saisie n'est pas dans la liste des choix")
                choice = input("Votre nouveau choix >>  ")
            else:
                entry = False
        return choice

    def add_player_tournament(self, data_players, list_players):
        """Vue pour l'ajout des joueurs pour un tournoi"""
        players_data = data_players
        titre = ""
        titre_tiret = "|"
        titre_num = "|  N°"
        titre_nom = "|  Nom"
        titre_prenom = "|  Prenom"
        number = 0
        list_base = []
        print("Sélectionner un joueur dans la liste suivante \n")
        print(titre.ljust(69, "-"))
        print(titre_num.ljust(8) + titre_nom.ljust(20) +
              titre_prenom.ljust(40) + titre_tiret)
        print(titre.ljust(69, "-"))
        for item in players_data:
            number += 1
            list_base.append(item)
            print(titre.ljust(69, "-"))
            print(titre_tiret.ljust(3) + str(number).ljust(5) +
                  titre_tiret.ljust(3) + str(item.last_name).ljust(17) +
                  titre_tiret.ljust(3) + str(item.first_name).ljust(37) +
                  titre_tiret
                  )
        print(titre.ljust(69, "-") + "\n")
        print("Entrez le N° du joueur souhaité \n")
        choice = input("Votre choix >>  ")
        entry = True
        while entry:
            if not choice.isnumeric() or int(choice) > number:
                print("Le numéro saisie n'est pas dans la liste des choix")
                choice = input("Votre nouveau choix >>  ")
            else:
                choice = int(choice)
                list_players.append(list_base[choice - 1])
                del list_base[choice - 1]
                verify = True
                while verify:
                    print("")
                    print("Souhaitez-vous ajouter un autre joueur \n")
                    print("   o / n \n")
                    user_choice = input("Votre choix >>  ")
                    if user_choice == "o":
                        data_players = list_base
                        if not data_players:
                            information = "Désolé la base de joueur est vide"
                            self.information(information)
                        else:
                            NewTournamentView.add_player_tournament(
                                self, data_players, list_players)
                        verify = False
                    elif user_choice == "n":
                        print("Sauvegarde des joueurs")
                        verify = False
                entry = False
        return list_players

    def validation_request(self, question):
        """Méthode pour valider un choix utilisateur"""
        clear()
        validation = self.utils_tournament.display_validation(self, question)
        return validation

    def information(self, information):
        """Méthode pour afficher une information"""
        clear()
        espace = ""
        print(espace.ljust(60, "-") + "\n")
        print(information + "\n")
        print(espace.ljust(60, "-"))
        time.sleep(4.0)

    def start_gamme_tournament(self, list_player_gamme):
        """Vue pour le lancement d'une partie"""
        entry = True
        list_of_matchs = []
        list_gamme = list_player_gamme
        random.shuffle(list_gamme)
        while entry:
            if len(list_gamme) >= 2:
                list_of_matchs.append((list_gamme[0], list_gamme[1]))
                del list_gamme[1], list_gamme[0]
            else:
                entry = False
        clear()
        print("La liste des matchs pour le round 1")
        UtilsTournament.display_match(self, list_of_matchs)
        print("Continuer, appuyer sur 'Entrée'")
        input("")
        return list_of_matchs

    def end_round_tournament(self, active_tournament):
        """vue pour la fin d'un round"""
        list_of_matchs = active_tournament[0].list_of_matchs
        UtilsTournament.display_result_match(self, list_of_matchs)
        return active_tournament[0].list_of_matchs

    def start_round_tournament(self, active_tournament):
        """Création d'un round"""
        list_of_matchs = []
        single_or_multiple_turn = (len(
            active_tournament[0].list_of_players) - active_tournament[0].current_round)
        list_players = active_tournament[0].list_of_players
        list_players = sorted(
            list_players, key=lambda player: player["points"], reverse=True)
        entry = True
        # Si le nombre de joueurs par rapport permet de faire des tours unique
        if single_or_multiple_turn >= 1:
            while entry:
                number_player = len(list_players)
                if number_player >= 2:
                    for i in range(1, number_player):
                        if not list_players[i]["player_id"] in list_players[0]["players_played"]:
                            list_of_matchs.append(
                                (list_players[0], list_players[i]))
                            del list_players[i], list_players[0]
                            break
                    else:
                        list_of_matchs.append(
                            (list_players[0], list_players[i]))
                        del list_players[i], list_players[0]
                else:
                    entry = False
        else:
            # Si le nombre de tours est supérieur ou égal au nombres de joueurs
            while entry:
                number_player = len(list_players)
                if number_player >= 2:
                    list_of_matchs.append((list_players[0], list_players[1]))
                    del list_players[1], list_players[0]
                else:
                    entry = False

        clear()
        print(f'La liste des matchs pour le round  {active_tournament[0].current_round}')
        UtilsTournament.display_match(self, list_of_matchs)
        print("Continuer, appuyer sur 'Entrée'")
        input("")
        return list_of_matchs

    def missing_a_player(self):
        """information que le nombre de joueurs n'est pas pair"""
        print("Le nombre de joueur n'est pas pair")

    def add_comment(self):
        """La vue pour l'ajout de commentaire"""
        clear()
        print("Entrez votre commentaire (ligne vide pour sortir)\n")
        lines = ""
        entry = True
        while entry:
            line = input()
            if not line == "":
                lines += line + "\n"
            else:
                entry = False
        question = "Confirmez vous l'eregistrement du commentaire"
        response = self.validation_request(question)
        # Si on ne veut pas enregistrer le commentaire on vide les lignes
        if not response:
            lines = ""
        return lines

    def end_tournamment(self):
        """Saisie de la date de fin de tournoi"""
        end_date = self.utils_tournament.display_menu_days(self)
        return end_date
