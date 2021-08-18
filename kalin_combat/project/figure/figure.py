from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def __str__(self):
        return f"Figure name: {self.name}\n" \
               f"Parameters:{', '.join(str(arg) for arg in self.args)}\n" \
               f"Area: {self.calculate_area()}\n" \
               f"Circumference: {self.calculate_circumference()}\n" \
               f"Relativity: {self.relativity()}"

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_circumference(self):
        pass

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, value):
        for arg in value:
            if arg < 0:
                raise ValueError("Negative number!")
        self.__args = value

    def relativity(self):
        return self.calculate_area() / self.calculate_circumference()
