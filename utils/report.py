"""Module pour le controle de saisie d'un nouveau joueur"""
# import datetime
from utils.clean_screen import clear


class UtilsReport:
    """Controle des saisies"""

    def __init__(self):
        pass

    def display_players_list(self):
        """Module pour l'affichage des titres des joueurs"""
        clear()
        print("".ljust(10, "#") +
              "  La liste des joueurs est la suivante :  " + "".ljust(10, "#"))
        print("".ljust(106, "-"))
        print("|     Nom".ljust(25) + "|     Prénom".ljust(25) +
              "|     Nombre de points".ljust(25) + "|     Date de naissance".ljust(30) + "|")
        print("".ljust(106, "-"))

    def display_player_list(self, item):
        """Module pour l'affichage des lignes de joueurs"""
        print("|  " + item.last_name.ljust(22) + "|  " + item.first_name.ljust(22) +
              "|  " + str(item.points).ljust(22) + "|  " + item.birth_date.ljust(27) + "|")
        print("".ljust(106, "-"))

    def display_players_tournament(self):
        """Module pour l'affichage du titre des joueurs pour un tournoi"""
        clear()
        print("".ljust(10, "#") +
              "  La liste des joueurs pour le tournoi est la suivante :  " + "".ljust(10, "#"))
        print("".ljust(106, "-"))
        print("|     Nom".ljust(37) + "|     Prénom".ljust(37) +
              "|     Nombre de points".ljust(31) + "|")
        print("".ljust(106, "-"))

    def display_player_tournament(self, item):
        """Module pour l'affichage des lignes de joueurs pour un tournoi"""
        print("|  " + item["last_name"].ljust(34) + "|  " + item["first_name"].ljust(34) +
              "|  " + str(item["points"]).ljust(28) + "|")
        print("".ljust(106, "-"))

    def display_tournaments_list(self):
        """Module pour l'affichage des titres des tournois"""
        clear()
        print("".ljust(10, "#") +
              "  La liste des tournois est la suivante :  " + "".ljust(10, "#"))
        print("".ljust(100, "-"))
        print("| Numéro  ".ljust(10) + "|     Nom".ljust(30) +
              "|     Lieu".ljust(30) + "|     Date du tournoi".ljust(29) + "|")
        print("".ljust(100, "-"))

    def display_tournament_list(self, item):
        """Module pour l'affichage des lignes de tournois"""
        print("|  " + str(item.tournament_id).ljust(7) + "|  " +
              str(item.tournament_name).ljust(27) + "|  " +
              str(item.tournament_place).ljust(27) + "|  " +
              str(item.start_date).ljust(26) + "|")
        print("".ljust(100, "-"))

    def display_detail_tournament(self, choice_tournament):
        """Module pour l'affichage des détails d'un tournoi"""
        clear()
        print("".ljust(10, "#") + "  Détails du tournoi N° " +
              str(choice_tournament[0].tournament_id) + "  ".ljust(10, "#"))
        print("".ljust(106, "-"))
        print("| Nom".ljust(20) + "|    " +
              str(choice_tournament[0].tournament_name).ljust(80) + "|")
        print("".ljust(106, "-"))
        print("| Lieu".ljust(20) + "|    " +
              str(choice_tournament[0].tournament_place).ljust(80) + "|")
        print("".ljust(106, "-"))
        print("| Date début".ljust(20) + "|    " +
              str(choice_tournament[0].start_date).ljust(80) + "|")
        print("".ljust(106, "-"))
        print("| Date fin".ljust(20) + "|    " +
              str(choice_tournament[0].end_date).ljust(80) + "|")
        print("".ljust(106, "-"))
