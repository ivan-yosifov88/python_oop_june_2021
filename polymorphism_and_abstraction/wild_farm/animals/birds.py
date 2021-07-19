from wild_farm.animals.animal import Bird


class Owl(Bird):
    WEIGHT_INCREASE = 0.25
    SOUND = "Hoot Hoot"
    FOOD_EAT = ['Meat']

    def make_sound(self):
        return Owl.SOUND

    def feed(self, food):
        if food.__class__.__name__ not in Owl.FOOD_EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Owl.WEIGHT_INCREASE
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_INCREASE = 0.35
    SOUND = "Cluck"
    FOOD_EAT = ['Meat', 'Vegetable', 'Fruit', 'Seed']

    def make_sound(self):
        return Hen.SOUND

    def feed(self, food):
        if food.__class__.__name__ not in Hen.FOOD_EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Hen.WEIGHT_INCREASE
        self.food_eaten += food.quantity





