from wild_farm.animals.animal import Mammal


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.1
    SOUND = "Squeak"
    FOOD_EAT = ['Vegetable', 'Fruit']

    def make_sound(self):
        return Mouse.SOUND

    def feed(self, food):
        if food.__class__.__name__ not in Mouse.FOOD_EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Mouse.WEIGHT_INCREASE
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_INCREASE = 0.4
    SOUND = "Woof!"
    FOOD_EAT = ['Meat']

    def make_sound(self):
        return Dog.SOUND

    def feed(self, food):
        if food.__class__.__name__ not in Dog.FOOD_EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Dog.WEIGHT_INCREASE
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_INCREASE = 1
    SOUND = "ROAR!!!"
    FOOD_EAT = ['Meat']

    def make_sound(self):
        return Tiger.SOUND

    def feed(self, food):
        if food.__class__.__name__ not in Tiger.FOOD_EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Tiger.WEIGHT_INCREASE
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_INCREASE = 0.3
    SOUND = "Meow"
    FOOD_EAT = ['Meat', 'Vegetable']

    def make_sound(self):
        return Cat.SOUND

    def feed(self, food):
        if food.__class__.__name__ not in Cat.FOOD_EAT:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Cat.WEIGHT_INCREASE
        self.food_eaten += food.quantity
