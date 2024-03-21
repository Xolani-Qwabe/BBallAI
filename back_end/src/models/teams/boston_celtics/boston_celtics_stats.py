from src.models.stats.stats import Stats


class Boston_Celtics_Stats(Stats):
    def __init__(self, name):
        super().__init__(name)
        self.team_stats = {}

    def add_team_stats(self, team, statistics):
        self.team_stats[team] = statistics