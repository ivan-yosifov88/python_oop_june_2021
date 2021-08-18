from project.figure.figure import Figure


class Triangle(Figure):
    def calculate_area(self):
        return self.args[0] * self.args[1] / 2

    def calculate_circumference(self):
        return self.args[0] + self.args[2] + self.args[3]


# print(Triangle("Triangle", 3, 4, 5, 6))
