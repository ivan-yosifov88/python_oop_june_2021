import unittest

from project.figure.figure import Figure


class TestFigure(unittest.TestCase):
    def test_init__when_try_to_init__should_raise(self):
        expect_message = '''Can't instantiate abstract class Figure with abstract methods calculate_area, " \
                         "calculate_circumference'''
        with self.assertRaises(TypeError):
            figure = Figure("Test", 5)
        self.assertTrue(TypeError)

    def test_str__when_all_correct__should_return_message(self):
        pass

