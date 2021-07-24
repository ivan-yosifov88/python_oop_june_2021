from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    PAINKILLER_VALUE = 20

    def __init__(self):
        Medicine.__init__(self, Painkiller.PAINKILLER_VALUE)

