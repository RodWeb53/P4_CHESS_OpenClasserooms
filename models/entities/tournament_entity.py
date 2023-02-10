"""Modèle de données d'un tournoi"""

class Tournament:

    def __init__(self, tournament_name, tournament_place, start_date,
                 number_of_round="", list_of_rounds=[], current_round="",
                 list_of_players=[], list_of_matchs=[], comments="",
                 tournament_id=0
                ):
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.start_date = start_date
        self.number_of_round = number_of_round
        self.list_of_rounds = list_of_rounds
        self.current_round = current_round
        self.list_of_players = list_of_players
        self.list_of_matchs = list_of_matchs
        self.comments = comments


    def set_tournament_name(self, tournament_name):
        self.tournament_name = tournament_name


    def set_tournament_place(self, tournament_place):
        self.tournament_place = tournament_place


    def set_start_date(self, start_date):
        self.start_date = start_date


    def set_number_of_round(self, number_of_round):
        self.number_of_round = number_of_round


    def set_list_of_rounds(self, list_of_rounds):
        self.list_of_rounds = list_of_rounds


    def set_current_round(self, current_round):
        self.current_round = current_round


    def set_list_of_players(self, list_of_players):
        self.list_of_players = list_of_players


    def set_list_of_matchs(self, list_of_matchs):
        self.list_of_matchs = list_of_matchs


    def set_comments(self, comments):
        self.comments = comments


    def set_tournament_id(self, tournament_id):
        self.tournament_id = tournament_id
