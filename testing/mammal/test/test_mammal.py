import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def test_init_when_all_attributes_are_correct(self):
        name = "Test name"
        mammal_type = "test type"
        sound = "test sound"
        mammal = Mammal(name, mammal_type, sound)
        self.assertEqual(name, mammal.name)
        self.assertEqual(mammal_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound__should_to_return_correct_string(self):
        name = "Test name"
        mammal_type = "test type"
        sound = "test sound"
        mammal = Mammal(name, mammal_type, sound)
        expect = f"{name} makes {sound}"
        self.assertEqual(expect, mammal.make_sound())

    def test_get_kingdom__should_return_protected_attribute_animals(self):
        name = "Test name"
        mammal_type = "test type"
        sound = "test sound"
        mammal = Mammal(name, mammal_type, sound)
        kingdom = "animals"
        self.assertEqual(kingdom, mammal.get_kingdom())

    def test_get_info__should_return_correct_string(self):
        name = "Test name"
        mammal_type = "test type"
        sound = "test sound"
        mammal = Mammal(name, mammal_type, sound)
        expect = f"{name} is of type {mammal_type}"
        self.assertEqual(expect, mammal.info())


if __name__ == "__main__":
    unittest.main()
