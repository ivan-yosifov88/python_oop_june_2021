from project.battle.battle import Battle
from project.figure.figure import Figure


class CircumferenceBattle(Battle):

    @staticmethod
    def battle(figure_1: Figure, figure_2: Figure):
        if figure_2.calculate_circumference() == figure_1.calculate_circumference():
            return None
        return figure_1 if figure_1.calculate_circumference() > figure_2.calculate_circumference() else figure_2