from guild_system.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        if player not in self.players:
            return f"Player {player.name} is in another guild."

        return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name):
        filter_players = [player for player in self.players if player.name == player_name]
        if not filter_players:
            return f"Player {player_name} is not in the guild."

        current_player = filter_players[0]
        self.players.remove(current_player)
        current_player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.players:
            result += player.player_info()
        return result

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
