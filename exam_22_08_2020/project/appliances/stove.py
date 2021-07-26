from project.appliances.appliance import Appliance


class Stove(Appliance):
    appliance_cost = 0.7

    def __init__(self):
        super().__init__(self.appliance_cost)
