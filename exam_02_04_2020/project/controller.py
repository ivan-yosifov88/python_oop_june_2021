from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    @staticmethod
    def get_name(obj_name, obj_list):
        return [obj for obj in obj_list if obj.username == obj_name]

    def add_player(self, type, username):
        if type == "Beginner":
            self.player_repository.add(Beginner(username))
        elif type == "Advanced":
            self.player_repository.add(Advanced(username))

        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type, name):
        if type == "Magic":
            self.card_repository.add(MagicCard(name))
        elif type == "Trap":
            self.card_repository.add(TrapCard(name))

        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        filtered_player = self.get_name(username, self.player_repository.players)
        filtered_card = [card for card in self.card_repository.cards if card.name == card_name]
        if filtered_player and filtered_card:
            filtered_player[0].card_repository.add(filtered_card[0])
            return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name, enemy_name):
        filtered_attackers = self.get_name(attack_name, self.player_repository.players)
        filtered_enemies = self.get_name(enemy_name, self.player_repository.players)
        if not (filtered_attackers and filtered_enemies):
            return

        attacker = filtered_attackers[0]
        enemy = filtered_enemies[0]
        battle_field = BattleField()
        battle_field.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for users in self.player_repository.players:
            result += f"Username: {users.username} - Health: {users.health} - Cards {users.card_repository.count}\n"
            for card in users.card_repository.cards:
                result += f"### Card: {card.name} - Damage: {card.damage_points}\n"
        return result
