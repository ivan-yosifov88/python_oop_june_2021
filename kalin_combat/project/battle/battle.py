from abc import ABC, abstractmethod


class Battle(ABC):

    @staticmethod
    @abstractmethod
    def battle(figure_1, figure_2):
        pass
