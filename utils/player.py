"""Module pour le controle de saisie d'un nouveau joueur"""
import datetime
from utils.clean_screen import clear

class UtilsPlayer:
    """Controle des saisies"""
    def __init__(self):
        pass

    def display_menu_last_name():
        """Menu pour demande le nom et le controle"""
        clear()
        print("")
        print("Entrez le Nom du nouveau joueur :")
        last_name = input("Votre saisie >> ")
        while not(last_name.isalpha()) or last_name == "":
            print("Le nom de peut être vide ou avec un nombre")
            print("Entrez de nouveau un nom :")
            last_name = input("Votre nouvelle saisie >> ")

        return last_name


    def display_menu_first_name():
        """Vérification du prénom saisie et le controle"""
        print("")
        print("Entrez le prénom du nouveau joueur :")
        first_name = input("Votre saisie >> ")
        while not(first_name.isalpha()) or first_name == "":
            print("Le prénom de peut être vide ou avec un nombre")
            print("Entrez de nouveau un prénom :")
            first_name = input("Votre nouvelle saisie >> ")

        return first_name
    

    def display_menu_birth_days():
        """Vérifiaction de la date de naissance et le controle"""
        date_format = '%d-%m-%Y'
        print("")
        print("Entrez la date de naissance au format jj-mm-aaaa :")
        birth_date = input("Votre saisie >> ")
        try:
            valide_date = datetime.datetime.strptime(birth_date, date_format)
        except ValueError:
            print("")
            print("La date saisie est non valide !")
            UtilsPlayer.display_menu_birth_days()
            return birth_date
        
        return birth_date
    

    def display_menu_user_choice_save():
        """Vérification si l'utilisateur veut enregistrer le joueur"""
        verify = True
        while verify:
            print("")
            print("Confirmez la création du nouveau joueur :")
            print("")
            print("   o / n")
            print("")
            user_choice_save = input("Votre confirmation >>")
            if user_choice_save == "o" or user_choice_save == "n":
                verify = False
        
        return user_choice_save

