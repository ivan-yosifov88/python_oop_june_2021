from project.supply.supply import Supply


class WaterSupply(Supply):
    value = 40

    def __init__(self):
        super().__init__(self.value)


