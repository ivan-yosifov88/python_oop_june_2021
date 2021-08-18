from project.battle.battle import Battle
from project.figure.figure import Figure


class RelativeBattle(Battle):

    @staticmethod
    def battle(figure_1: Figure, figure_2: Figure):
        if figure_2.relativity() == figure_1.relativity():
            return None
        return figure_1 if figure_1.relativity() > figure_2.relativity() else figure_2