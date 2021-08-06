from project.bunker import Bunker
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor

food_supply = FoodSupply()
water_supply = WaterSupply()
painkiller = Painkiller()
salve = Salve()
# survivor = Survivor("Gosho", 30)
survivor = Survivor("Gosho", 30)
bunker = Bunker()

bunker.add_survivor(survivor)
bunker.add_supply(water_supply)
bunker.add_supply(food_supply)
bunker.add_medicine(painkiller)
bunker.add_medicine(salve)
bunker.heal(survivor, "Painkiller")
# bunker.heal(survivor, painkiller)
bunker.heal(survivor, "Salve")
bunker.sustain(survivor, "Water_supply")
bunker.sustain(survivor, "Food_supply")
bunker.next_day()