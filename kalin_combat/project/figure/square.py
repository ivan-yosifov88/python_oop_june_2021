from project.figure.figure import Figure


class Square(Figure):

    def calculate_area(self):
        return self.args[0] ** 2

    def calculate_circumference(self):
        return self.args[0] * 4

# print(Square("test", 2))