from src.models.teams.team import Team


class Detroit_Pistons(Team):
    def __init__(self, name, city, conference, division):
        super().__init__(name)
        self.city = city
        self.conference = conference
        self.division = division
        self.roster = []

    def add_player(self, player):
        self.roster.append(player)

