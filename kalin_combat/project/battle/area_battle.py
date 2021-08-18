from project.battle.battle import Battle
from project.figure.figure import Figure


class AreaBattle(Battle):

    @staticmethod
    def battle(figure_1: Figure, figure_2: Figure):
        if figure_1.calculate_area() == figure_2.calculate_area():
            return None
        return figure_1 if figure_1.calculate_area() > figure_2.calculate_area() else figure_2
