"""Module views ajouter un nouveau joueur a la BD Json"""
from utils.player import UtilsPlayer
from utils.clean_screen import clear


class AddPlayerView:
    """Add player views"""
    def __init__(self):
        self.utils_player = UtilsPlayer

    def new_player(self):
        """Demander à l'utilisateur des infos pour la création d'un joueur"""
        new_player_add = {}
        create_entry = True

        while create_entry:

            last_name = self.utils_player.display_menu_last_name(self)
            first_name = self.utils_player.display_menu_first_name(self)
            birth_date = self.utils_player.display_menu_birth_days(self)
            choice_user = self.utils_player.display_menu_user_choice_save(self)

            create_entry = False

        # Si on veut sauvegarder le joueur
        if choice_user == "o":
            new_player_add = {
                "last_name": str(last_name),
                "first_name": str(first_name),
                "birth_date": str(birth_date)
            }
            return new_player_add
        # Si le choix est non
        elif choice_user == "n":
            return -1


    def choice_player_next(self):
        """Méthode pour demandé si on crée un nouveau joueur"""
        clear()
        print("Votre joueur à été créer avec succes dans la base de donnée")
        choice_next = self.utils_player.display_menu_user_choice_new(self)
        if choice_next == "o":
            AddPlayerView.new_player(self)
        elif  choice_next == "n":
            return -1


    def choice_player_new(self):
        """Méthode pour demandé si on crée un nouveau joueur"""
        clear()
        print("Votre joueur n'a pas été créé !!")
        choice_new = self.utils_player.display_menu_user_choice_new(self)
        if choice_new == "o":
            return 1
        elif  choice_new == "n":
            return -1
