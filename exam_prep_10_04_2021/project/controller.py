from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    _possible_aquarium_types = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
    _possible_decoration_types = {"Ornament": Ornament, "Plant": Plant}
    _possible_fish_types = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}
    _possible_fish_aquarium_type = {"FreshwaterFish":"FreshwaterAquarium", "SaltwaterFish": "SaltwaterAquarium"}

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in self._possible_aquarium_types:
            return "Invalid aquarium type."

        aquarium = self._possible_aquarium_types[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in self._possible_decoration_types:
            return "Invalid decoration type."

        decoration = self._possible_decoration_types[decoration_type]()
        self.decorations_repository.decorations.append(decoration)
        return f"Successfully added {decoration_type}."

    @staticmethod
    def _get_aquarium(name, list_of_aquariums):
        return [aquarium for aquarium in list_of_aquariums if name == aquarium.name]

    def insert_decoration(self, aquarium_name, decoration_type):
        filter_decoration = self.decorations_repository.find_by_type(decoration_type)
        filter_aquariums = self._get_aquarium(aquarium_name, self.aquariums)
        if filter_decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        if not filter_aquariums:
            return
        aquarium = filter_aquariums[0]
        aquarium.add_decoration(filter_decoration)
        self.decorations_repository.remove(filter_decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in self._possible_fish_types:
            return f"There isn't a fish of type {fish_type}."
        fish = self._possible_fish_types[fish_type](fish_name, fish_species, price)
        filter_aquariums = self._get_aquarium(aquarium_name, self.aquariums)
        if not filter_aquariums:
            return
        aquarium = filter_aquariums[0]
        if not self._possible_fish_aquarium_type[fish_type] == aquarium.__class__.__name__:
            return "Water not suitable."
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        filter_aquarium = self._get_aquarium(aquarium_name, self.aquariums)
        if not filter_aquarium:
            return
        aquarium = filter_aquarium[0]
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        filter_aquarium = self._get_aquarium(aquarium_name, self.aquariums)
        if not filter_aquarium:
            return
        aquarium = filter_aquarium[0]
        return aquarium.sum_of_all_decorations_price + aquarium.sum_of_all_fish

    def report(self):
        for aquarium in self.aquariums:
            print(aquarium)

