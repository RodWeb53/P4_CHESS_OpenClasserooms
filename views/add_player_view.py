"""Module views ajouter un nouveau joueur a la BD Json"""
from utils.player import UtilsPlayer


class AddPlayerView:
    """Add player views"""
    def __init__(self):
        self.utils_player = UtilsPlayer

    def new_player(self):
        """Demander à l'utilisateur des infos pour la création d'un joueur"""
        new_player_add = {}
        create_entry = True

        while create_entry:

            last_name = self.utils_player.display_menu_last_name()
            first_name = self.utils_player.display_menu_first_name()
            birth_date = self.utils_player.display_menu_birth_days()
            choice_user = self.utils_player.display_menu_user_choice_save()

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




    def save_new_player(self, user_create):
        """Enregistrer un nouveau joueur"""
        self.add_player.new_player_save(user_create)
