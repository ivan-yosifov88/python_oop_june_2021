from project.player.player import Player


class Beginner(Player):
    initial_points = 50

    def __init__(self, username):
        super().__init__(username, self.initial_points)


