"""Module views du menu Tournoi"""
import time
from utils.tournament import UtilsTournament
from utils.clean_screen import clear

class NewTournamentView:
    """View de création d'un tournoi"""
    def __init__(self):
        self.utils_tournament = UtilsTournament


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
        titre_num = "|  N°"
        titre_nom = "|  Nom"
        titre_emplacement = "|  Emplacement"
        titre_tiret = "|"
        titre = ""
        clear()
        print("Sélectionner un tournoi dans la liste suivante")
        print("")
        print(titre.ljust(69, "-"))
        print(titre_num.ljust(8) + titre_nom.ljust(20) + titre_emplacement.ljust(40) + titre_tiret)
        print(titre.ljust(69, "-"))

        for item in self.data_tournaments:
            number += 1
            print(titre.ljust(69, "-"))
            print(titre_tiret.ljust(3) + str(item.tournament_id).ljust(5) +
                    titre_tiret.ljust(3) + str(item.tournament_name).ljust(17) +
                    titre_tiret.ljust(3) + str(item.tournament_place).ljust(37) + 
                    titre_tiret
                )
        print(titre.ljust(69, "-"))
        print("")
        print("Entrez le N° de tournoi souhaité")
        print("")
        choice = input("Votre choix >>  ")
        entry = True
        while entry:
            if not choice.isnumeric() or int(choice) > number:
                print("Le numéro saisie n'est pas dans la liste des choix")
                choice = input("Votre nouveau choix >>  ")
            else:
                entry = False

        return choice


    def add_player_tournament(self, data_players, list_players):
        #méthodes pour ajouter des joueurs au tournoi
        self.players_data = data_players
        titre = ""
        titre_tiret = "|"
        titre_num = "|  N°"
        titre_nom = "|  Nom"
        titre_prenom = "|  Prenom"
        number = 0
        self.list_players = list_players
        list_base = []

        print("Sélectionner un joueur dans la liste suivante")
        print("")
        print(titre.ljust(69, "-"))
        print(titre_num.ljust(8) + titre_nom.ljust(20) + titre_prenom.ljust(40) + titre_tiret)
        print(titre.ljust(69, "-"))

        for item in self.players_data:
            number += 1
            list_base.append(item)
            print(titre.ljust(69, "-"))
            print(titre_tiret.ljust(3) + str(number).ljust(5) +
                    titre_tiret.ljust(3) + str(item.last_name).ljust(17) +
                    titre_tiret.ljust(3) + str(item.first_name).ljust(37) + 
                    titre_tiret
                )
        print(titre.ljust(69, "-"))
        print("")
        print("Entrez le N° du joueur souhaité")
        print("")
        choice = input("Votre choix >>  ")
        entry = True
        while entry:
            if not choice.isnumeric() or int(choice) > number:
                print("Le numéro saisie n'est pas dans la liste des choix")
                choice = input("Votre nouveau choix >>  ")
            else:
                choice = int(choice)
                list_players.append(list_base[choice -1])
                del list_base[choice -1]
                verify = True
                while verify:
                    print("")
                    print("Souhaitez-vous ajouter un autre joueur")
                    print("")
                    print("   o / n")
                    print("")
                    user_choice = input("Votre choix >>  ")
                    if user_choice == "o":
                        data_players = list_base
                        if data_players == []:
                            print("Désolé la base de joueur est vide")
                            verify = False
                        else:
                            NewTournamentView.add_player_tournament(self, data_players, list_players)
                    elif  user_choice == "n":
                        print("Sauvegarde des joueurs")
                    verify = False

                entry = False

        return list_players


    def validation_request(self, question):
        """Méthode pour valider un choix utilisateur"""
        clear()
        validation = self.utils_tournament.display_validation(self, question)
        
        return validation
    

    def start_gamme_tournament(self, list_player_gamme):
        match = 1
        espace = ""
        entry = True
        list_of_matchs = []
        while entry:
            if len(list_player_gamme) >=2:
                list_of_matchs.append((list_player_gamme[0], list_player_gamme[1]))
                del list_player_gamme[1], list_player_gamme[0]

            else:
                entry = False
        clear()
        print("La liste des matchs pour le round 1")
        print(espace.ljust(35, "-"))
        print("")
        for item in list_of_matchs:
            print("Match : " + str(match))
            print(espace.ljust(10, "-"))
            print(espace.ljust(8) + item[0]["last_name"].ljust(15) + item[0]["first_name"])
            print(espace.ljust(20) + "VS")
            print(espace.ljust(8) + item[1]["last_name"].ljust(15) + item[1]["first_name"])
            print(espace.ljust(35, "-"))
            print("")
            match +=1
        
        return list_of_matchs

    def missing_a_player(self):
        print("Le nombre de joueur n'est pas pair")


    def tournament_current(self):
        clear()
        print("Impossible le tournoi est commencé")
        time.sleep(2.0)

