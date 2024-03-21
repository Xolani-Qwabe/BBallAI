from src.models.confrence.eastern_conference import Eastern_Conference


class South_East(Eastern_Conference):
    def __init__(self, name):
        super().__init__(name)
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)
