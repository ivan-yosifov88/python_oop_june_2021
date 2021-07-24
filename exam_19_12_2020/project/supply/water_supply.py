from project.supply.supply import Supply


class WaterSupply(Supply):
    WATER_SUPPLY = 40

    def __init__(self):
        Supply.__init__(self, WaterSupply.WATER_SUPPLY)


