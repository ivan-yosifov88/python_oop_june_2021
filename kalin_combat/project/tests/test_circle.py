import unittest

from project.figure.circle import Circle


class TestCircle(unittest.TestCase):
    def test_init__when_all_valid__should_set(self):
        circle = Circle("test", 10)
        self.assertEqual("test", circle.name)
        self.assertEqual(10, circle.args[0])

    def test_calculate_area__when_radius__should_return_result(self):
        circle = Circle("test", 10)
        self.assertEqual(314.15926535897932384626433832795, circle.calculate_area())

    def test_calculate_circumference(self):
        circle = Circle("test", 10)
        self.assertEqual(62.83185307179586476925286766559, circle.calculate_circumference())

