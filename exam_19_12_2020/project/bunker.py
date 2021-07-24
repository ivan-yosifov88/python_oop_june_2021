class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_list = []
        for supply in self.supplies:
            if type(supply).__name__ == "FoodSupply":
                food_list.append(supply)
        if not food_list:
            raise IndexError("There are no food supplies left!")
        return food_list

    @property
    def water(self):
        water_list = []
        for supply in self.supplies:
            if type(supply).__name__ == "WaterSupply":
                water_list.append(supply)
        if not water_list:
            raise IndexError("There are no water supplies left!")
        return water_list

    @property
    def painkillers(self):
        painkillers_list = []
        for medicine in self.medicine:
            if type(medicine).__name__ == "Painkiller":
                painkillers_list.append(medicine)
        if not painkillers_list:
            raise IndexError("There are no painkillers left!")
        return painkillers_list

    @property
    def salves(self):
        salves_list = []
        for medicine in self.medicine:
            if type(medicine).__name__ == "Painkiller":
                salves_list.append(medicine)
        if not salves_list:
            raise IndexError("There are no salves left!")
        return salves_list

    @staticmethod
    def get_reduced(age):
        return age * 2

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            for i in range(len(self.medicine) - 1, -1, -1):
                medicine = self.medicine[i]
                if type(medicine).__name__ == medicine_type:
                    medicine.apply(survivor)
                    self.medicine.pop(i)
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            for i in range(len(self.supplies) - 1, -1, -1):
                supply = self.supplies[i]
                if type(supply).__name__ == sustenance_type:
                    survivor.needs += supply.needs_increase
                    self.supplies.pop(i)
                    return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= self.get_reduced(survivor.age)
        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
            # if survivor.needs_sustenance:
            #     food_for_survivor = self.food[-1]
            #     self.supplies.remove(food_for_survivor)
            #     food_for_survivor.apply(survivor)
            # if survivor.needs_sustenance:
            #     water_for_survivor = self.water[-1]
            #     self.supplies.remove(water_for_survivor)
            #     water_for_survivor.apply(survivor)


