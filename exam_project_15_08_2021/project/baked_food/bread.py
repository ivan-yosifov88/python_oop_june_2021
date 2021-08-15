from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    _portion = 200

    def __init__(self, name, price):
        super().__init__(name, self._portion, price)