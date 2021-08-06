class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        rooms_to_remove = []
        for room in self.rooms:
            current_room_expenses = room.expenses + room.room_cost
            if not current_room_expenses <= room.budget:
                rooms_to_remove.append(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                continue
            room.budget -= current_room_expenses
            result.append(f"{room.family_name} paid {current_room_expenses:.2f}$ and have {room.budget:.2f}$ left.")
        for current_room in rooms_to_remove:
            self.rooms.remove(current_room)
        return '\n'.join(result)

    def status(self):
        all_people_in_the_hotel = sum(r.members_count for r in self.rooms)
        result = f"Total population: {all_people_in_the_hotel}\n"

        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members." \
                      f" Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if type(room).__name__ == "YoungCoupleWithChildren" and room.children:
                for i in range(len(room.children)):
                    total_child_expenses = 0
                    current_child = room.children[i].get_monthly_expense()
                    total_child_expenses += current_child
                    result += f"--- Child {i + 1} monthly cost: {current_child:.2f}$\n"
                    room.expenses -= total_child_expenses
            result += f"--- Appliances monthly cost: {room.expenses:.2f}$\n"

        return result