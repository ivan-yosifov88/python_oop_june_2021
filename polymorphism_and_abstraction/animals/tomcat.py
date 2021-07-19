from animals.cat import Cat


class Tomcat(Cat):
    MAKE_SOUND = "Hiss"
    GENDER = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.GENDER)

    def make_sound(self):
        return Tomcat.MAKE_SOUND