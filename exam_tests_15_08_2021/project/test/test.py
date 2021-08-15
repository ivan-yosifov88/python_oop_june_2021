import unittest

from project.pet_shop import PetShop


class TestPetShop(unittest.TestCase):
    def setUp(self):
        self.test_pet = PetShop("Test")

    def test_init__when_all_correct__should_set(self):
        self.assertEqual("Test", self.test_pet.name)
        self.assertEqual({}, self.test_pet.food)
        self.assertEqual([], self.test_pet.pets)

    def test_add_food__when_quantity_is_0__should_raise(self):
        expected_message = 'Quantity cannot be equal to or less than 0'
        with self.assertRaises(ValueError) as message:
            self.test_pet.add_food("Test", 0)
        self.assertEqual(expected_message, str(message.exception))

    def test_add_food__when_quantity_is_less_than_0__should_raise(self):
        expected_message = 'Quantity cannot be equal to or less than 0'
        with self.assertRaises(ValueError) as message:
            self.test_pet.add_food("Test", -1)
        self.assertEqual(expected_message, str(message.exception))

    def test_add_food__when_name_not_in_food__should_add_and_return_message(self):
        quantity = 2
        name = "Testov"
        expected_message = f"Successfully added {quantity:.2f} grams of {name}."
        expected_result = self.test_pet.add_food(name, quantity)
        self.assertEqual(expected_result, expected_message)
        self.assertEqual({name:quantity}, self.test_pet.food)

    def test_add_pet_when_pet_in_pets__should_raise(self):
        expected_message = "Cannot add a pet with the same name"
        with self.assertRaises(Exception) as message:
            self.test_pet.pets = ["Test"]
            self.test_pet.add_pet("Test")
        self.assertEqual(expected_message, str(message.exception))

    def test_add_pet_when_pet_not_in_pets__should_append(self):
        name = "Test"
        expected_message = f"Successfully added {name}."
        result = self.test_pet.add_pet(name)
        self.assertEqual(expected_message, result)
        self.assertEqual([name], self.test_pet.pets)

    def test_feed_pet__when_pet_name_not_in_pets__should_raise(self):
        food_name = "test_food"
        name = "Test"
        expected_message = "Please insert a valid pet name"
        with self.assertRaises(Exception) as message:
            self.test_pet.feed_pet(name, food_name)
        self.assertEqual(expected_message, str(message.exception))
        with self.assertRaises(Exception) as message:
            self.test_pet.pets = ["Testov"]
            self.test_pet.feed_pet(name, food_name)
        self.assertEqual(expected_message, str(message.exception))

    def test_feed_pet__when_food_name_not_in_food__should_return_message(self):
        food_name = "test_food"
        name = "Test"
        expected_message = f'You do not have {food_name}'
        self.test_pet.pets = [name]
        result = self.test_pet.feed_pet(food_name, name)
        self.assertEqual(expected_message, result)

    def test_feed_pet__when_food_quantity_is_less_than_100__should_return_message(self):
        food_name = "test_food"
        food_quantity = 10
        name = "Test"
        expected_message = "Adding food..."
        self.test_pet.pets = [name]
        self.test_pet.food = {food_name:food_quantity}
        result = self.test_pet.feed_pet(food_name, name)
        self.assertEqual(expected_message, result)
        self.assertEqual(1010, self.test_pet.food[food_name])

    def test_feed_pet_when_all_correct__should_feed_animal_and_return_message(self):
        food_name = "test_food"
        food_quantity = 150
        name = "Test"
        expected_message = f"{name} was successfully fed"
        self.test_pet.pets = [name]
        self.test_pet.food = {food_name: food_quantity}
        result = self.test_pet.feed_pet(food_name, name)
        self.assertEqual(expected_message, result)
        self.assertEqual(50, self.test_pet.food[food_name])

    def test_repr__when_correct__should_return_message(self):
        name = "Test"
        self.test_pet.pets = [name]
        expected_message = f'Shop {name}:\n'f'Pets: {name}'
        result = self.test_pet.__repr__()
        self.assertEqual(expected_message, result)




if __name__ == "__main__":
    unittest.main()
