import datetime
from utils.clean_screen import clear

class UtilsTournament:
    """Controle des saisies"""
    def __init__(self):
        pass


    def display_menu_name():
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
    

    def display_menu_place():
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
    

    def display_menu_days():
        """Vérification de la date de début de tournoi et le controle"""
        date_format = '%d-%m-%Y'
        print("")
        print("Entrez la date de de début de tournoi au format jj-mm-aaaa :")
        start_date = input("Votre saisie >> ")
        try:
            valide_date = datetime.datetime.strptime(start_date, date_format)
        except ValueError:
            print("")
            print("La date saisie est non valide !")
            UtilsTournament.display_menu_days()
            return start_date
        
        return start_date
    

    def display_menu_number_of_rounds():
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
                return number_of_round
        else:
            number_of_round = 4
            return number_of_round
