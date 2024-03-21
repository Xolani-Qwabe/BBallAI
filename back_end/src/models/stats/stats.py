from src.models.nba import NBA


class Stats(NBA):
    def __init__(self, name):
        super().__init__(name)
        self.team_stats = {}

    def add_team_stats(self, team, statistics):
        self.team_stats[team] = statistics
