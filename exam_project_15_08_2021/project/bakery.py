from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    _possible_food_types = {"Bread": Bread, "Cake": Cake}
    _possible_drink_types = {"Tea": Tea, "Water": Water}
    _possible_table_types = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.table_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @staticmethod
    def _get_object_by_name(name, ll_of_obj):
        return [obj for obj in ll_of_obj if obj.name == name]

    @staticmethod
    def _get_object_by_table_number(number, ll_of_obj):
        return [obj for obj in ll_of_obj if obj.table_number == number]

    def add_food(self, food_type, name, price):
        if food_type not in self._possible_food_types:
            return
        filtered_foods = self._get_object_by_name(name, self.food_menu)
        if filtered_foods:
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = self._possible_food_types[food_type](name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if drink_type not in self._possible_drink_types:
            return
        filtered_drinks = self._get_object_by_name(name, self.drinks_menu)
        if filtered_drinks:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self._possible_drink_types[drink_type](name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_type not in self._possible_table_types:
            return
        filtered_tables = self._get_object_by_table_number(table_number, self.table_repository)
        if filtered_tables:
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self._possible_table_types[table_type](table_number, capacity)
        self.table_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.table_repository:
            if table.is_reserved or not table.capacity <= number_of_people:
                return f"No available table for {number_of_people} people"

            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number, *food_names):
        filtered_table = self._get_object_by_table_number(table_number, self.table_repository)
        if not filtered_table:
            return f"Could not find table {table_number}"
        current_table = filtered_table[0]
        ordered_food_not_in_menu = []
        for food in food_names:
            current_food = self._get_object_by_name(food, self.food_menu)
            if not current_food:
                ordered_food_not_in_menu.append(food)
            else:
                current_table.order_food(current_food[0])
        result_orders = f"Table {table_number} ordered:\n"
        result_orders += '\n'.join([str(element) for element in current_table.food_orders])
        if ordered_food_not_in_menu:
            result_orders += f"\n{self.name} does not have in the menu:\n"
            result_orders += '\n'.join(ordered_food_not_in_menu)

        return result_orders

    def order_drink(self, table_number, *drinks_names):
        filtered_table = self._get_object_by_table_number(table_number, self.table_repository)
        if not filtered_table:
            return f"Could not find table {table_number}"
        current_table = filtered_table[0]
        ordered_drink_not_in_menu = []
        for drink in drinks_names:
            current_drink = self._get_object_by_name(drink, self.drinks_menu)
            if not current_drink :
                ordered_drink_not_in_menu.append(drink)
            else:
                current_table.order_drink(current_drink[0])
        result_orders = f"Table {table_number} ordered:\n"
        result_orders += '\n'.join([str(element) for element in current_table.food_orders])
        if ordered_drink_not_in_menu:
            result_orders += f"\n{self.name} does not have in the menu:\n"
            result_orders += '\n'.join(ordered_drink_not_in_menu)

        return result_orders

    def leave_table(self, table_number):
        filtered_table = self._get_object_by_table_number(table_number, self.table_repository)
        if not filtered_table:
            return
        current_table = filtered_table[0]
        table_bill = current_table.get_bill()
        self.total_income += table_bill
        current_table.clear()
        return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.table_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())
        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"