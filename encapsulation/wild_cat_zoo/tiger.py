from wild_cat_zoo.animal import Animal


class Tiger(Animal):
    MONEY_FOR_CARE_TIGER = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, money_for_care=Tiger.MONEY_FOR_CARE_TIGER)