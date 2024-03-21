from src.models.nba import NBA


class Western_Conference(NBA):
    def __init__(self, name):
        super().__init__(name)
        self.divisions = []

    def add_division(self, division):
        self.divisions.append(division)