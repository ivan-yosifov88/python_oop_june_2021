from wild_cat_zoo.animal import Animal


class Cheetah(Animal):
    MONEY_FOR_CARE_CHEETAH = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, money_for_care=Cheetah.MONEY_FOR_CARE_CHEETAH)