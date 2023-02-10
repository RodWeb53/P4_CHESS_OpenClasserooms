"""Modele de données d'un joueur"""

class Player:

    def __init__(self, last_name, first_name, birth_date, id=None, points=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.id = id
        self.points = points

    
    def set_last_name(self, last_name):
        self.last_name = last_name

    
    def set_first_name(self, first_name):
        self.first_name = first_name


    def set_birth_date(self, birth_date):
        self.birth_date = birth_date


    def set_id(self, id):
        self.id = id


    def set_points(self, points):
        self.points = points
        