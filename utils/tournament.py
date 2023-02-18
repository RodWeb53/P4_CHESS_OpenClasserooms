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
        print("Entrez la date de de début de tournoi au format jj-mm-aaaa :")
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
        print("   o  /  n")
        print("")
        choice = input("Votre saisie >>  ")
        print("")
        if choice == "o":
            print("Combien de tours souhaitez-vous faire ?")
            print("")
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
            print(question)
            print("")
            print("   o / n")
            print("")
            user_choice = input("Votre choix >>  ")
            if user_choice == "o":
                verify = False
                return True
            elif user_choice == "n":
                verify = False
                return False

    def display_match(self, list_of_matchs):
        """Affichage des matchs dans un round"""
        match = 1
        espace = ""
        print(espace.ljust(35, "-"))
        print("")
        for item in list_of_matchs:
            print("Match : " + str(match))
            print(espace.ljust(10, "-"))
            print(espace.ljust(8) +
                  item[0]["last_name"].ljust(15) + item[0]["first_name"])
            print(espace.ljust(20) + "VS")
            print(espace.ljust(8) +
                  item[1]["last_name"].ljust(15) + item[1]["first_name"])
            print(espace.ljust(35, "-"))
            print("")
            match += 1

    def display_result_match(self, list_of_matchs):
        """Affichage des matchs dans un round"""
        match = 1
        espace = ""
        print(espace.ljust(35, "-"))
        print("")
        for item in list_of_matchs:
            # clear()
            print("Match : " + str(match))
            print(espace.ljust(10, "-"))
            print(espace.ljust(8) +
                  item[0]["last_name"].ljust(15) + item[0]["first_name"])
            print(espace.ljust(20) + "VS")
            print(espace.ljust(8) +
                  item[1]["last_name"].ljust(15) + item[1]["first_name"])
            print(espace.ljust(35, "-"))
            print("")
            print("Qui est le vainqueur du match ?")
            print("")
            print(" 1 - " + item[0]["last_name"].ljust(15) +
                  item[0]["first_name"].ljust(15) + "est le vainqueur")
            print(" 2 - " + item[1]["last_name"].ljust(15) +
                  item[1]["first_name"].ljust(15) + "est le vainqueur")
            print(" 3 - Match nul pas de vainqueur")
            print("")

            # while entry:
            resultat = input("Votre réponse >> ")
            print("La réponse est :")
            # print(resultat)

            if resultat.isnumeric() and int(resultat) <= 3:

                if int(resultat) == 1:
                    print("dans le premier if des points")
                    item[0]["points"] = 1
                    item[1]["points"] = 0
                    # entry = False

                elif int(resultat) == 2:
                    print("dans le deuxieme if des points")
                    item[0]["points"] = 0
                    item[1]["points"] = 1
                    # entry = False

                elif int(resultat) == 3:
                    print("dans le troisieme if des points")
                    item[0]["points"] = 0.5
                    item[1]["points"] = 0.5
                    # entry = False
            else:
                resultat = input("Votre réponse >> ")
                print("La réponse est :")
            # entry = False

            match += 1
            # print("List apres affectation des points")
            # print(list_of_matchs)
