from src.models.teams.team import Team
from src.models.players.positions import Positions


class Player(Team):
    def __init__(self, name, position, team):
        super().__init__(name)
        self.position = Positions
        self.statistics = {}
        self.team = team

    def add_statistic(self, statistic_name, value):
        self.statistics[statistic_name] = value
