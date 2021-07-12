class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        if self.water_requirements <= quantity:
            self.is_happy = True

    def status(self):
        return f"{self.name} is happy" if self.is_happy else f"{self.name} is not happy"