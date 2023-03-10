"""Module views du menu Tournoi"""
from utils.clean_screen import clear


class ReportMenuView:
    """Tournoi menu views"""
    def __init__(self, menu):
        self.menu = menu

    # Création d'une méthodes pour afficher le menu
    def _display_menu(self):
        clear()
        print("")
        print("♔ 🏁        Menu gestion des rapports       🏁 ♔ \n")
        print("------------------------------------------------")
        for key, entry in self.menu.items():
            print(f"|  {key} : {entry.option}")
            print("------------------------------------------------")

    def get_user_choice_tournament(self):
        """Boucle pour afficher tant que l'utilisateur n'a pas fait de bon choix"""
        while True:
            # Afficher le menu à l'utilisateur
            self._display_menu()
            # Demander à l'utilisateur de faire un choix
            choice = input("Entrez votre choix >> ")
            # Valider le choix de l'utilisateur
            if choice in self.menu:
                # Retourner le choix de l'utilisateur
                return self.menu[choice]
