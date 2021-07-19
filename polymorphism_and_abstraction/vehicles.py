from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    FUEL_CONSUMPTION_INCREASE_IN_SUMMER = 0.9

    def drive(self, distance):
        fuel_spent = distance * (self.fuel_consumption + Car.FUEL_CONSUMPTION_INCREASE_IN_SUMMER)
        if fuel_spent <= self.fuel_quantity:
            self.fuel_quantity -= fuel_spent

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FUEL_CONSUMPTION_INCREASE_IN_SUMMER = 1.6
    TRUCK_FUEL_TANK_LOOSES = 0.95

    def drive(self, distance):
        fuel_spent = distance * (self.fuel_consumption + Truck.FUEL_CONSUMPTION_INCREASE_IN_SUMMER)
        if fuel_spent <= self.fuel_quantity:
            self.fuel_quantity -= fuel_spent

    def refuel(self, fuel):
        fuel_to_add = fuel * Truck.TRUCK_FUEL_TANK_LOOSES
        self.fuel_quantity += fuel_to_add


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
