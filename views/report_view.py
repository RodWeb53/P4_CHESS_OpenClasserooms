"""Module views ajouter un nouveau joueur a la BD Json"""
from utils.player import UtilsPlayer
from utils.clean_screen import clear
from utils.tournament import UtilsTournament
from utils.report import UtilsReport


class ReportView:
    """Add player views"""

    def __init__(self):
        self.utils_player = UtilsPlayer
        self.utils_tournament = UtilsTournament
        self.utils_report = UtilsReport

    def sort_order(self):
        """Vue global de la liste des joueurs"""
        start = "|  "
        clear()
        print("dans la vue de la liste global des joueurs")
        print("".ljust(54, "-"))
        print(start + "Souhaitez-vous le classement par ordre : ".ljust(50) + start)
        print(start + " 1 - Alphabétique ".ljust(50) + start)
        print(start + " 2 - Classement ".ljust(50) + start)
        print("".ljust(54, "-") + "\n")
        choice = input("Votre choix >> ")
        entry = True
        while entry:
            if not choice.isnumeric() or int(choice) <= 0 or int(choice) > 2:
                print("Le numéro saisie n'est pas dans la liste des choix")
                choice = input("Votre nouveau choix >>  ")
            elif choice.isnumeric() and choice == 1:
                print("Le choix est 1")
            elif choice.isnumeric() and choice == 1:
                print("le choix est 2")
            else:
                entry = False

        return choice

    def list_global_players(self, choice, data_players):
        """Vue pour l'affichage des joueurs par ordre"""
        #Liste par classement alphabétique
        if int(choice) == 1:
            list_players = data_players
            list_players = sorted(
                list_players, key=lambda player: (
                    str.lower(player.last_name), str.lower(player.first_name)))
            UtilsReport.display_players_list(self)
            for item in list_players:
                UtilsReport.display_player_list(self, item)
        #Liste par classement des points
        else:
            list_players = data_players
            list_players = sorted(
                list_players, key=lambda player: (player.points, str.lower(
                    player.last_name), str.lower(player.first_name)), reverse=True)
            UtilsReport.display_players_list(self)
            for item in list_players:
                UtilsReport.display_player_list(self, item)

        print("Pour continuer, appuyer sur 'Entrée'")
        input("")
        return 0


    def tournaments_list(self, data_tournaments):
        """Vue pour l'affichage des tournois"""
        print("dans la vue des tournois")
        UtilsReport.display_tournaments_list(self)
        for item in data_tournaments:
            UtilsReport.display_tournament_list(self, item)

        print("Pour continuer, appuyer sur 'Entrée'")
        input("")


    def tournament_details(self, choice_tournament):
        """Vue pour l'affichage des détails d'un tournoi"""
        UtilsReport.display_detail_tournament(self, choice_tournament)

        print("Pour continuer, appuyer sur 'Entrée'")
        input("")


    def choice_tournament(self, data_tournaments):
        """Vue pour l'affichage des tournois"""
        number = []
        UtilsReport.display_tournaments_list(self)
        for item in data_tournaments:
            number.append(item.tournament_id)
            UtilsReport.display_tournament_list(self, item)
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

    def player_list_tournament(self, choice, data_players):
        """Vue pour l'affichage des joueurs d'un tournoi par ordre"""
        #Liste par classement alphabétique
        if int(choice) == 1:
            list_players = data_players[0].list_of_players
            list_players = sorted(
                list_players, key=lambda player: (
                    str.lower(player["last_name"]), str.lower(player["first_name"])))
            UtilsReport.display_players_tournament(self)
            for item in list_players:
                UtilsReport.display_player_tournament(self, item)
        #Liste par classement des points
        else:
            list_players = data_players[0].list_of_players
            list_players = sorted(
                list_players, key=lambda player: (player["points"], str.lower(
                    player["last_name"]), str.lower(player["first_name"])), reverse=True)
            UtilsReport.display_players_tournament(self)
            for item in list_players:
                UtilsReport.display_player_tournament(self, item)

        print("Pour continuer, appuyer sur 'Entrée'")
        input("")


    def commentary_tournament(self, data):
        """Vue pour l'affichage des commentaires d'un tournoi"""
        clear()
        print("".ljust(10, "#") +
              "  Les commentaires pour le tournoi sont les suivants :  " + "".ljust(10, "#"))
        print("".ljust(106, "-"))
        if data[0].comments:
            print(data[0].comments)
        else:
            print("Il n'y a pas de commentaire pour ce tournoi ")
        print("".ljust(106, "-") + "\n")
        print("Pour continuer, appuyer sur 'Entrée'")
        input("")


    def tournament_match(self, tournament):
        """Vue pour l'affichage des tours et des matchs pour un tournoi"""
        rounds = tournament[0].list_of_rounds
        clear()
        print("".ljust(100, "-"))
        print("".ljust(10, "#") + "".ljust(5) +
            "Liste des tours et des matchs pour le tournoi : " +
             tournament[0].tournament_name.ljust(27) + "".ljust(10, "#"))
        print("".ljust(100, "-"))

        for item in rounds:
            number = 0
            print("|".ljust(40) + item[0]["round"].ljust(40) + "".ljust(19) + "|")
            print("".ljust(100, "-"))
            print("| Match N° ".ljust(10) + "|".ljust(10) + "Joueur 1".ljust(20) +
                    "|".ljust(10) + "Joueur 2".ljust(20) + "|".ljust(10) +
                      "Vainqueur".ljust(18) + "|")
            print("".ljust(100, "-"))

            for matchs in item[0]["list_of_match"]:
                number += 1

                if matchs[0]["points"] == 1:
                    vainqueur = "Joueur 1"
                elif matchs[0]["points"] == 0:
                    vainqueur = "Joueur 2"
                else:
                    vainqueur = "Match nul"

                print("|  " + str(number).ljust(8) + "| " +
                       matchs[0]["last_name"].ljust(14) +
                         matchs[0]["first_name"].ljust(14) + "| " +
                         matchs[1]["last_name"].ljust(14) +
                           matchs[1]["first_name"].ljust(14) + "| ".ljust(10) +
                           vainqueur.ljust(18) + "|")
                print("".ljust(100, "-"))
        print("")
        print("Pour continuer, appuyer sur 'Entrée'")
        input("")
