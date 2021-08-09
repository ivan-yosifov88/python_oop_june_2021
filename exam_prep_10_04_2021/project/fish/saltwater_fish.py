from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    DEFAULT_SIZE_TO_INCREASE = 3
    _initial_size = 5

    def __init__(self, name, species, price):
        super().__init__(name, species, self._initial_size, price)

    def eat(self):
        self.size += self.DEFAULT_SIZE_TO_INCREASE
