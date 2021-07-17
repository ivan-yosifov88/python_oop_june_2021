class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        filtered_players = [player for player in self.__players if player.name == player_name]
        if not filtered_players:
            return f"Player {player_name} not found"

        player_for_remove = filtered_players[0]
        self.__players.remove(player_for_remove)
        return player_for_remove