from project.medicine.medicine import Medicine


class Salve(Medicine):
    value = 50

    def __init__(self):
        super().__init__(self.value)
