from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    @staticmethod
    def get_player(username, list_of_obj):
        return [obj for obj in list_of_obj if obj.username == username]

    def add(self, player: Player):
        current_player = self.get_player(player.username, self.players)
        if current_player:
            raise ValueError(f"Player {player.username} already exists!")

        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        filtered_players = self.get_player(player, self.players)
        if filtered_players:
            player_to_remove = filtered_players[0]
            self.players.remove(player_to_remove)
            self.count -= 1

    def find(self, username):
        filtered_players = self.get_player(username, self.players)
        if filtered_players:
            return filtered_players[0]
