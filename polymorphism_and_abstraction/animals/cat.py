from animals.animal import Animal


class Cat(Animal):
    MAKE_SOUND = "Meow meow!"

    def make_sound(self):
        return Cat.MAKE_SOUND