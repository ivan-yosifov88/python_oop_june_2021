from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren (Room):
    members = 2
    default_room_cost = 30
    appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
    appliances_for_one_child = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, self.members + len(children))
        self.room_cost = self.default_room_cost
        self.children = list(children)
        self.appliances.extend(self.get_child_appliances(self.appliances_for_one_child, len(self.children)))
        self.calculate_expenses(self.appliances, self.children)

    @staticmethod
    def get_child_appliances(ll, number_of_children):
        children_appliances = []
        for _ in range(number_of_children):
            children_appliances.extend(ll)
        return children_appliances
