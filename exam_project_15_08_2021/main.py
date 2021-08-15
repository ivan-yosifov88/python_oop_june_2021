from project.bakery import Bakery

bakery = Bakery("Test")

print(bakery.add_food("Bread", "bread", 10))
print(bakery.add_food("Bread", "bread_2", 10))
print(bakery.add_food("Cake", "cake", 20))
print(bakery.add_food("Cake", "cake_2", 20))
print(bakery.add_drink("Tea", "tea", 10, "T"))
print(bakery.add_drink("Tea", "tea_2", 10, "T"))
print(bakery.add_drink("Water", "water", 5, "W"))
print(bakery.add_drink("Water", "water_2", 5, "W"))



print(bakery.add_table("InsideTable", 10, 10))
print(bakery.add_table("OutsideTable", 55, 4))

print(bakery.reserve_table(10))
print(bakery.reserve_table(11))

print(bakery.order_food(10, "Garash", "Cherveno_Kadife", "bread", "bread_2"))
print(bakery.order_drink(10, "Vodka", "Wine", "tea", "tea_2"))

print(bakery.leave_table(10))

print(bakery.get_free_tables_info())
print(bakery.get_total_income())