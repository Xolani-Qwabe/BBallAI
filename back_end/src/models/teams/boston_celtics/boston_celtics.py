from src.models.confrence.eastern_conference import Eastern_Conference
from src.models.teams.team import Team
from src.models.divisions.atlantic import Atlantic
import numpy as np
import pandas as pd


class Boston_Celtics(Team):

    def __init__(self, name="Boston_Celtics", city="Boston", conference=Eastern_Conference, division=Atlantic):
        super().__init__(name)
        self.city = city
        self.conference = conference
        self.division = division
        self.roster = []

    def add_player(self, player):
        self.roster.append(player)

    @staticmethod
    def get_roster():
        roster = pd.read_csv(r"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\BOS\BOS_Roster.csv")




roster = Boston_Celtics.get_roster()
