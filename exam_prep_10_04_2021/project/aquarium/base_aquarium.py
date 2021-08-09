from abc import ABC,abstractmethod


class BaseAquarium(ABC):
    _possible_fish_types = ["FreshwaterFish", "SaltwaterFish"]

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def __str__(self):
        fish_names = ' '.join([fish.name for fish in self.fish]) if self.fish else "none"
        return f"{self.name}:\n" \
               f"Fish: {fish_names}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish):
        if not self.capacity > len(self.fish):
            return "Not enough capacity."
        if fish.__class__.__name__ not in self._possible_fish_types:
            return

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if self.fish and fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat()for fish in self.fish]

    @property
    def sum_of_all_fish(self):
        return sum([fish.price for fish in self.fish])

    @property
    def sum_of_all_decorations_price(self):
        return sum([decorations.price for decorations in self.decorations])





