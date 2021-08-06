import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        username = "User"
        level = 1
        health = 100
        damage = 100
        self.hero = Hero(username, level, health, damage)

    def test_init_when_all_correct_should_set(self):
        username = "User"
        level = 1
        health = 100
        damage = 100
        self.assertEqual(username, self.hero.username)
        self.assertEqual(level, self.hero.level)
        self.assertEqual(health, self.hero.health)
        self.assertEqual(damage, self.hero.damage)

    def test_battle__when_user_and_and_enemy_have_the_same_names__should_raise_Exception(self):
        enemy_username = "User"
        level = 1
        health = 100
        damage = 100
        enemy = Hero(enemy_username, level, health, damage)
        expected_message = "You cannot fight yourself"
        with self.assertRaises(Exception) as message:
            self.hero.battle(enemy)
        self.assertEqual(expected_message, str(message.exception))

    def test_battle__when_hero_health_becomes_less_than_zero__should_raise_ValueError(self):
        enemy_username = "Enemy"
        level = 1
        health = 100
        damage = 100
        enemy = Hero(enemy_username, level, health, damage)
        self.hero.health = -1
        expected_message = "Your health is lower than or equal to 0. You need to rest"
        with self.assertRaises(ValueError) as message:
            self.hero.battle(enemy)
        self.assertEqual(expected_message, str(message.exception))

    def test_battle__when_enemy_health_is_less_than_zero__should_raise_ValueError(self):
        enemy_username = "Enemy"
        level = 1
        health = -1
        damage = 100
        enemy = Hero(enemy_username, level, health, damage)
        expected_message = f"You cannot fight {enemy_username}. He needs to rest"
        with self.assertRaises(ValueError) as message:
            self.hero.battle(enemy)
        self.assertEqual(expected_message, str(message.exception))

    def test_battle__when_battle_and_hero_and_enemy_health_are_less_then_zero__should_return_draw(self):
        enemy_username = "Enemy"
        enemy_level = 1
        enemy_health = 100
        enemy_damage = 101
        enemy = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)
        self.hero.damage = 101
        expected_message = "Draw"
        self.assertEqual(expected_message, self.hero.battle(enemy))
        self.assertEqual(-1, self.hero.health)
        self.assertEqual(-1, enemy.health)

    def test_battle__when_battle_and_hero_and_enemy_health_are_equal_to_zero__should_return_draw(self):
        enemy_username = "Enemy"
        enemy_level = 1
        enemy_health = 100
        enemy_damage = 100
        enemy = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)
        self.hero.damage = 100
        expected_message = "Draw"
        self.assertEqual(expected_message, self.hero.battle(enemy))
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, enemy.health)

    def test_battle__when_battle_only_enemy_health_is_less_then_zero__should_return_win(self):
        enemy_username = "Enemy"
        enemy_level = 1
        enemy_health = 100
        enemy_damage = 99
        enemy = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)
        self.hero.damage = 101
        expected_message = "You win"
        self.assertEqual(expected_message, self.hero.battle(enemy))
        self.assertEqual(2, self.hero.level)
        self.assertEqual(6, self.hero.health)
        self.assertEqual(106, self.hero.damage)

    def test_battle__when_battle_only_enemy_health_is_greater_then_zero__should_return_lose(self):
        enemy_username = "Enemy"
        enemy_level = 1
        enemy_health = 101
        enemy_damage = 100
        enemy = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)
        expected_message = "You lose"
        self.assertEqual(expected_message, self.hero.battle(enemy))
        self.assertEqual(2, enemy.level)
        self.assertEqual(6, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_str_when_correct__should_return_string(self):
        username = "User"
        level = 1
        health = 100
        damage = 100
        expected_message = f"Hero {username}: {level} lvl\n" \
               f"Health: {health}\n" \
               f"Damage: {damage}\n"

        self.assertEqual(expected_message, self.hero.__str__())

if __name__ == "__main__":
    unittest.TestCase