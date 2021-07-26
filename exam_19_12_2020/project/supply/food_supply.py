from project.supply.supply import Supply


class FoodSupply(Supply):
    value = 20

    def __init__(self):
        super().__init__(self.value)

