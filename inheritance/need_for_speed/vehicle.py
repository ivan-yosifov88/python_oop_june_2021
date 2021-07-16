class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        current_fuel_for_kilometers = self.fuel_consumption * kilometers
        if current_fuel_for_kilometers <= self.fuel:
            self.fuel -= current_fuel_for_kilometers
