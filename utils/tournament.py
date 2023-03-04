"""Module utilitaire pour le tournoi"""
import datetime
from utils.clean_screen import clear


class UtilsTournament:
    """Controle des saisies"""

    def display_menu_name(self):
        """Menu pour demander le nom du tournoi"""
        clear()
        print("")
        print("Entrez le Nom du nouveau tournoi :")
        tournament_name = input("Votre saisie >> ")
        while tournament_name == "":
            print("Le nom du tournoi ne peut être vide")
            print("Entrez de nouveau un nom de tournoi :")
            tournament_name = input("Votre nouvelle saisie >> ")
        print("")
        return tournament_name

    def display_menu_place(self):
        """Menu pour demander l'emplacement du tournoi"""
        print("")
        print("Entrez l'emplacement du tournoi :")
        tournament_place = input("Votre saisie >> ")
        while tournament_place == "":
            print("L'emplacement du tournoi ne peut être vide")
            print("Entrez de nouveau l'emplacement du tournoi :")
            tournament_place = input("Votre nouvelle saisie >> ")
        print("")
        return tournament_place

    def display_menu_days(self):
        """Vérification de la date de début de tournoi et le controle"""
        date_format = '%d-%m-%Y'
        print("")
        print("Entrez la date du jour du tournoi au format jj-mm-aaaa :")
        start_date = input("Votre saisie >> ")
        try:
            datetime.datetime.strptime(start_date, date_format)
            # valide_date = datetime.datetime.strptime(start_date, date_format)
        except ValueError:
            print("")
            print("La date saisie est non valide !")
            UtilsTournament.display_menu_days(self)
            return start_date
        return start_date

    def display_menu_number_of_rounds(self):
        """Demande le nombre de tours du tournoi"""
        print("")
        print("Le nombre de tour dans le tournoi est de 4 par défaut")
        print("Est ce que vous voulez changer le nombre de tours ?")
        print("   o  /  n \n")
        choice = input("Votre saisie >>  ")
        print("")
        if choice == "o":
            print("Combien de tours souhaitez-vous faire ? \n")
            number_of_round = input("Votre saisie >>  ")
            if number_of_round.isnumeric():
                number_of_round = int(number_of_round)
                return number_of_round
        else:
            number_of_round = 4
            return number_of_round

    def display_validation(self, question):
        """Methode pour l'affichage d'une question"""
        verify = True
        while verify:
            print("")
            print(question + "\n")
            print("   o / n \n")
            user_choice = input("Votre choix >>  ")
            if user_choice == "o":
                verify = False
                return True
            elif user_choice == "n":
                verify = False
                return False

    def display_match(self, list_of_matchs):
        """Affichage des matchs dans un round"""
        number = 0
        print("".ljust(96, "-"))
        print("| Match N° ".ljust(10) + "|".ljust(16) + "Joueur 1".ljust(26) +
              "|".ljust(16) + "Joueur 2".ljust(26) + "|")
        print("".ljust(96, "-"))
        for item in list_of_matchs:
            number += 1
            print("|  " + str(number).ljust(8) + "| " +
                  item[0]["last_name"].ljust(20) +
                  item[0]["first_name"].ljust(20) + "| " +
                  item[1]["last_name"].ljust(20) +
                  item[1]["first_name"].ljust(20) + "| ")
            print("".ljust(96, "-"))

    def display_result_match(self, list_of_matchs):
        """Affichage des matchs dans un round"""
        match = 1
        espace = ""
        print(espace.ljust(35, "-") + "\n")
        for item in list_of_matchs:
            clear()
            print("Match : " + str(match))
            print(espace.ljust(10, "-"))
            print(espace.ljust(8) +
                  item[0]["last_name"].ljust(15) + item[0]["first_name"])
            print(espace.ljust(20) + "VS")
            print(espace.ljust(8) +
                  item[1]["last_name"].ljust(15) + item[1]["first_name"] + "\n")
            print(espace.ljust(35, "-") + "\n")
            print("Qui est le vainqueur du match ? \n")
            print(" 1 - " + item[0]["last_name"].ljust(15) +
                  item[0]["first_name"].ljust(15) + "est le vainqueur")
            print(" 2 - " + item[1]["last_name"].ljust(15) +
                  item[1]["first_name"].ljust(15) + "est le vainqueur")
            print(" 3 - Match nul pas de vainqueur \n")

            resultat = input("Votre réponse >> ")
            entry = True
            while entry:
                if resultat.isnumeric() and int(resultat) >= 1 and int(resultat) <= 3:
                    if int(resultat) == 1:
                        item[0]["points"] = 1
                        item[1]["points"] = 0
                    elif int(resultat) == 2:
                        item[0]["points"] = 0
                        item[1]["points"] = 1
                    elif int(resultat) == 3:
                        item[0]["points"] = 0.5
                        item[1]["points"] = 0.5
                    match += 1
                    entry = False
                else:
                    print("Le résultat n'est pas dans la liste de choix")
                    resultat = input("Votre réponse >> ")
