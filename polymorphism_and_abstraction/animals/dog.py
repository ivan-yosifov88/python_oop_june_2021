from animals.animal import Animal


class Dog(Animal):
    MAKE_SOUND = "Woof!"

    def make_sound(self):
        return Dog.MAKE_SOUND