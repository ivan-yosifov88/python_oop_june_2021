from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    members = 1
    default_room_cost = 10
    appliances = [TV()]

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, self.members)
        self.room_cost = self.default_room_cost
        self.calculate_expenses(self.appliances)



