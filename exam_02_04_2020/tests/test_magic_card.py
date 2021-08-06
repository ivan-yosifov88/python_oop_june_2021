import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def test_init__when_all_correct__should_set(self):
        card = MagicCard("Test")
        self.assertEqual("Test", card.name)
        self.assertEqual(5, card.damage_points)
        self.assertEqual(80, card.health_points)

    def test_name__when_name_is_empty__should_raise_ValueError(self):
        with self.assertRaises(ValueError) as message:
            card = MagicCard("")
        self.assertEqual("Card's name cannot be an empty string.", str(message.exception))

    def test_damage_points__when_damage_points_are_less_then_0__should_raise_ValueError(self):
        card = MagicCard("Test")
        with self.assertRaises(ValueError) as message:
            card.damage_points = -1
        self.assertEqual("Card's damage points cannot be less than zero.", str(message.exception))

    def test_health_points__when_health_points_are_less_then_0__should_raise_ValueError(self):
        card = MagicCard("Test")
        with self.assertRaises(ValueError) as message:
            card.health_points = -1
        self.assertEqual("Card's HP cannot be less than zero.", str(message.exception))


if __name__ == "__main__":
    unittest.main()