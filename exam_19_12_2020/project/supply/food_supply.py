from project.supply.supply import Supply


class FoodSupply(Supply):
    FOOD_SUPPLY = 20

    def __init__(self):
        Supply.__init__(self, FoodSupply.FOOD_SUPPLY)

