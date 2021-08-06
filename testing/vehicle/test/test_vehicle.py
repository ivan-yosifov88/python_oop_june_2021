import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def test_class_attributes__should_default_fuel_consumption_to_be_set(self):
        default_fuel_consumption = 1.25
        self.assertEqual(default_fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init_method_should_set_attributes(self):
        fuel = 10
        horse_power = 100
        test_vehicle = Vehicle(fuel, horse_power)
        capacity = 10
        fuel_consumption = 1.25
        self.assertEqual(fuel, test_vehicle.fuel)
        self.assertEqual(horse_power, test_vehicle.horse_power)
        self.assertEqual(capacity, test_vehicle.capacity)
        self.assertEqual(fuel_consumption, test_vehicle.fuel_consumption)

    def test_drive__if_fuel_is_less_then_needed_should_raise_Exeption(self):
        fuel = 10
        horse_power = 100
        fuel_consumption = 1.25
        kilometers = 9
        test_vehicle = Vehicle(fuel, horse_power)
        with self.assertRaises(Exception) as message:
            test_vehicle.drive(kilometers)
        self.assertEqual("Not enough fuel", str(message.exception))

    def test_drive__if_fuel_is_greater_then_needed_should_reduce_fuel(self):
        fuel = 112.5
        horse_power = 100
        fuel_consumption = 1.25
        kilometers = 10
        test_vehicle = Vehicle(fuel, horse_power)
        test_vehicle.drive(kilometers)
        expect = fuel - (kilometers * fuel_consumption)
        self.assertEqual(expect, test_vehicle.fuel)

    def test_drive__if_fuel_is_equal_then_needed_should_reduce_fuel(self):
        fuel = 12.5
        horse_power = 100
        fuel_consumption = 1.25
        kilometers = 10
        test_vehicle = Vehicle(fuel, horse_power)
        test_vehicle.drive(kilometers)
        expect = fuel - (kilometers * fuel_consumption)
        self.assertEqual(expect, test_vehicle.fuel)

    def test_refuel__when_fuel_with_added_fuel_is_greater_then_capacity__should_raise_Exception(self):
        fuel = 10
        horse_power = 100
        fuel_to_add = 10
        test_vehicle = Vehicle(fuel, horse_power)
        with self.assertRaises(Exception) as message:
            test_vehicle.refuel(fuel_to_add)
        self.assertEqual("Too much fuel", str(message.exception))

    def test_refuel__when_fuel_with_added_fuel_is_less_then_capacity__should_add_fuel(self):
        fuel = 10
        horse_power = 100
        fuel_to_add = 9
        capacity = 20
        test_vehicle = Vehicle(fuel, horse_power)
        test_vehicle.capacity = capacity
        expect = fuel + fuel_to_add
        test_vehicle.refuel(fuel_to_add)
        self.assertEqual(expect, test_vehicle.fuel)

    def test_str_when_correct__should_return_string(self):
        fuel = 10
        horse_power = 100
        fuel_consumption = 1.25
        test_vehicle = Vehicle(fuel, horse_power)
        test_vehicle.fuel_consumption = fuel_consumption
        expect = f"The vehicle has {horse_power} " \
               f"horse power with {fuel} fuel left and {fuel_consumption} fuel consumption"
        self.assertEqual(expect, test_vehicle.__str__())


if __name__ == "__main__":
    unittest.main()