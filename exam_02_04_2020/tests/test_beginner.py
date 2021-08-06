import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def test_init_method__when_all_correct__should_set(self):
        beginner = Beginner("Test")
        self.assertEqual("Test", beginner.username)
        self.assertEqual(50, beginner.initial_points)

    def test_username__when_empty_should_raise_ValueError(self):
        with self.assertRaises(ValueError) as message:
            beginner = Beginner("")
        self.assertEqual("Player's username cannot be an empty string.", str(message.exception))

    def test_health__when_value_is_less_than_0__should_raise_ValueError(self):
        beginner = Beginner("Test")
        with self.assertRaises(ValueError) as message:
            beginner.health = -1
        self.assertEqual("Player's health bonus cannot be less than zero.", str(message.exception))

    def test_take_damage__when_points_are_less_than_0__should_raise_ValueError(self):
        damage_points = -1
        beginner = Beginner("Test")
        with self.assertRaises(ValueError) as message:
            beginner.take_damage(damage_points)
        self.assertEqual("Damage points cannot be less than zero.", str(message.exception))

    def test_take_damage__when_points_are_greater_than_0__should_decrease_health(self):
        damage_points = 5
        beginner = Beginner("Test")
        beginner.take_damage(damage_points)
        self.assertEqual(45, beginner.health)

    def test_is_dead_property__when_health_is_greater_than_zero__should_return_False(self):
        beginner = Beginner("Test")
        damage_points = 5
        beginner.take_damage(damage_points)
        self.assertFalse(beginner.is_dead)


if __name__ == "__main__":
    unittest.main()