from src.models.nba import NBA
from src.models.stats.stats import Stats


class Season(NBA):
    def __init__(self, name, start_date, end_date):
        super().__init__(name)
        self.start_date = start_date
        self.end_date = end_date
        self.schedule = []
        self.stats = Stats("Season Stats")

    def add_game_to_schedule(self, game):
        self.schedule.append(game)