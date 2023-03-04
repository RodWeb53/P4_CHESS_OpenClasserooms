"""Modele de données d'un joueur"""


class Player:
    """Modèle pour la création d'un joueur"""

    def __init__(self, last_name, first_name, birth_date, player_id=None, points=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.player_id = player_id
        self.points = points

    def set_last_name(self, last_name):
        """Methodes set pour la création de last_name"""
        self.last_name = last_name

    def set_first_name(self, first_name):
        """Methodes set pour la création de first_name"""
        self.first_name = first_name

    def set_birth_date(self, birth_date):
        """Methodes set pour la création de birth_date"""
        self.birth_date = birth_date

    def set_player_id(self, player_id):
        """Methodes set pour la création de player_id"""
        self.player_id = player_id

    def set_points(self, points):
        """Methodes set pour la création de points"""
        self.points = points
