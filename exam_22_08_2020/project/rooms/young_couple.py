from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    members = 2
    default_room_cost = 20
    appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, self.members)
        self.room_cost = self.default_room_cost
        self.calculate_expenses(self.appliances)
