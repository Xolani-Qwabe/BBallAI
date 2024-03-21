from src.models.confrence.western_conference import Western_Conference


class Pacific(Western_Conference):
    def __init__(self, name):
        super().__init__(name)
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)
  


