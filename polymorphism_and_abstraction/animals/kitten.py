from animals.cat import Cat


class Kitten(Cat):
    MAKE_SOUND = "Meow"
    GENDER = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.GENDER)

    def make_sound(self):
        return Kitten.MAKE_SOUND