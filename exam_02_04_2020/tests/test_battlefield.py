import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):

    def test_fight__when_attacker_is_dead__should_raise_ValueError(self):
        battle_field = BattleField()
        attacker = Beginner("beginner")
        enemy = Advanced("advanced")
        with self.assertRaises(ValueError) as message:
            attacker.health = 0
            battle_field.fight(attacker, enemy)
        self.assertEqual("Player is dead!", str(message.exception))

    def test_fight__when_enemy_is_dead__should_raise_ValueError(self):
        battle_field = BattleField()
        attacker = Beginner("beginner")
        enemy = Advanced("advanced")
        with self.assertRaises(ValueError) as message:
            enemy.health = 0
            battle_field.fight(attacker, enemy)
        self.assertEqual("Player is dead!", str(message.exception))

    def test_fight__when_attacker_is_beginner__should_increase_health(self):
        battle_field = BattleField()
        card = MagicCard("Card")
        player = Beginner("beginner")
        enemy = Advanced("advanced")
        player.card_repository.cards = [card]
        battle_field.fight(player, enemy)
        self.assertEqual(35, player.card_repository.cards[0].damage_points)
        self.assertEqual(170, player.health)
        self.assertEqual(215, enemy.health)

    def test_fight__when_enemy_is_beginner__should_increase_health(self):
        battle_field = BattleField()
        card = MagicCard("Card")
        player = Advanced("advanced")
        enemy = Beginner("beginner")
        enemy.card_repository.cards = [card]
        battle_field.fight(player, enemy)
        self.assertEqual(35, enemy.card_repository.cards[0].damage_points)
        self.assertEqual(250, player.health)
        self.assertEqual(135, enemy.health)

    def test_fight__when_enemy_is_dead_in_battle__should_raise(self):
        battle_field = BattleField()
        card = MagicCard("Card")
        card_2 = TrapCard("Card_2")
        card_3 = TrapCard("Card_3")
        player = Advanced("advanced")
        enemy = Beginner("beginner")
        enemy.card_repository.cards = [card, card_2, card_3]
        with self.assertRaises(ValueError) as message:
            battle_field.fight(player, enemy)
        self.assertEqual("Player's health bonus cannot be less than zero.", str(message.exception))


    def test_is_beginner__when_player_is_beginner__should_return_True(self):
        battle_field = BattleField()
        player = Beginner("Test")
        result = battle_field.is_beginner(player)
        self.assertTrue(result)
    



if __name__ == "__main__":
    unittest.main()