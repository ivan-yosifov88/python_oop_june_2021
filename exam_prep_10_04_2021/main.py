from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.controller import Controller

plant = Plant()
ornament = Ornament()
test_ornament = Ornament()
repo = DecorationRepository()

# freshwater_aquarium = FreshwaterAquarium("Fresh")
# freshwater_aquarium_2 = FreshwaterAquarium("Fresh2")
# saltwater_aquarium = SaltwaterAquarium("Salt")
# saltwater_aquarium_2 = SaltwaterAquarium("Salt2")

controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "Fresh"))
print(controller.add_aquarium("SaltwaterAquarium", "Salt"))
print(controller.add_aquarium("FreshwaterAquarium", "Fresh2"))
print(controller.add_aquarium("SaltwaterAquarium", "Salt2"))
print(controller.add_aquarium("WRONG", "Salt2"))

print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("WRONG"))

print(controller.insert_decoration("Fresh", "Wrong"))
print(controller.insert_decoration("Fresh", "Plant"))

print(controller.add_fish("Fresh", "FreshwaterFish", "FRESH_FISH", "SPECIES", 10))
print(controller.add_fish("Fresh2", "FreshwaterFish", "FRESH_FISH2", "SPECIES", 10))
print(controller.add_fish("Salt", "SaltwaterFish", "SALT_FISH", "SPECIES", 10))
print(controller.add_fish("Salt2", "SaltwaterFish", "FRESH_FISH", "SPECIES", 10))
print(controller.add_fish("Salt2", "WRONG", "FRESH_FISH", "SPECIES", 10))
print(controller.add_fish("Fresh", "SaltwaterFish", "FRESH_FISH", "SPECIES", 10))

print(controller.feed_fish("Fresh"))

print(controller.calculate_value("Fresh"))

controller.report()



