from project.medicine.medicine import Medicine


class Salve(Medicine):
    SALVE_VALUE = 50

    def __init__(self):
        Medicine.__init__(self, Salve.SALVE_VALUE)
