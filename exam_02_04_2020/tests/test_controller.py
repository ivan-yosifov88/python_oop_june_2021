import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestController(unittest.TestCase):
    def test_init_method__when_initialise_repos_len__should_be_zero(self):
        controller = Controller()
        self.assertEqual(0, len(controller.player_repository.players))
        self.assertEqual(0, len(controller.card_repository.cards))

    def test_add_player__when_type_beginner__should_add(self):
        controller = Controller()
        controller.add_player("Beginner", "Test")
        self.assertIn("Test", controller.player_repository.players[0].username)
        self.assertEqual("Beginner", type(controller.player_repository.players[0]).__name__)

    def test_add_player__when_type_advanced_should_add(self):
        controller = Controller()
        controller.add_player("Advanced", "Test")
        self.assertIn("Test", controller.player_repository.players[0].username)
        self.assertEqual("Advanced", type(controller.player_repository.players[0]).__name__)

    def test_add_card__when_type_magic_should_add(self):
        controller = Controller()
        result = controller.add_card("Magic", "Magic")
        self.assertIn("Magic", controller.card_repository.cards[0].name)
        self.assertEqual("Successfully added card of type MagicCard with name: Magic", result)

    def test_add_card__when_type_trap_should_add(self):
        controller = Controller()
        result = controller.add_card("Trap", "Trap")
        self.assertIn("Trap", controller.card_repository.cards[0].name)
        self.assertEqual("Successfully added card of type TrapCard with name: Trap", result)

    def test_add_player_card__when_player_and_card__should_add_card_to_player_repo_and_return_message(self):
        controller = Controller()
        player_name = "beginner"
        player_type = "Beginner"
        card_name = "card"
        card_type = "Magic"
        controller.add_player(player_type, player_name)
        controller.add_card(card_type, card_name)
        result = controller.add_player_card("beginner", "card")
        self.assertIn(card_name, controller.player_repository.players[0].card_repository.cards[0].name)
        self.assertEqual(f"Successfully added card: {card_name} to user: {player_name}", result)

    def test_attack__when_attacker_and_enemy__should_fight_and_return_message(self):
        controller = Controller()
        attacker_name = "beginner"
        attacker_type = "Beginner"
        enemy_name = "advanced"
        enemy_type = "Advanced"
        magic_card_name = "magic_card"
        magic_card_type = "Magic"
        trap_card_name = "trap_card"
        trap_card_type = "Trap"
        controller.add_player(attacker_type, attacker_name)
        controller.add_player(enemy_type, enemy_name)
        controller.add_card(magic_card_type, magic_card_name)
        controller.add_card(trap_card_type, trap_card_name)
        controller.add_player_card(attacker_name, magic_card_name)
        controller.add_player_card(enemy_name, trap_card_name)
        result = controller.fight("beginner", "advanced")
        self.assertEqual(f"Attack user health 170 - Enemy user health 100", result)

    def test_report__when_all_correct__should_return_result(self):
        controller = Controller()
        attacker_name = "beginner"
        attacker_type = "Beginner"
        enemy_name = "advanced"
        enemy_type = "Advanced"
        magic_card_name = "magic_card"
        magic_card_type = "Magic"
        trap_card_name = "trap_card"
        trap_card_type = "Trap"
        controller.add_player(attacker_type, attacker_name)
        controller.add_player(enemy_type, enemy_name)
        controller.add_card(magic_card_type, magic_card_name)
        controller.add_card(trap_card_type, trap_card_name)
        controller.add_player_card(attacker_name, magic_card_name)
        controller.add_player_card(enemy_name, trap_card_name)
        result = "Username: beginner - Health: 50 - Cards 1\n" \
                 "### Card: magic_card - Damage: 5\n" \
                 "Username: advanced - Health: 250 - Cards 1\n" \
                 "### Card: trap_card - Damage: 120\n"
        self.assertEqual(result, controller.report())


if __name__ == "__main__":
    unittest.main()
