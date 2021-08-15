from project.drink.drink import Drink


class Water(Drink):
    _cost = 1.50

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, self._cost, brand)