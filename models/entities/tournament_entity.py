"""Modèle de données d'un tournoi"""

class Tournament:
    """Modèle pour la création d'un tournoi"""

    def __init__(self, tournament_name, tournament_place, start_date, end_date="",
                 end_round="", start_round="", number_of_round="",
                 list_of_rounds=[], current_round="",
                 list_of_players=[], list_of_matchs=[], comments="",
                 tournament_id=0, tournament_valid = True
                ):
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_round = number_of_round
        self.list_of_rounds = list_of_rounds
        self.current_round = current_round
        self.list_of_players = list_of_players
        self.list_of_matchs = list_of_matchs
        self.comments = comments
        self.start_round = start_round
        self.end_round = end_round
        self.tournament_valid = tournament_valid


    def set_tournament_name(self, tournament_name):
        """Methodes set pour la création de tournament_name"""
        self.tournament_name = tournament_name


    def set_tournament_place(self, tournament_place):
        """Methodes set pour la création de tournament_place"""
        self.tournament_place = tournament_place


    def set_start_date(self, start_date):
        """Methodes set pour la création de start_date"""
        self.start_date = start_date


    def set_end_date(self, end_date):
        """Methodes set pour la création de start_date"""
        self.end_date = end_date


    def set_number_of_round(self, number_of_round):
        """Methodes set pour la création de number_of_round"""
        self.number_of_round = number_of_round


    def set_list_of_rounds(self, list_of_rounds):
        """Methodes set pour la création de list_of_rounds"""
        self.list_of_rounds = list_of_rounds


    def set_current_round(self, current_round):
        """Methodes set pour la création de current_round"""
        self.current_round = current_round


    def set_list_of_players(self, list_of_players):
        """Methodes set pour la création de list_of_players"""
        self.list_of_players = list_of_players


    def set_list_of_matchs(self, list_of_matchs):
        """Methodes set pour la création de list_of_matchs"""
        self.list_of_matchs = list_of_matchs


    def set_comments(self, comments):
        """Methodes set pour la création de comments"""
        self.comments = comments


    def set_tournament_id(self, tournament_id):
        """Methodes set pour la création de tournament_id"""
        self.tournament_id = tournament_id


    def set_start_round(self, start_round):
        """Methodes set pour la création de start_round"""
        self.start_round = start_round

    def set_end_round(self, end_round):
        """Methodes set pour la création de end_round"""
        self.end_round = end_round


    def set_tournament_valid(self, tournament_valid):
        """Methodes set pour la création de end_round"""
        self.tournament_valid = tournament_valid
