"""Module views du menu joueur"""
from utils.clean_screen import clear

class PlayerMenuView:
    """Player menu views"""
    def __init__(self, menu):
        self.menu = menu

    #Création d'une méthodes pour afficher le menu
    def _display_menu(self):
        clear()
        print("")
        print("♔ 🏁    Menu gestion des joueurs   🏁 ♔ \n")
        print("---------------------------------------")
        for key, entry in self.menu.items():
            print(f"|  {key} : {entry.option}")
            print("---------------------------------------")


    def get_user_choice(self):
        """Boucle pour afficher tant que l'utilisateur n'a pas fait de bon choix"""

        while True:
            # afficher le menu à l'utilisateur
            self._display_menu()
            # Demander à l'utilisateur de faire un choix
            choice = input("Entrez votre choix >> ")
            # Valider le choix de l'utilisateur
            if choice in self.menu:
                # Retourner le choix de l'utilisateur
                return self.menu[choice]
