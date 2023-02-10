"""Module views du menu Tournoi"""
from utils.tournament import UtilsTournament
from utils.clean_screen import clear

class NewTournamentView:
    """View de création d'un tournoi"""
    def __init__(self):
        self.utils_tournament = UtilsTournament
        pass

    def new_tournament(self):
        #méthode de création du tournoi
        create_entry = True

        while create_entry:

            tournament_name = self.utils_tournament.display_menu_name()
            tournament_place = self.utils_tournament.display_menu_place()
            start_date = self.utils_tournament.display_menu_days()
            number_of_round = self.utils_tournament.display_menu_number_of_rounds()

            create_entry = False

        new_tournament_add = {
            "tournament_name": tournament_name,
            "tournament_place": tournament_place,
            "start_date": start_date,
            "number_of_round": number_of_round
        }

        return new_tournament_add
    
    def choice_tournament(self, data_tournaments):
        #Sélection d'un tournoi dans une liste
        self.data_tournaments = data_tournaments
        number = 0
        clear()

        print("Sélectionner un tournoi dans la liste suivante")
        print("")
        print("-----------------------------------------------")
        print("|  N°      Nom            Emplacement")
        print("-----------------------------------------------")

        for item in self.data_tournaments:
            number += 1
            print("-----------------------------------------------")
            print("|  " + str(item.tournament_id).ljust(8, ' ') +
                    str(item.tournament_name).ljust(15, ' ') +
                    str(item.tournament_place).ljust(20, ' ')
                )
            print("-----------------------------------------------")

        print("")
        print(f"le nombre de tournoi est  {number}")
        print("Entrez le N° de tournoi souhaité")
        print("")
        choice = input("Votre choix >>  ")
        entry = True
        while entry:
            if not choice.isnumeric() or int(choice) > number:
                print("Le numéro saisie n'est pas dans la liste des choix")
                choice = input("Votre nouveau choix >>  ")
            entry = False

        return choice
 

    

    def add_player_tournament(self, data_tournament, data_players):
        #méthodes pour ajouter des joueurs au tournoi
        tournament_data = data_tournament
        players_data = data_players

        print("les données de tournaments data")
        print(tournament_data)
        print("")
        print("")
        print("les données de players data")
        print(players_data)



        