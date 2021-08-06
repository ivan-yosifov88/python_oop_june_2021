import unittest

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("Factory", 10)
        self.paint_factory.ingredients = {}
        self.paint_factory.valid_ingredients = ["white", "yellow", "blue", "green", "red"]

    def test_init_paint_factory(self):
        self.assertEqual(self.paint_factory.name, "Factory")
        self.assertEqual(self.paint_factory.capacity, 10)
        self.assertEqual(self.paint_factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        self.assertEqual(self.paint_factory.ingredients, {})

    def test_add_ingredient__when_ingredient_type_not_in_valid_ingredients__should_raise_type_error(self):
        ingredient_type = "test_ingredient"
        with self.assertRaises(TypeError) as message:
            self.paint_factory.add_ingredient(ingredient_type, 10)
        self.assertEqual(f"Ingredient of type {ingredient_type} not allowed in PaintFactory", str(message.exception))

    def test_add_ingredient__when_capacity_is_less_then_quantity__should_raise_value_error(self):
        quantity = 11
        valid_ingredient = "blue"
        with self.assertRaises(ValueError) as message:
            self.paint_factory.add_ingredient(valid_ingredient, quantity)
        self.assertEqual("Not enough space in factory", str(message.exception))

    def test_add_ingredient__when_ingredient_type_is_not_in_ingredients_dict__should_create_new_key_with_value_zero(self):
        ingredient_type = "blue"
        quantity = 0
        result_dict = {ingredient_type: 0}
        self.paint_factory.add_ingredient(ingredient_type, quantity)
        result = self.paint_factory.ingredients
        self.assertEqual(result, result_dict)

    def test_add_ingredient__when_input_is_valid__should_add_quantity_in_ingredient_dict(self):
        ingredient_type = "blue"
        initialise_quantity = 0
        quantity = 5
        result_dict = {ingredient_type: quantity}
        # self.paint_factory.add_ingredient(ingredient_type, initialise_quantity)
        self.paint_factory.add_ingredient(ingredient_type, quantity)
        result = self.paint_factory.ingredients
        self.assertEqual(result, result_dict)

    def test_remove_ingredient__when_ingredient_type_not_in_ingredients__should_raise_key_error(self):
        initialise_ingredient_type = "blue"
        initialise_quantity = 2
        ingredient_type = "Invalid ingredient"
        expected_message = "No such ingredient in the factory"
        self.paint_factory.add_ingredient(initialise_ingredient_type, initialise_quantity)
        with self.assertRaises(KeyError) as message:
            self.paint_factory.remove_ingredient(ingredient_type, initialise_quantity)
        mess = str(message.exception).strip("''")
        self.assertEqual(expected_message, mess)

    def test_remove_ingredient__when_quantity_type_is_greater_than_ingredient_quantity__should_raise_value_error(self):
        initialise_ingredient_type = "blue"
        initialise_quantity = 5
        quantity = 7
        self.paint_factory.ingredients = {initialise_ingredient_type: initialise_quantity}
        with self.assertRaises(ValueError) as message:
            self.paint_factory.remove_ingredient(initialise_ingredient_type, quantity)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(message.exception))

    def test_can_add__when_capacity_is_greater_or_equal_to_values__should_return_True(self):
        ingredient_type = "blue"
        quantity = 5
        value_to_add = 4
        self.paint_factory.add_ingredient(ingredient_type, quantity)
        self.assertEqual(self.paint_factory.can_add(value_to_add), True)

    def test_can_add__when_capacity_is_less_to_values__should_return_False(self):
        ingredient_type = "blue"
        quantity = 5
        value_to_add = 6
        self.paint_factory.add_ingredient(ingredient_type, quantity)
        self.assertEqual(self.paint_factory.can_add(value_to_add), False)

    def test_property_product__should_return_ingredients(self):
        initialise_ingredient_type = "blue"
        initialise_quantity = 5
        self.paint_factory.add_ingredient(initialise_ingredient_type, initialise_quantity)

        self.assertEqual(self.paint_factory.products, self.paint_factory.ingredients)

    def test_repr__with_value__should_repr_correct(self):
        initialise_ingredient_type = "blue"
        initialise_quantity = 2
        self.paint_factory.add_ingredient(initialise_ingredient_type, initialise_quantity)
        result = f"Factory name: {self.paint_factory.name} with capacity {self.paint_factory.capacity}.\n" \
                 f"{initialise_ingredient_type}: {initialise_quantity}\n"
        self.assertEqual(result, repr(self.paint_factory))


if __name__ == '__main__':
    unittest.main()
