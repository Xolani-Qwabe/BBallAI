from src.models.nba import NBA


class Game(NBA):
    def __init__(self, name, date_time, game_info):
        super().__init__(name)
        self.date_time = date_time
        # game_info will be an object with information about the game
        self.game_info = game_info

    def add_team(self, team):
        self.teams.append(team)
