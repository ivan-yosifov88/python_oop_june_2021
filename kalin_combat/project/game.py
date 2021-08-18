from project.battle.area_battle import AreaBattle
from project.battle.circumference_battle import CircumferenceBattle
from project.battle.relative_battle import RelativeBattle
from project.suitcase import Suitcase


class Game:
    def __init__(self):
        self.figures = Suitcase()

    def __repr__(self):
        return f"""
The winner is:
{str(self.total_battle())}
"""


    @staticmethod
    def area_battle(figure_1, figure_2):
        return AreaBattle().battle(figure_1, figure_2)

    @staticmethod
    def circumference_battle(figure_1,  figure_2):
        return CircumferenceBattle().battle(figure_1, figure_2)

    @staticmethod
    def relative_battle(figure_1,  figure_2):
        return RelativeBattle.battle(figure_1, figure_2)

    def total_battle(self):
        while len(self.figures.repository) > 1:

            figure_one = self.figures.repository.pop(0)
            figure_two = self.figures.repository.pop(0)
        first_combat = self.area_battle(figure_one, figure_two)
        second_combat = self.circumference_battle(figure_one, figure_two)
        combats = [first_combat, second_combat]

        if None * 2 in combats or (figure_one in combats and figure_two in combats):
            return self.relative_battle(figure_one, figure_two)

        if figure_one * 2 in combats:
            return figure_one
        if figure_two * 2 in combats:
            return figure_two


